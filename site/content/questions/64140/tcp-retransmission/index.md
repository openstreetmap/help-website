+++
type = "question"
title = "TCP Retransmission"
description = '''Hi colleges! I have a problem.  What does it mean?  209437 2017-10-23 12:58:51,305454 10.216.43.66 10.217.53.23 TCP 67 58579 → 1522 [PSH, ACK] Seq=206761 Ack=215228 Win=63495 Len=13 209439 2017-10-23 12:58:51,332787 10.216.43.66 10.217.53.23 TCP 67 [TCP Retransmission] 58579 → 1522 [PSH, ACK] Seq=20...'''
date = "2017-10-24T00:47:00Z"
lastmod = "2017-10-24T14:22:00Z"
weight = 64140
keywords = [ "retransmission", "tcp" ]
aliases = [ "/questions/64140" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission](/questions/64140/tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64140-score" class="post-score" title="current number of votes">0</div><span id="post-64140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi colleges! I have a problem. What does it mean?</p><pre><code>209437  2017-10-23 12:58:51,305454  10.216.43.66    10.217.53.23    TCP 67  58579 → 1522 [PSH, ACK] Seq=206761 Ack=215228 Win=63495 Len=13
209439  2017-10-23 12:58:51,332787  10.216.43.66    10.217.53.23    TCP 67  [TCP Retransmission] 58579 → 1522 [PSH, ACK] Seq=206761 Ack=215228 Win=63495 Len=13
209442  2017-10-23 12:58:51,355010  10.216.43.66    10.217.53.23    TCP 67  58579 → 1522 [PSH, ACK, CWR] Seq=206774 Ack=215239 Win=63484 Len=13</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/03d3cab83c736b783c574bf8b62d46ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silenciovoid&#39;s gravatar image" /><p><span>Silenciovoid</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silenciovoid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '17, 03:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-64140" class="comments-container"></div><div id="comment-tools-64140" class="comment-tools"></div><div class="clear"></div><div id="comment-64140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64169"></span>

<div id="answer-container-64169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64169-score" class="post-score" title="current number of votes">0</div><span id="post-64169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like 10.216.43.66 thinks there is packet loss, so it retransmits a packet and signals "Congestion Window reduced", meaning it will slow down. I doubt much more can be said about a text dump that short.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-64169" class="comments-container"></div><div id="comment-tools-64169" class="comment-tools"></div><div class="clear"></div><div id="comment-64169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

