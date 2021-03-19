+++
type = "question"
title = "SSL handshake failure when using a certificate that contains NON ASCII characters in Issuer DN"
description = '''Hello,  I am working on an issue where the SSL handshake fails with a connection reset only when using a certificate that is added under trusted CA&#x27;s at server that contains a non ascii character in issuer DN. The client presents a certificate that is signed by this certificate. The SSL handshake wo...'''
date = "2014-06-01T01:08:00Z"
lastmod = "2014-06-01T01:49:00Z"
weight = 33236
keywords = [ "ssl_connection" ]
aliases = [ "/questions/33236" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL handshake failure when using a certificate that contains NON ASCII characters in Issuer DN](/questions/33236/ssl-handshake-failure-when-using-a-certificate-that-contains-non-ascii-characters-in-issuer-dn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33236-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am working on an issue where the SSL handshake fails with a connection reset only when using a certificate that is added under trusted CA's at server that contains a non ascii character in issuer DN. The client presents a certificate that is signed by this certificate. The SSL handshake works fine with a certificate that doesn't contain a non ascii character. I have checked that the certificate has valid values for the non ascii character. I am clueless as to what is the exact failure of this SSL handshake. Can you please help? wireshark log at : <a href="http://www.filedropper.com/tcpdump03031320">http://www.filedropper.com/tcpdump03031320</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/failure_trace.jpg" alt="alt text" /> Frame 6 : server hello contains the certificate. The hex value for é character is e9 which is displayed correctly in wireshark.</p><p>The certificate data is :</p><p>Serial Number: 30, 96. Subject Name: ST=Brabant,[email protected],L=B-1170 Brussels,TEL=+32 2 661 44 11,STREET=Terhulpsesteenweg 150 Chaussée de la Hulpe,CN=Portima PKI Root CA (Qualification),OU=Security,O=Portima s.c. n.v.,C=BE Issues Name: ST=Brabant,[email protected],L=B-1170 Brussels,TEL=+32 2 661 44 11,STREET=Terhulpsesteenweg 150 Chaussée de la Hulpe,CN=Portima PKI Root CA (Qualification),OU=Security,O=Portima s.c. n.v.,C=BE Version: X509 Version 3. Validity: Not Before: Tue Feb 14 09:00:00 EST 2006, Not After: Sat Feb 14 09:00:00 EST 2026. Basic Contraints: CA, path length: not specified. Key Usage: not critical. Certificate extensions: BasicConstraints,Critical SubjectKeyID,: Not Critical KeyUsage,: Not Critical</p><p>It looks like our customer's wireshark log was incomplete and client authentication was enabled and after client sent certificateVerify packet, it failed. We captured these in ssl debug log.</p><p>Here is the ssl debug log : <a href="http://www.filedropper.com/rsasdk">http://www.filedropper.com/rsasdk</a> Upto line 3157, we have a successful transaction for a certificate containing ascii data.</p><p>From line 3157, the server presented a certificate whose CA at client has non ascii data.</p><p>At line 3148 : ***WRITE ClientHello</p><p>At line 3727 : ***READ ServerHello</p><p>At line 3738 : *** Session created</p><p>At line 3864 : ***READ Certificate chain</p><p>At line 3976 : Found trusted certificate</p><p>At line 4030 : ***READ ServerHelloDone</p><p>At line 4042 : *** WRITE ClientKeyExchange RSA PreMasterSecret</p><p>At line 4099 : ***WRITE ChangeCipherSpec</p><p>At line 4134 : ***READ ChangeCipherSpec</p><p>At line 4161 : ***WRITE Application Data</p><p>At line 4269 : ***READ HelloRequest ( ?? I got a Read Application data packet for the successful one at this point)</p><p>At line 4280 : ***WRITE ClientHello</p><p>At line 4859 : ***READ ServerHello</p><p>At line 4870 : *** Session created</p><p>At line 4996 : ***READ Certificate chain</p><p>At line 5108 : Found trusted certificate</p><p>At line 5303 : ***READ CertificateRequest</p><p>At line 5330 : ***READ ServerHelloDone</p><p>At line 5432 : ***WRITE Certificate chain</p><p>At line 5507 : *** WRITE ClientKeyExchange RSA PreMasterSecret</p><p>At line 5558 : ***WRITE CertificateVerify</p><p>At line 5832 : ***WRITE ChangeCipherSpec</p><p>At line 5858 : ***WRITE Finished</p><p>At line 5862 : ***SEND Alert Warning, Close Notify</p></div><div id="question-tags" class="tags-container tags">ssl_connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '14, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/23e402e79613f20cb37caf2d888b6b6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mahathi%20Priya&#39;s gravatar image" /><p>Mahathi Priya<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mahathi Priya has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jun '14, 04:29</p></div></div><div id="comments-container-33236" class="comments-container"></div><div id="comment-tools-33236" class="comment-tools"></div><div class="clear"></div><div id="comment-33236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33237"></span>

<div id="answer-container-33237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33237-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just a 'wild' guess: your client does not accept those characters, encoded as <strong>bmpString</strong>!?</p><p><strong>EDIT</strong>:</p><p>After I had time to check the capture file, I don't believe it's a client problem. The client finishes the handshake and send encrypted data, which means it has accepted the cert and the chain. Furthermore, it's the <strong>server</strong> who closes the connection with a RESET. There must be another reason for the problem.</p><p>Do you have access to the servers private key? If so, you can decrypt the capture file and check if there is anything "strange" in the communication. Otherwise, just check the logs of the server.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '14, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '14, 16:23</p></div></div><div id="comments-container-33237" class="comments-container"><span id="33254"></span><div id="comment-33254" class="comment"><div id="post-33254-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt! I do not have access to the server's private key.But I had learnt that we can decrypt data if the session keys of this session had been exported.</p><p>I had initially thought that it had something to do with the certificate, because the server sends a RST only in this case. Yesterday I researched a bit on analyzing these packets and as you said, we are getting past the verification of the certificate. So probably it has nothing to do with the non-ascii character. I do not think the certificates plays a role later after the session key has been obtained through the handshake. As of now, I will try decrypting the data at server and look at the reason for sending a RST.</p><p>Thank you very much for your help!</p></div><div id="comment-33254-info" class="comment-info"><span class="comment-age">(01 Jun '14, 22:34)</span> Mahathi Priya</div></div><span id="33267"></span><div id="comment-33267" class="comment"><div id="post-33267-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I think i had looked at the incomplete wireshark log. The ssl debug log tells that the client sends a "Alert Warning, Close Notify" after the certificate Verify phase.</p></div><div id="comment-33267-info" class="comment-info"><span class="comment-age">(02 Jun '14, 04:34)</span> Mahathi Priya</div></div></div><div id="comment-tools-33237" class="comment-tools"></div><div class="clear"></div><div id="comment-33237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

