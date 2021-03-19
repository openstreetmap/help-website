+++
type = "question"
title = "Problem with decrypting the SSL using the private key"
description = '''Hello everyone, We are trying to decypt an SSL traffic. I created a test environment with openssl So I created my private key, I created my certificate. The paramteter in the Wireshark seems well configured :  192.168.11.200,443,http,C:&#92;OpenSSL-Win32&#92;bin&#92;testkey.pem But I still do not decrypt this S...'''
date = "2014-12-08T07:47:00Z"
lastmod = "2014-12-15T06:12:00Z"
weight = 38441
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/38441" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with decrypting the SSL using the private key](/questions/38441/problem-with-decrypting-the-ssl-using-the-private-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>We are trying to decypt an SSL traffic. I created a test environment with openssl</p><p>So I created my private key, I created my certificate. The paramteter in the Wireshark seems well configured : 192.168.11.200,443,http,C:\OpenSSL-Win32\bin\testkey.pem</p><p>But I still do not decrypt this SSL while I have all the information... To simulate the server I am using : openssl s_server -key testkey.pem -cert testcert.pem -WWW -cipher RC4-SHA -accept 443</p><p>In the debug file I have <strong>decrypt_ssl3_record: no decoder available</strong></p><p>I add that I am capturing the SSL handshake since the start of the cession..</p><p>Here you can find the key : Thekey seems not protected with a passphrase.</p><p>-----BEGIN RSA PRIVATE KEY-----</p><p>MIICXwIBAAKBgQDubfA0PyHS2vmvW1A+I3vM1+cFRuXbaG/OsDbZeytOoB7OXjIb OeS87ErT7l6fFrIEyCcQozmPQGZdiMuXKvUtiscvRm5oYZzXnUwP3UL19gtmBHjN u1odENV+S2V6jRa3d0XeDiFUMPeYvDsC8s+A/H2OzGA0v7zD1ssDCFd3uwIDAQAB AoGBANdMaOoU1Asd9vc04omp6wG3OAJY2fi9HrEqB+1svld6WTcKcf6J0ZYTXSJw jfrkOI3+2t+4NKK5iXYOr6DqhocB5NMDXPtdHpVyUkOQF6ugE9/fA6DfAVLTdtIE s5aQqt+8PcxZzwdw0fg07vVHNx7dEXr0q34cTDeIDrXUB6cRAkEA/73swjLosyOJ gjK61YgHhFKl5r/q3B4Et/cDru7mx4e+gA9vJODujvVkrwJZKly4KWGKSrudXyUr W3jHIhWOWQJBAO6ril5EyZ1GQwg1jNuyPw7FEzZGDFLwCeDI5Si+bJzpK1TGOf+6 IUJMFaVGSevVCZCLxHUEpMVlcCM4QNzBfDMCQQDth7ONM8eaCtm/CesqROvmZPUd +wbiZycuzsinA9FpZZT0UGGEuT4ZnaZkPiQfCnsqRCQ0AUnLgzRgAy/BYpARAkEA 1enT66f1mEvoOoxcgnChCejizks8Mn3ILLuCgOEj0gM+fg3o3+aAdr5gzDBSgtf/ aZmL7GHMGMxRFJAPuoyEdwJBAPWF7C3sgtW4Rqxy4MJ2zp5h72C5rkvs7Rxqma/R GGvsMKINd3Gm1IKUXv5HIPxyHIgrTrgFMsMO81ASiLrPJWw=</p><p>-----END RSA PRIVATE KEY-----</p><p>Here the prt of the debug file :<img src="https://osqa-ask.wireshark.org/upfiles/CaptureDebug.JPG" alt="alt text" /></p><p>Thanks in advance, I am becoming crazy since I have all the files but could no decypt the DATA.</p></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '14, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/848ee97cc734c0106a9502fc4bb882f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knacky&#39;s gravatar image" /><p>knacky<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knacky has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '14, 08:02</p></div></div><div id="comments-container-38441" class="comments-container"><span id="38445"></span><div id="comment-38445" class="comment"><div id="post-38445-score" class="comment-score">1</div><div class="comment-text"><p>Imho the provided log is not enough. Can you provide more data?</p><p>Some general things:</p><ul><li>Wireshark is only able to decrypt SSL when the full first SSL handshake is available ("Client Hello" with Session-ID = 0)</li><li>The Key-Exchange should be RSA (not DHE or ECDHE)</li><li>SSL: "Reassemble SSL records spanning multiple TCP segments" should be enabled</li><li>TCP: "Allow subdissectors to reassemble TCP streams" should also be enabled</li></ul></div><div id="comment-38445-info" class="comment-info"><span class="comment-age">(08 Dec '14, 10:25)</span> Uli</div></div><span id="38446"></span><div id="comment-38446" class="comment"><div id="post-38446-score" class="comment-score"></div><div class="comment-text"><p>please post the full log file as <strong>text</strong> and not as screenshot!</p><p>As you've already posted the private key, can you please share the public key and the capture file on google drive, dropbox, etc. - and post the link here.</p></div><div id="comment-38446-info" class="comment-info"><span class="comment-age">(08 Dec '14, 11:14)</span> Kurt Knochner ♦</div></div><span id="38494"></span><div id="comment-38494" class="comment"><div id="post-38494-score" class="comment-score"></div><div class="comment-text"><p>Thx guys for your answers.</p><p>You can see here the Certificate, what is the public key if I understand well :</p><p>-----BEGIN CERTIFICATE-----</p><p>MIICnDCCAgWgAwIBAgIJAPGXk7yteXUQMA0GCSqGSIb3DQEBBQUAMGcxCzAJBgNV BAYTAlNXMQ8wDQYDVQQIDAZHZW5ldmExDzANBgNVBAcMBkdlbmV2YTEUMBIGA1UE CgwLU2t5c29mdC1BVE0xCzAJBgNVBAsMAklUMRMwEQYDVQQDDApEVUZPVVJKRVJP MB4XDTE0MTIwODE1MDkwMloXDTE1MDEwNzE1MDkwMlowZzELMAkGA1UEBhMCU1cx DzANBgNVBAgMBkdlbmV2YTEPMA0GA1UEBwwGR2VuZXZhMRQwEgYDVQQKDAtTa3lz b2Z0LUFUTTELMAkGA1UECwwCSVQxEzARBgNVBAMMCkRVRk9VUkpFUk8wgZ8wDQYJ KoZIhvcNAQEBBQADgY0AMIGJAoGBAO5t8DQ/IdLa+a9bUD4je8zX5wVG5dtob86w Ntl7K06gHs5eMhs55LzsStPuXp8WsgTIJxCjOY9AZl2Iy5cq9S2Kxy9GbmhhnNed TA/dQvX2C2YEeM27Wh0Q1X5LZXqNFrd3Rd4OIVQw95i8OwLyz4D8fY7MYDS/vMPW ywMIV3e7AgMBAAGjUDBOMB0GA1UdDgQWBBTfpYLI0I7y25YqasZD8wALlmi0lTAf BgNVHSMEGDAWgBTfpYLI0I7y25YqasZD8wALlmi0lTAMBgNVHRMEBTADAQH/MA0G CSqGSIb3DQEBBQUAA4GBAOoCP3JJETB/vjHgYdY7Bg1Ltsxj/kkAWrlg8CJjJ3PV TCl3RwUmxbAEnxIrITK1i8EJlhiD1xpnNBubvzz101g5Djp0W8gCYU4VEqv7nVQT CxGsdrKkhGnq9PJOago8Ly1HK026QTiIXPFv7mN47ZU2SpLhNLTypO9AOjTPtiFr</p><p>-----END CERTIFICATE-----</p><p>And Here you can find the Debug.txt</p><p><a href="https://drive.google.com/file/d/0BwRtcvviHMo_QVYwU3dBTlRsVUE/view?usp=sharing">https://drive.google.com/file/d/0BwRtcvviHMo_QVYwU3dBTlRsVUE/view?usp=sharing</a></p><p>My process is simple:</p><ul><li>I create the certificate</li><li>I create the private key</li><li>I convert this key with <strong>RSA</strong></li><li>I simulate the server SSL with open SSL (Windows7)</li><li>And before to connect with a Client (firefox on ubuntu) <strong>I delete all the history to have the full Handshake.</strong></li></ul><p>Regarding the 2 last propositions I will check.</p><ul><li>SSL: "Reassemble SSL records spanning multiple TCP segments" should be enabled</li><li>TCP: "Allow subdissectors to reassemble TCP streams" should also be enabled</li></ul><p>Thanks a lot for your contribution.</p></div><div id="comment-38494-info" class="comment-info"><span class="comment-age">(09 Dec '14, 07:53)</span> knacky</div></div></div><div id="comment-tools-38441" class="comment-tools"></div><div class="clear"></div><div id="comment-38441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38567"></span>

