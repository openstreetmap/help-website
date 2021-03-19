+++
type = "question"
title = "tcp duplicate ack in MPTCP iscsi traffic"
description = '''I am looking at the multi-path iscsi traffic trace and seeing occasional tcp duplicate acks. 3706 2013-11-08 14:02:09.353893 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#1] 59969 &amp;gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5193408 3708 2013-11-08 14:02:09.3539...'''
date = "2013-11-08T11:22:00Z"
lastmod = "2013-11-09T06:47:00Z"
weight = 26784
keywords = [ "ack", "iscsi", "mptcp", "tcp" ]
aliases = [ "/questions/26784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp duplicate ack in MPTCP iscsi traffic](/questions/26784/tcp-duplicate-ack-in-mptcp-iscsi-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26784-score" class="post-score" title="current number of votes">0</div><span id="post-26784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at the multi-path iscsi traffic trace and seeing occasional tcp duplicate acks.</p><p>3706 2013-11-08 14:02:09.353893 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#1] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5193408</p><p>3708 2013-11-08 14:02:09.353927 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#2] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5202368</p><p>3710 2013-11-08 14:02:09.353955 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#3] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5205232</p><p>3712 2013-11-08 14:02:09.354131 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#4] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5214192</p><p>3716 2013-11-08 14:02:09.354191 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#5] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5223103</p><p>3722 2013-11-08 14:02:09.354414 192.168.1.1 192.168.1.250 TCP [TCP Dup ACK 3704#6] 59969 &gt; iscsi-target [ACK] Seq=11134753 Ack=5166528 Win=65535 Len=0 SLE=5175488 SRE=5232063</p><p>if I interpreted rfc6824 correctly, [TCP Dup ACK] should not be a concern unless you get more than two in a row?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-mptcp" rel="tag" title="see questions tagged &#39;mptcp&#39;">mptcp</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-26784" class="comments-container"></div><div id="comment-tools-26784" class="comment-tools"></div><div class="clear"></div><div id="comment-26784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26796"></span>

<div id="answer-container-26796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26796-score" class="post-score" title="current number of votes">1</div><span id="post-26796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicate acks are sent immediately when packets arrive out of order. When the sender sees the 3rd (sometimes 2nd) duplicate ACK it considers the segment lost and starts a fast retransmission. Happens now and then in streaming traffic like your iSCSI. This trace shows that the SACK option is used on the session. The client is missing seq# 5166528 in the length of 8960 bytes and bytes 5175488-5232063 have successfully been received.</p><p>If it doesn't happen too often, it is nothing to be too concerned about</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dupack.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '13, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-26796" class="comments-container"><span id="26801"></span><div id="comment-26801" class="comment"><div id="post-26801-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If it doesn't happen too often, it is nothing to be too concerned about</p></blockquote><p>Got it, can you define "too often"</p></div><div id="comment-26801-info" class="comment-info"><span class="comment-age">(09 Nov '13, 06:31)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="26802"></span><div id="comment-26802" class="comment"><div id="post-26802-score" class="comment-score"></div><div class="comment-text"><p>This capture was done from one of 3 iscsi paths that this server has. I am also seeing missing segments, but that’s probably because they traveled over other iscsi links. Do I have to capture traffic on all 3 at the same time and then somehow merge all 3 captures in to one to see the whole picture?</p></div><div id="comment-26802-info" class="comment-info"><span class="comment-age">(09 Nov '13, 06:36)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="26803"></span><div id="comment-26803" class="comment"><div id="post-26803-score" class="comment-score"></div><div class="comment-text"><p>It depends what the throughput expectations are based on the infrastructure being used. A long distance connection surely suffers more often than a local Gb ethernet which is being used here as jumbo frames are being used. TCP will slow down when packet loss is detected, so in an iscsi environment I'd expect to see cloe to zero packet loss rate</p></div><div id="comment-26803-info" class="comment-info"><span class="comment-age">(09 Nov '13, 06:47)</span> <span class="comment-user userinfo">mrEEde2</span></div></div></div><div id="comment-tools-26796" class="comment-tools"></div><div class="clear"></div><div id="comment-26796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

