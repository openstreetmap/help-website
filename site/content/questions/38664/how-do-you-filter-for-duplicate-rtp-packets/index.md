+++
type = "question"
title = "How do you filter for duplicate RTP packets?"
description = '''Can anyone identify a way to filter Duplicate RTP packets in WS? We are sniffing RTP packets on a workstation which are coming from a Cisco Cube and compiling them into an ASF file for Call Recording Evaluation purposes. The duplciate packets are causing problems for us and our network team is askin...'''
date = "2014-12-22T12:43:00Z"
lastmod = "2014-12-23T00:39:00Z"
weight = 38664
keywords = [ "filter", "duplicate", "packets", "rtp" ]
aliases = [ "/questions/38664" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you filter for duplicate RTP packets?](/questions/38664/how-do-you-filter-for-duplicate-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone identify a way to filter Duplicate RTP packets in WS? We are sniffing RTP packets on a workstation which are coming from a Cisco Cube and compiling them into an ASF file for Call Recording Evaluation purposes. The duplciate packets are causing problems for us and our network team is asking for evidence.<br />
</p><p>It took a lot of time to identify it in one of the WS captures but we showed the duplicate packet to them. The network and telephony teams now want numerous examples and we cannot find an easy way to identify duplicate RTP packets in the WS captures, only TCP. Ideas would be greatly appreciated.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">filter duplicate packets rtp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/89f1389ec8304aa31a394d2dda517861?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swaisboy&#39;s gravatar image" /><p>swaisboy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swaisboy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-38664" class="comments-container"></div><div id="comment-tools-38664" class="comment-tools"></div><div class="clear"></div><div id="comment-38664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38668"></span>

<div id="answer-container-38668" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38668-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicate IP ID field values in the IP header would be one clear indicator of a duplicate packet. The system generating the initial IP packet typically increments that field with each successive packet, and no router should every modify it, so if you see two packets with the same IP ID field and the same content, that's a really strong indicator of a duplicate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '14, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '14, 15:40</p></div></div><div id="comments-container-38668" class="comments-container"><span id="38669"></span><div id="comment-38669" class="comment"><div id="post-38669-score" class="comment-score"></div><div class="comment-text"><p>Thanks Quadratic. We are able to identify the duplicate packets as you indicated above using similar methods, but we need help trying to Filter for all Duplicate RTP packets. There is a ton of data to parse through. We see there is a way to do that with TCP, but have not found a way to Filter specificlaly duplciate RTP packets. Thanks.</p></div><div id="comment-38669-info" class="comment-info"><span class="comment-age">(22 Dec '14, 16:10)</span> swaisboy</div></div><span id="38671"></span><div id="comment-38671" class="comment"><div id="post-38671-score" class="comment-score"></div><div class="comment-text"><p>One method is simply to use editcap to filter them out. The '-d' option of editcap should do it if the duplicates are close together and truly identical (uses MD5 hash comparison to detect them):</p><p><a href="https://www.wireshark.org/docs/man-pages/editcap.html">https://www.wireshark.org/docs/man-pages/editcap.html</a></p><p>In that example: editcap -d capture.pcap capture_without_duplicates.pcap</p></div><div id="comment-38671-info" class="comment-info"><span class="comment-age">(22 Dec '14, 19:28)</span> Quadratic</div></div></div><div id="comment-tools-38668" class="comment-tools"></div><div class="clear"></div><div id="comment-38668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38672"></span>

<div id="answer-container-38672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use a Lua script to do it.</p><p>For example the script below will create a fake "rtpdup" protocol for RTP packets, and set a new field called "rtpdup.duplicate" to true if it's a duplicate. That way you can filter on that field's value in Wireshark.</p><p>So just copy paste the below code into a new file with a <code>.lua</code> extension (e.g., "<code>rtpdup.lua</code>"), and put it in your Wireshark personal plugins directory; and then start Wireshark, load up your capture file, and use the display filter "<code>rtpdup.duplicate == true</code>", and voilà you'll only see duplicate RTP packets. This script uses the combination of IP ID field, RTP sequence number, and RTP SSRC field... all three must match for another packet to be considered a duplicate. (or you can reduce it by changing the Lua code... it's fairly straightforward)</p><hr /><pre><code>-- our new Proto object
local rtpdup = Proto(&quot;rtpdup&quot;,&quot;RTP Duplicates Protocol&quot;)

-- new fields for our &quot;rtpdup&quot; protocol
-- the purpose for these is so they can be filtered upon
local pf_is_dup    = ProtoField.bool(&quot;rtpdup.duplicate&quot;, &quot;Duplicated&quot;)
local pf_dup_frame = ProtoField.framenum(&quot;rtpdup.frame&quot;, &quot;DupFrame&quot;, base.NONE)

-- register the ProtoFields above
rtpdup.fields = { pf_is_dup, pf_dup_frame }

-- some existing fields we need to extract from RTP packets, to determine duplicates
-- all 3 of these must be the same for us to consider two packets duplicates
local f_ip_id    = Field.new(&quot;ip.id&quot;)
local f_rtp_seq  = Field.new(&quot;rtp.seq&quot;)
local f_rtp_ssrc = Field.new(&quot;rtp.ssrc&quot;)

-- the table we use to track seen packet #s and seen field info
-- we&#39;ll use this as both an array and map table
-- the array portion is indexed by packet number
-- the map portion is keyed by &quot;ip.id:rtp.seq:rtp.ssrc&quot;
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
function rtpdup.init()
    packets = {}
end

-- some forward &quot;declarations&quot; of helper functions we use in the dissector
local createProtoTree

-- our dissector function
function rtpdup.dissector(tvb, pinfo, tree)
    -- first, check if this is an rtp packet, by seeing if it has a rtp.seq
    local rtp_seq = select(1, f_rtp_seq())

    if not rtp_seq then
        -- not an RTP packet
        return
    end

    local pnum = pinfo.number

    -- see if we&#39;ve already processed this packet number
    local list = packets[pnum]

    if not list then
        -- haven&#39;t processed this packet
        -- see if the fields match another packet we&#39;ve seen before
        local ip_id = select(1, f_ip_id())
        local rtp_ssrc = select(1, f_rtp_ssrc())
        local key = generateKey(tostring(ip_id), tostring(rtp_seq), tostring(rtp_ssrc))

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
    local tree = root:add(rtpdup)

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

-- then we register rtpdup as a postdissector
register_postdissector(rtpdup)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-38672" class="comments-container"></div><div id="comment-tools-38672" class="comment-tools"></div><div class="clear"></div><div id="comment-38672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

