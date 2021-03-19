+++
type = "question"
title = "How to decrypt ssl packet with tshark 1.8"
description = '''I have tried to decrypt https traffic with tshark. The command that I used was as below: tshark -r 1.pcap -o ssl.keys_list:&quot;10.140.8.27&quot;,&quot;443&quot;,&quot;http&quot;,&quot;test_ca.pem&quot; -o ssl.debug_file:&quot;ssldebug.log&quot; -V The same pcap file can be decrypted by the same key file with wireshark 2.2.6. However, it failed wi...'''
date = "2017-05-02T01:57:00Z"
lastmod = "2017-05-02T05:03:00Z"
weight = 61153
keywords = [ "ssl", "tshark" ]
aliases = [ "/questions/61153" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to decrypt ssl packet with tshark 1.8](/questions/61153/how-to-decrypt-ssl-packet-with-tshark-18)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61153-score" class="post-score" title="current number of votes">0</div><span id="post-61153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried to decrypt https traffic with tshark. The command that I used was as below:</p><p><code>tshark -r 1.pcap -o ssl.keys_list:"10.140.8.27","443","http","test_ca.pem" -o ssl.debug_file:"ssldebug.log" -V</code></p><p>The same pcap file can be decrypted by the same key file with wireshark 2.2.6. However, it failed with tshark 1.8.</p><p>tshark SSL debug log:</p><pre><code>Private key imported: KeyID d3:3a:0a:2a:4f:97:3a:c1:df:62:1b:d9:5c:2a:77:6d:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;10.140.8.27&#39; (10.140.8.27) port &#39;443&#39; filename &#39;test_ca.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file test_ca.pem successfully loaded.
association_add TCP port 443 protocol http handle 0x1058760

dissect_ssl enter frame #1 (first time)
ssl_session_init: initializing ptr 0x7f48afd920f0 size 680
  conversation = 0x7f48afd91dc8, ssl_session = 0x7f48afd920f0
  record: offset = 0, reported_length_remaining = 81
  need_desegmentation: offset = 0, reported_length_remaining = 81

dissect_ssl enter frame #3 (first time)
  conversation = 0x7f48afd91dc8, ssl_session = 0x7f48afd920f0
  record: offset = 0, reported_length_remaining = 1121
  need_desegmentation: offset = 0, reported_length_remaining = 1121

dissect_ssl enter frame #9 (first time)
ssl_session_init: initializing ptr 0x7f48afd92978 size 680
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 109
  need_desegmentation: offset = 0, reported_length_remaining = 109

dissect_ssl enter frame #11 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 864
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 53, ssl state 0x10
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 49 bytes, remaining 58
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello found CIPHER 0x0035 -&gt; state 0x16
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 58, reported_length_remaining = 806
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 796, ssl state 0x16
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 63 length 792 bytes, remaining 859
  record: offset = 859, reported_length_remaining = 5
  need_desegmentation: offset = 859, reported_length_remaining = 5

dissect_ssl enter frame #13 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 322
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x16
association_find: TCP port 44716 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267
trying to use SSL keylog in
failed to open SSL keylog
  record: offset = 267, reported_length_remaining = 55
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 44716 found (nil)
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 273, reported_length_remaining = 49
  need_desegmentation: offset = 273, reported_length_remaining = 49

dissect_ssl enter frame #15 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 262
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 202, ssl state 0x16
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 4 offset 5 length 198 bytes, remaining 207
  record: offset = 207, reported_length_remaining = 55
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER
  record: offset = 213, reported_length_remaining = 49
  need_desegmentation: offset = 213, reported_length_remaining = 49

dissect_ssl enter frame #16 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 182
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 44716 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 44716 found (nil)
association_find: TCP port 443 found 0x1ac91d0
  record: offset = 37, reported_length_remaining = 145
  need_desegmentation: offset = 37, reported_length_remaining = 145

dissect_ssl enter frame #18 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 544
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x1ac91d0
  record: offset = 37, reported_length_remaining = 507
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 384, ssl state 0x16
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x1ac91d0
  record: offset = 426, reported_length_remaining = 118
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x16
association_find: TCP port 443 found 0x1ac91d0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x1ac91d0
  record: offset = 463, reported_length_remaining = 81
  need_desegmentation: offset = 463, reported_length_remaining = 81

