+++
type = "question"
title = "unable to decode SSL"
description = '''Hi, I have configured preference -&amp;gt;ssl with the private key.But still wireshark is unable to decode ssl.Below is the output from the log file. ssl_association_remove removing TCP 443 - http handle 0000000003D911A0 Private key imported: KeyID 52:53:3d:d3:ce:ce:cd:2e:29:ab:0b:c8:0b:ca:78:ba:... ssl...'''
date = "2012-04-19T08:48:00Z"
lastmod = "2012-04-19T09:03:00Z"
weight = 10286
keywords = [ "ssl", "decrypt" ]
aliases = [ "/questions/10286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unable to decode SSL](/questions/10286/unable-to-decode-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10286-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have configured preference -&gt;ssl with the private key.But still wireshark is unable to decode ssl.Below is the output from the log file.</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0000000003D911A0
Private key imported: KeyID 52:53:3d:d3:ce:ce:cd:2e:29:ab:0b:c8:0b:ca:78:ba:...
ssl_init IPv4 addr &#39;IPaddressofmyserver&#39; (IPaddressofmyserver) port &#39;443&#39; filename &#39;c:\\BckUP\\server.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file c:\\BckUP\\server.pem successfully loaded.
association_add TCP port 443 protocol http handle 0000000003D911A0

dissect_ssl enter frame #3 (first time)
ssl_session_init: initializing ptr 0000000005871BC0 size 680
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 141
packet_from_server: is from server - FALSE
ssl_find_private_key server IPaddressofmyserver:443
client random len: 16 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #9 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 262, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
ssl_decrypt_pre_master_secret key exchange 0 different from KEX_RSA (16)
dissect_ssl3_handshake can&#39;t decrypt pre master secret

dissect_ssl enter frame #10 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #11 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37

dissect_ssl enter frame #13 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 340
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 335, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 31891 found 0000000000000000
association_find: TCP port 443 found 00000000057ABA10

dissect_ssl enter frame #14 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 1448
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 1565, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder

dissect_ssl enter frame #15 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 122

dissect_ssl enter frame #16 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 29
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 24, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 31891 found 0000000000000000
association_find: TCP port 443 found 00000000057ABA10

dissect_ssl enter frame #19 (first time)
  conversation = 0000000005871880, ssl_session = 0000000005871BC0
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18, ssl state 0x11
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37

dissect_ssl enter frame #13 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 340
dissect_ssl3_record: content_type 23
association_find: TCP port 31891 found 0000000000000000
association_find: TCP port 443 found 00000000057ABA10

dissect_ssl enter frame #14 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 1448

dissect_ssl enter frame #15 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 122

dissect_ssl enter frame #16 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 29
dissect_ssl3_record: content_type 23
association_find: TCP port 31891 found 0000000000000000
association_find: TCP port 443 found 00000000057ABA10

dissect_ssl enter frame #19 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 23
dissect_ssl3_record: content_type 21

dissect_ssl enter frame #10 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec

dissect_ssl enter frame #9 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267

dissect_ssl enter frame #3 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 141

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37

dissect_ssl enter frame #9 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267

dissect_ssl enter frame #11 (already visited)
  conversation = 0000000005871880, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 187 offset 5 length 4019139 bytes, remaining 37</code></pre><p>please help me ,how can i decode the ssl.</p></div><div id="question-tags" class="tags-container tags">ssl decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/54dfb1796a8beedf9843a326d673eaae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vikram&#39;s gravatar image" /><p>vikram<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vikram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '12, 08:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10286" class="comments-container"></div><div id="comment-tools-10286" class="comment-tools"></div><div class="clear"></div><div id="comment-10286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10287"></span>

<div id="answer-container-10287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10287-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There doesn't appear to be any frames that come from the server, at least I can't see any with <code>packet_from_server: is from server - TRUE</code>. Did you capture both sides of the conversation?</p><p>I'm also assuming that the entries such as <code>'IPaddressofmyserver'</code> are a result of you doing a search and replace on the log file for obfuscation purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10287" class="comments-container"><span id="10319"></span><div id="comment-10319" class="comment"><div id="post-10319-score" class="comment-score"></div><div class="comment-text"><p>No ,as you said i didn't captured both sides <a href="http://conversation.So">conversation.So</a> do i need to capture conversation from both sides,if i do that ,how can we merge the two log files?Can you kindly let me?</p><p>'IPaddressofmyserver' is modifed by me..</p></div><div id="comment-10319-info" class="comment-info"><span class="comment-age">(19 Apr '12, 20:00)</span> vikram</div></div><span id="10335"></span><div id="comment-10335" class="comment not_top_scorer"><div id="post-10335-score" class="comment-score"></div><div class="comment-text"><p>To decrypt SSL, Wireshark needs to see both sides of the conversation, that is packets from both the client and the server <strong>from the start</strong> of the conversation.</p><p>You can try using mergecap to merge the two captures. See the manual page <a href="http://www.wireshark.org/docs/man-pages/mergecap.html">here</a> and info from the documentation <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolsmergecap.html">here</a></p></div><div id="comment-10335-info" class="comment-info"><span class="comment-age">(20 Apr '12, 02:01)</span> grahamb ♦</div></div><span id="10348"></span><div id="comment-10348" class="comment not_top_scorer"><div id="post-10348-score" class="comment-score"></div><div class="comment-text"><p>Maybe "sides" is a bit misleading. You need both flows (client-&gt;server and server-&gt;cient) of the TCP session in the trace.</p><p>It is OK to capture only on one location (at the client, at the server or somewhere in between).</p></div><div id="comment-10348-info" class="comment-info"><span class="comment-age">(20 Apr '12, 05:35)</span> SYN-bit ♦♦</div></div><span id="10371"></span><div id="comment-10371" class="comment not_top_scorer"><div id="post-10371-score" class="comment-score"></div><div class="comment-text"><p>currently i am capturing at one location atclient..i used a command called tcpflow and captured the conversation in a .log <a href="http://file.Is">file.Is</a> there any command line option to do the same in wireshark ?Also after decode of the SSL, will i be albe to see/capture the atual payload(soap xml in my case) that is getting exchanged between the client and server ?</p></div><div id="comment-10371-info" class="comment-info"><span class="comment-age">(21 Apr '12, 01:45)</span> vikram</div></div><span id="10373"></span><div id="comment-10373" class="comment not_top_scorer"><div id="post-10373-score" class="comment-score"></div><div class="comment-text"><p>Yes, in Wireshark you can use "Follow SSL stream" to get a dump of the decrypted data from the SSL session.</p><p>You might be able to reconstruct the whole ssl session by merging two matching flows saved by tcpflow. When you loaded x.x.x.x:a-&gt;y.y.y.y:443, you can merge with:</p><pre><code>mergecap -w out.pcap x.x.x.x:a-&gt;y.y.y.y:443.pcap y.y.y.y:443-&gt;x.x.x.x:a.pcap</code></pre><p>(or something like that, I don't know how tcpflow names the individual files for each flow)</p></div><div id="comment-10373-info" class="comment-info"><span class="comment-age">(21 Apr '12, 03:27)</span> SYN-bit ♦♦</div></div><span id="10376"></span><div id="comment-10376" class="comment not_top_scorer"><div id="post-10376-score" class="comment-score"></div><div class="comment-text"><p>ok..i am aware of Follow ssl stream(GUI option)..but i wanted to know the command line..please let me know if we have command line option for the same..wat i want is to decode ssl messges(live) and write to a file..</p></div><div id="comment-10376-info" class="comment-info"><span class="comment-age">(21 Apr '12, 08:15)</span> vikram</div></div><span id="10421"></span><div id="comment-10421" class="comment not_top_scorer"><div id="post-10421-score" class="comment-score"></div><div class="comment-text"><p>Hi, I used the tshark command mentioned below and opened the log(vik24_01.log ) using wireshark in GUI.and when i click on Follow SSL stream,new window that comes up is blank and says conversation bytes zero.</p><p><code>tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: MYSERVERIP,443,http,server.pem" -o "ssl.debug_file: wireshark01.log" -i eth1 -R "tcp.port == 443" -w vik24_01.log</code></p><p>unable to understand why i am not able to see decrypted (should be a XML message in my case) message.</p></div><div id="comment-10421-info" class="comment-info"><span class="comment-age">(24 Apr '12, 05:49)</span> vikram</div></div><span id="10424"></span><div id="comment-10424" class="comment not_top_scorer"><div id="post-10424-score" class="comment-score"></div><div class="comment-text"><p>I see the below output in ssl debug file..it looks like this time..tshark is able to decode the ssl..but still i see the data in some hexdecimal formart (it should be xml in my case after decode) eg:- pre master encrypted[256]: 65 8c f3 c2 07 7f ba dc 36 e9 b6 ab ce 37 85 9a not sure if the above is the data the is decrypted and exchanged between the applications ?</p><pre><code>ssl_init keys string:
MYSERVERIP,443,http,server.pem
ssl_init found host entry MYSERVERIP,443,http,server.pem
ssl_init addr &#39;MYSERVERIP&#39; port &#39;443&#39; filename &#39;server.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 9F:15:AA:5E:9F:7E:56:2E:60:DD:9C:49:68:A3:00:CD:...
ssl_init private key file server.pem successfully loaded
association_add TCP port 443 protocol http handle 0x8bdcf50
association_find: TCP port 993 found 0x91e6608
ssl_association_remove removing TCP 993 - imap handle 0x8d5ac78
association_add TCP port 993 protocol imap handle 0x8d5ac78
association_find: TCP port 995 found 0x91e6640
ssl_association_remove removing TCP 995 - pop handle 0x8e18650
association_add TCP port 995 protocol pop handle 0x8e18650

