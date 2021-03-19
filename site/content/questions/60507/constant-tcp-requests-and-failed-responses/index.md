+++
type = "question"
title = "Constant TCP requests and failed responses"
description = '''I&#x27;m getting one of these per second: 457 205.494657 127.0.0.1 127.0.0.1 TCP 68 49507→23454 [SYN] Seq=0 Win=65535 Len=0 MSS=16344 WS=32 TSval=630136859 TSecr=0 SACK_PERM=1  458 205.494702 127.0.0.1 127.0.0.1 TCP 44 23454→49507 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0  Each time the source port is increment...'''
date = "2017-04-01T07:08:00Z"
lastmod = "2017-04-02T00:15:00Z"
weight = 60507
keywords = [ "localhost", "tcp", "loopback" ]
aliases = [ "/questions/60507" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Constant TCP requests and failed responses](/questions/60507/constant-tcp-requests-and-failed-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting one of these per second:</p><pre><code>457 205.494657  127.0.0.1   127.0.0.1   TCP 68  49507→23454 [SYN] Seq=0 Win=65535 Len=0 MSS=16344 WS=32 TSval=630136859 TSecr=0 SACK_PERM=1

458 205.494702  127.0.0.1   127.0.0.1   TCP 44  23454→49507 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre><p>Each time the source port is incremented by 1 and the destination is always <em>23454</em></p><p>I have closed every app, turned off wifi, no ethernet connect, and tried to close any process in the application monitor that had any network traffic.<br />
</p><p>Any help would be appreciated</p><pre><code>Frame 457: 68 bytes on wire (544 bits), 68 bytes captured (544 bits) on interface 0
    Interface id: 0 (lo0)
    Encapsulation type: NULL/Loopback (15)
    Arrival Time: Mar 31, 2017 22:35:17.546056000 EDT
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1491014117.546056000 seconds
    [Time delta from previous captured frame: 1.066713000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 205.494657000 seconds]
    Frame Number: 457
    Frame Length: 68 bytes (544 bits)
    Capture Length: 68 bytes (544 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: null:ip:tcp]
    [Coloring Rule Name: TCP SYN/FIN]
    [Coloring Rule String: tcp.flags &amp; 0x02 || tcp.flags.fin == 1]
Null/Loopback
    Family: IP (2)
Internet Protocol Version 4, Src: 127.0.0.1, Dst: 127.0.0.1
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 64
    Identification: 0x061b (1563)
    Flags: 0x02 (Don&#39;t Fragment)
        0... .... = Reserved bit: Not set
        .1.. .... = Don&#39;t fragment: Set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (6)
    Header checksum: 0x0000 [validation disabled]
    [Header checksum status: Unverified]
    Source: 127.0.0.1
    Destination: 127.0.0.1
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: 49507, Dst Port: 23454, Seq: 0, Len: 0
    Source Port: 49507
    Destination Port: 23454
    [Stream index: 193]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 0
    Header Length: 44 bytes
    Flags: 0x002 (SYN)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgment: Not set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 23454]
                [Connection establish request (SYN): server port 23454]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
        [TCP Flags: ··········S·]
    Window size value: 65535
    [Calculated window size: 65535]
    Checksum: 0xfe34 [unverified]
    [Checksum Status: Unverified]
    Urgent pointer: 0
    Options: (24 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), Timestamps, SACK permitted, End of Option List (EOL)
        Maximum segment size: 16344 bytes
            Kind: Maximum Segment Size (2)
            Length: 4
            MSS Value: 16344
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        Window scale: 5 (multiply by 32)
            Kind: Window Scale (3)
            Length: 3
            Shift count: 5
            [Multiplier: 32]
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        Timestamps: TSval 630136859, TSecr 0
            Kind: Time Stamp Option (8)
            Length: 10
            Timestamp value: 630136859
            Timestamp echo reply: 0
        TCP SACK Permitted Option: True
            Kind: SACK Permitted (4)
            Length: 2
        End of Option List (EOL)
            Type: 0
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0000 = Number: End of Option List (EOL) (0)

Frame 458: 44 bytes on wire (352 bits), 44 bytes captured (352 bits) on interface 0
    Interface id: 0 (lo0)
    Encapsulation type: NULL/Loopback (15)
    Arrival Time: Mar 31, 2017 22:35:17.546101000 EDT
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1491014117.546101000 seconds
    [Time delta from previous captured frame: 0.000045000 seconds]
    [Time delta from previous displayed frame: 0.000045000 seconds]
    [Time since reference or first frame: 205.494702000 seconds]
    Frame Number: 458
    Frame Length: 44 bytes (352 bits)
    Capture Length: 44 bytes (352 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: null:ip:tcp]
    [Coloring Rule Name: TCP RST]
    [Coloring Rule String: tcp.flags.reset eq 1]
Null/Loopback
    Family: IP (2)
Internet Protocol Version 4, Src: 127.0.0.1, Dst: 127.0.0.1
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
        0000 00.. = Differentiated Services Codepoint: Default (0)
        .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)
    Total Length: 40
    Identification: 0x7fc1 (32705)
    Flags: 0x02 (Don&#39;t Fragment)
        0... .... = Reserved bit: Not set
        .1.. .... = Don&#39;t fragment: Set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (6)
    Header checksum: 0x0000 [validation disabled]
    [Header checksum status: Unverified]
    Source: 127.0.0.1
    Destination: 127.0.0.1
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: 23454, Dst Port: 49507, Seq: 1, Ack: 1, Len: 0
    Source Port: 23454
    Destination Port: 49507
    [Stream index: 193]
    [TCP Segment Len: 0]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header Length: 20 bytes
    Flags: 0x014 (RST, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .1.. = Reset: Set
            [Expert Info (Warning/Sequence): Connection reset (RST)]
                [Connection reset (RST)]
                [Severity level: Warning]
                [Group: Sequence]
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······A·R··]
    Window size value: 0
    [Calculated window size: 0]
    [Window size scaling factor: -1 (unknown)]
    Checksum: 0xfe1c [unverified]
    [Checksum Status: Unverified]
    Urgent pointer: 0
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 457]
        [The RTT to ACK the segment was: 0.000045000 seconds]
        [iRTT: 0.000045000 seconds]</code></pre></div><div id="question-tags" class="tags-container tags">localhost tcp loopback</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '17, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/3fa9ae6259c477f6d965156688c15878?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jschwa&#39;s gravatar image" /><p>jschwa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jschwa has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-60507" class="comments-container"></div><div id="comment-tools-60507" class="comment-tools"></div><div class="clear"></div><div id="comment-60507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60516"></span>

<div id="answer-container-60516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60516-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try to use netstat to find out what application runs an open socket on port 23454? On Windows you could run</p><pre><code>netstat -ano</code></pre><p>to get a list of all open sockets with the process ID (PID) of the process servicing the port. With the help of a task manager / process explorer you can find the program associated to the PID.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60516" class="comments-container"></div><div id="comment-tools-60516" class="comment-tools"></div><div class="clear"></div><div id="comment-60516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

