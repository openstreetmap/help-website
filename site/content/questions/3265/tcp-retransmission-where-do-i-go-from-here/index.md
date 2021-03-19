+++
type = "question"
title = "TCP retransmission. Where do I go from here?"
description = '''Hi all, I&#x27;m rather new to being able to diagnose problems from tcpdumps so please forgive me. We&#x27;re getting connectivity issues between two of ours sites, a dump of a http trace shows regular TCP retransmissions. What are the next steps to diagnose what&#x27;s going on, and more importantly how to fix it...'''
date = "2011-04-01T03:35:00Z"
lastmod = "2011-04-04T00:56:00Z"
weight = 3265
keywords = [ "tcp-fast-retransmit", "tcp" ]
aliases = [ "/questions/3265" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP retransmission. Where do I go from here?](/questions/3265/tcp-retransmission-where-do-i-go-from-here)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3265-score" class="post-score" title="current number of votes">0</div><span id="post-3265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm rather new to being able to diagnose problems from tcpdumps so please forgive me. We're getting connectivity issues between two of ours sites, a dump of a http trace shows regular TCP retransmissions.</p><p>What are the next steps to diagnose what's going on, and more importantly how to fix it? Below is a small sample of the trace.</p><pre><code>&quot;132&quot;,&quot;22.431990&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;[TCP Previous segment lost] Continuation or non-HTTP traffic&quot;
&quot;133&quot;,&quot;22.432062&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#1] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=47430&quot;
&quot;134&quot;,&quot;22.433992&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;Continuation or non-HTTP traffic&quot;
&quot;135&quot;,&quot;22.434066&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#2] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=48890&quot;
&quot;136&quot;,&quot;22.436012&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;Continuation or non-HTTP traffic&quot;
&quot;137&quot;,&quot;22.436082&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#3] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=50350&quot;
&quot;138&quot;,&quot;22.437991&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;Continuation or non-HTTP traffic&quot;
&quot;139&quot;,&quot;22.438067&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#4] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=51810&quot;
&quot;140&quot;,&quot;22.439992&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;Continuation or non-HTTP traffic&quot;
&quot;141&quot;,&quot;22.439997&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;Continuation or non-HTTP traffic&quot;
&quot;142&quot;,&quot;22.440068&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#5] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=53270&quot;
&quot;143&quot;,&quot;22.440087&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;[TCP Dup ACK 131#6] mns-mail &gt; http [ACK] Seq=1756 Ack=44510 Win=65700 [TCP CHECKSUM INCORRECT] Len=0 SLE=45970 SRE=53624&quot;
&quot;144&quot;,&quot;22.444995&quot;,&quot;192.168.2.13&quot;,&quot;192.168.1.94&quot;,&quot;HTTP&quot;,&quot;[TCP Fast Retransmission] Continuation or non-HTTP traffic&quot;
&quot;145&quot;,&quot;22.445110&quot;,&quot;192.168.1.94&quot;,&quot;192.168.2.13&quot;,&quot;TCP&quot;,&quot;mns-mail &gt; http [ACK] Seq=1756 Ack=53624 Win=65700 [TCP CHECKSUM INCORRECT] Len=0&quot;</code></pre><p>Any help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-fast-retransmit" rel="tag" title="see questions tagged &#39;tcp-fast-retransmit&#39;">tcp-fast-retransmit</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '11, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/4aad49e9bf7cd79a721ae0997f351dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan%20Hollis&#39;s gravatar image" /><p><span>Alan Hollis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan Hollis has no accepted answers">0%</span></p></div></div><div id="comments-container-3265" class="comments-container"></div><div id="comment-tools-3265" class="comment-tools"></div><div class="clear"></div><div id="comment-3265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3268"></span>

<div id="answer-container-3268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3268-score" class="post-score" title="current number of votes">1</div><span id="post-3268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You probably need to describe in more detail waht "connectivity issues" you mean. Are you talking about initiating connections, or throughput issues or timeouts/pauses in your application, or something else?</p><p>The sample you have give is only for 14ms - a pretty short time period - yet a lot is happening, so it is possibly a fairly fast link. From what we can see, this connection is using SACK (selective acknowledgment) to recover from a lost packet. All this is fairly normal, and possibly the result of congestion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-3268" class="comments-container"></div><div id="comment-tools-3268" class="comment-tools"></div><div class="clear"></div><div id="comment-3268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3269"></span>

<div id="answer-container-3269" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3269-score" class="post-score" title="current number of votes">0</div><span id="post-3269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you very much for your reply.</p><p>At the time there was only one request coming from my machine to that host. I guess by congestion you mean other machines on the network using that link?.</p><p>The link between the two subnets is a 10 megabyte per second Ethernet link, which shouldn't be congested at all I don't believe. We have 7 machines in the office and maybe two of them in total SHOULD be communicating with this link at any one time? Would that be something worth investigating? The problem came to light because every so often a soap message we use to determine information about some software is failing, and generating alarms.</p><p>The trace is of a http request to a webserver sitting on the .2 subnet is that helps.</p><p>Thanks again for your reply it's very much appreciated.</p><p>Alan</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/4aad49e9bf7cd79a721ae0997f351dd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan%20Hollis&#39;s gravatar image" /><p><span>Alan Hollis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan Hollis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '11, 07:04</strong> </span></p></div></div><div id="comments-container-3269" class="comments-container"><span id="3280"></span><div id="comment-3280" class="comment"><div id="post-3280-score" class="comment-score"></div><div class="comment-text"><p>If you can post the actual packet capture somewhere, I'm sure more people can help you. But it looks to me like you have a duplex mismatch. Make sure the swtitchport and the NICs all match.</p></div><div id="comment-3280-info" class="comment-info"><span class="comment-age">(01 Apr '11, 17:54)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="3319"></span><div id="comment-3319" class="comment"><div id="post-3319-score" class="comment-score"></div><div class="comment-text"><p>Thanks again. The full csv file is here (http://www.alanhollis.com/work/tcpdump) unfortunately I didn't save the full dump. I'll have a go at looking at all the duplex settings now. Thanks for your reply!</p></div><div id="comment-3319-info" class="comment-info"><span class="comment-age">(04 Apr '11, 00:56)</span> <span class="comment-user userinfo">Alan Hollis</span></div></div></div><div id="comment-tools-3269" class="comment-tools"></div><div class="clear"></div><div id="comment-3269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

