+++
type = "question"
title = "Is my method of decrypting SSL correct?"
description = '''Hello all and thank you for your time. My main goal is to capture encrypted traffic between my PC and another device which both are on the same network (router). PC is connected via WiFi and the device is connected via hardline (RJ45). Let me quickly explain the scenario: I created a certificate usi...'''
date = "2014-03-28T12:41:00Z"
lastmod = "2014-04-02T14:08:00Z"
weight = 31252
keywords = [ "ssl" ]
aliases = [ "/questions/31252" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is my method of decrypting SSL correct?](/questions/31252/is-my-method-of-decrypting-ssl-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31252-score" class="post-score" title="current number of votes">0</div><span id="post-31252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all and thank you for your time.</p><p>My main goal is to capture encrypted traffic between my PC and another device which both are on the same network (router). PC is connected via WiFi and the device is connected via hardline (RJ45).</p><p>Let me quickly explain the scenario:</p><p>I created a certificate using OpenSSL with RSA. Mailed certificate to get signed. Received signed certificate. Converted the certificate and was prompted with a passkey</p><p>cmd was as follows :</p><blockquote><p>pkcs12 -export -in filename.cer -inkey filename.key -out filename.p12 -name tomcat -CAfile abcd.cer -cname root -chain</p></blockquote><p>This signed certificate (.p12) is then copied into the tomcat directory and being used to encrypt traffic from my PC to some local device.</p><p>I converted the .p12 file to a .pem file using OpenSSL.</p><p>After going into Edit -&gt; Preferences -&gt; Protocol -&gt; SSL, I added the .PEM to the RSA keys list with IP = 0.0.0.0 and port 0. There are two entries, http &amp; tcp.</p><p>This should then decrypt all traffic on ports. This however does not.<br />
</p><p>After setting up a filter to only view packets between the local device and my PC, everything is still decrypted.<br />
</p><p>Below is a sample of my log file with some attempts. The top "paragraph" of the log file says the key and everything was successfully loaded, no error, etc.</p><p>What is it that I am doing wrong? I bolded what I think is a problem.</p><pre><code>dissect_ssl enter frame #19 (first time)
ssl_session_init: initializing ptr 050A7D2C size 592
  conversation = 050A7AEC, ssl_session = 050A7D2C
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record found version 0x0301(TLS 1.0) -&gt; state 0x10
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 65534 found 00000000
packet_from_server: is from server - FALSE
**decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available**
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 65534 found 00000000
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430

dissect_ssl enter frame #19 (already visited)
  conversation = 050A7AEC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430

dissect_ssl enter frame #19 (already visited)
  conversation = 050A7AEC, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 74
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430
  record: offset = 37, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 65534 found 00000000
association_find: TCP port 443 found 04B61430

dissect_ssl enter frame #82 (first time)
  conversation = 050A7AEC, ssl_session = 050A7D2C
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 443 found 04B61430
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04B61430

dissect_ssl enter frame #83 (first time)
  conversation = 050A7AEC, ssl_session = 050A7D2C
  record: offset = 0, reported_length_remaining = 37
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x10
association_find: TCP port 443 found 04B61430
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
decrypt_ssl3_record: no decoder available
association_find: TCP port 443 found 04B61430
</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/0cd8ee806d27d5e65eb9df394382bbd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTaNoob&#39;s gravatar image" /><p><span>JTaNoob</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTaNoob has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '14, 15:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-31252" class="comments-container"></div><div id="comment-tools-31252" class="comment-tools"></div><div class="clear"></div><div id="comment-31252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31258"></span>

<div id="answer-container-31258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31258-score" class="post-score" title="current number of votes">0</div><span id="post-31258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I converted the .p12 file to a .pem file using OpenSSL.</p></blockquote><p>you did not mention the important part: how did you convert the file (openssl command options). Please add that information.</p><p>I <strong>guess</strong> you just extracted the cert instead of the RSA key and thus it does not work.</p><blockquote><p>pkcs12 -export -in filename.cer <strong>-inkey filename.key</strong> -out filename.p12 -name tomcat -CAfile abcd.cer -cname root -chain</p></blockquote><p>Why didn't you just take the 'original' <strong>filename.key</strong> and imported that into Wireshark. Why did you convert the pkcs#12 !??</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '14, 14:47</strong> </span></p></div></div><div id="comments-container-31258" class="comments-container"><span id="31260"></span><div id="comment-31260" class="comment"><div id="post-31260-score" class="comment-score"></div><div class="comment-text"><p>If I remember correctly, I used something along the lines of</p><pre><code>openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes</code></pre><p>I was not aware of being able to just import keys - I was told Wireshark only reads pkcs#12 and .pem.<br />
</p><p>Reason I converted the pkcs#12 was because of this same problem and I was desperate hoping some magic would work.</p></div><div id="comment-31260-info" class="comment-info"><span class="comment-age">(28 Mar '14, 14:52)</span> <span class="comment-user userinfo">JTaNoob</span></div></div><span id="31262"></span><div id="comment-31262" class="comment"><div id="post-31262-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>.pem.</p></blockquote><p>PEM is just an encoding method (in this context). PEM files can contain keys and/or certs. Please use <strong>filename.key</strong> directly <strong>or</strong> modify <strong>keyStore.pem</strong> to only contain the key (not the cert) and it should work.</p></div><div id="comment-31262-info" class="comment-info"><span class="comment-age">(28 Mar '14, 14:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31268"></span><div id="comment-31268" class="comment"><div id="post-31268-score" class="comment-score"></div><div class="comment-text"><p>Thank you sir. If I do however come across any problems, I may reply back.<br />
</p><p>TY</p></div><div id="comment-31268-info" class="comment-info"><span class="comment-age">(28 Mar '14, 15:53)</span> <span class="comment-user userinfo">JTaNoob</span></div></div><span id="31439"></span><div id="comment-31439" class="comment"><div id="post-31439-score" class="comment-score"></div><div class="comment-text"><p>any progress?</p></div><div id="comment-31439-info" class="comment-info"><span class="comment-age">(02 Apr '14, 14:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31258" class="comment-tools"></div><div class="clear"></div><div id="comment-31258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

