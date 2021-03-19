+++
type = "question"
title = "Why is wireshark reporting that my WebSocket Connection Close is a Malformed Packet?"
description = '''Is it because my payload length is zero? RFC 6455 seems to state that the payload for this is optional. Thanks  No. Time Source Destination Protocol sPort dPort Length Info  161 0.000097000 192.168.60.80 192.168.60.2 WebSocket 80 4477 60 WebSocket Connection Close [FIN] [Malformed Packet] Frame 161:...'''
date = "2015-06-11T12:51:00Z"
lastmod = "2015-06-11T14:14:00Z"
weight = 43085
keywords = [ "close", "connection", "websocket", "malformed" ]
aliases = [ "/questions/43085" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is wireshark reporting that my WebSocket Connection Close is a Malformed Packet?](/questions/43085/why-is-wireshark-reporting-that-my-websocket-connection-close-is-a-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43085-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it because my payload length is zero? RFC 6455 seems to state that the payload for this is optional.</p><p>Thanks</p><pre><code>No.     Time           Source                Destination           Protocol sPort  dPort  Length Info
    161 0.000097000    192.168.60.80         192.168.60.2          WebSocket 80     4477   60     WebSocket Connection Close [FIN] [Malformed Packet]
Frame 161: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
    Interface id: 0 (eth0)
    Encapsulation type: Ethernet (1)
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: True]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp:http:websocket]
    [Coloring Rule Name: HTTP]
    [Coloring Rule String: http || tcp.port == 80 || http2]
Ethernet II, Src: Informat_34:56:78 (00:00:12:34:56:78), Dst: CadmusCo_ec:2d:88 (08:00:27:ec:2d:88)
    Destination: CadmusCo_ec:2d:88 (08:00:27:ec:2d:88)
        Address: CadmusCo_ec:2d:88 (08:00:27:ec:2d:88)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: Informat_34:56:78 (00:00:12:34:56:78)
        Address: Informat_34:56:78 (00:00:12:34:56:78)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IP (0x0800)
    Padding: 00000000
Internet Protocol Version 4, Src: 192.168.60.80 (192.168.60.80), Dst: 192.168.60.2 (192.168.60.2)
    Version: 4
    Header Length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 42
    Identification: 0x06b6 (1718)
    Flags: 0x00
        0... .... = Reserved bit: Not set
        .0.. .... = Don&#39;t fragment: Not set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (6)
    Header checksum: 0x7a75 [validation disabled]
        [Good: False]
        [Bad: False]
    Source: 192.168.60.80 (192.168.60.80)
    Destination: 192.168.60.2 (192.168.60.2)
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: 80 (80), Dst Port: 4477 (4477), Seq: 755, Ack: 591, Len: 2
    Source Port: 80 (80)
    Destination Port: 4477 (4477)
    [Stream index: 12]
    [TCP Segment Len: 2]
    Sequence number: 755    (relative sequence number)
    [Next sequence number: 757    (relative sequence number)]
    Acknowledgment number: 591    (relative ack number)
    Header Length: 20 bytes
    .... 0000 0001 1000 = Flags: 0x018 (PSH, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 1... = Push: Set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 1460
    [Calculated window size: 1460]
    [Window size scaling factor: -2 (no window scaling used)]
    Checksum: 0x0490 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Urgent pointer: 0
    [SEQ/ACK analysis]
        [iRTT: 0.000583000 seconds]
        [Bytes in flight: 2]
WebSocket
    1... .... = Fin: True
    .000 .... = Reserved: 0x00
    .... 1000 = Opcode: Connection Close (8)
    0... .... = Mask: False
    .000 0000 = Payload length: 0
    Payload
        Close: &lt;missing&gt;
[Malformed Packet: WebSocket]
    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
        [Malformed Packet (Exception occurred)]
        [Severity level: Error]
        [Group: Malformed]
0000  08 00 27 ec 2d 88 00 00 12 34 56 78 08 00 45 00   ..&#39;.-....4Vx..E.
0010  00 2a 06 b6 00 00 40 06 7a 75 c0 a8 3c 50 c0 a8   .*[email protected]&lt;p.. 0020=&quot;&quot; 3c=&quot;&quot; 02=&quot;&quot; 00=&quot;&quot; 50=&quot;&quot; 11=&quot;&quot; 7d=&quot;&quot; 21=&quot;&quot; 71=&quot;&quot; 9a=&quot;&quot; 4c=&quot;&quot; 3f=&quot;&quot; 65=&quot;&quot; 16=&quot;&quot; f3=&quot;&quot; 50=&quot;&quot; 18=&quot;&quot; &lt;..p.}!q.l?e..p.=&quot;&quot; 0030=&quot;&quot; 05=&quot;&quot; b4=&quot;&quot; 04=&quot;&quot; 90=&quot;&quot; 00=&quot;&quot; 00=&quot;&quot; 88=&quot;&quot; 00=&quot;&quot; 00=&quot;&quot; 00=&quot;&quot; 00=&quot;&quot; 00=&quot;&quot; ............=&quot;&quot; &lt;=&quot;&quot; code=&quot;&quot;&gt;</code></pre></div><div id="question-tags" class="tags-container tags">close connection websocket malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/6c7ff6b58d8399db804fa403bd6f2c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brownslink&#39;s gravatar image" /><p>brownslink<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brownslink has no accepted answers">0%</span></p></div></div><div id="comments-container-43085" class="comments-container"></div><div id="comment-tools-43085" class="comment-tools"></div><div class="clear"></div><div id="comment-43085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43088"></span>

<div id="answer-container-43088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like an issue that was solved in Wiresahrk 1.99.x branch and not in Wireshark 1.12.x: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=d555aa759b9fb3199eb5822c20c86ed80c4608d3">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=d555aa759b9fb3199eb5822c20c86ed80c4608d3</a></p><p>Could you give a try to Wireshark 1.99.6 development build found on <a href="http://www.wireshark.org">http://www.wireshark.org</a> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43088" class="comments-container"></div><div id="comment-tools-43088" class="comment-tools"></div><div class="clear"></div><div id="comment-43088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

