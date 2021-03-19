+++
type = "question"
title = "Web &amp; App Server Communication [RST] - Help"
description = '''All, We have admins reporting a network issue; however have confirmed there to be no network issue occuring. The issue is intermittent and the capture below is whats captured during the issue. Can anyone assist me in determining the cause for the [RST] at the very end of this stream? Thanks in advan...'''
date = "2014-09-30T09:20:00Z"
lastmod = "2014-09-30T09:38:00Z"
weight = 36727
keywords = [ "rst", "capture" ]
aliases = [ "/questions/36727" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Web & App Server Communication \[RST\] - Help](/questions/36727/web-app-server-communication-rst-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36727-score" class="post-score" title="current number of votes">0</div><span id="post-36727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>We have admins reporting a network issue; however have confirmed there to be no network issue occuring. The issue is intermittent and the capture below is whats captured during the issue. Can anyone assist me in determining the cause for the [RST] at the very end of this stream?</p><p>Thanks in advance for any and all feedback</p><pre><code>No.     Source Destination Protocol Length 
   1255 10.10.60.42           172.17.133.75         TCP      70     63757 &gt; 9004 [SYN] Seq=0 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1

Frame 1255: 70 bytes on wire (560 bits), 70 bytes captured (560 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.172015000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.172015000 seconds
    [Time delta from previous captured frame: 0.549209000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 487.332510000 seconds]
    Frame Number: 1255
    Frame Length: 70 bytes (560 bits)
    Capture Length: 70 bytes (560 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP SYN/FIN]
    [Coloring Rule String: tcp.flags &amp; 0x02 || tcp.flags.fin == 1]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 0, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 0    (relative sequence number)
    Header length: 32 bytes
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
            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port 9004]
                [Message: Connection establish request (SYN): server port 9004]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    Checksum: 0x1a4f [validation disabled]
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted

No.     Source Destination Protocol Length 
   1256 172.17.133.75         10.10.60.42           TCP      70     9004 &gt; 63757 [SYN, ACK] Seq=0 Ack=1 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1

Frame 1256: 70 bytes on wire (560 bits), 70 bytes captured (560 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.172785000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.172785000 seconds
    [Time delta from previous captured frame: 0.000770000 seconds]
    [Time delta from previous displayed frame: 0.000770000 seconds]
    [Time since reference or first frame: 487.333280000 seconds]
    Frame Number: 1256
    Frame Length: 70 bytes (560 bits)
    Capture Length: 70 bytes (560 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP SYN/FIN]
    [Coloring Rule String: tcp.flags &amp; 0x02 || tcp.flags.fin == 1]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 0, Ack: 1, Len: 0
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 32 bytes
    Flags: 0x012 (SYN, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port 9004]
                [Message: Connection establish acknowledge (SYN+ACK): server port 9004]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    Checksum: 0xc74d [validation disabled]
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1257 10.10.60.42           172.17.133.75         TCP      64     63757 &gt; 9004 [ACK] Seq=1 Ack=1 Win=49640 Len=0

Frame 1257: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.173110000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.173110000 seconds
    [Time delta from previous captured frame: 0.000325000 seconds]
    [Time delta from previous displayed frame: 0.000325000 seconds]
    [Time since reference or first frame: 487.333605000 seconds]
    Frame Number: 1257
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 1, Ack: 1, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x0819 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1258 10.10.60.42           172.17.133.75         TCP      126    63757 &gt; 9004 [PSH, ACK] Seq=1 Ack=1 Win=49640 Len=68

Frame 1258: 126 bytes on wire (1008 bits), 126 bytes captured (1008 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.175079000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.175079000 seconds
    [Time delta from previous captured frame: 0.001969000 seconds]
    [Time delta from previous displayed frame: 0.001969000 seconds]
    [Time since reference or first frame: 487.335574000 seconds]
    Frame Number: 1258
    Frame Length: 126 bytes (1008 bits)
    Capture Length: 126 bytes (1008 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 1, Ack: 1, Len: 68
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 69    (relative sequence number)]
    Acknowledgment number: 1    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x2e12 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1259 172.17.133.75         10.10.60.42           TCP      60     9004 &gt; 63757 [ACK] Seq=1 Ack=69 Win=49640 Len=0

Frame 1259: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.175295000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.175295000 seconds
    [Time delta from previous captured frame: 0.000216000 seconds]
    [Time delta from previous displayed frame: 0.000216000 seconds]
    [Time since reference or first frame: 487.335790000 seconds]
    Frame Number: 1259
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 1, Ack: 69, Len: 0
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 1    (relative sequence number)
    Acknowledgment number: 69    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x07d5 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1260 172.17.133.75         10.10.60.42           TCP      945    9004 &gt; 63757 [PSH, ACK] Seq=1 Ack=69 Win=49640 Len=887

Frame 1260: 945 bytes on wire (7560 bits), 945 bytes captured (7560 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.198195000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.198195000 seconds
    [Time delta from previous captured frame: 0.022900000 seconds]
    [Time delta from previous displayed frame: 0.022900000 seconds]
    [Time since reference or first frame: 487.358690000 seconds]
    Frame Number: 1260
    Frame Length: 945 bytes (7560 bits)
    Capture Length: 945 bytes (7560 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 1, Ack: 69, Len: 887
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 1    (relative sequence number)
    [Next sequence number: 888    (relative sequence number)]
    Acknowledgment number: 69    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x1c70 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1261 10.10.60.42           172.17.133.75         TCP      64     63757 &gt; 9004 [ACK] Seq=69 Ack=888 Win=49640 Len=0

Frame 1261: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.198570000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.198570000 seconds
    [Time delta from previous captured frame: 0.000375000 seconds]
    [Time delta from previous displayed frame: 0.000375000 seconds]
    [Time since reference or first frame: 487.359065000 seconds]
    Frame Number: 1261
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 69, Ack: 888, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 69    (relative sequence number)
    Acknowledgment number: 888    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x045e [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1262 10.10.60.42           172.17.133.75         TCP      198    63757 &gt; 9004 [PSH, ACK] Seq=69 Ack=888 Win=49640 Len=140

Frame 1262: 198 bytes on wire (1584 bits), 198 bytes captured (1584 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.229655000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.229655000 seconds
    [Time delta from previous captured frame: 0.031085000 seconds]
    [Time delta from previous displayed frame: 0.031085000 seconds]
    [Time since reference or first frame: 487.390150000 seconds]
    Frame Number: 1262
    Frame Length: 198 bytes (1584 bits)
    Capture Length: 198 bytes (1584 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 69, Ack: 888, Len: 140
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 69    (relative sequence number)
    [Next sequence number: 209    (relative sequence number)]
    Acknowledgment number: 888    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x6ef7 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1263 172.17.133.75         10.10.60.42           TCP      60     9004 &gt; 63757 [ACK] Seq=888 Ack=209 Win=49640 Len=0

Frame 1263: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.229963000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.229963000 seconds
    [Time delta from previous captured frame: 0.000308000 seconds]
    [Time delta from previous displayed frame: 0.000308000 seconds]
    [Time since reference or first frame: 487.390458000 seconds]
    Frame Number: 1263
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 888, Ack: 209, Len: 0
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 888    (relative sequence number)
    Acknowledgment number: 209    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x03d2 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1264 172.17.133.75         10.10.60.42           TCP      125    9004 &gt; 63757 [PSH, ACK] Seq=888 Ack=209 Win=49640 Len=67

Frame 1264: 125 bytes on wire (1000 bits), 125 bytes captured (1000 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.243915000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.243915000 seconds
    [Time delta from previous captured frame: 0.013952000 seconds]
    [Time delta from previous displayed frame: 0.013952000 seconds]
    [Time since reference or first frame: 487.404410000 seconds]
    Frame Number: 1264
    Frame Length: 125 bytes (1000 bits)
    Capture Length: 125 bytes (1000 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 888, Ack: 209, Len: 67
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 888    (relative sequence number)
    [Next sequence number: 955    (relative sequence number)]
    Acknowledgment number: 209    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0xb7ee [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1265 10.10.60.42           172.17.133.75         TCP      64     63757 &gt; 9004 [ACK] Seq=209 Ack=955 Win=49640 Len=0

Frame 1265: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.244171000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.244171000 seconds
    [Time delta from previous captured frame: 0.000256000 seconds]
    [Time delta from previous displayed frame: 0.000256000 seconds]
    [Time since reference or first frame: 487.404666000 seconds]
    Frame Number: 1265
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 209, Ack: 955, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 209    (relative sequence number)
    Acknowledgment number: 955    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x038f [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1266 10.10.60.42           172.17.133.75         TCP      212    63757 &gt; 9004 [PSH, ACK] Seq=209 Ack=955 Win=49640 Len=154

Frame 1266: 212 bytes on wire (1696 bits), 212 bytes captured (1696 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.244621000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.244621000 seconds
    [Time delta from previous captured frame: 0.000450000 seconds]
    [Time delta from previous displayed frame: 0.000450000 seconds]
    [Time since reference or first frame: 487.405116000 seconds]
    Frame Number: 1266
    Frame Length: 212 bytes (1696 bits)
    Capture Length: 212 bytes (1696 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 209, Ack: 955, Len: 154
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 209    (relative sequence number)
    [Next sequence number: 363    (relative sequence number)]
    Acknowledgment number: 955    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x5757 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1267 172.17.133.75         10.10.60.42           TCP      287    9004 &gt; 63757 [PSH, ACK] Seq=955 Ack=363 Win=49640 Len=229

Frame 1267: 287 bytes on wire (2296 bits), 287 bytes captured (2296 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.252848000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.252848000 seconds
    [Time delta from previous captured frame: 0.008227000 seconds]
    [Time delta from previous displayed frame: 0.008227000 seconds]
    [Time since reference or first frame: 487.413343000 seconds]
    Frame Number: 1267
    Frame Length: 287 bytes (2296 bits)
    Capture Length: 287 bytes (2296 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 955, Ack: 363, Len: 229
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 955    (relative sequence number)
    [Next sequence number: 1184    (relative sequence number)]
    Acknowledgment number: 363    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x65a2 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1268 172.17.133.75         10.10.60.42           TCP      81     9004 &gt; 63757 [PSH, ACK] Seq=1184 Ack=363 Win=49640 Len=23

Frame 1268: 81 bytes on wire (648 bits), 81 bytes captured (648 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.253821000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.253821000 seconds
    [Time delta from previous captured frame: 0.000973000 seconds]
    [Time delta from previous displayed frame: 0.000973000 seconds]
    [Time since reference or first frame: 487.414316000 seconds]
    Frame Number: 1268
    Frame Length: 81 bytes (648 bits)
    Capture Length: 81 bytes (648 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 1184, Ack: 363, Len: 23
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 1184    (relative sequence number)
    [Next sequence number: 1207    (relative sequence number)]
    Acknowledgment number: 363    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x37ea [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1269 10.10.60.42           172.17.133.75         TCP      64     63757 &gt; 9004 [ACK] Seq=363 Ack=1207 Win=49640 Len=0

Frame 1269: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.254020000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.254020000 seconds
    [Time delta from previous captured frame: 0.000199000 seconds]
    [Time delta from previous displayed frame: 0.000199000 seconds]
    [Time since reference or first frame: 487.414515000 seconds]
    Frame Number: 1269
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 363, Ack: 1207, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 363    (relative sequence number)
    Acknowledgment number: 1207    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x01f9 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1270 172.17.133.75         10.10.60.42           TCP      60     9004 &gt; 63757 [FIN, ACK] Seq=1207 Ack=363 Win=49640 Len=0

Frame 1270: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.254040000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.254040000 seconds
    [Time delta from previous captured frame: 0.000020000 seconds]
    [Time delta from previous displayed frame: 0.000020000 seconds]
    [Time since reference or first frame: 487.414535000 seconds]
    Frame Number: 1270
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP SYN/FIN]
    [Coloring Rule String: tcp.flags &amp; 0x02 || tcp.flags.fin == 1]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 1207, Ack: 363, Len: 0
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 1207    (relative sequence number)
    Acknowledgment number: 363    (relative ack number)
    Header length: 20 bytes
    Flags: 0x011 (FIN, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...1 = Fin: Set
            [Expert Info (Chat/Sequence): Connection finish (FIN)]
                [Message: Connection finish (FIN)]
                [Severity level: Chat]
                [Group: Sequence]
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x01f8 [validation disabled]

No.     Source Destination Protocol Length 
   1271 10.10.60.42           172.17.133.75         TCP      64     63757 &gt; 9004 [ACK] Seq=363 Ack=1208 Win=49640 Len=0

Frame 1271: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.254298000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.254298000 seconds
    [Time delta from previous captured frame: 0.000258000 seconds]
    [Time delta from previous displayed frame: 0.000258000 seconds]
    [Time since reference or first frame: 487.414793000 seconds]
    Frame Number: 1271
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 363, Ack: 1208, Len: 0
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 363    (relative sequence number)
    Acknowledgment number: 1208    (relative ack number)
    Header length: 20 bytes
    Flags: 0x010 (ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x01f8 [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1272 10.10.60.42           172.17.133.75         TCP      81     63757 &gt; 9004 [PSH, ACK] Seq=363 Ack=1208 Win=49640 Len=23

Frame 1272: 81 bytes on wire (648 bits), 81 bytes captured (648 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.254701000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.254701000 seconds
    [Time delta from previous captured frame: 0.000403000 seconds]
    [Time delta from previous displayed frame: 0.000403000 seconds]
    [Time since reference or first frame: 487.415196000 seconds]
    Frame Number: 1272
    Frame Length: 81 bytes (648 bits)
    Capture Length: 81 bytes (648 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp:data]
    [Coloring Rule Name: TCP]
    [Coloring Rule String: tcp]
Ethernet II, Src: Oracle_43:61:dc (00:21:28:43:61:dc), Dst: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Destination: Cisco_fe:1b:04 (00:0b:fc:fe:1b:04)
    Source: Oracle_43:61:dc (00:21:28:43:61:dc)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 206
Internet Protocol Version 4, Src: 10.10.60.42 (10.10.60.42), Dst: 172.17.133.75 (172.17.133.75)
Transmission Control Protocol, Src Port: 63757 (63757), Dst Port: 9004 (9004), Seq: 363, Ack: 1208, Len: 23
    Source port: 63757 (63757)
    Destination port: 9004 (9004)
    [Stream index: 48]
    Sequence number: 363    (relative sequence number)
    [Next sequence number: 386    (relative sequence number)]
    Acknowledgment number: 1208    (relative ack number)
    Header length: 20 bytes
    Flags: 0x018 (PSH, ACK)
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
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0xaf8a [validation disabled]
    [SEQ/ACK analysis]

No.     Source Destination Protocol Length 
   1273 172.17.133.75         10.10.60.42           TCP      60     9004 &gt; 63757 [RST] Seq=1208 Win=49640 Len=0

Frame 1273: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 25, 2014 09:08:08.254892000 Eastern Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1411650488.254892000 seconds
    [Time delta from previous captured frame: 0.000191000 seconds]
    [Time delta from previous displayed frame: 0.000191000 seconds]
    [Time since reference or first frame: 487.415387000 seconds]
    Frame Number: 1273
    Frame Length: 60 bytes (480 bits)
    Capture Length: 60 bytes (480 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:vlan:ip:tcp]
    [Coloring Rule Name: TCP RST]
    [Coloring Rule String: tcp.flags.reset eq 1]
Ethernet II, Src: IntelCor_14:30:a5 (90:e2:ba:14:30:a5), Dst: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Destination: Cisco_9f:f0:e9 (00:00:0c:9f:f0:e9)
    Source: IntelCor_14:30:a5 (90:e2:ba:14:30:a5)
    Type: 802.1Q Virtual LAN (0x8100)
802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 233
Internet Protocol Version 4, Src: 172.17.133.75 (172.17.133.75), Dst: 10.10.60.42 (10.10.60.42)
Transmission Control Protocol, Src Port: 9004 (9004), Dst Port: 63757 (63757), Seq: 1208, Len: 0
    Source port: 9004 (9004)
    Destination port: 63757 (63757)
    [Stream index: 48]
    Sequence number: 1208    (relative sequence number)
    Header length: 20 bytes
    Flags: 0x004 (RST)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...0 .... = Acknowledgment: Not set
        .... .... 0... = Push: Not set
        .... .... .1.. = Reset: Set
            [Expert Info (Chat/Sequence): Connection reset (RST)]
                [Message: Connection reset (RST)]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
    Window size value: 49640
    [Calculated window size: 49640]
    [Window size scaling factor: 1]
    Checksum: 0x0285 [validation disabled]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/43de8e28e7a2786fa142b09c584d3883?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boothrobertl&#39;s gravatar image" /><p><span>boothrobertl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boothrobertl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '14, 09:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36727" class="comments-container"><span id="36729"></span><div id="comment-36729" class="comment"><div id="post-36729-score" class="comment-score">1</div><div class="comment-text"><p>Wall of text analysis is very tedious. You might get a better response if you post a capture file somewhere, e.g. <a href="http://cloudshark.org">CloudShark</a>, DropBox, Google Drive etc. (and edit your question with a link to the file), so folks can use the tool they like best (Wireshark) to analyse the data.</p></div><div id="comment-36729-info" class="comment-info"><span class="comment-age">(30 Sep '14, 09:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36727" class="comment-tools"></div><div class="clear"></div><div id="comment-36727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

