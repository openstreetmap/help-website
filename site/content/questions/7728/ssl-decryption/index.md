+++
type = "question"
title = "ssl decryption"
description = '''Just upgraded to 1.7.0 from 1.6.4 In neither release was ssl decryption working (at least I couldn&#x27;t get it to work) Have read the zillions of available googles on the topic. My question is simple -  Has anyone actually got this to work with this version ? Either way I&#x27;ll likely give up - but I just...'''
date = "2011-12-01T08:29:00Z"
lastmod = "2011-12-05T12:00:00Z"
weight = 7728
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/7728" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ssl decryption](/questions/7728/ssl-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7728-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Just upgraded to 1.7.0 from 1.6.4 In neither release was ssl decryption working (at least I couldn't get it to work) Have read the zillions of available googles on the topic. My question is simple - Has anyone actually got this to work with this version ?</p><p>Either way I'll likely give up - but I just wanted to know if someone had actually, with their very own fingers, gotten this to work with 1.7.0 1.6.4.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ssl decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '11, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/8d1804678e43c4c287d395126b8f4a6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="colayack&#39;s gravatar image" /><p>colayack<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="colayack has no accepted answers">0%</span></p></div></div><div id="comments-container-7728" class="comments-container"></div><div id="comment-tools-7728" class="comment-tools"></div><div class="clear"></div><div id="comment-7728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7730"></span>

<div id="answer-container-7730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7730-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, even today...</p><p>There are three things you need to make sure of:</p><ul><li>Provide the proper private key (check the ssl-debug log to see if it actually loaded OK)</li><li>Make sure the whole SSL handshake for this SSL session is in the tracefile (make sure you see the "Certificate" message from the server)</li><li>Check whether you're <strong>not</strong> using a DiffieHellman cipher (the cipher in the ServerHello message should not contain DHE or DH)</li></ul><p>If that does not get you started, have a look at my <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">Sharkfest presentation on troubleshooting SSL</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '11, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7730" class="comments-container"><span id="7732"></span><div id="comment-7732" class="comment"><div id="post-7732-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for the response. I believe all of the items above check out ok. I'll add some 'exciting' snippets from the log file. If you'd like more info - that would be fine. If you'd care not to look any further - I understand that, too. This would be a lifesaver if it worked. Thanks, Steve</p><p>Items that might be interesting: <strong>looks like things start out fine:</strong></p><pre><code>ssl_association_remove removing TCP 443 - http handle 03818A60
Private key imported: KeyID 60:66:fc:9d:79:d8:4b:0c:23:82:cb:f1:fa:11:ac:06:...
ssl_init IPv4 addr &#39;10.5.4.224&#39; (10.5.4.224) port &#39;443&#39; filename &#39;Q:\yackes\certs\devpc\ecomtls.pk&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file Q:\yackes\certs\devpc\ecomtls.pk successfully loaded.
association_add TCP port 443 protocol http handle 03818A60
Private key imported: KeyID 5b:2c:ed:79:fb:c4:ed:33:ef:74:69:0b:d5:36:2a:23:...
ssl_init IPv4 addr &#39;10.5.1.189&#39; (10.5.1.189) port &#39;443&#39; filename &#39;Q:\yackes\certs\leoa\navtls.pk&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file Q:\yackes\certs\leoa\navtls.pk successfully loaded.
association_add TCP port 443 protocol http handle 03818A60</code></pre><p><strong>this is the only hint of an error</strong></p><pre><code>ssl_decrypt_pre_master_secret wrong pre_master_secret length (123, expected 48)
dissect_ssl3_handshake can&#39;t decrypt pre master secret
  record: offset = 279, reported_length_remaining = 59</code></pre><p><strong>lots of these</strong></p><pre><code>decrypt_ssl3_record: no decoder available</code></pre></div><div id="comment-7732-info" class="comment-info"><span class="comment-age">(01 Dec '11, 13:26)</span> colayack</div></div><span id="7735"></span><div id="comment-7735" class="comment"><div id="post-7735-score" class="comment-score"></div><div class="comment-text"><p>Are you sure the key is the one matching the certificate? I have seen the "wrong pre_master_secret length" errors when I was providing the wrong key.</p><p>You should point Wireshark to the (PEM formatted) private key which resides on the server 10.5.4.224.</p></div><div id="comment-7735-info" class="comment-info"><span class="comment-age">(01 Dec '11, 15:23)</span> SYN-bit ♦♦</div></div><span id="7740"></span><div id="comment-7740" class="comment"><div id="post-7740-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>After initial failings I made the keys/certs myself. Following is the pattern.</p><p>Problem is I am ignorant enough to be dangerous. I wouldn't know a PEM from ... well whatever</p><p>Does the below qualify as a PEM ?</p><p>Thanks (and I'll check on your most recent suggestions right now)</p><p>2330 openssl genrsa -des3 -out server_224.key 2048 2331 openssl rsa -in server_224.key -out server_224.key.insecure 2332 openssl req -new -key server_224.key.insecure -out server_224.csr 2334 openssl x509 -req -days 365 -in server_224.csr -signkey server_224.key.insecure -out server_224.crt</p></div><div id="comment-7740-info" class="comment-info"><span class="comment-age">(02 Dec '11, 05:55)</span> colayack</div></div><span id="7741"></span><div id="comment-7741" class="comment"><div id="post-7741-score" class="comment-score"></div><div class="comment-text"><p>2330 openssl genrsa -des3 -out server_224.key 2048</p><p>2331 openssl rsa -in server_224.key -out server_224.key.insecure</p><p>2332 openssl req -new -key server_224.key.insecure -out server_224.csr</p><p>2334 openssl x509 -req -days 365 -in server_224.csr -signkey server_224.key.insecure -out server_224.crt</p></div><div id="comment-7741-info" class="comment-info"><span class="comment-age">(02 Dec '11, 05:56)</span> colayack</div></div><span id="7745"></span><div id="comment-7745" class="comment"><div id="post-7745-score" class="comment-score"></div><div class="comment-text"><p>@colayack I converted your "answers" to comments, as they were responses to SYNbit's answer.</p></div><div id="comment-7745-info" class="comment-info"><span class="comment-age">(02 Dec '11, 10:59)</span> grahamb ♦</div></div><span id="7774"></span><div id="comment-7774" class="comment not_top_scorer"><div id="post-7774-score" class="comment-score"></div><div class="comment-text"><p>Thanks for all the help. I'm sure it works great. I'll just 'move on'</p></div><div id="comment-7774-info" class="comment-info"><span class="comment-age">(05 Dec '11, 08:25)</span> colayack</div></div></div><div id="comment-tools-7730" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-7730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7775"></span>

