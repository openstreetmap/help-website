+++
type = "question"
title = "SSL decrypting with master secret but no session id"
description = '''RSA Session-ID:xxxx Master-Key:yyyy  Is one of the formats for decrypting SSL traffic if I have the master secret. But some sites like google don&#x27;t send a Session-ID (Session Id Length 0). The other format for RSA based key exchange with the encrypted pre master key and pre master key I can&#x27;t use be...'''
date = "2013-08-27T02:32:00Z"
lastmod = "2013-12-22T16:00:00Z"
weight = 24086
keywords = [ "session-id", "decryption", "master-key", "ssl" ]
aliases = [ "/questions/24086" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decrypting with master secret but no session id](/questions/24086/ssl-decrypting-with-master-secret-but-no-session-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24086-score" class="post-score" title="current number of votes">0</div><span id="post-24086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>RSA Session-ID:xxxx Master-Key:yyyy</code></pre><p>Is one of the formats for decrypting SSL traffic if I have the master secret. But some sites like google don't send a Session-ID (Session Id Length 0). The other format for RSA based key exchange with the encrypted pre master key and pre master key I can't use because I don't have access to the pre master keys. As far as I understand trunk-1.10/epan/dissectors/packet-ssl-utils.c:</p><pre><code>ssl_keylog_parse_session_id(...
if (ssl_session-&gt;session_id.data_len == 0)
    return FALSE;</code></pre><p>as soon as the session id is 0, the format RSA Session-ID: Master-Key: isn't usable. Could someone confirm that or may be have an alternative solution (without modifying Wireshark)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session-id" rel="tag" title="see questions tagged &#39;session-id&#39;">session-id</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-master-key" rel="tag" title="see questions tagged &#39;master-key&#39;">master-key</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/a4b7b8b35822715dfe0b431c6fce987f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack%20Norris&#39;s gravatar image" /><p><span>Jack Norris</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack Norris has one accepted answer">100%</span></p></div></div><div id="comments-container-24086" class="comments-container"></div><div id="comment-tools-24086" class="comment-tools"></div><div class="clear"></div><div id="comment-24086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24140"></span>

<div id="answer-container-24140" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24140-score" class="post-score" title="current number of votes">1</div><span id="post-24140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jack Norris has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Simple solution for that problem, reduce the possible cipher suites to the suites supported by wireshark. You find the supported ones in <code>epan/dissectors/packet-ssl-utils.c</code> under <code>static SslCipherSuite cipher_suites[]={</code></p><p>For example Qt (OpenSSL) :</p><pre><code>wiresharkSupportedCipherSuites = [&quot;EXP-RC4-MD5&quot;, &quot;RC4-MD5&quot;, &quot;RC4-SHA&quot;, &quot;EXP-RC2-CBC-MD5&quot;, &quot;IDEA-CBC-SHA&quot;, &quot;EXP-DES-CBC-SHA&quot;, &quot;DES-CBC3-SHA&quot;, &quot;AES128-SHA&quot;, &quot;DHE-DSS-AES128-SHA&quot;, &quot;DHE-RSA-AES128-SHA&quot;, &quot;AES256-SHA&quot;, &quot;DHE-DSS-AES256-SHA&quot;, &quot;DHE-RSA-AES256-SHA&quot;, &quot;AES128-SHA256&quot;, &quot;AES256-SHA256&quot;, &quot;DHE-DSS-AES128-SHA256&quot;, &quot;DHE-RSA-AES128-SHA256&quot;, &quot;DHE-DSS-AES256-SHA256&quot;, &quot;DHE-RSA-AES256-SHA256&quot;]</code></pre><p>The notation is a bit strange in Qt, took some time to compare the cipher suite names.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/a4b7b8b35822715dfe0b431c6fce987f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack%20Norris&#39;s gravatar image" /><p><span>Jack Norris</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack Norris has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '13, 08:22</strong> </span></p></div></div><div id="comments-container-24140" class="comments-container"></div><div id="comment-tools-24140" class="comment-tools"></div><div class="clear"></div><div id="comment-24140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24090"></span>

<div id="answer-container-24090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24090-score" class="post-score" title="current number of votes">1</div><span id="post-24090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The SSL dissector will try 3 formats:</p><pre><code>    if (ssl_keylog_parse_session_id(line, ssl_session) ||
        ssl_keylog_parse_rsa_premaster(line, ssl_session,
                                       encrypted_pre_master) ||
        ssl_keylog_parse_client_random(line, ssl_session)) {
        ret = 1;
        break;</code></pre><p>The formats are:</p><pre><code>RSA Session-ID:&lt;hex session id&gt; Master-Key:&lt;hex TLS master secret&gt;
RSA &lt;hex, 8-bytes of encrypted pre-master secret&gt; &lt;hex pre-master secret&gt;
CLIENT_RANDOM &lt;hex client_random&gt; &lt;hex TLS master secret&gt;</code></pre><p>So if you can index your master secret with the client random for the session, you can still use the out-of-box functionality of wireshark 1.10. If not, a change to the code will be necessary.</p><p>Out-of-curiosity: Which application/library are you using to log the master-secret?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24090" class="comments-container"><span id="24092"></span><div id="comment-24092" class="comment"><div id="post-24092-score" class="comment-score"></div><div class="comment-text"><p>I tried the CLIENT_RANDOM but it doesn't work for me (for RSA based key exchange).</p><p>I use QtWebkit with a modified Qt library. It's easy to modify and recompile Qt if you use the source package of your distribution. In qsslsocket_openssl.cpp (Qt source package) you find some commented lines for writing a file with the master secrets.</p></div><div id="comment-24092-info" class="comment-info"><span class="comment-age">(27 Aug '13, 04:10)</span> <span class="comment-user userinfo">Jack Norris</span></div></div><span id="24094"></span><div id="comment-24094" class="comment"><div id="post-24094-score" class="comment-score"></div><div class="comment-text"><p>Could that be the problem that CLIENT_RANDOM doesn't work:</p><pre><code>dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x9C</code></pre><p>I checked the packet-ssl-utils.c file and cipher suite 0x9C (<code>TLS_RSA_WITH_AES_128_GCM_SHA256</code>) should be present in Wireshark</p><pre><code>dissect_ssl enter frame #18 (first time)
  conversation = 0x7f825d2d04b0, ssl_session = 0x7f825d2d0ac0
  record: offset = 0, reported_length_remaining = 1418
dissect_ssl3_record found version 0x0303(TLS 1.2) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 62, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 58 bytes, remaining 67 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session
trying to use SSL keylog in /home/jim/Projects/Browser/pcaps/ssl-master-keys
  checking keylog line: RSA Session-ID:95DCDB01178B16AED12D269495048F60625A16904868D38DEDF0F751576A7B5B Master-Key:B5044BA33AD5BF283D1B04483480812B57173DFDD40757C729B33E2F7B796F12529A3E9A6B10C8C724904FAA3B3A5D4E
    line does not match
  checking keylog line: CLIENT_RANDOM 521C962164B2D2DB7349E44B80F49AF27AAD2CF84DC3369DC1C08C8C1CEB35D6 B5044BA33AD5BF283D1B04483480812B57173DFDD40757C729B33E2F7B796F12529A3E9A6B10C8C724904FAA3B3A5D4E
found master secret in key log
  cannot find master secret in keylog file either
dissect_ssl3_hnd_srv_hello can&#39;t find cipher suite 0x9C
  record: offset = 67, reported_length_remaining = 1351
  need_desegmentation: offset = 67, reported_length_remaining = 1351</code></pre></div><div id="comment-24094-info" class="comment-info"><span class="comment-age">(27 Aug '13, 05:49)</span> <span class="comment-user userinfo">Jack Norris</span></div></div><span id="28128"></span><div id="comment-28128" class="comment"><div id="post-28128-score" class="comment-score"></div><div class="comment-text"><p><span>@Jack Norris</span> The GCM cipher suite is supported in the development version (1.11.0 or newer).</p></div><div id="comment-28128-info" class="comment-info"><span class="comment-age">(15 Dec '13, 12:09)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="28330"></span><div id="comment-28330" class="comment"><div id="post-28330-score" class="comment-score"></div><div class="comment-text"><p><span>@Lekensteyn</span> This is great news! Thank you for this information!</p></div><div id="comment-28330-info" class="comment-info"><span class="comment-age">(22 Dec '13, 16:00)</span> <span class="comment-user userinfo">Jack Norris</span></div></div></div><div id="comment-tools-24090" class="comment-tools"></div><div class="clear"></div><div id="comment-24090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

