+++
type = "question"
title = "Link Layer Protocol ?"
description = '''If I look at a packet, how can I tell what the link-layer protocol is? Where is it shown in wireshark?? Many thanks.. Sorry if this is an obvious question.'''
date = "2012-12-14T11:41:00Z"
lastmod = "2012-12-14T12:52:00Z"
weight = 16910
keywords = [ "protocol", "layer", "link" ]
aliases = [ "/questions/16910" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Link Layer Protocol ?](/questions/16910/link-layer-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16910-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I look at a packet, how can I tell what the link-layer protocol is? Where is it shown in wireshark??</p><p>Many thanks.. Sorry if this is an obvious question.</p></div><div id="question-tags" class="tags-container tags">protocol layer link</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '12, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/25bfab3fbdcc85732922e9d5de11cae0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smc20&#39;s gravatar image" /><p>smc20<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smc20 has no accepted answers">0%</span></p></div></div><div id="comments-container-16910" class="comments-container"></div><div id="comment-tools-16910" class="comment-tools"></div><div class="clear"></div><div id="comment-16910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16916"></span>

<div id="answer-container-16916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16916-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would say it is the first layer of the packet you should look at ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16916" class="comments-container"><span id="16917"></span><div id="comment-16917" class="comment"><div id="post-16917-score" class="comment-score"></div><div class="comment-text"><p>Thanks. In this case; it says:</p><p>Frame 2831: 128 bytes on wire (1024 bits), 128 bytes captured (1024 bits)</p><p>So i'm guessing that's the Link-Layer. Thanks Kurt :)</p></div><div id="comment-16917-info" class="comment-info"><span class="comment-age">(14 Dec '12, 12:57)</span> smc20</div></div><span id="16918"></span><div id="comment-16918" class="comment"><div id="post-16918-score" class="comment-score"></div><div class="comment-text"><p>erm, no. :-) The link layer protocol is: ethernet, ppp, hdlc, etc. In Wireshark it is the first layer shown <strong>after</strong> the 'Frame layer'. The link layer protocol is the protocol that is spoken on the physical medium (cable, air).</p></div><div id="comment-16918-info" class="comment-info"><span class="comment-age">(14 Dec '12, 13:01)</span> Kurt Knochner ♦</div></div><span id="16919"></span><div id="comment-16919" class="comment"><div id="post-16919-score" class="comment-score"></div><div class="comment-text"><p>Ahh okay :-) Thanks. I bet I seem stupid. Better to ask though, right?</p></div><div id="comment-16919-info" class="comment-info"><span class="comment-age">(14 Dec '12, 13:04)</span> smc20</div></div><span id="16920"></span><div id="comment-16920" class="comment"><div id="post-16920-score" class="comment-score"></div><div class="comment-text"><p>No problem. I recommend this book:</p><blockquote><p><code>http://www.amazon.com/TCP-Illustrated-Protocols-Addison-Wesley-Professional/dp/0321336313/ref=sr_1_2?s=books&amp;ie=UTF8&amp;qid=1355519196&amp;sr=1-2&amp;keywords=tcp+ip+illustrated</code><br />
</p></blockquote><p>HINT: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-16920-info" class="comment-info"><span class="comment-age">(14 Dec '12, 13:06)</span> Kurt Knochner ♦</div></div><span id="16923"></span><div id="comment-16923" class="comment"><div id="post-16923-score" class="comment-score"></div><div class="comment-text"><p>Note also that some link layers don't show up as what they really are - PPP might show up as Ethernet on Windows or as "Linux cooked-mode capture" on Linux, and 802.11 might show up as Ethernet, for example.</p><p>Some link layers might also provide "metadata" that shows up as a layer after "Frame" but before the link layer, such as the various forms of radio information metadata for 802.11.</p></div><div id="comment-16923-info" class="comment-info"><span class="comment-age">(14 Dec '12, 20:28)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16916" class="comment-tools"></div><div class="clear"></div><div id="comment-16916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

