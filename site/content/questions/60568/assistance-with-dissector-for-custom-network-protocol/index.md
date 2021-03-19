+++
type = "question"
title = "Assistance with dissector for custom network protocol"
description = '''Hello, At my job we regularly use switches which got a proprietary ring redundancy protocol. In order to make our job easier, I am trying to make a dissector so wireshark correctly shows information instead of showing &#x27;llc&#x27; as it currently does. I looked up multiple tutorials, but so far almost all ...'''
date = "2017-04-04T08:10:00Z"
lastmod = "2017-04-05T02:13:00Z"
weight = 60568
keywords = [ "llc", "ethernet", "dissector" ]
aliases = [ "/questions/60568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Assistance with dissector for custom network protocol](/questions/60568/assistance-with-dissector-for-custom-network-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60568-score" class="post-score" title="current number of votes">0</div><span id="post-60568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>At my job we regularly use switches which got a proprietary ring redundancy protocol. In order to make our job easier, I am trying to make a dissector so wireshark correctly shows information instead of showing 'llc' as it currently does.</p><p>I looked up multiple tutorials, but so far almost all of those I found talk about connecting to a specific UDP or TCP port while what I intend to do hooks directly on the MAC/ethernet level.</p><p>I know for sure that the lua gets loaded, as writing an error or invalid action causes a crash. I tried multiple ways of getting wireshark to translate as my protocol instead of LLC, but I got no success so far. If anyone can give me a hint or a source where I can find the answer myself I would appreciate it!</p><p>wireshark trace of a few packets of the protocol: <a href="https://drive.google.com/file/d/0B9vmLCalgzm1NC1KUzNqRENFY1E/view?usp=sharing">https://drive.google.com/file/d/0B9vmLCalgzm1NC1KUzNqRENFY1E/view?usp=sharing</a></p><p>image for those who rather don't download files from unknown sources: <img src="https://osqa-ask.wireshark.org/upfiles/rgerp.PNG" alt="alt text" /></p><p>My current code attempt:</p><pre><code>    original_802_3_dissector = DissectorTable.get( &quot;wtap_encap&quot; ):get_dissector( 1 )

protoRGERP = Proto(&quot;RGERP&quot;, &quot;Redundant Gigabit Ethernet Ring Protocol&quot;)

local f = protoRGERP.fields
local vs_state = {[0]=&quot;normal&quot;,[1]=&quot;abnormal&quot;}

f.ringId = ProtoField.uint16(&quot;protoRGERP.ringId&quot;, &quot;Ring ID&quot;)
f.ringState = ProtoField.bool(&quot;protoRGERP.ringState&quot;, &quot;Ring Status&quot;)
f.ringMaster = ProtoField.ether(&quot;protoRGERP.ringMaster&quot;,&quot;Ring Master&quot;)
f.ringData = ProtoField.bytes (&quot;protoRGERP.ringData&quot;,&quot;Data&quot;)
--f.ringInfo = ProtoField.string(&quot;protoRGERP.ringInfo&quot;,&quot;Ring Info&quot;)

local packet_counter
function protoRGERP.init()
    packet_counter = 0
end

function protoRGERP.dissector(buffer, pinfo, tree)
    --run default ethernet dissector
    original_802_3_dissector:call(buffer,pinfo,tree)
    --tree additions
    local subtree = tree:add(protoRGERP, buffer())
    local offset=12
    local ringId = buffer(offset,1)
    subtree:add (f.ringId, ringId)
    subtree:append_text(&quot;, Ring ID: &quot;..ringId:uint())
    offset=offset+1

    local ringState = buffer(offset,1)
    subtree:add(f.ringState, ringState)
    subtree:append_text(&quot;, Ring normal : &quot;..ringState:bool())
    offset=offset+1

    local ringMaster = buffer(offset,6)
    subtree:add(f.ringMaster, ringMaster)
    subtree:append_text(&quot;, RM MAC: &quot;..ringMaster:ether())
    offset=offset+6

    subtree:add( f.ringData, buffer(offset))

    -- modify columns; to be extended
    pinfo.cols[&#39;protocol&#39;] = &quot;RGERP&quot;
    pinfo.cols.info = &quot;RGERP ID: &quot;
    pinfo.cols.info:append(ringId:uint())

end

--local wtap_encap_table = DissectorTable.get(&quot;wtap_encap&quot;)
--wtap_encap_table:add(0x1a, protoRGERP)
--below causes wireshark to crash
--local llc_table = DissectorTable.get(&quot;llc.dsap&quot;)
--llc_table:add(0x6b, protoRGERP)
local dissector_table2 = DissectorTable.get(&quot;ethertype&quot;)
dissector_table2:add(0x1a,protoRGERP)
local dissector_table3 = DissectorTable.get(&quot;wtap_encap&quot;)
dissector_table3:add(wtap.USER0, protoRGERP)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '17, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/f328cb5777099d25c9aeaa2e8dc95654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikdubois&#39;s gravatar image" /><p><span>nikdubois</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikdubois has one accepted answer">100%</span></p></img></div></div><div id="comments-container-60568" class="comments-container"><span id="60569"></span><div id="comment-60569" class="comment"><div id="post-60569-score" class="comment-score"></div><div class="comment-text"><p>minor update: with replacing ethernet I can get it working, but I can't get the if structure working to run the original ethernet dissector if mine isn't needed. A way to do this might be a good workaround if anyone knows how/if this is possible!</p><p>this is how I replaced the dissector:</p><pre><code>original_802_3_dissector = DissectorTable.get( &quot;wtap_encap&quot; ):get_dissector( 1 )
local dissector_table3 = DissectorTable.get(&quot;wtap_encap&quot;)
dissector_table3:add(1, protoRGERP)</code></pre><p>and then I wrapped my code in the proto.dissector in an if:</p><pre><code>function protoRGERP.dissector(buffer, pinfo, tree)
    if buffer(0xE,4):string()~=&#39;6b726e78&#39; then
       ~code~
    else
        original_802_3_dissector:call(buffer,pinfo,tree)
    end
end</code></pre><p>But this causes 'wireshark has stopped responding'. I couldn't find an error in a log yet.</p></div><div id="comment-60569-info" class="comment-info"><span class="comment-age">(04 Apr '17, 08:48)</span> <span class="comment-user userinfo">nikdubois</span></div></div><span id="60573"></span><div id="comment-60573" class="comment"><div id="post-60573-score" class="comment-score">1</div><div class="comment-text"><p>So does this protocol run atop Ethernet?</p><p>If so, does it:</p><ol><li>have an Ethernet type value assigned to it;</li><li>have an 802.2 DSAP assigned to it;</li><li>have a SNAP OUI and protocol ID assigned to it;</li><li>violate the Ethernet spec?</li></ol><p>(<em>All</em> protocols that run atop Ethernet do one of those four things; i.e., if they don't have one of those values assigned to them, they're violating the Ethernet spec.)</p></div><div id="comment-60573-info" class="comment-info"><span class="comment-age">(04 Apr '17, 18:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="60578"></span><div id="comment-60578" class="comment"><div id="post-60578-score" class="comment-score"></div><div class="comment-text"><p>I fear it is the last. I will raise the issue with the manufacturer, but I don't think this can/will be changed by them anytime soon.</p><p>My guess is that I will have to do the workaround using a chained dissector (my own into the ethernet if it is not my own protocol). So far this always crashes for me though, so if you have a working example using the ethernet dissector I would appreciate it!</p></div><div id="comment-60578-info" class="comment-info"><span class="comment-age">(05 Apr '17, 00:15)</span> <span class="comment-user userinfo">nikdubois</span></div></div></div><div id="comment-tools-60568" class="comment-tools"></div><div class="clear"></div><div id="comment-60568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60583"></span>

<div id="answer-container-60583" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60583-score" class="post-score" title="current number of votes">0</div><span id="post-60583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nikdubois has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I managed to get it working eventually, but make sure to read the comment of Guy Harris as he is right. What I used below is an ugly way to get around it and there are better solutions. Just posting this so others in a similar situation can get a workaround untill they fix it.</p><pre><code>protoRGERP = Proto(&quot;RGERP&quot;, &quot;RGERP&quot;, &quot;Redundant Gigabit Ethernet Ring Protocol&quot;)

local f = protoRGERP.fields
local vs_ringState = {[0]=&quot;normal&quot;,[1]=&quot;abnormal&quot;}
local vs_portState = {[0]=&quot;up&quot;,[1]=&quot;down&quot;}

--f.packetSource = ProtoField.ether(&quot;protoRGERP.packetSource&quot;,&quot;Source&quot;)
--f.packetDest = ProtoField.ether(&quot;protoRGERP.packetSource&quot;,&quot;Destination&quot;)
f.packetType = ProtoField.string(&quot;protoRGERP.packetType&quot;,&quot;LLC Type&quot;)
f.ringId = ProtoField.uint16(&quot;protoRGERP.ringId&quot;, &quot;Ring ID&quot;)
f.ringState = ProtoField.uint16(&quot;protoRGERP.ringState&quot;, &quot;Ring State&quot;)
f.ringMaster = ProtoField.ether(&quot;protoRGERP.ringMaster&quot;,&quot;Ring Master&quot;)

f.portState = ProtoField.uint16(&quot;protoRGERP.portState&quot;, &quot;Port State&quot;)
f.portId = ProtoField.uint16(&quot;protoRGERP.portId&quot;, &quot;Port ID&quot;)
f.packetSender = ProtoField.ether(&quot;protoRGERP.packetSender&quot;,&quot;Packet Sender&quot;)

local packet_counter
function protoRGERP.init()
    packet_counter = 0
end

function protoRGERP.dissector(buffer, pinfo, tree)
    local subtree = tree:add(protoRGERP, buffer())

    --tree additions
    local packetType
    if string.sub(tostring(pinfo.cols.src),-1)==&#39;2&#39; then
        packetType=&quot;LINK_CHANGE_DOWN&quot;
    elseif string.sub(tostring(pinfo.cols.dst),-1)==&#39;3&#39; then
        packetType=&quot;LINK_CHANGE_UP&quot;
    else
        packetType=&quot;WATCHDOG&quot;
    end
    subtree:add(f.packetType, packetType)

    local offset=0
    if packetType==&quot;WATCHDOG&quot; then
        local ringId = buffer(offset,1)
        subtree:add (f.ringId, ringId)
        offset=offset+1

        local ringState = buffer(offset,1)
        subtree:add(f.ringState, ringState)
        offset=offset+1

        local ringMaster = buffer(offset,6)
        subtree:add(f.ringMaster, ringMaster)
        offset=offset+6

        -- modify columns; replace LLC with custom
        pinfo.cols[&#39;protocol&#39;] = &quot;RGERP&quot;
        pinfo.cols.info = &quot;Ring ID: &quot;
        pinfo.cols.info:append(ringId:uint())
        pinfo.cols.info:append(&quot;, ring status: &quot;)
        pinfo.cols.info:append(vs_ringState[ringState:uint()])
        pinfo.cols.info:append(&quot;, packet type: &quot;..packetType)
    else
        --linkchange
        local portState = buffer(offset,1)
        subtree:add (f.portState, portState)
        offset = offset+1

        local portId = buffer(offset,1)
        subtree:add (f.portId, portId)
        offset = offset+1

        local packetSender = buffer(offset,6)
        subtree:add (f.packetSender, packetSender)
        offset = offset+1

        local ringId = buffer(offset,1)
        subtree:add (f.ringId, ringId)
        offset=offset+1

        pinfo.cols[&#39;protocol&#39;] = &quot;RGERP&quot;
        pinfo.cols.info = &quot;Ring ID: &quot;
        pinfo.cols.info:append(ringId:uint())
        pinfo.cols.info:append(&quot;, port ID: &quot;..portId:uint()..&quot; is &quot;)
        pinfo.cols.info:append(vs_portState[portState:uint()])
        pinfo.cols.info:append(&quot;, packet type: &quot;..packetType)        
    end
end

local llc_table = DissectorTable.get(&quot;llc.dsap&quot;)
llc_table:add(0x6b, protoRGERP)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '17, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/f328cb5777099d25c9aeaa2e8dc95654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikdubois&#39;s gravatar image" /><p><span>nikdubois</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikdubois has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Apr '17, 02:15</strong> </span></p></div></div><div id="comments-container-60583" class="comments-container"></div><div id="comment-tools-60583" class="comment-tools"></div><div class="clear"></div><div id="comment-60583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

