+++
type = "question"
title = "question regarding ACK ?"
description = '''Dear All, I have question regarding how to understand pcap capture by tcpdump and read by wireshark. Below are the listing between 2 ports and 2 ip. If I understand correctly 103.11.134.43 port 9091 receive 1460 byte of data and then reply to the sender that it has acknowledge the data (frame5) to b...'''
date = "2014-05-24T21:51:00Z"
lastmod = "2014-05-25T00:07:00Z"
weight = 33044
keywords = [ "ack", "skip", "frame" ]
aliases = [ "/questions/33044" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [question regarding ACK ?](/questions/33044/question-regarding-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33044-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All, I have question regarding how to understand pcap capture by tcpdump and read by wireshark. Below are the listing between 2 ports and 2 ip. If I understand correctly 103.11.134.43 port 9091 receive 1460 byte of data and then reply to the sender that it has acknowledge the data (frame5) to be accepted. If my understanding is correct, then I should have been able to see the byte sent by frame5 in my Java Socket programming when I do socket.read(byte) - rhetorical question. I do get the next frame7 in my Java Socket programming when I do socket.read(byte). -- by right, I should have been able to read frame5 as it has been acknowledged. It seems there is a skipped (instead of reading frame5, it read frame7) -- this happens in non consistent basis - from time to time I get to read frame5 in my socket.read(byte). Why such inconsistency in TCP part? or in Java Socket part?</p><p>In my program, I kept getting 0 byte in the server side - while tcpdump and wireshark showed that I actually get 1460 byte - do I get the concept correct?</p><pre><code>5 0.027797    202.146.134.42        103.11.134.43         1514   4013 &gt; 9091 [PSH, ACK] Seq=39 Ack=1 Win=16384 Len=1460

Frame 5: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits) Ethernet II, Src: Routerbo_f0:be:b1 (00:0c:42:f0:be:b1), Dst: AsustekC_e8:1a:4d (00:24:8c:e8:1a:4d) Internet Protocol Version 4, Src: 202.146.134.42 (202.146.134.42), Dst: 103.11.134.43 (103.11.134.43) Transmission Control Protocol, Src Port: 4013 (4013), Dst Port: 9091 (9091), Seq: 39, Ack: 1, Len: 1460
    Source port: 4013 (4013)
    Destination port: 9091 (9091)
    [Stream index: 0]
    Sequence number: 39    (relative sequence number)
    [Next sequence number: 1499    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
    Window size value: 64
    [Calculated window size: 16384]
    [Window size scaling factor: 256]
    Checksum: 0x1f93 [validation disabled]
    [SEQ/ACK analysis]
        [Bytes in flight: 1498] Data (1460 bytes)</code></pre><p>The next sequence of ACK for the byte 1498</p><pre><code>6 0.027819    103.11.134.43         202.146.134.42        54     9091 &gt; 4013 [ACK] Seq=1 Ack=1499 Win=64192 Len=0

Frame 6: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) Ethernet II, Src: AsustekC_e8:1a:4d (00:24:8c:e8:1a:4d), Dst: Routerbo_f0:be:b1 (00:0c:42:f0:be:b1) Internet Protocol Version 4, Src:
103.11.134.43 (103.11.134.43), Dst: 202.146.134.42 (202.146.134.42) Transmission Control Protocol, Src Port: 9091 (9091), Dst Port: 4013 (4013), Seq: 1, Ack: 1499, Len: 0
    Source port: 9091 (9091)
    Destination port: 4013 (4013)
    [Stream index: 0]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1499    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
    Window size value: 1003
    [Calculated window size: 64192]
    [Window size scaling factor: 64]
    Checksum: 0x3e0e [validation disabled]
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 5]
        [The RTT to ACK the segment was: 0.000022000 seconds]</code></pre><p>The part that socket.read(byte) got to read is the following (frame7 got read instead of frame5)</p><pre><code>7 0.027825    202.146.134.42    103.11.134.43         228    4013 &gt; 9091 [PSH, ACK] Seq=1499 Ack=1 Win=16384 Len=174

Frame 7: 228 bytes on wire (1824 bits), 228 bytes captured (1824 bits) Ethernet II, Src: Routerbo_f0:be:b1 (00:0c:42:f0:be:b1), Dst: AsustekC_e8:1a:4d (00:24:8c:e8:1a:4d) Internet Protocol Version 4, Src:
202.146.134.42 (202.146.134.42), Dst: 103.11.134.43 (103.11.134.43) Transmission Control Protocol, Src Port: 4013 (4013), Dst Port: 9091 (9091), Seq: 1499, Ack: 1, Len: 174
    Source port: 4013 (4013)
    Destination port: 9091 (9091)
    [Stream index: 0]
    Sequence number: 1499    (relative sequence number)
    [Next sequence number: 1673    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
    Window size value: 64
    [Calculated window size: 16384]
    [Window size scaling factor: 256]
    Checksum: 0x4cfa [validation disabled]
    [SEQ/ACK analysis]
        [Bytes in flight: 174] Data (174 bytes)</code></pre></div><div id="question-tags" class="tags-container tags">ack skip frame</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '14, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/ba074f56389247e05c8afcd1d8f1440c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edisonch&#39;s gravatar image" /><p>edisonch<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edisonch has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '14, 03:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33044" class="comments-container"></div><div id="comment-tools-33044" class="comment-tools"></div><div class="clear"></div><div id="comment-33044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33045"></span>

<div id="answer-container-33045" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dear All,</p><p>It seems I have solve the inconsistency of the problem above by changing the way my Java code do thing. I change the communication protocol.</p><p>Original Protocol:</p><p>client's side: 1. send order (order for server including file name and file size - form of String) 2. send the actual file 3. receive server's acknowledgement (form of String)</p><p>server's side: 1. receive order from client 2. receive the actual file 3. send server's acknowledgement</p><p>New Protocol</p><p>client's side: 1. send order 2. receive confirmation 3. send actual file 4. receive server's acknowledgement</p><p>server's side: 1. receive order 2. send confirmation 3. receive actual file 4. send server's acknowledgement</p><p>With new protocol, the file consistently send and if there is a miss, the TCP's protocol re transmit the missing frame.</p><p>Even though the problem is somehow solved, I still don't know what cause such inconsistent send/receive file in TCP's socket programming.</p><p>Thanks. If anyone can explain the problem above, I would like to thank you in advance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/ba074f56389247e05c8afcd1d8f1440c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edisonch&#39;s gravatar image" /><p>edisonch<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edisonch has no accepted answers">0%</span></p></div></div><div id="comments-container-33045" class="comments-container"></div><div id="comment-tools-33045" class="comment-tools"></div><div class="clear"></div><div id="comment-33045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

