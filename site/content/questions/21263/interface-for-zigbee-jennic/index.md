+++
type = "question"
title = "Interface for Zigbee (jennic)"
description = '''Dear Sir, I have wireless sensor network which work on IEEE 802.15.4 which i use Jennic JN51349 evaluation board I set the microcontroller as sniffer, and i run the sniffer server, and then i make an interface ( Microsoft Loopback adapter) but when I running the wireshark for capture and analyze the...'''
date = "2013-05-19T08:10:00Z"
lastmod = "2013-05-20T04:16:00Z"
weight = 21263
keywords = [ "zigbee", "interface" ]
aliases = [ "/questions/21263" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Interface for Zigbee (jennic)](/questions/21263/interface-for-zigbee-jennic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21263-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir,</p><p>I have wireless sensor network which work on IEEE 802.15.4 which i use Jennic JN51349 evaluation board</p><p>I set the microcontroller as sniffer, and i run the sniffer server, and then i make an interface ( Microsoft Loopback adapter)</p><p>but when I running the wireshark for capture and analyze the data,, I got no data capture by wire shark when I see the interface details, there is no packet received</p><p>why it happened? is there any wrong setting that i set?</p><p>thanks a lot best Regards</p></div><div id="question-tags" class="tags-container tags">zigbee interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/e7724b9d2f3ac05e7e1bfadf18b0e53e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paxdhe&#39;s gravatar image" /><p>paxdhe<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paxdhe has no accepted answers">0%</span></p></div></div><div id="comments-container-21263" class="comments-container"></div><div id="comment-tools-21263" class="comment-tools"></div><div class="clear"></div><div id="comment-21263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21301"></span>

<div id="answer-container-21301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21301-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I presume you are using the Jennic plugin for Wireshark as detailed in their <a href="http://www.jennic.com/files/support_documentation/JN-AN-1115-Protocol-Sniffer-with-Wireshark.pdf">Application Note AN1115</a>?</p><p>Are you sure you are using the correct version of Wireshark (1.6.5) and have set up your system exactly as described in the AN? Did you follow the guidance in the note:</p><p><em>Note: The loopback adaptor will not become visible in Wireshark until after Windows has been rebooted.</em></p><p>What version of WinPCap do you have installed? WinPCap is responsible for providing the interface list and performing the capture and may have changed if you aren't using the version distributed with Wireshark 1.6.5.</p><p>You may have more success asking your question in the Jennic (NXP) forums as the plugin is their code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21301" class="comments-container"><span id="21346"></span><div id="comment-21346" class="comment"><div id="post-21346-score" class="comment-score"></div><div class="comment-text"><p>I follow the note AN-1115</p><p>the Ms loopback adapter visible in wireshark,</p><p>but when I check the status in Loopback adapter the sent but not received to</p><p>how can?</p><p>I try ask in NXP jennic forum,, and follow the instruction,, but not succed,, no data received into loopback adapter</p><p>thanks</p></div><div id="comment-21346-info" class="comment-info"><span class="comment-age">(21 May '13, 08:17)</span> paxdhe</div></div><span id="21347"></span><div id="comment-21347" class="comment"><div id="post-21347-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Are you running any AV or VPN software on the capturing machine? They have been found in the past to interfere with capturing.</p></div><div id="comment-21347-info" class="comment-info"><span class="comment-age">(21 May '13, 09:12)</span> grahamb ♦</div></div><span id="21365"></span><div id="comment-21365" class="comment"><div id="post-21365-score" class="comment-score"></div><div class="comment-text"><p>sorry,</p><p>how to rebooted the capturing machine?</p><p>I use Wireshark 1.9.2</p><p>I have few VPn connection ,, when I running the wire shark I try to disable the LAN ethernet and Wireless Ethernet</p><p>So, what are the problem in my setup ?</p></div><div id="comment-21365-info" class="comment-info"><span class="comment-age">(22 May '13, 00:23)</span> paxdhe</div></div><span id="21366"></span><div id="comment-21366" class="comment"><div id="post-21366-score" class="comment-score"></div><div class="comment-text"><p>@paxdhe, Yet again I have had to convert your "answer" to a comment, please take time to read the FAQ and learn to use this site to your best advantage.</p><p>Your best chance of success is to follow the instructions in AN-1115 <strong>exactly</strong> as written. That means using Wireshark 1.6.5, rebooting the XP machine after adding the Loopback Adaptor and all the other fine instructions in the Application note.</p></div><div id="comment-21366-info" class="comment-info"><span class="comment-age">(22 May '13, 01:16)</span> grahamb ♦</div></div></div><div id="comment-tools-21301" class="comment-tools"></div><div class="clear"></div><div id="comment-21301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21292"></span>

<div id="answer-container-21292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21292-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and then i make an interface ( Microsoft Loopback adapter)</p></blockquote><p>WinPcap cannot (properly) capture traffic on a loopback interface.</p><blockquote><p><a href="http://www.winpcap.org/misc/faq.htm#Q-13">http://www.winpcap.org/misc/faq.htm#Q-13</a><br />
<a href="http://wiki.wireshark.org/CaptureSetup/Loopback">http://wiki.wireshark.org/CaptureSetup/Loopback</a></p></blockquote><p>You can try to capture the traffic with <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> then use Wireshark to analyze it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21292" class="comments-container"><span id="21350"></span><div id="comment-21350" class="comment"><div id="post-21350-score" class="comment-score"></div><div class="comment-text"><p>Can You Guide Me how to use Microsoft Neetwork monitor,, then analyze it with wireshark?</p><p>Thanks Best regards</p></div><div id="comment-21350-info" class="comment-info"><span class="comment-age">(21 May '13, 10:49)</span> paxdhe</div></div><span id="21357"></span><div id="comment-21357" class="comment"><div id="post-21357-score" class="comment-score"></div><div class="comment-text"><p>@paxdhe,</p><p>Your "answer" has been converted to a comment (again) as that's how this site works. Please read the FAQ for more information.</p><p>You'll find operating instructions for Network Monitor on the Microsoft site. Make the required capture and save it from NM and then open the capture in Wireshark.</p><p>You didn't answer the questions in my answer above:</p><p>Are you using the correct version of Wireshark (1.6.5)? Have you rebooted the capturing machine after adding the loopback adaptor? Do you have any AV or VPN software running on the capturing machine?</p></div><div id="comment-21357-info" class="comment-info"><span class="comment-age">(21 May '13, 15:17)</span> grahamb ♦</div></div></div><div id="comment-tools-21292" class="comment-tools"></div><div class="clear"></div><div id="comment-21292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

