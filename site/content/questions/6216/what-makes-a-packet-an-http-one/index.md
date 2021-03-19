+++
type = "question"
title = "What makes a packet an HTTP one"
description = '''I am trying to figure out why WireShark does not treat a packet as an HTTP one. Here is the scenario: A client ( from port x) sends a GET request to a server (to port 80). In response, the server (from port 80) sends a packet to the client (to port 80).  WireShark recognizes the client -&amp;gt; server ...'''
date = "2011-09-08T12:50:00Z"
lastmod = "2011-09-08T14:07:00Z"
weight = 6216
keywords = [ "http" ]
aliases = [ "/questions/6216" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What makes a packet an HTTP one](/questions/6216/what-makes-a-packet-an-http-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6216-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to figure out why WireShark does not treat a packet as an HTTP one. Here is the scenario: A client ( from port x) sends a GET request to a server (to port 80). In response, the server (from port 80) sends a packet to the client (to port 80). WireShark recognizes the client -&gt; server packet as an HTTP one, but does not recognize the response packet as an HTTP one even though it has the status line HTTP/1.0 200 OK.</p><p>I am wondering if anyone could offer some clue for understanding this. The response packet is the following:</p><p>Transmission Control Protocol, Src Port: http (80), Dst Port: 50374 (50374), Seq: 1, Ack: 628, Len: 100</p><pre><code>Source port: http (80)
Destination port: 50374 (50374)
[Stream index: 15]
Sequence number: 1    (relative sequence number)
[Next sequence number: 101    (relative sequence number)]
Acknowledgement number: 628    (relative ack number)
Header length: 20 bytes
Flags: 0x18 (PSH, ACK)
    000. .... .... = Reserved: Not set
    ...0 .... .... = Nonce: Not set
    .... 0... .... = Congestion Window Reduced (CWR): Not set
    .... .0.. .... = ECN-Echo: Not set
    .... ..0. .... = Urgent: Not set
    .... ...1 .... = Acknowledgement: Set
    .... .... 1... = Push: Set
    .... .... .0.. = Reset: Not set
    .... .... ..0. = Syn: Not set
    .... .... ...0 = Fin: Not set
Window size value: 3547
[Calculated window size: 7094]
[Window size scaling factor: 2]
Checksum: 0x248e [validation disabled]
    [Good Checksum: False]
    [Bad Checksum: False]
[SEQ/ACK analysis]
    [Bytes in flight: 100]
TCP segment data (100 bytes)</code></pre><p>0000  00 24 8c d9 a4 33 00 40 8c be 65 28 08 00 45 00   [email protected](..E. 0010  00 8c 85 e6 40 00 40 06 32 1a c0 a8 00 5f c0 a8   [email protected]@.2...._.. 0020  00 bc 00 50 c4 c6 54 49 3f 4a 66 aa 68 4a 50 18   ...P..TI?Jf.hJP. 0030  0d db 24 8e 00 00 48 54 54 50 2f 31 2e 30 20 32   ..$...HTTP/1.0 2 0040  30 30 20 4f 4b 0d 0a 43 6f 6e 74 65 6e 74 2d 54   00 OK..Content-T 0050  79 70 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e   ype: application 0060  2f 78 2d 72 74 73 70 2d 74 75 6e 6e 65 6c 6c 65   /x-rtsp-tunnelle 0070  64 0d 0a 44 61 74 65 3a 20 54 68 75 2c 20 30 38   d..Date: Thu, 08 0080  20 53 65 70 20 32 30 31 31 20 31 37 3a 34 33 3a    Sep 2011 17:43: 0090  32 32 20 47 4d 54 0d 0a 0d 0a                     22 GMT....</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '11, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/e23332dc51869f08737cc96395284e59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hong&#39;s gravatar image" /><p>Hong<br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hong has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '11, 13:00</p></div></div><div id="comments-container-6216" class="comments-container"></div><div id="comment-tools-6216" class="comment-tools"></div><div class="clear"></div><div id="comment-6216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6218"></span>

<div id="answer-container-6218" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6218-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP protocol preference "Allow Subdissector to reassemble TCP streams" is enabled. This means that any protocol than runs atop TCP can tell TCP to collect more data until it has a full PDU. In the case of HTTP, the HTTP dissector will try to collect a full HTTP response before showing it.</p><p>In the hex data that you supplied, the full HTTP header is visible. However, there is no "Content-Length" header and no "Transfer-Encoding: Chunked" header. This means the end of the HTTP PDU is when the TCP connection gets closed by the FIN packets. If the FIN packets are not in the trace, then Wireshark has no way of knowing that the HTTP response is complete and will keep trying to collect data until it sees the FIN.</p><p>You can make Wireshark show the HTTP response straight away by disabling the "Allow Subdissector to reassemble TCP streams" in the TCP protocol preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '11, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6218" class="comments-container"><span id="6220"></span><div id="comment-6220" class="comment"><div id="post-6220-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for the elucidation! Yes, the referred packet shows up as an HTTP one once "Allow Subdissector to reassemble TCP streams" is disabled.</p></div><div id="comment-6220-info" class="comment-info"><span class="comment-age">(08 Sep '11, 15:18)</span> Hong</div></div></div><div id="comment-tools-6218" class="comment-tools"></div><div class="clear"></div><div id="comment-6218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