dissect_ssl enter frame #21 (first time)
  conversation = 0x7f48afd92650, ssl_session = 0x7f48afd92978
  record: offset = 0, reported_length_remaining = 33
  need_desegmentation: offset = 0, reported_length_remaining = 33</code></pre><p>command output:</p><pre><code>frame:0:151:Frame 1: 151 bytes on wire (1208 bits), 151 bytes captured (1208 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:45.947506000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369265.947506000 seconds
0:0:    [Time delta from previous captured frame: 0.000000000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000000000 seconds]
0:0:    [Time since reference or first frame: 0.000000000 seconds]
0:0:    Frame Number: 1
0:0:    Frame Length: 151 bytes (1208 bits)
0:0:    Capture Length: 151 bytes (1208 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
147:4:    Frame check sequence: 0x40f19622 [incorrect, should be 0xb0ad2882]
147:4:        [FCS Good: False]
147:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 173.36.7.6 (173.36.7.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 137
18:2:    Identification: 0x6cbf (27839)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 111
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0xd7de [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 173.36.7.6 (173.36.7.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 50101 (50101), Seq: 1, Ack: 1, Len: 81
34:2:    Source port: https (443)
36:2:    Destination port: 50101 (50101)
34:0:    [Stream index: 0]
38:4:    Sequence number: 1    (relative sequence number)
34:0:    [Next sequence number: 82    (relative sequence number)]
42:4:    Acknowledgment number: 1    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 511
48:2:    [Calculated window size: 511]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xcb50 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 344870702, TSecr 1325455116
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 344870702
62:4:            Timestamp echo reply: 1325455116
34:0:    [SEQ/ACK analysis]
34:0:        [Bytes in flight: 81]
66:81:    TCP segment data (81 bytes)
ssl:66:81:Secure Sockets Layer

frame:0:66:Frame 2: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:45.947601000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369265.947601000 seconds
0:0:    [Time delta from previous captured frame: 0.000095000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000095000 seconds]
0:0:    [Time since reference or first frame: 0.000095000 seconds]
0:0:    Frame Number: 2
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0x148e4f2e [incorrect, should be 0x2a9e80cf]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 173.36.7.6 (173.36.7.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0xaf4e (44878)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xc4a4 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 173.36.7.6 (173.36.7.6)
tcp:34:32:Transmission Control Protocol, Src Port: 50101 (50101), Dst Port: https (443), Seq: 1338627855, Ack: 4017034065
34:2:    Source port: 50101 (50101)
36:2:    Destination port: https (443)
34:0:    [Stream index: 0]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1338627855    (relative sequence number)
42:4:    Acknowledgment number: 4017034065    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4093
48:2:    [Calculated window size: 4093]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xc6f7 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:1191:Frame 3: 1191 bytes on wire (9528 bits), 1191 bytes captured (9528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:45.947757000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369265.947757000 seconds
0:0:    [Time delta from previous captured frame: 0.000156000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000156000 seconds]
0:0:    [Time since reference or first frame: 0.000251000 seconds]
0:0:    Frame Number: 3
0:0:    Frame Length: 1191 bytes (9528 bits)
0:0:    Capture Length: 1191 bytes (9528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
1187:4:    Frame check sequence: 0xdae3d5af [incorrect, should be 0xc78d91bf]
1187:4:        [FCS Good: False]
1187:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 173.36.7.6 (173.36.7.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 1177
18:2:    Identification: 0x6cc0 (27840)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 111
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0xd3cd [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 173.36.7.6 (173.36.7.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 50101 (50101), Seq: 86, Ack: 1, Len: 1121
34:2:    Source port: https (443)
36:2:    Destination port: 50101 (50101)
34:0:    [Stream index: 0]
38:4:    Sequence number: 86    (relative sequence number)
34:0:    [Next sequence number: 1207    (relative sequence number)]
42:4:    Acknowledgment number: 1    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 511
48:2:    [Calculated window size: 511]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xefe0 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 344870702, TSecr 1325455116
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 344870702
62:4:            Timestamp echo reply: 1325455116
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
66:1121:    TCP segment data (1121 bytes)
ssl:66:1121:Secure Sockets Layer

frame:0:66:Frame 4: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:45.947809000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369265.947809000 seconds
0:0:    [Time delta from previous captured frame: 0.000052000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000052000 seconds]
0:0:    [Time since reference or first frame: 0.000303000 seconds]
0:0:    Frame Number: 4
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0x148e4f2e [incorrect, should be 0x172daf2c]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 173.36.7.6 (173.36.7.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x6812 (26642)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x0be1 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 173.36.7.6 (173.36.7.6)
tcp:34:32:Transmission Control Protocol, Src Port: 50101 (50101), Dst Port: https (443), Seq: 1338627855, Ack: 4017035190
34:2:    Source port: 50101 (50101)
36:2:    Destination port: https (443)
34:0:    [Stream index: 0]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1338627855    (relative sequence number)
42:4:    Acknowledgment number: 4017035190    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4060
48:2:    [Calculated window size: 4060]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xc6f7 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:74:Frame 5: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.261631000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.261631000 seconds
0:0:    [Time delta from previous captured frame: 3.313822000 seconds]
0:0:    [Time delta from previous displayed frame: 3.313822000 seconds]
0:0:    [Time since reference or first frame: 3.314125000 seconds]
0:0:    Frame Number: 5
0:0:    Frame Length: 74 bytes (592 bits)
0:0:    Capture Length: 74 bytes (592 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
70:4:    Frame check sequence: 0x01030307 [incorrect, should be 0x98521542]
70:4:        [FCS Good: False]
70:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 60
18:2:    Identification: 0x68db (26843)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8ce5 [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:40:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 3115282787
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 3115282787    (relative sequence number)
46:1:    Header length: 40 bytes
46:2:    Flags: 0x002 (SYN)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...0 .... = Acknowledgment: Not set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..1. = Syn: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection establish request (SYN): server port https]
0:0:                [Message: Connection establish request (SYN): server port https]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 14600
48:2:    [Calculated window size: 14600]
50:2:    Checksum: 0x289e [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:78:Frame 6: 78 bytes on wire (624 bits), 78 bytes captured (624 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.261783000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.261783000 seconds
0:0:    [Time delta from previous captured frame: 0.000152000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000152000 seconds]
0:0:    [Time since reference or first frame: 3.314277000 seconds]
0:0:    Frame Number: 6
0:0:    Frame Length: 78 bytes (624 bits)
0:0:    Capture Length: 78 bytes (624 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
74:4:    Frame check sequence: 0x04020000 [incorrect, should be 0xaa9638ad]
74:4:        [FCS Good: False]
74:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 64
18:2:    Identification: 0x3d12 (15634)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xb2aa (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:44:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959621331, Ack: 3115282788
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959621331    (relative sequence number)
42:4:    Acknowledgment number: 3115282788    (relative ack number)
46:1:    Header length: 44 bytes
46:2:    Flags: 0x012 (SYN, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..1. = Syn: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port https]
0:0:                [Message: Connection establish acknowledge (SYN+ACK): server port https]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 65535
48:2:    [Calculated window size: 65535]
50:2:    Checksum: 0x4b2e [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:66:Frame 7: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.262151000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.262151000 seconds
0:0:    [Time delta from previous captured frame: 0.000368000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000368000 seconds]
0:0:    [Time since reference or first frame: 3.314645000 seconds]
0:0:    Frame Number: 7
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0x4f0192d6 [incorrect, should be 0xe9b1f1d4]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x68dc (26844)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8cec [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 3115282788, Ack: 1959621332
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 3115282788    (relative sequence number)
42:4:    Acknowledgment number: 1959621332    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 115
48:2:    [Calculated window size: 115]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xc675 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:66:Frame 8: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.262181000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.262181000 seconds
0:0:    [Time delta from previous captured frame: 0.000030000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000030000 seconds]
0:0:    [Time since reference or first frame: 3.314675000 seconds]
0:0:    Frame Number: 8
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19b8 [incorrect, should be 0x49829acc]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0xf163 (61795)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xfe64 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959621332, Ack: 3115282788
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959621332    (relative sequence number)
42:4:    Acknowledgment number: 3115282788    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4117
48:2:    [Calculated window size: 4117]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:179:Frame 9: 179 bytes on wire (1432 bits), 179 bytes captured (1432 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.262353000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.262353000 seconds
0:0:    [Time delta from previous captured frame: 0.000172000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000172000 seconds]
0:0:    [Time since reference or first frame: 3.314847000 seconds]
0:0:    Frame Number: 9
0:0:    Frame Length: 179 bytes (1432 bits)
0:0:    Capture Length: 179 bytes (1432 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
175:4:    Frame check sequence: 0x00230000 [incorrect, should be 0x97c956c0]
175:4:        [FCS Good: False]
175:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 165
18:2:    Identification: 0x68dd (26845)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8c7a [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 1, Ack: 1, Len: 109
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
38:4:    Sequence number: 1    (relative sequence number)
34:0:    [Next sequence number: 110    (relative sequence number)]
42:4:    Acknowledgment number: 1    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 115
48:2:    [Calculated window size: 115]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x63f5 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 2787842489, TSecr 1325503190
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 2787842489
62:4:            Timestamp echo reply: 1325503190
34:0:    [SEQ/ACK analysis]
34:0:        [Bytes in flight: 109]
66:109:    TCP segment data (109 bytes)
ssl:66:109:Secure Sockets Layer

frame:0:66:Frame 10: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.262387000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.262387000 seconds
0:0:    [Time delta from previous captured frame: 0.000034000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000034000 seconds]
0:0:    [Time since reference or first frame: 3.314881000 seconds]
0:0:    Frame Number: 10
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19b9 [incorrect, should be 0x2036bf16]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0xbed3 (48851)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x30f5 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959621332, Ack: 3115282901
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959621332    (relative sequence number)
42:4:    Acknowledgment number: 3115282901    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4114
48:2:    [Calculated window size: 4114]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:934:Frame 11: 934 bytes on wire (7472 bits), 934 bytes captured (7472 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.263053000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.263053000 seconds
0:0:    [Time delta from previous captured frame: 0.000666000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000666000 seconds]
0:0:    [Time since reference or first frame: 3.315547000 seconds]
0:0:    Frame Number: 11
0:0:    Frame Length: 934 bytes (7472 bits)
0:0:    Capture Length: 934 bytes (7472 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl:pkcs-1:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:x509sat:pkcs-1:pkcs-1]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
930:4:    Frame check sequence: 0x0e000000 [incorrect, should be 0x988536b8]
930:4:        [FCS Good: False]
930:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 920
18:2:    Identification: 0xc88f (51343)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x23d5 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1, Ack: 114, Len: 864
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
38:4:    Sequence number: 1    (relative sequence number)
34:0:    [Next sequence number: 865    (relative sequence number)]
42:4:    Acknowledgment number: 114    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4114
48:2:    [Calculated window size: 4114]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4e86 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 1325503191, TSecr 2787842489
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 1325503191
62:4:            Timestamp echo reply: 2787842489
34:0:    [SEQ/ACK analysis]
34:0:        [Bytes in flight: 864]
34:0:        [TCP Analysis Flags]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
925:5:    TCP segment data (5 bytes)
ssl:66:864:Secure Sockets Layer
66:58:    TLSv1 Record Layer: Handshake Protocol: Server Hello
66:1:        Content Type: Handshake (22)
67:2:        Version: TLS 1.0 (0x0301)
69:2:        Length: 53
71:53:        Handshake Protocol: Server Hello
71:1:            Handshake Type: Server Hello (2)
72:3:            Length: 49
75:2:            Version: TLS 1.0 (0x0301)
text:77:32:            Random
77:4:                gmt_unix_time: Mar 25, 2050 22:49:28.000000000 UTC
81:28:                random_bytes: a6749ab12a7308416d3fdedbc00a73681102b8da8b4b7a9c...
109:1:            Session ID Length: 0
110:2:            Cipher Suite: TLS_RSA_WITH_AES_256_CBC_SHA (0x0035)
112:1:            Compression Method: null (0)
113:2:            Extensions Length: 9
text:115:5:            Extension: renegotiation_info
115:2:                Type: renegotiation_info (0xff01)
117:2:                Length: 1
text:119:1:                Renegotiation Info extension
119:1:                    Renegotiation info extension length: 0
text:120:4:            Extension: SessionTicket TLS
120:2:                Type: SessionTicket TLS (0x0023)
122:2:                Length: 0
124:0:                Data (0 bytes)
124:801:    TLSv1 Record Layer: Handshake Protocol: Certificate
124:1:        Content Type: Handshake (22)
125:2:        Version: TLS 1.0 (0x0301)
127:2:        Length: 796
129:796:        Handshake Protocol: Certificate
129:1:            Handshake Type: Certificate (11)
130:3:            Length: 792
133:3:            Certificates Length: 789
136:789:            Certificates (789 bytes)
136:3:                Certificate Length: 786
139:786:                Certificate (id-at-commonName=test_ca,id-at-organizationName=Cisco,id-at-localityName=SH,id-at-stateOrProvinceName=SH,id-at-countryName=CN)
143:506:                    signedCertificate
text:149:9:                        serialNumber : 0x00fe771004b47eef3a
158:15:                        signature (shaWithRSAEncryption)
162:9:                            Algorithm Id: 1.2.840.113549.1.1.5 (shaWithRSAEncryption)
173:75:                        issuer: rdnSequence (0)
175:73:                            rdnSequence: 5 items (id-at-commonName=test_ca,id-at-organizationName=Cisco,id-at-localityName=SH,id-at-stateOrProvinceName=SH,id-at-countryName=CN)
177:11:                                RDNSequence item: 1 item (id-at-countryName=CN)
177:11:                                    RelativeDistinguishedName item (id-at-countryName=CN)
181:3:                                        Id: 2.5.4.6 (id-at-countryName)
186:2:                                        CountryName: CN
190:11:                                RDNSequence item: 1 item (id-at-stateOrProvinceName=SH)
190:11:                                    RelativeDistinguishedName item (id-at-stateOrProvinceName=SH)
194:3:                                        Id: 2.5.4.8 (id-at-stateOrProvinceName)
197:4:                                        DirectoryString: printableString (1)
199:2:                                            printableString: SH
203:11:                                RDNSequence item: 1 item (id-at-localityName=SH)
203:11:                                    RelativeDistinguishedName item (id-at-localityName=SH)
207:3:                                        Id: 2.5.4.7 (id-at-localityName)
210:4:                                        DirectoryString: printableString (1)
212:2:                                            printableString: SH
216:14:                                RDNSequence item: 1 item (id-at-organizationName=Cisco)
216:14:                                    RelativeDistinguishedName item (id-at-organizationName=Cisco)
220:3:                                        Id: 2.5.4.10 (id-at-organizationName)
223:7:                                        DirectoryString: printableString (1)
225:5:                                            printableString: Cisco
232:16:                                RDNSequence item: 1 item (id-at-commonName=test_ca)
232:16:                                    RelativeDistinguishedName item (id-at-commonName=test_ca)
236:3:                                        Id: 2.5.4.3 (id-at-commonName)
239:9:                                        DirectoryString: teletexString (0)
241:7:                                            teletexString: test_ca
248:32:                        validity
250:15:                            notBefore: utcTime (0)
252:13:                                utcTime: 17-04-28 05:52:10 (UTC)
265:15:                            notAfter: utcTime (0)
267:13:                                utcTime: 27-04-26 05:52:10 (UTC)
280:75:                        subject: rdnSequence (0)
282:73:                            rdnSequence: 5 items (id-at-commonName=test_ca,id-at-organizationName=Cisco,id-at-localityName=SH,id-at-stateOrProvinceName=SH,id-at-countryName=CN)
284:11:                                RDNSequence item: 1 item (id-at-countryName=CN)
284:11:                                    RelativeDistinguishedName item (id-at-countryName=CN)
288:3:                                        Id: 2.5.4.6 (id-at-countryName)
293:2:                                        CountryName: CN
297:11:                                RDNSequence item: 1 item (id-at-stateOrProvinceName=SH)
297:11:                                    RelativeDistinguishedName item (id-at-stateOrProvinceName=SH)
301:3:                                        Id: 2.5.4.8 (id-at-stateOrProvinceName)
304:4:                                        DirectoryString: printableString (1)
306:2:                                            printableString: SH
310:11:                                RDNSequence item: 1 item (id-at-localityName=SH)
310:11:                                    RelativeDistinguishedName item (id-at-localityName=SH)
314:3:                                        Id: 2.5.4.7 (id-at-localityName)
317:4:                                        DirectoryString: printableString (1)
319:2:                                            printableString: SH
323:14:                                RDNSequence item: 1 item (id-at-organizationName=Cisco)
323:14:                                    RelativeDistinguishedName item (id-at-organizationName=Cisco)
327:3:                                        Id: 2.5.4.10 (id-at-organizationName)
330:7:                                        DirectoryString: printableString (1)
332:5:                                            printableString: Cisco
339:16:                                RDNSequence item: 1 item (id-at-commonName=test_ca)
339:16:                                    RelativeDistinguishedName item (id-at-commonName=test_ca)
343:3:                                        Id: 2.5.4.3 (id-at-commonName)
346:9:                                        DirectoryString: teletexString (0)
348:7:                                            teletexString: test_ca
355:294:                        subjectPublicKeyInfo
359:15:                            algorithm (rsaEncryption)
363:9:                                Algorithm Id: 1.2.840.113549.1.1.1 (rsaEncryption)
378:1:                            Padding: 0
379:270:                            subjectPublicKey: 3082010a0282010100b5ca8f507bc2b7aaf780f1579cf75c...
649:15:                    algorithmIdentifier (shaWithRSAEncryption)
653:9:                        Algorithm Id: 1.2.840.113549.1.1.5 (shaWithRSAEncryption)
668:1:                    Padding: 0
669:256:                    encrypted: 51786d103611f86bdf3ca77a99f7fd7e17d09e7e251aa34a...

frame:0:66:Frame 12: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.263455000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.263455000 seconds
0:0:    [Time delta from previous captured frame: 0.000402000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000402000 seconds]
0:0:    [Time since reference or first frame: 3.315949000 seconds]
0:0:    Frame Number: 12
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0x4f0192d7 [incorrect, should be 0x8c48b6d4]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x68de (26846)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8cea [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 3115282901, Ack: 1959622200
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 3115282901    (relative sequence number)
42:4:    Acknowledgment number: 1959622200    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 128
48:2:    [Calculated window size: 128]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xc290 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:392:Frame 13: 392 bytes on wire (3136 bits), 392 bytes captured (3136 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.263955000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.263955000 seconds
0:0:    [Time delta from previous captured frame: 0.000500000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000500000 seconds]
0:0:    [Time since reference or first frame: 3.316449000 seconds]
0:0:    Frame Number: 13
0:0:    Frame Length: 392 bytes (3136 bits)
0:0:    Capture Length: 392 bytes (3136 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
388:4:    Frame check sequence: 0x5bc2edf1 [incorrect, should be 0x8cab1d1e]
388:4:        [FCS Good: False]
388:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 378
18:2:    Identification: 0x68df (26847)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8ba3 [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 114, Ack: 869, Len: 322
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
38:4:    Sequence number: 114    (relative sequence number)
34:0:    [Next sequence number: 436    (relative sequence number)]
42:4:    Acknowledgment number: 869    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 128
48:2:    [Calculated window size: 128]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x11dd [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 2787842490, TSecr 1325503191
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 2787842490
62:4:            Timestamp echo reply: 1325503191
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
339:49:    TCP segment data (49 bytes)
ssl:66:322:Secure Sockets Layer
66:267:    TLSv1 Record Layer: Handshake Protocol: Client Key Exchange
66:1:        Content Type: Handshake (22)
67:2:        Version: TLS 1.0 (0x0301)
69:2:        Length: 262
71:262:        Handshake Protocol: Client Key Exchange
71:1:            Handshake Type: Client Key Exchange (16)
72:3:            Length: 258
text:75:258:            RSA Encrypted PreMaster Secret
75:2:                Encrypted PreMaster length: 256
77:256:                Encrypted PreMaster: 8d18212a0338ab9dabd92c07a430f3b696a157a1559d4906...
333:6:    TLSv1 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
333:1:        Content Type: Change Cipher Spec (20)
334:2:        Version: TLS 1.0 (0x0301)
336:2:        Length: 1
338:1:        Change Cipher Spec Message

frame:0:66:Frame 14: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.263981000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.263981000 seconds
0:0:    [Time delta from previous captured frame: 0.000026000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000026000 seconds]
0:0:    [Time since reference or first frame: 3.316475000 seconds]
0:0:    Frame Number: 14
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19ba [incorrect, should be 0x75fb3dda]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x1d98 (7576)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xd230 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959622200, Ack: 3115283227
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959622200    (relative sequence number)
42:4:    Acknowledgment number: 3115283227    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4104
48:2:    [Calculated window size: 4104]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:332:Frame 15: 332 bytes on wire (2656 bits), 332 bytes captured (2656 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.305811000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.305811000 seconds
0:0:    [Time delta from previous captured frame: 0.041830000 seconds]
0:0:    [Time delta from previous displayed frame: 0.041830000 seconds]
0:0:    [Time since reference or first frame: 3.358305000 seconds]
0:0:    Frame Number: 15
0:0:    Frame Length: 332 bytes (2656 bits)
0:0:    Capture Length: 332 bytes (2656 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
328:4:    Frame check sequence: 0x04c79a64 [incorrect, should be 0xd1f92cbf]
328:4:        [FCS Good: False]
328:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 318
18:2:    Identification: 0x306c (12396)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xbe52 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 869, Ack: 440, Len: 262
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
38:4:    Sequence number: 869    (relative sequence number)
34:0:    [Next sequence number: 1131    (relative sequence number)]
42:4:    Acknowledgment number: 440    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4104
48:2:    [Calculated window size: 4104]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4c2c [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 1325503232, TSecr 2787842490
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 1325503232
62:4:            Timestamp echo reply: 2787842490
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
279:49:    TCP segment data (49 bytes)
ssl:66:262:Secure Sockets Layer
66:207:    TLSv1 Record Layer: Handshake Protocol: New Session Ticket
66:1:        Content Type: Handshake (22)
67:2:        Version: TLS 1.0 (0x0301)
69:2:        Length: 202
71:202:        Handshake Protocol: New Session Ticket
71:1:            Handshake Type: New Session Ticket (4)
72:3:            Length: 198
text:75:198:            TLS Session Ticket
75:4:                Session Ticket Lifetime Hint: 300
79:2:                Session Ticket Length: 192
81:192:                Session Ticket: e265f83b3f31816110128fd37bfb7411eb57860e3d9fc93d...
273:6:    TLSv1 Record Layer: Change Cipher Spec Protocol: Change Cipher Spec
273:1:        Content Type: Change Cipher Spec (20)
274:2:        Version: TLS 1.0 (0x0301)
276:2:        Length: 1
278:1:        Change Cipher Spec Message

frame:0:252:Frame 16: 252 bytes on wire (2016 bits), 252 bytes captured (2016 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.306535000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.306535000 seconds
0:0:    [Time delta from previous captured frame: 0.000724000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000724000 seconds]
0:0:    [Time since reference or first frame: 3.359029000 seconds]
0:0:    Frame Number: 16
0:0:    Frame Length: 252 bytes (2016 bits)
0:0:    Capture Length: 252 bytes (2016 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
248:4:    Frame check sequence: 0xca7709f6 [incorrect, should be 0x93642189]
248:4:        [FCS Good: False]
248:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 238
18:2:    Identification: 0x68e0 (26848)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8c2e [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 440, Ack: 1135, Len: 182
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
38:4:    Sequence number: 440    (relative sequence number)
34:0:    [Next sequence number: 622    (relative sequence number)]
42:4:    Acknowledgment number: 1135    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 142
48:2:    [Calculated window size: 142]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x330e [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 2787842533, TSecr 1325503232
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 2787842533
62:4:            Timestamp echo reply: 1325503232
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
103:145:    TCP segment data (145 bytes)
ssl:66:182:Secure Sockets Layer
66:37:    TLSv1 Record Layer: Application Data Protocol: http
66:1:        Content Type: Application Data (23)
67:2:        Version: TLS 1.0 (0x0301)
69:2:        Length: 32
71:32:        Encrypted Application Data: bcac7bb15372231b6186397c24dfa33661885e77bca09cb2...

frame:0:66:Frame 17: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.306581000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.306581000 seconds
0:0:    [Time delta from previous captured frame: 0.000046000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000046000 seconds]
0:0:    [Time since reference or first frame: 3.359075000 seconds]
0:0:    Frame Number: 17
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19e5 [incorrect, should be 0x7117b2ac]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x4859 (18521)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xa76f (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959622466, Ack: 3115283413
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959622466    (relative sequence number)
42:4:    Acknowledgment number: 3115283413    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4098
48:2:    [Calculated window size: 4098]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:614:Frame 18: 614 bytes on wire (4912 bits), 614 bytes captured (4912 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.308134000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.308134000 seconds
0:0:    [Time delta from previous captured frame: 0.001553000 seconds]
0:0:    [Time delta from previous displayed frame: 0.001553000 seconds]
0:0:    [Time since reference or first frame: 3.360628000 seconds]
0:0:    Frame Number: 18
0:0:    Frame Length: 614 bytes (4912 bits)
0:0:    Capture Length: 614 bytes (4912 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
610:4:    Frame check sequence: 0xa8d1e1f2 [incorrect, should be 0x0d798732]
610:4:        [FCS Good: False]
610:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 600
18:2:    Identification: 0xe29f (58015)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x0b05 (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1135, Ack: 626, Len: 544
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
38:4:    Sequence number: 1135    (relative sequence number)
34:0:    [Next sequence number: 1679    (relative sequence number)]
42:4:    Acknowledgment number: 626    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4098
48:2:    [Calculated window size: 4098]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4d46 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 1325503233, TSecr 2787842533
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 1325503233
62:4:            Timestamp echo reply: 2787842533
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
529:81:    TCP segment data (81 bytes)
ssl:66:544:Secure Sockets Layer
66:37:    TLSv1 Record Layer: Application Data Protocol: http
66:1:        Content Type: Application Data (23)
67:2:        Version: TLS 1.0 (0x0301)
69:2:        Length: 32
71:32:        Encrypted Application Data: 0cb8d85909e4ccbc7de74d8e3fd32955a213314fc162b21c...
103:389:    TLSv1 Record Layer: Application Data Protocol: http
103:1:        Content Type: Application Data (23)
104:2:        Version: TLS 1.0 (0x0301)
106:2:        Length: 384
108:384:        Encrypted Application Data: 8d9d9b321f5dde9219cf2bcfeacbc36503fe967e59dea13f...
492:37:    TLSv1 Record Layer: Application Data Protocol: http
492:1:        Content Type: Application Data (23)
493:2:        Version: TLS 1.0 (0x0301)
495:2:        Length: 32
497:32:        Encrypted Application Data: 3f9e5b01ea6773b3641bd3557c630e2be184ccc73d9bd1ae...

frame:0:66:Frame 19: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309407000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309407000 seconds
0:0:    [Time delta from previous captured frame: 0.001273000 seconds]
0:0:    [Time delta from previous displayed frame: 0.001273000 seconds]
0:0:    [Time since reference or first frame: 3.361901000 seconds]
0:0:    Frame Number: 19
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0x4f019301 [incorrect, should be 0x53e78c45]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x68e1 (26849)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x8ce7 [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:32:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 3115283413, Ack: 1959623014
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 3115283413    (relative sequence number)
42:4:    Acknowledgment number: 1959623014    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x011 (FIN, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...1 = Fin: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection finish (FIN)]
0:0:                [Message: Connection finish (FIN)]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
48:2:    Window size value: 155
48:2:    [Calculated window size: 155]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0xbcee [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:66:Frame 20: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309500000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309500000 seconds
0:0:    [Time delta from previous captured frame: 0.000093000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000093000 seconds]
0:0:    [Time since reference or first frame: 3.361994000 seconds]
0:0:    Frame Number: 20
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19e8 [incorrect, should be 0xb3f66a7c]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x85fd (34301)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x69cb (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959623014, Ack: 3115283414
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959623014    (relative sequence number)
42:4:    Acknowledgment number: 3115283414    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x010 (ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4098
48:2:    [Calculated window size: 4098]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:103:Frame 21: 103 bytes on wire (824 bits), 103 bytes captured (824 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309585000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309585000 seconds
0:0:    [Time delta from previous captured frame: 0.000085000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000085000 seconds]
0:0:    [Time since reference or first frame: 3.362079000 seconds]
0:0:    Frame Number: 21
0:0:    Frame Length: 103 bytes (824 bits)
0:0:    Capture Length: 103 bytes (824 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp:ssl]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
99:4:    Frame check sequence: 0xe324293c [incorrect, should be 0x2945b534]
99:4:        [FCS Good: False]
99:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 89
18:2:    Identification: 0x4d08 (19720)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0xa29b (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1683, Ack: 627, Len: 33
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
38:4:    Sequence number: 1683    (relative sequence number)
34:0:    [Next sequence number: 1716    (relative sequence number)]
42:4:    Acknowledgment number: 627    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x018 (PSH, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 1... = Push: Set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 4098
48:2:    [Calculated window size: 4098]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b47 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
54:12:    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
text:54:1:        No-Operation (NOP)
54:1:            Type: 1
54:1:                0... .... = Copy on fragmentation: No
54:1:                .00. .... = Class: Control (0)
54:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:55:1:        No-Operation (NOP)
55:1:            Type: 1
55:1:                0... .... = Copy on fragmentation: No
55:1:                .00. .... = Class: Control (0)
55:1:                ...0 0001 = Number: No-Operation (NOP) (1)
text:56:10:        Timestamps: TSval 1325503235, TSecr 2787842536
56:1:            Kind: Timestamp (8)
57:1:            Length: 10
58:4:            Timestamp value: 1325503235
62:4:            Timestamp echo reply: 2787842536
34:0:    [SEQ/ACK analysis]
34:0:        [TCP Analysis Flags]
34:0:            [A segment before this frame wasn&#39;t captured]
expert:0:0:                [Expert Info (Warn/Sequence): Previous segment not captured (common at capture start)]
0:0:                    [Message: Previous segment not captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
34:0:            [This frame ACKs a segment we have not seen]
expert:0:0:                [Expert Info (Warn/Sequence): ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Message: ACKed segment that wasn&#39;t captured (common at capture start)]
0:0:                    [Severity level: Warn]
0:0:                    [Group: Sequence]
66:33:    TCP segment data (33 bytes)
ssl:66:33:Secure Sockets Layer

frame:0:66:Frame 22: 66 bytes on wire (528 bits), 66 bytes captured (528 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309649000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309649000 seconds
0:0:    [Time delta from previous captured frame: 0.000064000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000064000 seconds]
0:0:    [Time since reference or first frame: 3.362143000 seconds]
0:0:    Frame Number: 22
0:0:    Frame Length: 66 bytes (528 bits)
0:0:    Capture Length: 66 bytes (528 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Apple_52:5a:c7 (40:6c:8f:52:5a:c7), Dst: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:    Destination: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
62:4:    Frame check sequence: 0xa62b19e8 [incorrect, should be 0xd84ed639]
62:4:        [FCS Good: False]
62:4:        [FCS Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
ip:14:20:Internet Protocol Version 4, Src: 10.140.8.27 (10.140.8.27), Dst: 10.79.46.6 (10.79.46.6)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 52
18:2:    Identification: 0x5b29 (23337)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 64
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0x0000 [incorrect, should be 0x949f (may be caused by &quot;IP checksum offload&quot;?)]
24:2:        [Good: False]
24:2:        [Bad: True]
expert:0:0:            [Expert Info (Error/Checksum): Bad checksum]
0:0:                [Message: Bad checksum]
0:0:                [Severity level: Error]
0:0:                [Group: Checksum]
26:4:    Source: 10.140.8.27 (10.140.8.27)
30:4:    Destination: 10.79.46.6 (10.79.46.6)
tcp:34:32:Transmission Control Protocol, Src Port: https (443), Dst Port: 44716 (44716), Seq: 1959623051, Ack: 3115283414
34:2:    Source port: https (443)
36:2:    Destination port: 44716 (44716)
34:0:    [Stream index: 1]
text:34:0:    [Short segment. Segment/fragment does not contain a full TCP header (might be NMAP or someone else deliberately sending unusual packets)]
expert:0:0:        [Expert Info (Warn/Malformed): Short segment]
0:0:            [Message: Short segment]
0:0:            [Severity level: Warn]
0:0:            [Group: Malformed]
38:4:    Sequence number: 1959623051    (relative sequence number)
42:4:    Acknowledgment number: 3115283414    (relative ack number)
46:1:    Header length: 32 bytes
46:2:    Flags: 0x011 (FIN, ACK)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...1 .... = Acknowledgment: Set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .0.. = Reset: Not set
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...1 = Fin: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection finish (FIN)]
0:0:                [Message: Connection finish (FIN)]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
48:2:    Window size value: 4098
48:2:    [Calculated window size: 4098]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x4b22 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:14:0:[Malformed Packet: TCP]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:60:Frame 23: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309880000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309880000 seconds
0:0:    [Time delta from previous captured frame: 0.000231000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000231000 seconds]
0:0:    [Time since reference or first frame: 3.362374000 seconds]
0:0:    Frame Number: 23
0:0:    Frame Length: 60 bytes (480 bits)
0:0:    Capture Length: 60 bytes (480 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
54:6:    Padding: 000000000000
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 40
18:2:    Identification: 0x0000 (0)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0xf5d4 [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:20:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 627, Len: 0
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
38:4:    Sequence number: 627    (relative sequence number)
46:1:    Header length: 20 bytes
46:2:    Flags: 0x004 (RST)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...0 .... = Acknowledgment: Not set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .1.. = Reset: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection reset (RST)]
0:0:                [Message: Connection reset (RST)]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 0
48:2:    [Calculated window size: 0]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x86f7 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:0:0:[Malformed Packet: Ethernet]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]

frame:0:60:Frame 24: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
0:0:    WTAP_ENCAP: 1
0:0:    Arrival Time: Apr 28, 2017 08:47:49.309971000 UTC
0:0:    [Time shift for this packet: 0.000000000 seconds]
0:0:    Epoch Time: 1493369269.309971000 seconds
0:0:    [Time delta from previous captured frame: 0.000091000 seconds]
0:0:    [Time delta from previous displayed frame: 0.000091000 seconds]
0:0:    [Time since reference or first frame: 3.362465000 seconds]
0:0:    Frame Number: 24
0:0:    Frame Length: 60 bytes (480 bits)
0:0:    Capture Length: 60 bytes (480 bits)
0:0:    [Frame is marked: False]
0:0:    [Frame is ignored: False]
0:0:    [Protocols in frame: eth:ip:tcp]
eth:0:14:Ethernet II, Src: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc), Dst: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:    Destination: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:6:        Address: Apple_52:5a:c7 (40:6c:8f:52:5a:c7)
0:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
0:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
6:6:    Source: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:6:        Address: Cisco_ff:fd:cc (00:08:e3:ff:fd:cc)
6:3:        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
6:3:        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
12:2:    Type: IP (0x0800)
54:6:    Padding: 000000000000
ip:14:20:Internet Protocol Version 4, Src: 10.79.46.6 (10.79.46.6), Dst: 10.140.8.27 (10.140.8.27)
14:1:    Version: 4
14:1:    Header length: 20 bytes
15:1:    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
15:1:        0000 00.. = Differentiated Services Codepoint: Default (0x00)
15:1:        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
16:2:    Total Length: 40
18:2:    Identification: 0x0000 (0)
20:1:    Flags: 0x02 (Don&#39;t Fragment)
20:1:        0... .... = Reserved bit: Not set
20:1:        .1.. .... = Don&#39;t fragment: Set
20:1:        ..0. .... = More fragments: Not set
20:2:    Fragment offset: 0
22:1:    Time to live: 58
23:1:    Protocol: TCP (6)
24:2:    Header checksum: 0xf5d4 [correct]
24:2:        [Good: True]
24:2:        [Bad: False]
26:4:    Source: 10.79.46.6 (10.79.46.6)
30:4:    Destination: 10.140.8.27 (10.140.8.27)
tcp:34:20:Transmission Control Protocol, Src Port: 44716 (44716), Dst Port: https (443), Seq: 627, Len: 0
34:2:    Source port: 44716 (44716)
36:2:    Destination port: https (443)
34:0:    [Stream index: 1]
38:4:    Sequence number: 627    (relative sequence number)
46:1:    Header length: 20 bytes
46:2:    Flags: 0x004 (RST)
46:1:        000. .... .... = Reserved: Not set
46:1:        ...0 .... .... = Nonce: Not set
47:1:        .... 0... .... = Congestion Window Reduced (CWR): Not set
47:1:        .... .0.. .... = ECN-Echo: Not set
47:1:        .... ..0. .... = Urgent: Not set
47:1:        .... ...0 .... = Acknowledgment: Not set
47:1:        .... .... 0... = Push: Not set
47:1:        .... .... .1.. = Reset: Set
expert:0:0:            [Expert Info (Chat/Sequence): Connection reset (RST)]
0:0:                [Message: Connection reset (RST)]
0:0:                [Severity level: Chat]
0:0:                [Group: Sequence]
47:1:        .... .... ..0. = Syn: Not set
47:1:        .... .... ...0 = Fin: Not set
48:2:    Window size value: 0
48:2:    [Calculated window size: 0]
48:2:    [Window size scaling factor: -1 (unknown)]
50:2:    Checksum: 0x86f7 [validation disabled]
50:2:        [Good Checksum: False]
50:2:        [Bad Checksum: False]
malformed:0:0:[Malformed Packet: Ethernet]
expert:0:0:    [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)]
0:0:        [Message: Malformed Packet (Exception occurred)]
0:0:        [Severity level: Error]
0:0:        [Group: Malformed]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/2e1e083486948d2a22563b861609015d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frank%20Lin&#39;s gravatar image" /><p><span>Frank Lin</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frank Lin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '17, 03:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61153" class="comments-container"></div><div id="comment-tools-61153" class="comment-tools"></div><div class="clear"></div><div id="comment-61153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61155"></span>

<div id="answer-container-61155" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61155-score" class="post-score" title="current number of votes">1</div><span id="post-61155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Frank Lin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://wiki.wireshark.org/Development/LifeCycle#End_of_Life_planning">Wireshark 1.8 is old and unsupported</a>. Many improvements have entered successive versions so that is why it is possible that 2.2 is working while 1.8 is not working.</p><p>Based on your debug log, it seems that Wireshark was able to find the required information from the server side but failed to find the information from the client side.</p><p>You are recommended to upgrade to 2.2 or later.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '17, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '17, 07:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-61155" class="comments-container"></div><div id="comment-tools-61155" class="comment-tools"></div><div class="clear"></div><div id="comment-61155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

