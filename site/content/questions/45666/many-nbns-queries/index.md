+++
type = "question"
title = "many NBNS... queries"
description = '''Hello! I&#x27;m new here in the world of networking and in wireshark too. I&#x27;ve been seeing so much activity with the protocol NBNS and others related and want to know if it is normal or not. I Think it is not normal. The internet velocity has decreased. Please help! here a capture of wireshark (in bold w...'''
date = "2015-09-07T08:41:00Z"
lastmod = "2015-09-08T08:14:00Z"
weight = 45666
keywords = [ "nbns" ]
aliases = [ "/questions/45666" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [many NBNS... queries](/questions/45666/many-nbns-queries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45666-score" class="post-score" title="current number of votes">0</div><span id="post-45666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I'm new here in the world of networking and in wireshark too. I've been seeing so much activity with the protocol NBNS and others related and want to know if it is normal or not. I Think it is not normal. The internet velocity has decreased. Please help!</p><p>here a capture of wireshark (in bold what I see):</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
      1 0.000000    0.0.0.0               255.255.255.255       DHCP     342    DHCP Discover - Transaction ID 0x116c2541

Frame 1: 342 bytes on wire (2736 bits), 342 bytes captured (2736 bits)
Ethernet II, Src: 48:f8:b3:22:0f:a6 (48:f8:b3:22:0f:a6), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 0.0.0.0 (0.0.0.0), Dst: 255.255.255.255 (255.255.255.255)
User Datagram Protocol, Src Port: bootpc (68), Dst Port: bootps (67)
Bootstrap Protocol

No.     Time        Source                Destination           Protocol Length Info
      2 0.236672    fe80::f0a1:beec:ef8e:f67a ff02::c               SSDP     181    M-SEARCH * HTTP/1.1

Frame 2: 181 bytes on wire (1448 bits), 181 bytes captured (1448 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: IPv6mcast_00:00:00:0c (33:33:00:00:00:0c)
Internet Protocol Version 6, Src: fe80::f0a1:beec:ef8e:f67a (fe80::f0a1:beec:ef8e:f67a), Dst: ff02::c (ff02::c)
User Datagram Protocol, Src Port: 58769 (58769), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

No.     Time        Source                Destination           Protocol Length Info
      3 0.236860    192.9.205.101         239.255.255.250       SSDP     167    M-SEARCH * HTTP/1.1

Frame 3: 167 bytes on wire (1336 bits), 167 bytes captured (1336 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 239.255.255.250 (239.255.255.250)
User Datagram Protocol, Src Port: 58771 (58771), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

No.     Time        Source                Destination           Protocol Length Info
      4 0.237597    fe80::f0a1:beec:ef8e:f67a ff02::c               SSDP     179    M-SEARCH * HTTP/1.1

Frame 4: 179 bytes on wire (1432 bits), 179 bytes captured (1432 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: IPv6mcast_00:00:00:0c (33:33:00:00:00:0c)
Internet Protocol Version 6, Src: fe80::f0a1:beec:ef8e:f67a (fe80::f0a1:beec:ef8e:f67a), Dst: ff02::c (ff02::c)
User Datagram Protocol, Src Port: 58769 (58769), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

No.     Time        Source                Destination           Protocol Length Info
      5 0.237728    192.9.205.101         239.255.255.250       SSDP     165    M-SEARCH * HTTP/1.1

Frame 5: 165 bytes on wire (1320 bits), 165 bytes captured (1320 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 239.255.255.250 (239.255.255.250)
User Datagram Protocol, Src Port: 58771 (58771), Dst Port: ssdp (1900)
Hypertext Transfer Protocol

**No.     Time        Source             Destination           Protocol Length Info
      6 0.503913    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 6: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
      7 0.958494    192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 7: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
      8 1.126748    201.248.76.123        192.9.205.125         TCP      66     https &gt; 38942 [ACK] Seq=1 Ack=1 Win=1201 Len=0 TSval=1501769264 TSecr=1823832

Frame 8: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 201.248.76.123 (201.248.76.123), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38942 (38942), Seq: 1, Ack: 1, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
      9 1.253602    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 9: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     10 1.415554    192.9.205.125         199.16.156.52         TCP      66     46968 &gt; https [ACK] Seq=1 Ack=1 Win=2550 Len=0 TSval=1847730 TSecr=1154942667

Frame 10: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 199.16.156.52 (199.16.156.52)
Transmission Control Protocol, Src Port: 46968 (46968), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     11 1.708104    192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 11: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     12 2.003606    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 12: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     13 2.379740    192.9.205.112         192.9.205.255         BROWSER  243    Host Announcement JUNIOR-PC, Workstation, Server, Print Queue Server, NT Workstation, Potential Browser**

Frame 13: 243 bytes on wire (1944 bits), 243 bytes captured (1944 bits)
Ethernet II, Src: AsrockIn_38:96:98 (00:25:22:38:96:98), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.112 (192.9.205.112), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-dgm (138), Dst Port: netbios-dgm (138)
NetBIOS Datagram Service
SMB (Server Message Block Protocol)
SMB MailSlot Protocol
Microsoft Windows Browser Protocol

**No.     Time        Source                Destination           Protocol Length Info
     14 2.457990    192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 14: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     15 2.755773    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 15: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     16 3.210501    QuantaCo_1b:04:47     Broadcast             ARP      60     Who has 192.9.205.5?  Tell 192.9.205.122**

Frame 16: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time        Source                Destination           Protocol Length Info
     17 3.271072    199.16.156.52         192.9.205.125         TCP      66     [TCP ACKed lost segment] https &gt; 46968 [ACK] Seq=1 Ack=2 Win=139 Len=0 TSval=1154989370 TSecr=1754934

Frame 17: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 199.16.156.52 (199.16.156.52), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 46968 (46968), Seq: 1, Ack: 2, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     18 3.505728    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 18: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     19 3.871562    192.9.205.125         173.194.216.188       TCP      66     52811 &gt; hpvroom [ACK] Seq=1 Ack=1 Win=2288 Len=0 TSval=1848344 TSecr=165495603

Frame 19: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 173.194.216.188 (173.194.216.188)
Transmission Control Protocol, Src Port: 52811 (52811), Dst Port: hpvroom (5228), Seq: 1, Ack: 1, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     20 4.255774    192.9.205.101         192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 20: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: Elitegro_cf:f9:8c (00:25:11:cf:f9:8c), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.101 (192.9.205.101), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     21 5.505831    fe80::b089:aa83:ac1f:2fe2 ff02::1:3             LLMNR    89     Standard query A ELIANA-PC**

Frame 21: 89 bytes on wire (712 bits), 89 bytes captured (712 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b089:aa83:ac1f:2fe2 (fe80::b089:aa83:ac1f:2fe2), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 62764 (62764), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     22 5.506030    192.9.205.18          224.0.0.252           LLMNR    69     Standard query A ELIANA-PC**

Frame 22: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 52816 (52816), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     23 5.606255    fe80::b089:aa83:ac1f:2fe2 ff02::1:3             LLMNR    89     Standard query A ELIANA-PC**

Frame 23: 89 bytes on wire (712 bits), 89 bytes captured (712 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b089:aa83:ac1f:2fe2 (fe80::b089:aa83:ac1f:2fe2), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 62764 (62764), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     24 5.606288    192.9.205.18          224.0.0.252           LLMNR    69     Standard query A ELIANA-PC**

Frame 24: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 52816 (52816), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     25 5.806577    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 25: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     26 5.954897    173.194.216.188       192.9.205.125         TCP      66     [TCP ACKed lost segment] hpvroom &gt; 52811 [ACK] Seq=1 Ack=2 Win=366 Len=0 TSval=165543213 TSecr=1778826

Frame 26: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 173.194.216.188 (173.194.216.188), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: hpvroom (5228), Dst Port: 52811 (52811), Seq: 1, Ack: 2, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     27 6.556177    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 27: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     28 7.306170    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 28: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     29 7.541744    AsrockIn_c6:5a:76     Broadcast             ARP      60     Who has 192.9.205.5?  Tell 192.9.205.15

Frame 29: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

**No.     Time        Source                Destination           Protocol Length Info
     30 8.058309    fe80::b089:aa83:ac1f:2fe2 ff02::1:3             LLMNR    89     Standard query A ELIANA-PC**

Frame 30: 89 bytes on wire (712 bits), 89 bytes captured (712 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b089:aa83:ac1f:2fe2 (fe80::b089:aa83:ac1f:2fe2), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 62272 (62272), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     31 8.058580    192.9.205.18          224.0.0.252           LLMNR    69     Standard query A ELIANA-PC**

Frame 31: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 60755 (60755), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     32 8.161522    fe80::b089:aa83:ac1f:2fe2 ff02::1:3             LLMNR    89     Standard query A ELIANA-PC**

Frame 32: 89 bytes on wire (712 bits), 89 bytes captured (712 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b089:aa83:ac1f:2fe2 (fe80::b089:aa83:ac1f:2fe2), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 62272 (62272), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     33 8.161601    192.9.205.18          224.0.0.252           LLMNR    69     Standard query A ELIANA-PC**

Frame 33: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 60755 (60755), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     34 8.361425    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 34: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     35 9.111204    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 35: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

**No.     Time        Source                Destination           Protocol Length Info
     36 9.861224    192.9.205.18          192.9.205.255         NBNS     92     Name query NB ELIANA-PC&lt;20&gt;**

Frame 36: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     37 10.044808   192.9.205.125         91.189.89.22          TCP      74     44618 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=1849887 TSecr=0 WS=16

Frame 37: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 0, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     38 10.109680   AsrockIn_0d:ce:69     Broadcast             ARP      60     Who has 192.9.205.122?  Tell 192.9.205.54**

Frame 38: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: AsrockIn_0d:ce:69 (bc:5f:f4:0d:ce:69), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Address Resolution Protocol (request)

No.     Time        Source                Destination           Protocol Length Info
     39 10.955187   Cisco-Li_84:64:18     fc:aa:14:50:17:45     ARP      60     Who has 192.9.205.125?  Tell 192.9.205.5

Frame 39: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Address Resolution Protocol (request)

No.     Time        Source                Destination           Protocol Length Info
     40 10.955195   fc:aa:14:50:17:45     Cisco-Li_84:64:18     ARP      42     192.9.205.125 is at fc:aa:14:50:17:45

Frame 40: 42 bytes on wire (336 bits), 42 bytes captured (336 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Address Resolution Protocol (reply)

No.     Time        Source                Destination           Protocol Length Info
     41 11.021178   74.125.141.189        192.9.205.125         TLSv1.2  126    Application Data

Frame 41: 126 bytes on wire (1008 bits), 126 bytes captured (1008 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 74.125.141.189 (74.125.141.189), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 39708 (39708), Seq: 1, Ack: 1, Len: 60
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     42 11.021208   192.9.205.125         74.125.141.189        TCP      66     39708 &gt; https [ACK] Seq=1 Ack=61 Win=1306 Len=0 TSval=1850131 TSecr=4033384573

Frame 42: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 74.125.141.189 (74.125.141.189)
Transmission Control Protocol, Src Port: 39708 (39708), Dst Port: https (443), Seq: 1, Ack: 61, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     43 11.043563   192.9.205.125         91.189.89.22          TCP      74     44618 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=1850137 TSecr=0 WS=16

Frame 43: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 0, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     44 11.345497   91.189.89.22          192.9.205.125         TCP      74     https &gt; 44618 [SYN, ACK] Seq=0 Ack=1 Win=14480 Len=0 MSS=536 SACK_PERM=1 TSval=463463289 TSecr=1849887 WS=128

Frame 44: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     45 11.345515   192.9.205.125         91.189.89.22          TCP      66     44618 &gt; https [ACK] Seq=1 Ack=1 Win=14608 Len=0 TSval=1850212 TSecr=463463289

Frame 45: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     46 11.345683   192.9.205.125         91.189.89.22          SSLv3    138    Client Hello

Frame 46: 138 bytes on wire (1104 bits), 138 bytes captured (1104 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 1, Ack: 1, Len: 72
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     47 11.583826   192.9.205.125         8.8.8.8               DNS      76     Standard query A daisy.ubuntu.com

Frame 47: 76 bytes on wire (608 bits), 76 bytes captured (608 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 8.8.8.8 (8.8.8.8)
User Datagram Protocol, Src Port: 19644 (19644), Dst Port: domain (53)
Domain Name System (query)

No.     Time        Source                Destination           Protocol Length Info
     48 11.713600   fe80::b17d:20ce:f940:c364 ff02::1:3             LLMNR    84     Standard query A wpad

Frame 48: 84 bytes on wire (672 bits), 84 bytes captured (672 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b17d:20ce:f940:c364 (fe80::b17d:20ce:f940:c364), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 54835 (54835), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     49 11.713722   192.9.205.15          224.0.0.252           LLMNR    64     Standard query A wpad**

Frame 49: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.15 (192.9.205.15), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 55249 (55249), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     50 11.814725   fe80::b17d:20ce:f940:c364 ff02::1:3             LLMNR    84     Standard query A wpad**

Frame 50: 84 bytes on wire (672 bits), 84 bytes captured (672 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: IPv6mcast_00:01:00:03 (33:33:00:01:00:03)
Internet Protocol Version 6, Src: fe80::b17d:20ce:f940:c364 (fe80::b17d:20ce:f940:c364), Dst: ff02::1:3 (ff02::1:3)
User Datagram Protocol, Src Port: 54835 (54835), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

**No.     Time        Source                Destination           Protocol Length Info
     51 11.814728   192.9.205.15          224.0.0.252           LLMNR    64     Standard query A wpad**

Frame 51: 64 bytes on wire (512 bits), 64 bytes captured (512 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: IPv4mcast_00:00:fc (01:00:5e:00:00:fc)
Internet Protocol Version 4, Src: 192.9.205.15 (192.9.205.15), Dst: 224.0.0.252 (224.0.0.252)
User Datagram Protocol, Src Port: 55249 (55249), Dst Port: llmnr (5355)
Link-local Multicast Name Resolution (query)

No.     Time        Source                Destination           Protocol Length Info
     52 11.873409   fe80::f8ed:8a7f:a3bf:9878 ff02::1:2             DHCPv6   153    Solicit XID: 0x1598c3 CID: 000100011bed42b60030673cbef7

Frame 52: 153 bytes on wire (1224 bits), 153 bytes captured (1224 bits)
Ethernet II, Src: BiostarM_3c:be:f7 (00:30:67:3c:be:f7), Dst: IPv6mcast_00:01:00:02 (33:33:00:01:00:02)
Internet Protocol Version 6, Src: fe80::f8ed:8a7f:a3bf:9878 (fe80::f8ed:8a7f:a3bf:9878), Dst: ff02::1:2 (ff02::1:2)
User Datagram Protocol, Src Port: dhcpv6-client (546), Dst Port: dhcpv6-server (547)
DHCPv6

No.     Time        Source                Destination           Protocol Length Info
     53 11.898973   192.9.205.125         8.8.8.8               DNS      75     Standard query A mail.google.com

Frame 53: 75 bytes on wire (600 bits), 75 bytes captured (600 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 8.8.8.8 (8.8.8.8)
User Datagram Protocol, Src Port: 10088 (10088), Dst Port: domain (53)
Domain Name System (query)

No.     Time        Source                Destination           Protocol Length Info
     54 11.901424   108.160.170.45        192.9.205.125         TLSv1    391    Application Data

Frame 54: 391 bytes on wire (3128 bits), 391 bytes captured (3128 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 108.160.170.45 (108.160.170.45), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 46949 (46949), Seq: 1, Ack: 1, Len: 325
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     55 11.902528   192.9.205.125         108.160.170.45        TLSv1    492    Application Data, Application Data

Frame 55: 492 bytes on wire (3936 bits), 492 bytes captured (3936 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 108.160.170.45 (108.160.170.45)
Transmission Control Protocol, Src Port: 46949 (46949), Dst Port: https (443), Seq: 1, Ack: 326, Len: 426
Secure Sockets Layer

**No.     Time        Source                Destination           Protocol Length Info
     56 12.017731   192.9.205.15          192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 56: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.15 (192.9.205.15), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     57 12.251209   91.189.89.22          192.9.205.125         TCP      74     https &gt; 44618 [SYN, ACK] Seq=0 Ack=1 Win=14480 Len=0 MSS=536 SACK_PERM=1 TSval=463463540 TSecr=1849887 WS=128

Frame 57: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     58 12.251215   192.9.205.125         91.189.89.22          TCP      66     [TCP Dup ACK 46#1] 44618 &gt; https [ACK] Seq=73 Ack=1 Win=14608 Len=0 TSval=1850438 TSecr=463463289

Frame 58: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 73, Ack: 1, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     59 12.596406   192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 59: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     60 12.763447   91.189.89.22          192.9.205.125         TCP      66     https &gt; 44618 [ACK] Seq=1 Ack=73 Win=14592 Len=0 TSval=463463617 TSecr=1850212

Frame 60: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 1, Ack: 73, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     61 12.765183   91.189.89.22          192.9.205.125         SSLv3    73     Alert (Level: Fatal, Description: Handshake Failure)

Frame 61: 73 bytes on wire (584 bits), 73 bytes captured (584 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 1, Ack: 73, Len: 7
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     62 12.765200   192.9.205.125         91.189.89.22          TCP      66     44618 &gt; https [ACK] Seq=73 Ack=8 Win=14608 Len=0 TSval=1850567 TSecr=463463617

Frame 62: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 73, Ack: 8, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     63 12.765286   192.9.205.125         91.189.89.22          TCP      66     44618 &gt; https [FIN, ACK] Seq=73 Ack=8 Win=14608 Len=0 TSval=1850567 TSecr=463463617

Frame 63: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 73, Ack: 8, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     64 12.765321   91.189.89.22          192.9.205.125         TCP      66     https &gt; 44618 [FIN, ACK] Seq=8 Ack=73 Win=14592 Len=0 TSval=463463617 TSecr=1850212

Frame 64: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 8, Ack: 73, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     65 12.765327   192.9.205.125         91.189.89.22          TCP      66     44618 &gt; https [ACK] Seq=74 Ack=9 Win=14608 Len=0 TSval=1850567 TSecr=463463617

Frame 65: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 91.189.89.22 (91.189.89.22)
Transmission Control Protocol, Src Port: 44618 (44618), Dst Port: https (443), Seq: 74, Ack: 9, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     66 12.781961   192.9.205.15          192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;

Frame 66: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.15 (192.9.205.15), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     67 12.821213   8.8.8.8               192.9.205.125         DNS      108    Standard query response A 91.189.92.55 A 91.189.92.57

Frame 67: 108 bytes on wire (864 bits), 108 bytes captured (864 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 8.8.8.8 (8.8.8.8), Dst: 192.9.205.125 (192.9.205.125)
User Datagram Protocol, Src Port: domain (53), Dst Port: 19644 (19644)
Domain Name System (response)

No.     Time        Source                Destination           Protocol Length Info
     68 12.821677   192.9.205.125         8.8.8.8               DNS      76     Standard query A daisy.ubuntu.com

Frame 68: 76 bytes on wire (608 bits), 76 bytes captured (608 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 8.8.8.8 (8.8.8.8)
User Datagram Protocol, Src Port: 62764 (62764), Dst Port: domain (53)
Domain Name System (query)

No.     Time        Source                Destination           Protocol Length Info
     69 13.215726   8.8.8.8               192.9.205.125         DNS      118    Standard query response CNAME googlemail.l.google.com A 216.58.219.101

Frame 69: 118 bytes on wire (944 bits), 118 bytes captured (944 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 8.8.8.8 (8.8.8.8), Dst: 192.9.205.125 (192.9.205.125)
User Datagram Protocol, Src Port: domain (53), Dst Port: 10088 (10088)
Domain Name System (response)

No.     Time        Source                Destination           Protocol Length Info
     70 13.215863   192.9.205.125         216.58.219.101        TCP      74     38881 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=1850680 TSecr=0 WS=16

Frame 70: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 0, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     71 13.251286   108.160.170.45        192.9.205.125         TCP      66     https &gt; 46949 [ACK] Seq=326 Ack=427 Win=80 Len=0 TSval=4052677314 TSecr=1850351

Frame 71: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 108.160.170.45 (108.160.170.45), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 46949 (46949), Seq: 326, Ack: 427, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     72 13.346153   192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;

Frame 72: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     73 13.402488   192.9.205.125         216.58.219.101        TCP      74     38882 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=1850726 TSecr=0 WS=16

Frame 73: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38882 (38882), Dst Port: https (443), Seq: 0, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     74 13.497672   192.9.205.18          192.9.205.255         NBNS     92     Name query NB W.SHARETHIS.COM&lt;00&gt;**

Frame 74: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

N**o.     Time        Source                Destination           Protocol Length Info
     75 13.546341   192.9.205.15          192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;**

Frame 75: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: AsrockIn_c6:5a:76 (bc:5f:f4:c6:5a:76), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.15 (192.9.205.15), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     76 13.885315   8.8.8.8               192.9.205.125         DNS      108    Standard query response A 91.189.92.57 A 91.189.92.55

Frame 76: 108 bytes on wire (864 bits), 108 bytes captured (864 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 8.8.8.8 (8.8.8.8), Dst: 192.9.205.125 (192.9.205.125)
User Datagram Protocol, Src Port: domain (53), Dst Port: 62764 (62764)
Domain Name System (response)

No.     Time        Source                Destination           Protocol Length Info
     77 13.889382   91.189.89.22          192.9.205.125         TCP      66     https &gt; 44618 [ACK] Seq=9 Ack=74 Win=14592 Len=0 TSval=463463970 TSecr=1850567

Frame 77: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 91.189.89.22 (91.189.89.22), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 44618 (44618), Seq: 9, Ack: 74, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     78 14.096229   192.9.205.122         192.9.205.255         NBNS     92     Name query NB WPAD&lt;00&gt;

Frame 78: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: QuantaCo_1b:04:47 (60:eb:69:1b:04:47), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.122 (192.9.205.122), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     79 14.211293   216.58.219.101        192.9.205.125         TCP      74     https &gt; 38881 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=536 SACK_PERM=1 TSval=1522311232 TSecr=1850680 WS=128

Frame 79: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38881 (38881), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     80 14.211305   192.9.205.125         216.58.219.101        TCP      66     38881 &gt; https [ACK] Seq=1 Ack=1 Win=14608 Len=0 TSval=1850928 TSecr=1522311232

Frame 80: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     81 14.211493   192.9.205.125         216.58.219.101        TLSv1.2  583    Client Hello

Frame 81: 583 bytes on wire (4664 bits), 583 bytes captured (4664 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 1, Ack: 1, Len: 517
Secure Sockets Layer

**No.     Time        Source                Destination           Protocol Length Info
     82 14.247286   192.9.205.18          192.9.205.255         NBNS     92     Name query NB W.SHARETHIS.COM&lt;00&gt;**

Frame 82: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     83 14.399559   192.9.205.125         216.58.219.101        TCP      74     38882 &gt; https [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM=1 TSval=1850976 TSecr=0 WS=16

Frame 83: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38882 (38882), Dst Port: https (443), Seq: 0, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     84 14.409389   216.58.219.101        192.9.205.125         TCP      74     https &gt; 38882 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=536 SACK_PERM=1 TSval=1522320089 TSecr=1850726 WS=128

Frame 84: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38882 (38882), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     85 14.409449   192.9.205.125         216.58.219.101        TCP      66     38882 &gt; https [ACK] Seq=1 Ack=1 Win=14608 Len=0 TSval=1850978 TSecr=1522320089

Frame 85: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38882 (38882), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     86 14.593591   216.58.219.101        192.9.205.125         TCP      74     https &gt; 38881 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=536 SACK_PERM=1 TSval=1522311676 TSecr=1850680 WS=128

Frame 86: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38881 (38881), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     87 14.593603   192.9.205.125         216.58.219.101        TCP      66     [TCP Dup ACK 81#1] 38881 &gt; https [ACK] Seq=518 Ack=1 Win=14608 Len=0 TSval=1851024 TSecr=1522311232

Frame 87: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 518, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     88 14.739235   216.58.219.101        192.9.205.125         TCP      74     https &gt; 38882 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=536 SACK_PERM=1 TSval=1522320450 TSecr=1850726 WS=128

Frame 88: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38882 (38882), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     89 14.739246   192.9.205.125         216.58.219.101        TCP      66     [TCP Dup ACK 85#1] 38882 &gt; https [ACK] Seq=1 Ack=1 Win=14608 Len=0 TSval=1851060 TSecr=1522320089

Frame 89: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38882 (38882), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0

**No.     Time        Source                Destination           Protocol Length Info
     90 14.997254   192.9.205.18          192.9.205.255         NBNS     92     Name query NB W.SHARETHIS.COM&lt;00&gt;**

Frame 90: 92 bytes on wire (736 bits), 92 bytes captured (736 bits)
Ethernet II, Src: BiostarM_65:cd:dc (b8:97:5a:65:cd:dc), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Internet Protocol Version 4, Src: 192.9.205.18 (192.9.205.18), Dst: 192.9.205.255 (192.9.205.255)
User Datagram Protocol, Src Port: netbios-ns (137), Dst Port: netbios-ns (137)
NetBIOS Name Service

No.     Time        Source                Destination           Protocol Length Info
     91 15.041315   216.58.219.101        192.9.205.125         TCP      66     https &gt; 38881 [ACK] Seq=1 Ack=518 Win=43648 Len=0 TSval=1522312238 TSecr=1850928

Frame 91: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38881 (38881), Seq: 1, Ack: 518, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     92 15.043384   216.58.219.101        192.9.205.125         TLSv1.2  216    Server Hello, Change Cipher Spec, Hello Request, Hello Request

Frame 92: 216 bytes on wire (1728 bits), 216 bytes captured (1728 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38881 (38881), Seq: 1, Ack: 518, Len: 150
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     93 15.043390   192.9.205.125         216.58.219.101        TCP      66     38881 &gt; https [ACK] Seq=518 Ack=151 Win=15648 Len=0 TSval=1851136 TSecr=1522312238

Frame 93: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 518, Ack: 151, Len: 0

No.     Time        Source                Destination           Protocol Length Info
     94 15.045006   192.9.205.125         216.58.219.101        TLSv1.2  253    Change Cipher Spec, Hello Request, Hello Request

Frame 94: 253 bytes on wire (2024 bits), 253 bytes captured (2024 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 518, Ack: 151, Len: 187
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     95 15.053216   192.9.205.125         216.58.219.101        TLSv1.2  119    Application Data

Frame 95: 119 bytes on wire (952 bits), 119 bytes captured (952 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 705, Ack: 151, Len: 53
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     96 15.053270   192.9.205.125         216.58.219.101        TLSv1.2  116    Application Data

Frame 96: 116 bytes on wire (928 bits), 116 bytes captured (928 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 758, Ack: 151, Len: 50
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     97 15.053312   192.9.205.125         216.58.219.101        TLSv1.2  108    Application Data

Frame 97: 108 bytes on wire (864 bits), 108 bytes captured (864 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 808, Ack: 151, Len: 42
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
     98 15.053586   192.9.205.125         216.58.219.101        TCP      590    [TCP segment of a reassembled PDU]

Frame 98: 590 bytes on wire (4720 bits), 590 bytes captured (4720 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 850, Ack: 151, Len: 524

No.     Time        Source                Destination           Protocol Length Info
     99 15.053591   192.9.205.125         216.58.219.101        TCP      590    [TCP segment of a reassembled PDU]

Frame 99: 590 bytes on wire (4720 bits), 590 bytes captured (4720 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 1374, Ack: 151, Len: 524

No.     Time        Source                Destination           Protocol Length Info
    100 15.053610   192.9.205.125         216.58.219.101        TCP      590    [TCP segment of a reassembled PDU]

Frame 100: 590 bytes on wire (4720 bits), 590 bytes captured (4720 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 1898, Ack: 151, Len: 524

No.     Time        Source                Destination           Protocol Length Info
    101 15.053612   192.9.205.125         216.58.219.101        TLSv1.2  533    Application Data

Frame 101: 533 bytes on wire (4264 bits), 533 bytes captured (4264 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38881 (38881), Dst Port: https (443), Seq: 2422, Ack: 151, Len: 467
[4 Reassembled TCP Segments (2039 bytes): #98(524), #99(524), #100(524), #101(467)]
Secure Sockets Layer

No.     Time        Source                Destination           Protocol Length Info
    102 15.267398   216.58.219.101        192.9.205.125         TCP      74     https &gt; 38882 [SYN, ACK] Seq=0 Ack=1 Win=42540 Len=0 MSS=536 SACK_PERM=1 TSval=1522321086 TSecr=1850726 WS=128

Frame 102: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
Ethernet II, Src: Cisco-Li_84:64:18 (00:16:b6:84:64:18), Dst: fc:aa:14:50:17:45 (fc:aa:14:50:17:45)
Internet Protocol Version 4, Src: 216.58.219.101 (216.58.219.101), Dst: 192.9.205.125 (192.9.205.125)
Transmission Control Protocol, Src Port: https (443), Dst Port: 38882 (38882), Seq: 0, Ack: 1, Len: 0

No.     Time        Source                Destination           Protocol Length Info
    103 15.267424   192.9.205.125         216.58.219.101        TCP      66     [TCP Dup ACK 85#2] 38882 &gt; https [ACK] Seq=1 Ack=1 Win=14608 Len=0 TSval=1851192 TSecr=1522320089

Frame 103: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
Ethernet II, Src: fc:aa:14:50:17:45 (fc:aa:14:50:17:45), Dst: Cisco-Li_84:64:18 (00:16:b6:84:64:18)
Internet Protocol Version 4, Src: 192.9.205.125 (192.9.205.125), Dst: 216.58.219.101 (216.58.219.101)
Transmission Control Protocol, Src Port: 38882 (38882), Dst Port: https (443), Seq: 1, Ack: 1, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nbns" rel="tag" title="see questions tagged &#39;nbns&#39;">nbns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/cd87e170a7a2ddbf79b06c3fb8b0c141?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jicelle&#39;s gravatar image" /><p><span>Jicelle</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jicelle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Sep '15, 08:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-45666" class="comments-container"><span id="45668"></span><div id="comment-45668" class="comment"><div id="post-45668-score" class="comment-score"></div><div class="comment-text"><p>Analysis of a wall of text isn't much fun, especially given all the tools in Wireshark if given a capture file.</p><p>Can you share the capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox?</p></div><div id="comment-45668-info" class="comment-info"><span class="comment-age">(07 Sep '15, 08:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45671"></span><div id="comment-45671" class="comment"><div id="post-45671-score" class="comment-score"></div><div class="comment-text"><p>ok ;) well here is another capture ;)</p><p>1) <img src="https://osqa-ask.wireshark.org/upfiles/wireshark1234.png" alt="alt text" /></p><p><img src="https://www.dropbox.com/s/jnutju8shopsjpd/wireshark1234.png?dl=0" alt="alt text" /></p><p>2) <img src="https://www.dropbox.com/s/3q67ugangoprwql/wireshar123.png?dl=0" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshar123_yKUlafv.png" alt="alt text" /></p><p>thanks!</p></div><div id="comment-45671-info" class="comment-info"><span class="comment-age">(07 Sep '15, 10:11)</span> <span class="comment-user userinfo">Jicelle</span></div></div></div><div id="comment-tools-45666" class="comment-tools"></div><div class="clear"></div><div id="comment-45666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45681"></span>

<div id="answer-container-45681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45681-score" class="post-score" title="current number of votes">2</div><span id="post-45681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>NBNS queries are "normal" in a lot of networks.</p><blockquote><p>The internet velocity has decreased.</p></blockquote><p>I can see quite a number of requests for <strong>WPAD</strong>. That's the browser trying to (automatically) find a local proxy, maybe because you enabled something like "Automatically detect settings" in the Proxy settings of Internet Explorer, or "Auto-detect proxy settings for this network" in Firefox. These queries for WPAD can indeed slow down internet access. Please disable those settings in your browser (please google how to do that!).</p><pre><code>     66 12.781961   192.9.205.15  192.9.205.255 NBNS 92  Name query NB WPAD&lt;00&gt; &lt;=== HERE</code></pre><p>See also: <a href="https://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol">https://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-45681" class="comments-container"><span id="45703"></span><div id="comment-45703" class="comment"><div id="post-45703-score" class="comment-score"></div><div class="comment-text"><p>thank you, I'll check that :)</p></div><div id="comment-45703-info" class="comment-info"><span class="comment-age">(08 Sep '15, 07:27)</span> <span class="comment-user userinfo">Jicelle</span></div></div><span id="45706"></span><div id="comment-45706" class="comment"><div id="post-45706-score" class="comment-score"></div><div class="comment-text"><p>good luck.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-45706-info" class="comment-info"><span class="comment-age">(08 Sep '15, 08:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45681" class="comment-tools"></div><div class="clear"></div><div id="comment-45681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

