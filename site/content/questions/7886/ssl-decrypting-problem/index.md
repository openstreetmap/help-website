+++
type = "question"
title = "SSL decrypting problem"
description = '''We set up a test environment to experiment with sniffing related attacks. Basically it is an Apache2 server using https authenticating against an LDAP Active Directory. We have several pcap captures using tcpdump, tshark and wireshark done while users were authenticating. As the authentication invol...'''
date = "2011-12-09T11:51:00Z"
lastmod = "2011-12-09T12:41:00Z"
weight = 7886
keywords = [ "apache", "ssl", "dissector", "https", "decryption" ]
aliases = [ "/questions/7886" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decrypting problem](/questions/7886/ssl-decrypting-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7886-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>We set up a test environment to experiment with sniffing related attacks. Basically it is an Apache2 server using https authenticating against an LDAP Active Directory. We have several pcap captures using tcpdump, tshark and wireshark done while users were authenticating. As the authentication involves the external LDAP server Apache can't use other method than basic plain text, so it should be pretty straightforward for an attacker to capture the data, and use the private key (providing he somehow manage to get it) to obtain the login information and cause havoc.</p><p>Nevertheless, we haven't been able to replicate that scenario with wireshark. Here is part of the debug log:</p><pre><code>ssl_init keys string:
10.0.4.19,443,http,/home/jkane/Temp/snakeoil.key
ssl_init found host entry 10.0.4.19,443,http,/home/jkane/Temp/snakeoil.key
ssl_init addr &#39;10.0.4.19&#39; port &#39;443&#39; filename &#39;/home/jkane/Temp/snakeoil.key&#39; password(only for p12 file) &#39;(null)&#39;
Private key imported: KeyID 2d:71:01:cc:75:09:3d:34:7d:ff:1b:6c:d2:aa:9e:44:...
ssl_init private key file /home/jkane/Temp/snakeoil.key successfully loaded
association_add TCP port 443 protocol http handle 0x7f3c2c1b46d0

dissect_ssl enter frame #146 (first time)
ssl_session_init: initializing ptr 0x7f3c146be980 size 672
  conversation = 0x7f3c146be720, ssl_session = 0x7f3c146be980
  record: offset = 0, reported_length_remaining = 3

dissect_ssl enter frame #151 (first time)
  conversation = 0x7f3c146be720, ssl_session = 0x7f3c146be980
  record: offset = 0, reported_length_remaining = 10

dissect_ssl enter frame #153 (first time)
  conversation = 0x7f3c146be720, ssl_session = 0x7f3c146be980
  record: offset = 0, reported_length_remaining = 4

dissect_ssl enter frame #817 (first time)
ssl_session_init: initializing ptr 0x7f3c146d4df0 size 672
  conversation = 0x7f3c146d4068, ssl_session = 0x7f3c146d4df0
  record: offset = 0, reported_length_remaining = 175
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 170, ssl state 0x00
association_find: TCP port 37364 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 166 bytes, remaining 175 
packet_from_server: is from server - FALSE
ssl_find_private_key server 10.0.4.19:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #818 (first time)
ssl_session_init: initializing ptr 0x7f3c146d5188 size 672
  conversation = 0x7f3c146d4400, ssl_session = 0x7f3c146d5188
  record: offset = 0, reported_length_remaining = 175
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 170, ssl state 0x00
association_find: TCP port 37365 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 166 bytes, remaining 175

dissect_ssl enter frame #823 (first time)
  conversation = 0x7f3c146d4068, ssl_session = 0x7f3c146d4df0
  record: offset = 0, reported_length_remaining = 890
dissect_ssl3_record found version 0x0301 -&gt; state 0x11
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 48, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 44 bytes, remaining 53 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x39
  record: offset = 53, reported_length_remaining = 837
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 421, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 11 offset 58 length 417 bytes, remaining 479 
  record: offset = 479, reported_length_remaining = 411
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 397, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 12 offset 484 length 393 bytes, remaining 881 
  record: offset = 881, reported_length_remaining = 9
dissect_ssl3_record: content_type 22
decrypt_ssl3_record: app_data len 4, ssl state 0x13
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl4_handshake iteration 1 type 14 offset 886 length 0 bytes, remaining 890</code></pre><p>I notice 'no decoder available' in all segments, no idea why. The private key is the one Apache uses by default, and I made sure according to the documentation that the format is the right one http://wiki.wireshark.org/SSL</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">apache ssl dissector https decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '11, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/36830ff9210bdaae9ca9f57b486f79e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacob%20Kane&#39;s gravatar image" /><p>Jacob Kane<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacob Kane has no accepted answers">0%</span></p></div></div><div id="comments-container-7886" class="comments-container"><span id="7889"></span><div id="comment-7889" class="comment"><div id="post-7889-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, you're totally right, we totally overlooked the whole cipher suite thing...</p><p>Great news actually! The current option in the table was changing the plataform to use NTLM as auth scheme.</p></div><div id="comment-7889-info" class="comment-info"><span class="comment-age">(09 Dec '11, 13:31)</span> Jacob Kane</div></div></div><div id="comment-tools-7886" class="comment-tools"></div><div class="clear"></div><div id="comment-7886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7888"></span>

<div id="answer-container-7888" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7888-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SSL session is using a DiffieHellman cipher (0x39 = TLS_DHE_RSA_WITH_AES_256_CBC_SHA). This means the session key is transferred encrypted with a dynamically generated keypair (instead of encrypted with the public key from the certificate). This means you can't decrypt this session with wireshark by providing the private key.</p><p>Have a look at the following for more info:</p><ul><li>This <a href="http://ask.wireshark.org/questions/7728/ssl-decryption">other question</a> at this site</li><li>My presentation on SSL troubleshooting at <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">Sharkfest'09</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '11, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7888" class="comments-container"></div><div id="comment-tools-7888" class="comment-tools"></div><div class="clear"></div><div id="comment-7888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

