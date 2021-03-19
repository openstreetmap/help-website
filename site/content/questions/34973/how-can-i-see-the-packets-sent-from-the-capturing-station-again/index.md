+++
type = "question"
title = "how can i see the packets sent from the capturing station again?"
description = '''Trying to compare send and receive times between a workstation and a remote server to determine the cause of an issue with file transfer times. Recently upgraded a dot release to Version 1.10.8 at both ends (v1.10.8-2-g52a5244 from master-1.10 is on the server) and I cannot see the source packets of...'''
date = "2014-07-29T10:13:00Z"
lastmod = "2014-08-03T10:19:00Z"
weight = 34973
keywords = [ "capture-options", "packet-capture", "capture-setup" ]
aliases = [ "/questions/34973" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can i see the packets sent from the capturing station again?](/questions/34973/how-can-i-see-the-packets-sent-from-the-capturing-station-again)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34973-score" class="post-score" title="current number of votes">0</div><span id="post-34973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to compare send and receive times between a workstation and a remote server to determine the cause of an issue with file transfer times.</p><p>Recently upgraded a dot release to Version 1.10.8 at both ends (v1.10.8-2-g52a5244 from master-1.10 is on the server) and I cannot see the source packets of the workstation.</p><p>I can see both the source and the replies from the server but not the workstation.</p><p>I tried again with the Version 1.12.0rc3 (v1.12.0rc3-0-ge14d5b6 from master-1.12) on the workstation but no luck.</p><p>Workstation: Running on 64-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 3.1.22, Gcrypt 1.6.0, without AirPcap. Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz, with 8032MB of physical memory.</p><p>Server: Running on 64-bit Windows Server 2008 R2 Service Pack 1, build 7601, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.12.18, Gcrypt 1.4.6, without AirPcap. Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz, with 4095MB of physical memory.</p><p>I need this in order to compare times and determine that it is an endpoint problem and not a firewall problem.</p><p>I'm hoping it's something simple. Can you help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-options" rel="tag" title="see questions tagged &#39;capture-options&#39;">capture-options</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '14, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/be5a385942209542cd67838ed05285ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdesoucey&#39;s gravatar image" /><p><span>jdesoucey</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdesoucey has no accepted answers">0%</span></p></div></div><div id="comments-container-34973" class="comments-container"></div><div id="comment-tools-34973" class="comment-tools"></div><div class="clear"></div><div id="comment-34973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35106"></span>

<div id="answer-container-35106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35106-score" class="post-score" title="current number of votes">0</div><span id="post-35106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm hoping it's something simple. Can you help?</p></blockquote><p>Maybe. I guess it's some kind of security software on your client like: AV, Firewall, Endpoint Security, VPN client, etc. Disable or uninstall that kind of software and it should work.</p><p>We have had several similar reports in the past. Please read the Q&amp;A of similar problems reported here:</p><blockquote><p><a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '14, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35106" class="comments-container"></div><div id="comment-tools-35106" class="comment-tools"></div><div class="clear"></div><div id="comment-35106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

