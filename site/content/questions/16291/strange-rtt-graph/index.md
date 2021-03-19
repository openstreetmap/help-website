+++
type = "question"
title = "Strange RTT graph"
description = '''Hi! What is the reason of this kind of RTT graph? BR.'''
date = "2012-11-26T00:13:00Z"
lastmod = "2012-12-04T04:24:00Z"
weight = 16291
keywords = [ "rtt" ]
aliases = [ "/questions/16291" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Strange RTT graph](/questions/16291/strange-rtt-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16291-score" class="post-score" title="current number of votes">0</div><span id="post-16291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>What is the reason of this kind of RTT graph?</p><p>BR.<img src="https://osqa-ask.wireshark.org/upfiles/1.UE_2.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '12, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/d86423e347d84a887ef265da9fba230f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nurik&#39;s gravatar image" /><p><span>Nurik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nurik has no accepted answers">0%</span></p></img></div></div><div id="comments-container-16291" class="comments-container"><span id="16302"></span><div id="comment-16302" class="comment"><div id="post-16302-score" class="comment-score"></div><div class="comment-text"><p>can you please add a "Throughput Graph" and a "Time-Sequence Graph (tcptrace)".</p></div><div id="comment-16302-info" class="comment-info"><span class="comment-age">(26 Nov '12, 02:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16533"></span><div id="comment-16533" class="comment"><div id="post-16533-score" class="comment-score"></div><div class="comment-text"><p>Throuput graph<img src="https://osqa-ask.wireshark.org/upfiles/01_04-Dec-12_16.22.18.jpg" alt="alt text" /></p></div><div id="comment-16533-info" class="comment-info"><span class="comment-age">(04 Dec '12, 04:23)</span> <span class="comment-user userinfo">Nurik</span></div></div><span id="16534"></span><div id="comment-16534" class="comment"><div id="post-16534-score" class="comment-score"></div><div class="comment-text"><p>Time-Sequence Graph (tcptrace)<img src="https://osqa-ask.wireshark.org/upfiles/02_04-Dec-12_16.23.00.jpg" alt="alt text" /></p></div><div id="comment-16534-info" class="comment-info"><span class="comment-age">(04 Dec '12, 04:24)</span> <span class="comment-user userinfo">Nurik</span></div></div></div><div id="comment-tools-16291" class="comment-tools"></div><div class="clear"></div><div id="comment-16291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16298"></span>

<div id="answer-container-16298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16298-score" class="post-score" title="current number of votes">1</div><span id="post-16298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The vertical "lines" in your RTT graph might be wrongly assumed high delay packets, when wireshark is checking a certain sequence number for the time it takes TCP to ACK the data. When you have packet loss, this can be a typical graphical outcome of wireshark interpreting constant ACK numbers while waiting for a retransmission of lost data.</p><p>That could in theory also explain why your UDP transfer gets higher throughput, if the UDP application doesn't care for packet loss, while TCP very well does - check for tcp.analysis.flags</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></img></div></div><div id="comments-container-16298" class="comments-container"></div><div id="comment-tools-16298" class="comment-tools"></div><div class="clear"></div><div id="comment-16298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16292"></span>

<div id="answer-container-16292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16292-score" class="post-score" title="current number of votes">0</div><span id="post-16292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks pretty normal to me... you've got tons of times below 0.05 seconds, and sometimes it goes up when there is contention, which is caused by buffering delays.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-16292" class="comments-container"><span id="16293"></span><div id="comment-16293" class="comment"><div id="post-16293-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but how it can be solved? Previous RTT graph was made on client side logs. I think i have low throughput due to this delays. Below RTT graph of same session from point closer to server. <img src="https://osqa-ask.wireshark.org/upfiles/3.EPC.jpg" alt="alt text" /></p></div><div id="comment-16293-info" class="comment-info"><span class="comment-age">(26 Nov '12, 00:35)</span> <span class="comment-user userinfo">Nurik</span></div></div><span id="16294"></span><div id="comment-16294" class="comment"><div id="post-16294-score" class="comment-score"></div><div class="comment-text"><p>and what it means "which is caused by buffering delays." ?</p><p>BR</p></div><div id="comment-16294-info" class="comment-info"><span class="comment-age">(26 Nov '12, 00:36)</span> <span class="comment-user userinfo">Nurik</span></div></div><span id="16295"></span><div id="comment-16295" class="comment"><div id="post-16295-score" class="comment-score"></div><div class="comment-text"><p>Additional info regarding this issue, with UDP I'm getting 30Mbps, but with TCP no more then 10Mbps.</p></div><div id="comment-16295-info" class="comment-info"><span class="comment-age">(26 Nov '12, 00:38)</span> <span class="comment-user userinfo">Nurik</span></div></div></div><div id="comment-tools-16292" class="comment-tools"></div><div class="clear"></div><div id="comment-16292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

