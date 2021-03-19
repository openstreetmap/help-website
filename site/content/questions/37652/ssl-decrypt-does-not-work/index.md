+++
type = "question"
title = "ssl decrypt does not work"
description = '''OK, I&#x27;ve read all of the posts I can find for the past two weeks, tried this and that, and I&#x27;m finally down to it. I downloaded the latest versions of Wireshark for Mac and PC (I run both). I ran the sample capture to be sure my Mac and PC implementations are working:   (http://wiki.wireshark.org/Sa...'''
date = "2014-11-07T07:48:00Z"
lastmod = "2014-11-07T10:38:00Z"
weight = 37652
keywords = [ "ssl", "ssl_decrypt" ]
aliases = [ "/questions/37652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ssl decrypt does not work](/questions/37652/ssl-decrypt-does-not-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37652-score" class="post-score" title="current number of votes">0</div><span id="post-37652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, I've read all of the posts I can find for the past two weeks, tried this and that, and I'm finally down to it.</p><p>I downloaded the latest versions of Wireshark for Mac and PC (I run both). I ran the sample capture to be sure my Mac and PC implementations are working: (<a href="http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys).">http://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys).</a> I received a PFX copy of the private key from my security guys (no, I didn't include it here). I ran thru the steps to derive an RSA PEM file: (<a href="http://blogs.technet.com/b/nettracer/archive/2010/10/01/how-to-decrypt-an-ssl-or-tls-session-by-using-wireshark.aspx)">http://blogs.technet.com/b/nettracer/archive/2010/10/01/how-to-decrypt-an-ssl-or-tls-session-by-using-wireshark.aspx)</a> I loaded the file in Preferences &gt; SSL I shut off everything I could think of. I started the trace first. I opened Firefox. I went to iwdmobile.iowa.gov And I got---<em>TLSv1.2</em>---unadulterated, ENCRYPTED TLSv1.2 payloads. Needless to say, not what I'm looking for. I'd like to include a copy of the ssl debug and a jpg of the packet list so you can see the actual order of the packets as I'm seeing them if someone can tell me a place I can load them for viewing. Please, anybody, I'd like to buy a vowel and figure out what stupid thing I'm doing to myself. BTW, if anyone has a definitions page on what the lines in ssl debug are trying to tell me I'd appreciate the reference material. -d</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/e9731598241220667226ea8b75584a70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dribniff&#39;s gravatar image" /><p><span>dribniff</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dribniff has no accepted answers">0%</span></p></div></div><div id="comments-container-37652" class="comments-container"><span id="37654"></span><div id="comment-37654" class="comment"><div id="post-37654-score" class="comment-score"></div><div class="comment-text"><p>Post the SSL debug out put as text straight in your question. Use the "code" button to format it for easier viewing.</p><p>It's possible that the TLS session is using a DH key exchange which makes it more difficult to decrypt, see <a href="http://security.stackexchange.com/questions/35639/decrypting-tls-in-wireshark-when-using-dhe-rsa-ciphersuites/42350#42350">this</a> question from StackExchange. In Firefox, click on the padlock | More Information ... and then in the "Technical Details" section what is the reported connection info.</p><p>Have you also read through the Wireshark Wiki page on SSL, it's <a href="http://wiki.wireshark.org/SSL">here</a>?</p></div><div id="comment-37654-info" class="comment-info"><span class="comment-age">(07 Nov '14, 09:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37652" class="comment-tools"></div><div class="clear"></div><div id="comment-37652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37658"></span>

