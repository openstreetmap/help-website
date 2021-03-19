+++
type = "question"
title = "Why the tcp.flags.ack=1,but no data received!"
description = '''i captured many tcp packets,why the server mark the tcp.flags.ack=1,but not received any packets from client?'''
date = "2012-10-25T18:10:00Z"
lastmod = "2012-10-27T02:33:00Z"
weight = 15283
keywords = [ "ack" ]
aliases = [ "/questions/15283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why the tcp.flags.ack=1,but no data received!](/questions/15283/why-the-tcpflagsack1but-no-data-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15283-score" class="post-score" title="current number of votes">0</div><span id="post-15283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i captured many tcp packets,why the server mark the tcp.flags.ack=1,but not received any packets from client?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '12, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p><span>chinasan</span><br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div></div><div id="comments-container-15283" class="comments-container"></div><div id="comment-tools-15283" class="comment-tools"></div><div class="clear"></div><div id="comment-15283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15286"></span>

<div id="answer-container-15286" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15286-score" class="post-score" title="current number of votes">3</div><span id="post-15286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure if I get the question right, but I guess you wonder why the ACK flag would be set even though the client sent no data in its packets? If so: basically, all packets after the first SYN have the ACK flag set, no matter if the other system sent payload data or not. For example in an FTP data transfer usually one system only sends data and never receives anything, but it will still set the ACK flag for each data packet it sends out.</p><p>If you meant that see ACK packets and you do not see any client packets you usually have a problem with the capture setup, maybe asynchronous routing or a SPAN port that mirrors only one direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '12, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15286" class="comments-container"><span id="15303"></span><div id="comment-15303" class="comment"><div id="post-15303-score" class="comment-score"></div><div class="comment-text"><p>//Yes,you get my point.Thank you for your good answer!</p></div><div id="comment-15303-info" class="comment-info"><span class="comment-age">(26 Oct '12, 20:16)</span> <span class="comment-user userinfo">chinasan</span></div></div><span id="15308"></span><div id="comment-15308" class="comment"><div id="post-15308-score" class="comment-score"></div><div class="comment-text"><p>Glad to be able to help. If you like, you can accept my answer with the checkmark button on the left next to it ;-) That would indicate that the question was answered successfully to others looking at it.</p></div><div id="comment-15308-info" class="comment-info"><span class="comment-age">(27 Oct '12, 02:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-15286" class="comment-tools"></div><div class="clear"></div><div id="comment-15286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

