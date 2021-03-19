+++
type = "question"
title = "DHCP Discover and Request packets not captured"
description = '''I have a problem similar (if not identical) to https://ask.wireshark.org/questions/22194/dhcp-broadcast-packets-not-displayed . I am capturing packets from a Cisco SPAN port and watching a MacBook Pro perform a Netboot (BSDP, Apple&#x27;s version of PXE booting). I have Wireshark Version 1.12.4 (v1.12.4-...'''
date = "2015-04-29T15:14:00Z"
lastmod = "2015-05-04T13:56:00Z"
weight = 41955
keywords = [ "dhcp", "request", "discover" ]
aliases = [ "/questions/41955" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP Discover and Request packets not captured](/questions/41955/dhcp-discover-and-request-packets-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41955-score" class="post-score" title="current number of votes">0</div><span id="post-41955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem similar (if not identical) to <a href="https://ask.wireshark.org/questions/22194/dhcp-broadcast-packets-not-displayed">https://ask.wireshark.org/questions/22194/dhcp-broadcast-packets-not-displayed</a> . I am capturing packets from a Cisco SPAN port and watching a MacBook Pro perform a Netboot (BSDP, Apple's version of PXE booting).</p><p>I have Wireshark Version 1.12.4 (v1.12.4-0-gb4861da from master-1.12) on Windows 7 64 bit, with WinPcap 4.1.3.</p><p>If I perform the capture using a Linux box with tcpdump (a simple "tcpdump -i eth0 -s 0 -w mac-bsdp.pcap ether host d4:9a:20:xx:xx:xx") the full DHCP DORA is visible in the resulting file when read into Wireshark on Windows.</p><p>If I attempt to capture directly on the Windows box however, the DHCP Discover and Request packets do not appear to ever be captured. Other broadcasts from the device (ARPs for example) are captured.</p><p>I am not sure where to go next to troubleshoot the problem from here. I understood that WinPcap is lower in the network stack than most (all?) of the things suggested in the previous posting (VPN clients, AV, Firewalls, etc), and so turning them on or off I would think would not impact Wireshark's capture.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-discover" rel="tag" title="see questions tagged &#39;discover&#39;">discover</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '15, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/b7893991fae6dcd827d0b77c36e13d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustineas&#39;s gravatar image" /><p><span>augustineas</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustineas has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '15, 15:48</strong> </span></p></div></div><div id="comments-container-41955" class="comments-container"></div><div id="comment-tools-41955" class="comment-tools"></div><div class="clear"></div><div id="comment-41955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42064"></span>

<div id="answer-container-42064" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42064-score" class="post-score" title="current number of votes">0</div><span id="post-42064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="augustineas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it appears you are correct, at least in part. I tried disabling the three most likely culprits, "VirtualBox Bridged Networking Driver", "Cisco AnyConnect Network Access Filter Driver", and "Sophos Client Firewall NDIS packet filter", and sure enough it started capturing properly.</p><p>However, in order to determine which one was the actual culprit, I enabled them one by one. The captures continued to work properly after enabling each one. So now they are all re-enabled, and it still appears to capture properly.</p><p>Clearly something was not working properly in the stack, and disabling and re-enabling those features fixed it. All without a reboot.</p><p>Very strange.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '15, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/b7893991fae6dcd827d0b77c36e13d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustineas&#39;s gravatar image" /><p><span>augustineas</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustineas has one accepted answer">100%</span></p></div></div><div id="comments-container-42064" class="comments-container"></div><div id="comment-tools-42064" class="comment-tools"></div><div class="clear"></div><div id="comment-42064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41973"></span>

<div id="answer-container-41973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41973-score" class="post-score" title="current number of votes">1</div><span id="post-41973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>(VPN clients, VA, Firewalls, etc), and so turning them on or off <strong>I would think would not impact Wirehair's capture.</strong></p></blockquote><p>That's not necessarily the case, at least you can't tell for sure unless you know exactly where every piece of security software hooks itself into the TCP/IP stack.</p><p>Did you try to eliminate all security/network related software packages on your Windows system? If no: please do so, as that's the most likely reason for the effect you are seeing.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41973" class="comments-container"><span id="42065"></span><div id="comment-42065" class="comment"><div id="post-42065-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So now they are all re-enabled, and it still appears to capture properly.</p></blockquote><p>The order in which each product has been "inserted" into the stack might have an influence on this as well...</p></div><div id="comment-42065-info" class="comment-info"><span class="comment-age">(04 May '15, 13:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41973" class="comment-tools"></div><div class="clear"></div><div id="comment-41973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

