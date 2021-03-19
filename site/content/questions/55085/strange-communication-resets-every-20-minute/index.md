+++
type = "question"
title = "strange communication resets every 20 minute"
description = '''Hi All, I am new to Wireshark. I started using it to understand some strange errors on our Exchange Server. At some point of time I noticed big number of Schannel errors on the server. I could not find any explanation. The errors are usually logged every 20 minutes or so. When I started using Wiresh...'''
date = "2016-08-23T18:31:00Z"
lastmod = "2016-08-31T11:48:00Z"
weight = 55085
keywords = [ "communication", "resets" ]
aliases = [ "/questions/55085" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [strange communication resets every 20 minute](/questions/55085/strange-communication-resets-every-20-minute)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55085-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new to Wireshark. I started using it to understand some strange errors on our Exchange Server. At some point of time I noticed big number of Schannel errors on the server. I could not find any explanation. The errors are usually logged every 20 minutes or so. When I started using Wireshark I noticed that some clients start communication with the Exchange and got reset after initial communication establishment. All clients have .in domain names (like mail.somedomain.in) with IP addresses in different countries (Europe, US, Canada and etc.). When I block the domain name or IP, after a day or two I get the same from another domain in .in from a different IP Below is the Wireshark's "catch" example:</p><pre><code>12724   10:51:06.415375 clientIP    serverIP  TCP   70  11396 → 25 [SYN] Seq=0 Win=14600 Len=0 MSS=1452 TSval=1922222740 TSecr=0

12725   10:51:06.415480 serverIP     clientIP   TCP 70  25 → 11396 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 TSval=7971354 TSecr=1922222740

12728   10:51:06.638712 clientIP    serverIP  TCP   66  11396 → 25 [ACK] Seq=1 Ack=1 Win=14600 Len=0 TSval=1922222963 TSecr=7971354

12729   10:51:06.639302 serverIP  clientIP  SMTP    168 S: 220 MyExServer.mydomain.local Microsoft ESMTP MAIL Service ready at Wed, 24 Aug 2016 10:51:06 +1000

12738   10:51:06.862930 clientIP    serverIP TCP    66  11396 → 25 [ACK] Seq=1 Ack=103 Win=14600 Len=0 TSval=1922223187 TSecr=7971377

12739   10:51:06.862978 clientIP    serverIP    SMTP    90  C: EHLO mail.somedomain.in

12740   10:51:06.863217 serverIP     clientIP   SMTP    334 S: 250 MyExServer.mydomain.localHello [clientIP] | 250 SIZE | 250 PIPELINING | 250 DSN | 250 ENHANCEDSTATUSCODES | 250 STARTTLS | 250 X-ANONYMOUSTLS | 250 AUTH NTLM | 250 X-EXPS GSSAPI NTLM | 250 8BITMIME | 250 BINARYMIME | 250 CHUNKING | 250 XEXCH50 | 250 XRDST | 250 XSHADOW

12747   10:51:07.086053 clientIP    serverIP    SMTP    76  C: STARTTLS

12748   10:51:07.086269 serverIP     clientIP   SMTP    95  S: 220 2.0.0 SMTP server ready

12755   10:51:07.310538 clientIP    serverIP    TLSv1   276 Client Hello

12757   10:51:07.334693 serverIP    clientIP TLSv1  1300    Server Hello, Certificate, Server Key Exchange, Server Hello Done

12762   10:51:07.558485 clientIP    serverIP    SMTP    90  C: EHLO mail.somedomain.in

12763   10:51:07.558805 serverIP    clientIP    TCP 66  25 → 11396 [FIN, ACK] Seq=1634 Ack=269 Win=64532 Len=0 TSval=7971469 TSecr=1922223883

12770   10:51:07.782102 clientIP    serverIP    TCP 66  11396 → 25 [RST, ACK] Seq=269 Ack=1635 Win=17276 Len=0 TSval=1922224106 TSecr=7971469</code></pre><p>Again, all this happens every 20 minutes, and when I block it will come from another domain in .in.</p><p>Any ideas? Thanks in advance.</p><hr /><p>Hi,</p><p>As expected it is back again, please, see the catch below</p><pre><code>No.     Time               Source                Destination           Protocol Length Info
  12488 13:04:52.526684    clientIP         192.168.x.x        TCP      70     59299 → 25 [SYN] Seq=0 Win=14600 Len=0 MSS=1452 TSval=2535048776 TSecr=0
Frame 12488: 70 bytes on wire (560 bits), 70 bytes captured (560 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 0, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12489 13:04:52.526793    192.168.x.x        clientIP         TCP      70     25 → 59299 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 TSval=69252615 TSecr=2535048776
Frame 12489: 70 bytes on wire (560 bits), 70 bytes captured (560 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 0, Ack: 1, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12490 13:04:52.748385    clientIP         192.168.x.x        TCP      66     59299 → 25 [ACK] Seq=1 Ack=1 Win=14600 Len=0 TSval=2535048998 TSecr=69252615
Frame 12490: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 1, Ack: 1, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12491 13:04:52.749013    192.168.x.x        clientIP         SMTP     168    S: 220 DS2008SVR01.mydomain.local Microsoft ESMTP MAIL Service ready at Wed, 31 Aug 2016 13:04:51 +1000
Frame 12491: 168 bytes on wire (1344 bits), 168 bytes captured (1344 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 1, Ack: 1, Len: 102
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
  12492 13:04:52.771823    192.168.x.92        192.168.x.x        TCP      60     [TCP Keep-Alive] 51150 → 445 [ACK] Seq=1 Ack=1 Win=2052 Len=1
Frame 12492: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: Microsof_8f:35:f0 (58:82:a8:8f:35:f0), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.92, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 51150 (51150), Dst Port: 445 (445), Seq: 1, Ack: 1, Len: 1
Data (1 byte)
0000  00                                                .

No.     Time               Source                Destination           Protocol Length Info
  12493 13:04:52.771847    192.168.x.x        192.168.x.92        TCP      66     [TCP Keep-Alive ACK] 445 → 51150 [ACK] Seq=1 Ack=2 Win=256 Len=0 SLE=1 SRE=2
Frame 12493: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Microsof_8f:35:f0 (58:82:a8:8f:35:f0)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.92
Transmission Control Protocol, Src Port: 445 (445), Dst Port: 51150 (51150), Seq: 1, Ack: 2, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12494 13:04:52.846088    192.168.x.26        192.168.x.x        TCP      66     64368 → 8059 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
Frame 12494: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 0, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12495 13:04:52.846199    192.168.x.x        192.168.x.26        TCP      66     8059 → 64368 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
Frame 12495: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.26
Transmission Control Protocol, Src Port: 8059 (8059), Dst Port: 64368 (64368), Seq: 0, Ack: 1, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12496 13:04:52.846466    192.168.x.26        192.168.x.x        TCP      60     64368 → 8059 [ACK] Seq=1 Ack=1 Win=65536 Len=0
Frame 12496: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 1, Ack: 1, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12497 13:04:52.846549    192.168.x.26        192.168.x.x        TCP      320    [TCP segment of a reassembled PDU]
Frame 12497: 320 bytes on wire (2560 bits), 320 bytes captured (2560 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 1, Ack: 1, Len: 266

No.     Time               Source                Destination           Protocol Length Info
  12498 13:04:52.970731    clientIP         192.168.x.x        TCP      66     59299 → 25 [ACK] Seq=1 Ack=103 Win=14600 Len=0 TSval=2535049220 TSecr=69252637
Frame 12498: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 1, Ack: 103, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12499 13:04:52.970794    clientIP         192.168.x.x        SMTP     88     C: EHLO mail.clientDoman.in
Frame 12499: 88 bytes on wire (704 bits), 88 bytes captured (704 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 1, Ack: 103, Len: 22
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
  12500 13:04:52.971065    192.168.x.x        clientIP         SMTP     334    S: 250 DS2008SVR01.mydomain.local Hello [clientIP] | 250 SIZE | 250 PIPELINING | 250 DSN | 250 ENHANCEDSTATUSCODES | 250 STARTTLS | 250 X-ANONYMOUSTLS | 250 AUTH NTLM | 250 X-EXPS GSSAPI NTLM | 250 8BITMIME | 250 BINARYMIME | 250 CHUNKING | 250 XEXCH50 | 250 XRDST | 250 XSHADOW
Frame 12500: 334 bytes on wire (2672 bits), 334 bytes captured (2672 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 103, Ack: 23, Len: 268
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
  12501 13:04:52.975902    192.168.x.x        192.168.x.92        TCP      55     [TCP Keep-Alive] 445 → 51150 [ACK] Seq=0 Ack=2 Win=256 Len=1
Frame 12501: 55 bytes on wire (440 bits), 55 bytes captured (440 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Microsof_8f:35:f0 (58:82:a8:8f:35:f0)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.92
Transmission Control Protocol, Src Port: 445 (445), Dst Port: 51150 (51150), Seq: 0, Ack: 2,     Len: 1
Data (1 byte)
0000  00                                                .

No.     Time               Source                Destination           Protocol Length Info
  12502 13:04:52.976651    192.168.x.92        192.168.x.x        TCP      66     [TCP Keep-Alive ACK] 51150 → 445 [ACK] Seq=2 Ack=1 Win=2052 Len=0 SLE=0 SRE=1
Frame 12502: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: Microsof_8f:35:f0 (58:82:a8:8f:35:f0), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.92, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 51150 (51150), Dst Port: 445 (445), Seq: 2, Ack: 1, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12503 13:04:53.053891    192.168.x.x        192.168.x.26        TCP      54     8059 → 64368 [ACK] Seq=1 Ack=267 Win=65536 Len=0
Frame 12503: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.26
Transmission Control Protocol, Src Port: 8059 (8059), Dst Port: 64368 (64368), Seq: 1, Ack: 267, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12504 13:04:53.054100    192.168.x.26        192.168.x.x        HTTP     126    POST /officescan/cgi/cgiLog.exe HTTP/1.1  (application/x-www-form-urlencoded)
Frame 12504: 126 bytes on wire (1008 bits), 126 bytes captured (1008 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 267, Ack: 1, Len: 72
[2 Reassembled TCP Segments (338 bytes): #12497(266), #12504(72)]
Hypertext Transfer Protocol
HTML Form URL Encoded: application/x-www-form-urlencoded

No.     Time               Source                Destination           Protocol Length Info
  12505 13:04:53.070409    192.168.x.x        192.168.x.26        HTTP     256    HTTP/1.1 200 OK  (text/html)
Frame 12505: 256 bytes on wire (2048 bits), 256 bytes captured (2048 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.26
Transmission Control Protocol, Src Port: 8059 (8059), Dst Port: 64368 (64368), Seq: 1, Ack: 339, Len: 202
Hypertext Transfer Protocol
Line-based text data: text/html

No.     Time               Source                Destination           Protocol Length Info
  12506 13:04:53.070781    192.168.x.26        192.168.x.x        TCP      60     64368 → 8059 [FIN, ACK] Seq=339 Ack=203 Win=65280 Len=0
Frame 12506: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 339, Ack: 203, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12507 13:04:53.070833    192.168.x.x        192.168.x.26        TCP      54     8059 → 64368 [FIN, ACK] Seq=203 Ack=340 Win=65536 Len=0
Frame 12507: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.x.26
Transmission Control Protocol, Src Port: 8059 (8059), Dst Port: 64368 (64368), Seq: 203, Ack: 340, Len: 0

No.     Time               Source                Destination           Protocol Length Info
12508 13:04:53.071052    192.168.x.26        192.168.x.x        TCP      60     64368 → 8059 [ACK] Seq=340 Ack=204 Win=65280 Len=0
Frame 12508: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: Micro-St_d4:ca:43 (d4:3d:7e:d4:ca:43), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.x.26, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 64368 (64368), Dst Port: 8059 (8059), Seq: 340, Ack: 204, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12509 13:04:53.192607    clientIP         192.168.x.x        SMTP     76     C: STARTTLS
Frame 12509: 76 bytes on wire (608 bits), 76 bytes captured (608 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 23, Ack: 371, Len: 10
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
  12510 13:04:53.192833    192.168.x.x        clientIP         SMTP     95     S: 220 2.0.0 SMTP server ready
Frame 12510: 95 bytes on wire (760 bits), 95 bytes captured (760 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 371, Ack: 33, Len: 29
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
  12511 13:04:53.414714    clientIP         192.168.x.x        TLSv1    276    Client Hello
Frame 12511: 276 bytes on wire (2208 bits), 276 bytes captured (2208 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 33, Ack: 400, Len: 210
Secure Sockets Layer

No.     Time               Source                Destination           Protocol Length Info
  12512 13:04:53.443803    192.168.x.x        clientIP         TLSv1    1300   Server Hello, Certificate, Server Key Exchange, Server Hello Done
Frame 12512: 1300 bytes on wire (10400 bits), 1300 bytes captured (10400 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 400, Ack: 243, Len: 1234
Secure Sockets Layer

No.     Time               Source                Destination           Protocol Length Info
  12513 13:04:53.646731    192.168.x.x        192.168.y.202       TCP      55     [TCP Keep-Alive] 445 → 49288 [ACK] Seq=1 Ack=1 Win=255 Len=1
Frame 12513: 55 bytes on wire (440 bits), 55 bytes captured (440 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: 192.168.y.202
Transmission Control Protocol, Src Port: 445 (445), Dst Port: 49288 (49288), Seq: 1, Ack: 1, Len: 1
Data (1 byte)
0000  00                                                .

No.     Time               Source                Destination           Protocol Length Info
  12514 13:04:53.647197    192.168.y.202       192.168.x.x        TCP      66     [TCP Keep-Alive ACK] 49288 → 445 [ACK] Seq=1 Ack=2 Win=16334 Len=0 SLE=1 SRE=2
Frame 12514: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: 192.168.y.202, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 49288 (49288), Dst Port: 445 (445), Seq: 1, Ack: 2, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12515 13:04:53.665666    clientIP         192.168.x.x        SMTP     88     C: EHLO mail.clientDoman.in
Frame 12515: 88 bytes on wire (704 bits), 88 bytes captured (704 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 243, Ack: 1634, Len: 22
Simple Mail Transfer Protocol

No.     Time               Source                Destination           Protocol Length Info
12516 13:04:53.666047    192.168.x.x        clientIP         TCP      66     25 → 59299 [FIN, ACK] Seq=1634 Ack=265 Win=64536 Len=0 TSval=69252729 TSecr=2535049915
Frame 12516: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e), Dst: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f)
Internet Protocol Version 4, Src: 192.168.x.x, Dst: clientIP
Transmission Control Protocol, Src Port: 25 (25), Dst Port: 59299 (59299), Seq: 1634, Ack: 265, Len: 0

No.     Time               Source                Destination           Protocol Length Info
  12517 13:04:53.887403    clientIP         192.168.x.x        TCP      66     59299 → 25 [RST, ACK] Seq=265 Ack=1635 Win=17276 Len=0 TSval=2535050137 TSecr=69252729
Frame 12517: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: AxiomTec_4a:20:7f (00:60:e0:4a:20:7f), Dst: IbmCorp_41:1a:4e (e4:1f:13:41:1a:4e)
Internet Protocol Version 4, Src: clientIP, Dst: 192.168.x.x
Transmission Control Protocol, Src Port: 59299 (59299), Dst Port: 25 (25), Seq: 265, Ack: 1635, Len: 0</code></pre><p>Any ideas or suggestions?</p></div><div id="question-tags" class="tags-container tags">communication resets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '16, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/25015116fbc9d7fbeae4f5f671421b4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArtZ&#39;s gravatar image" /><p>ArtZ<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArtZ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '16, 23:43</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55085" class="comments-container"><span id="55126"></span><div id="comment-55126" class="comment"><div id="post-55126-score" class="comment-score"></div><div class="comment-text"><p>You don't show the packets after the TLS Server Hello Done - is that on purpose?<br />
</p><p>You hopefully see a successful TLS handshake continuing with a Client Key Exchange and Encrypted Handshake messages in 17258-17261 .</p><p>Still it is unclear to me why the SMTP client sends another EHLO message after the TLS handshake - if it was successful ...</p></div><div id="comment-55126-info" class="comment-info"><span class="comment-age">(26 Aug '16, 06:34)</span> mrEEde</div></div><span id="55152"></span><div id="comment-55152" class="comment"><div id="post-55152-score" class="comment-score"></div><div class="comment-text"><p>I did not show the packets after the TLS as they were not relevant, they were for other connection. For now I have blocked the client and it seems gone for a while. When it is back I will post the log in more details</p></div><div id="comment-55152-info" class="comment-info"><span class="comment-age">(28 Aug '16, 18:45)</span> ArtZ</div></div><span id="55164"></span><div id="comment-55164" class="comment"><div id="post-55164-score" class="comment-score"></div><div class="comment-text"><p>If those packets were for a different connection then the TLS handshake did not complete !</p><p>... and the client should not continue with another EHLO ....</p></div><div id="comment-55164-info" class="comment-info"><span class="comment-age">(29 Aug '16, 07:13)</span> mrEEde</div></div></div><div id="comment-tools-55085" class="comment-tools"></div><div class="clear"></div><div id="comment-55085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55120"></span>

<div id="answer-container-55120" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55120-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My first thought is that in pkt #12763 the server is implementing a blocking rule for the domain (mail.somedomain.in) advertised in pkt #12762. I'm not sure based on your description if there was a rule in place to block this domain or not, so the block rule assumption may be wrong.</p><p>After marinating on that a bit, it seems like a FIN is too polite to be a block/refusal and the blocking rule should trigger sooner in the conversation. The FIN flag is used to signal that the data stream has been sent and there is nothing more to say, but does not close the session immediately. A RST would be more appropriate for connection refusal based off a filtering rule. The client's RST,ACK response appears to be a commonly observed behavior for certain OS's implementation of the TCP stack or a browser session, in order to tear down the session abruptly if there is nothing more to send.</p><p>One way to determine block behavior would be to setup a deny rule for an address that you own and then start a capture to see what happens when the blocked address attempts to connect to your server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '16, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span> </br></p></div></div><div id="comments-container-55120" class="comments-container"><span id="55153"></span><div id="comment-55153" class="comment"><div id="post-55153-score" class="comment-score"></div><div class="comment-text"><p>I have rechecked and there was no blocking rule for the domain. I have blocked it for now. It is gone for a while (may be for a couple of days or weeks). I will keep an eye to see if it is back again after some time.</p></div><div id="comment-55153-info" class="comment-info"><span class="comment-age">(28 Aug '16, 18:54)</span> ArtZ</div></div><span id="55219"></span><div id="comment-55219" class="comment"><div id="post-55219-score" class="comment-score"></div><div class="comment-text"><p>The issue is back again. I edited my initial question to include the new data. As before, it comes every 20 minutes, from a .in domain (different every time but within .in), from an IP this time located in Canada. If I block the IP or domain, it will go away for a couple of days and will be back after some time again. And this generates Schannel errors (Schannel 36888, The following fatal alert was generated: 10. The internal error state is 10.) on the Exchange Server. It is like an automated action or attack or similar because every time the signature is the same, the client uses Apache on CentOS, the domain name's contact email is always on a free email service(like yahoo, gmail).</p></div><div id="comment-55219-info" class="comment-info"><span class="comment-age">(30 Aug '16, 21:41)</span> ArtZ</div></div><span id="55224"></span><div id="comment-55224" class="comment"><div id="post-55224-score" class="comment-score"></div><div class="comment-text"><p>@mrEEde was right - the client sends an EHLO, gets the server capabilities list, and sends STARTTLS, the server responds 220 server ready and the client initiates the TLS handshake by sending Client Hello. Server responds by Server Hello, but if there are really no other TLS packets in the same TCP session (Client IP:59299 &lt;-&gt; Server IP:25) as the TCP Ack and Seq numbers seem to confirm, it is clearly an issue of the client application which sends another plaintext EHLO rather than finishing the TLS handshake and using it to send further commands.</p><p>As a consequence, my guess No. 1 is that the server sends FIN because there is no way to handle such behaviour in a clean way, and my guess No. 2 is that the client sends a RST because it deems the FIN an erroneous behaviour from its own perspective.</p><p>If you say that this happens for various SMTP clients from <code>.in</code>, is there any security device between your Exchange on private IP address and the client in the internet, or is it just a plain router with NAT and port forwarding? Can you simultaneously capture at the public side of that box to see whether the second EHLO comes from the real client or whether the box forges it?</p></div><div id="comment-55224-info" class="comment-info"><span class="comment-age">(31 Aug '16, 01:33)</span> sindy</div></div></div><div id="comment-tools-55120" class="comment-tools"></div><div class="clear"></div><div id="comment-55120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55251"></span>

<div id="answer-container-55251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Agreed, @mrEEde and @sindy nailed it with their descriptions.</p><p>In regards to the Schannel error, it looks like that is an expected log for when a client misbehaves in the protocol flow and submits an invalid ClientHello to the server.</p><p><a href="https://social.technet.microsoft.com/Forums/exchange/en-US/b327f967-f01a-478b-bba2-0cc4ea25dc15/error-36888-schannel-the-following-fatal-alert-was-generated-10-the-internal-error-state-is?forum=exchange2010">https://social.technet.microsoft.com/Forums/exchange/en-US/b327f967-f01a-478b-bba2-0cc4ea25dc15/error-36888-schannel-the-following-fatal-alert-was-generated-10-the-internal-error-state-is?forum=exchange2010</a></p><p>One of the more interesting things in the capture, besides the client misbehaving and the server responding with a close to the session, is the client that appears in pkt# 12494. The 3-way handshake takes place in pkts 12494-12496. Immediately after that, in pkt# 12497 it sends a TCP segment. The second half of the segment appears in pkt# 12504 - ~200ms later. The reconstructed payload is POST /officescan/cgi/cgiLog.exe HTTP/1.1. The payload is segmented even though it does not need to be (both packets are smaller than full size), most likely to bypass a DPI/SPI. It's strange that an unauthenticated user would be sending a POST request to your exchange server asking it to run an executable. See links for info on the known cgiLog.exe CVE.</p><p><a href="https://www.tenable.com/pvs-plugins/4724">https://www.tenable.com/pvs-plugins/4724</a></p><p><a href="http://www.secuobs.com/plugs/34490.shtml">http://www.secuobs.com/plugs/34490.shtml</a><br />
</p><p>Even more interesting, is the fact the server responds back with a HTTP/1.1 200 OK. In a POST request, the response will contain an entity describing or containing the result of the action. I would dig into the contents of that payload to determine if the .exe was run, the results of the execution, and what is returned to this client. Based off this behavior, the clients from the .in domain appear to be either abusing the TLS protocol or are crafting malicious payloads and probing servers. I would deny that entire .in domain if it doesn't cause an outage for your legit users.</p><p>If your not using Trend Micro for security you may want to look into if it is installed and removing it. <a href="https://www.reasoncoresecurity.com/cgilog.exe-ddcd8f683819d9fda9ec1474757a05212c1d321b.aspx">https://www.reasoncoresecurity.com/cgilog.exe-ddcd8f683819d9fda9ec1474757a05212c1d321b.aspx</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '16, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '16, 12:38</p></div></div><div id="comments-container-55251" class="comments-container"></div><div id="comment-tools-55251" class="comment-tools"></div><div class="clear"></div><div id="comment-55251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

