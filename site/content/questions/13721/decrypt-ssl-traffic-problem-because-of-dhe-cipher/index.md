+++
type = "question"
title = "Decrypt SSL traffic problem because of DHE Cipher"
description = '''Decrypt SSL traffic problem because of DHE Cipher Hi, I read a lot about Wireshark and decrypting SSL using the private key. I read most of the post SYN-bit wrote, and saw his presentations he did @Sharkfest.  I just want to know, how can I create a SSL certificate without the DHE cipher in it? I we...'''
date = "2012-08-18T15:27:00Z"
lastmod = "2012-08-21T22:23:00Z"
weight = 13721
keywords = [ "decode", "ssl", "decrypt" ]
aliases = [ "/questions/13721" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypt SSL traffic problem because of DHE Cipher](/questions/13721/decrypt-ssl-traffic-problem-because-of-dhe-cipher)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13721-score" class="post-score" title="current number of votes">0</div><span id="post-13721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Decrypt SSL traffic problem because of DHE Cipher</strong></p><p>Hi,</p><p>I read a lot about Wireshark and decrypting SSL using the private key. I read most of the post <a href="http://ask.wireshark.org/users/5/syn-bit">SYN-bit</a> wrote, and saw his presentations he did @Sharkfest.</p><p>I just want to know, how can I create a SSL certificate without the DHE cipher in it? I went through lots of doc. and man pages, but still can't figure it out.</p><p>I use wireshark 1.6.6, and am unable to decrypt the traffic I capture.</p><p>regards,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '12, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/0ce931f077e091c7dc397bda5e106b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sha8e&#39;s gravatar image" /><p><span>sha8e</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sha8e has no accepted answers">0%</span></p></div></div><div id="comments-container-13721" class="comments-container"></div><div id="comment-tools-13721" class="comment-tools"></div><div class="clear"></div><div id="comment-13721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13737"></span>

