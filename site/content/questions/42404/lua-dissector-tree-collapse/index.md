+++
type = "question"
title = "LUA Dissector tree collapse"
description = '''Hi all, I&#x27;m pretty new about the LUA Dissector. I have a problem with my code.  Every time that I expand the treelist all subtrees are expanded automatically.  How can I avoid this? Also, I&#x27;d like to ask you why the subtrees are displayed in grey color instead of white. Below you will find my code. ...'''
date = "2015-05-14T15:26:00Z"
lastmod = "2015-06-29T08:47:00Z"
weight = 42404
keywords = [ "lua", "dissector", "tree" ]
aliases = [ "/questions/42404" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [LUA Dissector tree collapse](/questions/42404/lua-dissector-tree-collapse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42404-score" class="post-score" title="current number of votes">0</div><span id="post-42404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm pretty new about the LUA Dissector. I have a problem with my code. Every time that I expand the treelist all subtrees are expanded automatically. How can I avoid this? Also, I'd like to ask you why the subtrees are displayed in grey color instead of white.</p><p>Below you will find my code. Thank you in advance for the help</p><p>Peter.</p><pre><code>-- New Protocol and  fields
p_mynewproto  = Proto (&quot;MyProtocol&quot;, &quot;Test&quot;)

-- Define Header fields
local protoHeader = p_mynewproto.fields
protoHeader.rxId        = ProtoField.uint16(&#39;protoHeader.rxId&#39;      , &#39;Rx ID &#39; , base.HEX, nil)
protoHeader.txId        = ProtoField.uint16(&#39;protoHeader.txId&#39;      , &#39;Tx ID &#39; , base.HEX, nil)
protoHeader.timeHour    = ProtoField.uint16(&#39;protoHeader.timeHour&#39;  , &#39;Hour  &#39; , base.HEX, nil)
protoHeader.timeMinute  = ProtoField.uint16(&#39;protoHeader.timeMinute&#39;, &#39;Minute&#39; , base.HEX, nil)
protoHeader.timeSecond  = ProtoField.uint16(&#39;protoHeader.timeSecond&#39;, &#39;Second&#39; , base.HEX, nil)

-- mynewproto dissector function
function p_mynewproto.dissector (buf, pkt, root)

   -- Check the packet length
   if buf:len() == 0 then return end
   pkt.cols.protocol = p_mynewproto.name

   -- start from offset 0
   local offset = 0

   -- create subtree for mynewproto
   subtreeA = root:add(p_mynewproto, buf(offset,buf:len())):append_text(&quot; [My Protocol Header]&quot;)

   -- Rx ID
   subtreeA:add(protoHeader.rxId , buf(offset,2))

   -- Tx ID
   subtreeA:add(protoHeader.txId , buf(offset+2,2))

   -- Time
   subtreeB = subtreeA:add(p_mynewproto, buf(offset+4,6),&quot;[TIME]&quot;)

   -- Time Hour
   subtreeB:add(protoHeader.timeHour , buf(offset+4,2))

   -- Time Minute
   subtreeB:add(protoHeader.timeMinute , buf(offset+6,2))

   -- Time Second
   subtreeB:add(protoHeader.timeSecond , buf(offset+8,2))
 end

-- Initialization function
function p_mynewproto.init()
end

-- Register a chained dissector for port 11111
local udp_dissector_table = DissectorTable.get(&quot;udp.port&quot;)
dissector = udp_dissector_table:get_dissector(11111)
udp_dissector_table:add(11111, p_mynewproto)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/70525b9d7b57a3138db49a82ffc66974?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter1969&#39;s gravatar image" /><p><span>Peter1969</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter1969 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '15, 18:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-42404" class="comments-container"><span id="42462"></span><div id="comment-42462" class="comment"><div id="post-42462-score" class="comment-score"></div><div class="comment-text"><p>Guys, I found this old wireshark question: <a href="https://ask.wireshark.org/questions/31356/how-to-get-all-tree-items-collapsed-as-default-in-gtk-version">https://ask.wireshark.org/questions/31356/how-to-get-all-tree-items-collapsed-as-default-in-gtk-version</a></p><p>But I don't understand very well the response. How can I adapt it to my code. Thank you Peter.</p></div><div id="comment-42462-info" class="comment-info"><span class="comment-age">(17 May '15, 07:51)</span> <span class="comment-user userinfo">Peter1969</span></div></div></div><div id="comment-tools-42404" class="comment-tools"></div><div class="clear"></div><div id="comment-42404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43617"></span>

<div id="answer-container-43617" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43617-score" class="post-score" title="current number of votes">1</div><span id="post-43617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Peter1969 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your example code above, the sub-tree you're adding is done with this:</p><pre><code>subtreeB = subtreeA:add(p_mynewproto, buf(offset+4,6),&quot;[TIME]&quot;)</code></pre><p>That tells Wireshark to add a child item to <code>subtreeA</code> (which you created earlier), and the thing you're telling wireshark to add is <code>p_mynewproto</code>. But <code>p_mynewproto</code> represents a Protocol (a <code>Proto</code> object), and it's exactly the same protocol that you added when you created subtreeA earlier - so when you expand the tree in the GUI for subtreeA, Wireshark will automatically expand the tree for subtreeB, because they're the same protocol, and thus the same internal tree-type. Also that's why it's gray and not white - because it's a tree item for a Protocol rather than a ProtoField of a protocol. All protocol tree items are colored gray.</p><p>What you should be doing instead is creating another <code>ProtoField</code> for a "Time" field - this won't be a distinct field like the others, but rather just something to hold/contain/encapsulate the other time fields. For example by going this:</p><pre><code>-- this is with your other ProtoField definitions:
protoHeader.time = ProtoField.bytes(&#39;protoHeader.time&#39;, &#39;Time&#39;)
-- this is inside your dissector:
subtreeB = subtreeA:add(protoHeader.time, buf(offset+4,6))
-- or this if you don&#39;t want to see the bytes shown:
subtreeB = subtreeA:add(protoHeader.time, buf(offset+4,6)):set_text(&#39;Time&#39;)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43617" class="comments-container"><span id="43666"></span><div id="comment-43666" class="comment"><div id="post-43666-score" class="comment-score"></div><div class="comment-text"><p>Thank you Hadriel, I really appreciate your help.</p><p>Regards,</p><p>Peter</p></div><div id="comment-43666-info" class="comment-info"><span class="comment-age">(29 Jun '15, 08:11)</span> <span class="comment-user userinfo">Peter1969</span></div></div><span id="43668"></span><div id="comment-43668" class="comment"><div id="post-43668-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-43668-info" class="comment-info"><span class="comment-age">(29 Jun '15, 08:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43617" class="comment-tools"></div><div class="clear"></div><div id="comment-43617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

