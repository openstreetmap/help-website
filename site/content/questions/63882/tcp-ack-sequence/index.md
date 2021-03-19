+++
type = "question"
title = "tcp ack sequence"
description = '''evaluating capture packets, client sends packets with seq numbers 1271, 2646, 4021, 5396, 6771, 8146, 9521, 10896, 12271, 13646 Receiver sends acknowledgements with acks= 5396, 8146, 10896, 13646 Why are acknowledgements sent for every other packet and where in the packet can this information be fou...'''
date = "2017-10-13T16:02:00Z"
lastmod = "2017-10-14T01:36:00Z"
weight = 63882
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/63882" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcp ack sequence](/questions/63882/tcp-ack-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63882-score" class="post-score" title="current number of votes">0</div><span id="post-63882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>evaluating capture packets, client sends packets with seq numbers 1271, 2646, 4021, 5396, 6771, 8146, 9521, 10896, 12271, 13646 Receiver sends acknowledgements with acks= 5396, 8146, 10896, 13646</p><p>Why are acknowledgements sent for every other packet and where in the packet can this information be found?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '17, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/e6f3653598fff83f2182e3f633d7403c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulPi&#39;s gravatar image" /><p><span>PaulPi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulPi has no accepted answers">0%</span></p></div></div><div id="comments-container-63882" class="comments-container"></div><div id="comment-tools-63882" class="comment-tools"></div><div class="clear"></div><div id="comment-63882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63888"></span>

<div id="answer-container-63888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63888-score" class="post-score" title="current number of votes">0</div><span id="post-63888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ACK frequency (every other packet) is something that was proposed in the TCP RFC, e.g. in <a href="https://tools.ietf.org/html/rfc1122">https://tools.ietf.org/html/rfc1122</a> at section "4.2.3.2 When to Send an ACK Segment". Every stack can chose the acknowledgement frequency it wants to use, but usually it's "every other packet". ACKing each packet would send unnecessary amounts of packets in most situations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '17, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63888" class="comments-container"></div><div id="comment-tools-63888" class="comment-tools"></div><div class="clear"></div><div id="comment-63888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63889"></span>

<div id="answer-container-63889" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63889-score" class="post-score" title="current number of votes">0</div><span id="post-63889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Because the communication path between the sender and the recipient and back may introduce a significant amount of delay, sending a packet only after receiving the acknowledge for the previously sent one could seriously limit the throughput. To mitigate the influence of RTT (Round-Trip Time) to the throughput, TCP has introduced a concept of receive window and a summary ACK which confirms reception of all <strong>bytes</strong> from the first one up to the ACKed one, rather than reception of individual packets. So there is no need to send ACK for each SEQ.</p><p>There is an add-on to this philosophy which allows to inform the sender about ranges of data newer than the ACKed ones which have already been received and which are still missing, it is called Selective Acknowledge - SACK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '17, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '17, 01:38</strong> </span></p></div></div><div id="comments-container-63889" class="comments-container"></div><div id="comment-tools-63889" class="comment-tools"></div><div class="clear"></div><div id="comment-63889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

