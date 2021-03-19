+++
type = "question"
title = "Latency on Citrix sessions"
description = '''Hi, we have some latency problems on our Citrix XenDesktop 6.5 sessions (regular 5sec freeze) Here is a sample of captured packets : [TCP Dup ACK 4#1] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=1461  [TCP Dup ACK 4#2] 59193 ; citriximaclient [ACK] Seq=106 A...'''
date = "2014-07-29T01:41:00Z"
lastmod = "2014-08-04T15:31:00Z"
weight = 34962
keywords = [ "latency", "tcp", "citrix" ]
aliases = [ "/questions/34962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Latency on Citrix sessions](/questions/34962/latency-on-citrix-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34962-score" class="post-score" title="current number of votes">0</div><span id="post-34962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, we have some latency problems on our Citrix XenDesktop 6.5 sessions (regular 5sec freeze) Here is a sample of captured packets :</p><pre><code>[TCP Dup ACK 4#1] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=1461

[TCP Dup ACK 4#2] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=2914

[TCP Dup ACK 4#3] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=4366

[TCP Dup ACK 4#4] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=5821

[TCP Dup ACK 4#5] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=7279 [TCP Dup ACK 4#6] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=8737

....

[TCP Dup ACK 4#43] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=57289

[TCP Dup ACK 4#44] 59193 ; citriximaclient [ACK] Seq=106 Ack=4294965385 Win=610 Len=0 SLE=4294966845 SRE=57788

[TCP Fast Retransmission] citriximaclient ; 59193 [ACK] Seq=4294965385 Ack=106 Win=511 Len=1460</code></pre><p>We can see 44 DUP ACK sent from the Citrix client to the server during 200 ms.</p><p>Is this the reason of our latency ?</p><p>How can we reduce that ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-citrix" rel="tag" title="see questions tagged &#39;citrix&#39;">citrix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/741d081def80a9559e7f252c1e6dd474?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoyo35&#39;s gravatar image" /><p><span>yoyo35</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoyo35 has no accepted answers">0%</span></p></div></div><div id="comments-container-34962" class="comments-container"><span id="35111"></span><div id="comment-35111" class="comment"><div id="post-35111-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is this the reason of our latency ?</p></blockquote><p>maybe, because the latency problem certainly has a reason. ;-))</p><blockquote><p>How can we reduce that ?</p></blockquote><p>I don't know, because doing packet analysis, based on a heavily reduced text representation of the capture file is:</p><ul><li>near to impossible</li><li>furthermore, time consuming and thus not really motivating for those you are asking for help</li><li>and ... boring</li></ul><p>;-))</p><p>So, if you want an answer that is at least close to what is (possibly) happening, you should post the capture file somewhere (google drive, dropbox, cloudshark.org). If you have concerns about privacy issues, you can anonymize the file with <a href="http://tracewrangler.com/">TraceWrangler</a>, a tool of our member <span>@Jasper</span>.</p></div><div id="comment-35111-info" class="comment-info"><span class="comment-age">(03 Aug '14, 10:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34962" class="comment-tools"></div><div class="clear"></div><div id="comment-34962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35175"></span>

<div id="answer-container-35175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35175-score" class="post-score" title="current number of votes">0</div><span id="post-35175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I don't think the Dup ACKs are causing the 5 second freeze if that's what you are asking. The 5 second freezes and Dup ACKs could have the same cause. To get a delay of 5 seconds due to a transport issue you would see either a TCP window issue or several TCP Retransmissions with significant delays between each.</p><p>I notice the client seems to be advertising a Window of 610. I guess we've missed the session start and so Wireshark doesn't have scaling info, hence the strange value. Anyway the server must think the window is bigger coz it sends 1,460 bytes.</p><p>Where was the trace data captured?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35175" class="comments-container"></div><div id="comment-tools-35175" class="comment-tools"></div><div class="clear"></div><div id="comment-35175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