<div id="answer-container-13737" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13737-score" class="post-score" title="current number of votes">1</div><span id="post-13737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sha8e has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the files that you sent me, the server has address 127.0.1.1 and not 127.0.0.1, so you need to fill in 127.0.1.1 in the SSL preferences to make it work...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '12, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13737" class="comments-container"><span id="13738"></span><div id="comment-13738" class="comment"><div id="post-13738-score" class="comment-score"></div><div class="comment-text"><p>Man I've been working since yesterday, I never ever noticed that. This really makes me sad :(</p><p>I'm very sorry I took your precious time to solve a dumb case like this.</p><p>BTW, why was Wireshark unable to capture the password sent between the client and server? I can see the response from the php application in the captures, but I'm unable to see the username/password I sent to login!</p><p>Thank you very much SYN-bit.</p></div><div id="comment-13738-info" class="comment-info"><span class="comment-age">(19 Aug '12, 05:22)</span> <span class="comment-user userinfo">sha8e</span></div></div></div><div id="comment-tools-13737" class="comment-tools"></div><div class="clear"></div><div id="comment-13737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13722"></span>

<div id="answer-container-13722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13722-score" class="post-score" title="current number of votes">1</div><span id="post-13722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>t is not the certificate that has a DHE cipher in it. The client presents a list of ciphers it supports and then the server choses one of those ciphers that it supports. The way to make sure that a non-DH cipher is used, you can either limit the supported ciphers on the client or limit the supported ciphers on the server.</p><p>If you use Firefox, you can type "about:config" in the location bar and then do a search on "dh" and disable all DH ciphers. On the server part it depends on your server type. In Apache you can use something like "SSLCipherSuite ALL:!DH".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '12, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13722" class="comments-container"><span id="13723"></span><div id="comment-13723" class="comment"><div id="post-13723-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick reply. I disabled all that as you told me. Still I'm unable to do the test.</p><p>What I did is the following: openssl req -new -x509 -out server.pem -nodes -keyout privkey.pem</p><p>Copied them to /etc/ssl/private &amp; chmod 400 them.</p><p>Configured Apache2 with the following: SSLCertificateFile /etc/ssl/private/privkey.pem SSLCertificateKeyFile /etc/ssl/private/server.pem</p><p>All other SSL Apache directives are commented, except the SSLEngine is on.</p><p>Now I ran Wireshark and connected to the website (locally server). I first got this notification from firefox that the certificate is self-signed and requires an exception from me to be added. I did that, and the website opened.</p><p>All that traffic was captured in Wireshark. I added the following to the ~/.wireshark/ssl_keys "server.local","443","http","/etc/ssl/private/server.pem"</p><p>All other configurations you talked about in other posts was done too, such as debug and restarting Wireshark.</p><p>But till now there is no decrypted traffic seen in Wireshark. What do you think is the problem?</p><p>I appreciate all the time and efforts you do in helping me and others.</p><p>Regards,</p></div><div id="comment-13723-info" class="comment-info"><span class="comment-age">(18 Aug '12, 16:27)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13724"></span><div id="comment-13724" class="comment"><div id="post-13724-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment, please reread the FAQ :-))</p><blockquote><p>All that traffic was captured in Wireshark. I added the following to the ~/.wireshark/ssl_keys "server.local","443","http","/etc/ssl/private/server.pem"</p></blockquote><p>I have not tried myself, but I believe there is no name resolution in the SSL key settings, so you need to configure the IP address of your local server. Also you need to use the private key instead of the certificate. You will have an entry like this:</p><pre><code>&quot;&lt;ip-of-server&gt;&quot;,&quot;443&quot;,&quot;http&quot;,&quot;/etc/ssl/private/privkey.pem&quot;</code></pre></div><div id="comment-13724-info" class="comment-info"><span class="comment-age">(19 Aug '12, 00:24)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13725"></span><div id="comment-13725" class="comment"><div id="post-13725-score" class="comment-score"></div><div class="comment-text"><p>I had to add my last reply as a reply because of the chars. left in comments :(</p><p>That was a typo SYN-bit, my config is indeed like this: "server.local","443","http","/etc/ssl/private/privkey.pem"</p><p>I also have <a href="http://server.local">server.local</a> configured in my /etc/hosts: 127.0.0.1 <a href="http://server.local">server.local</a></p><p>Is that what you mean? And do you think the problem is with Firefox? I'll give it a try using the openssl client.</p></div><div id="comment-13725-info" class="comment-info"><span class="comment-age">(19 Aug '12, 02:57)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13727"></span><div id="comment-13727" class="comment not_top_scorer"><div id="post-13727-score" class="comment-score"></div><div class="comment-text"><p>I did the following:</p><p><span class="__cf_email__" data-cfemail="40322f2f34002234">[email protected]</span>:~# tshark -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list: 127.0.0.1,443,http,/etc/apache2/ssl/privkey.pem" -o "ssl.debug_file: /root/wireshark-log" -i lo -R "tcp.port == 443" Running as user "root" and group "root". This could be dangerous. Capturing on lo</p><p>And the output is below in next comment :(</p></div><div id="comment-13727-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:15)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13728"></span><div id="comment-13728" class="comment"><div id="post-13728-score" class="comment-score">1</div><div class="comment-text"><p>Looking at the source code, hostnames are indeed supported. But only is name resolving is enabled in the settings. Could you try with a hardcoded IP address (127.0.0.1) in the SSL key list instead of the hostname?</p><p>Are you able to share your tracefile &amp; key? That would make helping you a lot easier :-)</p></div><div id="comment-13728-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:16)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13729"></span><div id="comment-13729" class="comment not_top_scorer"><div id="post-13729-score" class="comment-score"></div><div class="comment-text"><p>0.000000 127.0.0.1 -&gt; 127.0.0.1 TCP 74 58959 &gt; https [SYN] Seq=0 Win=32792 Len=0 MSS=16396 SACK_PERM=1 TSval=187391094 TSecr=0 WS=16 0.000010 127.0.0.1 -&gt; 127.0.0.1 TCP 74 https &gt; 58959 [SYN, ACK] Seq=0 Ack=1 Win=32768 Len=0 MSS=16396 SACK_PERM=1 TSval=187391094 TSecr=187391094 WS=16 0.000017 127.0.0.1 -&gt; 127.0.0.1 TCP 66 58959 &gt; https [ACK] Seq=1 Ack=1 Win=32800 Len=0 TSval=187391094 TSecr=187391094 0.000216 127.0.0.1 -&gt; 127.0.0.1 SSL 155 Client Hello</p></div><div id="comment-13729-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:17)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13730"></span><div id="comment-13730" class="comment not_top_scorer"><div id="post-13730-score" class="comment-score"></div><div class="comment-text"><p>0.000017 127.0.0.1 -&gt; 127.0.0.1 TCP 66 58959 &gt; https [ACK] Seq=1 Ack=1 Win=32800 Len=0 TSval=187391094 TSecr=187391094 0.000216 127.0.0.1 -&gt; 127.0.0.1 SSL 155 Client Hello 0.000231 127.0.0.1 -&gt; 127.0.0.1 TCP 66 https &gt; 58959 [ACK] Seq=1 Ack=90 Win=32768 Len=0 TSval=187391094 TSecr=187391094 0.000553 127.0.0.1 -&gt; 127.0.0.1 SSLv3 1116 Server Hello, Certificate, Server Hello Done 0.000594 127.0.0.1 -&gt; 127.0.0.1 TCP 66 58959 &gt; https [ACK] Seq=90 Ack=1051 Win=34896 Len=0 TSval=187391094 TSecr=187391094</p></div><div id="comment-13730-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:17)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13731"></span><div id="comment-13731" class="comment not_top_scorer"><div id="post-13731-score" class="comment-score"></div><div class="comment-text"><p>0.001393 127.0.0.1 -&gt; 127.0.0.1 SSLv3 294 Client Key Exchange, Change Cipher Spec, Finished 0.002275 127.0.0.1 -&gt; 127.0.0.1 SSLv3 157 Change Cipher Spec, Finished 0.009225 127.0.0.1 -&gt; 127.0.0.1 HTTP 156 GET / HTTP/1.1 0.009384 127.0.0.1 -&gt; 127.0.0.1 HTTP 508 HTTP/1.1 400 Bad Request (text/html) 0.009448 127.0.0.1 -&gt; 127.0.0.1 SSLv3 103 Alert (Level: Warning, Description: Close Notify)</p></div><div id="comment-13731-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:17)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13732"></span><div id="comment-13732" class="comment not_top_scorer"><div id="post-13732-score" class="comment-score"></div><div class="comment-text"><p>0.009448 127.0.0.1 -&gt; 127.0.0.1 SSLv3 103 Alert (Level: Warning, Description: Close Notify) 0.009504 127.0.0.1 -&gt; 127.0.0.1 TCP 66 https &gt; 58959 [FIN, ACK] Seq=1621 Ack=408 Win=33840 Len=0 TSval=187391096 TSecr=187391096 0.009957 127.0.0.1 -&gt; 127.0.0.1 SSLv3 103 Alert (Level: Warning, Description: Close Notify) 0.010013 127.0.0.1 -&gt; 127.0.0.1 TCP 66 58959 &gt; https [FIN, ACK] Seq=445 Ack=1622 Win=36992 Len=0 TSval=187391096 TSecr=187391096 0.010036 127.0.0.1 -&gt; 127.0.0.1 TCP 66 https &gt; 58959 [ACK] Seq=1622 Ack=446 Win=33840 Len=0 TSval=187391096 TSecr=187391096</p></div><div id="comment-13732-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:18)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13735"></span><div id="comment-13735" class="comment not_top_scorer"><div id="post-13735-score" class="comment-score"></div><div class="comment-text"><p>I also did the hardcoded IP but nothing new :(</p><p>Sure, I sent you all the files.</p><p>Thank you SYN-bit.</p></div><div id="comment-13735-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:43)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13736"></span><div id="comment-13736" class="comment"><div id="post-13736-score" class="comment-score">1</div><div class="comment-text"><p>Well, the above output shows that you did indeed decrypt the traffic:</p><blockquote><p>0.001393 127.0.0.1 -&gt; 127.0.0.1 SSLv3 294 Client Key Exchange, Change Cipher Spec, Finished</p></blockquote><p>The Finished handshake message would look like "Encrypted Handshake Message" if decryption did not work.</p><blockquote><p>0.002275 127.0.0.1 -&gt; 127.0.0.1 SSLv3 157 Change Cipher Spec, Finished 0.009225 127.0.0.1 -&gt; 127.0.0.1 HTTP 156 GET / HTTP/1.1 0.009384 127.0.0.1 -&gt; 127.0.0.1 HTTP 508 HTTP/1.1 400 Bad Request (text/html)</p></blockquote><p>And here is the HTTP data from within the SSL stream.</p></div><div id="comment-13736-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:59)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-13722" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-13722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13733"></span>

<div id="answer-container-13733" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13733-score" class="post-score" title="current number of votes">0</div><span id="post-13733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>And here is the openssl client test:</p><pre><code>[email protected]:~# (echo GET / HTTP/1.1; echo ; sleep 1) | openssl s_client -ssl3 -connect 127.0.0.1:443 -cert server.pem -key privkey.pem 
CONNECTED(00000003)
depth=0 /C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
verify error:num=18:self signed certificate
verify return:1
depth=0 /C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
verify return:1
---
Certificate chain
 0 s:/C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
   i:/C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDqDCCAxGgAwIBAgIJAK1kHE4p88WqMA0GCSqGSIb3DQEBBQUAMIGVMQswCQYD
VQQGEwJKUDESMBAGA1UECBMJSGlyb3NoaW1hMRIwEAYDVQQHEwlIaXJvc2hpbWEx
DjAMBgNVBAoTBVNIQThFMRkwFwYDVQQLExBUcmFmZmljIEFuYWx5c2lzMRMwEQYD
VQQDEwpidC5mb28ub3JnMR4wHAYJKoZIhvcNAQkBFg9yb290QGJ0LmZvby5vcmcw
HhcNMTIwODE4MTMxMzA5WhcNMTIwOTE3MTMxMzA5WjCBlTELMAkGA1UEBhMCSlAx
EjAQBgNVBAgTCUhpcm9zaGltYTESMBAGA1UEBxMJSGlyb3NoaW1hMQ4wDAYDVQQK
EwVTSEE4RTEZMBcGA1UECxMQVHJhZmZpYyBBbmFseXNpczETMBEGA1UEAxMKYnQu
Zm9vLm9yZzEeMBwGCSqGSIb3DQEJARYPcm9vdEBidC5mb28ub3JnMIGfMA0GCSqG
SIb3DQEBAQUAA4GNADCBiQKBgQC+1JYCj9tnygdHFPOztVbnztj2zdQRpDMR+xNO
6wYHXL0PpgrKD9N1JVVr1TEqPJb2gTn/mqay9w/npEM4B+XSYFMs38E/cRIEtEDA
QNsS/K5BqB9awwJ3ws8c/V24ZH3eweXd2ucYe4VJY/lDC8OjyOnMbE03X4c38O56
BzG7/QIDAQABo4H9MIH6MB0GA1UdDgQWBBQJntO243wq6c08Rl8ReQlKbNNDdTCB
ygYDVR0jBIHCMIG/gBQJntO243wq6c08Rl8ReQlKbNNDdaGBm6SBmDCBlTELMAkG
A1UEBhMCSlAxEjAQBgNVBAgTCUhpcm9zaGltYTESMBAGA1UEBxMJSGlyb3NoaW1h
MQ4wDAYDVQQKEwVTSEE4RTEZMBcGA1UECxMQVHJhZmZpYyBBbmFseXNpczETMBEG
A1UEAxMKYnQuZm9vLm9yZzEeMBwGCSqGSIb3DQEJARYPcm9vdEBidC5mb28ub3Jn
ggkArWQcTinzxaowDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQAvBloE
YBE6FqJl+/CCrKDQz1Skb/qlaBh3JM/uOQ3Ua8PY+5jTYmnuEQ6kX+cDROtSynP8
B4EBgMUkwkWuwRN7ajG6tW4aG6YorwQstmNGGuBXMQzQ60atXK/9+319dcYQjUOJ
dtvEuKthSxv8S8GSblHNHB3/kNtlkhqr9ZSFVw==
-----END CERTIFICATE-----
subject=/C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
issuer=/C=JP/ST=Hiroshima/L=Hiroshima/O=SHA8E/OU=Traffic Analysis/CN=server.local/[email protected]
---
No client certificate CA names sent
---
SSL handshake has read 1141 bytes and written 317 bytes
---
New, TLSv1/SSLv3, Cipher is AES256-SHA
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: zlib compression
Expansion: zlib compression
SSL-Session:
    Protocol  : SSLv3
    Cipher    : AES256-SHA
    Session-ID: 32CEC84CCD0AF087BE51A677BAD15639983FC4FCEE45D8110F0989E14C7821EE
    Session-ID-ctx: 
    Master-Key: 7377D1ECBEF3A21E4034B7FD457074AD3C71312C85E7283757A5D84B5580C7F69EF734476B95045EC435360C03053ADF
    Key-Arg   : None
   Compression: 1 (zlib compression)
    Start Time: 1345330539
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
---
HTTP/1.1 400 Bad Request
Date: Sat, 18 Aug 2012 22:55:39 GMT
Server: Apache/2.2.14 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 303
Connection: close
Content-Type: text/html; charset=iso-8859-1

&lt;!DOCTYPE HTML PUBLIC &quot;-//IETF//DTD HTML 2.0//EN&quot;&gt;
&lt;html&gt;&lt;head&gt;
&lt;title&gt;400 Bad Request&lt;/title&gt;
&lt;/head&gt;&lt;body&gt;
&lt;h1&gt;Bad Request&lt;/h1&gt;
&lt;p&gt;Your browser sent a request that this server could not understand.&lt;br /&gt;
&lt;/p&gt;
&lt;hr&gt;
&lt;address&gt;Apache/2.2.14 (Ubuntu) Server at server.local Port 443&lt;/address&gt;
&lt;/body&gt;&lt;/html&gt;
closed</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '12, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/0ce931f077e091c7dc397bda5e106b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sha8e&#39;s gravatar image" /><p><span>sha8e</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sha8e has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '12, 04:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-13733" class="comments-container"><span id="13734"></span><div id="comment-13734" class="comment"><div id="post-13734-score" class="comment-score"></div><div class="comment-text"><p>Here is the test: <a href="http://www.cloudshark.org/captures/dc99a1e082b6">http://www.cloudshark.org/captures/dc99a1e082b6</a></p><p>I will send you keys, and other stuff @email. I hope that's fine with you.</p><p>Thank you very much for your time in helping me out. I really appreciate that.</p></div><div id="comment-13734-info" class="comment-info"><span class="comment-age">(19 Aug '12, 04:38)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13739"></span><div id="comment-13739" class="comment"><div id="post-13739-score" class="comment-score"></div><div class="comment-text"><p>I noticed its saying:</p><p>Continuation or non-HTTP traffic[Malformed Packet]</p><p>I think this is the HTTP POST. But strange, why is Wireshark seeing it like that!</p></div><div id="comment-13739-info" class="comment-info"><span class="comment-age">(19 Aug '12, 05:56)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13740"></span><div id="comment-13740" class="comment"><div id="post-13740-score" class="comment-score">1</div><div class="comment-text"><p>For some reason the first byte of the request gets sent in one SSL record and the rest of the request is sent in another SSL record. Somehow Wireshark has problems re-assembling those parts. This is probably a bug. I'll try to find some time to have a look at it, but don't wait up for me ;-)</p></div><div id="comment-13740-info" class="comment-info"><span class="comment-age">(19 Aug '12, 06:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13742"></span><div id="comment-13742" class="comment"><div id="post-13742-score" class="comment-score"></div><div class="comment-text"><p>Do you want me to file a bug report or something? This is very important to me, I will wait for you, because no one maybe knows about it, except you :D</p><p>Thank you SYN-bit</p></div><div id="comment-13742-info" class="comment-info"><span class="comment-age">(19 Aug '12, 13:11)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13743"></span><div id="comment-13743" class="comment"><div id="post-13743-score" class="comment-score">1</div><div class="comment-text"><p>No need to file a bug-report. I found the issue and fixed it in SVN 44593.</p><p>In a couple of hours you can download an automated built from <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a> (please pick a file with a version number of 44953 or higher). Or you can wait for the next official release in which the fix will be included.</p></div><div id="comment-13743-info" class="comment-info"><span class="comment-age">(19 Aug '12, 16:55)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13748"></span><div id="comment-13748" class="comment not_top_scorer"><div id="post-13748-score" class="comment-score"></div><div class="comment-text"><p>Thank you SYN-bit, I think I'll wait for the official release better than screwing up my current system with compilation issues :)</p><p>I hope the builders for Linux won't take long in doing the update.</p><p>Your help was very grateful, you not only helped me, but I learned lots from you and your comments to other posts, plus your precious presentations.</p><p>Wish you good luck always.</p></div><div id="comment-13748-info" class="comment-info"><span class="comment-age">(20 Aug '12, 03:35)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13765"></span><div id="comment-13765" class="comment not_top_scorer"><div id="post-13765-score" class="comment-score"></div><div class="comment-text"><p>You are very welcome. I extracted my comments to a new answer, as it might help others :-)</p><p>If you feel your question is answered, please accept the asnwer that did indeed answer your question best by clicking on the check-mark next to it. This will help others and remove your question from the "unanswered questions" list.</p></div><div id="comment-13765-info" class="comment-info"><span class="comment-age">(20 Aug '12, 09:42)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="13766"></span><div id="comment-13766" class="comment not_top_scorer"><div id="post-13766-score" class="comment-score"></div><div class="comment-text"><p>You're the boss, anything you say. I marked it as answered even though honestly most of your replies were part of the whole answer. So how can I mark them all :$</p></div><div id="comment-13766-info" class="comment-info"><span class="comment-age">(20 Aug '12, 09:56)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13803"></span><div id="comment-13803" class="comment not_top_scorer"><div id="post-13803-score" class="comment-score"></div><div class="comment-text"><p>Hola, I just downloaded the new version of Wireshark 1.8.1, and it still doesn't capture the first POST packet! SYN-bit did you test it?</p></div><div id="comment-13803-info" class="comment-info"><span class="comment-age">(21 Aug '12, 16:47)</span> <span class="comment-user userinfo">sha8e</span></div></div><span id="13805"></span><div id="comment-13805" class="comment not_top_scorer"><div id="post-13805-score" class="comment-score"></div><div class="comment-text"><p>That's because 1.8.1 was already released before I committed the change. You will have to wait until 1.8.2 comes out. Or use one of the automated builds from <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a></p></div><div id="comment-13805-info" class="comment-info"><span class="comment-age">(21 Aug '12, 22:23)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-13733" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-13733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

