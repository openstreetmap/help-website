+++
type = "question"
title = "Can&#x27;t Decrypt TLSv1 Traffic"
description = '''Hi, I’m using Wireshark v1.8.4. I’m trying to learn about SSL package decryption using wireshark. I have downloaded sample capture file and private key (snakeoil2_070531.tgz) from http://wiki.wireshark.org/SSL and successfully decrypted the package. Then I tried to configure my own Apache Tomcat ser...'''
date = "2013-01-11T16:27:00Z"
lastmod = "2013-01-13T13:20:00Z"
weight = 17630
keywords = [ "tls", "ssl", "decrypt" ]
aliases = [ "/questions/17630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't Decrypt TLSv1 Traffic](/questions/17630/cant-decrypt-tlsv1-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17630-score" class="post-score" title="current number of votes">1</div><span id="post-17630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I’m using Wireshark v1.8.4.</p><p>I’m trying to learn about SSL package decryption using wireshark. I have downloaded sample capture file and private key (snakeoil2_070531.tgz) from <a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a> and successfully decrypted the package.</p><p>Then I tried to configure my own Apache Tomcat server to use SSL. When I capture the traffic to/from my Apache Tomcat server, Wireshark said that its protocol is “TLSv1” instead of “SSLv3”. I have provided the private key to Wireshark SSL protocol preference. But the traffic from my Apache Tomcat isn’t decrypted.</p><p>Here is my Wireshark SSL debug file.</p><pre><code>ssl_association_remove removing TCP 443 - http handle 00000000051D0CE0
Private key imported: KeyID a0:d7:ab:5c:93:66:ed:92:de:1d:ba:77:4f:db:22:e2:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;192.168.168.131&#39; (192.168.168.131) port &#39;443&#39; filename &#39;G:\Reference\ebook\Networking\Wireshark Network Analysis (Supplement Material)\9781893939943_allsupplements\9781893939943_traces\latihan\ssl\privkey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file G:\Reference\ebook\Networking\Wireshark Network Analysis (Supplement Material)\9781893939943_allsupplements\9781893939943_traces\latihan\ssl\privkey.pem successfully loaded.
association_add TCP port 443 protocol http handle 00000000051D0CE0

dissect_ssl enter frame #8 (first time)
ssl_session_init: initializing ptr 0000000006B164B0 size 680
  conversation = 0000000006B15DF8, ssl_session = 0000000006B164B0
  record: offset = 0, reported_length_remaining = 194
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 189, ssl state 0x00
association_find: TCP port 60193 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 185 bytes, remaining 194 
packet_from_server: is from server - FALSE
ssl_find_private_key server 192.168.168.131:443
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #9 (first time)
  conversation = 0000000006B15DF8, ssl_session = 0000000006B164B0
  record: offset = 0, reported_length_remaining = 1130
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 1125, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 1130 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0033 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 615 bytes, remaining 1130 
dissect_ssl3_handshake iteration 0 type 12 offset 698 length 424 bytes, remaining 1130 
dissect_ssl3_handshake iteration 0 type 14 offset 1126 length 0 bytes, remaining 1130 

dissect_ssl enter frame #10 (first time)
  conversation = 0000000006B15DF8, ssl_session = 0000000006B164B0
  record: offset = 0, reported_length_remaining = 166
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 102, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 98 bytes, remaining 107 
ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 107, reported_length_remaining = 59
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - FALSE
ssl_change_cipher CLIENT
  record: offset = 113, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 122 offset 118 length 13182942 bytes, remaining 166 

dissect_ssl enter frame #11 (first time)
  conversation = 0000000006B15DF8, ssl_session = 0000000006B164B0
  record: offset = 0, reported_length_remaining = 6
dissect_ssl3_record: content_type 20 Change Cipher Spec
dissect_ssl3_change_cipher_spec
packet_from_server: is from server - TRUE
ssl_change_cipher SERVER

dissect_ssl enter frame #12 (first time)
  conversation = 0000000006B15DF8, ssl_session = 0000000006B164B0
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 48, ssl state 0x17
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 182 offset 5 length 11033596 bytes, remaining 53 </code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/3684b44b1826047d44ed5321d84a62f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yudi&#39;s gravatar image" /><p><span>Yudi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yudi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '13, 00:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-17630" class="comments-container"></div><div id="comment-tools-17630" class="comment-tools"></div><div class="clear"></div><div id="comment-17630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17631"></span>

<div id="answer-container-17631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17631-score" class="post-score" title="current number of votes">2</div><span id="post-17631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here is the line from your ssl-debug file that tells you what the problem is:</p><pre><code>ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt</code></pre><p>DH key exchanges uses a randomly created public/private keypair to encrypt the session key in the ClientKeyExchange handshake message. As wireshark does not have the randomly created keypair, it can not decrypt the session key and therefor not decrypt the application data.</p><p>A RSA key exchange uses the public key from the certificate to encrypt the session key in the ClientKeyExchange handshake message. So when wireshark is pointed to the correct private key, it is able to decrypt the session key and then use the session key to decrypt the application data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17631" class="comments-container"><span id="17633"></span><div id="comment-17633" class="comment"><div id="post-17633-score" class="comment-score"></div><div class="comment-text"><p>Does DH key exchange refer to "Diffie–Hellman key exchange"? I read from <a href="http://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange">http://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange</a> and <a href="http://en.wikipedia.org/wiki/Key_exchange">http://en.wikipedia.org/wiki/Key_exchange</a> but none of them say about randomly generated public/private key pair.</p><p>Could you give further references about this DH key exchange?</p></div><div id="comment-17633-info" class="comment-info"><span class="comment-age">(11 Jan '13, 17:17)</span> <span class="comment-user userinfo">Yudi</span></div></div><span id="17636"></span><div id="comment-17636" class="comment"><div id="post-17636-score" class="comment-score"></div><div class="comment-text"><p>You are right, it is not a public/private key pair. However, both client and server generate a random value (not known to wireshark) which allows them to generate a shared secret (the session key) instead of exchanging the shared secret by encrypting it with the public key from the certificate (which can be decrypted by using the matching private key).</p></div><div id="comment-17636-info" class="comment-info"><span class="comment-age">(12 Jan '13, 02:14)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17648"></span><div id="comment-17648" class="comment"><div id="post-17648-score" class="comment-score"></div><div class="comment-text"><p>So, is the next question "How do I configure Tomcat to use RSA instead of DH key exchanges" or what? I realize that we're getting into off-topic things here, but it would be good if the answer also answered "Okay, so what next?", rather than just diagnose the problem.</p></div><div id="comment-17648-info" class="comment-info"><span class="comment-age">(12 Jan '13, 22:50)</span> <span class="comment-user userinfo">Warren Young</span></div></div><span id="17650"></span><div id="comment-17650" class="comment"><div id="post-17650-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, is the next question "How do I configure Tomcat to use RSA instead of DH key exchanges" or what?</p></blockquote><p>a very good question for a Tomcat forum, isn't it ;-)</p><p>As you did not tell us how you configured your Tomcat installation it is impossible to tell you what to change. It's either the webserver (Apache, Lighthttpd, ngnix) or Tomcat itself that handles SSL/TLS. Obviously the required changes depend on the setup.</p><p><a href="http://www.giyf.com/">Google is your friend</a>...</p><p>Tomcat: <a href="http://www.sslshopper.com/article-how-to-disable-weak-ciphers-and-ssl-2-in-tomcat.html">http://www.sslshopper.com/article-how-to-disable-weak-ciphers-and-ssl-2-in-tomcat.html</a><br />
Apache: <a href="http://httpd.apache.org/docs/2.2/ssl/ssl_faq.html">http://httpd.apache.org/docs/2.2/ssl/ssl_faq.html</a></p><p>Look for DHE or Diffie Hellman or similar strings.</p></div><div id="comment-17650-info" class="comment-info"><span class="comment-age">(13 Jan '13, 04:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17653"></span><div id="comment-17653" class="comment"><div id="post-17653-score" class="comment-score"></div><div class="comment-text"><p>So, is it absolutely impossible to decrypt DH key exchange using wireshark? Is there any workaround for this? Maybe like manually generate session key and force both client and server to temporarily use the known session key.</p></div><div id="comment-17653-info" class="comment-info"><span class="comment-age">(13 Jan '13, 13:08)</span> <span class="comment-user userinfo">Yudi</span></div></div><span id="17654"></span><div id="comment-17654" class="comment not_top_scorer"><div id="post-17654-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, is it absolutely impossible to decrypt DH key exchange</p></blockquote><p>without knowledge of the session key? Yes, that's why people use DH.</p><blockquote><p>Is there any workaround for this?</p></blockquote><p>As mentioned: Configure the server (webserver) or the client (browser) to refrain from using DH ciphers.</p><p>Another alternative would be to expose the session key within the server or client (<a href="http://ask.wireshark.org/questions/4229/follow-ssl-stream-using-master-key-and-session-id">see openssl client</a>). Unfortunately there is no "standard" way of doing that in the browser or the server. At least I don't know any. So again: <a href="http://www.giyf.com/">google is your friend</a>...</p></div><div id="comment-17654-info" class="comment-info"><span class="comment-age">(13 Jan '13, 13:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17631" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-17631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

