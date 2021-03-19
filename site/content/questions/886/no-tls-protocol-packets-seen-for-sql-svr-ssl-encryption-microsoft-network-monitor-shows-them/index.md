+++
type = "question"
title = "No TLS protocol packets seen for SQL Svr SSL Encryption.  Microsoft Network Monitor shows them."
description = '''Hello -  Problem Definition I&#x27;ve configured SQL Server 2005 Express edition to use SSL encryption for database connections. I use SQL Mgmt Studio to connect to my database with &quot;encrypt&quot; check box on. I&#x27;ve even enabled the FIPS 140-2 complaince in my local policy. I want to check if the DB connectio...'''
date = "2010-11-09T11:35:00Z"
lastmod = "2010-11-11T17:17:00Z"
weight = 886
keywords = [ "tls_aes" ]
aliases = [ "/questions/886" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No TLS protocol packets seen for SQL Svr SSL Encryption. Microsoft Network Monitor shows them.](/questions/886/no-tls-protocol-packets-seen-for-sql-svr-ssl-encryption-microsoft-network-monitor-shows-them)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-886-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello -</p><p>Problem Definition</p><p>I've configured SQL Server 2005 Express edition to use SSL encryption for database connections. I use SQL Mgmt Studio to connect to my database with "encrypt" check box on. I've even enabled the FIPS 140-2 complaince in my local policy. I want to check if the DB connection is truely using TLS/SSL when I connect from mgmt studio to the SQL Server db. My connection is successful, and when I use "Microsoft network monitor 3.4" utility to check the traffic, I can see the TLS protocol packets.</p><p>But when I use Wireshark, I only see TCP protocol packets. No TLS.<br />
Why???</p><p>My Environment</p><p>Windows 7 professional laptop, Sql Svr 2005 express svc pk 3</p><p>Wireshark 1.4.1 (with GnuTLS 2.8.5 - checked in about)</p><p>A self generated certificate using makecert</p><p>What I tried in Wireshark</p><p>Since TLS protocol packets were not showing up by default, I tried to follow some information on http://wiki.wireshark.org/SSL? to use SSL dissector.</p><p>The certificate I created and deployed for SQL Server was using the following command</p><p>makecert -r -pe -n "CN=mycompanyname" -b 01/01/2000 -e 01/01/2050 -eku 1.3.6.1.5.5.7.3.1 -ss my -sr localMachine -sky exchange -sp "Microsoft RSA SChannel Cryptographic Provider" -sy 12 c:mycert.cer</p><p>I imported the generated certificate using MMC. Then I exported this imported certificate along with the private key, in PFX format (mycert.pfx). The export happened for PKCS12</p><p>Then I used the following command to extract all the information in PEM file from the PFX file.</p><p>openssl pkcs12 -in exportedsproutscertWithPrivateKeyUsesPKCS12.pfx -out key.pem</p><p>Then I copied the private key from the generate PEM file into a separate file myprivatekey.key</p><p>Then I went in preferences-protocols-ssl in wireshark and configured the RSA Keys list box to say 127.0.0.1,0,tcp,c:pathtomyprivatekeymyprivatekey.key,privatekeypassword All other checkboxes are selected and I specified a log file for SSL Debug file.</p><p>When I apply and run wireshark to monitor the traffic, I get the following error in the debug file.</p><p>"gnutls_pkcs12_import(ssl_p12, &amp;data, GNUTLS_X509_FMT_DER, 0) - ASN1 parser: Error in TAG."</p><p>Why??</p><p>-Is there something wrong in my syntax for RSA keys list?</p><p>-If my private key is not valid or whatever, why wouldnt i see any errors when i generated the certificate using makecert or when i imported/exported it or when i used openssl to convert from PFX to PEM. I went from .cer to .pfx to .pem and saw no errors anywhere.<br />
</p></div><div id="question-tags" class="tags-container tags">tls_aes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/c80c843bd3b5566814cbc9c3b10ceb8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazybee26&#39;s gravatar image" /><p>lazybee26<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazybee26 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-886" class="comments-container"></div><div id="comment-tools-886" class="comment-tools"></div><div class="clear"></div><div id="comment-886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="924"></span>

<div id="answer-container-924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-924-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just a quick thought on "not seeing TLS" traffic. Is the traffic on port 443 or another port? If another port, add the port number to preferences &gt; HTTP in the SSL/TLS ports area.</p><p>The key syntax should look something like 127.0.0.1,443,http,c:keylistmykey.key - not the port is 443 and the protocol is http after it. You're not decrypting TCP - you're decrypting HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-924" class="comments-container"></div><div id="comment-tools-924" class="comment-tools"></div><div class="clear"></div><div id="comment-924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

