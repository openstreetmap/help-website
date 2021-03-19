+++
type = "question"
title = "SSL and encrypted alert"
description = '''I&#x27;ve configured an Apache server as a front for a Tomcat. On the httpd server, I&#x27;ve configured an https connection. This connection is mandatory, so all requests made using http are redirected to the https schema. My site is really slow using this environment. I suppose that there is a misconfigurat...'''
date = "2012-12-17T11:13:00Z"
lastmod = "2012-12-25T15:23:00Z"
weight = 16986
keywords = [ "apache", "ssl", "tomcat", "alert" ]
aliases = [ "/questions/16986" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL and encrypted alert](/questions/16986/ssl-and-encrypted-alert)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16986-score" class="post-score" title="current number of votes">0</div><span id="post-16986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've configured an Apache server as a front for a Tomcat. On the httpd server, I've configured an https connection. This connection is mandatory, so all requests made using http are redirected to the https schema.</p><p>My site is really slow using this environment. I suppose that there is a misconfiguration somewhere, but I don't know where.</p><p>I've made a capture with Wireshark, and I see some encrypted alert. Following advice I've found on some forum, I've read about those alert messages. Some are supposed to be ok, but some are not. For example I've seen an alert with the code 46. Is it possible that with this kind of alert my site would be encrypted, but really slow??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tomcat" rel="tag" title="see questions tagged &#39;tomcat&#39;">tomcat</span> <span class="post-tag tag-link-alert" rel="tag" title="see questions tagged &#39;alert&#39;">alert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/fd1adaf32d9dc6531d6041dbc379efb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benzen&#39;s gravatar image" /><p><span>benzen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benzen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Dec '12, 05:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-16986" class="comments-container"><span id="17169"></span><div id="comment-17169" class="comment"><div id="post-17169-score" class="comment-score"></div><div class="comment-text"><p>as you posted the same config file twice, I believe you did not see the <strong>show all</strong> link in the series of my comments, right? Click on it and you will see all comments, including a suggestion of mine regarding the config file.</p></div><div id="comment-17169-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16986" class="comment-tools"></div><div class="clear"></div><div id="comment-16986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16987"></span>

