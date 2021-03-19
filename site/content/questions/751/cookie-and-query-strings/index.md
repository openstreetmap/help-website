+++
type = "question"
title = "cookie and query strings"
description = '''Cookies: What&#x27;s a good way to find/locate/identify cookie transactions in the capture? Both for http and https transactions? (I know https should be hidden but I ask/include just for any additional clarification.)  Any idea the general frame/packet size of a cookie, i.e., how often then may exceed a...'''
date = "2010-10-30T18:51:00Z"
lastmod = "2010-10-31T02:25:00Z"
weight = 751
keywords = [ "cookie" ]
aliases = [ "/questions/751" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [cookie and query strings](/questions/751/cookie-and-query-strings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Cookies:</p><p>What's a good way to find/locate/identify cookie transactions in the capture? Both for http and https transactions? (I know https should be hidden but I ask/include just for any additional clarification.)</p><p>Any idea the general frame/packet size of a cookie, i.e., how often then may exceed a single packet (up to four are possible?)</p><p>Query Strings: As I understand query strings, they can serve nearly the same purpose of a cookie thereby replacing them, would there use prevent a sidejacking/hijacking or cookiemonster attack? And can both a query string and cookie be used simultaneously.</p><p>I'd like to identify either or both in entirety for a capture.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">cookie</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '10, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/d77dc7b32b12e8d1692a181f3684db11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bit4byte&#39;s gravatar image" /><p>bit4byte<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bit4byte has no accepted answers">0%</span></p></div></div><div id="comments-container-751" class="comments-container"></div><div id="comment-tools-751" class="comment-tools"></div><div class="clear"></div><div id="comment-751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="752"></span>

<div id="answer-container-752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-752-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTPS sessions should be encrypted (unless you have applied a decryption key) and therefore you won't be able to use Find or a display filter to locate packets with cookies set.</p><p>Try using <code>frame contains "Cookie"</code> as a display filter. You'll see all HTTP traffic that contains a Set-Cookie field. Use <code>frame contains "GET"</code> to locate all the HTTP Get requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '10, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Oct '10, 19:00</p></div></div><div id="comments-container-752" class="comments-container"></div><div id="comment-tools-752" class="comment-tools"></div><div class="clear"></div><div id="comment-752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="756"></span>

<div id="answer-container-756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First some theoretical backgraound:</p><ul><li><p><strong>Cookies:</strong> Cookies are a way for a HTTP server to store information on the client, which will be presented back to the server in following requests. The purpose is to have a way of maintaining information between the client and the server to simulate a session (http by itself has no notion of sessions, it's just a way to exchange objects).</p></li><li><p><strong>Query Strings:</strong> A query string is a way for the client to submit (dynamic) data to the server. Mostly this is done by having a FORM on a webpage that can be filled in and when it's submitted the filled in values are transferred to the server in the "Query String". This can be done with the GET method, in which the query string will be added to the requested URL. Or it can be done with the POST method in which the query string will be sent as HTTP data, after the HTTP headers.</p></li></ul><p>Both Cookies and Query Strings are completely independent of each other, but are widely used together. The way they are used depends on the way the web application has been written.</p><p>To filter all requests that contain a cookie, use:</p><pre><code>http.cookie
http.cookie contains &lt;cookiename&gt;</code></pre><p>To filter for query strings:</p><pre><code>http.request.uri contains &quot;?&quot; or http.request.method==&quot;POST&quot;</code></pre><p>This of course only works with HTTP as HTTPS traffic is encrypted. However, if you do have access to the private key used on the HTTPS server, you are able to decrypt the HTTPS traffic which makes the HTTP traffic inside the HTTPS traffic visible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '10, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-756" class="comments-container"></div><div id="comment-tools-756" class="comment-tools"></div><div class="clear"></div><div id="comment-756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

