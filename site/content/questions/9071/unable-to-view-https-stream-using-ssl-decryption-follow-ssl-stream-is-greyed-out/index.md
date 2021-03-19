+++
type = "question"
title = "Unable to view HTTPS stream using SSL decryption (&quot;Follow SSL Stream&quot; is greyed out.)"
description = '''I&#x27;m trying to use wireshark to debug a REST application running over HTTP with SSL.  I&#x27;m using Version 1.6.5 (SVN Rev 40429 from /trunk-1.6)running on Windows 7. I&#x27;ve installed the RSA key in Wireshark using Edit/Prefernces/Protocols/SSL and installing my server&#x27;s unencrypted private key inthe &quot;RSA ...'''
date = "2012-02-16T10:04:00Z"
lastmod = "2012-02-17T09:13:00Z"
weight = 9071
keywords = [ "ssl", "decrypt", "https" ]
aliases = [ "/questions/9071" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to view HTTPS stream using SSL decryption ("Follow SSL Stream" is greyed out.)](/questions/9071/unable-to-view-https-stream-using-ssl-decryption-follow-ssl-stream-is-greyed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9071-score" class="post-score" title="current number of votes">1</div><span id="post-9071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to use wireshark to debug a REST application running over HTTP with SSL.<br />
</p><p>I'm using Version 1.6.5 (SVN Rev 40429 from /trunk-1.6)running on Windows 7.</p><p>I've installed the RSA key in Wireshark using Edit/Prefernces/Protocols/SSL and installing my server's unencrypted private key inthe "RSA keys list". It's installed with the IP address of the server (in this case I'm running both server and client on the local machine, so it's the same as the address of the client), the port (which happens to be 8181), protocol=http (get an error if I try to put in https, so I assume http is the correct value here), and the location of my key file.<br />
</p><p>I also went to Edit/Preferences/Protocols/HTTP and addes 8181 after 443 in list of SSL ports for HTTP.</p><p>I also configured an ssl debug file location.</p><p>I captured some traffic using RawCap.exe and have it in a packet capture file. (If I try to capture directly using Wireshark it doesn't work, even though I'm using my machine's FQDN in the app, which is translating to the machine's address, not the loopback address, the traffic is perhaps still being sent via loopback, which I've read Wireshark can't sniff on Windows.)</p><p>When I open the packet capture file in Wireshark, I see some encouraging looking stuff in the ssl debug file (though I don't really know what it all means). However, what I really want to do is follow the TCP stream, and see the HTTP text that was sent back and forth. I can't seem to do this. The "Follow SSL Stream" option is greyed out. If I select "Follow TCP Stream" I see garbled data, though with some legible text scattered in.<br />
</p><p>Any suggestions?</p><p>Thanks,</p><p>Duncan</p><h2 id="ssldebug-file-contents-with-hex-decodes-snipped-out">ssldebug file contents (with hex decodes snipped out):</h2><pre><code>Private key imported: KeyID 13:3e:82:de:30:23:69:10:8c:6e:7d:4e:29:17:18:7f:...
ssl_init IPv4 addr &#39;192.168.1.6&#39; (192.168.1.6) port &#39;8181&#39; filename &#39;C:\Users\duncant\Documents\Keys and Certs\duncanpc-privkey.key&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\Users\duncant\Documents\Keys and Certs\duncanpc-privkey.key successfully loaded.
association_add TCP port 8181 protocol http handle 0000000004554940

dissect_ssl enter frame #32 (first time)
ssl_session_init: initializing ptr 0000000005F438C0 size 680
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 103
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.1.6:8181
client random len: 32 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #34 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 1432
  need_desegmentation: offset = 0, reported_length_remaining = 1432

dissect_ssl enter frame #35 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 2864
  need_desegmentation: offset = 0, reported_length_remaining = 2864

dissect_ssl enter frame #37 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 4296
  need_desegmentation: offset = 0, reported_length_remaining = 4296

dissect_ssl enter frame #38 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 5728
  need_desegmentation: offset = 0, reported_length_remaining = 5728

dissect_ssl enter frame #39 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 7160
  need_desegmentation: offset = 0, reported_length_remaining = 7160

dissect_ssl enter frame #40 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 8592
  need_desegmentation: offset = 0, reported_length_remaining = 8592

dissect_ssl enter frame #43 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 10024
  need_desegmentation: offset = 0, reported_length_remaining = 10024

dissect_ssl enter frame #44 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 11456
  need_desegmentation: offset = 0, reported_length_remaining = 11456

dissect_ssl enter frame #45 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 11894
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 11889, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 11894 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 1425 bytes, remaining 11894 
dissect_ssl3_handshake iteration 0 type 13 offset 1515 length 10371 bytes, remaining 11894 
dissect_ssl3_handshake iteration 0 type 14 offset 11890 length 0 bytes, remaining 11894

dissect_ssl enter frame #48 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 269, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 274 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 258 bytes, remaining 274 
pre master encrypted[256]:
&lt;SNIP&gt;
ssl_decrypt_pre_master_secret:RSA_private_decrypt
pcry_private_decrypt: stripping 207 bytes, decr_len 255
decrypted_unstrip_pre_master[255]:
&lt;SNIP&gt;
pre master secret[48]:
&lt;SNIP&gt;
ssl_generate_keyring_material:PRF(pre_master_secret)
pre master secret[48]:
&lt;SNIP&gt;
client random[32]:
&lt;SNIP&gt;
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
&lt;SNIP&gt;
tls_hash: hash seed[77]:
&lt;SNIP&gt;
hash out[48]:
&lt;SNIP&gt;
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
&lt;SNIP&gt;
tls_hash: hash seed[77]:
&lt;SNIP&gt;
hash out[48]:
&lt;SNIP&gt;
PRF out[48]:
&lt;SNIP&gt;
master secret[48]:
&lt;SNIP&gt;
ssl_generate_keyring_material sess key generation
tls_prf: tls_hash(md5 secret_len 24 seed_len 77 )
tls_hash: hash secret[24]:
&lt;SNIP&gt;
tls_hash: hash seed[77]:
&lt;SNIP&gt;
hash out[64]:
&lt;SNIP&gt;
tls_prf: tls_hash(sha)
tls_hash: hash secret[24]:
&lt;SNIP&gt;
tls_hash: hash seed[77]:
&lt;SNIP&gt;
hash out[64]:
&lt;SNIP&gt;
PRF out[64]:
&lt;SNIP&gt;
key expansion[64]:
&lt;SNIP&gt;
Client MAC key[16]:
&lt;SNIP&gt;
Server MAC key[16]:
&lt;SNIP&gt;
Client Write key[16]:
&lt;SNIP&gt;
Server Write key[16]:
&lt;SNIP&gt;
Client Write IV[8]:
&lt;SNIP&gt;
Server Write IV[8]:
&lt;SNIP&gt;
ssl_generate_keyring_material ssl_create_decoder(client)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material ssl_create_decoder(server)
ssl_create_decoder CIPHER: ARCFOUR
decoder initialized (digest len 16)
ssl_generate_keyring_material: client seq 0, server seq 0
ssl_save_session stored session id[32]:
&lt;SNIP&gt;
ssl_save_session stored master secret[48]:
&lt;SNIP&gt;
dissect_ssl3_handshake session keys successfully generated

dissect_ssl enter frame #52 (first time)
  conversation = 0000000005F43410, ssl_session = 0000000005F438C0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT

dissect_ssl enter frame #32 (already visited)
  conversation = 0000000005F43410, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 103

dissect_ssl enter frame #45 (already visited)
  conversation = 0000000005F43410, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 11894
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 77 bytes, remaining 11894 
dissect_ssl3_handshake iteration 0 type 11 offset 86 length 1425 bytes, remaining 11894 
dissect_ssl3_handshake iteration 0 type 13 offset 1515 length 10371 bytes, remaining 11894 
dissect_ssl3_handshake iteration 0 type 14 offset 11890 length 0 bytes, remaining 11894

dissect_ssl enter frame #48 (already visited)
  conversation = 0000000005F43410, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 274
dissect_ssl3_record: content_type 22
dissect_ssl3_handshake iteration 1 type 11 offset 5 length 3 bytes, remaining 274 
dissect_ssl3_handshake iteration 0 type 16 offset 12 length 258 bytes, remaining 274</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '12, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/415c9ce08f8e171ada8743d133cabf0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="duncant&#39;s gravatar image" /><p><span>duncant</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="duncant has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '12, 10:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></br></p></div></div><div id="comments-container-9071" class="comments-container"><span id="9098"></span><div id="comment-9098" class="comment"><div id="post-9098-score" class="comment-score"></div><div class="comment-text"><p>By the way, I should mention that I'm doing "mutual authentication", also known as "client authentication". I would assume that this wouldn't affect the SSL decode, but who knows...</p></div><div id="comment-9098-info" class="comment-info"><span class="comment-age">(17 Feb '12, 09:13)</span> <span class="comment-user userinfo">duncant</span></div></div></div><div id="comment-tools-9071" class="comment-tools"></div><div class="clear"></div><div id="comment-9071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