<div id="answer-container-7775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7775-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="http://www.cloudshark.org/captures/4b2026b526b0">the capture I posted at CloudShark</a>, you can use the following key to decrypt the traffic:</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDrHdbb+yGE6m6EZ03bXURpZCjch2H6g97ZAkJVGrjLZFfettBA
EYa8vYYxWsf8KBpEZeksSCsDA9MnU2H6QDjzqdOnaSWfeXMAr4OsCOpauStpreq7
q1hk8iOqy+f4KijRrhWplh1QW1A8gtSIg137pyUhW+WsfwxKwmzjGIC1SwIDAQAB
AoGBAMneA9U6KIxjb+JUg/99c7h9W6wEvTYHNTXjf6psWA+hpuQ82E65/ZJdszL6
+8vfbrYdPfdcOznKdehE6lGgBIRjhbOOeOxTxfbt1OWcVeqW17t52QiZbaK/dt/j
Fn8RyixrU4NSSPWG7NCyLJwYU2lgstUbhHg2Hz9Mz59GgS2xAkEA+fXI/b65qF29
/OAz8iHrmGU/qmwrP2+I+gNB1ji2bIPfXLg/V3Q70golpeRhcORB1SbMYP8+PCU5
5NsC1iRGuQJBAPDMO/w8Rzl4waw885c3DFlIar81H3VCBoswUqPBDdQvtSatMq1c
BA27q5Re+XewBGx4AbP84lPPsDD7aX8eWiMCQQCEUfVdRgq4My+w3usAwa4bFXYX
fH2EbkG/v9upUIpZdZHXXn3BiPll3hNB910RyvOCp7BHpLbIVhiIqtucisWZAkAs
b6QKMh16r5wd6smQ+CmhOEnqqyT5AIwwl2RIr9GbfIpTbtbRQw/EcQOCx9wFiEfo
tGSsEFi72rHK+DpJqRI9AkEA72gdyXRgPfGOS3rfQ3DBcImBQvDSCBa4cuU1XJ1/
MO93a8v9Vj87/yDm4xsBDsoz2PyBepawHVlIvZ6jDD0aXw==
-----END RSA PRIVATE KEY-----</code></pre><p>Please note that there are two bugs in Wireshark since 1.6.0 which seem to effect decryption:</p><ul><li>You need to restart wireshark after adding a key to the SSL preferences (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6032">bug 6032</a>)</li><li>You need to configure a SSL debug file (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6033">bug 6033</a>)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7775" class="comments-container"></div><div id="comment-tools-7775" class="comment-tools"></div><div class="clear"></div><div id="comment-7775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

