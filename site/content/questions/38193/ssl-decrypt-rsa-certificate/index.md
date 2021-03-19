+++
type = "question"
title = "SSL Decrypt : RSA certificate"
description = '''Please some one help me in creating a RSA key with an example, I tried with steps mentioned in the links : http://wiki.wireshark.org/SSL and https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144 but I am failing at the RSA certification creation level. When tried with sample examples rsasnakeoil2...'''
date = "2014-11-26T21:26:00Z"
lastmod = "2014-11-26T21:26:00Z"
weight = 38193
keywords = [ "rsa", "key" ]
aliases = [ "/questions/38193" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decrypt : RSA certificate](/questions/38193/ssl-decrypt-rsa-certificate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please some one help me in creating a RSA key with an example, I tried with steps mentioned in the links : <a href="http://wiki.wireshark.org/SSL">http://wiki.wireshark.org/SSL</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144</a> but I am failing at the RSA certification creation level.</p><p>When tried with sample examples rsasnakeoil2.cat and adding rsasnakeoil2.key I'm able to decrypt.</p></div><div id="question-tags" class="tags-container tags">rsa key</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 21:26</strong></p><img src="https://secure.gravatar.com/avatar/5da36ed019ea1702fa86f32866e1757e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kalsfru&#39;s gravatar image" /><p>kalsfru<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kalsfru has no accepted answers">0%</span></p></div></div><div id="comments-container-38193" class="comments-container"><span id="38200"></span><div id="comment-38200" class="comment"><div id="post-38200-score" class="comment-score"></div><div class="comment-text"><p>Adding SSL logs for the above question</p><pre><code>ssl_association_remove removing TCP 443 - http handle 0x107e3bd50
Private key imported: KeyID 86:10:02:53:bd:63:6e:c1:99:6f:27:3e:e8:92:a4:50:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;23.207.140.251&#39; (23.207.140.251) port &#39;443&#39; filename &#39;/Users/salam/Desktop/WireShark/cert2/testkey.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /Users/salam/Desktop/WireShark/cert2/testkey.pem successfully loaded.
association_add TCP port 443 protocol http handle 0x107e3bd50

dissect_ssl enter frame #103 (first time)
ssl_session_init: initializing ptr 0x10aa03f50 size 712
association_find: TCP port 993 found 0x10516a980
packet_from_server: is from server - TRUE
  conversation = 0x109201958, ssl_session = 0x10aa03f50
  record: offset = 0, reported_length_remaining = 551
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 546, ssl state 0x10
association_find: TCP port 993 found 0x10516a980
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10516a980

dissect_ssl enter frame #168 (first time)
association_find: TCP port 48215 found 0x0
packet_from_server: is from server - FALSE
  conversation = 0x109201958, ssl_session = 0x10aa03f50
  record: offset = 0, reported_length_remaining = 63
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 58, ssl state 0x10
association_find: TCP port 48215 found 0x0
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 48215 found 0x0
association_find: TCP port 993 found 0x10516a980

dissect_ssl enter frame #219 (first time)
association_find: TCP port 993 found 0x10516a980
packet_from_server: is from server - TRUE
  conversation = 0x109201958, ssl_session = 0x10aa03f50
  record: offset = 0, reported_length_remaining = 1045
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 1040, ssl state 0x10
association_find: TCP port 993 found 0x10516a980
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 993 found 0x10516a980</code></pre></div><div id="comment-38200-info" class="comment-info"><span class="comment-age">(26 Nov '14, 23:45)</span> Sharique</div></div><span id="38267"></span><div id="comment-38267" class="comment"><div id="post-38267-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but I am failing at the RSA certification creation level.</p></blockquote><p>what is the problem?</p></div><div id="comment-38267-info" class="comment-info"><span class="comment-age">(01 Dec '14, 17:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38193" class="comment-tools"></div><div class="clear"></div><div id="comment-38193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

