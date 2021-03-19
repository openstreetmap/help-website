+++
type = "question"
title = "Estimating/modeling TCP latency"
description = '''I&#x27;m using TCP to send messages among two linux hosts on the same subnet at a fixed period and I can see occasional cases where a &quot;fast retransmission&quot; occurs and the application appears to see significant jitter as a result.  A single segment looks like it may have been lost and the subsequent ones ...'''
date = "2013-03-29T10:23:00Z"
lastmod = "2013-03-29T12:54:00Z"
weight = 19939
keywords = [ "latency", "tcp" ]
aliases = [ "/questions/19939" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Estimating/modeling TCP latency](/questions/19939/estimatingmodeling-tcp-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19939-score" class="post-score" title="current number of votes">0</div><span id="post-19939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using TCP to send messages among two linux hosts on the same subnet at a fixed period and I can see occasional cases where a "fast retransmission" occurs and the application appears to see significant jitter as a result.<br />
</p><p>A single segment looks like it may have been lost and the subsequent ones all <del>back up</del>are queued for delivery to the application/head of line blocking -- classic case where TCP was not the right tool for the job.</p><p>I know I can mitigate the problem with UDP or SCTP, but I'd like to understand just how bad it is for TCP.</p><p>EDIT: UDP is appropriate because the application is so latency-sensitive. Late data is invalid data.</p><p>In my particular case, is the recovery/retransmission delay a function of the period at which I'm sending the messages? Or are there TCP specifications which guide this (usually specified as a function of RTT?). Or perhaps are there stack/implementation-specific timeouts that can be adjusted/tuned?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '13, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/5663a87dd96f05804570fc5b5aec2516?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bcain&#39;s gravatar image" /><p><span>bcain</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bcain has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '13, 12:56</strong> </span></p></div></div><div id="comments-container-19939" class="comments-container"></div><div id="comment-tools-19939" class="comment-tools"></div><div class="clear"></div><div id="comment-19939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19940"></span>

<div id="answer-container-19940" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19940-score" class="post-score" title="current number of votes">1</div><span id="post-19940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bcain has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Usually a lost TCP segment should not block remaining segments to be accepted, because the sender will keep sending until it notices that the segment was lost, and the receiver should keep putting the incoming segments into it's receive window. What may kill your performance (if you're close to doing real time processing) is the fact that the data in the TCP window may not be forwarded to the application while there still is the gap from the missing segment. You'd probably have a similar problem with UDP because it will lead to the same problem just a layer above the stack.</p><p>If you notice that your receiving TCP stack requests ALL packets again from the lost segment on you have a pretty inefficient stack on the receiver's side. If the sender starts retransmitting packets without them being lost in the first place your sender TCP stack is not very good at what it does.</p><p>What can happen is that when you have a pretty fast connection that it will take a while for a retransmission to get through, because it has to "get in line" after all the other segments that are already on their way. Maybe it could help if you force a smaller receive window on the receiving node by calculating the optimum window size. That way the sender cannot blast away with packets like crazy, and retransmission should be getting through as fast as possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '13, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19940" class="comments-container"><span id="19941"></span><div id="comment-19941" class="comment"><div id="post-19941-score" class="comment-score"></div><div class="comment-text"><p>"You'd probably have a similar problem with UDP because it will lead to the same problem just a layer above the stack" -- but any one of these messages is adequate (late data is invalid data). So I don't think it would be a problem.</p></div><div id="comment-19941-info" class="comment-info"><span class="comment-age">(29 Mar '13, 12:42)</span> <span class="comment-user userinfo">bcain</span></div></div><span id="19942"></span><div id="comment-19942" class="comment"><div id="post-19942-score" class="comment-score"></div><div class="comment-text"><p>Okay, you didn't mention that you can afford to lose some of the messages. In that case UDP might have a slight edge, but I still don't see why subsequent TCP messages should be delayed by a lost segment.</p></div><div id="comment-19942-info" class="comment-info"><span class="comment-age">(29 Mar '13, 12:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="19943"></span><div id="comment-19943" class="comment"><div id="post-19943-score" class="comment-score"></div><div class="comment-text"><p>Because it's designed to <a href="http://en.wikipedia.org/wiki/Head-of-line_blocking">preserve order</a>. I'm talking about the delay perceived by the application.</p></div><div id="comment-19943-info" class="comment-info"><span class="comment-age">(29 Mar '13, 12:54)</span> <span class="comment-user userinfo">bcain</span></div></div></div><div id="comment-tools-19940" class="comment-tools"></div><div class="clear"></div><div id="comment-19940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