dissect_ssl enter frame #45 (first time)
ssl_session_init: initializing ptr 0xb67ed3d8 size 564
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
dissect_ssl server MYSERVERIP:443
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
client random len: 16 padded to 32

dissect_ssl enter frame #51 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello not enough data to generate key (required 0x37)

dissect_ssl enter frame #53 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8

dissect_ssl enter frame #55 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8

dissect_ssl enter frame #57 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 3914 ssl, state 0x17
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3910 bytes, remaining 3919

dissect_ssl enter frame #58 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4 ssl, state 0x17
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #71 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 262 ssl, state 0x17
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
dissect_ssl3_handshake found SSL_HND_CLIENT_KEY_EXCHG state 0x17
pre master encrypted[256]:
65 8c f3 c2 07 7f ba dc 36 e9 b6 ab ce 37 85 9a 
1b 74 09 ad b3 85 58 29 90 6b 85 c7 57 77 9b 62 
44 f6 a1 13 f9 d4 cd cf d4 ac cb 6f 9a 85 73 b3 
1b 41 15 1c ec 4d 4f c4 cf 5b df a7 f5 37 68 8f 
9f b0 9e dd 58 86 5d 1e 99 63 d1 17 9c fd 95 c3 
dd 23 2e 36 98 e5 74 66 58 dc 98 35 1a c3 2a 50 
47 61 8f ef db b7 39 2a 6e 22 cf 2c 3b 1b 17 41 
24 ac 68 0e 0a 45 7d 8e 51 7d 0b 3e 80 5b 83 1a 
0b cf 6c 55 1a ce 35 3b 0c d7 54 31 87 56 40 95 
a0 e9 0c 82 97 7e 96 2f 1e ea f7 4a 0f a0 fc d8 
84 c7 f1 92 42 0f a7 c9 8d 26 d3 44 62 70 7a 19 
3a 84 9d 70 ec 9d 37 1d d0 11 73 7b 90 6c a2 85 
d3 7d c7 05 17 42 ea fc cf 89 cf a4 dc 01 1c 6b 
f8 27 7e bd ed 55 6a 84 a9 1b e0 8b ff f2 d6 9a 
87 d3 14 29 01 9a 47 7e fa a4 ba 39 f9 ef 94 b3 
dd 10 c3 4d 04 76 a1 d6 1f f0 6b d8 8f 06 7d 2b 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 34 bytes, decr_len 256
decrypted_unstrip_pre_master[256]:
65 97 fc 2a b6 d6 50 67 de 69 1e 95 62 51 62 3c 
39 ef 7e 47 a4 ee 57 0a 39 84 cf 0b a6 f7 28 b7 
df 00 b1 d6 5a d0 90 4c ae 42 59 e3 89 f2 e9 25 
93 a7 fa b3 d6 70 bb c5 8f fd f2 94 b4 87 45 e7 
05 22 8b d4 86 21 b3 2e 5c 62 85 12 0c 2e 8a 52 
40 ee 66 9c f7 1c 60 8d 85 e3 26 96 d1 a9 f2 d3 
0f 0c 93 66 3c 2e 95 2b c0 4b fa 99 06 fc ad 3d 
33 3a 34 e9 87 08 12 6a 58 f3 c4 8f 16 ff 2d 56 
b2 4d a4 e2 17 23 d7 56 e4 10 52 89 4f b2 f3 58 
68 db a0 fd 30 f2 44 eb dd 26 f6 49 c2 48 5d 1c 
26 c4 0c 43 18 fc b3 50 66 03 b5 3c 17 c7 56 c8 
ba fa 86 f9 99 3b 8c fd 7a 98 47 4a 89 d9 48 dc 
ac c3 d7 ee 3a 1f c4 8f 07 f0 64 e9 95 3c 3c 50 
a5 7c 00 07 26 8d 4e 10 b9 f9 c2 2a 1a f8 d3 1f 
c8 6a 58 d6 5e 72 03 f3 f2 ac 38 85 b3 83 50 24 
a0 72 24 33 0a 05 ba 0b c8 6b 7c d6 34 cb 46 04 
ssl_decrypt_pre_master_secret wrong pre_master_secret length (222, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret

dissect_ssl enter frame #72 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #73 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 7452990 bytes, remaining 37

dissect_ssl enter frame #76 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #77 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 118 offset 5 length 10820990 bytes, remaining 37

dissect_ssl enter frame #79 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 335 ssl, state 0x17
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 59763 found (nil)
association_find: TCP port 443 found 0x934b4e8

dissect_ssl enter frame #80 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 732 ssl, state 0x17
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 59763 found (nil)
association_find: TCP port 443 found 0x934b4e8

dissect_ssl enter frame #81 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 24 ssl, state 0x17
association_find: TCP port 59763 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 59763 found (nil)
association_find: TCP port 443 found 0x934b4e8

dissect_ssl enter frame #99 (first time)
  conversation = 0xb67ed200, ssl_session = 0xb67ed3d8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 723 ssl, state 0x17
association_find: TCP port 443 found 0x934b4e8
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x934b4e8</code></pre></div><div id="comment-10424-info" class="comment-info"><span class="comment-age">(24 Apr '12, 19:58)</span> vikram</div></div><span id="10428"></span><div id="comment-10428" class="comment not_top_scorer"><div id="post-10428-score" class="comment-score"></div><div class="comment-text"><p>From your log:</p><p><code>ssl_decrypt_pre_master_secret wrong pre_master_secret length (222, expected 48) dissect_ssl3_handshake can't decrypt pre master secret</code></p><p>There's still something wrong, hence the lack of decryption.</p></div><div id="comment-10428-info" class="comment-info"><span class="comment-age">(25 Apr '12, 01:39)</span> grahamb ♦</div></div><span id="10446"></span><div id="comment-10446" class="comment"><div id="post-10446-score" class="comment-score">1</div><div class="comment-text"><p>The log message "ssl_decrypt_pre_master_secret wrong pre_master_secret length (222, expected 48)" usually indicates that the private key does not match the certificate. Although recently I have seen it also happening with a specific version of the GnuTLS library. Which Wireshark version are you using and which library versions (see "About Wireshark")</p></div><div id="comment-10446-info" class="comment-info"><span class="comment-age">(25 Apr '12, 13:53)</span> SYN-bit ♦♦</div></div><span id="10565"></span><div id="comment-10565" class="comment not_top_scorer"><div id="post-10565-score" class="comment-score"></div><div class="comment-text"><p>1.) please post the new debug file.</p><p>2.) did you capture the WHOLE frame? This is only important if you did not capture with tshark/wireshark. Other sniffers might limit the packet size to 60-100 byte per default. If you don't change that, you'll be unable to decrypt SSL. For tcpdump use -s0.</p><p>3.) Is the given private key encrypted? Look for lines with the string "ENCRYPTED" in the pem file.</p><p>4.) Just by chance: Can you please verify that your SSL connection is NOT using any DH (Diffie Hellman) algorithms - look for DH or DHE in the cipher suite name (Cipher Suites in Server HELO). If DH is used, there is no (known) way to decrypt the session.</p><p>Regards<br />
Kurt</p></div><div id="comment-10565-info" class="comment-info"><span class="comment-age">(01 May '12, 22:49)</span> Kurt Knochner ♦</div></div><span id="10568"></span><div id="comment-10568" class="comment not_top_scorer"><div id="post-10568-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Please find my asnwers as below</p><p>1) debug file</p><pre><code>ssl_init keys string:
SERVERIP,443,http,osbserverkeyoutHTB.pem
ssl_init found host entry SERVERIP,443,http,osbserverkeyoutHTB.pem
ssl_init addr &#39;SERVERIP&#39; port &#39;443&#39; filename &#39;osbserverkeyoutHTB.pem&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 9F:15:AA:5E:9F:7E:56:2E:60:DD:9C:49:68:A3:00:CD:...
ssl_init private key file osbserverkeyoutHTB.pem successfully loaded
association_add TCP port 443 protocol http handle 0x881ff50
association_find: TCP port 993 found 0x8e29608
ssl_association_remove removing TCP 993 - imap handle 0x899dc78
association_add TCP port 993 protocol imap handle 0x899dc78
association_find: TCP port 995 found 0x8e29640
ssl_association_remove removing TCP 995 - pop handle 0x8a5b650
association_add TCP port 995 protocol pop handle 0x8a5b650

dissect_ssl enter frame #39 (first time)
ssl_session_init: initializing ptr 0xb67f6ed8 size 564
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
dissect_ssl server SERVERIP:443
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
client random len: 16 padded to 32

dissect_ssl enter frame #41 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 58 ssl, state 0x11
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 54 bytes, remaining 63 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello not enough data to generate key (required 0x37)

dissect_ssl enter frame #43 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8

dissect_ssl enter frame #45 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8

dissect_ssl enter frame #47 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 3914 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3910 bytes, remaining 3919

dissect_ssl enter frame #49 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 14 offset 5 length 0 bytes, remaining 9

dissect_ssl enter frame #51 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 262 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
dissect_ssl3_handshake found SSL_HND_CLIENT_KEY_EXCHG state 0x17
pre master encrypted[256]:
0a 66 ca bb 03 70 b8 d2 11 47 d5 d5 d9 98 bc b6 
37 52 3a 6a b5 21 d6 63 2e 58 eb bb 7c 83 0e 5c 
31 8d 90 59 9b bc 38 ac 77 88 2f ec e9 4c 10 7f 
be 09 e4 d6 f6 88 54 62 c7 3c 30 c0 5b 4d a3 cf 
24 bd d6 91 40 73 c4 43 77 03 91 f8 d8 e0 91 47 
4f 65 bb 67 ca a0 1a 1b 9e 97 bd 3c 14 97 44 1f 
29 2f 6c de e8 d4 69 1a 85 b2 3e f8 36 8d bf e7 
de 4a 4f 20 b3 1d 25 95 58 55 04 88 86 64 e7 9f 
ac d6 05 16 78 8c ec 48 a0 53 81 e5 3a 64 e0 5e 
e6 05 79 1b 58 30 6d 36 e6 8e ea c6 ba da fe a7 
26 5f 90 2d 38 29 65 9b 45 1e d4 e2 73 84 d0 1a 
dc 96 49 ec 09 6b af 57 b8 ca 45 f5 6c bb ce a4 
db b2 c6 47 59 03 64 5d 4e 7b e5 cf bd 1b 6e 5c 
16 a8 ce 34 73 38 db d1 95 ae 57 6f d8 fa a5 06 
08 73 05 07 9f 96 37 60 a9 5f 9b 10 2f 12 9d b4 
95 05 6c 3e 52 83 6f 61 99 21 38 85 f9 74 09 83 
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 0 bytes, decr_len 256
decrypted_unstrip_pre_master[256]:
39 30 71 23 f2 66 4a c6 d4 36 b2 b6 bf e8 b5 0c 
de 0d dc 4f df 7e 72 ac b1 b3 9a b2 dc b7 a4 02 
6c dc 72 0f 79 4a c7 b1 50 d3 d5 95 53 6a 18 1c 
82 44 17 d2 6b 26 20 05 fa d2 02 fc a8 eb 66 b9 
74 a5 35 a1 70 78 ff 97 2f 27 1b 8c db fa 8e 44 
59 23 a3 d3 5a d1 ea dd 6c b1 b8 c6 99 02 c8 bd 
e4 06 ed d5 5d b7 a2 9b 34 28 ff 34 6d a2 bd 10 
a2 a3 c3 46 a5 95 83 52 71 11 0a 7b ab 7e 5d 17 
26 7b aa 0d dc 30 a8 0c f8 0b 8e dd 4e ed fb ab 
aa e6 51 63 c0 a2 5e 67 b4 87 28 22 98 89 e7 6e 
dc 11 6d 91 40 2d aa 48 d5 f1 03 07 cc 10 08 df 
ad e0 96 69 c2 36 19 b8 42 1c eb ea 4e e7 61 72 
07 83 51 80 6b dc 9c f3 47 d3 32 1e d1 b7 f1 05 
9e 10 76 89 5e 41 cb f9 f6 84 c3 c6 33 5c 4e 4f 
02 27 93 ed b0 da 35 44 1f e0 5d 63 85 2c fa 94 
fd 3a f6 5e ee 4e d5 dc ad f5 10 62 9a 7b 0d bf 
ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret

dissect_ssl enter frame #52 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #54 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 71 offset 5 length 13161076 bytes, remaining 37

dissect_ssl enter frame #57 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #58 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 32 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 186 offset 5 length 16179502 bytes, remaining 37

dissect_ssl enter frame #60 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 335 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 12056 found (nil)
association_find: TCP port 443 found 0x8f8e710

dissect_ssl enter frame #61 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 726 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 12056 found (nil)
association_find: TCP port 443 found 0x8f8e710

dissect_ssl enter frame #62 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 24 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 12056 found (nil)
association_find: TCP port 443 found 0x8f8e710

dissect_ssl enter frame #67 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 262 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x8f8e710

dissect_ssl enter frame #68 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8

dissect_ssl enter frame #70 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8

dissect_ssl enter frame #71 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8

dissect_ssl enter frame #73 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 5182 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0x8f8e710

dissect_ssl enter frame #74 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 12056 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available

dissect_ssl enter frame #76 (first time)
  conversation = 0xb67f6d00, ssl_session = 0xb67f6ed8
dissect_ssl3_record: content_type 21
decrypt_ssl3_record: app_data len 18 ssl, state 0x17
association_find: TCP port 443 found 0x8f8e710
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre><p>2) I used tshark.</p><p>3) Private key is not encrypted</p><p>4) I see only one Cipher suite used for "server hello" and it is <code>TLS_RSA_WITH_RC4_128_MD5</code></p></div><div id="comment-10568-info" class="comment-info"><span class="comment-age">(01 May '12, 23:13)</span> vikram</div></div><span id="10590"></span><div id="comment-10590" class="comment not_top_scorer"><div id="post-10590-score" class="comment-score"></div><div class="comment-text"><p>i am still having the issue with decoding ..in the debug file i see a message "ssl_decrypt_pre_master_secret wrong pre_master_secret length (256, expected 48) dissect_ssl3_handshake can't decrypt pre master secret"</p><p>"decrypt_ssl3_record: using server decoder decrypt_ssl3_record: no decoder available"</p><p>Does this message means i am using a wrong private key ?To the best of my knowledge i am using the correct key.</p></div><div id="comment-10590-info" class="comment-info"><span class="comment-age">(02 May '12, 04:54)</span> vikram</div></div><span id="10594"></span><div id="comment-10594" class="comment not_top_scorer"><div id="post-10594-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit, I am sorry didn't saw your comment on my issue.I am using Version 1.6.7 (SVN Rev 41973 from /trunk-1.6 of wireshark</p></div><div id="comment-10594-info" class="comment-info"><span class="comment-age">(02 May '12, 05:50)</span> vikram</div></div><span id="10595"></span><div id="comment-10595" class="comment not_top_scorer"><div id="post-10595-score" class="comment-score"></div><div class="comment-text"><p>Please find my About Wireshark as below</p><p>Version 1.6.7 (SVN Rev 41973 from /trunk-1.6) Compiled (64-bit) with GTK+ 2.22.1, with GLib 2.26.1, with WinPcap (version unknown), with libz 1.2.5, without POSIX capabilities, without libpcre, without SMI, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS 2.12.18, with Gcrypt 1.4.6, without Kerberos, with GeoIP, with PortAudio V19-devel (built Apr 6 2012), with AirPcap.version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.12.18, Gcrypt 1.4.6, without AirPcap</p></div><div id="comment-10595-info" class="comment-info"><span class="comment-age">(02 May '12, 05:51)</span> vikram</div></div><span id="10596"></span><div id="comment-10596" class="comment not_top_scorer"><div id="post-10596-score" class="comment-score"></div><div class="comment-text"><p>Running on 64-bit Windows 7, build 7600, with WinPcap version 4.1.2 (packet.dll</p></div><div id="comment-10596-info" class="comment-info"><span class="comment-age">(02 May '12, 05:51)</span> vikram</div></div><span id="10597"></span><div id="comment-10597" class="comment not_top_scorer"><div id="post-10597-score" class="comment-score"></div><div class="comment-text"><p>I did some testing. Whenever the key does not match the certificate, I get exactly the same error message (see also comment of SYN-bit). However in my case: WinXP SP3 32-Bit.</p><p>Please check your key. How did you get (export) the key?</p></div><div id="comment-10597-info" class="comment-info"><span class="comment-age">(02 May '12, 06:19)</span> Kurt Knochner ♦</div></div><span id="10599"></span><div id="comment-10599" class="comment not_top_scorer"><div id="post-10599-score" class="comment-score"></div><div class="comment-text"><p>Also when we run the tshark command ,do we need to provide the private keys of both client and server ?</p></div><div id="comment-10599-info" class="comment-info"><span class="comment-age">(02 May '12, 06:50)</span> vikram</div></div><span id="10600"></span><div id="comment-10600" class="comment not_top_scorer"><div id="post-10600-score" class="comment-score"></div><div class="comment-text"><p>unless you are using client certificates, there is no client private key.</p><p>BTW: does the server request a client cert?</p></div><div id="comment-10600-info" class="comment-info"><span class="comment-age">(02 May '12, 06:53)</span> Kurt Knochner ♦</div></div><span id="10615"></span><div id="comment-10615" class="comment"><div id="post-10615-score" class="comment-score">1</div><div class="comment-text"><p>And even if you are using client certificates, you only need the server private key for decryption.</p></div><div id="comment-10615-info" class="comment-info"><span class="comment-age">(02 May '12, 14:27)</span> SYN-bit ♦♦</div></div><span id="10622"></span><div id="comment-10622" class="comment not_top_scorer"><div id="post-10622-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit ..can you please verify the details of the verision of wireshark and GnuTLS library that i am using..I have posted the details of the versions in the previous comments ..please let me know if the issue is with the version's i am using? Also i have two private keys in the jks keystore at the client side and i tried using both of them for decrypting in the tshark command.I am unable to export the server side private key,unfortunatley i don't remember the password of the p12 wallet file at the server side.</p></div><div id="comment-10622-info" class="comment-info"><span class="comment-age">(03 May '12, 00:15)</span> vikram</div></div><span id="10625"></span><div id="comment-10625" class="comment not_top_scorer"><div id="post-10625-score" class="comment-score"></div><div class="comment-text"><p>You <strong>must</strong> use the server key for decrypting, that is a basic part of ssl.</p></div><div id="comment-10625-info" class="comment-info"><span class="comment-age">(03 May '12, 02:32)</span> grahamb ♦</div></div><span id="10626"></span><div id="comment-10626" class="comment not_top_scorer"><div id="post-10626-score" class="comment-score"></div><div class="comment-text"><p>If i am not wrong we import the server key into the client keystore as well,as part of enabling SSL between client and server?In our scenario we raised a CSR request and got the digital signed certificates and then we imported them into the client keystore as well.</p></div><div id="comment-10626-info" class="comment-info"><span class="comment-age">(03 May '12, 03:07)</span> vikram</div></div><span id="10628"></span><div id="comment-10628" class="comment"><div id="post-10628-score" class="comment-score">1</div><div class="comment-text"><p>Well, I don't have a compatability list, but if you use a Wireshark version downloaded from <a href="http://www.wireshark.org">www.wireshark.org</a>, you should be fine.</p><p>When you create a CSR and let the server sign it, the you <em>don't</em> import the servers private key, you import a certificate which has been signed by the servers private key.</p><p>If you say "I am unable to export the server side private key,unfortunatley i don't remember the password of the p12 wallet file at the server side", you clearly state where your problem lies... You need this key.</p></div><div id="comment-10628-info" class="comment-info"><span class="comment-age">(03 May '12, 04:10)</span> SYN-bit ♦♦</div></div><span id="10633"></span><div id="comment-10633" class="comment not_top_scorer"><div id="post-10633-score" class="comment-score"></div><div class="comment-text"><p>so ..at the client side ..do we import the certificates which has been signed by the third party or do we export the private key of server and import it at the client side server ? If my dought is correct and we import the server private key at the client side application server then what i have been using till these will be the correct key(in the tshark command)</p></div><div id="comment-10633-info" class="comment-info"><span class="comment-age">(03 May '12, 05:31)</span> vikram</div></div><span id="10636"></span><div id="comment-10636" class="comment"><div id="post-10636-score" class="comment-score">1</div><div class="comment-text"><p>Let's make things easier... forget about whether or not you are using client certificates, they don't play a role in SSL decryption.</p><p>When you captured SSL traffic that you want to decrypt, there are TCP sessions initiated by the client with as destination the server. This server presents a certificate back to the client in the TCP session. This certificate corresponds to a private key on the server. It is this private key on the server that you will need to use in wireshark to decrypt the session.</p><p>Where the key resides on the server can be found in the configuration of the (web)server.</p></div><div id="comment-10636-info" class="comment-info"><span class="comment-age">(03 May '12, 07:25)</span> SYN-bit ♦♦</div></div><span id="10638"></span><div id="comment-10638" class="comment not_top_scorer"><div id="post-10638-score" class="comment-score"></div><div class="comment-text"><p>if it's a windows HTTP server, go to the server and open certmgr. Select the certificate and export it. If the private key is "exportable", select the option to include the private key. The resulting pcks#12 file will contain the cert and the private key. Use openssl to extract the private key.</p><p>if it's a webserver on unix, the private key will be located in a file (PEM/PKCS#12). In case of an encrypted PEM or a PKCS#12, the 'passphrase' to open that file must be part of the webserver configuration. Find that passphrase and decrypt the key.</p><p>Use the decrypted key (or PCKS#12) in wireshark!</p></div><div id="comment-10638-info" class="comment-info"><span class="comment-age">(03 May '12, 07:37)</span> Kurt Knochner ♦</div></div><span id="10659"></span><div id="comment-10659" class="comment not_top_scorer"><div id="post-10659-score" class="comment-score"></div><div class="comment-text"><p>Hi, At the client it is weblogic,and i used keytool commands and found there are two private keys in the keystore(jks file),Which i thoguht one of them to be the server private key (server side it is oracle app server p12 wallet file).SYN-bit please validate my statement "when we enable SSL between two server's,Server private key will not be imported at the client application server" .If this is correct then i need to find a way to get the private key from the server side wallet file(since i dont remember the password).</p></div><div id="comment-10659-info" class="comment-info"><span class="comment-age">(03 May '12, 20:55)</span> vikram</div></div><span id="10662"></span><div id="comment-10662" class="comment not_top_scorer"><div id="post-10662-score" class="comment-score"></div><div class="comment-text"><p>there is no reason to import the server key at the 'client' and apparently the key you are using in wireshark is not the right one. BTW: Have you tried to use ONLY the key, you believe to be the server key, in wirehark? If that all does not help, you'll need the passphrase for the p12 file of the oracle app server. The admin of that server should have the passphrase.</p></div><div id="comment-10662-info" class="comment-info"><span class="comment-age">(03 May '12, 22:53)</span> Kurt Knochner ♦</div></div><span id="10663"></span><div id="comment-10663" class="comment not_top_scorer"><div id="post-10663-score" class="comment-score"></div><div class="comment-text"><p>yes..i used the private key..which i belived was the servers private key.with tshark and the output of the debug file i have posted..above..</p></div><div id="comment-10663-info" class="comment-info"><span class="comment-age">(04 May '12, 01:15)</span> vikram</div></div><span id="10666"></span><div id="comment-10666" class="comment not_top_scorer"><div id="post-10666-score" class="comment-score"></div><div class="comment-text"><p>O.K. then it's the wrong key. Get the p12 file and the passphrase from the oracle wallet.</p></div><div id="comment-10666-info" class="comment-info"><span class="comment-age">(04 May '12, 01:57)</span> Kurt Knochner ♦</div></div><span id="11416"></span><div id="comment-11416" class="comment not_top_scorer"><div id="post-11416-score" class="comment-score"></div><div class="comment-text"><p>Hi all, I am able to decrypt the ssl ,after i regenerated the certificates and used the servers private key. I am intrested in reading the xml payload and writing it to file(planing to use a java code) .In the ssl debug file generated by the tshark i can see the payload ,however the problem here that payload is broken into parts ,which is making it difficult to read and get the full payload with out decryption related. So is there any way to read only the payload from the catptured ssl dump file or ssl debug file using tshark or any other command line tool?</p></div><div id="comment-11416-info" class="comment-info"><span class="comment-age">(27 May '12, 23:53)</span> vikram</div></div></div><div id="comment-tools-10287" class="comment-tools"><span class="comments-showing"> showing 5 of 32 </span> <a href="#" class="show-all-comments-link">show 27 more comments</a></div><div class="clear"></div><div id="comment-10287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

