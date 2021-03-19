+++
type = "question"
title = "wrong behavior for TCP-Delayed Ack"
description = '''Hi, I have a trace file which makes me be confused on the behavior of tcp-delayed Ack.  As you can see, 192. send 7 tcp segments to 10., but where is the Ack for packet #3 and #4.Shouldn&#x27;t we expect to see an Ack for those two packets according to the rule of tcp-delayed Ack? We see the Ack from 10....'''
date = "2013-12-30T22:32:00Z"
lastmod = "2013-12-31T01:14:00Z"
weight = 28494
keywords = [ "tcp_delayed_ack" ]
aliases = [ "/questions/28494" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [wrong behavior for TCP-Delayed Ack](/questions/28494/wrong-behavior-for-tcp-delayed-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28494-score" class="post-score" title="current number of votes">0</div><span id="post-28494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a trace file which makes me be confused on the behavior of tcp-delayed Ack. <img src="http://img.my.csdn.net/uploads/201312/31/1388471175_2006.jpg" alt="alt text" /></p><p>As you can see, 192. send 7 tcp segments to 10., but where is the Ack for packet #3 and #4.Shouldn't we expect to see an Ack for those two packets according to the rule of tcp-delayed Ack? We see the Ack from 10. at packet #10, which acked all of the bytes including #8.</p><p>Is it a right behavior?</p><p>Note: if you cannot see the full picture, please copy paste the link _<a href="http://img.my.csdn.net/uploads/201312/31/1388471175_2006.jpg">http://img.my.csdn.net/uploads/201312/31/1388471175_2006.jpg</a> directly to the web browser.</p><p>thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_delayed_ack" rel="tag" title="see questions tagged &#39;tcp_delayed_ack&#39;">tcp_delayed_ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '13, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></img></div></div><div id="comments-container-28494" class="comments-container"></div><div id="comment-tools-28494" class="comment-tools"></div><div class="clear"></div><div id="comment-28494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28499"></span>

<div id="answer-container-28499" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28499-score" class="post-score" title="current number of votes">0</div><span id="post-28499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://tools.ietf.org/html/rfc1122">RFC 1122</a> says that "...in a stream of full-sized segments there SHOULD be an ACK for every second segment."</p><p>The use of "SHOULD" in the RFC means that this behavior is not mandatory, and an implementation may adopt different behavior. There are TCP/IP stacks that send Delayed ACKs less often than every other segment. In other words, an ACK for every other segment is not really a rule.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '13, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-28499" class="comments-container"></div><div id="comment-tools-28499" class="comment-tools"></div><div class="clear"></div><div id="comment-28499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28495"></span>

<div id="answer-container-28495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28495-score" class="post-score" title="current number of votes">0</div><span id="post-28495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Packets 3-9 all arrive at the same time so when they were traced the receiving TCP didn't see them yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '13, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28495" class="comments-container"><span id="28498"></span><div id="comment-28498" class="comment"><div id="post-28498-score" class="comment-score"></div><div class="comment-text"><p>I think this packet trace was NOT captured on 10., because right after getting #3 and #4, the receiver tcp should generate an Ack to them according to the rule of tcp delayed-ack. What do you mean for arrive at the same time? From tcp perspective, shouldn't the tcp stack code always triage the function call to generate a Ack for every other packet?</p><p>Or do you mean we do have an Ack for #3 and #4, just wireshark cannot capture it?</p></div><div id="comment-28498-info" class="comment-info"><span class="comment-age">(31 Dec '13, 00:18)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-28495" class="comment-tools"></div><div class="clear"></div><div id="comment-28495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

