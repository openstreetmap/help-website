+++
type = "question"
title = "TCP previous segment not captured and Dup ACKs"
description = '''A small capture is here Please confirm or correct my analysis: Looking at #17, It appears that some packets were dropped on their way from the server (10.230.36.138) to the client (10.3.2.205). As a result, the client receives a TCP segment with a sequence number higher than the expected one (out of...'''
date = "2016-07-12T12:44:00Z"
lastmod = "2016-07-12T13:02:00Z"
weight = 54011
keywords = [ "dup-ack" ]
aliases = [ "/questions/54011" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP previous segment not captured and Dup ACKs](/questions/54011/tcp-previous-segment-not-captured-and-dup-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54011-score" class="post-score" title="current number of votes">0</div><span id="post-54011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A small capture is <a href="https://www.cloudshark.org/captures/fe90213f6815">here</a></p><p>Please confirm or correct my analysis:</p><p>Looking at <strong>#17</strong>, It appears that some packets were dropped on their way from the server (10.230.36.138) to the client (10.3.2.205). As a result, the client receives a TCP segment with a sequence number higher than the expected one (out of order segment).</p><p>The client updates the server with regards to the dropped/missing TCP segment by sending "DupAcks" to the server. (If say 20 packets were dropped, the client only sends DupAcks for <strong>the single packet</strong> it was expecting).</p><p>After sending 55 DupAcks, the server finally fast retransmit that single packet. We don't know why it took 55 DupAcks. It could be the server setting or DupAcks not making it to the server.</p><p>I could be totally wrong. So please advice.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/de898090cf41d70e79d07c92b2d09330?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sshamim&#39;s gravatar image" /><p><span>sshamim</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sshamim has no accepted answers">0%</span></p></div></div><div id="comments-container-54011" class="comments-container"></div><div id="comment-tools-54011" class="comment-tools"></div><div class="clear"></div><div id="comment-54011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54012"></span>

<div id="answer-container-54012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54012-score" class="post-score" title="current number of votes">1</div><span id="post-54012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The packet loss is always signaled by setting the ACK number to the last byte of payload the was received without a gap. So if anything is lost, the ACK number stays on the last successful byte, no matter how many more packets make it through. ACK is only increased when the retransmission arrives.</p><p>55 Dup ACKs has nothing to do with a server setting, or them not making it through. It just takes a while for the Fast Retranmission to make it through. It's a little hard to tell because you didn't capture the TCP handshake, so we don't know the initial round trip time. I guess you suffer from a minor case of buffer bloat. See this question: <a href="https://ask.wireshark.org/questions/39043/1500-duplicate-acks-before-retransmission">https://ask.wireshark.org/questions/39043/1500-duplicate-acks-before-retransmission</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54012" class="comments-container"></div><div id="comment-tools-54012" class="comment-tools"></div><div class="clear"></div><div id="comment-54012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

