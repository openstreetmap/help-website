+++
type = "question"
title = "Does Wireshark recognise serial over TCP protocols? E.G. Modbus, DNP3, etc."
description = '''Hi, I have an old black box speaking Modbus RTU and DNP3 over serial, and want to migrate that to a new computer to do the exact same thing, but I can&#x27;t find info about this custom made black box and the configuration it uses for this protocols, so I want to sniff its terminals. My idea is to use a ...'''
date = "2015-03-12T20:26:00Z"
lastmod = "2015-03-13T13:48:00Z"
weight = 40529
keywords = [ "modbus", "serial", "protocol", "dnp3" ]
aliases = [ "/questions/40529" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark recognise serial over TCP protocols? E.G. Modbus, DNP3, etc.](/questions/40529/does-wireshark-recognise-serial-over-tcp-protocols-eg-modbus-dnp3-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40529-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have an old black box speaking Modbus RTU and DNP3 over serial, and want to migrate that to a new computer to do the exact same thing, but I can't find info about this custom made black box and the configuration it uses for this protocols, so I want to sniff its terminals.</p><p>My idea is to use a serial to TCP/IP converter such as Lantronix to encapsulate this serial data and sniff it with Wireshark, but I'm not sure if it recognizes the protocols when they are actually the serial versions only encapsulated over a TCP frame.</p><p>Any hint will be appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags">modbus serial protocol dnp3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '15, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/98bddf33e54526e41c7a760e53c8ee11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="japz87&#39;s gravatar image" /><p>japz87<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="japz87 has no accepted answers">0%</span></p></div></div><div id="comments-container-40529" class="comments-container"></div><div id="comment-tools-40529" class="comment-tools"></div><div class="clear"></div><div id="comment-40529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40534"></span>

<div id="answer-container-40534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40534-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes.</p><p>However it sounds as though you are trying to capture an existing serial connection, so a simple terminal server might not be enough if both ends are fixed as serial.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '15, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40534" class="comments-container"></div><div id="comment-tools-40534" class="comment-tools"></div><div class="clear"></div><div id="comment-40534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40542"></span>

<div id="answer-container-40542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40542-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's unlikely to recognize those protocols in that case.</p><p>The Lantronix boxes probably translate byte streams from the serial port into Telnet or SSH or... sequences. The same is probably true of most serial-to-{Ethernet,Wi-Fi,etc.} boxes.</p><p>If no encryption is done (raw Telnet) Wireshark can dissect the packets at the Telnet level, but it doesn't include any support for dissecting the byte streams transferred by Telnet as if they were Modbus or DNP3 or... packet sequences - the Modbus, DNP3, etc. dissectors in Wireshark are oriented towards dissecting the official encapsulation of those protocols inside Ethernet or some Internet transport protocol, not towards dissecting the serial port versions when transmitted over Telnet, and the Telnet dissection code doesn't know about them.</p><p>If they're transmitted over SSH, then Wireshark won't even be able to decrypt the traffic, much less dissect it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '15, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40542" class="comments-container"><span id="40550"></span><div id="comment-40550" class="comment"><div id="post-40550-score" class="comment-score"></div><div class="comment-text"><p>Sorry Guy, this is incorrect. Lantronix and their cheaper equivalent terminal servers, can easily be configured to operate in a plain transport mode, so capturing the IP traffic with Wireshark is trivial and the protocols discussed in the question all dissect successfully. I do this nearly every day in my day job with the protocols mentioned and was the reason why I got started with Wireshark dev.</p><p>Generally the "master" end of the link, usually a SCADA\HMI application, runs on a PC and is configured for direct TCP/IP use, or a virtual COM port provided by the terminal server vendor, and it connects over Ethernet to the terminal server which then communicates with the field device using the serial interface.</p><p>Some telemetry protocols do not change when run over TCP/IP, e.g DNP3 which keeps it's serial protection mechanism of a 16 bit CRC every 16 bytes, some have variants, e.g Modbus has Open Modbus TCP along with the standard serial versions (Wireshark dissects both) and some have a specific variant that is to be used over TCP/IP, e.g. IEC 60870-5-104.</p><p>Where @japz87 might come unstuck though, is if they can't configure either the "black box" or the device to use TCP/IP or a virtual COM port. They might be able to configure 2 terminal servers back to back and then capture on the Ethernet link between them. but I've never need to do that.</p></div><div id="comment-40550-info" class="comment-info"><span class="comment-age">(14 Mar '15, 01:51)</span> grahamb ♦</div></div></div><div id="comment-tools-40542" class="comment-tools"></div><div class="clear"></div><div id="comment-40542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

