+++
type = "question"
title = "http host header with and without port number."
description = '''Here is the brief description of the issue Working condition: When client tried to use method CONNECT a.b.c.d:443 where host header is a.b.c.d:443 things went smooth. Non-working condition: When the same client tried to use method CONNECT a.b.c.d:443 where host header is just a.b.c.d(no port number)...'''
date = "2013-07-15T20:55:00Z"
lastmod = "2013-07-16T02:59:00Z"
weight = 22988
keywords = [ "header", "host", "http" ]
aliases = [ "/questions/22988" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [http host header with and without port number.](/questions/22988/http-host-header-with-and-without-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the brief description of the issue</p><p>Working condition:</p><p>When client tried to use method CONNECT a.b.c.d:443 where host header is a.b.c.d:443 things went smooth.</p><p>Non-working condition:</p><p>When the same client tried to use method CONNECT a.b.c.d:443 where host header is just a.b.c.d(no port number) we are not seeing any further SSL communication.</p><p>Is it must to specify host header with port number when the connection is not to default(port 80)?</p></div><div id="question-tags" class="tags-container tags">header host http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '13, 21:36</p></div></div><div id="comments-container-22988" class="comments-container"></div><div id="comment-tools-22988" class="comment-tools"></div><div class="clear"></div><div id="comment-22988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22996"></span>

<div id="answer-container-22996" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22996-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>CONNECT a.b.c.d:443</p></blockquote><p>CONNECT is the HTTP method used when a client requests a HTTPS connection <strong>through a proxy</strong> (usually), although it can be used to tunnel other TCP connections through a HTTP proxy as well.</p><p>It's up to the client to tell the proxy what to do (CONNECT and possibly Host header). It's up to the proxy to accept or deny that request.</p><p>So, if the request with the port in the Host header works and the other request does not work, your proxy dislikes the later for whatever reason (configuration, product limitation).</p><p>I did some tests with curl and a proxy and my proxy does not care about the port number in the Host header, at least not for the standard ports.</p><pre><code>curl adds the port number to the Host header, even for &#39;standard&#39; https requests.

C:\tools\curl&gt;curl -k  -v --proxy 172.16.200.1:8080 https://ask.wireshark.org 
* About to connect() to proxy 172.16.200.1 port 8080 (#0)
* Connected to 172.16.200.1 (172.16.200.1) port 8080 (#0)
* Establish HTTP proxy tunnel to ask.wireshark.org:443
&gt; CONNECT ask.wireshark.org:443 HTTP/1.1
&gt; Host: ask.wireshark.org:443
&gt; User-Agent: curl/7.21.3 (i386-pc-win32) libcurl/7.21.3 OpenSSL/0.9.8q zlib/1.2.5

Force a Host header without port.

C:\tools\curl&gt;curl -k  -v -H &quot;Host: ask.wireshark.org&quot; --proxy 172.16.200.1:8080
* Connected to 172.16.200.1 (172.16.200.1) port 8080 (#0)
* Establish HTTP proxy tunnel to ask.wireshark.org:443
&gt; CONNECT ask.wireshark.org:443 HTTP/1.1
&gt; Host: ask.wireshark.org
&gt; User-Agent: curl/7.21.3 (i386-pc-win32) libcurl/7.21.3 OpenSSL/0.9.8q zlib/1.2.5

Result: Both requests were accepted by the proxy.</code></pre><p>From <a href="http://www.ietf.org/rfc/rfc2616.txt">RFC 2616</a>:</p><pre><code>   The Host field value MUST represent
   the naming authority of the origin server or gateway given by the
   original URL. This allows the origin server or gateway to
   differentiate between internally-ambiguous URLs, such as the root &quot;/&quot;
   URL of a server for multiple host names on a single IP address.

       Host = &quot;Host&quot; &quot;:&quot; host [ &quot;:&quot; port ] ; Section 3.2.2

   A &quot;host&quot; without any trailing port information implies the default
   port for the service requested (e.g., &quot;80&quot; for an HTTP URL).</code></pre><p>I read this the following way: If the port in the URI/URL is different than the standard port (80,443), it must be added to the Host header as well. If it is the standard port, you 'can' add it, however it is not required.</p><blockquote><p><strong>Is it must to specify host header with port number</strong> when the connection is not to default(port 80)?</p></blockquote><p>I don't think so, if it is one of the standard ports (80,443). However, you <strong>can</strong> add it without creating problems as long as the port is the same as in the CONNECT statement.</p><p>So, your problem is probably a matter of the proxy configuration <strong>or</strong> a matter of proxy functionality. Please ask the vendor of that software.</p><p><strong>UPDATE</strong></p><p>I just tried it with a sample host on the internet (the first I found with google). Both my proxy and the server do not complain, if I omit the port number in the Host header, even if it is not one of the 'standard ports'.</p><pre><code>HINT: the output is partly anonymized

C:\tools\curl&gt;curl -k  -v --proxy 172.16.200.1:8080 -H &quot;Host: www.bbbb.org&quot; https://www.bbbb.org:8000/
* About to connect() to proxy 172.16.200.1 port 8080 (#0)
*   Trying 172.16.200.1... connected
* Connected to 172.16.200.1 (172.16.200.1) port 8080 (#0)
* Establish HTTP proxy tunnel to www.bbbb.org:8000
&gt; CONNECT www.bbbb.org:8000 HTTP/1.1
&gt; User-Agent: curl/7.21.3 (i386-pc-win32) libcurl/7.21.3 OpenSSL/0.9.8q zlib/1.2
.5
&gt; Proxy-Connection: Keep-Alive
&gt; Host: www.bbbb.org
&gt;
&lt; HTTP/1.1 200 Connection established
&lt; Connection: Keep-Alive
&lt;
* Proxy replied OK to CONNECT request
* SSLv3, TLS handshake, Client hello (1):
* SSLv3, TLS handshake, Server hello (2):
* SSLv3, TLS handshake, CERT (11):
* SSLv3, TLS handshake, Server finished (14):
* SSLv3, TLS handshake, Client key exchange (16):
* SSLv3, TLS change cipher, Client hello (1):
* SSLv3, TLS handshake, Finished (20):
* SSLv3, TLS change cipher, Client hello (1):
* SSLv3, TLS handshake, Finished (20):
* SSL connection using AES256-SHA
* Server certificate:
*        subject: C=US; ST=OHIO; L=CLEVELAND; O=BBBBBBB; CN=www.bbbb.org
*        start date: 2013-05-09 00:00:00 GMT
*        expire date: 2015-07-02 23:59:59 GMT
*        subjectAltName: www.bbbb.org matched
*        issuer: C=US; O=Thawte, Inc.; CN=Thawte SGC CA - G2
*        SSL certificate verify result: self signed certificate in certificate c
hain (19), continuing anyway.
&gt; GET / HTTP/1.1
&gt; User-Agent: curl/7.21.3 (i386-pc-win32) libcurl/7.21.3 OpenSSL/0.9.8q zlib/1.2
.5
&gt; Accept: */*
&gt; Host: www.bbbb.org
&gt;
&lt; HTTP/1.1 200 OK
&lt; Date: Tue, 16 Jul 2013 10:28:01 GMT
&lt; Last-Modified: Sun, 09 Jun 2013 03:12:02 GMT
&lt; ETag: &quot;0-50e-51b3f282&quot;
&lt; Accept-Ranges: bytes
&lt; Content-Length: 1294
&lt; Content-Type: text/html
&lt;

&lt;html&gt;
&lt;head&gt;
&lt;title&gt;E-Business Suite Home Page Redirect&lt;/title&gt;
&lt;meta http-equiv=&quot;REFRESH&quot; content=&quot;1; URL=&amp;lt;a href=&quot; https:=&quot;&quot; www.bbbb.org:8000=&quot;&quot; oa_html=&quot;&quot; appslogin&quot;=&quot;&quot;&gt;&quot;&gt;https://www.bbbb.org:8000/OA_HTML/AppsLogin&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
REMOVED
&lt;/body&gt;
&lt;/html&gt;
 * Connection #0 to host 172.16.200.1 left intact
 * Closing connection #0
 * SSLv3, TLS alert, Client hello (1):
</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '13, 05:52</p></div></div><div id="comments-container-22996" class="comments-container"><span id="23030"></span><div id="comment-23030" class="comment"><div id="post-23030-score" class="comment-score"></div><div class="comment-text"><p>Kurt, Extremely thankful for your reply.This is igniting interest to keep on learning/contributing from/to this community.I will check with the vendor of that software for any anomaly and update the thread. Thanks again.</p></div><div id="comment-23030-info" class="comment-info"><span class="comment-age">(16 Jul '13, 07:39)</span> krishnayeddula</div></div><span id="23034"></span><div id="comment-23034" class="comment"><div id="post-23034-score" class="comment-score"></div><div class="comment-text"><blockquote><p>.I will check with the vendor of that software for any anomaly and update the thread.</p></blockquote><p>Thanks!</p><p>BTW: Just for my interest. Is it possible to name the vendor here?</p></div><div id="comment-23034-info" class="comment-info"><span class="comment-age">(16 Jul '13, 07:46)</span> Kurt Knochner ♦</div></div><span id="23042"></span><div id="comment-23042" class="comment"><div id="post-23042-score" class="comment-score"></div><div class="comment-text"><p>I'm interested in the answer of their support. I guess (based on experience with all kinds of vendors), they will first claim, that it is not RFC compliant to omit the port. And I'm not really sure either (see above).</p></div><div id="comment-23042-info" class="comment-info"><span class="comment-age">(16 Jul '13, 08:05)</span> Kurt Knochner ♦</div></div><span id="23048"></span><div id="comment-23048" class="comment"><div id="post-23048-score" class="comment-score"></div><div class="comment-text"><p>Kurt i just deleted the application vendor name for privacy reasons(my friend is following this thread too:))I will get back to you once the proxy folks respond to this issue.</p></div><div id="comment-23048-info" class="comment-info"><span class="comment-age">(16 Jul '13, 08:16)</span> krishnayeddula</div></div></div><div id="comment-tools-22996" class="comment-tools"></div><div class="clear"></div><div id="comment-22996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

