+++
type = "question"
title = "Why isn&#x27;t Application Data being decoded in SSL transactions?"
description = '''I have an SSL trace on CloudShark below my question. My question is why isn&#x27;t the &quot;Application Data&quot; being decrypted in the trace? How can I get it decoded or can I? I keep seeing this in the debug  dissect_ssl enter frame #86 (first time) conversation = 04C66A1C, ssl_session = 04C675D0 record: offs...'''
date = "2012-09-14T20:09:00Z"
lastmod = "2012-09-17T10:09:00Z"
weight = 14286
keywords = [ "ssl", "data", "application" ]
aliases = [ "/questions/14286" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why isn't Application Data being decoded in SSL transactions?](/questions/14286/why-isnt-application-data-being-decoded-in-ssl-transactions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14286-score" class="post-score" title="current number of votes">0</div><span id="post-14286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an SSL trace on CloudShark below my question. My question is why isn't the "Application Data" being decrypted in the trace? How can I get it decoded or can I? I keep seeing this in the debug</p><pre><code>dissect_ssl enter frame #86 (first time)
conversation = 04C66A1C, ssl_session = 04C675D0
record: offset = 0, reported_length_remaining = 2480
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x11
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 2475, ssl state 0x11
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 2 offset 5 length 70 bytes, remaining 2480 
dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
dissect_ssl3_hnd_srv_hello found CIPHER 0x0004 -&gt; state 0x17
dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material
dissect_ssl3_handshake iteration 0 type 11 offset 79 length 2393 bytes, remaining 2480 
dissect_ssl3_handshake iteration 0 type 14 offset 2476 length 0 bytes, remaining 2480

dissect_ssl enter frame #94 (first time)
conversation = 04C66A1C, ssl_session = 04C675D0
record: offset = 0, reported_length_remaining = 267
dissect_ssl3_record: content_type 22 Handshake
decrypt_ssl3_record: app_data len 262, ssl state 0x17
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
dissect_ssl3_handshake iteration 1 type 16 offset 5 length 258 bytes, remaining 267 
pre master encrypted[256]:</code></pre><p>Looking at the debug file, the certificate gets loaded successfully. There are examples on frames 56 and 169. Any help would be appreciated.</p><p><a href="http://cloudshark.org/captures/77ff76bbe6e0?filter=tcp.port%20%3D%3D%20443">http://cloudshark.org/captures/77ff76bbe6e0?filter=tcp.port%20%3D%3D%20443</a></p><p>Terry</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/90ace4ca58ca53e9c64e6713d5950cf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tcoder&#39;s gravatar image" /><p><span>tcoder</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tcoder has no accepted answers">0%</span></p></div></div><div id="comments-container-14286" class="comments-container"><span id="14296"></span><div id="comment-14296" class="comment"><div id="post-14296-score" class="comment-score"></div><div class="comment-text"><p>What I have is something unusual. I have server A (HTTPS) going to client B (HTTPS). Server C (raw data) goes to client B (raw data). Server A is an authorization server. Server C is a data offload server.</p><p>Both servers are on the same PC. It was setup as a simple trace; there was no merging of files. (I wrote the server code.)</p><p>Client B gets through to both servers via a dialup modem router. Therefore the frame rate should be slow.</p><p>Why do I get "decrypt_ssl3_record: no decoder available"?</p><p>Thanks for your help.</p></div><div id="comment-14296-info" class="comment-info"><span class="comment-age">(15 Sep '12, 07:25)</span> <span class="comment-user userinfo">tcoder</span></div></div><span id="14297"></span><div id="comment-14297" class="comment"><div id="post-14297-score" class="comment-score"></div><div class="comment-text"><p>I believe you get "No decoder available" because the session has not entered the encrypted stage yet at that point in time (frame #86 seems to be the ServerHello message)</p></div><div id="comment-14297-info" class="comment-info"><span class="comment-age">(15 Sep '12, 15:21)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-14286" class="comment-tools"></div><div class="clear"></div><div id="comment-14286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14290"></span>

<div id="answer-container-14290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14290-score" class="post-score" title="current number of votes">1</div><span id="post-14290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Somehow there are two identical sessions in the trace file, the SSL dissector is not really good at handling that. You might want to filter out one complete stream and save that to a separate file. You can also use "edit -&gt; ignore packet" to ignore the frames in the secondary TCP session.</p><p>How was the trace file made? I don not see any vlan tags and the mac-addresses of these sessions are the same (as are the IP addresses, IP ID's, TCP ports and TCP sequence numbers). Did you merge the same pcap file twice into a new pcap file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '12, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14290" class="comments-container"><span id="14306"></span><div id="comment-14306" class="comment"><div id="post-14306-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Tracing only one interface helped.</p></div><div id="comment-14306-info" class="comment-info"><span class="comment-age">(16 Sep '12, 12:02)</span> <span class="comment-user userinfo">tcoder</span></div></div><span id="14326"></span><div id="comment-14326" class="comment"><div id="post-14326-score" class="comment-score"></div><div class="comment-text"><p>The fix was as you said. Reduce the traffic and trace on only one interface. Thanks.</p></div><div id="comment-14326-info" class="comment-info"><span class="comment-age">(17 Sep '12, 10:09)</span> <span class="comment-user userinfo">tcoder</span></div></div></div><div id="comment-tools-14290" class="comment-tools"></div><div class="clear"></div><div id="comment-14290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

