+++
type = "question"
title = "Wireshark does not capture packets w/ payloads?"
description = '''I have a very strange issue with wireshark that I&#x27;ve never seen before, and have been using Wireshark/Ethereal for some time now. This issue only occurs on one particular server. I am able to run Wireshark without an issue and I can see the proper interface listed and capture from it. The window fil...'''
date = "2012-07-30T13:32:00Z"
lastmod = "2012-08-08T12:59:00Z"
weight = 13131
keywords = [ "windows", "capture", "length", "payload", "packet" ]
aliases = [ "/questions/13131" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark does not capture packets w/ payloads?](/questions/13131/wireshark-does-not-capture-packets-w-payloads)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13131-score" class="post-score" title="current number of votes">0</div><span id="post-13131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very strange issue with wireshark that I've never seen before, and have been using Wireshark/Ethereal for some time now.</p><p>This issue only occurs on one particular server. I am able to run Wireshark without an issue and I can see the proper interface listed and capture from it. The window fills with both broadcast and unicast messages, both sourced from and destined for the interface from which I'm capturing. The issue is that none of the packets with any length coming from or to the PC are displayed (broadcast/flooded packets with payload are still displayed)... it's the strangest thing. The output in the capture window is as if I have a filter running that excludes len&gt;0 packets. Right-clicking and following any particular stream will show nothing- only TCP ack/syn/etc packets but nothing with the PSH flag, no data, etc.</p><p>I know for a fact that there <em>is</em> data being received/sent. To prove this I have a second PC capture from a span port that is mirroring traffic to/from the server's interface. On Wireshark on the second PC, the capture window is filled with the same broadcast/flooded traffic that the host sees however it also sees all of the expected unicast traffic that I thought I would see on the server.</p><p>Any thoughts? Drivers? I've already removed and re-installed Wireshark several times and tried different capture settings to no avail.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '12, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/4ab0941e59a6111afbb2179a88a9e213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varanda&#39;s gravatar image" /><p><span>varanda</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varanda has no accepted answers">0%</span></p></div></div><div id="comments-container-13131" class="comments-container"><span id="13133"></span><div id="comment-13133" class="comment"><div id="post-13133-score" class="comment-score"></div><div class="comment-text"><p>If it helps:</p><p>OS is Windows 2008 R2</p><p>NIC is Broadcom BCM5709C NetXtreme II GigE with driver 6.2.9.0, dated 2/4/2011</p></div><div id="comment-13133-info" class="comment-info"><span class="comment-age">(30 Jul '12, 13:44)</span> <span class="comment-user userinfo">varanda</span></div></div></div><div id="comment-tools-13131" class="comment-tools"></div><div class="clear"></div><div id="comment-13131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13134"></span>

<div id="answer-container-13134" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13134-score" class="post-score" title="current number of votes">1</div><span id="post-13134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="varanda has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That specific NIC supports TCP/IP offloading. Depending on the offloading capabilities, you won't see established TCP Connections with WinPcap (Wireshark).</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Offloading#TCP_Chimney</code><br />
</p></blockquote><p>Try to disable TCP Chimney, as described in the link above. If that does not help, try to disable TCP/IP offloading in the driver (driver advanced settings, or some 'obscure' registry settings -&gt; google). Look for something like "TCP Connection Offload".</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '12, 14:00</strong> </span></p></div></div><div id="comments-container-13134" class="comments-container"><span id="13137"></span><div id="comment-13137" class="comment"><div id="post-13137-score" class="comment-score"></div><div class="comment-text"><p>Sounds like a good idea to try. I'll check it out and update when I can verify.</p><p>FYI I would see the new connections establish and close- just nothing in between.</p></div><div id="comment-13137-info" class="comment-info"><span class="comment-age">(30 Jul '12, 14:26)</span> <span class="comment-user userinfo">varanda</span></div></div><span id="13477"></span><div id="comment-13477" class="comment"><div id="post-13477-score" class="comment-score"></div><div class="comment-text"><p>Just FYI Kurt, I did fix the issue based on your recommendation but the netsh command in that link was not available (specifically the "chimney" subcommand).</p><p>I went into the NIC properties via Device Manager, and found TCP connection offloading for IPv4 and disabled it. Server dropped connections for 10-15 seconds as I would expect, and then resumed operation as normal. Now Wireshark can see the traffic it was not able to see before. Thanks!</p></div><div id="comment-13477-info" class="comment-info"><span class="comment-age">(08 Aug '12, 12:49)</span> <span class="comment-user userinfo">varanda</span></div></div><span id="13478"></span><div id="comment-13478" class="comment"><div id="post-13478-score" class="comment-score"></div><div class="comment-text"><p>thanks for the update!</p></div><div id="comment-13478-info" class="comment-info"><span class="comment-age">(08 Aug '12, 12:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-13134" class="comment-tools"></div><div class="clear"></div><div id="comment-13134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

