+++
type = "question"
title = "SSL Decrypt difficulty"
description = '''I&#x27;m trying to decrypt an https stream between Safari (where I&#x27;m also running wireshark) and an openlitespeed server on a linux box. I have the private key for the server and it is in the proper format. I have disabled Diffie Hellman and have SSLv3 and TLSv1.2 enabled. I&#x27;ve used different combination...'''
date = "2014-09-11T13:51:00Z"
lastmod = "2014-09-11T13:51:00Z"
weight = 36212
keywords = [ "ssl", "decrypt" ]
aliases = [ "/questions/36212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decrypt difficulty](/questions/36212/ssl-decrypt-difficulty)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt an https stream between Safari (where I'm also running wireshark) and an openlitespeed server on a linux box. I have the private key for the server and it is in the proper format. I have disabled Diffie Hellman and have SSLv3 and TLSv1.2 enabled. I've used different combinations of SSLv3 and TLS versions and all have the same result. Wireshark is picking up the private key correctly, but I'm getting an error that no decoders are available. Here's the top of the debug log with SSLv3 and TLSv1.2, no DH, no SPDY. Wireshark build info below.</p><pre><code>Wireshark SSL debug log

ssl_association_remove removing TCP 8095 - http handle 0x10a22a660
Private key imported: KeyID 85:8c:ff:ee:74:26:7b:8f:00:f2:39:d0:3e:35:f7:40:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;10.0.0.25&#39; (10.0.0.25) port &#39;8095&#39; filename &#39;/Users/tommcd/lsws/server.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /Users/tommcd/lsws/server.key successfully loaded.
association_add TCP port 8095 protocol http handle 0x10a22a660

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0x10cba16e0 size 712
association_find: TCP port 49623 found 0x0
packet_from_server: is from server - FALSE
  conversation = 0x10ad01058, ssl_session = 0x10cba16e0
  record: offset = 0, reported_length_remaining = 177
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 172, ssl state 0x00
association_find: TCP port 49623 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 168 bytes, remaining 177 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.0.0.25:8095
ssl_find_private_key: testing 1 keys
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #6 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x10ad01058, ssl_session = 0x10cba16e0
  record: offset = 0, reported_length_remaining = 877
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 93, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 89 bytes, remaining 98 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0xC027 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
  record: offset = 98, reported_length_remaining = 779
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 555, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available</code></pre><p>Wireshark build info</p><pre><code>2014-09-11 16:52:00.660 defaults[75025:507] 
The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist
wireshark 1.12.1rc0-74-g3131847 (v1.12.0rc0-74-g3131847 from master-1.12)

Copyright 1998-2014 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GTK+ 2.24.17, with Cairo 1.10.2, with Pango 1.30.1, with
GLib 2.36.0, with libpcap, with libz 1.2.3, without POSIX capabilities, with SMI
0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS
2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP, with PortAudio
V19-devel (built Jul 16 2013 19:05:52), with AirPcap.

Running on Mac OS X 10.9.4, build 13E28 (Darwin 13.3.0), with locale .UTF-8,
with libpcap version 1.3.0 - Apple version 41, with libz 1.2.5, GnuTLS 2.12.19,
Gcrypt 1.5.0, without AirPcap.
       Intel(R) Core(TM) i5-2500S CPU @ 2.70GHz

Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build
2336.9.00).</code></pre></div><div id="question-tags" class="tags-container tags">ssl decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/79b965f8bf193f4c5f6f1da27da80c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DiabolicalTMcD&#39;s gravatar image" /><p>DiabolicalTMcD<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DiabolicalTMcD has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '14, 13:52</p></div></div><div id="comments-container-36212" class="comments-container"></div><div id="comment-tools-36212" class="comment-tools"></div><div class="clear"></div><div id="comment-36212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

