+++
type = "question"
title = "check RFC compliance with Wireshark / tcpdump ?"
description = '''hi guys, is Wireshark / tcpdump able to detect / mark non RFC compliant mails ??  I&#x27;m asking because the following document is stating that: To verify if the mail is corrupted it is advised to contact Technical support to enable RAW mail logging and create a network capture with tcpdump. https://sup...'''
date = "2016-01-05T06:15:00Z"
lastmod = "2016-01-05T08:11:00Z"
weight = 48866
keywords = [ "rfc", "mail", "tcpdump" ]
aliases = [ "/questions/48866" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [check RFC compliance with Wireshark / tcpdump ?](/questions/48866/check-rfc-compliance-with-wireshark-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>is Wireshark / tcpdump able to detect / mark non RFC compliant mails ??</p><p>I'm asking because the following document is stating that:</p><p>To verify if the mail is corrupted it is advised to contact Technical support to enable RAW mail logging <strong>and create a network capture with tcpdump.</strong></p><p><a href="https://support.symantec.com/en_US/article.TECH184271.html">https://support.symantec.com/en_US/article.TECH184271.html</a></p><p>Thank you in advance !</p><p>BR ADAM</p></div><div id="question-tags" class="tags-container tags">rfc mail tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '16, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-48866" class="comments-container"></div><div id="comment-tools-48866" class="comment-tools"></div><div class="clear"></div><div id="comment-48866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48873"></span>

<div id="answer-container-48873" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48873-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No: Wireshark does not check RFC compliance for emails (altho a dissection of same might fail).</p><p>(I expect that tcpdump (a completely different program than wireshark) also does not check for RFC compliance, but I don't actually know that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '16, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-48873" class="comments-container"><span id="48888"></span><div id="comment-48888" class="comment"><div id="post-48888-score" class="comment-score">1</div><div class="comment-text"><p>I would understand that requirement in such a way that Symantec just wants to have a bit-verbatim capture of the complete SMTP protocol exchange related to reception of the e-mail message in question, not that they would themselves use Wireshark to automatically verify the RFC compliance.</p><p>For that purpose, Wireshark (actually, dumpcap) is equally good as the tcpdump, as both capture network traffic and store it into a pcap or pcapng organised file.</p><p>If I read the article properly, Symantec wants <em>both</em> the pcap and their internal application log of the same transaction, and to switch the logging mode to "raw", you have to contact their support staff.</p><p>As @Bill Meier has stated, if Wireshark dissection of an e-mail message from the SMTP capture fails, it is quite likely that the message breaks some RFC in some way (assuming there is no packet loss); however, the fact that the dissection succeeds does not imply that there is no breach of some of the related RFCs.</p><p>As with recent hardware, capturing of TCP sessions may be affected by TCP offloading, I'd recommend to search this site for "tcp chimney" and "tcp offloading" keywords before attempting the capture.</p></div><div id="comment-48888-info" class="comment-info"><span class="comment-age">(05 Jan '16, 14:45)</span> sindy</div></div><span id="48900"></span><div id="comment-48900" class="comment"><div id="post-48900-score" class="comment-score"></div><div class="comment-text"><p>@Sindy I see your points.</p><p>So I would have to capture on their server on the receiving interface, correct ?</p><p>I'm partially aware of tcp chimney / offloading (e.g. checksum errors ) but other than that would it be a general rule to switch off this features for the time when doing the capture or is it "enough" to keep in the back of the head that it can cause errors but in fact this are not real errors ?</p><p>thank you</p><p>BR Adam</p></div><div id="comment-48900-info" class="comment-info"><span class="comment-age">(06 Jan '16, 03:36)</span> adasko</div></div><span id="48901"></span><div id="comment-48901" class="comment"><div id="post-48901-score" class="comment-score">1</div><div class="comment-text"><p>Adam,</p><p>from the description the role of "your" and "their" is not really clear.</p><p>I've understood it in such a way that you are running a Symantec software product at your own hardware (which may be a virtual one). If so, it seems that to get support from Symantec, you have to capture on your server running their product using tcpdump (not available at Windows) or Wireshark (available almost at all OSes) <em>and</em> ask their support to activate/tell you how to activate the RAW logging, whatever it means, before starting the capture and sending a test e-mail message whose processing should fail the way you've encountered.</p><p>As for the offloading: its purpose is to save the CPU power for better purposes, and there is a significant difference between "checksum offloading" and other types of offloading:</p><ul><li><p>you don't need to bother about <em>checksum</em> offloading if you keep in back of your head that you can ignore incorrect checksums of sent packets because they haven't been calculated yet at the moment when Wireshark has got the packet, while incorrect checksums of packets not sent by the card on which you run the capture indicate a trouble.</p></li><li><p>full tcp offloading prevents Wireshark from seeing the TCP session at all, except its establishment phase, so if your network adapter supports this feature and you want to capture TCP, you must deactivate the feature in order to be able to make a useful capture. The price you pay is the CPU power assigned to TCP handling, so it is up to you whether you'll keep the feature disabled systematically or only deactivate it while troubleshooting.</p></li></ul><p>To eventually troubleshoot the TCP offloading itself (which could theoretically also be related to your trouble) you must capture somewhere else (search this site for capturing using hubs, taps, monitoring ports of switches...). I mean, if you deactivate TCP offloading so that you could capture, and your original issue disappears, then there likely is an issue with the TCP offloading.</p></div><div id="comment-48901-info" class="comment-info"><span class="comment-age">(06 Jan '16, 03:57)</span> sindy</div></div><span id="48902"></span><div id="comment-48902" class="comment"><div id="post-48902-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy,</p><p>sorry for the confusion. Yes, we have their product (Symantec Encryption Management Server) installed on a virtual machine (VMware).</p><p>As for the offloading: its purpose is to save the CPU power for better purposes, and there is a significant difference between "checksum offloading"</p><p>So in general, the idea behind offloading is to save hosts CPU, correct?</p><p>Please tell only, if it's a VM do i have to check the NIC settings of the VM itself or the VMware host's physical interface or both ?</p><p>BR</p><p>Adam</p></div><div id="comment-48902-info" class="comment-info"><span class="comment-age">(06 Jan '16, 04:59)</span> adasko</div></div><span id="48905"></span><div id="comment-48905" class="comment"><div id="post-48905-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if it's a VM do i have to check the NIC settings of the VM itself or the VMware host's physical interface or both?</p></blockquote><p>Only of one of them - the one at which you capture using Wireshark. I'd suppose no offload feature on a virtual machine as it is not much logical but better check.</p><p>Off topic: the "thumbs up" icon next to the Answer marks the answer as "nice" or "useful" and is available to any user, but it doesn't change the Question status. To mark the Answer as "accepted" so that the Question appears as "usefully answered" (i.e. green) in the list, you have to use the checkmark icon, and you (the issuer of the question) are the only one who can do it. I have no idea why it is made so complex but it is.</p></div><div id="comment-48905-info" class="comment-info"><span class="comment-age">(06 Jan '16, 05:40)</span> sindy</div></div></div><div id="comment-tools-48873" class="comment-tools"></div><div class="clear"></div><div id="comment-48873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