<div id="answer-container-38567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let's do an analysis on the debug log, frame 38:</p><pre><code>dissect_ssl3_hnd_hello_common found SERVER RANDOM -&gt; state 0x13
ssl_restore_session can&#39;t find stored session</code></pre><p>No pre-master secret read from a keylog file. Should not be a problem since you have a RSA private key.</p><pre><code>dissect_ssl3_hnd_srv_hello found CIPHER 0x0005 -&gt; state 0x17</code></pre><p>Cipher suite ID 0x0005 is RC4-SHA which is not an ECDH suite, so you are able to use the RSA private key.</p><pre><code>dissect_ssl3_hnd_srv_hello trying to generate keys
ssl_generate_keyring_material not enough data to generate key (0x17 required 0x37 or 0x57)
dissect_ssl3_hnd_srv_hello can&#39;t generate keyring material</code></pre><p>This is more problematic, no Master Secret (0x40) nor Pre-Master secret (0x20) could be found. A few frames later (frame 40), the required key material can be generated.</p><p>Scanning further through your debug log, it appears that the decryption goes wrong. There was an issue in Wireshark 1.10 which could result in bad decryption for the TLS protocol (memmove vs memcpy). Your debug log says that TLS 1.2 is in use, so you need at least Wireshark 1.12 to get all SSL/TLS dissector improvements.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-38567" class="comments-container"></div><div id="comment-tools-38567" class="comment-tools"></div><div class="clear"></div><div id="comment-38567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

