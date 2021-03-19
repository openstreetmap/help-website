+++
type = "question"
title = "conversations and multiplexing"
description = '''How to write dissector in this case: My protocol contains internal channel number (one udp stream contains multiply data streams). Calling another dissector(A), which is using conversations creates bug: [udp.src1-&amp;gt;udp.dst1] [myproto.ch==1] SomeData1ForAnotherDissector1(X) [udp.src1-&amp;gt;udp.dst1] ...'''
date = "2015-07-22T02:31:00Z"
lastmod = "2015-07-23T14:33:00Z"
weight = 44365
keywords = [ "multiplexing", "conversations" ]
aliases = [ "/questions/44365" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [conversations and multiplexing](/questions/44365/conversations-and-multiplexing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44365-score" class="post-score" title="current number of votes">0</div><span id="post-44365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to write dissector in this case:<br />
My protocol contains internal channel number (one udp stream contains multiply data streams).<br />
Calling another dissector(A), which is using conversations creates bug:<br />
<strong>[udp.src1-&gt;udp.dst1] [myproto.ch==1] SomeData1ForAnotherDissector1(X)</strong><br />
[udp.src1-&gt;udp.dst1] [myproto.ch==2] SomeData2ForAnotherDissector1(Y)<br />
<strong>[udp.src1-&gt;udp.dst1] [myproto.ch==1] SomeData1ForAnotherDissector2(Z)</strong><br />
[udp.src1-&gt;udp.dst1] [myproto.ch==2] SomeData2ForAnotherDissector2(W)<br />
But dissector A known only about one Stream <strong>XYZW</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiplexing" rel="tag" title="see questions tagged &#39;multiplexing&#39;">multiplexing</span> <span class="post-tag tag-link-conversations" rel="tag" title="see questions tagged &#39;conversations&#39;">conversations</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '15, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/9ab5d88b30e1722e12e4303c76d44125?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chernyh&#39;s gravatar image" /><p><span>Andrew Chernyh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chernyh has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-44365" class="comments-container"><span id="44385"></span><div id="comment-44385" class="comment"><div id="post-44385-score" class="comment-score"></div><div class="comment-text"><p>So your protocol runs over UDP, and other protocols run over it? And a single UDP conversation carrying your protocol can have different subprotocols for different channels in your protocol?</p></div><div id="comment-44385-info" class="comment-info"><span class="comment-age">(22 Jul '15, 13:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44403"></span><div id="comment-44403" class="comment"><div id="post-44403-score" class="comment-score"></div><div class="comment-text"><p>Yes. My answer is about TDMoP protocol dissector. Protocol header contains source and dest TDM channel, and they are independent. I think, that tdmoe protocol dissector has same trouble: subaddress for channel identification. Calling of lapd_handle (lapd-bitstream), will give wrong result when multiply streams (same source mac, dest mac, but not same subaddress) captured.</p></div><div id="comment-44403-info" class="comment-info"><span class="comment-age">(22 Jul '15, 20:00)</span> <span class="comment-user userinfo">Andrew Chernyh</span></div></div></div><div id="comment-tools-44365" class="comment-tools"></div><div class="clear"></div><div id="comment-44365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44422"></span>

<div id="answer-container-44422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44422-score" class="post-score" title="current number of votes">0</div><span id="post-44422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to pass the channel number from your dissector to dissector A, and have it use <em>both</em> the UDP conversation and channel number to determine which subdissector to call.</p><p>Ideally, the libwireshark notion of conversations would be more general, and your dissector would create a TDMoP conversation which would be indexed by source and destination IP addresses, source and destination ports, <em>and</em> the channel number, and a dissector could be associated with a TDMoP conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '15, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-44422" class="comments-container"></div><div id="comment-tools-44422" class="comment-tools"></div><div class="clear"></div><div id="comment-44422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

