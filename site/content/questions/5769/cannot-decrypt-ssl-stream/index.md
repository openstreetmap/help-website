+++
type = "question"
title = "Cannot decrypt SSL stream"
description = '''Using Wireshark 1.6.1 on Win 7 x64. I am trying to get the decrypted stream from a client/server interaction (the &quot;server&quot; is actually IIS/SQL Server 2005), but I am not having success with the decryption. Following is the SSL Debug File - thanks for any assistance.  Private key imported: KeyID 1c:5...'''
date = "2011-08-19T13:49:00Z"
lastmod = "2011-08-19T14:26:00Z"
weight = 5769
keywords = [ "ssl", "wireshark" ]
aliases = [ "/questions/5769" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot decrypt SSL stream](/questions/5769/cannot-decrypt-ssl-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5769-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark 1.6.1 on Win 7 x64.</p><p>I am trying to get the decrypted stream from a client/server interaction (the "server" is actually IIS/SQL Server 2005), but I am not having success with the decryption. Following is the SSL Debug File - thanks for any assistance.</p><hr /><pre><code>Private key imported: KeyID 1c:52:0e:11:b5:11:20:19:0d:1d:66:d6:85:7a:e4:12:...
ssl_init IPv4 addr &#39;127.0.0.1&#39; (127.0.0.1) port &#39;444&#39; filename &#39;c:\ws088.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file c:\ws088.pem successfully loaded.
association_add TCP port 444 protocol tcp handle 00000000050F98C0

dissect_ssl enter frame #7 (first time)
ssl_session_init: initializing ptr 00000000066F2460 size 680
  conversation = 00000000066F2200, ssl_session = 00000000066F2460
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record found version 0x0301 -&gt; state 0x10
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 64, ssl state 0x10
association_find: TCP port 443 found 0000000005836E30
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #10 (first time)
  conversation = 00000000066F2200, ssl_session = 00000000066F2460
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 64, ssl state 0x10
association_find: TCP port 61659 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #11 (first time)
  conversation = 00000000066F2200, ssl_session = 00000000066F2460
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 61659 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #10 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #11 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #17 (first time)
ssl_session_init: initializing ptr 00000000066F3440 size 680
  conversation = 00000000066F31E0, ssl_session = 00000000066F3440
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record found version 0x0301 -&gt; state 0x10
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 608, ssl state 0x10
association_find: TCP port 50284 found 0000000000000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (first time)
  conversation = 00000000066F31E0, ssl_session = 00000000066F3440
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 2784, ssl state 0x10
association_find: TCP port 444 found 0000000005B709C0
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #7 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #7 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #10 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #11 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #7 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #7 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #10 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #11 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #7 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #10 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #11 (already visited)
  conversation = 00000000066F2200, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23
association_find: TCP port 61659 found 0000000000000000
association_find: TCP port 443 found 0000000005836E30

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #47 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 2789
dissect_ssl3_record: content_type 23
association_find: TCP port 444 found 0000000005B709C0

dissect_ssl enter frame #17 (already visited)
  conversation = 00000000066F31E0, ssl_session = 0000000000000000
  record: offset = 0, reported_length_remaining = 613
dissect_ssl3_record: content_type 23
association_find: TCP port 50284 found 0000000000000000
association_find: TCP port 444 found 0000000005B709C0</code></pre><hr /></div><div id="question-tags" class="tags-container tags">ssl wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '11, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/1dc0914cda671a1f86527ad799b1ff3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cgtyoder&#39;s gravatar image" /><p>cgtyoder<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cgtyoder has no accepted answers">0%</span></p></div></div><div id="comments-container-5769" class="comments-container"><span id="5770"></span><div id="comment-5770" class="comment"><div id="post-5770-score" class="comment-score"></div><div class="comment-text"><p>Forgot to say - I am running Wireshark on the "server;" the SSL port is 444. The SSL cert is actually not valid (it is expired) - would that make a difference? Also, does the SSL Decrypt Profile IP address need to match the cert or anything like that?</p></div><div id="comment-5770-info" class="comment-info"><span class="comment-age">(19 Aug '11, 14:10)</span> cgtyoder</div></div></div><div id="comment-tools-5769" class="comment-tools"></div><div class="clear"></div><div id="comment-5769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5772"></span>

<div id="answer-container-5772" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5772-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SSL debug log shows that you started to capture while the SSL handshake had already taken place. To be able to decrypt SSL traffic, you need to capture the full SSL handshake. The best way to accomplish this is to start capturing <em>before</em> you start your browser (close the browser completely before starting the capture).</p><p>Have a look at slides of the presentation I gave at Sharkfest'09 about <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">troubleshooting SSL with Wireshark</a> (or <a href="http://www.lovemytool.com/blog/2009/06/sake_blok_11.html">watch the video at LoveMyTool</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '11, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5772" class="comments-container"><span id="5775"></span><div id="comment-5775" class="comment"><div id="post-5775-score" class="comment-score"></div><div class="comment-text"><p>I actually am not calling this from a browser, but from soapUI, a SOAP debugging tool. I will try to restart that (on Monday at the office) and see if that makes a difference.</p></div><div id="comment-5775-info" class="comment-info"><span class="comment-age">(19 Aug '11, 17:35)</span> cgtyoder</div></div><span id="5804"></span><div id="comment-5804" class="comment"><div id="post-5804-score" class="comment-score">1</div><div class="comment-text"><p>That did it - I just had to trace from the start of the soapUI connection. Thanks much for the assistance.</p></div><div id="comment-5804-info" class="comment-info"><span class="comment-age">(22 Aug '11, 06:50)</span> cgtyoder</div></div></div><div id="comment-tools-5772" class="comment-tools"></div><div class="clear"></div><div id="comment-5772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

