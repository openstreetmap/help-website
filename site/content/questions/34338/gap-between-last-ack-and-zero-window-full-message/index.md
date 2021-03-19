+++
type = "question"
title = "Gap between last ACK and Zero Window Full message"
description = '''In this scenaraio the client is asking the server for a file and then (deliberatly) slows down the rate at which it reads. From the log, the client&#x27;s receive window size gradually decreaese to zero and then the server stops sending. The question is why there is a quite a large time gap between the [...'''
date = "2014-07-02T00:21:00Z"
lastmod = "2014-07-03T06:25:00Z"
weight = 34338
keywords = [ "zero", "full", "window" ]
aliases = [ "/questions/34338" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Gap between last ACK and Zero Window Full message](/questions/34338/gap-between-last-ack-and-zero-window-full-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34338-score" class="post-score" title="current number of votes">0</div><span id="post-34338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In this scenaraio the client is asking the server for a file and then (deliberatly) slows down the rate at which it reads. From the log, the client's receive window size gradually decreaese to zero and then the server stops sending. The question is why there is a quite a large time gap between the [ TCP Window Full ] message and the last client ACK (Packets 72, 102 in the stream)</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
     53 16.344495   192.168.4.114         192.168.4.101         HTTP     61     Continuation or non-HTTP traffic

Frame 53: 61 bytes on wire (488 bits), 61 bytes captured (488 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 111, Ack: 1, Len: 7
Hypertext Transfer Protocol

No.     Time        Source                Destination           Protocol Length Info
     54 16.344710   192.168.4.101         192.168.4.114         TCP      60     57856 &gt; data-port [ACK] Seq=1 Ack=118 Win=65536 Len=0

Frame 54: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 1, Ack: 118, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     57 16.354841   192.168.4.101         192.168.4.114         TCP      494    [TCP segment of a reassembled PDU]

Frame 57: 494 bytes on wire (3952 bits), 494 bytes captured (3952 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 1, Ack: 118, Len: 440

No.     Time        Source                Destination           Protocol Length Info
     58 16.355109   192.168.4.101         192.168.4.114         TCP      60     [TCP segment of a reassembled PDU]

Frame 58: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 441, Ack: 118, Len: 6

No.     Time        Source                Destination           Protocol Length Info
     59 16.355193   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=447 Win=7748 Len=0

Frame 59: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 447, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     60 16.355608   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 60: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 447, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     61 16.355807   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 61: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 1907, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     62 16.355861   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=3367 Win=8192 Len=0

Frame 62: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 3367, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     63 16.356285   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 63: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 3367, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     64 16.356495   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 64: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 4827, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     65 16.356564   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=6287 Win=8192 Len=0

Frame 65: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 6287, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     66 16.356618   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 66: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 6287, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     67 16.356702   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 67: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 7747, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     68 16.356765   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=9207 Win=8192 Len=0

Frame 68: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 9207, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     69 16.356979   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 69: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 9207, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     70 16.357185   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 70: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 10667, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     71 16.357247   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=12127 Win=5272 Len=0

Frame 71: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 12127, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     72 16.357304   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 72: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 12127, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     73 16.357408   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 73: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 13587, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     74 16.357459   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=15047 Win=2352 Len=0

Frame 74: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 15047, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     75 16.357619   192.168.4.101         192.168.4.114         TCP      1514   [TCP segment of a reassembled PDU]

Frame 75: 1514 bytes on wire (12112 bits), 1514 bytes captured (12112 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 15047, Ack: 118, Len: 1460

No.     Time        Source                Destination           Protocol Length Info
     77 16.554222   192.168.4.114         192.168.4.101         TCP      54     data-port &gt; 57856 [ACK] Seq=118 Ack=16507 Win=892 Len=0

Frame 77: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 16507, Len: 0

No.     Time        Source                Destination           Protocol Length Info
    102 21.355650   192.168.4.101         192.168.4.114         TCP      946    [TCP Window Full] [TCP segment of a reassembled PDU]

Frame 102: 946 bytes on wire (7568 bits), 946 bytes captured (7568 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 16507, Ack: 118, Len: 892

No.     Time        Source                Destination           Protocol Length Info
    104 21.554174   192.168.4.114         192.168.4.101         TCP      54     [TCP ZeroWindow] data-port &gt; 57856 [ACK] Seq=118 Ack=17399 Win=0 Len=0

Frame 104: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 17399, Len: 0

No.     Time        Source                Destination           Protocol Length Info
    105 21.870026   192.168.4.101         192.168.4.114         TCP      60     [TCP ZeroWindowProbe] [TCP segment of a reassembled PDU]

Frame 105: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 17399, Ack: 118, Len: 1

No.     Time        Source                Destination           Protocol Length Info
    106 22.074080   192.168.4.114         192.168.4.101         TCP      54     [TCP ZeroWindow] [TCP ACKed unseen segment] data-port &gt; 57856 [ACK] Seq=118 Ack=17400 Win=0 Len=0

Frame 106: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 17400, Len: 0

No.     Time        Source                Destination           Protocol Length Info
    108 22.837310   192.168.4.101         192.168.4.114         TCP      60     [TCP Previous segment not captured] [TCP segment of a reassembled PDU]

Frame 108: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 17400, Ack: 118, Len: 1

No.     Time        Source                Destination           Protocol Length Info
    109 23.034097   192.168.4.114         192.168.4.101         TCP      54     [TCP ZeroWindow] [TCP ACKed unseen segment] data-port &gt; 57856 [ACK] Seq=118 Ack=17401 Win=0 Len=0

Frame 109: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 17401, Len: 0

No.     Time        Source                Destination           Protocol Length Info
    112 24.958829   192.168.4.101         192.168.4.114         TCP      60     [TCP ZeroWindowProbe] [TCP segment of a reassembled PDU]

Frame 112: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 17401, Ack: 118, Len: 1

No.     Time        Source                Destination           Protocol Length Info
    113 25.164016   192.168.4.114         192.168.4.101         TCP      54     [TCP ZeroWindow] [TCP ACKed unseen segment] data-port &gt; 57856 [ACK] Seq=118 Ack=17402 Win=0 Len=0

No.     Time        Source                Destination           Protocol Length Info
    148 29.576307   192.168.4.101         192.168.4.114         TCP      60     [TCP Previous segment not captured] [TCP segment of a reassembled PDU]

Frame 148: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: D-Link_09:1b:61 (00:24:01:09:1b:61), Dst: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5)
Internet Protocol Version 4, Src: 192.168.4.101 (192.168.4.101), Dst: 192.168.4.114 (192.168.4.114)
Transmission Control Protocol, Src Port: 57856 (57856), Dst Port: data-port (3578), Seq: 17402, Ack: 118, Len: 1

No.     Time        Source                Destination           Protocol Length Info
    149 29.576509   192.168.4.114         192.168.4.101         TCP      54     [TCP ZeroWindow] [TCP ACKed unseen segment] data-port &gt; 57856 [ACK] Seq=118 Ack=17402 Win=0 Len=0

Frame 149: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: AsustekC_7f:f4:b5 (20:cf:30:7f:f4:b5), Dst: D-Link_09:1b:61 (00:24:01:09:1b:61)
Internet Protocol Version 4, Src: 192.168.4.114 (192.168.4.114), Dst: 192.168.4.101 (192.168.4.101)
Transmission Control Protocol, Src Port: data-port (3578), Dst Port: 57856 (57856), Seq: 118, Ack: 17402, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zero" rel="tag" title="see questions tagged &#39;zero&#39;">zero</span> <span class="post-tag tag-link-full" rel="tag" title="see questions tagged &#39;full&#39;">full</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '14, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/7a9a23ebdb86cc1c11e43fd4df8e913d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beijingdj&#39;s gravatar image" /><p><span>beijingdj</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beijingdj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '14, 01:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-34338" class="comments-container"><span id="34339"></span><div id="comment-34339" class="comment"><div id="post-34339-score" class="comment-score">1</div><div class="comment-text"><p>Trying to diagnose an issue by staring at a wall of text is very frustrating. Please post a public capture someplace, e.g. <a href="http://cloudshark.org">CloudShark</a>, Dropbox, Google Drive etc.</p></div><div id="comment-34339-info" class="comment-info"><span class="comment-age">(02 Jul '14, 01:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34352"></span><div id="comment-34352" class="comment"><div id="post-34352-score" class="comment-score"></div><div class="comment-text"><p>Added a screendshot<img src="https://osqa-ask.wireshark.org/upfiles/Gap_2.bmp" alt="alt text" /></p></div><div id="comment-34352-info" class="comment-info"><span class="comment-age">(02 Jul '14, 08:46)</span> <span class="comment-user userinfo">beijingdj</span></div></div><span id="34354"></span><div id="comment-34354" class="comment"><div id="post-34354-score" class="comment-score"></div><div class="comment-text"><p>That's just a prettier wall of text, still not a capture.</p></div><div id="comment-34354-info" class="comment-info"><span class="comment-age">(02 Jul '14, 08:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-34338" class="comment-tools"></div><div class="clear"></div><div id="comment-34338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34359"></span>

<div id="answer-container-34359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34359-score" class="post-score" title="current number of votes">0</div><span id="post-34359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Having a window size smaller than one Full-sized segment is quite an issue for the sending TCP stack. Imaging you have 200k Bytes of Data to send filled your send buffer with 1.460 byte segments. When the client's RWIN reaches the &lt;1.460 value like 892 in your question or 192 in the screenshot the sender has to decide to: A: Take all packets from the sending buffer (1460,1460,1460 etc.), rebuild them into new segments where possibly the first one is big enough to match the RWIN value (892,1460,1460 etc.) and by that having to re-segment all the data or B: wait for the client to do a Window Update allowing full-sized segments to be sent again.</p><p>In your case, I'd say it is that behaviour where the sender doesn't want to re-segment all the data but after multiple seconds sees no other way but to do so and send a sub-MSS sized segment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></img></div></div><div id="comments-container-34359" class="comments-container"><span id="34363"></span><div id="comment-34363" class="comment"><div id="post-34363-score" class="comment-score"></div><div class="comment-text"><p>s it possible to avoid this situation happening by doing some configuration on the client side ?</p></div><div id="comment-34363-info" class="comment-info"><span class="comment-age">(02 Jul '14, 13:24)</span> <span class="comment-user userinfo">beijingdj</span></div></div></div><div id="comment-tools-34359" class="comment-tools"></div><div class="clear"></div><div id="comment-34359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34360"></span>

<div id="answer-container-34360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34360-score" class="post-score" title="current number of votes">0</div><span id="post-34360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks to be the sender attempting to avoid <em><a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff570811%28v=vs.85%29.aspx">"Silly Window Syndrome"</a></em>. (See also <a href="http://tools.ietf.org/html/rfc813">RFC 813</a> and <a href="http://www.pcvr.nl/tcpip/tcp_pers.htm">http://www.pcvr.nl/tcpip/tcp_pers.htm</a>, which is straight from Stevens' TCP/IP Illusrated, Vol 1.)</p><p>Also, from <a href="http://tools.ietf.org/html/rfc793#section-3.7">RFC 793, section 3.7</a></p><pre><code>Window Management Suggestions

Another suggestion is for the sender to avoid sending small
segments by waiting until the window is large enough before
sending data.</code></pre><p>It looks like the server is attempting to avoid sending many small segments by giving the client some time to open up its receive window. When the last 192 byte segment (which is obviously less than an MSS) is sent following the 5 second delay, the server is hoping that the ACK to the segment will include a bigger receive window size so bigger segments can be sent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-34360" class="comments-container"><span id="34362"></span><div id="comment-34362" class="comment"><div id="post-34362-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to avoid this situation happening by doing some configuration on the client side ?</p></div><div id="comment-34362-info" class="comment-info"><span class="comment-age">(02 Jul '14, 13:24)</span> <span class="comment-user userinfo">beijingdj</span></div></div><span id="34382"></span><div id="comment-34382" class="comment"><div id="post-34382-score" class="comment-score"></div><div class="comment-text"><p>Maybe look at why the client takes so long to process the data.</p></div><div id="comment-34382-info" class="comment-info"><span class="comment-age">(03 Jul '14, 06:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-34360" class="comment-tools"></div><div class="clear"></div><div id="comment-34360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

