+++
type = "question"
title = "Duplicate ACKs + delayed retransmission"
description = '''I am doing a TCP benchmark on a TI DSP (C6474 on a EVMC6474) using NTTCP and am seeing some strange results... Sometimes the transfer goes well and I get over 220Mbps, which is what I roughly expect with my current setup. However, some transfers are &amp;lt; 50Mbps. There&#x27;s a clear pattern: every time t...'''
date = "2015-02-16T15:34:00Z"
lastmod = "2015-04-15T06:07:00Z"
weight = 39898
keywords = [ "tcp_nodelay", "duplicate_acks", "so_linger", "tcp_retransmission" ]
aliases = [ "/questions/39898" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Duplicate ACKs + delayed retransmission](/questions/39898/duplicate-acks-delayed-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39898-score" class="post-score" title="current number of votes">0</div><span id="post-39898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing a TCP benchmark on a TI DSP (C6474 on a EVMC6474) using NTTCP and am seeing some strange results... Sometimes the transfer goes well and I get over 220Mbps, which is what I roughly expect with my current setup. However, some transfers are &lt; 50Mbps. There's a clear pattern: every time the speed is &lt; 220Mbps there are 5 "duplicate ACKs" from my PC host system (172.22.23.250) followed by a long delay (about 1 second!) where both systems are not outputting any data and then finally a TCP retransmission from the DSP after which the transmission resumes at full speed. This pattern can recur multiple times during my 8MB transfer. What could cause this? I have tested with and without TCP_NODELAY as well as varied the SO_LINGER value (between 50ms and 1 second)), but to no avail. The problematic sequence still shows up about 20-50% of the time.</p><p>The DSP is running "ndk_2_0_0" and on the receiving end I have used Ubuntu 12.01 and Cygwin (on a Win 7 host). I am doing some more tests using UDP and with a newer IP-stack from TI in case this will shed some light on the situation.</p><p>I uploaded a <a href="https://www.cloudshark.org/captures/faff95c615f6">capture here</a>.</p><p>Thanks, Dirk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_nodelay" rel="tag" title="see questions tagged &#39;tcp_nodelay&#39;">tcp_nodelay</span> <span class="post-tag tag-link-duplicate_acks" rel="tag" title="see questions tagged &#39;duplicate_acks&#39;">duplicate_acks</span> <span class="post-tag tag-link-so_linger" rel="tag" title="see questions tagged &#39;so_linger&#39;">so_linger</span> <span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '15, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/bdcd60c8f4bd21eda021aa35fc76b4d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djbuijs&#39;s gravatar image" /><p><span>djbuijs</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djbuijs has no accepted answers">0%</span></p></div></div><div id="comments-container-39898" class="comments-container"></div><div id="comment-tools-39898" class="comment-tools"></div><div class="clear"></div><div id="comment-39898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39903"></span>

<div id="answer-container-39903" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39903-score" class="post-score" title="current number of votes">1</div><span id="post-39903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="djbuijs has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture shows that TCP/IP stack on the system with IP address 172.22.23.211 does not use "Fast Retransmission" (see <a href="https://tools.ietf.org/html/rfc5681#section-3.2">rfc5681</a>). Maybe it does not support it, maybe it is not enabled. But since it does not use fast retransmission, it uses the retransmission timeout for resending a packet that was lost.</p><p>The next question is why is there packet loss in the first place?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39903" class="comments-container"><span id="39917"></span><div id="comment-39917" class="comment"><div id="post-39917-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply, this is very helpful! With the term "fast retransmission" I found this thread on the TI forum (the manufacturer of NDK) where the issue is discussed: <a href="http://e2e.ti.com/support/embedded/tirtos/f/355/t/169622.">http://e2e.ti.com/support/embedded/tirtos/f/355/t/169622.</a> As a "workaround" they advise you to use " Selective Acknowledgment(SACK)" as "Fast retransmit" in not supported.</p><p>I am not sure why there's packet loss yet though.... Next I'll do a test with the latest NDK to make sure it's not a bug (I don't believe so, but this will be an easy way to exclude it). I'll post results here. Thanks!</p></div><div id="comment-39917-info" class="comment-info"><span class="comment-age">(17 Feb '15, 10:00)</span> <span class="comment-user userinfo">djbuijs</span></div></div><span id="41452"></span><div id="comment-41452" class="comment"><div id="post-41452-score" class="comment-score"></div><div class="comment-text"><p>Hi, I am experiencing TCP retransmission timeouts with the TI NDK. Did you find a solution for your problem? Best regards David</p></div><div id="comment-41452-info" class="comment-info"><span class="comment-age">(15 Apr '15, 05:50)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div><span id="41453"></span><div id="comment-41453" class="comment"><div id="post-41453-score" class="comment-score"></div><div class="comment-text"><p><span>@DavidA_2015</span>: By experience, it does not make sense to comment on a solved question that has been answered more that 4 years ago.</p><p>Please create your own question, with your own problem description and if necessary, add a link to this question (for further information).<br />
</p><p>Regards<br />
Kurt</p></div><div id="comment-41453-info" class="comment-info"><span class="comment-age">(15 Apr '15, 06:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-39903" class="comment-tools"></div><div class="clear"></div><div id="comment-39903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

