+++
type = "question"
title = "LUA - how to filter duplicate TCP packets"
description = '''I stumbled across this thread: https://ask.wireshark.org/questions/38664/how-do-you-filter-for-duplicate-rtp-packets and blatantly copied the LUA script. My use case is to filter out duplicate TCP packets which are in the original trace due to SPAN from both sender and receiver. The SPAN cannot be c...'''
date = "2016-08-08T04:03:00Z"
lastmod = "2016-08-09T05:54:00Z"
weight = 54645
keywords = [ "duplicates", "lua" ]
aliases = [ "/questions/54645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LUA - how to filter duplicate TCP packets](/questions/54645/lua-how-to-filter-duplicate-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54645-score" class="post-score" title="current number of votes">0</div><span id="post-54645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I stumbled across this thread: <a href="https://ask.wireshark.org/questions/38664/how-do-you-filter-for-duplicate-rtp-packets">https://ask.wireshark.org/questions/38664/how-do-you-filter-for-duplicate-rtp-packets</a> and blatantly copied the LUA script.</p><p>My use case is to filter out duplicate TCP packets which are in the original trace due to SPAN from both sender and receiver. The SPAN cannot be changed since it captures continuously to a latency analysis engine so now I need to be able to filter the redundant traffic in order to do troubleshooting.</p><p>For this very specific use case I can filter on TCP sequence number, source and destination port and TCP stream index. Perhaps more must be added but this is not directly related to my question.</p><p>The script makes it possible to use a display filter such as "tcpdup.duplicate == true" which will show all TCP packets now identified as duplicate - and it works! :-)</p><p>However I would like to filter out half of these packets, so I see the <em>one</em> of the packets and in effect hide the duplicates. Naturally this is possible doing manual filtering on e.g. destination MAC address but this is not a uniform solution as it's very specific to one particular TCP session.</p><p>Is it possible to make this more general to simply filter out the 2nd packet and if so how?</p><p>I realize this is mostly down to scripting/coding knowledge which by now should be obvious is not one of my strong skills, so if you have any pointers or suggestions please don't hesitate :-)</p><p>Here's my script so far:</p><pre><code>-- our new Proto object
local tcpdup = Proto(&quot;tcpdup&quot;,&quot;TCP Duplicates Protocol&quot;)

-- new fields for our &quot;tcpdup&quot; protocol
-- the purpose for these is so they can be filtered upon
local pf_is_dup    = ProtoField.bool(&quot;tcpdup.duplicate&quot;, &quot;Duplicated&quot;)
local pf_dup_frame = ProtoField.framenum(&quot;tcpdup.frame&quot;, &quot;DupFrame&quot;, base.NONE)

-- register the ProtoFields above
tcpdup.fields = { pf_is_dup, pf_dup_frame }

-- some existing fields we need to extract from TCP packets, to determine duplicates
-- all of these must be the same for us to consider two packets duplicates
local f_ip_id    = Field.new(&quot;ip.id&quot;)
local f_tcp_seq  = Field.new(&quot;tcp.seq&quot;)
local f_tcp_srcport  = Field.new(&quot;tcp.srcport&quot;)
local f_tcp_dstport  = Field.new(&quot;tcp.dstport&quot;)
local f_tcp_stream = Field.new(&quot;tcp.stream&quot;)

-- the table we use to track seen packet #s and seen field info
-- we&#39;ll use this as both an array and map table
-- the array portion is indexed by packet number
-- the map portion is keyed by &quot;ip.id:tcp.seq:tcp.stream&quot;
-- the resultant for both is the same instance of a subtable with the
-- packet numbers of the dups in an array list
local packets = {}

local function generateKey(...)
    local t = { ... }
    return table.concat(t, &#39;:&#39;)
end

-- adds the packet&#39;s number to both the array and map
-- which is done when we see a particular set of fields for the first time
local function addPacketList(pnum, key)
    local list = { pnum }
    packets[key] = list
    packets[pnum] = list
end

-- adds the packet to the array part, using an existing list of dups
-- also adds the packet&#39;s number to the list of dups
local function addPacket(pnum, list)
    -- add this packet&#39;s number to the array portion of the big table
    packets[pnum] = list
    -- add this packet&#39;s number to the list of dups
    list[#list + 1] = pnum
end

-- whenever a new capture file is opened, we want to reset our table
-- so we hook into the init() routine to do that
function tcpdup.init()
    packets = {}
end

-- some forward &quot;declarations&quot; of helper functions we use in the dissector
local createProtoTree

-- our dissector function
function tcpdup.dissector(tvb, pinfo, tree)
    -- first, check if this is an tcp packet, by seeing if it has a tcp.seq
    local tcp_seq = select(1, f_tcp_seq())

    if not tcp_seq then
        -- not a TCP packet
        return
    end

    local pnum = pinfo.number

    -- see if we&#39;ve already processed this packet number
    local list = packets[pnum]

    if not list then
        -- haven&#39;t processed this packet
        -- see if the fields match another packet we&#39;ve seen before
        local ip_id = select(1, f_ip_id())
        local tcp_srcport = select(1, f_tcp_srcport())
        local tcp_dstport = select(1, f_tcp_dstport())
        local tcp_stream = select(1, f_tcp_stream())
        local key = generateKey(tostring(ip_id), tostring(tcp_seq), tostring(tcp_srcport), tostring(tcp_dstport), tostring(tcp_stream))

        list = packets[key]

        if not list then
            -- haven&#39;t seen these fields before, so add it as a non-dup (so far)
            addPacketList(pnum, key)
            createProtoTree(pnum, tree)
        else
            -- we haven&#39;t processed this packet, but we have seen the same fields
            -- so it&#39;s a duplicate.  Add its number to the array and entry...
            addPacket(pnum, list)
            -- and now create its tree
            createProtoTree(pnum, tree, list)
        end
    else
        -- we found the packet number already in the table, which means
        -- we&#39;ve processed it before
        createProtoTree(pnum, tree, list)
    end
end

createProtoTree = function (pnum, root, list)
    -- add our &quot;protocol&quot;
    local tree = root:add(tcpdup)

    if not list or #list &lt; 2 then
        -- it&#39;s not a duplicate
        tree:add(pf_is_dup, false):set_generated()
    else
        tree:add(pf_is_dup, true):set_generated()
        -- now add the other packet numbers as reference tree item fields
        for _, num in ipairs(list) do
            if num ~= pnum then
                tree:add(pf_dup_frame, num):set_generated()
            end
        end
    end
end

-- then we register tcpdup as a postdissector
register_postdissector(tcpdup)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicates" rel="tag" title="see questions tagged &#39;duplicates&#39;">duplicates</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/5a55fd7d0ca800a3b0724f350dbfec0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NJL&#39;s gravatar image" /><p><span>NJL</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NJL has no accepted answers">0%</span></p></div></div><div id="comments-container-54645" class="comments-container"><span id="54646"></span><div id="comment-54646" class="comment"><div id="post-54646-score" class="comment-score"></div><div class="comment-text"><p>just a question - have you tried to do get rid of the duplicates using <a href="https://sharkfest.wireshark.org/assets/presentations15/18.pptx">Super Deduper</a>?</p></div><div id="comment-54646-info" class="comment-info"><span class="comment-age">(08 Aug '16, 04:58)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="54649"></span><div id="comment-54649" class="comment"><div id="post-54649-score" class="comment-score"></div><div class="comment-text"><p>Or <a href="https://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> which comes with Wireshark?</p></div><div id="comment-54649-info" class="comment-info"><span class="comment-age">(08 Aug '16, 05:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="54661"></span><div id="comment-54661" class="comment"><div id="post-54661-score" class="comment-score"></div><div class="comment-text"><p>I tried editcap and used it initially to remove the vast majority of the duplicates. I should have stated that but forgot :-)</p><p>The duplicates that are left are from traffic that had to be routed (source and destination on different subnets on the same switch). They have different source and destination MAC addresses, hence editcap does not see them as duplicates even though everything else is identical.</p><p>I have not tried Super Deduper, I'll give that a try, however I could see this LUA script (if I can get it working the way I want) really useful for other use cases.</p><p>I've given it some more thought and I think what I need is "simply" a number of each duplicate packet. That way I should be able to use a display filter with e.g. "tcpdup.duplicate_packet_number == 1" which would then only display the 1st packet of all duplicates identified.</p><p>Any suggestions on how to do it or where to find more information is very welcome :-)</p></div><div id="comment-54661-info" class="comment-info"><span class="comment-age">(08 Aug '16, 07:03)</span> <span class="comment-user userinfo">NJL</span></div></div><span id="54675"></span><div id="comment-54675" class="comment"><div id="post-54675-score" class="comment-score"></div><div class="comment-text"><p>The point is that a dissector is not called just once per frame but several times - once when the file is loaded, and then at least each time you click a packet in the packet list. So you would have to extend the contents of the <code>list</code> with <code>frame.number</code> for each copy of the packet, compare the <code>frame.number</code> of the currently dissected packet with all the stored ones, and only mark as duplicates those whose <code>frame.number</code> would be higher than the lowest stored one. Or you could even assign order numbers 1 to N to each copy, assuming that for the first time, the frames would be dissected in the order they are read in, and that you would always calculate the order number to be assigned to the tree in that dissector run by finding its <code>frame.number</code> in the list.</p></div><div id="comment-54675-info" class="comment-info"><span class="comment-age">(08 Aug '16, 14:39)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-54645" class="comment-tools"></div><div class="clear"></div><div id="comment-54645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54700"></span>

<div id="answer-container-54700" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54700-score" class="post-score" title="current number of votes">0</div><span id="post-54700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the help.</p><p>A colleague of mine with more coding skills than me were kind enough to help.</p><p>That resulted in the dissector script below.</p><p>The script looks for packets which have the following identical fields: - IP ID - TCP sequence number - TCP source port - TCP destination port - TCP stream index</p><p>The new "TCP Duplicates Protocol" dissector identifies (just as the original) any duplicates by inserting a new boolean field called "Duplicated". If a duplicate exist the duplicate frame number is also inserted in a separate field called "DupFrame". Finally, the first frame of any duplicates are identified with another boolean field called "FirstSeen".</p><p>For my use case I can use a display filter like this "tcpdup.duplicate == false || tcpdup.firstseen == true"</p><p>This results in the dissector filtering out all the duplicates, while still showing the frames that were <em>not</em> duplicated.</p><p>I'm sure there are more ways to skin this cat, and most likely also more elegant ways, but for now this serves the purpose.</p><p>Hopefully someone else can get benefit from this dissector :-)</p><pre><code>-- our new Proto object
local tcpdup = Proto(&quot;tcpdup&quot;,&quot;TCP Duplicates Protocol&quot;)

-- new fields for our &quot;tcpdup&quot; protocol
-- the purpose for these is so they can be filtered upon
local pf_is_dup    = ProtoField.bool(&quot;tcpdup.duplicate&quot;, &quot;Duplicated&quot;)
local pf_dup_frame = ProtoField.framenum(&quot;tcpdup.frame&quot;, &quot;DupFrame&quot;, base.NONE)
local pf_dup_frame_firstseen = ProtoField.bool(&quot;tcpdup.firstseen&quot;, &quot;FirstSeen&quot;)

-- register the ProtoFields above
tcpdup.fields = { pf_is_dup, pf_dup_frame, pf_dup_frame_firstseen }

-- some existing fields we need to extract from TCP packets, to determine duplicates
-- all of these must be the same for us to consider two packets duplicates
local f_ip_id    = Field.new(&quot;ip.id&quot;)
local f_tcp_seq  = Field.new(&quot;tcp.seq&quot;)
local f_tcp_srcport  = Field.new(&quot;tcp.srcport&quot;)
local f_tcp_dstport  = Field.new(&quot;tcp.dstport&quot;)
local f_tcp_stream = Field.new(&quot;tcp.stream&quot;)

-- the table we use to track seen packet #s and seen field info
-- we&#39;ll use this as both an array and map table
-- the array portion is indexed by packet number
-- the map portion is keyed by &quot;ip.id:tcp.seq:tcp.stream&quot;
-- the resultant for both is the same instance of a subtable with the
-- packet numbers of the dups in an array list
local packets = {}

local function generateKey(...)
    local t = { ... }
    return table.concat(t, &#39;:&#39;)
end

-- adds the packet&#39;s number to both the array and map
-- which is done when we see a particular set of fields for the first time
local function addPacketList(pnum, key)
    local list = { pnum }
    packets[key] = list
    packets[pnum] = list
end

-- adds the packet to the array part, using an existing list of dups
-- also adds the packet&#39;s number to the list of dups
local function addPacket(pnum, list)
    -- add this packet&#39;s number to the array portion of the big table
    packets[pnum] = list
    -- add this packet&#39;s number to the list of dups
    list[#list + 1] = pnum
end

-- whenever a new capture file is opened, we want to reset our table
-- so we hook into the init() routine to do that
function tcpdup.init()
    packets = {}
end

-- some forward &quot;declarations&quot; of helper functions we use in the dissector
local createProtoTree

-- our dissector function
function tcpdup.dissector(tvb, pinfo, tree)
    -- first, check if this is an tcp packet, by seeing if it has a tcp.seq
    local tcp_seq = select(1, f_tcp_seq())

    if not tcp_seq then
        -- not a TCP packet
        return
    end

    local pnum = pinfo.number

    -- see if we&#39;ve already processed this packet number
    local list = packets[pnum]

    if not list then
        -- haven&#39;t processed this packet
        -- see if the fields match another packet we&#39;ve seen before
        local ip_id = select(1, f_ip_id())
        local tcp_seq = select(1, f_tcp_seq())
        local tcp_srcport = select(1, f_tcp_srcport())
        local tcp_dstport = select(1, f_tcp_dstport())
        local tcp_stream = select(1, f_tcp_stream())
        local key = generateKey(tostring(ip_id), tostring(tcp_seq), tostring(tcp_srcport), tostring(tcp_dstport), tostring(tcp_stream))

        list = packets[key]

        if not list then
            -- haven&#39;t seen these fields before, so add it as a non-dup (so far)
            addPacketList(pnum, key)
            createProtoTree(pnum, tree)
        else
            -- we haven&#39;t processed this packet, but we have seen the same fields
            -- so it&#39;s a duplicate.  Add its number to the array and entry...
            addPacket(pnum, list)
            -- and now create its tree
            createProtoTree(pnum, tree, list)
        end
    else
        -- we found the packet number already in the table, which means
        -- we&#39;ve processed it before
        createProtoTree(pnum, tree, list)
    end
end

createProtoTree = function (pnum, root, list)
    -- add our &quot;protocol&quot;
    local tree = root:add(tcpdup)
    local number_of_packets
    number_of_packets=1
    if not list or #list &lt; 2 then
        -- it&#39;s not a duplicate
        tree:add(pf_is_dup, false):set_generated()
    else
        tree:add(pf_is_dup, true):set_generated()
        -- now add the other packet numbers as reference tree item fields
        for _, num in ipairs(list) do
            if num &lt; pnum then
                tree:add(pf_dup_frame, num):set_generated()
                                tree:add(pf_dup_frame_firstseen,false):set_generated()
                end
            if num &gt; pnum then
                tree:add(pf_dup_frame, num):set_generated()
                                tree:add(pf_dup_frame_firstseen,true):set_generated()
            end
        end
    end
end

-- then we register tcpdup as a postdissector
register_postdissector(tcpdup)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/5a55fd7d0ca800a3b0724f350dbfec0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NJL&#39;s gravatar image" /><p><span>NJL</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NJL has no accepted answers">0%</span></p></div></div><div id="comments-container-54700" class="comments-container"></div><div id="comment-tools-54700" class="comment-tools"></div><div class="clear"></div><div id="comment-54700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

