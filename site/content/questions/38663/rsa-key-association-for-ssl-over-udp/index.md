+++
type = "question"
title = "RSA Key association for SSL over UDP"
description = '''I&#x27;ve written my own dissector (in lua) to dissect USB URB packets, remove a header, and send the remaining packet data on to the ssl dissector like so: local ssl = Dissector.get(&#x27;ssl&#x27;)  local newbuf = tvbuf:range(42, pktlen-42):tvb()  ssl:call(newbuf, pktinfo, root) Works all well and good ^.^ but w...'''
date = "2014-12-22T11:53:00Z"
lastmod = "2014-12-22T16:47:00Z"
weight = 38663
keywords = [ "ssl", "sub-dissector", "ssl_decrypt" ]
aliases = [ "/questions/38663" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RSA Key association for SSL over UDP](/questions/38663/rsa-key-association-for-ssl-over-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written my own dissector (in lua) to dissect USB URB packets, remove a header, and send the remaining packet data on to the ssl dissector like so:</p><p><code>local ssl = Dissector.get('ssl')   local newbuf = tvbuf:range(42, pktlen-42):tvb()   ssl:call(newbuf, pktinfo, root)</code></p><p>Works all well and good ^.^ but when I add RSA keys, they seem to be associated with TCP port 0, so I cannot get them to be recognized by my packet stream which logs them as "UDP port -1"</p><p>ssl-debug.log excerpts:</p><p><code>ssl_association_remove removing TCP 0 - data handle 0x1f471b0 Private key imported: KeyID 4c:2a:fb:42:99:02:85:8d:24:87:ff:f7:67:97:e6:6b:... ssl_load_key: swapping p and q parameters and recomputing u ssl_init IPv4 addr '0.0.0.0' (0.0.0.0) port '0' filename '/home/jonah/Workspace/mobdev/iRealD/root_private_key.pem' password(only for p12 file) '' ssl_init private key file /home/jonah/Workspace/mobdev/iRealD/root_private_key.pem successfully loaded. association_add TCP port 0 protocol data handle 0x1f471b0</code></p><p><code>dissect_ssl enter frame #103 (first time)   conversation = 0x7f0b999dda38, ssl_session = 0x7f0b999ddb30   record: offset = 0, reported_length_remaining = 138 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 133, ssl state 0x00 association_find: UDP port -1 found (nil) packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 1 offset 5 length 129 bytes, remaining 138  packet_from_server: is from server - FALSE ssl_find_private_key server 7.4:4 ssl_find_private_key can't find private key for this server! Try it again with universal port 0 ssl_find_private_key can't find private key for this server (universal port)! Try it again with universal address 0.0.0.0 ssl_find_private_key can't find any private key! dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01</code></p><p><code>dissect_ssl enter frame #105 (first time)   conversation = 0x7f0b999ddf10, ssl_session = 0x7f0b999ddfb0   record: offset = 0, reported_length_remaining = 79 dissect_ssl3_record found version 0x0300 -&gt; state 0x10 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 74, ssl state 0x10 association_find: UDP port 5 found (nil) packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 79  dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x12 dissect_ssl3_hnd_srv_hello found CIPHER 0x0035 -&gt; state 0x16 dissect_ssl3_hnd_srv_hello trying to generate keys ssl_generate_keyring_material not enough data to generate key (0x16 required 0x37 or 0x57) dissect_ssl3_hnd_srv_hello can't generate keyring material</code></p><p><code>dissect_ssl enter frame #106 (first time)   conversation = 0x7f0b999ddf10, ssl_session = 0x7f0b999ddfb0   record: offset = 0, reported_length_remaining = 608 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 580, ssl state 0x16 association_find: UDP port 5 found (nil) packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 11 offset 5 length 576 bytes, remaining 585    record: offset = 585, reported_length_remaining = 23 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 9, ssl state 0x16 association_find: UDP port 5 found (nil) packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 13 offset 590 length 5 bytes, remaining 599    record: offset = 599, reported_length_remaining = 9 dissect_ssl3_record: content_type 22 Handshake decrypt_ssl3_record: app_data len 4, ssl state 0x16 association_find: UDP port 5 found (nil) packet_from_server: is from server - FALSE decrypt_ssl3_record: using client decoder decrypt_ssl3_record: no decoder available dissect_ssl3_handshake iteration 1 type 14 offset 604 length 0 bytes, remaining 608</code></p></div><div id="question-tags" class="tags-container tags">ssl sub-dissector ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/7e7087f7160dbb93badf777a52317f61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TinyTimZamboni&#39;s gravatar image" /><p>TinyTimZamboni<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TinyTimZamboni has no accepted answers">0%</span></p></div></div><div id="comments-container-38663" class="comments-container"></div><div id="comment-tools-38663" class="comment-tools"></div><div class="clear"></div><div id="comment-38663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38670"></span>

<div id="answer-container-38670" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38670-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Non-satisfying answer to my own question:</p><p>RSA key-matching is done on port_type, port, and ip. <code>port_type</code> is hardcoded to <code>PT_TCP</code> whenever the SSL dissector is used and <code>PT_UDP</code> when the dtls dissector is used. When I apply the dtls dissector, it's not able to dissect my packets anymore.</p><p>From Lua, I can't seem to set <code>port_type</code> so I can either rewrite my dissector in C or rebuild Wireshark with <code>tcp = FALSE</code> instead of hardcoded to true.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '14, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/7e7087f7160dbb93badf777a52317f61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TinyTimZamboni&#39;s gravatar image" /><p>TinyTimZamboni<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TinyTimZamboni has no accepted answers">0%</span></p></div></div><div id="comments-container-38670" class="comments-container"></div><div id="comment-tools-38670" class="comment-tools"></div><div class="clear"></div><div id="comment-38670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

