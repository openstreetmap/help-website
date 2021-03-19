+++
type = "question"
title = "NTP responses are not shown by Wireshark once added to NLB"
description = '''I have two servers running Windows Server 2008; both are running with a third party NTP server. Before adding the server to NLB, when I send NTP requests to the server&#x27;s IP address I could see request and response in Wireshark. Whereas once I add the server to NLB and when I hit the NTP request to N...'''
date = "2014-11-19T21:04:00Z"
lastmod = "2014-11-20T01:38:00Z"
weight = 37988
keywords = [ "ntp", "nlb", "outbound", "wireshark" ]
aliases = [ "/questions/37988" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [NTP responses are not shown by Wireshark once added to NLB](/questions/37988/ntp-responses-are-not-shown-by-wireshark-once-added-to-nlb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two servers running Windows Server 2008; both are running with a third party NTP server.</p><p>Before adding the server to NLB, when I send NTP requests to the server's IP address I could see request and response in Wireshark. Whereas once I add the server to NLB and when I hit the NTP request to NLB IP, I could see only the NTP requests hitting the server and there were no NTP responses shown in Wireshark. Meanwhile with another packet capturing tool (Microsoft Network Monitoring tool) I could see both request and response for all NTP packets. Also the NTP server's log shows both request and response.</p><ol><li>Microsoft Net Mon Capture - <a href="https://www.dropbox.com/s/um8ijkn1v25w9nf/Net%20Mon%20Capture.JPG?dl=0">https://www.dropbox.com/s/um8ijkn1v25w9nf/Net%20Mon%20Capture.JPG?dl=0</a></li><li>NTP Software Log - <a href="https://www.dropbox.com/s/a97h6jip709z8p9/NTP%20Software%20Log.JPG?dl=0">https://www.dropbox.com/s/a97h6jip709z8p9/NTP%20Software%20Log.JPG?dl=0</a></li><li>Wireshark Capture - <a href="https://www.dropbox.com/s/wnarmznip9i9smb/Wireshark%20Capture.JPG?dl=0">https://www.dropbox.com/s/wnarmznip9i9smb/Wireshark%20Capture.JPG?dl=0</a></li></ol><p>Compare the timing across all the three pics. At 12:30:12 PM there is an incoming NTP request from 10.238.59.3(Client) hitting 10.238.160.1 (NLB IP address) and there were no response shown in Wireshark but the response can be seen in both NTP server trace and in NetMon tool trace.</p><p>Same can be found for subsequent requests as well.</p><p>Initially I tried with Wireshark v1.10.7 and later I checked with 1.12.x (which seems to be the latest version) but didn't help.</p><p>Note: I have 2 interfaces in server but one NIC is disabled.</p><p>Let me know if this is a bug with Wireshark. If not kindly give me suggestion to get the responses in Wireshark.</p><p>Thanks, Ashok Prabhu. J</p></div><div id="question-tags" class="tags-container tags">ntp nlb outbound wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 21:04</strong></p><img src="https://secure.gravatar.com/avatar/c978e60d67d544bbfad832d3481b3dba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashok&#39;s gravatar image" /><p>Ashok<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashok has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '14, 01:38</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-37988" class="comments-container"></div><div id="comment-tools-37988" class="comment-tools"></div><div class="clear"></div><div id="comment-37988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38000"></span>

<div id="answer-container-38000" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38000-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Let me know if this is a bug with Wireshark. If not kindly give me suggestion to get the responses in Wireshark.</p></blockquote><p>No, this is not a bug, it's a "limitation" of WinPcap (the capturing sub-system of Wireshark). It is related to the way WinPcap is inserted into the kernel to capture frames. If anything in the kernel "removes" the frames before WinPcap is able to see them, then you won't see anything in Wireshark. This is a known issue and is being reported for a some security software as well (VPN clients, AV, IDS/IPS, Endpoint Security, etc.).</p><p>See here:</p><blockquote><p><a href="https://ask.wireshark.org/tags/outbound/">https://ask.wireshark.org/tags/outbound/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38000" class="comments-container"><span id="38001"></span><div id="comment-38001" class="comment"><div id="post-38001-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your prompt response. Let me go through other posts and come back if I have any questions. Till then let the post be open.</p><p>Regards, Ashok Prabhu. J</p></div><div id="comment-38001-info" class="comment-info"><span class="comment-age">(20 Nov '14, 01:45)</span> Ashok</div></div><span id="38003"></span><div id="comment-38003" class="comment"><div id="post-38003-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Let me go through other posts and come back if I have any questions.</p></blockquote><p>If you are looking for a solution, I have bad news for you. There is no solution, except uninstalling the "offending" software, which would be kind of "tricky" in the case of NLB ;-)</p><p>So, your option is: Capture the traffic with Microsoft Network Monitor, if that works with NLB, and do the analysis with Wireshark.</p></div><div id="comment-38003-info" class="comment-info"><span class="comment-age">(20 Nov '14, 01:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38000" class="comment-tools"></div><div class="clear"></div><div id="comment-38000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

