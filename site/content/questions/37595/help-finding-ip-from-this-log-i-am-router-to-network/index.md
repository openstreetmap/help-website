+++
type = "question"
title = "Help Finding IP from this log ( I-Am-Router-To-Network )"
description = '''I am at a loss of finding the IP of the following device. Previous Firmwares would display the IP however all I am finding as the source is ( SclEleme_00:1f:a0 )  Is there any option with in Wireshark that could deceiver the IP ?  SclEleme_00:1f:a0 Broadcast BACnet-NPDU I-Am-Router-To-Network 200.82...'''
date = "2014-11-05T13:43:00Z"
lastmod = "2014-11-06T01:55:00Z"
weight = 37595
keywords = [ "ip", "mac", "find", "bacnet" ]
aliases = [ "/questions/37595" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Help Finding IP from this log ( I-Am-Router-To-Network )](/questions/37595/help-finding-ip-from-this-log-i-am-router-to-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37595-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am at a loss of finding the IP of the following device. Previous Firmwares would display the IP however all I am finding as the source is ( SclEleme_00:1f:a0 )</p><p>Is there any option with in Wireshark that could deceiver the IP ?</p><pre><code>SclEleme_00:1f:a0   Broadcast   BACnet-NPDU I-Am-Router-To-Network  200.821781000   1137    60

SclEleme_00:1f:a0 Broadcast BACnet-NPDU I-Am-Router-To-Network
200.821781000 1137 60
Frame 1137: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Interface id: 0
Encapsulation type: Ethernet (1)
Arrival Time: Nov 5, 2014 15:28:35.345502000 Eastern Standard Time
[Time shift for this packet: 0.000000000 seconds]
Epoch Time: 1415219315.345502000 seconds
[Time delta from previous captured frame: 2.252785000 seconds]
[Time delta from previous displayed frame: 2.252785000 seconds]
[Time since reference or first frame: 200.821781000 seconds]
Frame Number: 1137
Frame Length: 60 bytes (480 bits)
Capture Length: 60 bytes (480 bits)
[Frame is marked: False]
[Frame is ignored: False]
[Protocols in frame: eth:llc:bacnet:data]
[Coloring Rule Name: Broadcast]
[Coloring Rule String: eth[0] &amp; 1]
IEEE 802.3 Ethernet
Destination: Broadcast (ff:ff:ff:ff:ff:ff)
Address: Broadcast (ff:ff:ff:ff:ff:ff)
.... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the fac
tory default)
.... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
Source: SclEleme_00:1f:a0 (e4:ad:7d:00:1f:a0)
Address: SclEleme_00:1f:a0 (e4:ad:7d:00:1f:a0)
.... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
.... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Length: 12
Padding: 000000000000000000000000000000000000000000000000...
Logical-Link Control
DSAP: BACnet (0x82)
IG Bit: Individual
SSAP: BACnet (0x82)
CR Bit: Command
Control field: U, func=UI (0x03)
000. 00.. = Command: Unnumbered Information (0x00)
.... ..11 = Frame type: Unnumbered frame (0x03)
Building Automation and Control Network NPDU
Version: 0x01 (ASHRAE 135-1995)
Control: 0xa0
1... .... = NSDU contains: network layer message, message type field present.
.0.. .... = Reserved: Shall be zero and is zero.
..1. .... = Destination Specifier: DNET, DLEN and Hop Count present. If DLEN=0: broadcast
, dest. address field absent.
...0 .... = Reserved: Shall be zero and is zero.
.... 0... = Source specifier: SNET, SLEN and SADR absent
.... .0.. = Expecting Reply: Other than a BACnet-Confirmed-Request-PDU, segment of BACnet
-ComplexACK-PDU or network layer message expecting a reply present.
.... ..0. = Priority: Not a Life Safety or Critical Equipment message.
.... ...0 = Priority: Normal message
Destination Network Address: 65535
Destination MAC Layer Address Length: 0 indicates Broadcast on Destination Network
Hop Count: 14
Network Layer Message Type: 01 (I-Am-Router-To-Network)
Destination Network Address: 40991
0000 ff ff ff ff ff ff e4 ad 7d 00 1f a0 00 0c 82 82 ........}.......
0010 03 01 a0 ff ff 00 0e 01 a0 1f 00 00 00 00 00 00 ................
0020 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
0030 00 00 00 00 00 00 00 00 00 00 00 00 ............</code></pre></div><div id="question-tags" class="tags-container tags">ip mac find bacnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '14, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/f769b931a063881ba83a7fea6af732ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wall-IT&#39;s gravatar image" /><p>Wall-IT<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wall-IT has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Nov '14, 01:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37595" class="comments-container"></div><div id="comment-tools-37595" class="comment-tools"></div><div class="clear"></div><div id="comment-37595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37607"></span>

<div id="answer-container-37607" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37607-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From your text dump:</p><blockquote>[Protocols in frame: eth:llc:bacnet:data]</blockquote><p>So there is no IP protocol in this frame, hence no IP address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '14, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37607" class="comments-container"><span id="37619"></span><div id="comment-37619" class="comment"><div id="post-37619-score" class="comment-score"></div><div class="comment-text"><p>Any one with any ideas besides a massive arp request to derive the IP of the device from the MAC that was provided in the broadcast. ?</p><p>Up until now the broadcast after power cycling these devices included the IP.</p></div><div id="comment-37619-info" class="comment-info"><span class="comment-age">(06 Nov '14, 07:10)</span> Wall-IT</div></div><span id="37620"></span><div id="comment-37620" class="comment"><div id="post-37620-score" class="comment-score"></div><div class="comment-text"><p>Why a massive arp, surely one will do for the MAC address e4:ad:7d:00:1f:a0?</p></div><div id="comment-37620-info" class="comment-info"><span class="comment-age">(06 Nov '14, 07:35)</span> grahamb ♦</div></div></div><div id="comment-tools-37607" class="comment-tools"></div><div class="clear"></div><div id="comment-37607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

