+++
type = "question"
title = "Unable to take RDP"
description = '''Hi, I am trying to RDP a computer(115.112.218.144) on Internet and its not working. My computer(192.168.168.65) is going through a sonicwall firewall  Firewall LAN IP: 192.168.168.168 Firewall WAN IP: 192.168.1.5 Modem is having public IP. Source: 192.168.168.65 Destination: 115.112.218.144 I did a ...'''
date = "2014-06-22T01:38:00Z"
lastmod = "2014-06-22T04:30:00Z"
weight = 34030
keywords = [ "tcppackets" ]
aliases = [ "/questions/34030" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to take RDP](/questions/34030/unable-to-take-rdp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34030-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to RDP a computer(115.112.218.144) on Internet and its not working.</p><p>My computer(192.168.168.65) is going through a sonicwall firewall</p><p>Firewall LAN IP: 192.168.168.168 Firewall WAN IP: 192.168.1.5 Modem is having public IP.</p><p>Source: 192.168.168.65 Destination: 115.112.218.144</p><p>I did a packet capture on my sonicwall firewall and found that SYN is sent from 192.168.168.65 to 115.112.218.144, SYN_ACK received from 115.112.218.144 to 192.168.168.65 and then immediately RST,ACK is received from 115.112.218.144 to 192.168.168.65. This issue is intermittent. If I bypass the firewall everything is working fine. Following is the packets captured from sonicwall. Please suggest. Thanks in advance.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_8.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcppackets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '14, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/2e89e2dd9ccb2eb37582dc0ac4d2385f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan%20Joseph&#39;s gravatar image" /><p>Dan Joseph<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan Joseph has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '14, 02:04</p></div></div><div id="comments-container-34030" class="comments-container"><span id="34031"></span><div id="comment-34031" class="comment"><div id="post-34031-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the capture for better analysis,its clear that RST is being sent by 115.112.218.144 but one more thing i want to look is IP.ID field on syn ack and RST packet by 115.112.218.144.Are they same or different.</p></div><div id="comment-34031-info" class="comment-info"><span class="comment-age">(22 Jun '14, 03:14)</span> kishan pandey</div></div></div><div id="comment-tools-34030" class="comment-tools"></div><div class="clear"></div><div id="comment-34030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34032"></span>

<div id="answer-container-34032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34032-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I did a packet <strong>capture on my sonicwall firewall</strong> and found ...</p></blockquote><p>According to your description (i.e. works without the Firewall), I conclude that the firewall blocks the connection itself for whatever reason by sending RESET itself.</p><p>Just one example: The RST-ACK in frame #19 is at the same time stamp as the SYN-ACK in frame #17. I guess the firewall generated the RESET itself because it did not like something in the SYN-ACK or because there is a policy that does not allow the connection.</p><p>To verify my assumption, please <strong>do not</strong> capture on the firewall. Instead capture between the firewall and the modem, using one of the methods described in the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a>. If I'm right, you won't see the RST-ACK there.</p><p>Then you could enable packet tracing within the SonicWall to figure out what's going on in the firewall.</p><p>See the <strong>Packet Trace</strong> tool, and other Sonicwall CLI tools (please ask your local Sonicwall guru!)</p><blockquote><p><a href="http://help.mysonicwall.com/sw/eng/305/ui2/23100/System/Diagnostics.htm">http://help.mysonicwall.com/sw/eng/305/ui2/23100/System/Diagnostics.htm</a><br />
<a href="http://208.17.117.208/downloads/High-Level_Debugging_on_SonicWALL_UTM_and_CSM_Appliances.pdf">http://208.17.117.208/downloads/High-Level_Debugging_on_SonicWALL_UTM_and_CSM_Appliances.pdf</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '14, 04:43</p></div></div><div id="comments-container-34032" class="comments-container"></div><div id="comment-tools-34032" class="comment-tools"></div><div class="clear"></div><div id="comment-34032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

