+++
type = "question"
title = "SSL Stream Order of Conversation"
description = '''I&#x27;m trying to decipher why my HTTP POST connection works but HTTPS POST will not. When doing HTTPS, the SSL stream seems to indicate the server responds prior to all of the headers being provided. I&#x27;m wondering if the SSL Stream is showing me the true order in which packets are being transmitted. Cl...'''
date = "2016-02-09T13:10:00Z"
lastmod = "2016-02-09T13:47:00Z"
weight = 50027
keywords = [ "ssl" ]
aliases = [ "/questions/50027" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Stream Order of Conversation](/questions/50027/ssl-stream-order-of-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50027-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decipher why my HTTP POST connection works but HTTPS POST will not. When doing HTTPS, the SSL stream seems to indicate the server responds prior to all of the headers being provided. I'm wondering if the SSL Stream is showing me the true order in which packets are being transmitted.</p><p>Client:</p><pre><code>POST  HTTP/1.0
Content-type: text/xml
Content-length: 1505
host: somewhere.com:443</code></pre><p>Server:</p><pre><code>HTTP/1.1 400 Bad Request
Content-Type: text/html; charset=us-ascii
Server: Microsoft-HTTPAPI/2.0
Date: Fri, 05 Feb 2016 19:16:31 GMT
Connection: close
Content-Length: 324

&lt; !DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.01//EN&quot;&quot;http://www.w3.org/TR/html4/strict.dtd&quot;&gt;
&lt; HTML&gt;&lt; HEAD&gt;&lt; TITLE&gt;Bad Request&lt; /TITLE&gt;
&lt; META HTTP-EQUIV=&quot;Content-Type&quot; Content=&quot;text/html; charset=us-ascii&quot;&gt;&lt; /HEAD&gt;
&lt; BODY&gt;&lt; h2&gt;Bad Request - Invalid URL&lt; /h2&gt;
&lt;hr&gt;&lt;p&gt;HTTP Error 400. The request URL is invalid.&lt;/p&gt;
&lt; /BODY&gt;&lt; /HTML&gt;</code></pre><p>Client:</p><pre><code>&lt; ?xml version = &#39;1.0&#39; encoding = &#39;UTF-8&#39;?&gt;
And so on...</code></pre></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '16, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/2f45d8323539ec40d081e4c4b5af282c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chad%20Bozeman&#39;s gravatar image" /><p>Chad Bozeman<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chad Bozeman has no accepted answers">0%</span></p></div></div><div id="comments-container-50027" class="comments-container"></div><div id="comment-tools-50027" class="comment-tools"></div><div class="clear"></div><div id="comment-50027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50030"></span>

<div id="answer-container-50030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50030-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can imagine that the server answers as soon as it has got enough information to decide to reject the request and that the client does not get (or process) the response early enough to stop sending the rest of the message. Can you provide the timestamp information for the individual packets, and if you send the POST from the same client to the same server as both http and https, can you compare the headers of the POST messages in both cases?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50030" class="comments-container"><span id="50054"></span><div id="comment-50054" class="comment"><div id="post-50054-score" class="comment-score"></div><div class="comment-text"><p>I was able to verify as you suggested that the server is responding as soon as it has enough information to reject.</p><p>The server is a different VM than the client. I've tried both from within my Network and coming from the internet with the same results. I'll go back and see if I can pull the headers for both test cases.</p></div><div id="comment-50054-info" class="comment-info"><span class="comment-age">(10 Feb '16, 07:28)</span> Chad Bozeman</div></div><span id="50056"></span><div id="comment-50056" class="comment"><div id="post-50056-score" class="comment-score"></div><div class="comment-text"><p>The "same" was related to "same client for both http and https", not "client and server processes running at the same machine". I.e. more or less I wanted to point your attention to whether the client application and its configuration is the same for both http and https requests or whether you send http from one client application and https from another client application, with possibly different behaviour and settings, and the fact that the use of tls may not be the real reason of different reaction of the server.</p></div><div id="comment-50056-info" class="comment-info"><span class="comment-age">(10 Feb '16, 07:39)</span> sindy</div></div></div><div id="comment-tools-50030" class="comment-tools"></div><div class="clear"></div><div id="comment-50030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

