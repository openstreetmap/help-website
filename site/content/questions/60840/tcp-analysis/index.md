+++
type = "question"
title = "TCP analysis"
description = '''How does TCP anaysis duplicate ACK (tcp.analysis.duplicate_ack), TCP analysis RTT (tcp.analysis.ack_rtt), Fast retransmission (tcp.analysis.fast_retransmission) affect the evaluation (estimation) of TCP congestion window (cwnd)? Will my evaluation without these analysis parameters be meaningful for ...'''
date = "2017-04-15T03:33:00Z"
lastmod = "2017-04-15T04:50:00Z"
weight = 60840
keywords = [ "congestion", "congestion-control", "congestion-avoidance", "tcp", "wireshark" ]
aliases = [ "/questions/60840" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP analysis](/questions/60840/tcp-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60840-score" class="post-score" title="current number of votes">0</div><span id="post-60840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does TCP anaysis duplicate ACK (<strong>tcp.analysis.duplicate_ack</strong>), TCP analysis RTT (<strong>tcp.analysis.ack_rtt</strong>), Fast retransmission (<strong>tcp.analysis.fast_retransmission</strong>) affect the evaluation (estimation) of TCP congestion window (cwnd)? Will my evaluation without these analysis parameters be meaningful for estimating TCP cwnd?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span> <span class="post-tag tag-link-congestion-control" rel="tag" title="see questions tagged &#39;congestion-control&#39;">congestion-control</span> <span class="post-tag tag-link-congestion-avoidance" rel="tag" title="see questions tagged &#39;congestion-avoidance&#39;">congestion-avoidance</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '17, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '17, 10:50</strong> </span></p></div></div><div id="comments-container-60840" class="comments-container"></div><div id="comment-tools-60840" class="comment-tools"></div><div class="clear"></div><div id="comment-60840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60841"></span>

<div id="answer-container-60841" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60841-score" class="post-score" title="current number of votes">1</div><span id="post-60841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Interesting question, but I guess you'll have to start reading TCP stack code now, most likely of the Linux kernel (because it's available), e.g.:</p><p><a href="https://github.com/torvalds/linux/blob/master/net/ipv4/tcp.c">https://github.com/torvalds/linux/blob/master/net/ipv4/tcp.c</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '17, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Apr '17, 04:51</strong> </span></p></div></div><div id="comments-container-60841" class="comments-container"></div><div id="comment-tools-60841" class="comment-tools"></div><div class="clear"></div><div id="comment-60841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

