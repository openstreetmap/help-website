+++
type = "question"
title = "dumpcap and wireshark only capture the first three packets of every tcp stream"
description = '''I have a win2003 server with two HP NC382i DP network controllers [v5.2.17.0] working as a team (Network Teaming Intermediate Driver NTID) [CPQTEAM.sys v9.90.1.0) I execute a web service test from a Win7 client. If I capture on the server (with wireshark or with dumpcap) I only capture the first 3 p...'''
date = "2013-10-22T08:22:00Z"
lastmod = "2013-10-23T03:58:00Z"
weight = 26288
keywords = [ "win2003", "ntid", "teaming" ]
aliases = [ "/questions/26288" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap and wireshark only capture the first three packets of every tcp stream](/questions/26288/dumpcap-and-wireshark-only-capture-the-first-three-packets-of-every-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26288-score" class="post-score" title="current number of votes">0</div><span id="post-26288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a win2003 server with two HP NC382i DP network controllers [v5.2.17.0] working as a team (Network Teaming Intermediate Driver NTID) [CPQTEAM.sys v9.90.1.0)</p><p>I execute a web service test from a Win7 client.</p><p>If I capture on the server (with wireshark or with dumpcap) I only capture the first 3 packets of every TCP socket. They are always [SYN], [SYN, ACK] and [ACK] If I capture on the client (Win7) I can see all the expected packets of the socket (6 typically)</p><p>Also, if the socket is pre-established (there is not 3 way hashake), on the server I can not capture any packet, but in the client I can.</p><p>Is there any limitation with the network cards or the teaming configuration I have?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win2003" rel="tag" title="see questions tagged &#39;win2003&#39;">win2003</span> <span class="post-tag tag-link-ntid" rel="tag" title="see questions tagged &#39;ntid&#39;">ntid</span> <span class="post-tag tag-link-teaming" rel="tag" title="see questions tagged &#39;teaming&#39;">teaming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/e0ca40365e0601cbfef67d5c9b7d27f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chirrin%20Dul%20Ari&#39;s gravatar image" /><p><span>Chirrin Dul Ari</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chirrin Dul Ari has no accepted answers">0%</span></p></div></div><div id="comments-container-26288" class="comments-container"></div><div id="comment-tools-26288" class="comment-tools"></div><div class="clear"></div><div id="comment-26288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26289"></span>

<div id="answer-container-26289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26289-score" class="post-score" title="current number of votes">2</div><span id="post-26289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If I capture on the server (with wireshark or with dumpcap) I only capture the first 3 packets of every TCP socket. <strong>They are always [SYN], [SYN, ACK] and [ACK]</strong></p></blockquote><p>That's most certainly due to <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">TCP offloading into the NIC driver</a>. The connection setup is handled by OS and the rest of the TCP connection is offloaded into the NIC driver. So, if you want to capture the whole connection on the server, you would have to disable TCP offloading. <strong>But</strong> is that really worth doing, just to be able to capture on the server? I suggest to capture on a <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">mirror/monitor port of the switch</a> instead.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '13, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '13, 08:34</strong> </span></p></div></div><div id="comments-container-26289" class="comments-container"><span id="26313"></span><div id="comment-26313" class="comment"><div id="post-26313-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt. Probably you are right, but still I don't understand why wireshark cannot see the packet containing application data (CPU work I guess), but can see TCP handshaking (Network Card work).</p><p>As you suggest, it is better to leave the server (in production) as is configured and try to capture traffic from another point.</p><p>Thank you.</p></div><div id="comment-26313-info" class="comment-info"><span class="comment-age">(23 Oct '13, 00:49)</span> <span class="comment-user userinfo">Chirrin Dul Ari</span></div></div><span id="26316"></span><div id="comment-26316" class="comment"><div id="post-26316-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but still I don't understand why wireshark cannot see the packet containing application data (CPU work I guess), but can see TCP handshaking (Network Card work).</p></blockquote><p>That's because of the way WinPcap (the capture library on Windows) is 'attached' to the TCP/IP stack. Please read the following:</p><blockquote><p><a href="http://www.winpcap.org/docs/docs_41b5/html/group__NPF.html">http://www.winpcap.org/docs/docs_41b5/html/group__NPF.html</a></p></blockquote></div><div id="comment-26316-info" class="comment-info"><span class="comment-age">(23 Oct '13, 03:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26289" class="comment-tools"></div><div class="clear"></div><div id="comment-26289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

