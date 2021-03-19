+++
type = "question"
title = "could someone tell me what a microsoft interface is.  I have had all kinds of problems with network.  Is this normal?  This is home computer that may have been hijacked."
description = '''No. Time Source Destination Protocol Info  1 0.000000 74.125.227.116 192.168.1.3 TLSv1 Application Data  Frame 1: 115 bytes on wire (920 bits), 115 bytes captured (920 bits) Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e) Internet Protocol, Src: 74....'''
date = "2012-03-26T19:09:00Z"
lastmod = "2012-03-26T23:47:00Z"
weight = 9777
keywords = [ "interface", "microsoft" ]
aliases = [ "/questions/9777" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [could someone tell me what a microsoft interface is. I have had all kinds of problems with network. Is this normal? This is home computer that may have been hijacked.](/questions/9777/could-someone-tell-me-what-a-microsoft-interface-is-i-have-had-all-kinds-of-problems-with-network-is-this-normal-this-is-home-computer-that-may-have-been-hijacked)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9777-score" class="post-score" title="current number of votes">-2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>No.     Time        Source                Destination           Protocol Info
      1 0.000000    74.125.227.116        192.168.1.3           TLSv1    Application Data

Frame 1: 115 bytes on wire (920 bits), 115 bytes captured (920 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.116 (74.125.227.116), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 53933 (53933), Seq: 1, Ack: 1, Len: 61
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
      2 0.000507    74.125.227.116        192.168.1.3           TLSv1    Application Data

Frame 2: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.116 (74.125.227.116), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 53933 (53933), Seq: 62, Ack: 1, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
      3 0.000636    192.168.1.3           74.125.227.116        TCP      53933 &gt; https [ACK] Seq=1 Ack=99 Win=55439 Len=0

Frame 3: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.116 (74.125.227.116)
Transmission Control Protocol, Src Port: 53933 (53933), Dst Port: https (443), Seq: 1, Ack: 99, Len: 0

No.     Time        Source                Destination           Protocol Info
      4 0.000860    74.125.227.116        192.168.1.3           TCP      https &gt; 53933 [FIN, ACK] Seq=99 Ack=1 Win=10374 Len=0

Frame 4: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.116 (74.125.227.116), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 53933 (53933), Seq: 99, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Info
      5 0.000927    192.168.1.3           74.125.227.116        TCP      53933 &gt; https [ACK] Seq=1 Ack=100 Win=55439 Len=0

Frame 5: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.116 (74.125.227.116)
Transmission Control Protocol, Src Port: 53933 (53933), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
      6 0.001974    192.168.1.3           74.125.227.116        TCP      53933 &gt; https [FIN, ACK] Seq=1 Ack=100 Win=55439 Len=0

Frame 6: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.116 (74.125.227.116)
Transmission Control Protocol, Src Port: 53933 (53933), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
      7 0.034845    74.125.227.116        192.168.1.3           TCP      https &gt; 53933 [ACK] Seq=100 Ack=2 Win=10374 Len=0

Frame 7: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.116 (74.125.227.116), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 53933 (53933), Seq: 100, Ack: 2, Len: 0

No.     Time        Source                Destination           Protocol Info
      8 0.358743    74.125.227.109        192.168.1.3           TLSv1    Application Data

Frame 8: 115 bytes on wire (920 bits), 115 bytes captured (920 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.109 (74.125.227.109), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54094 (54094), Seq: 1, Ack: 1, Len: 61
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
      9 0.359312    74.125.227.109        192.168.1.3           TLSv1    Application Data

Frame 9: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.109 (74.125.227.109), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54094 (54094), Seq: 62, Ack: 1, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     10 0.359397    192.168.1.3           74.125.227.109        TCP      54094 &gt; https [ACK] Seq=1 Ack=99 Win=4102 Len=0

Frame 10: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.109 (74.125.227.109)
Transmission Control Protocol, Src Port: 54094 (54094), Dst Port: https (443), Seq: 1, Ack: 99, Len: 0

No.     Time        Source                Destination           Protocol Info
     11 0.359840    74.125.227.109        192.168.1.3           TCP      https &gt; 54094 [FIN, ACK] Seq=99 Ack=1 Win=145 Len=0

Frame 11: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.109 (74.125.227.109), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54094 (54094), Seq: 99, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Info
     12 0.359888    192.168.1.3           74.125.227.109        TCP      54094 &gt; https [ACK] Seq=1 Ack=100 Win=4102 Len=0

Frame 12: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.109 (74.125.227.109)
Transmission Control Protocol, Src Port: 54094 (54094), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     13 0.360493    192.168.1.3           74.125.227.109        TCP      54094 &gt; https [FIN, ACK] Seq=1 Ack=100 Win=4102 Len=0

Frame 13: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.109 (74.125.227.109)
Transmission Control Protocol, Src Port: 54094 (54094), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     14 0.392622    74.125.227.109        192.168.1.3           TCP      https &gt; 54094 [ACK] Seq=100 Ack=2 Win=145 Len=0

Frame 14: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.109 (74.125.227.109), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54094 (54094), Seq: 100, Ack: 2, Len: 0

No.     Time        Source                Destination           Protocol Info
     15 1.075340    74.125.227.125        192.168.1.3           TLSv1    Application Data

Frame 15: 115 bytes on wire (920 bits), 115 bytes captured (920 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.125 (74.125.227.125), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54096 (54096), Seq: 1, Ack: 1, Len: 61
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     16 1.075872    74.125.227.125        192.168.1.3           TLSv1    Application Data

Frame 16: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.125 (74.125.227.125), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54096 (54096), Seq: 62, Ack: 1, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     17 1.076017    192.168.1.3           74.125.227.125        TCP      54096 &gt; https [ACK] Seq=1 Ack=99 Win=4083 Len=0

Frame 17: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.125 (74.125.227.125)
Transmission Control Protocol, Src Port: 54096 (54096), Dst Port: https (443), Seq: 1, Ack: 99, Len: 0

No.     Time        Source                Destination           Protocol Info
     18 1.076244    74.125.227.125        192.168.1.3           TCP      https &gt; 54096 [FIN, ACK] Seq=99 Ack=1 Win=196 Len=0

Frame 18: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.125 (74.125.227.125), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54096 (54096), Seq: 99, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Info
     19 1.076308    192.168.1.3           74.125.227.125        TCP      54096 &gt; https [ACK] Seq=1 Ack=100 Win=4083 Len=0

Frame 19: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.125 (74.125.227.125)
Transmission Control Protocol, Src Port: 54096 (54096), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     20 1.077449    192.168.1.3           74.125.227.125        TCP      54096 &gt; https [FIN, ACK] Seq=1 Ack=100 Win=4083 Len=0

Frame 20: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.125 (74.125.227.125)
Transmission Control Protocol, Src Port: 54096 (54096), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     21 1.109326    74.125.227.125        192.168.1.3           TCP      https &gt; 54096 [ACK] Seq=100 Ack=2 Win=196 Len=0

Frame 21: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.125 (74.125.227.125), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54096 (54096), Seq: 100, Ack: 2, Len: 0

No.     Time        Source                Destination           Protocol Info
     22 1.337220    74.125.227.138        192.168.1.3           TLSv1    Application Data

Frame 22: 115 bytes on wire (920 bits), 115 bytes captured (920 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.138 (74.125.227.138), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54092 (54092), Seq: 1, Ack: 1, Len: 61
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     23 1.338192    74.125.227.138        192.168.1.3           TLSv1    Application Data

Frame 23: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.138 (74.125.227.138), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54092 (54092), Seq: 62, Ack: 1, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     24 1.338281    192.168.1.3           74.125.227.138        TCP      54092 &gt; https [ACK] Seq=1 Ack=99 Win=4290 Len=0

Frame 24: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.138 (74.125.227.138)
Transmission Control Protocol, Src Port: 54092 (54092), Dst Port: https (443), Seq: 1, Ack: 99, Len: 0

No.     Time        Source                Destination           Protocol Info
     25 1.339131    74.125.227.138        192.168.1.3           TCP      https &gt; 54092 [FIN, ACK] Seq=99 Ack=1 Win=157 Len=0

Frame 25: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.138 (74.125.227.138), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54092 (54092), Seq: 99, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Info
     26 1.339208    192.168.1.3           74.125.227.138        TCP      54092 &gt; https [ACK] Seq=1 Ack=100 Win=4290 Len=0

Frame 26: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.138 (74.125.227.138)
Transmission Control Protocol, Src Port: 54092 (54092), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     27 1.339420    192.168.1.3           74.125.227.138        TCP      54092 &gt; https [FIN, ACK] Seq=1 Ack=100 Win=4290 Len=0

Frame 27: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.138 (74.125.227.138)
Transmission Control Protocol, Src Port: 54092 (54092), Dst Port: https (443), Seq: 1, Ack: 100, Len: 0

No.     Time        Source                Destination           Protocol Info
     28 1.373024    74.125.227.138        192.168.1.3           TCP      https &gt; 54092 [ACK] Seq=100 Ack=2 Win=157 Len=0

Frame 28: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.138 (74.125.227.138), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54092 (54092), Seq: 100, Ack: 2, Len: 0

No.     Time        Source                Destination           Protocol Info
     29 1.596468    192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 29: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1, Ack: 1, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     30 1.597747    192.168.1.3           74.125.227.118        TCP      [TCP segment of a reassembled PDU]

Frame 30: 1484 bytes on wire (11872 bits), 1484 bytes captured (11872 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 38, Ack: 1, Len: 1430

No.     Time        Source                Destination           Protocol Info
     31 1.597912    192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 31: 150 bytes on wire (1200 bits), 150 bytes captured (1200 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1468, Ack: 1, Len: 96
[Reassembled TCP Segments (1526 bytes): #30(1430), #31(96)]
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     32 1.598033    192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 32: 163 bytes on wire (1304 bits), 163 bytes captured (1304 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1564, Ack: 1, Len: 109
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     33 1.628470    74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 33: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 1, Ack: 38, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     34 1.662142    74.125.227.118        192.168.1.3           TCP      https &gt; 54078 [ACK] Seq=38 Ack=1564 Win=62920 Len=0

Frame 34: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 38, Ack: 1564, Len: 0

No.     Time        Source                Destination           Protocol Info
     35 1.708089    74.125.227.118        192.168.1.3           TCP      https &gt; 54078 [ACK] Seq=38 Ack=1673 Win=62920 Len=0

Frame 35: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 38, Ack: 1673, Len: 0

No.     Time        Source                Destination           Protocol Info
     36 1.749118    74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 36: 109 bytes on wire (872 bits), 109 bytes captured (872 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 38, Ack: 1673, Len: 55
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     37 1.749250    192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=1673 Ack=93 Win=64082 Len=0

Frame 37: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1673, Ack: 93, Len: 0

No.     Time        Source                Destination           Protocol Info
     38 1.749456    74.125.227.118        192.168.1.3           TLSv1    Application Data, Application Data

Frame 38: 123 bytes on wire (984 bits), 123 bytes captured (984 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 93, Ack: 1673, Len: 69
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     39 1.948380    192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=1673 Ack=162 Win=64013 Len=0

Frame 39: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1673, Ack: 162, Len: 0

No.     Time        Source                Destination           Protocol Info
     40 2.595793    192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 40: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1673, Ack: 162, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     41 2.627464    74.125.227.118        192.168.1.3           TCP      https &gt; 54078 [ACK] Seq=162 Ack=1710 Win=62920 Len=0

Frame 41: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 162, Ack: 1710, Len: 0

No.     Time        Source                Destination           Protocol Info
     42 2.628065    74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 42: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 162, Ack: 1710, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     43 2.827420    192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=1710 Ack=199 Win=63976 Len=0

Frame 43: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1710, Ack: 199, Len: 0

No.     Time        Source                Destination           Protocol Info
     44 8.973717    74.125.227.118        192.168.1.3           TLSv1    Application Data, Application Data

Frame 44: 133 bytes on wire (1064 bits), 133 bytes captured (1064 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 199, Ack: 1710, Len: 79
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     45 9.173590    192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=1710 Ack=278 Win=63897 Len=0

Frame 45: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1710, Ack: 278, Len: 0

No.     Time        Source                Destination           Protocol Info
     46 24.496733   192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 46: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1710, Ack: 278, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     47 24.498178   192.168.1.3           74.125.227.118        TCP      [TCP segment of a reassembled PDU]

Frame 47: 1484 bytes on wire (11872 bits), 1484 bytes captured (11872 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 1747, Ack: 278, Len: 1430

No.     Time        Source                Destination           Protocol Info
     48 24.498359   192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 48: 345 bytes on wire (2760 bits), 345 bytes captured (2760 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3177, Ack: 278, Len: 291
[Reassembled TCP Segments (1721 bytes): #47(1430), #48(291)]
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     49 24.529195   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 49: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 278, Ack: 1747, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     50 24.566769   74.125.227.118        192.168.1.3           TCP      https &gt; 54078 [ACK] Seq=315 Ack=3468 Win=62920 Len=0

Frame 50: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 315, Ack: 3468, Len: 0

No.     Time        Source                Destination           Protocol Info
     51 24.729074   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3468 Ack=315 Win=63860 Len=0

Frame 51: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 315, Len: 0

No.     Time        Source                Destination           Protocol Info
     52 24.930140   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 52: 189 bytes on wire (1512 bits), 189 bytes captured (1512 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 315, Ack: 3468, Len: 135
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     53 24.933791   74.125.227.118        192.168.1.3           TLSv1    Application Data, Application Data

Frame 53: 1404 bytes on wire (11232 bits), 1404 bytes captured (11232 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 450, Ack: 3468, Len: 1350
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     54 24.933887   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3468 Ack=1800 Win=62375 Len=0

Frame 54: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 1800, Len: 0

No.     Time        Source                Destination           Protocol Info
     55 24.937923   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 55: 1404 bytes on wire (11232 bits), 1404 bytes captured (11232 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 1800, Ack: 3468, Len: 1350
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     56 24.939749   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 56: 886 bytes on wire (7088 bits), 886 bytes captured (7088 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 3150, Ack: 3468, Len: 832
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     57 24.939841   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3468 Ack=3982 Win=62920 Len=0

Frame 57: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 3982, Len: 0

No.     Time        Source                Destination           Protocol Info
     58 24.943481   74.125.227.118        192.168.1.3           TLSv1    Application Data, Application Data

Frame 58: 1404 bytes on wire (11232 bits), 1404 bytes captured (11232 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 3982, Ack: 3468, Len: 1350
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     59 24.946799   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 59: 1404 bytes on wire (11232 bits), 1404 bytes captured (11232 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 5332, Ack: 3468, Len: 1350
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     60 24.946925   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3468 Ack=6682 Win=64350 Len=0

Frame 60: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 6682, Len: 0

No.     Time        Source                Destination           Protocol Info
     61 24.947503   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 61: 418 bytes on wire (3344 bits), 418 bytes captured (3344 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 6682, Ack: 3468, Len: 364
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     62 25.150162   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3468 Ack=7046 Win=63986 Len=0

Frame 62: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 7046, Len: 0

No.     Time        Source                Destination           Protocol Info
     63 25.496729   192.168.1.3           74.125.227.118        TLSv1    Application Data

Frame 63: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3468, Ack: 7046, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     64 25.528416   74.125.227.118        192.168.1.3           TLSv1    Application Data

Frame 64: 91 bytes on wire (728 bits), 91 bytes captured (728 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 7046, Ack: 3505, Len: 37
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     65 25.728058   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3505 Ack=7083 Win=63949 Len=0

Frame 65: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3505, Ack: 7083, Len: 0

No.     Time        Source                Destination           Protocol Info
     66 29.352313   Arcadyan_05:ae:6e     Netgear_6b:01:1c      ARP      Who has 192.168.1.1?  Tell 192.168.1.3

Frame 66: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Address Resolution Protocol (request)

No.     Time        Source                Destination           Protocol Info
     67 29.354726   Netgear_6b:01:1c      Arcadyan_05:ae:6e     ARP      192.168.1.1 is at e0:46:9a:6b:01:1c

Frame 67: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Address Resolution Protocol (reply)

No.     Time        Source                Destination           Protocol Info
     68 35.249117   74.125.227.118        192.168.1.3           TLSv1    Application Data, Application Data

Frame 68: 133 bytes on wire (1064 bits), 133 bytes captured (1064 bits)
Ethernet II, Src: Netgear_6b:01:1c (e0:46:9a:6b:01:1c), Dst: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e)
Internet Protocol, Src: 74.125.227.118 (74.125.227.118), Dst: 192.168.1.3 (192.168.1.3)
Transmission Control Protocol, Src Port: https (443), Dst Port: 54078 (54078), Seq: 7083, Ack: 3505, Len: 79
Secure Socket Layer

No.     Time        Source                Destination           Protocol Info
     69 35.448534   192.168.1.3           74.125.227.118        TCP      54078 &gt; https [ACK] Seq=3505 Ack=7162 Win=63870 Len=0

Frame 69: 54 bytes on wire (432 bits), 54 bytes captured (432 bits)
Ethernet II, Src: Arcadyan_05:ae:6e (7c:4f:b5:05:ae:6e), Dst: Netgear_6b:01:1c (e0:46:9a:6b:01:1c)
Internet Protocol, Src: 192.168.1.3 (192.168.1.3), Dst: 74.125.227.118 (74.125.227.118)
Transmission Control Protocol, Src Port: 54078 (54078), Dst Port: https (443), Seq: 3505, Ack: 7162, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags">interface microsoft</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '12, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/677274c9b147b884e802472c53024fff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="russfromokla&#39;s gravatar image" /><p>russfromokla<br />
<span class="score" title="-1 reputation points">-1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="russfromokla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '12, 02:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9777" class="comments-container"></div><div id="comment-tools-9777" class="comment-tools"></div><div class="clear"></div><div id="comment-9777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9781"></span>

<div id="answer-container-9781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9781-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of issues with your question that will prevent you getting a satisfactory answer:</p><ol><li>Wireshark is a packet analyzer and although it can be used to find some information about networking issues caused by virus infections, it isn't the best tool for the job.</li><li>Posting a large screed of text from a capture isn't easy to look at, the actual capture posted on a site such as CloudShark is much more useful, with the caution that your capture may contain sensitive personal information so should be reviewed as such before posting in a public place.</li><li>Your capture appears to show traffic that is encrypted by SSL/TLS. As such, without the private key from the remote server it can't be decrypted.</li></ol><p>Also posting essentially duplicate questions doesn't get you an answer twice as quickly.</p><p>I think you'll be better off going to a specialist anti-virus forum such as <a href="http://forums.majorgeeks.com/showthread.php?t=35407">MajorGeeks</a>. Read the instructions carefully and follow them precisely and the fine folks there will help you out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9781" class="comments-container"></div><div id="comment-tools-9781" class="comment-tools"></div><div class="clear"></div><div id="comment-9781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

