+++
type = "question"
title = "Filtering by fields generated in lua"
description = '''I&#x27;m parsing some payloads in IEEE 802.15.4. The structure of the payloads is that the first byte indicates the data type. I would like to be able to filter by payload type. I seem to be able to create the filter for my dissector that is visible in the &quot;Display Filter Expressions&quot; dialog, but wheneve...'''
date = "2017-02-23T17:48:00Z"
lastmod = "2017-02-24T14:02:00Z"
weight = 59650
keywords = [ "lua", "protofield", "fields" ]
aliases = [ "/questions/59650" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filtering by fields generated in lua](/questions/59650/filtering-by-fields-generated-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59650-score" class="post-score" title="current number of votes">0</div><span id="post-59650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm parsing some payloads in IEEE 802.15.4. The structure of the payloads is that the first byte indicates the data type. I would like to be able to filter by payload type. I seem to be able to create the filter for my dissector that is visible in the "Display Filter Expressions" dialog, but whenever I try to filter by the value it always filter out every one of my packets regardless of how I define my filter, such as type!=123 when I know that I have many times other than 123. Also simply entering type in the filter window filter out all my packets. I've tried a bunch of ways to try and set the type filed and no joy. Would appreciate any pointers. Here is the code:</p><pre><code>-- MyProto protocol
-- declare our protocol
MyProto = Proto(&quot;MyProto&quot;,&quot;MyProto Protocol&quot;)
-- Create the protocol fields
local f_type = ProtoField.uint8(&quot;type&quot;, &quot;Type&quot;, base.HEX, proxyClientMsgType_t, 0, &quot;MyProto Packet Type&quot; )
MyProto.fields = { f_type }

-- create a function to dissect it
function MyProto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = MyProto.name
    --local subtree = tree:add(MyProto,buffer(),&quot;MyProto Protocol Data&quot;)

    local PacketType = buffer(0,1):uint()
    MyProto.fields.type = 2

   MyProto.fields.f_type = PacketType      --does not seem to help with filter
   f_type = PacketType                     --does not seem to help with filter

    --MyProtoType
    local subtree = tree:add(MyProto.fields.f_type , buffer(), &quot;MyProto - &quot; .. proxyClientMsgType_t[PacketType]:sub(13)  .. &quot; - &quot; .. PacketType .. &quot; - &lt;&lt;&quot;  ..   buffer(0,pktlen-1) .. &quot;&gt;&gt;&quot;) )
    subtree:add(&quot;Packet Type: &quot; .. PacketType .. &quot; - &quot;.. MsgType_t[PacketType] .. &quot; - &quot; ..  MsgTypeDetailed_t[PacketType], buffer (0,1) )
end

-- load the wpan table
wpan_table = DissectorTable.get(&quot;wpan.panid&quot;)
-- register our protocol to handle udp port 7777
wpan_table:add(104,MyProto )
wpan_table:add(127, MyProto )</code></pre><p>As a bonus question, I seem to behaving difficulty getting the sub trees of my packet byte pane to highlight subsections of the payload bytes. How to I do that tied together?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-protofield" rel="tag" title="see questions tagged &#39;protofield&#39;">protofield</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '17, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/b4b7f09942345d067d2c40d60da675cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MountainLogic&#39;s gravatar image" /><p><span>MountainLogic</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MountainLogic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '17, 11:48</strong> </span></p></div></div><div id="comments-container-59650" class="comments-container"></div><div id="comment-tools-59650" class="comment-tools"></div><div class="clear"></div><div id="comment-59650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59669"></span>

<div id="answer-container-59669" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59669-score" class="post-score" title="current number of votes">1</div><span id="post-59669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MountainLogic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>wpan_table:add(104,cota)
wpan_table:add(127, cota)</code></pre><p>What is <code>cota</code>? For starters, I don't think your dissector is being registered properly and thus it's probably not ever being called. Maybe start with a smaller, simpler dissector first and build from there, for example:</p><pre><code>-- Protocol
local p_myproto = Proto(&quot;MyProto&quot;, &quot;MyProto Protocol&quot;)

-- Fields
local f_myproto_type = ProtoField.uint8(&quot;myproto.type&quot;, &quot;Type&quot;, base.HEX)
p_myproto.fields = { f_myproto_type }

-- Dissection
function p_myproto.dissector(buffer, pinfo, tree)
    local myproto_tree = tree:add(p_myproto, buffer(0,-1))

    pinfo.cols.protocol:set(&quot;MYProto&quot;)
    myproto_tree:add(f_myproto_type, buffer(0, 1))
end

-- Registration
local wpan_table = DissectorTable.get(&quot;wpan.panid&quot;)
wpan_table:add(104, p_myproto)
wpan_table:add(127, p_myproto)</code></pre><p>See if that gets you any further?</p><p>There are also many Lua examples available on the wiki that should help you. See my answer to <a href="https://ask.wireshark.org/questions/53802/how-dissect-two-segments-of-one-protocol-in-the-same-packet-in-the-same-tcp-segment-lua">this</a> question for a list of some. I also provided a simple Lua example in a comment I made to <a href="https://ask.wireshark.org/questions/23519/ipv6-dissecting-throws-lua-ft-not-yet-supported-error-why">this other question</a>, along with a link to a capture file hosted at cloudshark, which may or may not be useful to you as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59669" class="comments-container"><span id="59674"></span><div id="comment-59674" class="comment"><div id="post-59674-score" class="comment-score"></div><div class="comment-text"><p>Christopher , great answer. Works like a charm and I it has really helped. Yes, I had tried to change variable name to something a bit more general and in the original it did get called just fine. I've edited my code in the the question so I believe you can delete everything up to "Maybe" in your answer. Thanks --scott</p></div><div id="comment-59674-info" class="comment-info"><span class="comment-age">(24 Feb '17, 14:02)</span> <span class="comment-user userinfo">MountainLogic</span></div></div></div><div id="comment-tools-59669" class="comment-tools"></div><div class="clear"></div><div id="comment-59669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

