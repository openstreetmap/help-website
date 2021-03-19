+++
type = "question"
title = "Decoding TCP request to IoT device"
description = '''I am trying to decode the request/response to a generic IoT device (with no documentation) so that I can integrate it with my exiting home automation hub. The IoT kit contains a hub that connects to the router and a set of electrical switches + temperature/humidity sensor that talk to the hub over 8...'''
date = "2016-07-10T08:34:00Z"
lastmod = "2016-07-10T10:42:00Z"
weight = 53961
keywords = [ "iot", "tcp" ]
aliases = [ "/questions/53961" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding TCP request to IoT device](/questions/53961/decoding-tcp-request-to-iot-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53961-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode the request/response to a generic IoT device (with no documentation) so that I can integrate it with my exiting home automation hub. The IoT kit contains a hub that connects to the router and a set of electrical switches + temperature/humidity sensor that talk to the hub over 865mhz RF (WIR1186) The switches are controlled via an android app that seems to be sending requests to an aws server that in turn sends a request to the hub What I want to do is decode the request so that I can send the request directly from my home automation server on the LAN</p><p>I captured the packets to and from the aws server via wireshark running on a PC as man-in-the-middle - the on/off request packets seem to be simple TCP requests Unfortunately I am not very conversant with the TCP protocol and am unable to decode it any further</p><p>Here is a sample request</p><p>+---------+---------------+----------+ 13:40:15,856,271 ETHER |0 |b8|ae|ed|ea|a3|3f|e4|f4|c6|03|d8|13|08|00|45|00|00|39|3d|9b|40|00|6e|06|ba|fa|34|1d|1e|ff|c0|a8|00|65|30|39|f3|c5|3c|48|b0|48|00|00|1d|25|50|18|f8|e5|cd|1e|00|00|55|aa|ff|ff|11|00|02|6e|ff|ff|11|13|0a|0b|00|a2|23|</p></div><div id="question-tags" class="tags-container tags">iot tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '16, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/77e0ecbdc92691de7b30c196ba69422b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superczar&#39;s gravatar image" /><p>superczar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superczar has no accepted answers">0%</span></p></div></div><div id="comments-container-53961" class="comments-container"><span id="53963"></span><div id="comment-53963" class="comment"><div id="post-53963-score" class="comment-score"></div><div class="comment-text"><p>Here is the request in what is possibly a more east to understand format</p><p>Sending a switch on request for switch 1 results in the following TCP request from port x of remote server to port y of hub</p><p>55 AA FF FF 11 00 02 B8 ED 00 11 00 0D 31 00 B7 23 55 AA FF FF 11 00 02 B8 ED 30 11 00 0D 32 05 B2 10</p><p>Unfortunately translating the hex string to ascii doesn't yield anything</p></div><div id="comment-53963-info" class="comment-info"><span class="comment-age">(10 Jul '16, 09:18)</span> superczar</div></div></div><div id="comment-tools-53961" class="comment-tools"></div><div class="clear"></div><div id="comment-53961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53964"></span>

<div id="answer-container-53964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53964-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the data you show is actually 2 messages:</p><pre><code>55 AA FF FF 11 00 02 B8 ED 00 11 00 0D 31 00 B7 23
55 AA FF FF 11 00 02 B8 ED 30 11 00 0D 32 05 B2 10</code></pre><p>55 AA is a typical start message sequence that is easy to pick out and synchronise on for radio transmissions, The last 2 bytes are likely to be some form of checksum. Try capturing the same operation to a different switch to determine which parts of the message are the switch identifier.</p><p>Also, can you name the manufacturer of the device, it's entirely possible someone else has already decoded the protocol.?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '16, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53964" class="comments-container"><span id="53975"></span><div id="comment-53975" class="comment"><div id="post-53975-score" class="comment-score"></div><div class="comment-text"><p>The device is called Oakter (oakter.com) I somehow doubt that this has been decoded before</p><p>Here is another capture through a man-in-the-middle- This is the request sent from the remote server when switching on switch 1 (same as the earlier one)</p><p>Summary 29 3.693913 52.29.30.255 192.168.137.212 TCP 71 12345 → 42087 [PSH, ACK] Seq=1 Ack=1 Win=64301 Len=17</p><p>HEX dum (the part from 55 AA onwards is the actual request)</p><p>0000 18 fe 34 f3 c8 21 02 db df c2 db 11 08 00 45 00 0010 00 39 10 75 40 00 6d 06 5f b1 34 1d 1e ff c0 a8 0020 89 d4 30 39 a4 67 95 ce bc d1 00 06 18 a9 50 18 0030 fb 2d 9d 45 00 00 55 aa ed 30 11 00 02 ca ff ff 0040 43 0d 32 31 01 db 6c</p><p>The response back to the server Summary: 31 3.755657 192.168.137.212 52.29.30.255 TCP 54 42087 → 12345 [ACK] Seq=1 Ack=18 Win=5721 Len=0</p><p>HEX 0000 02 db df c2 db 11 18 fe 34 f3 c8 21 08 00 45 00 0010 00 28 03 ba 00 00 ff 06 1a 7d c0 a8 89 d4 34 1d 0020 1e ff a4 67 30 39 00 06 18 a9 95 ce bc e2 50 10 0030 16 59 bb e1 00 00</p></div><div id="comment-53975-info" class="comment-info"><span class="comment-age">(11 Jul '16, 01:26)</span> superczar</div></div></div><div id="comment-tools-53964" class="comment-tools"></div><div class="clear"></div><div id="comment-53964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

