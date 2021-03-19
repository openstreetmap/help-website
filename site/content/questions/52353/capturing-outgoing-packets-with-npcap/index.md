+++
type = "question"
title = "Capturing outgoing packets with NPCAP"
description = '''I asked a similar question a few months ago and after some additional information, I think the answer is the xPCAP being used. With WinPCAP, I don&#x27;t see certain messages emanating from my computer. If I focus the capture to a particular host and ping that host, I only see the responses. The importan...'''
date = "2016-05-09T09:59:00Z"
lastmod = "2016-05-10T03:46:00Z"
weight = 52353
keywords = [ "winpcap", "missing_packets", "sent", "npcap" ]
aliases = [ "/questions/52353" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing outgoing packets with NPCAP](/questions/52353/capturing-outgoing-packets-with-npcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I asked a similar question a few months ago and after some additional information, I think the answer is the xPCAP being used. With WinPCAP, I don't see certain messages emanating from my computer. If I focus the capture to a particular host and ping that host, I only see the responses. The important information I was interested in seeing was the raw UDP traffic between my computer and the remote system (an embedded serial terminal server interface without the benefit of being able to do any captures). With WinPCAP, Wireshark did not report any UDP data transfers.</p><p>In looking through other Q&amp;A's, I saw notes to use NPCAP from the NMAP project. I downloaded NPCAP (latest version - 0.07) installed it and uninstalled WinPCAP. Using NPCAP, I was able to see all of the data - ping send/receive and UDP traffic to and from my computer. I have seen other responses that lack of sent data was due to other applications (VPN, AV, etc) interfering with the data transfer. Since NPCAP can capture and display the data, I don't believe that interference is the issue.</p><p>This was good until I rebooted my computer. After the reboot, none of my network connections were operational. I uninstalled NPCAP and the networks were operational again. In the event that the latest version of NPCAP had an issue, I removed it and installed the last version of the prior release (0.06r19). This had the same behavior.</p><p>SO, why am I posting this here instead of on the NPCAP issues site (really the NMAP site)? That site appears to be oriented towards developers. I simply want to know if other users have experienced this and/or if others have suggestions about other capture drivers that might work better. Additionally, is there any information about whether or not WinPCAP is in active support and development? There don't appear to be any version changes in the last 3 years.</p><p>Thanks,</p><p>Ed.</p></div><div id="question-tags" class="tags-container tags">winpcap missing_packets sent npcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '16, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/3445770e50fe863101eea5c5d4813e66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejhellertc&#39;s gravatar image" /><p>ejhellertc<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejhellertc has no accepted answers">0%</span></p></div></div><div id="comments-container-52353" class="comments-container"><span id="52374"></span><div id="comment-52374" class="comment"><div id="post-52374-score" class="comment-score"></div><div class="comment-text"><p>WinPcap development is effectively dead. Npcap is likely to replace WinPcap in the Wireshark installer at some point in the future.</p></div><div id="comment-52374-info" class="comment-info"><span class="comment-age">(09 May '16, 14:33)</span> grahamb ♦</div></div></div><div id="comment-tools-52353" class="comment-tools"></div><div class="clear"></div><div id="comment-52353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52389"></span>

<div id="answer-container-52389" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52389-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi @ejhellertc,</p><p>I'm the author of Npcap. Thanks for using it!</p><blockquote><p>This was good until I rebooted my computer. After the reboot, none of my network connections were operational. I uninstalled NPCAP and the networks were operational again. In the event that the latest version of NPCAP had an issue, I removed it and installed the last version of the prior release (0.06r19). This had the same behavior.</p></blockquote><p>There are a few cases reporting that network disconnection fails after installing Npcap. But this disconnection will be gone after 1) wait for 90 seconds, or 2) disable and re-enable the adapter icon in ncpa.cpl, or 3) reboot.</p><p>You said your system won't connect to network after reboot. Have you tried 1) or 2)?</p><p>I suspect it's because you have installed some incompatible software. It can be VPN, anti-virus, firewall or other network related software. We are maintaining an incompatible software list at the bottom of <a href="https://github.com/nmap/npcap">https://github.com/nmap/npcap</a>. So you can uninstall all those potential softwares one by one. And see which one causes the issue. Then report it to me.</p><blockquote><p>SO, why am I posting this here instead of on the NPCAP issues site (really the NMAP site)? That site appears to be oriented towards developers. I simply want to know if other users have experienced this and/or if others have suggestions about other capture drivers that might work better. Additionally, is there any information about whether or not WinPCAP is in active support and development? There don't appear to be any version changes in the last 3 years.</p></blockquote><p>The best place to fire an issue about Npcap is at GitHub Issues of Nmap: <a href="https://github.com/nmap/nmap/issues">https://github.com/nmap/nmap/issues</a>. You can also post the question here, but it may be slow to be handled because I won't be notified as @sindy said.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-52389" class="comments-container"><span id="52396"></span><div id="comment-52396" class="comment"><div id="post-52396-score" class="comment-score"></div><div class="comment-text"><p>I retried Npcap. During the installation, I did not enable the start on boot option. This may have effectively performed the "Wait 90 seconds", as my other network connections come up now. WS runs and captures all the data I need. The delay to load the driver when WS starts (if it does) does not seem appreciable.</p><p>I also read somewhere that there is a limit on the number of hooks or filters that Win7 can handle. I had some duplicate MS VPN connections which I removed. I am not sure, but that may have helped as well.</p><p>Thanks, Ed.</p></div><div id="comment-52396-info" class="comment-info"><span class="comment-age">(10 May '16, 08:53)</span> ejhellertc</div></div></div><div id="comment-tools-52389" class="comment-tools"></div><div class="clear"></div><div id="comment-52389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52370"></span>

<div id="answer-container-52370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52370-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Since NPCAP can capture and display the data, I don't believe that interference is the issue.</p></blockquote><p>Although it may be hard to believe, the interference really is the issue. The point is that WinPcap and NPcap hook as "filters" (actually filtering out no packets but only using the API intended for packet filters) to the software stack between the NIC driver and the higher protocol layers, but each of them hooks in at a different layer. The filters of those security software products hook to the same places too, sometimes "bridging over" the WinPcap's "filter" in one or both directions. So if such a (carelessly implemented) security software's driver hooks at the same level like WinPcap does, NPcap may still see the frames (and probably vice versa, there's not much security software hooking in at Ndis 6 yet).</p><p>NPcap is a work in progress and more or less a one-man show. But that one man, @Yang Luo, is really responsive, so if you have an issue with NPcap, the best thing to do is to open an issue at that "developer-oriented" site and provide the information. Woes on loosely related sites are much less efficient (as it takes Yang Luo longer to notice them).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '16, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '16, 13:39</p></div></div><div id="comments-container-52370" class="comments-container"></div><div id="comment-tools-52370" class="comment-tools"></div><div class="clear"></div><div id="comment-52370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