<div id="answer-container-37658" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37658-score" class="post-score" title="current number of votes">0</div><span id="post-37658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/PacketList.jpg" alt="alt text" /></p><p>As requested:</p><pre><code>   ssl_association_remove removing TCP 443 - http handle 0x10c187820
    Private key imported: KeyID dd:29:74:15:7b:e6:76:47:f5:f0:68:3e:8a:55:61:62:...
    ssl_load_key: swapping p and q parameters and recomputing u
    ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;443&#39; filename &#39;/Users/haguerc/Downloads/snakeoil2_070531/rsasnakeoil2.key&#39; password(only for p12 file) &#39;&#39;
    ssl_init private key file /Users/haguerc/Downloads/snakeoil2_070531/rsasnakeoil2.key successfully loaded.
    association_add TCP port 443 protocol http handle 0x10c187820
    Private key imported: KeyID 8f:7d:52:a1:b2:f3:d0:83:0b:bf:d8:7f:f0:36:54:2f:...
    ssl_load_key: swapping p and q parameters and recomputing u
    ssl_init IPv4 addr &#39;165.206.254.134&#39; (165.206.254.134) port &#39;443&#39; filename &#39;/Volumes/SOLERA/wildcard.rsa.pem&#39; password(only for p12 file) &#39;&#39;
    ssl_init private key file /Volumes/SOLERA/wildcard.rsa.pem successfully loaded.
    association_add TCP port 443 protocol http handle 0x10c187820

    dissect_ssl enter frame #174 (first time)
    ssl_session_init: initializing ptr 0x113210790 size 712
    association_find: TCP port 59674 found 0x0
    packet_from_server: is from server - FALSE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 171
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 166, ssl state 0x00
    association_find: TCP port 59674 found 0x0
    packet_from_server: is from server - FALSE
    decrypt_ssl3_record: using client decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 1 offset 5 length 162 bytes, remaining 171 
    packet_from_server: is from server - FALSE
    ssl_find_private_key server 165.206.254.134:443
    ssl_find_private_key: testing 2 keys
    dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

    dissect_ssl enter frame #176 (first time)
    packet_from_server: is from server - TRUE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 1368
    dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 65, ssl state 0x11
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 2 offset 5 length 61 bytes, remaining 70 
    dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
    ssl_restore_session Cannot restore using an empty SessionID
    trying to use SSL keylog in 
    failed to open SSL keylog
      cannot find master secret in keylog file either
    dissect_ssl3_hnd_srv_hello found CIPHER 0xC014 -&gt; state 0x17
    dissect_ssl3_hnd_srv_hello trying to generate keys
    ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
    dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
      record: offset = 70, reported_length_remaining = 1298
      need_desegmentation: offset = 70, reported_length_remaining = 1298

    dissect_ssl enter frame #179 (first time)
    packet_from_server: is from server - TRUE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 4675
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 4670, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 11 offset 5 length 4666 bytes, remaining 4675

    dissect_ssl enter frame #179 (first time)
    packet_from_server: is from server - TRUE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 347
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 333, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 12 offset 5 length 329 bytes, remaining 338 
      record: offset = 338, reported_length_remaining = 9
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 4, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 14 offset 343 length 0 bytes, remaining 347

    dissect_ssl enter frame #184 (first time)
    packet_from_server: is from server - FALSE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 150
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 70, ssl state 0x17
    packet_from_server: is from server - FALSE
    decrypt_ssl3_record: using client decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 16 offset 5 length 66 bytes, remaining 75 
    ssl_generate_pre_master_secret: found SSL_HND_CLIENT_KEY_EXCHG, state 17
    ssl_decrypt_pre_master_secret session uses DH (17) key exchange, which is impossible to decrypt
    ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
    trying to use SSL keylog in 
    failed to open SSL keylog
    dissect_ssl3_handshake can&#39;t generate pre master secret
      record: offset = 75, reported_length_remaining = 75
    dissect_ssl3_record: content_type 20 Change Cipher Spec
    dissect_ssl3_change_cipher_spec
    packet_from_server: is from server - FALSE
    ssl_change_cipher CLIENT
      record: offset = 81, reported_length_remaining = 69
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 64, ssl state 0x17
    packet_from_server: is from server - FALSE
    decrypt_ssl3_record: using client decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 6 offset 86 length 4641658 bytes, remaining 150

    dissect_ssl enter frame #187 (first time)
    packet_from_server: is from server - TRUE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 298
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 218, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 4 offset 5 length 214 bytes, remaining 223 
    ssl_save_session_ticket stored session_ticket[208]:
    | 5e a8 e9 32 60 3d 43 7d f9 73 d7 d7 7d 4d 0f c2 |^..2`=C}.s..}M..|
    | 32 f4 2c 27 b6 04 fa 5c e1 ae f8 61 e1 d0 2f 0a |2.,&#39;...\...a../.|
    | 73 cf ac 37 30 16 e2 db 73 c5 22 9f 4c b2 fd cb |s..70...s.&quot;.L...|
    | 61 04 4e ac 61 4a 1b 1f 4d 68 ac cf e3 60 0d 03 |a.N.aJ..Mh...`..|
    | f2 17 f0 c8 49 60 39 3d df c4 b7 e0 a3 c3 fb a8 |....I`9=........|
    | cc e0 f3 54 50 4d e1 c4 5a 72 f8 d6 03 80 d2 03 |...TPM..Zr......|
    | d1 c0 d3 82 97 46 69 0d 7c db 5f 5e 9d 55 00 7e |.....Fi.|._^.U.~|
    | c7 a0 ab d0 b4 c3 64 a2 86 8e e2 19 81 aa 26 af |......d.......&amp;.|
    | 0e b4 2b 69 39 59 bf 52 0e f0 69 25 7f c6 f8 64 |..+i9Y.R..i%...d|
    | 1b 58 6d 23 2c 63 d2 8b 4f 6b a2 33 50 dc 6b cb |.Xm#,c..Ok.3P.k.|
    | 2f 6c 62 46 4a 43 5a ad 6d 88 e0 fe 85 71 32 5d |/lbFJCZ.m....q2]|
    | 60 a8 61 d9 2e b8 a3 a7 9b 72 66 b4 80 85 ec c4 |`.a......rf.....|
    | 8f 2f 91 43 8c 16 2c 15 86 df 10 d2 0c 5f 61 cb |./.C..,......_a.|
    ssl_save_session_ticket stored master secret[48]:
    | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
    | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
    | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 |................|
      record: offset = 223, reported_length_remaining = 75
    dissect_ssl3_record: content_type 20 Change Cipher Spec
    dissect_ssl3_change_cipher_spec
    packet_from_server: is from server - TRUE
    ssl_change_cipher SERVER
      record: offset = 229, reported_length_remaining = 69
    dissect_ssl3_record: content_type 22 Handshake
    decrypt_ssl3_record: app_data len 64, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    dissect_ssl3_handshake iteration 1 type 227 offset 234 length 973435 bytes, remaining 298

    dissect_ssl enter frame #200 (first time)
    packet_from_server: is from server - FALSE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 357
    dissect_ssl3_record: content_type 23 Application Data
    decrypt_ssl3_record: app_data len 352, ssl state 0x17
    packet_from_server: is from server - FALSE
    decrypt_ssl3_record: using client decoder
    decrypt_ssl3_record: no decoder available
    association_find: TCP port 59674 found 0x0
    association_find: TCP port 443 found 0x110d43980

    dissect_ssl enter frame #201 (first time)
    packet_from_server: is from server - TRUE
      conversation = 0x10ce04ab0, ssl_session = 0x113210790
      record: offset = 0, reported_length_remaining = 596
    dissect_ssl3_record: content_type 23 Application Data
    decrypt_ssl3_record: app_data len 368, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    association_find: TCP port 443 found 0x110d43980
      record: offset = 373, reported_length_remaining = 223
    dissect_ssl3_record: content_type 23 Application Data
    decrypt_ssl3_record: app_data len 48, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    association_find: TCP port 443 found 0x110d43980
      record: offset = 426, reported_length_remaining = 170
    dissect_ssl3_record: content_type 23 Application Data
    decrypt_ssl3_record: app_data len 112, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    association_find: TCP port 443 found 0x110d43980
      record: offset = 543, reported_length_remaining = 53
    dissect_ssl3_record: content_type 23 Application Data
    decrypt_ssl3_record: app_data len 48, ssl state 0x17
    packet_from_server: is from server - TRUE
    decrypt_ssl3_record: using server decoder
    decrypt_ssl3_record: no decoder available
    association_find: TCP port 443 found 0x110d43980</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/e9731598241220667226ea8b75584a70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dribniff&#39;s gravatar image" /><p><span>dribniff</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dribniff has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37658" class="comments-container"></div><div id="comment-tools-37658" class="comment-tools"></div><div class="clear"></div><div id="comment-37658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