<div id="answer-container-16987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16987-score" class="post-score" title="current number of votes">1</div><span id="post-16987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Code 46 means "certificate_unknown", so it might be a problem with the certificate checking process. Well, then the browser should display an error message. Without further information about your setup (OS version, server software, client software, certificates) it's hard to make a good assumption about the possible problem.</p><p>One possible reason: If there is a <strong>CRL distribution point</strong> in your certificate, your browser might try to fetch the CRL and if it can't it may slow down your connection. The same is true for OCSP.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16987" class="comments-container"><span id="16988"></span><div id="comment-16988" class="comment"><div id="post-16988-score" class="comment-score"></div><div class="comment-text"><p>Sorry i'm fairly new to this. Could you explain to me what is a crl or OCSP.</p><p>Maybe that could help to understand better, my cert is a self</p></div><div id="comment-16988-info" class="comment-info"><span class="comment-age">(17 Dec '12, 11:53)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="16992"></span><div id="comment-16992" class="comment"><div id="post-16992-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Sorry i'm fairly new to this. Could you explain to me what is a crl or OCSP.</p></blockquote><p>that are both methods to check the validity of a certificate.</p><blockquote><p><code>http://en.wikipedia.org/wiki/Certificate_revocation_list</code><br />
<code>http://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol</code></p></blockquote><p>Some questions:</p><ul><li>Do you get any error in the browser (please test several tools: IE, Firefox, curl)</li><li>Where did you get the cert from? Your own CA? Self-signed?</li><li>Do you see any request from your browser that might be OCSP or a request for the CRL via HTTP/S or LDAP?</li></ul><p>Can you post the output of the following command?</p><blockquote><p><code>openssl x509 -in yourtcert.pem -text</code><br />
</p></blockquote><p>You need openssl for windows to run this command.</p><blockquote><p><code>http://slproweb.com/download/Win32OpenSSL_Light-1_0_1c.exe</code><br />
</p></blockquote></div><div id="comment-16992-info" class="comment-info"><span class="comment-age">(17 Dec '12, 12:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16999"></span><div id="comment-16999" class="comment"><div id="post-16999-score" class="comment-score"></div><div class="comment-text"><p>In the browser, i didn't get any error. The webapp i'm building in this environement is pretty slow. And sometimes some resources are timedout. The cert is a slef signed cert.</p><p>Also, i know that my cert is out dated. But since the site is still running, i didn't changed it. Can it cause a delay??</p><pre><code>Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 9923774039305754792 (0x89b853e90c1018a8)
    Signature Algorithm: sha1WithRSAEncryption
        Issuer: C=CA, ST=Quebec, L=Montreal, O=Chaire de logiciel libre - Finance sociale et solidaire, CN=testdev.chaire-logiciel-libre.uqam.ca
        Validity
            Not Before: Aug  7 14:27:29 2012 GMT
            Not After : Sep  6 14:27:29 2012 GMT
        Subject: C=CA, ST=Quebec, L=Montreal, O=Chaire de logiciel libre - Finance sociale et solidaire, CN=testdev.chaire-logiciel-libre.uqam.ca
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:b1:ac:86:55:e2:b6:44:e3:a0:5e:51:c7:3d:06:
                    35:02:8c:aa:db:99:7c:f1:bf:9b:18:ff:80:22:ec:
                    fa:ff:93:35:ab:85:66:96:5f:05:2c:4b:09:08:00:
                    70:da:06:75:02:f5:ca:b4:70:ef:f0:a5:28:72:b4:
                    2a:ec:0e:5c:a0:78:eb:8b:85:8a:72:f2:a2:68:2d:
                    3d:5e:bb:ab:52:5b:b3:f2:3e:c2:02:6a:5a:25:a5:
                    65:05:e6:95:ea:5e:1f:38:8c:5e:b3:5a:73:2e:0f:
                    53:8a:78:ce:79:0b:87:b5:94:eb:8e:98:85:ed:32:
                    ee:eb:af:35:ae:0d:07:8f:11:ca:af:b2:6e:f3:fa:
                    0c:a6:d8:62:92:ff:51:01:4d:58:a4:b5:03:42:99:
                    5c:ff:91:26:98:e9:de:8d:3f:86:b8:2b:12:7f:6d:
                    c4:6d:a2:63:2c:3f:93:36:3a:9a:97:be:d5:ba:c0:
                    25:b3:3c:3a:3b:8c:07:b6:f5:cd:86:5a:c2:24:ee:
                    c8:86:ef:d5:e8:f6:14:f9:0c:25:f5:54:60:e4:db:
                    7b:2e:68:9e:b9:cc:58:73:59:b1:1f:bc:48:95:99:
                    94:61:38:20:62:cc:35:51:2a:3f:61:cf:d7:16:dc:
                    b3:57:f9:6e:36:5a:a6:4a:b5:62:4a:a6:12:a7:ce:
                    df:a5
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                F8:4C:5B:39:4D:DC:50:1B:CD:CC:E4:49:ED:3E:80:F7:98:10:A3:65
            X509v3 Authority Key Identifier: 
                keyid:F8:4C:5B:39:4D:DC:50:1B:CD:CC:E4:49:ED:3E:80:F7:98:10:A3:65

            X509v3 Basic Constraints: 
                CA:TRUE
    Signature Algorithm: sha1WithRSAEncryption
         3a:b7:3b:bc:1b:8e:26:80:a4:17:61:5c:bb:b4:4d:06:1e:55:
         a6:3a:a8:0f:09:2b:a2:78:a0:0f:58:aa:30:38:8b:2d:9b:51:
         b8:5d:bc:92:45:8a:53:81:11:4f:0f:3c:50:8c:0a:02:59:12:
         35:67:d5:70:c3:56:51:2c:7b:3e:d9:97:2f:f9:98:3f:b8:45:
         b7:73:ff:1f:9d:14:db:3a:f2:14:66:40:cf:1c:a2:2b:7b:a2:
         77:95:0b:3f:a5:34:22:3a:af:1c:ec:53:31:75:f7:96:4e:25:
         44:c1:f6:04:e5:22:42:28:bd:c8:2a:1c:7a:69:e7:ac:b3:0b:
         13:3a:08:36:56:ed:84:4c:91:1b:eb:26:be:7c:37:e2:1d:17:
         c5:f7:a9:b4:a1:81:b6:2a:2b:28:b6:6c:24:bb:d2:fb:5c:f7:
         f5:de:03:46:d5:3d:b2:ae:55:78:7f:bf:a1:ec:89:35:38:e7:
         08:41:79:84:62:38:14:d8:6f:1b:b6:1c:52:f0:37:87:d9:77:
         b0:3c:59:05:12:eb:ae:3c:dc:cb:bf:e0:b2:f5:8a:9e:47:f5:
         ca:03:11:4b:53:8a:7e:d5:6d:2a:b9:26:b2:2b:1b:3a:b9:0a:
         88:44:9d:d0:6b:0a:ab:00:e8:0c:0e:33:f9:7e:4a:7c:65:bb:
         4e:ba:81:35
-----BEGIN CERTIFICATE-----

I removed the content between those lines

-----END CERTIFICATE-----</code></pre></div><div id="comment-16999-info" class="comment-info"><span class="comment-age">(17 Dec '12, 16:23)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17010"></span><div id="comment-17010" class="comment"><div id="post-17010-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In the browser, i didn't get any error.</p></blockquote><p>as it's a self signed cert, you must have accepted the cert some day.</p><blockquote><p>The webapp i'm building in this environement is pretty slow. And sometimes some resources are timedout. The cert is a slef signed cert.</p></blockquote><p>at the first glance, there nothing special/wrong with this self signed cert.</p><blockquote><p>Also, i know that my cert is out dated. But since the site is still running, i didn't changed it. Can it cause a delay??</p></blockquote><p>I don't think so.</p><p>What about my other questions?</p><ul><li>Did you try different browsers IE, Firefox, Chrome?</li></ul><p>New</p><ul><li>Do you see any error messages in your webserver log?</li><li>Does the application work fast(er) if your just use HTTP?</li><li>Can you post a capture file of a slow connection somewhere?</li><li>Please use Fiddler2 (google it) to analyze the HTTPS requests and responses.</li></ul></div><div id="comment-17010-info" class="comment-info"><span class="comment-age">(18 Dec '12, 00:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17019"></span><div id="comment-17019" class="comment"><div id="post-17019-score" class="comment-score"></div><div class="comment-text"><p>I tryed with chrome, firefox, safari and opera. As i'm using macos i can't test with ie. On the apache server i've got some messages like this [Sun Dec 16 06:47:20 2012] [debug] ssl_engine_io.c(1908): OpenSSL: I/O error, 5 bytes expected to read on BIO#7f612c001340 [mem: 7f612c006c73]</p><p>And i also noticed that for a same session there is multiple handshake. I assume it's the sign of a problem somewhere but i don't know where.</p><p>The application is really faster on plain http.</p><p>I put the dump here <a href="https://docs.google.com/open?id=0B2y0ax8r16GxNHVuUmQzekF3S3c">https://docs.google.com/open?id=0B2y0ax8r16GxNHVuUmQzekF3S3c</a> The ip of the server is 132.208.137.9 I dont't have a copy of windows so i can't use fidler</p></div><div id="comment-17019-info" class="comment-info"><span class="comment-age">(18 Dec '12, 05:16)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17026"></span><div id="comment-17026" class="comment not_top_scorer"><div id="post-17026-score" class="comment-score"></div><div class="comment-text"><p>Following advice founded here</p><p>I wondered if the session cache was working <a href="http://ldp.linux.no/HOWTO/Apache-WebDAV-LDAP-HOWTO/ssl.html">http://ldp.linux.no/HOWTO/Apache-WebDAV-LDAP-HOWTO/ssl.html</a></p><p>This page recommend to try this command</p><pre><code>openssl s_client -connect your.server.dom:443 -state  -reconnect</code></pre><p>The handshake work well but when it try to reconnect here is what i've got drop connection and then reconnect</p><pre><code>CONNECTED(00000003)
1201:error:1408E0F4:SSL routines:SSL3_GET_MESSAGE:unexpected message:/SourceCache/OpenSSL098/OpenSSL098-35.1/src/ssl/s3_both.c:462:</code></pre></div><div id="comment-17026-info" class="comment-info"><span class="comment-age">(18 Dec '12, 06:19)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17028"></span><div id="comment-17028" class="comment not_top_scorer"><div id="post-17028-score" class="comment-score"></div><div class="comment-text"><blockquote><p>[Sun Dec 16 06:47:20 2012] [debug] ssl_engine_io.c(1908): OpenSSL: I/O error, 5 bytes expected to read on BIO#7f612c001340 [mem: 7f612c006c73]</p></blockquote><p>That's not a good sign ;-)</p><p>That message occurs with several apache bugs.</p><blockquote><p><code>https://issues.apache.org/bugzilla/show_bug.cgi?id=46952</code><br />
<code>https://issues.apache.org/bugzilla/show_bug.cgi?id=53193</code></p></blockquote><p>I suggest to use the debugging methods shown in the bug reports to figure out what's going wrong. Please also search google for debugging hints for apache <strong>or</strong> ask in a apache forum. To me it looks like an apache configuration issue (or a bug).</p><blockquote><p>I dont't have a copy of windows so i can't use fidler</p></blockquote><p>What is you client OS? There are similar tools for Linux (<a href="http://portswigger.net/burp/).">http://portswigger.net/burp/).</a></p></div><div id="comment-17028-info" class="comment-info"><span class="comment-age">(18 Dec '12, 06:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17044"></span><div id="comment-17044" class="comment not_top_scorer"><div id="post-17044-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The handshake work well but when it try to reconnect here is what i've got drop connection and then reconnect</p></blockquote><p>Can you please post the whole output of the following command (including the <strong><code>-debug</code></strong> statement)?</p><blockquote><p><code>openssl s_client -debug -connect your.server.dom:443 -state  -reconnect</code></p></blockquote></div><div id="comment-17044-info" class="comment-info"><span class="comment-age">(18 Dec '12, 09:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17062"></span><div id="comment-17062" class="comment not_top_scorer"><div id="post-17062-score" class="comment-score"></div><div class="comment-text"><p>any progress on the <strong><code>-debug</code></strong> output?</p></div><div id="comment-17062-info" class="comment-info"><span class="comment-age">(19 Dec '12, 08:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17095"></span><div id="comment-17095" class="comment not_top_scorer"><div id="post-17095-score" class="comment-score"></div><div class="comment-text"><p>As you mentioned it could be a mis conf of the apache server Here is my site conf</p><pre><code>&lt;IfModule mod_ssl.c&gt;
  # Activer le cache pour éviter de répéter les handshakes
  SSLSessionCache shm:/var/log/apache2/ssl_cache_shm
  # Temps d&#39;expiration du cache en secondes
  SSLSessionCacheTimeout 600
  # SSL Pseudo Random Number Generator
  SSLRandomSeed startup file:/dev/urandom 1024
  SSLRandomSeed connect file:/dev/urandom 1024
  ErrorLog /var/log/apache2/ssl_engine.log
  LogLevel debug
&lt;/IfModule&gt;
&lt;VirtualHost *:80&gt;
ServerAdmin [email protected]
ServerName xxxxx #i removed the value here
# Possible values include: debug, info, notice, warn, error,
# crit, alert, emerg.
LogLevel notice
CustomLog /var/log/apache2/access.log combined
ErrorLog /var/log/apache2/error.log
# Toutes les requetes HTTP sont réacheminées vers HTTPS
#RewriteEngine on
#RewriteCond %{HTTPS} !=on
Redirect permanent / #https:// url is removed#
&lt;/VirtualHost&gt;
# Hote HTTPS
&lt;VirtualHost _default_:443&gt;
ServerName ##url is removed
ServerAdmin [email protected]
# Toutes les requetes sont reacheminees vers Tomcat
# (Voir configuration de mod_jk)
JKMount /* worker1
# Valeurs possibles: debug, info, notice, warn, error,
# crit, alert, emerg
LogLevel debug
ErrorLog /var/log/apache2/error.log
CustomLog /var/log/apache2/ssl_access.log combined
DocumentRoot /var/www
&lt;Directory /&gt;
Options None
Order deny,allow
AllowOverride None
Deny from all
&lt;LimitExcept GET POST PUT OPTIONS&gt;
Order deny,allow
Deny from all
&lt;/LimitExcept&gt;
SSLRequireSSL
&lt;/Directory&gt;
# SSL est activé pour cet hote
SSLEngine on
# Désactiver les proxys SSL
SSLProxyEngine off
SSLOptions +StrictRequire
# Protocole SSL à utiliser
SSLProtocol -all TLSv1 +SSLv3
# Ne prendre en charge que la cryptographie élevée
SSLCipherSuite HIGH:MEDIUM:!aNULL:+SHA1:+MD5:+HIGH:+MEDIUM
# Emplacement de la clé privée et du certificat du serveur
SSLCertificateKeyFile /etc/ssl/private/serveur.key
SSLCertificateFile /etc/ssl/certs/serveur.crt
# Chemin des symlinks vers les certificats valides
SSLCACertificateFile /etc/ssl/certs/serveur.crt
# Chemin des symlinks vers les certificats révoqués
#SSLCARevocationPath /etc/apache2/ssl.crl/
# Exiger des clients de présenter des certificats
# SSLVerifyClient require
# Profondeur de vérification de l&#39;identité de l&#39;émetteur
# des certificats clients
# SSLVerifyDepth 5
# Hack pour Internet Explorer
BrowserMatch &quot;MSIE [2-6]&quot; \
nokeepalive ssl-unclean-shutdown \
downgrade-1.0 force-response-1.0
# MSIE 7 and newer should be able to use keepalive
BrowserMatch &quot;MSIE [17-9]&quot; ssl-unclean-shutdown
&lt;/VirtualHost&gt;</code></pre><p>Any comment would be helpful</p></div><div id="comment-17095-info" class="comment-info"><span class="comment-age">(20 Dec '12, 05:17)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17096"></span><div id="comment-17096" class="comment not_top_scorer"><div id="post-17096-score" class="comment-score"></div><div class="comment-text"><p>well, looks O.K. Can you please post the output of</p><ul><li><code>openssl s_client -debug -connect your.server.dom:443 -state -reconnect</code></li><li>Except the message you already posted, do you see anything in /var/log/apache2/ssl_engine.log</li></ul></div><div id="comment-17096-info" class="comment-info"><span class="comment-age">(20 Dec '12, 06:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17098"></span><div id="comment-17098" class="comment not_top_scorer"><div id="post-17098-score" class="comment-score"></div><div class="comment-text"><p>wait a moment.</p><blockquote><p><code>SSLCACertificateFile /etc/ssl/certs/serveur.crt</code><br />
</p></blockquote><p>Please remove that line from the config and restart apache. Then repeat your tests.</p></div><div id="comment-17098-info" class="comment-info"><span class="comment-age">(20 Dec '12, 06:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17166"></span><div id="comment-17166" class="comment not_top_scorer"><div id="post-17166-score" class="comment-score"></div><div class="comment-text"><p>??? see my comment above your 2nd post of the config.....</p></div><div id="comment-17166-info" class="comment-info"><span class="comment-age">(22 Dec '12, 09:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17186"></span><div id="comment-17186" class="comment not_top_scorer"><div id="post-17186-score" class="comment-score"></div><div class="comment-text"><p>I just test to remove the SSLCACertificateFile But i didnt't see any difference in the response time</p></div><div id="comment-17186-info" class="comment-info"><span class="comment-age">(22 Dec '12, 23:51)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17187"></span><div id="comment-17187" class="comment not_top_scorer"><div id="post-17187-score" class="comment-score"></div><div class="comment-text"><p>When executing the openssl command, nothing is added to the given log file.</p></div><div id="comment-17187-info" class="comment-info"><span class="comment-age">(22 Dec '12, 23:58)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17188"></span><div id="comment-17188" class="comment not_top_scorer"><div id="post-17188-score" class="comment-score"></div><div class="comment-text"><p>can you please post the <strong><code>-debug</code></strong> output here? Without further information I would have to use telepathy ;-)</p></div><div id="comment-17188-info" class="comment-info"><span class="comment-age">(23 Dec '12, 02:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17232"></span><div id="comment-17232" class="comment not_top_scorer"><div id="post-17232-score" class="comment-score"></div><div class="comment-text"><p>Here is my output for the command openssl s_client -debug -connect your.server.dom:443 -state -reconnect</p><pre><code>CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d16570 [0x1d165f0] (226 bytes =&gt; 226 (0xE2))
0000 - 16 03 01 00 dd 01 00 00-d9 03 02 50 d8 58 57 b2   ...........P.XW.
0010 - fd 39 c1 dd 9f 46 9d ae-13 b1 bd be bf 11 ab 6f   .9...F.........o
0020 - 1e ff 6d 05 65 fc 16 57-ae a5 5c 00 00 66 c0 14   ..m.e..W..\..f..
0030 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0040 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0050 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0060 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0070 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
0080 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
0090 - 00 03 00 ff 02 01 00 00-49 00 0b 00 04 03 00 01   ........I.......
00a0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00b0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00c0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00d0 - 02 00 03 00 0f 00 10 00-11 00 23 00 00 00 0f 00   ..........#.....
00e0 - 01 01                                             ..
SSL_connect:unknown state
read from 0x1d16570 [0x1d1bb50] (7 bytes =&gt; 7 (0x7))
0000 - 16 03 02 00 3a 02                                 ....:.
0007 - &lt;SPACES/NULS&gt;
read from 0x1d16570 [0x1d1bb5a] (56 bytes =&gt; 56 (0x38))
0000 - 00 36 03 02 50 d8 58 54-c0 3b 61 d8 85 ea 2b 38   .6..P.XT.;a...+8
0010 - be d2 97 1c fd 5b 62 80-b7 df da 99 29 06 b0 1a   .....[b.....)...
0020 - 80 75 51 fe 00 00 39 00-00 0e ff 01 00 01 00 00   .uQ...9.........
0030 - 23 00 00 00 0f 00 01 01-                          #.......
SSL_connect:SSLv3 read server hello A
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 04 29                                    ....)
read from 0x1d16570 [0x1d1bb58] (1065 bytes =&gt; 1065 (0x429))
0000 - 0b 00 04 25 00 04 22 00-04 1f 30 82 04 1b 30 82   ...%..&quot;...0...0.
0010 - 03 03 a0 03 02 01 02 02-09 00 89 b8 53 e9 0c 10   ............S...
0020 - 18 a8 30 0d 06 09 2a 86-48 86 f7 0d 01 01 05 05   ..0...*.H.......
0030 - 00 30 81 a3 31 0b 30 09-06 03 55 04 06 13 02 43   .0..1.0...U....C
0040 - 41 31 0f 30 0d 06 03 55-04 08 0c 06 51 75 65 62   A1.0...U....Queb
0050 - 65 63 31 11 30 0f 06 03-55 04 07 0c 08 4d 6f 6e   ec1.0...U....Mon
0060 - 74 72 65 61 6c 31 40 30-3e 06 03 55 04 0a 0c 37   [email protected]&gt;..U...7
0070 - 43 68 61 69 72 65 20 64-65 20 6c 6f 67 69 63 69   Chaire de logici
0080 - 65 6c 20 6c 69 62 72 65-20 2d 20 46 69 6e 61 6e   el libre - Finan
0090 - 63 65 20 73 6f 63 69 61-6c 65 20 65 74 20 73 6f   ce sociale et so
00a0 - 6c 69 64 61 69 72 65 31-2e 30 2c 06 03 55 04 03   lidaire1.0,..U..
00b0 - 0c 25 74 65 73 74 64 65-76 2e 63 68 61 69 72 65   .%server
00c0 - 2d 6c 6f 67 69 63 69 65-6c 2d 6c 69 62 72 65 2e   name
00d0 - 75 71 61 6d 2e 63 61 30-1e 17 0d 31 32 30 38 30   is hidden0...12080
00e0 - 37 31 34 32 37 32 39 5a-17 0d 31 32 30 39 30 36   7142729Z..120906
00f0 - 31 34 32 37 32 39 5a 30-81 a3 31 0b 30 09 06 03   142729Z0..1.0...
0100 - 55 04 06 13 02 43 41 31-0f 30 0d 06 03 55 04 08   U....CA1.0...U..
0110 - 0c 06 51 75 65 62 65 63-31 11 30 0f 06 03 55 04   ..Quebec1.0...U.
0120 - 07 0c 08 4d 6f 6e 74 72-65 61 6c 31 40 30 3e 06   [email protected]&gt;.
0130 - 03 55 04 0a 0c 37 43 68-61 69 72 65 20 64 65 20   .U...7Chaire de 
0140 - 6c 6f 67 69 63 69 65 6c-20 6c 69 62 72 65 20 2d   logiciel libre -
0150 - 20 46 69 6e 61 6e 63 65-20 73 6f 63 69 61 6c 65    Finance sociale
0160 - 20 65 74 20 73 6f 6c 69-64 61 69 72 65 31 2e 30    et solidaire1.0
0170 - 2c 06 03 55 04 03 0c 25-74 65 73 74 64 65 76 2e   ,..U...%server
0180 - 63 68 61 69 72 65 2d 6c-6f 67 69 63 69 65 6c 2d   name is 
0190 - 6c 69 62 72 65 2e 75 71-61 6d 2e 63 61 30 82 01   hidden0..
01a0 - 22 30 0d 06 09 2a 86 48-86 f7 0d 01 01 01 05 00   &quot;0...*.H........
01b0 - 03 82 01 0f 00 30 82 01-0a 02 82 01 01 00 b1 ac   .....0..........
01c0 - 86 55 e2 b6 44 e3 a0 5e-51 c7 3d 06 35 02 8c aa   .U..D..^Q.=.5...
01d0 - db 99 7c f1 bf 9b 18 ff-80 22 ec fa ff 93 35 ab   ..|......&quot;....5.
01e0 - 85 66 96 5f 05 2c 4b 09-08 00 70 da 06 75 02 f5   .f._.,K...p..u..
01f0 - ca b4 70 ef f0 a5 28 72-b4 2a ec 0e 5c a0 78 eb   ..p...(r.*..\.x.
0200 - 8b 85 8a 72 f2 a2 68 2d-3d 5e bb ab 52 5b b3 f2   ...r..h-=^..R[..
0210 - 3e c2 02 6a 5a 25 a5 65-05 e6 95 ea 5e 1f 38 8c   &gt;..jZ%.e....^.8.
0220 - 5e b3 5a 73 2e 0f 53 8a-78 ce 79 0b 87 b5 94 eb   ^.Zs..S.x.y.....
0230 - 8e 98 85 ed 32 ee eb af-35 ae 0d 07 8f 11 ca af   ....2...5.......
0240 - b2 6e f3 fa 0c a6 d8 62-92 ff 51 01 4d 58 a4 b5   .n.....b..Q.MX..
0250 - 03 42 99 5c ff 91 26 98-e9 de 8d 3f 86 b8 2b 12   .B.\..&amp;....?..+.
0260 - 7f 6d c4 6d a2 63 2c 3f-93 36 3a 9a 97 be d5 ba   .m.m.c,?.6:.....
0270 - c0 25 b3 3c 3a 3b 8c 07-b6 f5 cd 86 5a c2 24 ee   .%.&lt;:;......Z.$.
0280 - c8 86 ef d5 e8 f6 14 f9-0c 25 f5 54 60 e4 db 7b   .........%.T`..{
0290 - 2e 68 9e b9 cc 58 73 59-b1 1f bc 48 95 99 94 61   .h...XsY...H...a
02a0 - 38 20 62 cc 35 51 2a 3f-61 cf d7 16 dc b3 57 f9   8 b.5Q*?a.....W.
02b0 - 6e 36 5a a6 4a b5 62 4a-a6 12 a7 ce df a5 02 03   n6Z.J.bJ........
02c0 - 01 00 01 a3 50 30 4e 30-1d 06 03 55 1d 0e 04 16   ....P0N0...U....
02d0 - 04 14 f8 4c 5b 39 4d dc-50 1b cd cc e4 49 ed 3e   ...L[9M.P....I.&gt;
02e0 - 80 f7 98 10 a3 65 30 1f-06 03 55 1d 23 04 18 30   .....e0...U.#..0
02f0 - 16 80 14 f8 4c 5b 39 4d-dc 50 1b cd cc e4 49 ed   ....L[9M.P....I.
0300 - 3e 80 f7 98 10 a3 65 30-0c 06 03 55 1d 13 04 05   &gt;.....e0...U....
0310 - 30 03 01 01 ff 30 0d 06-09 2a 86 48 86 f7 0d 01   0....0...*.H....
0320 - 01 05 05 00 03 82 01 01-00 3a b7 3b bc 1b 8e 26   .........:.;...&amp;
0330 - 80 a4 17 61 5c bb b4 4d-06 1e 55 a6 3a a8 0f 09   ...a\..M..U.:...
0340 - 2b a2 78 a0 0f 58 aa 30-38 8b 2d 9b 51 b8 5d bc   +.x..X.08.-.Q.].
0350 - 92 45 8a 53 81 11 4f 0f-3c 50 8c 0a 02 59 12 35   .E.S..O.&lt;P...Y.5
0360 - 67 d5 70 c3 56 51 2c 7b-3e d9 97 2f f9 98 3f b8   g.p.VQ,{&gt;../..?.
0370 - 45 b7 73 ff 1f 9d 14 db-3a f2 14 66 40 cf 1c a2   E.s.....:[email protected]
0380 - 2b 7b a2 77 95 0b 3f a5-34 22 3a af 1c ec 53 31   +{.w..?.4&quot;:...S1
0390 - 75 f7 96 4e 25 44 c1 f6-04 e5 22 42 28 bd c8 2a   u..N%D....&quot;B(..*
03a0 - 1c 7a 69 e7 ac b3 0b 13-3a 08 36 56 ed 84 4c 91   .zi.....:.6V..L.
03b0 - 1b eb 26 be 7c 37 e2 1d-17 c5 f7 a9 b4 a1 81 b6   ..&amp;.|7..........
03c0 - 2a 2b 28 b6 6c 24 bb d2-fb 5c f7 f5 de 03 46 d5   *+(.l$...\....F.
03d0 - 3d b2 ae 55 78 7f bf a1-ec 89 35 38 e7 08 41 79   =..Ux.....58..Ay
03e0 - 84 62 38 14 d8 6f 1b b6-1c 52 f0 37 87 d9 77 b0   .b8..o...R.7..w.
03f0 - 3c 59 05 12 eb ae 3c dc-cb bf e0 b2 f5 8a 9e 47   &lt;Y....&lt;........G
0400 - f5 ca 03 11 4b 53 8a 7e-d5 6d 2a b9 26 b2 2b 1b   ....KS.~.m*.&amp;.+.
0410 - 3a b9 0a 88 44 9d d0 6b-0a ab 00 e8 0c 0e 33 f9   :...D..k......3.
0420 - 7e 4a 7c 65 bb 4e ba 81-35                        ~J|e.N..5
depth=0 C = FR, ST = region, L = city, O = organisation, CN = server name is hidden
verify error:num=18:self signed certificate
verify return:1
depth=0 C = FR, ST = region, L =city, O = org, CN = server name is hidden
verify error:num=10:certificate has expired
notAfter=Sep  6 14:27:29 2012 GMT
verify return:1
depth=0 C = FR, ST = Region, L = city, O = org, CN = server name is hidden
notAfter=Sep  6 14:27:29 2012 GMT
verify return:1
SSL_connect:SSLv3 read server certificate A
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 02 0d                                    .....
read from 0x1d16570 [0x1d1bb58] (525 bytes =&gt; 525 (0x20D))
0000 - 0c 00 02 09 00 80 d6 7d-e4 40 cb bb dc 19 36 d6   .......}[email protected]
0010 - 93 d3 4a fd 0a d5 0c 84-d2 39 a4 5f 52 0b b8 81   ..J......9._R...
0020 - 74 cb 98 bc e9 51 84 9f-91 2e 63 9c 72 fb 13 b4   t....Q....c.r...
0030 - b4 d7 17 7e 16 d5 5a c1-79 ba 42 0b 2a 29 fe 32   ...~..Z.y.B.*).2
0040 - 4a 46 7a 63 5e 81 ff 59-01 37 7b ed dc fd 33 16   JFzc^..Y.7{...3.
0050 - 8a 46 1a ad 3b 72 da e8-86 00 78 04 5b 07 a7 db   .F..;r....x.[...
0060 - ca 78 74 08 7d 15 10 ea-9f cc 9d dd 33 05 07 dd   .xt.}.......3...
0070 - 62 db 88 ae aa 74 7d e0-f4 d6 e2 bd 68 b0 e7 39   b....t}.....h..9
0080 - 3e 0f 24 21 8e b3 00 01-02 00 80 5e a6 39 f3 85   &gt;.$!.......^.9..
0090 - a9 67 9e 2d b2 ed 1b 70-3c ed 52 36 27 e3 b4 75   .g.-...p&lt;.R6&#39;..u
00a0 - 14 a2 b8 66 01 66 86 62-a3 53 5b be a2 66 40 7a   ...f.f.b.S[[email protected]
00b0 - b4 b6 da 43 bd 61 f4 2b-7e 4b 34 c3 27 3e fc 07   ...C.a.+~K4.&#39;&gt;..
00c0 - a6 12 c5 f0 2a e3 28 94-aa 4a f1 a4 ea d1 6f ea   ....*.(..J....o.
00d0 - 94 c7 19 dd 1b ab e1 c9-61 48 2a 24 61 e0 33 6b   ........aH*$a.3k
00e0 - 5d 81 77 4c ff b1 04 77-0a 5c d9 b6 bd 54 fa d5   ].wL...w.\...T..
00f0 - 86 ad 5a 01 ba 15 c7 fa-29 b5 cb e8 ec 57 14 f0   ..Z.....)....W..
0100 - 1f b6 6f 2f 8e ff 67 a9-d1 36 6b 01 00 68 c6 62   ..o/..g..6k..h.b
0110 - cc 7c b6 10 98 d7 c7 e5-80 e7 c0 ac 38 01 3c 0d   .|..........8.&lt;.
0120 - 7b d0 47 50 a4 38 5a 87-eb 44 01 7d f1 e3 7f 08   {.GP.8Z..D.}....
0130 - 55 fc 7f 93 32 b8 dd 1a-7f 1e ee 58 e0 25 65 ab   U...2......X.%e.
0140 - f9 5d bb a6 e3 e3 53 1f-ed 81 60 45 15 cd 72 c8   .]....S...`E..r.
0150 - 17 66 9f 00 09 bd 41 c2-ca c8 a1 73 c6 73 62 b6   .f....A....s.sb.
0160 - 21 66 05 c1 cc 84 f1 cd-ef b0 be ea 0d 5b 44 54   !f...........[DT
0170 - b8 71 c9 16 93 5d a0 8a-01 2d 47 3b 19 54 48 cb   .q...]...-G;.TH.
0180 - 13 9e a3 af 1f e2 0c 60-ab 0e 99 ad 3d 64 54 79   .......`....=dTy
0190 - e8 f8 96 55 66 1a 70 05-ff 40 f9 b0 b9 b6 29 ab   [email protected]).
01a0 - 4a d5 b6 a3 7d 5b e7 25-7c f1 ac 5a 7e 56 bd d8   J...}[.%|..Z~V..
01b0 - d9 b4 65 a4 78 82 36 1a-ae 83 04 85 3c 3d 1e 05   ..e.x.6.....&lt;=..
01c0 - 1c 9a d8 82 53 34 30 bf-10 53 cd 5f a6 ff 7f ff   ....S40..S._....
01d0 - 52 d4 38 a8 80 3f cd ad-2e 61 8c 4b 3b 59 34 72   R.8..?...a.K;Y4r
01e0 - 3e 5f 89 99 2b d5 f7 03-38 83 77 3d 0d e7 85 6b   &gt;_..+...8.w=...k
01f0 - 49 c2 06 a9 8f ac 73 55-a0 bb bb 09 eb 29 5c 5c   I.....sU.....)\\
0200 - 7c 1d 5f ee b6 82 8c 77-15 a7 54 0f 48            |._....w..T.H
SSL_connect:SSLv3 read server key exchange A
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 04                                    .....
read from 0x1d16570 [0x1d1bb58] (4 bytes =&gt; 4 (0x4))
0000 - 0e                                                .
0004 - &lt;SPACES/NULS&gt;
SSL_connect:SSLv3 read server done A
write to 0x1d16570 [0x1d258e0] (139 bytes =&gt; 139 (0x8B))
0000 - 16 03 02 00 86 10 00 00-82 00 80 37 8d 68 38 a2   ...........7.h8.
0010 - 93 6c fb da b5 72 07 11-20 46 48 ef 70 4b ad 32   .l...r.. FH.pK.2
0020 - 5b ad 82 6b 27 54 7c b9-9a 4d b5 96 0f bc 5b 5a   [..k&#39;T|..M....[Z
0030 - 32 8e e4 e5 0d 6e d6 d6-24 3d 11 7b d4 80 da db   2....n..$=.{....
0040 - ee 74 30 43 cf 56 91 cd-8c a3 fc cb 8d 65 27 00   .t0C.V.......e&#39;.
0050 - 75 9e 21 84 33 a6 14 21-85 b1 d1 d0 1c 2d 6b f6   u.!.3..!.....-k.
0060 - f2 f1 ce fe a5 b9 c0 5f-14 9e 92 93 80 a4 7e 75   ......._......~u
0070 - 11 80 58 58 d9 11 85 6f-5d 18 22 4a 89 e2 35 06   ..XX...o].&quot;J..5.
0080 - 3b 91 2b 4c 78 63 fe b2-65 85 5f                  ;.+Lxc..e._
SSL_connect:SSLv3 write client key exchange A
write to 0x1d16570 [0x1d258e0] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d16570 [0x1d258e0] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 bc cd 08-e4 e1 69 49 02 5f 55 d1   [email protected]_U.
0010 - 5e b3 4a a1 1f ab f5 89-e1 fd 20 54 43 a5 81 2c   ^.J....... TC..,
0020 - e2 d6 94 bf 80 aa 64 79-c5 eb 1a c2 b5 93 fa 13   ......dy........
0030 - 57 fe 77 34 f3 26 cd a2-f1 16 cd c8 01 d2 3c ca   W.w4.&amp;........&lt;.
0040 - b5 a2 73 bc 6c                                    ..s.l
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 ca                                    .....
read from 0x1d16570 [0x1d1bb58] (202 bytes =&gt; 202 (0xCA))
0000 - 04 00 00 c6 00 00 01 2c-00 c0 e7 6f e6 e3 6b 8d   .......,...o..k.
0010 - 30 8e 73 e7 97 38 a5 2e-8c 5d 04 a6 52 50 4f 34   0.s..8...]..RPO4
0020 - db 25 67 b6 7f 39 a3 0b-77 de e4 f6 71 a5 c6 46   .%g..9..w...q..F
0030 - d6 71 a3 6d e0 4c a1 7f-b4 ee e2 8c 56 a4 f0 d2   .q.m.L......V...
0040 - 22 ab 36 67 8a 68 da 37-98 4d d3 8c 57 4f 85 b7   &quot;.6g.h.7.M..WO..
0050 - 4a 2a bf fc c9 c8 31 16-a2 93 3d fc 04 8d 90 9f   J*....1...=.....
0060 - bd 29 e3 a6 56 10 b4 45-c4 76 15 53 86 c8 e3 59   .)..V..E.v.S...Y
0070 - 72 fe 7c 47 a1 cb f1 b7-9a 87 d8 db 46 53 9a f4   r.|G........FS..
0080 - 51 3f 47 27 22 5c 6c a7-0f 10 f8 49 f0 84 f7 00   Q?G&#39;&quot;\l....I....
0090 - bd 05 73 4d 49 4a 80 55-4d 0e e3 ae 57 a4 86 ca   ..sMIJ.UM...W...
00a0 - 9b 5f d0 80 59 aa bd c0-cf cd 9f 9d 1f 37 3b 98   ._..Y........7;.
00b0 - 29 8d 88 85 39 6b 39 8b-3b a9 39 d5 eb 2c 98 81   )...9k9.;.9..,..
00c0 - 5a e6 28 dd 07 61 4e 8b-5b f4                     Z.(..aN.[.
SSL_connect:SSLv3 read server session ticket A
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d16570 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d16570 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d16570 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - d4 41 7d 8a c6 7d 69 c6-87 19 e3 03 f5 fc 55 90   .A}..}i.......U.
0010 - 8d 89 cf e3 23 23 3e 35-7c 33 02 ed e3 aa ae 32   ....##&gt;5|3.....2
0020 - 68 6e 0a b2 a4 79 98 46-82 b3 1c c1 79 9e 6d f2   hn...y.F....y.m.
0030 - a8 74 4d c0 2c eb c5 80-af 47 e8 34 0a 7d 18 4a   .tM.,....G.4.}.J
SSL_connect:SSLv3 read finished A
---
Certificate chain
 0 s:/C=FR/ST=Region/L=City/O=organisation /CN=server name is hidden
   i:/C=FR/ST=Region/L=City/O=organization/CN=server name is hidden
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEGzCCAwOgAwIBAgIJAIm4U+kMEBioMA0GCSqGSIb3DQEBBQUAMIGjMQswCQYD
VQQGEwJDQTEPMA0GA1UECAwGUXVlYmVjMREwDwYDVQQHDAhNb250cmVhbDFAMD4G
A1UECgw3Q2hhaXJlIGRlIGxvZ2ljaWVsIGxpYnJlIC0gRmluYW5jZSBzb2NpYWxl
IGV0IHNvbGlkYWlyZTEuMCwGA1UEAwwldGVzdGRldi5jaGFpcmUtbG9naWNpZWwt
bGlicmUudXFhbS5jYTAeFw0xMjA4MDcxNDI3MjlaFw0xMjA5MDYxNDI3MjlaMIGj
MQswCQYDVQQGEwJDQTEPMA0GA1UECAwGUXVlYmVjMREwDwYDVQQHDAhNb250cmVh
bDFAMD4GA1UECgw3Q2hhaXJlIGRlIGxvZ2ljaWVsIGxpYnJlIC0gRmluYW5jZSBz
b2NpYWxlIGV0IHNvbGlkYWlyZTEuMCwGA1UEAwwldGVzdGRldi5jaGFpcmUtbG9n
aWNpZWwtbGlicmUudXFhbS5jYTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBALGshlXitkTjoF5Rxz0GNQKMqtuZfPG/mxj/gCLs+v+TNauFZpZfBSxLCQgA
cNoGdQL1yrRw7/ClKHK0KuwOXKB464uFinLyomgtPV67q1Jbs/I+wgJqWiWlZQXm
lepeHziMXrNacy4PU4p4znkLh7WU646Yhe0y7uuvNa4NB48Ryq+ybvP6DKbYYpL/
UQFNWKS1A0KZXP+RJpjp3o0/hrgrEn9txG2iYyw/kzY6mpe+1brAJbM8OjuMB7b1
zYZawiTuyIbv1ej2FPkMJfVUYOTbey5onrnMWHNZsR+8SJWZlGE4IGLMNVEqP2HP
1xbcs1f5bjZapkq1YkqmEqfO36UCAwEAAaNQME4wHQYDVR0OBBYEFPhMWzlN3FAb
zczkSe0+gPeYEKNlMB8GA1UdIwQYMBaAFPhMWzlN3FAbzczkSe0+gPeYEKNlMAwG
A1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBADq3O7wbjiaApBdhXLu0TQYe
VaY6qA8JK6J4oA9YqjA4iy2bUbhdvJJFilOBEU8PPFCMCgJZEjVn1XDDVlEsez7Z
ly/5mD+4Rbdz/x+dFNs68hRmQM8coit7oneVCz+lNCI6rxzsUzF195ZOJUTB9gTl
IkIovcgqHHpp56yzCxM6CDZW7YRMkRvrJr58N+IdF8X3qbShgbYqKyi2bCS70vtc
9/XeA0bVPbKuVXh/v6HsiTU45whBeYRiOBTYbxu2HFLwN4fZd7A8WQUS66483Mu/
4LL1ip5H9coDEUtTin7VbSq5JrIrGzq5CohEndBrCqsA6AwOM/l+Snxlu066gTU=
-----END CERTIFICATE-----
subject=/C=FR/ST=Region/L=City/O=org/CN=server name is hidden
issuer=/C=fr/ST=REGION/L=City/O=orgnisation /CN=server name is hidden
---
No client certificate CA names sent
---
SSL handshake has read 1954 bytes and written 440 bytes
---
New, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
drop connection and then reconnect
write to 0x1d16570 [0x1d200a3] (53 bytes =&gt; 53 (0x35))
0000 - 15 03 02 00 30 d3 c6 6c-e6 04 90 4f 19 ea 8f 73   ....0..l...O...s
0010 - ff 0d fa 3d 67 4b 41 50-eb 06 06 fe 97 91 0a c4   ...=gKAP........
0020 - 57 42 a7 1a 60 20 f7 f6-c2 ea fa e3 1b a1 f8 c1   WB..` ..........
0030 - 07 98 47 da 2b                                    ..G.+
SSL3 alert write:warning:close notify
CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d2a770 [0x1d200a3] (450 bytes =&gt; 450 (0x1C2))
0000 - 16 03 01 01 bd 01 00 01-b9 03 02 50 d8 58 57 af   ...........P.XW.
0010 - f3 8b 45 91 8a 93 ca 31-95 30 70 13 9b 97 ab 89   ..E....1.0p.....
0020 - 55 51 ae b9 a0 d6 5f 98-e4 f2 a2 20 ef 64 0a d6   UQ...._.... .d..
0030 - b2 18 4a 2f 48 44 e1 64-d5 f1 19 0b 8c 59 06 4b   ..J/HD.d.....Y.K
0040 - cd 78 ce 51 34 85 7c 2b-e0 30 96 df 00 66 c0 14   .x.Q4.|+.0...f..
0050 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0060 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0070 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0080 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0090 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
00a0 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
00b0 - 00 03 00 ff 02 01 00 01-09 00 0b 00 04 03 00 01   ................
00c0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00d0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00e0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00f0 - 02 00 03 00 0f 00 10 00-11 00 23 00 c0 e7 6f e6   ..........#...o.
0100 - e3 6b 8d 30 8e 73 e7 97-38 a5 2e 8c 5d 04 a6 52   .k.0.s..8...]..R
0110 - 50 4f 34 db 25 67 b6 7f-39 a3 0b 77 de e4 f6 71   PO4.%g..9..w...q
0120 - a5 c6 46 d6 71 a3 6d e0-4c a1 7f b4 ee e2 8c 56   ..F.q.m.L......V
0130 - a4 f0 d2 22 ab 36 67 8a-68 da 37 98 4d d3 8c 57   ...&quot;.6g.h.7.M..W
0140 - 4f 85 b7 4a 2a bf fc c9-c8 31 16 a2 93 3d fc 04   O..J*....1...=..
0150 - 8d 90 9f bd 29 e3 a6 56-10 b4 45 c4 76 15 53 86   ....)..V..E.v.S.
0160 - c8 e3 59 72 fe 7c 47 a1-cb f1 b7 9a 87 d8 db 46   ..Yr.|G........F
0170 - 53 9a f4 51 3f 47 27 22-5c 6c a7 0f 10 f8 49 f0   S..Q?G&#39;&quot;\l....I.
0180 - 84 f7 00 bd 05 73 4d 49-4a 80 55 4d 0e e3 ae 57   .....sMIJ.UM...W
0190 - a4 86 ca 9b 5f d0 80 59-aa bd c0 cf cd 9f 9d 1f   ...._..Y........
01a0 - 37 3b 98 29 8d 88 85 39-6b 39 8b 3b a9 39 d5 eb   7;.)...9k9.;.9..
01b0 - 2c 98 81 5a e6 28 dd 07-61 4e 8b 5b f4 00 0f 00   ,..Z.(..aN.[....
01c0 - 01 01                                             ..
SSL_connect:SSLv3 write client hello A
read from 0x1d2a770 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 56                                    ....V
read from 0x1d2a770 [0x1d1bb58] (86 bytes =&gt; 86 (0x56))
0000 - 02 00 00 52 03 02 50 d8-58 54 de e8 f6 1f 57 8e   ...R..P.XT....W.
0010 - 90 9c b1 ba 1c e4 1d 17-61 60 7a 42 7a c1 3a 41   ........a`zBz.:A
0020 - 00 3d a1 5f 0a 7d 20 ef-64 0a d6 b2 18 4a 2f 48   .=._.} .d....J/H
0030 - 44 e1 64 d5 f1 19 0b 8c-59 06 4b cd 78 ce 51 34   D.d.....Y.K.x.Q4
0040 - 85 7c 2b e0 30 96 df 00-39 00 00 0a ff 01 00 01   .|+.0...9.......
0050 - 00 00 0f 00 01 01                                 ......
SSL_connect:SSLv3 read server hello A
read from 0x1d2a770 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d2a770 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d2a770 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d2a770 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - 06 c5 6c a5 9c ee 85 1b-24 62 f6 c9 15 63 57 9d   ..l.....$b...cW.
0010 - 79 14 1f b5 4d f7 30 67-db c2 1f 7a c8 71 a7 19   y...M.0g...z.q..
0020 - 4c 8f ce b1 18 8f ca 47-40 81 7b 0c 80 06 d7 fe   [email protected]{.....
0030 - a3 db 98 a6 d0 bd 48 72-89 d1 82 47 5c 7c 5e ee   ......Hr...G\|^.
SSL_connect:SSLv3 read finished A
write to 0x1d2a770 [0x1d25830] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d2a770 [0x1d25830] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 62 42 2e-40 6a 66 13 ca 2a df 85   ....@bB.@jf..*..
0010 - f3 3e 56 93 ef 7f fd 29-e8 e7 d2 f0 4c ac 50 c3   .&gt;V....)....L.P.
0020 - eb 3c ff 69 dd fb fb 8c-49 1c 30 01 aa fb 5f 9c   .&lt;.i....I.0..._.
0030 - c6 34 3e 45 d9 af b9 f5-a4 99 de 4d 2d 28 09 2a   .4&gt;E.......M-(.*
0040 - 83 99 30 ca 0c                                    ..0..
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
---
Reused, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
drop connection and then reconnect
write to 0x1d2a770 [0x1d200a3] (53 bytes =&gt; 53 (0x35))
0000 - 15 03 02 00 30 e0 58 d6-f0 a5 79 6b 22 5a 50 3a   ....0.X...yk&quot;ZP:
0010 - 71 0b f3 98 03 bd 11 e1-8b 9c 53 89 cf 5e c7 f8   q.........S..^..
0020 - 89 4e a8 08 89 f8 66 f5-ba db 39 bb ec 41 b7 e3   .N....f...9..A..
0030 - 6c e5 ff b3 bb                                    l....
SSL3 alert write:warning:close notify
CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d1bad0 [0x1d200a3] (450 bytes =&gt; 450 (0x1C2))
0000 - 16 03 01 01 bd 01 00 01-b9 03 02 50 d8 58 57 f9   ...........P.XW.
0010 - 61 73 71 a8 c2 91 b5 b2-df 93 e3 20 ca ce d6 37   asq........ ...7
0020 - 5f fb de 92 35 c7 2f 08-67 bd 49 20 ef 64 0a d6   _...5./.g.I .d..
0030 - b2 18 4a 2f 48 44 e1 64-d5 f1 19 0b 8c 59 06 4b   ..J/HD.d.....Y.K
0040 - cd 78 ce 51 34 85 7c 2b-e0 30 96 df 00 66 c0 14   .x.Q4.|+.0...f..
0050 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0060 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0070 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0080 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0090 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
00a0 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
00b0 - 00 03 00 ff 02 01 00 01-09 00 0b 00 04 03 00 01   ................
00c0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00d0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00e0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00f0 - 02 00 03 00 0f 00 10 00-11 00 23 00 c0 e7 6f e6   ..........#...o.
0100 - e3 6b 8d 30 8e 73 e7 97-38 a5 2e 8c 5d 04 a6 52   .k.0.s..8...]..R
0110 - 50 4f 34 db 25 67 b6 7f-39 a3 0b 77 de e4 f6 71   PO4.%g..9..w...q
0120 - a5 c6 46 d6 71 a3 6d e0-4c a1 7f b4 ee e2 8c 56   ..F.q.m.L......V
0130 - a4 f0 d2 22 ab 36 67 8a-68 da 37 98 4d d3 8c 57   ...&quot;.6g.h.7.M..W
0140 - 4f 85 b7 4a 2a bf fc c9-c8 31 16 a2 93 3d fc 04   O..J*....1...=..
0150 - 8d 90 9f bd 29 e3 a6 56-10 b4 45 c4 76 15 53 86   ....)..V..E.v.S.
0160 - c8 e3 59 72 fe 7c 47 a1-cb f1 b7 9a 87 d8 db 46   ..Yr.|G........F
0170 - 53 9a f4 51 3f 47 27 22-5c 6c a7 0f 10 f8 49 f0   S..Q?G&#39;&quot;\l....I.
0180 - 84 f7 00 bd 05 73 4d 49-4a 80 55 4d 0e e3 ae 57   .....sMIJ.UM...W
0190 - a4 86 ca 9b 5f d0 80 59-aa bd c0 cf cd 9f 9d 1f   ...._..Y........
01a0 - 37 3b 98 29 8d 88 85 39-6b 39 8b 3b a9 39 d5 eb   7;.)...9k9.;.9..
01b0 - 2c 98 81 5a e6 28 dd 07-61 4e 8b 5b f4 00 0f 00   ,..Z.(..aN.[....
01c0 - 01 01                                             ..
SSL_connect:SSLv3 write client hello A
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 56                                    ....V
read from 0x1d1bad0 [0x1d1bb58] (86 bytes =&gt; 86 (0x56))
0000 - 02 00 00 52 03 02 50 d8-58 54 e4 ec 17 34 47 a3   ...R..P.XT...4G.
0010 - bb 5a 22 01 7c 7d 90 ff-f0 1c 68 63 05 96 7c 30   .Z&quot;.|}....hc..|0
0020 - 62 be 21 df d4 a5 20 ef-64 0a d6 b2 18 4a 2f 48   b.!... .d....J/H
0030 - 44 e1 64 d5 f1 19 0b 8c-59 06 4b cd 78 ce 51 34   D.d.....Y.K.x.Q4
0040 - 85 7c 2b e0 30 96 df 00-39 00 00 0a ff 01 00 01   .|+.0...9.......
0050 - 00 00 0f 00 01 01                                 ......
SSL_connect:SSLv3 read server hello A
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d1bad0 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d1bad0 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - f4 41 b5 ea b2 7d ae df-39 99 80 78 f3 e8 de 4b   .A...}..9..x...K
0010 - 7d 07 3d ba 59 95 a3 8b-42 e0 d3 c2 03 0b cf 30   }.=.Y...B......0
0020 - 6f d3 15 d2 4b 34 56 46-8a 70 cd bd 1d fd f8 46   o...K4VF.p.....F
0030 - 25 39 24 81 3c 30 1b 11-80 21 ca 57 c6 b0 fc c5   %9$.&lt;0...!.W....
SSL_connect:SSLv3 read finished A
write to 0x1d1bad0 [0x1d25830] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d1bad0 [0x1d25830] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 db 10 93-62 6c 44 d1 20 25 f5 a4   [email protected] %..
0010 - 2c 72 a3 05 4b 0c 03 69-3d b8 39 b0 95 0a 5c ab   ,r..K..i=.9...\.
0020 - ae 37 39 c2 56 b7 3f 7b-f3 54 c2 5e 6e 70 7b ea   .79.V.?{.T.^np{.
0030 - 96 6a ed 88 e0 a9 ef 4d-46 75 a7 ef b8 3d a5 2a   .j.....MFu...=.*
0040 - 5a 76 fb 52 c5                                    Zv.R.
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
---
Reused, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
drop connection and then reconnect
write to 0x1d1bad0 [0x1d200a3] (53 bytes =&gt; 53 (0x35))
0000 - 15 03 02 00 30 b6 78 ae-0c 39 a0 87 02 b1 0d cf   ....0.x..9......
0010 - 7b 6b d9 1c 32 ca 2c 89-b0 03 a0 b6 62 87 fc 4a   {k..2.,.....b..J
0020 - bc 3b 31 0f 7b 3f 65 c0-cb e8 01 2e 89 04 b2 95   .;1.{?e.........
0030 - 3d b6 ed d1 7b                                    =...{
SSL3 alert write:warning:close notify
CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d26a60 [0x1d200a3] (450 bytes =&gt; 450 (0x1C2))
0000 - 16 03 01 01 bd 01 00 01-b9 03 02 50 d8 58 57 f3   ...........P.XW.
0010 - ad 0c 7e 11 21 1a 32 e7-77 48 0e 41 fa 3d 67 20   ..~.!.2.wH.A.=g 
0020 - 68 ae 75 1a c5 9b ec 56-0e bb 63 20 ef 64 0a d6   h.u....V..c .d..
0030 - b2 18 4a 2f 48 44 e1 64-d5 f1 19 0b 8c 59 06 4b   ..J/HD.d.....Y.K
0040 - cd 78 ce 51 34 85 7c 2b-e0 30 96 df 00 66 c0 14   .x.Q4.|+.0...f..
0050 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0060 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0070 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0080 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0090 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
00a0 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
00b0 - 00 03 00 ff 02 01 00 01-09 00 0b 00 04 03 00 01   ................
00c0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00d0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00e0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00f0 - 02 00 03 00 0f 00 10 00-11 00 23 00 c0 e7 6f e6   ..........#...o.
0100 - e3 6b 8d 30 8e 73 e7 97-38 a5 2e 8c 5d 04 a6 52   .k.0.s..8...]..R
0110 - 50 4f 34 db 25 67 b6 7f-39 a3 0b 77 de e4 f6 71   PO4.%g..9..w...q
0120 - a5 c6 46 d6 71 a3 6d e0-4c a1 7f b4 ee e2 8c 56   ..F.q.m.L......V
0130 - a4 f0 d2 22 ab 36 67 8a-68 da 37 98 4d d3 8c 57   ...&quot;.6g.h.7.M..W
0140 - 4f 85 b7 4a 2a bf fc c9-c8 31 16 a2 93 3d fc 04   O..J*....1...=..
0150 - 8d 90 9f bd 29 e3 a6 56-10 b4 45 c4 76 15 53 86   ....)..V..E.v.S.
0160 - c8 e3 59 72 fe 7c 47 a1-cb f1 b7 9a 87 d8 db 46   ..Yr.|G........F
0170 - 53 9a f4 51 3f 47 27 22-5c 6c a7 0f 10 f8 49 f0   S..Q?G&#39;&quot;\l....I.
0180 - 84 f7 00 bd 05 73 4d 49-4a 80 55 4d 0e e3 ae 57   .....sMIJ.UM...W
0190 - a4 86 ca 9b 5f d0 80 59-aa bd c0 cf cd 9f 9d 1f   ...._..Y........
01a0 - 37 3b 98 29 8d 88 85 39-6b 39 8b 3b a9 39 d5 eb   7;.)...9k9.;.9..
01b0 - 2c 98 81 5a e6 28 dd 07-61 4e 8b 5b f4 00 0f 00   ,..Z.(..aN.[....
01c0 - 01 01                                             ..
SSL_connect:SSLv3 write client hello A
read from 0x1d26a60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 56                                    ....V
read from 0x1d26a60 [0x1d1bb58] (86 bytes =&gt; 86 (0x56))
0000 - 02 00 00 52 03 02 50 d8-58 54 41 7d 11 b4 d1 84   ...R..P.XTA}....
0010 - 59 08 a4 4a 74 1c b3 90-14 81 77 90 e1 7c 56 84   Y..Jt.....w..|V.
0020 - 31 9f 9e 18 9f 33 20 ef-64 0a d6 b2 18 4a 2f 48   1....3 .d....J/H
0030 - 44 e1 64 d5 f1 19 0b 8c-59 06 4b cd 78 ce 51 34   D.d.....Y.K.x.Q4
0040 - 85 7c 2b e0 30 96 df 00-39 00 00 0a ff 01 00 01   .|+.0...9.......
0050 - 00 00 0f 00 01 01                                 ......
SSL_connect:SSLv3 read server hello A
read from 0x1d26a60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d26a60 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d26a60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d26a60 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - 88 c1 f8 18 c3 47 3b 1c-80 bf c4 87 90 ae 72 08   .....G;.......r.
0010 - 3a eb 40 e4 e8 9e c0 5c-9c 96 e2 3d c7 2d f4 c1   :[email protected]\...=.-..
0020 - 8a c0 b7 12 cf 13 03 05-a5 bc e9 59 8e 94 62 fa   ...........Y..b.
0030 - 13 d3 89 65 a8 07 f2 ec-f1 5a 9a ba d4 31 28 50   ...e.....Z...1(P
SSL_connect:SSLv3 read finished A
write to 0x1d26a60 [0x1d25830] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d26a60 [0x1d25830] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 24 08 8c-a7 fd 4d 2e 6d 51 db 6e   [email protected]$....M.mQ.n
0010 - 66 65 e0 82 cb b2 bf 9f-cc 5d 90 75 f0 e3 06 9c   fe.......].u....
0020 - 38 78 b3 8d 8c c6 91 96-bc 4a 8b 47 9d 12 65 25   8x.......J.G..e%
0030 - 78 92 ce ef 40 36 d7 a3-c5 9c 2b d3 9d e2 15 ec   x...@6....+.....
0040 - 9a b0 5e ca 34                                    ..^.4
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
---
Reused, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
drop connection and then reconnect
write to 0x1d26a60 [0x1d200a3] (53 bytes =&gt; 53 (0x35))
0000 - 15 03 02 00 30 e7 04 70-66 d8 70 d8 98 fa b1 f0   ....0..pf.p.....
0010 - 84 19 f5 68 f6 f5 f7 0c-dd 41 a0 8c 17 87 31 1a   ...h.....A....1.
0020 - 54 98 ff c8 7c 51 e2 e2-15 a4 b2 42 50 73 05 9c   T...|Q.....BPs..
0030 - b4 52 60 8c 2f                                    .R`./
SSL3 alert write:warning:close notify
CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d1bad0 [0x1d200a3] (450 bytes =&gt; 450 (0x1C2))
0000 - 16 03 01 01 bd 01 00 01-b9 03 02 50 d8 58 57 18   ...........P.XW.
0010 - 28 ec 04 5e 85 e0 11 28-46 0e b2 4e 05 76 ac 90   (..^...(F..N.v..
0020 - 58 b9 10 15 24 1f 68 b1-cb 24 c3 20 ef 64 0a d6   X...$.h..$. .d..
0030 - b2 18 4a 2f 48 44 e1 64-d5 f1 19 0b 8c 59 06 4b   ..J/HD.d.....Y.K
0040 - cd 78 ce 51 34 85 7c 2b-e0 30 96 df 00 66 c0 14   .x.Q4.|+.0...f..
0050 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0060 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0070 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0080 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0090 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
00a0 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
00b0 - 00 03 00 ff 02 01 00 01-09 00 0b 00 04 03 00 01   ................
00c0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00d0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00e0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00f0 - 02 00 03 00 0f 00 10 00-11 00 23 00 c0 e7 6f e6   ..........#...o.
0100 - e3 6b 8d 30 8e 73 e7 97-38 a5 2e 8c 5d 04 a6 52   .k.0.s..8...]..R
0110 - 50 4f 34 db 25 67 b6 7f-39 a3 0b 77 de e4 f6 71   PO4.%g..9..w...q
0120 - a5 c6 46 d6 71 a3 6d e0-4c a1 7f b4 ee e2 8c 56   ..F.q.m.L......V
0130 - a4 f0 d2 22 ab 36 67 8a-68 da 37 98 4d d3 8c 57   ...&quot;.6g.h.7.M..W
0140 - 4f 85 b7 4a 2a bf fc c9-c8 31 16 a2 93 3d fc 04   O..J*....1...=..
0150 - 8d 90 9f bd 29 e3 a6 56-10 b4 45 c4 76 15 53 86   ....)..V..E.v.S.
0160 - c8 e3 59 72 fe 7c 47 a1-cb f1 b7 9a 87 d8 db 46   ..Yr.|G........F
0170 - 53 9a f4 51 3f 47 27 22-5c 6c a7 0f 10 f8 49 f0   S..Q?G&#39;&quot;\l....I.
0180 - 84 f7 00 bd 05 73 4d 49-4a 80 55 4d 0e e3 ae 57   .....sMIJ.UM...W
0190 - a4 86 ca 9b 5f d0 80 59-aa bd c0 cf cd 9f 9d 1f   ...._..Y........
01a0 - 37 3b 98 29 8d 88 85 39-6b 39 8b 3b a9 39 d5 eb   7;.)...9k9.;.9..
01b0 - 2c 98 81 5a e6 28 dd 07-61 4e 8b 5b f4 00 0f 00   ,..Z.(..aN.[....
01c0 - 01 01                                             ..
SSL_connect:SSLv3 write client hello A
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 56                                    ....V
read from 0x1d1bad0 [0x1d1bb58] (86 bytes =&gt; 86 (0x56))
0000 - 02 00 00 52 03 02 50 d8-58 54 6d 17 32 2d c3 ff   ...R..P.XTm.2-..
0010 - 88 a6 a7 3a 53 83 2a b8-97 e3 e4 69 1d b1 64 88   ...:S.*....i..d.
0020 - 8f 93 e8 d2 9a fc 20 ef-64 0a d6 b2 18 4a 2f 48   ...... .d....J/H
0030 - 44 e1 64 d5 f1 19 0b 8c-59 06 4b cd 78 ce 51 34   D.d.....Y.K.x.Q4
0040 - 85 7c 2b e0 30 96 df 00-39 00 00 0a ff 01 00 01   .|+.0...9.......
0050 - 00 00 0f 00 01 01                                 ......
SSL_connect:SSLv3 read server hello A
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d1bad0 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d1bad0 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d1bad0 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - b7 3f bf 3f e3 1e 0c 17-59 4e 2a fa 13 fb 26 ec   .?.?....YN*...&amp;.
0010 - 1f 1d fa ca 3f b8 24 75-7f 7c b8 17 c7 a1 b0 32   ....?.$u.|.....2
0020 - b0 27 82 54 57 82 b3 d8-13 b3 c2 7d f2 c7 95 1c   .&#39;.TW......}....
0030 - a3 f4 d7 34 b4 6c cd 54-6c f5 15 de b7 aa 71 6d   ...4.l.Tl.....qm
SSL_connect:SSLv3 read finished A
write to 0x1d1bad0 [0x1d25830] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d1bad0 [0x1d25830] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 8c f5 34-bb db 45 6a ca 01 3f 14   [email protected]?.
0010 - 57 05 68 94 93 df 65 92-7b 00 b6 03 eb b6 23 d7   W.h...e.{.....#.
0020 - 39 f5 67 38 58 40 9a 5e-34 03 ab cf 57 2e 59 29   [email protected]^4...W.Y)
0030 - da 34 d6 63 e4 72 43 da-8a a2 90 1a 99 d6 bb 1f   .4.c.rC.........
0040 - 7d 31 e5 43 76                                    }1.Cv
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
---
Reused, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
drop connection and then reconnect
write to 0x1d1bad0 [0x1d200a3] (53 bytes =&gt; 53 (0x35))
0000 - 15 03 02 00 30 74 d0 af-ee ad a7 dc 40 cd f2 e5   [email protected]
0010 - 06 eb b4 8e 44 8f 83 ac-77 d3 af 1f ea 0c 40 fc   [email protected]
0020 - 75 ef 5c d3 90 b8 01 90-57 1b 4d 0a 9d 0b 98 ac   u.\.....W.M.....
0030 - de b2 9f 91 93                                    .....
SSL3 alert write:warning:close notify
CONNECTED(00000003)
SSL_connect:before/connect initialization
write to 0x1d29f60 [0x1d200a3] (450 bytes =&gt; 450 (0x1C2))
0000 - 16 03 01 01 bd 01 00 01-b9 03 02 50 d8 58 57 a9   ...........P.XW.
0010 - 46 5a c3 01 ca ae 34 3c-e6 b9 83 55 33 91 51 d2   FZ....4&lt;...U3.Q.
0020 - a4 99 1b 6f 01 a6 9a b1-7b 2d b9 20 ef 64 0a d6   ...o....{-. .d..
0030 - b2 18 4a 2f 48 44 e1 64-d5 f1 19 0b 8c 59 06 4b   ..J/HD.d.....Y.K
0040 - cd 78 ce 51 34 85 7c 2b-e0 30 96 df 00 66 c0 14   .x.Q4.|+.0...f..
0050 - c0 0a c0 22 c0 21 00 39-00 38 00 88 00 87 c0 0f   ...&quot;.!.9.8......
0060 - c0 05 00 35 00 84 c0 12-c0 08 c0 1c c0 1b 00 16   ...5............
0070 - 00 13 c0 0d c0 03 00 0a-c0 13 c0 09 c0 1f c0 1e   ................
0080 - 00 33 00 32 00 9a 00 99-00 45 00 44 c0 0e c0 04   .3.2.....E.D....
0090 - 00 2f 00 96 00 41 c0 11-c0 07 c0 0c c0 02 00 05   ./...A..........
00a0 - 00 04 00 15 00 12 00 09-00 14 00 11 00 08 00 06   ................
00b0 - 00 03 00 ff 02 01 00 01-09 00 0b 00 04 03 00 01   ................
00c0 - 02 00 0a 00 34 00 32 00-0e 00 0d 00 19 00 0b 00   ....4.2.........
00d0 - 0c 00 18 00 09 00 0a 00-16 00 17 00 08 00 06 00   ................
00e0 - 07 00 14 00 15 00 04 00-05 00 12 00 13 00 01 00   ................
00f0 - 02 00 03 00 0f 00 10 00-11 00 23 00 c0 e7 6f e6   ..........#...o.
0100 - e3 6b 8d 30 8e 73 e7 97-38 a5 2e 8c 5d 04 a6 52   .k.0.s..8...]..R
0110 - 50 4f 34 db 25 67 b6 7f-39 a3 0b 77 de e4 f6 71   PO4.%g..9..w...q
0120 - a5 c6 46 d6 71 a3 6d e0-4c a1 7f b4 ee e2 8c 56   ..F.q.m.L......V
0130 - a4 f0 d2 22 ab 36 67 8a-68 da 37 98 4d d3 8c 57   ...&quot;.6g.h.7.M..W
0140 - 4f 85 b7 4a 2a bf fc c9-c8 31 16 a2 93 3d fc 04   O..J*....1...=..
0150 - 8d 90 9f bd 29 e3 a6 56-10 b4 45 c4 76 15 53 86   ....)..V..E.v.S.
0160 - c8 e3 59 72 fe 7c 47 a1-cb f1 b7 9a 87 d8 db 46   ..Yr.|G........F
0170 - 53 9a f4 51 3f 47 27 22-5c 6c a7 0f 10 f8 49 f0   S..Q?G&#39;&quot;\l....I.
0180 - 84 f7 00 bd 05 73 4d 49-4a 80 55 4d 0e e3 ae 57   .....sMIJ.UM...W
0190 - a4 86 ca 9b 5f d0 80 59-aa bd c0 cf cd 9f 9d 1f   ...._..Y........
01a0 - 37 3b 98 29 8d 88 85 39-6b 39 8b 3b a9 39 d5 eb   7;.)...9k9.;.9..
01b0 - 2c 98 81 5a e6 28 dd 07-61 4e 8b 5b f4 00 0f 00   ,..Z.(..aN.[....
01c0 - 01 01                                             ..
SSL_connect:SSLv3 write client hello A
read from 0x1d29f60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 56                                    ....V
read from 0x1d29f60 [0x1d1bb58] (86 bytes =&gt; 86 (0x56))
0000 - 02 00 00 52 03 02 50 d8-58 54 30 e1 c4 39 83 67   ...R..P.XT0..9.g
0010 - f6 04 91 e1 d5 86 46 1e-9b d8 bc 6f 39 12 13 ef   ......F....o9...
0020 - 35 62 63 ca b2 84 20 ef-64 0a d6 b2 18 4a 2f 48   5bc... .d....J/H
0030 - 44 e1 64 d5 f1 19 0b 8c-59 06 4b cd 78 ce 51 34   D.d.....Y.K.x.Q4
0040 - 85 7c 2b e0 30 96 df 00-39 00 00 0a ff 01 00 01   .|+.0...9.......
0050 - 00 00 0f 00 01 01                                 ......
SSL_connect:SSLv3 read server hello A
read from 0x1d29f60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 14 03 02 00 01                                    .....
read from 0x1d29f60 [0x1d1bb58] (1 bytes =&gt; 1 (0x1))
0000 - 01                                                .
read from 0x1d29f60 [0x1d1bb53] (5 bytes =&gt; 5 (0x5))
0000 - 16 03 02 00 40                                    [email protected]
read from 0x1d29f60 [0x1d1bb58] (64 bytes =&gt; 64 (0x40))
0000 - 2f 2c b8 e7 01 cb 03 e7-70 9e 4c 79 da da d0 fa   /,......p.Ly....
0010 - a9 1b 37 fc 3e da 15 ae-a4 2a 49 92 c4 9d 08 4c   ..7.&gt;....*I....L
0020 - b4 82 6e 5f 8f c0 58 04-51 5c 32 74 00 72 26 d9   ..n_..X.Q\2t.r&amp;.
0030 - ff 18 14 6c 01 c1 69 fd-31 50 97 ab a4 49 40 a7   [email protected]
SSL_connect:SSLv3 read finished A
write to 0x1d29f60 [0x1d25830] (6 bytes =&gt; 6 (0x6))
0000 - 14 03 02 00 01 01                                 ......
SSL_connect:SSLv3 write change cipher spec A
write to 0x1d29f60 [0x1d25830] (69 bytes =&gt; 69 (0x45))
0000 - 16 03 02 00 40 47 1c bf-f4 13 56 76 3c be f6 9a   ....@G....Vv&lt;...
0010 - de d6 0a 83 9e d5 b0 f5-55 88 18 51 b4 bc 73 eb   ........U..Q..s.
0020 - 9c 9a e0 0d 7b b5 d2 eb-e4 43 0b e6 8e 6f 47 28   ....{....C...oG(
0030 - 71 b2 17 1f 5b 92 7a 83-89 f2 9a e1 cf a6 b3 8d   q...[.z.........
0040 - dd 5e 47 6f 29                                    .^Go)
SSL_connect:SSLv3 write finished A
SSL_connect:SSLv3 flush data
---
Reused, TLSv1/SSLv3, Cipher is DHE-RSA-AES256-SHA
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.1
    Cipher    : DHE-RSA-AES256-SHA
    Session-ID: EF640AD6B2184A2F4844E164D5F1190B8C59064BCD78CE5134857C2BE03096DF
    Session-ID-ctx: 
    Master-Key: D489A400C767F1A8B4D94B2A3AC7EC832E461BC10F2BE7A0170373D9D48622C4219D0A1000BAB7C17A03AC3A7A2B10B7
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e7 6f e6 e3 6b 8d 30 8e-73 e7 97 38 a5 2e 8c 5d   .o..k.0.s..8...]
    0010 - 04 a6 52 50 4f 34 db 25-67 b6 7f 39 a3 0b 77 de   ..RPO4.%g..9..w.
    0020 - e4 f6 71 a5 c6 46 d6 71-a3 6d e0 4c a1 7f b4 ee   ..q..F.q.m.L....
    0030 - e2 8c 56 a4 f0 d2 22 ab-36 67 8a 68 da 37 98 4d   ..V...&quot;.6g.h.7.M
    0040 - d3 8c 57 4f 85 b7 4a 2a-bf fc c9 c8 31 16 a2 93   ..WO..J*....1...
    0050 - 3d fc 04 8d 90 9f bd 29-e3 a6 56 10 b4 45 c4 76   =......)..V..E.v
    0060 - 15 53 86 c8 e3 59 72 fe-7c 47 a1 cb f1 b7 9a 87   .S...Yr.|G......
    0070 - d8 db 46 53 9a f4 51 3f-47 27 22 5c 6c a7 0f 10   ..FS..Q?G&#39;&quot;\l...
    0080 - f8 49 f0 84 f7 00 bd 05-73 4d 49 4a 80 55 4d 0e   .I......sMIJ.UM.
    0090 - e3 ae 57 a4 86 ca 9b 5f-d0 80 59 aa bd c0 cf cd   ..W...._..Y.....
    00a0 - 9f 9d 1f 37 3b 98 29 8d-88 85 39 6b 39 8b 3b a9   ...7;.)...9k9.;.
    00b0 - 39 d5 eb 2c 98 81 5a e6-28 dd 07 61 4e 8b 5b f4   9..,..Z.(..aN.[.

    Start Time: 1356355671
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---</code></pre></div><div id="comment-17232-info" class="comment-info"><span class="comment-age">(24 Dec '12, 05:34)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17241"></span><div id="comment-17241" class="comment not_top_scorer"><div id="post-17241-score" class="comment-score"></div><div class="comment-text"><p>I don't see any ssl/tls related errors in the debug output. There are some inconsistencies, however I believe that's from your attempt to anonymize the output (removing site specific information).</p><p>BTW: The mentioned error is also no longer there:</p><pre><code>CONNECTED(00000003)
1201:error:1408E0F4:SSL routines:SSL3_GET_MESSAGE:unexpected message:/SourceCache/OpenSSL098/OpenSSL098-35.1/src/ssl/s3_both.c:462:</code></pre><p>So, you must have changed something in your environment, right? Maybe the restart of apache fixed that specific problem!?!</p><p>Looking again at your capture file I don't see any ssl/tls or network related problems for your reported performance issue. Actually, the tls connections are all quite fast (&lt; 1 second), with exception to the last 5 streams.</p><blockquote><p><code>Apply this fiter: ip.addr  eq 132.208.137.9</code></p></blockquote><p>then</p><blockquote><p><code>Statistics -&gt; Conversations -&gt; TCP (Limit to display filter)</code></p></blockquote><p>As you can see, the duration of all conversations (except the last 5) are &lt;&lt; 1 seconds, which should be O.K. The duration of the last 5 conversations is ~7 seconds. However, if you look at them in detail, you will see, that there is a delay of 5 seconds before the connection is closed. That delay comes most certainly from your Keepalive timeout of 5 seconds. So nothing special there as well.</p><p><strong>IF however</strong> you run into the timeout a lot, then you might get into trouble, as most browser will only open a certain number of parallel connections to one sever. So, if the client does not reuse the connection (for whatever reason), it will wait until the connection gets closed until it can open a new connection for the next request. If you sum up all those wait times and you have a lot of request, <strong>then</strong> you will experience severe performance problems. However, the posted capture file is to short for that kind of analysis.</p><p><strong>Conclusion:</strong> After you have changed the configuration (removed <code>SSLCACertificateFile</code> there is no ssl/tls error 48 (unknown CA) anymore. The conversation in the capture file you posted looks O.K. (except what I said above). There are no error messages in the openssl output anymore and SSL session reuse does work. I don't see any problem with the network nor with SSL/TLS.</p><p>There might be an issue with the keepalive timeout (see above). However, I can't explain why it would be faster with http. As you did not provide any data to show how much faster it actually is with http, I cannot judge on that.</p><p><strong>Recommendation</strong>: You need to either decrypt the SSL/TLS communication with Wireshark (you need the server key) and then look at the single requests and responses, <strong>or</strong> use tools like <a href="http://www.fiddler2.com/fiddler2/">Fiddler2</a>, <a href="http://portswigger.net/burp/proxy.html">burp</a>, or <a href="https://addons.mozilla.org/de/firefox/addon/httpfox/">Firefox HttpFox</a>. Additionally I recommend to enable debugging in tomcat and check the logs together with the output of the mentioned tools. Additionally try to modify the Keepalive timeout value (reduce it to 1 second) and check if your application is faster.</p><p>Regards<br />
Kurt</p></div><div id="comment-17241-info" class="comment-info"><span class="comment-age">(25 Dec '12, 15:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16987" class="comment-tools"><span class="comments-showing"> showing 5 of 18 </span> <a href="#" class="show-all-comments-link">show 13 more comments</a></div><div class="clear"></div><div id="comment-16987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17054"></span>

<div id="answer-container-17054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17054-score" class="post-score" title="current number of votes">0</div><span id="post-17054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I opened your pcap file and looked at the SSL sessions to server 132.208.137.9. I used the filter "ip.addr==132.208.137.9 &amp;&amp; (tcp.flags&amp;7 || ssl)" to get a "clean" view on the traffic. Here are my findings:</p><ul><li>You mentioned in the other answer-thread that you are not sure whether your server is configured with SSL session reuse. It is, as you can see by the short SSL handshakes in the tracefile (there is a SessionID in the ClientHello and the server responds with the same SessionID, therefor reusing the same SSL session and skipping the Certificate and CLientKeyExchange handshake messages).</li><li>There are quite a few occasions in which the client closes the SSL session straight after opening it. This seems to be a problem on the client. However, it does not introduce much delay (&lt;25ms per occasion)</li><li>The client closes each TCP session after retrieving one object. This can be a client-side configuration or a server-side (mis-)configuration do you have HTTP <a href="http://httpd.apache.org/docs/2.2/mod/core.html#keepalive">KeepAlive</a> configured in Apache?</li><li>While there is some client side delay (time between receiving a response and sending the next request), most of the delay in this pcap file is server side delay (delay between receiving the request and sending the response). I see response times of up to ~1 sec. If you use my filter, you can see 984ms delay between frame 683 and 772, 736ms delay between frame 870 and 1119, 470ms delay between frame 1187 and 1227, etc)</li></ul><p>Since SSL is a big CPU burden on a system (that's why there are a lot of devices offloading SSL from the server), my suspicion is that your server just can't take the load once all traffic is encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '12, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-17054" class="comments-container"><span id="17055"></span><div id="comment-17055" class="comment"><div id="post-17055-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comments. The KeepAlive is enabled on the apache conf. But i don't know a way to test that it's working.</p><p>When running a similar scenario as the on of the pcap file and looking at top (the unix command) result. I don't see any significant load caused by apache nor openssl. The only load comes from the tomcat server that sit behind the apache.</p></div><div id="comment-17055-info" class="comment-info"><span class="comment-age">(19 Dec '12, 06:46)</span> <span class="comment-user userinfo">benzen</span></div></div><span id="17060"></span><div id="comment-17060" class="comment"><div id="post-17060-score" class="comment-score"></div><div class="comment-text"><p>You can check by looking at the http data inside the ssl sessions. One way to do this is by adding the plugin httpfox to FireFox and then connect to your server. You should be seeing headers like:</p><pre><code>Connection: KeepAlive</code></pre><p>... in the server response.</p><p>To compare performance over HTTP and HTTPS, it is best to do the same steps over HTTP and HTTPS and capture the data (please start the trace before starting the browser, to capture the full SSL handshake). If it is possible for you to share the private key (or use a temporary certificate during the test), that would give more insight...</p></div><div id="comment-17060-info" class="comment-info"><span class="comment-age">(19 Dec '12, 08:12)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-17054" class="comment-tools"></div><div class="clear"></div><div id="comment-17054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

