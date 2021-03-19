+++
type = "question"
title = "SSL decrypting when Browser in play ??"
description = '''I am trying to decrypt a complete SSL session using wireshark (and then will use tshark). I have the server private key and can see wireshark decrypting return traffic from server to client. However, the client sourced traffic is not decrypted (I can&#x27;t see the decrypted GET). I am using the Internet...'''
date = "2012-04-10T12:37:00Z"
lastmod = "2012-04-11T23:30:00Z"
weight = 10045
keywords = [ "ssl", "browser" ]
aliases = [ "/questions/10045" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decrypting when Browser in play ??](/questions/10045/ssl-decrypting-when-browser-in-play)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt a complete SSL session using wireshark (and then will use tshark). I have the server private key and can see wireshark decrypting return traffic from server to client. However, the client sourced traffic is not decrypted (I can't see the decrypted GET). I am using the Internet Explorer browser on a Win7 system. Wireshark is running on the Win7 system.</p><p>Now for a few questions:</p><p>1) do I need to have the IE browser private key loaded into wireshark ??</p><p>2) if so, where do I find the private key used by the browser ?? must I somehow extract it ??</p><p>Any/all advice would be appreciated. (yes, I've read the various tag entries regarding ssl but haven't seen anything that fully addresses my question. If I missed the golden nugget, please provide a pointer)</p><p>thanks, wk</p></div><div id="question-tags" class="tags-container tags">ssl browser</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p>wakelt<br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div></div><div id="comments-container-10045" class="comments-container"></div><div id="comment-tools-10045" class="comment-tools"></div><div class="clear"></div><div id="comment-10045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10047"></span>

<div id="answer-container-10047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10047-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you don't need anything from the client, there must be some other reason that it won't decrypt the client messages...</p><p>Do you see a "Finished" handshake message from the client? If so, then decryption did start correctly for the client side (otherwise there would be an "Encrypted Handshake" message instead).</p><p>If it is a server in a test environment, could you post the capture file on <a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the link here accompanied by the server key?</p><p>If that's not possible, can you attach the SSL debug log to your question?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '12, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10047" class="comments-container"><span id="10084"></span><div id="comment-10084" class="comment"><div id="post-10084-score" class="comment-score"></div><div class="comment-text"><p>Thanks for sharing this valuable information.</p></div><div id="comment-10084-info" class="comment-info"><span class="comment-age">(11 Apr '12, 22:57)</span> Mano</div></div><span id="10085"></span><div id="comment-10085" class="comment"><div id="post-10085-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p><p>(I converted your "answer" to a "comment", which is how this site works best, please see the FAQ)</p></div><div id="comment-10085-info" class="comment-info"><span class="comment-age">(11 Apr '12, 23:30)</span> SYN-bit ♦♦</div></div><span id="10128"></span><div id="comment-10128" class="comment"><div id="post-10128-score" class="comment-score"></div><div class="comment-text"><p>Answers to questions from Syn-Bit...</p><p>1) yes there is a client FINISH. The finish is contained in the same packet as the Client Key Exchange and Change Cipher messages.</p><p>2) It seems that the SSL dissector may be trying to convert to regular HTTP, but its claiming a malformed packet thus I don't see the GET. I'm not sure what it doesn't like about the packet ?? If I run the same page w/o SSL, wireshark doesn't complain about malformation. The log entry for the malformed (packet #30) is below. It is the first packet from client to server after the client FINISH (client is ie browser).</p><pre><code>dissect_ssl enter frame #30 (first time)
  conversation = 03E32978, ssl_session = 03E32CE0
  record: offset = 0, reported_length_remaining = 666
dissect_ssl3_record: content_type 23
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
51 46 f2 c0 98 0f f8 d5 30 e2 27 63 c0 1b e9 fa 
1d b4 a3 93 77 34 b1 d7 06 1c 15 a0 00 63 4e 9b 
Plaintext[32]:
47 36 54 ed ff ea d9 0f df 11 b0 50 50 05 3e e4 
9b 6b 8f 5d f8 0a 0a 0a 0a 0a 0a 0a 0a 0a 0a 0a 
ssl_decrypt_record found padding 10 final len 21
checking mac (len 1, version 301, ct 23 seq 1)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
36 54 ed ff ea d9 0f df 11 b0 50 50 05 3e e4 9b 
6b 8f 5d f8 
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 1, seq = 0, nxtseq = 1
association_find: TCP port 60129 found 00000000
association_find: TCP port 443 found 03793460
dissect_ssl3_record decrypted len 1
decrypted app data fragment: G
dissect_ssl3_record found association 03793460</code></pre><p>I couldn't figure out how to attach the complete log file. I'd love to know what the dissector is having issues with ?? The site seems to work fine. The good news is that the issue is very reproduceable.</p><p>Thanks so much for any help you can provide.</p><p>-walter</p></div><div id="comment-10128-info" class="comment-info"><span class="comment-age">(13 Apr '12, 07:40)</span> wakelt</div></div><span id="10129"></span><div id="comment-10129" class="comment"><div id="post-10129-score" class="comment-score"></div><div class="comment-text"><p>OK, decryption works, but indeed the HTTP request is garbled. What you can do is to use "data" in your SSL-keys list instead of "http" to disable http processing by Wireshark.</p><p>You can also do "Follow SSL stream" to get a few on the decrypted data.</p></div><div id="comment-10129-info" class="comment-info"><span class="comment-age">(13 Apr '12, 08:12)</span> SYN-bit ♦♦</div></div><span id="10133"></span><div id="comment-10133" class="comment"><div id="post-10133-score" class="comment-score"></div><div class="comment-text"><p>Thanks Syn-Bit...I am looking at the "data" within the packet as you suggest. I see the following oddity:</p><ul><li><p>immediately after the client FINISH, the client sends the encrypted GET out (so far so good)</p></li><li><p>wireshark is decoding 2 data field in the same packet:</p></li></ul><p>Data (1 byte)<br />
Data: 47 [Length: 1] Data (743 bytes) Data: 45675xxxxxxxxxxxxxxxxxx...lots of bytes [Length: 743]</p><p>It so happens that 0x47 is ascii letter G (the first letter of GET). The second data field has the remainder of the request.</p><p>Why is the SSL dissector seeing two data fields ?? Something feels odd about this. What separates one data field from the next ?? Is there some type of index that is off ?? As mentioned earlier, the server has no issue interpreting the encrypted command and respond with proper data.</p><p>thanks, Walter</p></div><div id="comment-10133-info" class="comment-info"><span class="comment-age">(13 Apr '12, 10:29)</span> wakelt</div></div><span id="10139"></span><div id="comment-10139" class="comment not_top_scorer"><div id="post-10139-score" class="comment-score"></div><div class="comment-text"><p>snippet of the packet byte output where wireshark claims malformation. Again, not sure why the dissector splits up the G ET into two separate data decryptions ???? (if that is indeed what it is doing)</p><p>===================================================================================== 02e0 28 e9 56 ed 40 01 69 aa 68 6d 72 df 88 29 a2 99 ([email protected]).. 02f0 fe ee 84 b5 fd 8c af 29 b3 dd 64 f0 4c e6 d1 d6 .......)..d.L... 0300 d3 4f ac 95 fb 48 e8 62 f0 a9 2d e7 5b 36 1c 68 .O...H.b..-.[6.h 0310 04 bb 6b 25 2d 34 cb cb 35 df c7 ca 41 18 45 d6 ..k%-4..5...A.E. 0320 fe 07 c0 36 e2 96 35 fa 28 ab 12 c5 15 da 80 09 ...6..5.(.......</p><p>Decrypted SSL data (1 bytes):</p><p>0000 47 G</p><p>Decrypted SSL data (697 bytes):</p><p>0000 45 54 20 2f 63 73 73 2f 6d 61 69 6e 2e 63 73 73 ET /css/main.css 0010 20 48 54 54 50 2f 31 2e 31 0d 0a 41 63 63 65 70 HTTP/1.1..Accep 0020 74 3a 20 2a 2f 2a 0d 0a 52 65 66 65 72 65 72 3a t: <em>/</em>..Referer: 0030 20 68 74 74 70 73 3a 2f 2f 6f 72 69 67 69 6e 2d <a href="https://origin">https://origin</a>-</p></div><div id="comment-10139-info" class="comment-info"><span class="comment-age">(13 Apr '12, 12:15)</span> wakelt</div></div><span id="10140"></span><div id="comment-10140" class="comment not_top_scorer"><div id="post-10140-score" class="comment-score"></div><div class="comment-text"><p>@wakelt I changed your "answers" to comments. See the <a href="http://ask.wireshark.org/faq/" title="FAQ">FAQ</a> about how this Q&amp;A site works. To add such long pieces of updated information to your <em>questions</em> in the future, you should edit the original question.</p></div><div id="comment-10140-info" class="comment-info"><span class="comment-age">(13 Apr '12, 13:34)</span> multipleinte...</div></div></div><div id="comment-tools-10047" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-10047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10086"></span>

<div id="answer-container-10086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10086-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Step one – set up an SSL-protected server to use as a testbed</p><p>To illustrate the process, we’re going to use OpenSSL to generate a certificate and act as a web server running HTTP over SSL (aka HTTPS) – it’s quite straightforward.</p><p>To begin with, we need to get ourselves a self-signed certificate that our HTTPS server can use. We can do this with a single command:</p><p>openssl req -x509 -nodes -newkey rsa:1024 -keyout testkey.pem -out testcert.pem</p><p>OpenSSL will ask you for some input to populate your certificate with; once you’ve answered all the questions, the output of this command is two files, testkey.pem (containing a 1024 bit RSA private key) and testcert.pem (containing a self signed certificate). PEM (Privacy Enhanced Mail) format files are plaintext, and consist of a BASE64 encoded body with header and footer lines. You can look at the contents of your key and certificate files in more detail like this:</p><p>openssl rsa -in testkey.pem -text -noout (output here) openssl x509 -in testcert.pem -text -noout (output here; more info here)</p><p>We need to perform one tiny tweak to the format of the private key file (Wireshark will use this later on, and it won’t work properly until we’ve done this):</p><p>openssl rsa -in testkey.pem -out testkey.pem</p><p>Now we’re ready to fire up our HTTPS server:</p><p>openssl s_server -key testkey.pem -cert testcert.pem -WWW -cipher RC4-SHA -accept 443</p><p>The -key and -cert parameters to the s_server command reference the files we’ve just created, and the -WWW parameter (this one is case sensitive) causes OpenSSL to act like a simple web server capable of retrieving files in the current directory (I created a simple test file called myfile.html for the purposes of the test).</p><p>The -cipher parameter tells the server to use a particular cipher suite – I’m using RC4-SHA because that’s what’s used when you go to <a href="https://www.google.com">https://www.google.com</a>. The RC4-SHA cipher suite will use RSA keys for authentication and key exchange, 128-bit RC4 for encryption, and SHA1 for hashing.</p><p>Having got our server up and running, we can point a browser at <a href="https://myserver/myfile.html">https://myserver/myfile.html</a> and retrieve our test file via SSL (you can ignore any warnings about the validity of the certificate). If you’ve got this working, we can move on to…</p><p>Step two – capture some traffic with Wireshark</p><p>Fire up Wireshark on the server machine, ideally with a capture filter like “tcp port 443″ so that we don’t capture any unnecessary traffic. Once we’re capturing, point your browser (running on a different machine) at <a href="https://myserver/myfile.html">https://myserver/myfile.html</a> and stop the capture once it’s complete.</p><p>Right-click on any of the captured frames and select “Follow TCP stream” – a window will pop up that’s largely full of SSL-protected gobbledegook:</p><p>Step three – configuring Wireshark for decryption</p><p>Close the TCP Stream window and select Preferences from Wireshark’s Edit menu. Expand the “Protocols” node in the tree on the left and scroll down to SSL (in newer versions of Wireshark, you can open the node and type SSL and it will take you there).</p><p>Once SSL is selected, there’s an option on the right to enter an “RSA keys list”. Enter something like this:</p><p>10.16.8.5,443,http,c:\openssl-win32\bin\testkey.pem</p><p>You’ll need to edit the server IP address and path to testkey.pem as appropriate. If this has worked, we’ll notice two things:</p><pre><code>* Wireshark’s SSL dissector can look into otherwise encrypted SSL packets and dissect the protocol inside:
* We can right-click on any of the captured frames that are listed as SSL or TLS and select “Follow SSL stream”:</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '12, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/a344d652cf70aee497362b696383e1a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Crispina&#39;s gravatar image" /><p>Crispina<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Crispina has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10086" class="comments-container"><span id="10091"></span><div id="comment-10091" class="comment"><div id="post-10091-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the replies above. I've been out of the office since Tuesday afternoon. I'll be back in tomorrow.</p><p>@SYN-bit, it is a public site so I can provide the private key. I will provide the log file. I could provide a capture as well if it would help.</p><p>@Crispina, I have followed ALL these steps (I believe) and can see the server side decrypted. I don't see the client side decrypted. The question is why ???</p><p>I look forward to your continued support.</p><p>thanks, walter</p></div><div id="comment-10091-info" class="comment-info"><span class="comment-age">(12 Apr '12, 09:35)</span> wakelt</div></div></div><div id="comment-tools-10086" class="comment-tools"></div><div class="clear"></div><div id="comment-10086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

