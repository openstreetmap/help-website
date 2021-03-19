+++
type = "question"
title = "SSLv2 Client Hello - Alert (Level: Fatal, Description: Handshake Failure)"
description = '''   I got a strange problem on HTTPS connection. I run same Tomcat 7 (same config) on two window server 2003/2012. But I fail to access the page of the one at Window 2012. I found that Window 2012 fails to reponse the &quot;client hello&quot;. I trace the TCP package, window 2003 and 2012 ACK with a differet s...'''
date = "2015-07-23T01:44:00Z"
lastmod = "2015-07-23T02:32:00Z"
weight = 44409
keywords = [ "tls", "tcpwindowsize", "https", "sslv2" ]
aliases = [ "/questions/44409" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSLv2 Client Hello - Alert (Level: Fatal, Description: Handshake Failure)](/questions/44409/sslv2-client-hello-alert-level-fatal-description-handshake-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44409-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp_log_2003_uNI6qaB.jpg" alt="Win 2003" /> <img src="https://osqa-ask.wireshark.org/upfiles/tcp_log_2012.jpg" alt="Win 2012 R2" /> <img src="https://osqa-ask.wireshark.org/upfiles/first_load_error.jpg" alt="Load page error" /></p><p>I got a strange problem on HTTPS connection. I run same Tomcat 7 (same config) on two window server 2003/2012. But I fail to access the page of the one at Window 2012. I found that Window 2012 fails to reponse the "client hello". I trace the TCP package, window 2003 and 2012 ACK with a differet size of WIN SIZE (64240 vs 8192). Then the client send the "client hello" with SSLv2 and TLSV1.1 depends. I suspect it is the problom of TCP Recieve Size configuration. Please give me some direction of the problem</p></div><div id="question-tags" class="tags-container tags">tls tcpwindowsize https sslv2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '15, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/52cfeb08ad4b8b2e6ee701a2f20706b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rocky%20Shek&#39;s gravatar image" /><p>Rocky Shek<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rocky Shek has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44409" class="comments-container"></div><div id="comment-tools-44409" class="comment-tools"></div><div class="clear"></div><div id="comment-44409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44410"></span>

<div id="answer-container-44410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The traffic is getting through, it's the server rejecting the connection, possibly it's because the server isn't happy with the ciphers offered by the client in the Client Hello. Later versions of Windows are less tolerant of older versions of SSL and poor ciphers.</p><p>Can you post the captures somewhere publically, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox? We only need the packets from the initial SYN to the Change Cipher Spec or Alert message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-44410" class="comments-container"><span id="44424"></span><div id="comment-44424" class="comment"><div id="post-44424-score" class="comment-score"></div><div class="comment-text"><p>It is strange that my client machine says "client hello" with SSLv2 protocol when connect to Win 2012, but with TLS to Win 2003. The only different is tcp window size. I wonder that may affect the communication protocol.</p></div><div id="comment-44424-info" class="comment-info"><span class="comment-age">(23 Jul '15, 18:07)</span> Rocky Shek</div></div><span id="44425"></span><div id="comment-44425" class="comment"><div id="post-44425-score" class="comment-score"></div><div class="comment-text"><p>There are the packet capture file of my Window 2003 and Window 2012 servers, thank you.</p><p><a href="https://drive.google.com/open?id=0B5JKgxJqOIn-eFFSeU5teVQ2eGs">https://drive.google.com/open?id=0B5JKgxJqOIn-eFFSeU5teVQ2eGs</a> <a href="https://drive.google.com/open?id=0B5JKgxJqOIn-WDRIdkxZTjZ0dDQ">https://drive.google.com/open?id=0B5JKgxJqOIn-WDRIdkxZTjZ0dDQ</a></p></div><div id="comment-44425-info" class="comment-info"><span class="comment-age">(23 Jul '15, 18:28)</span> Rocky Shek</div></div><span id="44432"></span><div id="comment-44432" class="comment"><div id="post-44432-score" class="comment-score"></div><div class="comment-text"><p>That link only seems to have the Server 2003 capture.</p></div><div id="comment-44432-info" class="comment-info"><span class="comment-age">(24 Jul '15, 09:29)</span> grahamb ♦</div></div><span id="44510"></span><div id="comment-44510" class="comment"><div id="post-44510-score" class="comment-score"></div><div class="comment-text"><p>2003 <a href="https://drive.google.com/open?id=0B5JKgxJqOIn-eFFSeU5teVQ2eGs">https://drive.google.com/open?id=0B5JKgxJqOIn-eFFSeU5teVQ2eGs</a></p><p>2012 <a href="https://drive.google.com/open?id=0B5JKgxJqOIn-WDRIdkxZTjZ0dDQ">https://drive.google.com/open?id=0B5JKgxJqOIn-WDRIdkxZTjZ0dDQ</a></p></div><div id="comment-44510-info" class="comment-info"><span class="comment-age">(26 Jul '15, 17:43)</span> Rocky Shek</div></div><span id="44516"></span><div id="comment-44516" class="comment"><div id="post-44516-score" class="comment-score"></div><div class="comment-text"><p>From the captures, the client in the Server 2K3 capture sends a TLS 1.1 handshake record containing a TLS 1.1 Client Hello message which the server is happy with.</p><p>In the Server 2K12R2 capture, the client sends an SSL 2.0 record containing a TLS 1.1 Client Hello. Quite rightly, as SSL 2.0 is <a href="https://tools.ietf.org/html/rfc6176">prohibited</a>, the server rejects the connection.<br />
</p><p>The solution is to configure the client to use an acceptable version of TLS, i.e. at least TLS 1.1 (as TLS 1.0 isn't recommended these days).</p></div><div id="comment-44516-info" class="comment-info"><span class="comment-age">(27 Jul '15, 02:23)</span> grahamb ♦</div></div><span id="44550"></span><div id="comment-44550" class="comment not_top_scorer"><div id="post-44550-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I know SSL2.0 is prohibited and should not be used anymore. But for some reason (some other systems are not administrated by me), I cannot turn down SSL2.0. I just dont understand why my client have different behavior to 2003 and 2012. The client should not know which version of OS of the server before the "hello" message, right?</p></div><div id="comment-44550-info" class="comment-info"><span class="comment-age">(27 Jul '15, 18:17)</span> Rocky Shek</div></div><span id="44558"></span><div id="comment-44558" class="comment not_top_scorer"><div id="post-44558-score" class="comment-score"></div><div class="comment-text"><p>I can't think why a client would "choose" to send SSL 2.0 to a particular server, I would think it's some form of configuration. What is the client running, OS and application?</p></div><div id="comment-44558-info" class="comment-info"><span class="comment-age">(28 Jul '15, 02:23)</span> grahamb ♦</div></div><span id="44580"></span><div id="comment-44580" class="comment not_top_scorer"><div id="post-44580-score" class="comment-score"></div><div class="comment-text"><p>Window 7, IE11 , HTTPS application</p></div><div id="comment-44580-info" class="comment-info"><span class="comment-age">(28 Jul '15, 17:46)</span> Rocky Shek</div></div><span id="44590"></span><div id="comment-44590" class="comment not_top_scorer"><div id="post-44590-score" class="comment-score"></div><div class="comment-text"><p>I'm not aware of any "per-site" configuration options for IE, you can set "global" options from IE -&gt; Internet Options -&gt; Advanced, where you can enable\disable SSL\TLS protocols. SSL 2.0 and 3.0 should be disabled (maybe TLS 1.0 as well).</p></div><div id="comment-44590-info" class="comment-info"><span class="comment-age">(29 Jul '15, 05:38)</span> grahamb ♦</div></div></div><div id="comment-tools-44410" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-44410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

