+++
type = "question"
title = "SSL session not decrypted"
description = '''I am running Wireshark on CentOS. I need to decode SSL traffic. I have the server&#x27;s key. I set the ip address, port, protocol, key in edit&amp;gt;preferences&amp;gt;protocols&amp;gt;SSL&amp;gt;key info. For the key, I use the pem key exported from the application. Then I start my web browser &amp;amp; application. I go...'''
date = "2014-10-31T12:26:00Z"
lastmod = "2014-11-02T10:01:00Z"
weight = 37510
keywords = [ "sll", "not_decrypted" ]
aliases = [ "/questions/37510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL session not decrypted](/questions/37510/ssl-session-not-decrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark on CentOS. I need to decode SSL traffic. I have the server's key. I set the ip address, port, protocol, key in edit&gt;preferences&gt;protocols&gt;SSL&gt;key info. For the key, I use the pem key exported from the application. Then I start my web browser &amp; application. I go through a transaction, stop wireshark capture and look at the frames.</p><p>I see the frames captured. When I click on "Follow SSL Stream", nothing is displayed in dialog window. When I click on "Follow TCP Stream" (on the same frame), I see the at the beginning of the conversation my certificate, from which I extracted the key (with openssl), being exchanged.</p><p>Getting no display on "Follow SSL Stream" indicates to me some key issue. When I look at the "Wireshark SSL Debug Log", I see the below, which I do not completely understand. The first "paragraph" indicates successful PEM key load, but then it encounters problems with key.</p><p>Is there any hint of what is going wrong in log that I am missing? I am as sure as humanly possible that I have the right key... What is meant with "try it again with universal address 0.0.0.0"? What could the reason be for "sslfindprivatekey cannot find private key for this server"?</p><p>Thanks.</p><p>**</p><h2 id="wireshark-ssl-debug-log">Wireshark SSL debug log</h2><p>**</p><pre><code>ssl_association_remove removing TCP 9031 - http handle 0x2dc1770
Private key imported: KeyID 06:74:d4:cb:70:e5:f9:3a:78:b4:2b:6d:87:f7:71:7f:...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;9031&#39; filename &#39;/home/cemil/keytests/14966CD11F8.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file /home/cemil/keytests/14966CD11F8.pem successfully loaded.
association_add TCP port 9031 protocol http handle 0x2dc1770

dissect_ssl enter frame #10 (first time)
ssl_session_init: initializing ptr 0x7fc8c36468a8 size 688
  conversation = 0x7fc8c3645718, ssl_session = 0x7fc8c36468a8
  record: offset = 0, reported_length_remaining = 233
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 228, ssl state 0x00
association_find: TCP port 42803 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 224 bytes, remaining 233 
packet_from_server: is from server - FALSE
ssl_find_private_key server ::1:9031
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #12 (first time)
ssl_session_init: initializing ptr 0x7fc8c3646e18 size 688
  conversation = 0x7fc8c3645cd8, ssl_session = 0x7fc8c3646e18
  record: offset = 0, reported_length_remaining = 233
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 228, ssl state 0x00
association_find: TCP port 42804 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 224 bytes, remaining 233 
packet_from_server: is from server - FALSE
ssl_find_private_key server ::1:9031
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01

dissect_ssl enter frame #14 (first time)
ssl_session_init: initializing ptr 0x7fc8c3647388 size 688
  conversation = 0x7fc8c3646298, ssl_session = 0x7fc8c3647388
  record: offset = 0, reported_length_remaining = 233
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 228, ssl state 0x00
association_find: TCP port 42805 found (nil)
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 1 offset 5 length 224 bytes, remaining 233 
packet_from_server: is from server - FALSE
ssl_find_private_key server ::1:9031
ssl_find_private_key can&#39;t find private key for this server! Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
dissect_ssl3_hnd_hello_common found CLIENT RANDOM -&gt; state 0x01
</code></pre></div><div id="question-tags" class="tags-container tags">sll not_decrypted</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '14, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/8ff0dedad0c32b08f2f65114c9dade91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CemilB&#39;s gravatar image" /><p>CemilB<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CemilB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '14, 09:49</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-37510" class="comments-container"></div><div id="comment-tools-37510" class="comment-tools"></div><div class="clear"></div><div id="comment-37510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37543"></span>

<div id="answer-container-37543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What could the reason be for "sslfindprivatekey cannot find private key for this server"?</p></blockquote><p>I don't know, maybe there is something wrong with your</p><ul><li>capture file</li><li>private key</li><li>ssl preferences (key settings)</li></ul><p>Please try the whole SSL decryption process with the following sample file:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=snakeoil2_070531.tgz">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=snakeoil2_070531.tgz</a></p></blockquote><p>The key is included in the file (use 7-ZIP to open it).</p><p>If that does not work (it work should - I just tested it), there is something wrong with one of the things mentioned above.</p><p>Which one? Impossible to tell, without access to the capture file and the key, or at least a <strong>full</strong> ssl debug file (only the first 20 frames).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '14, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37543" class="comments-container"><span id="37557"></span><div id="comment-37557" class="comment"><div id="post-37557-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt. I just untarred and tried the files you sent, and I could decode fine. At least this tells me that my install is OK. Does this lead you to any other conclusion that would help? Do you have any further suggestion? Best, Cemil</p></div><div id="comment-37557-info" class="comment-info"><span class="comment-age">(03 Nov '14, 09:54)</span> CemilB</div></div><span id="37560"></span><div id="comment-37560" class="comment"><div id="post-37560-score" class="comment-score"></div><div class="comment-text"><p>As I said. Without additional information I can only offer wild guesses, which I'm not going to do ;-)</p></div><div id="comment-37560-info" class="comment-info"><span class="comment-age">(03 Nov '14, 12:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37543" class="comment-tools"></div><div class="clear"></div><div id="comment-37543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

