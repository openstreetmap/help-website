+++
type = "question"
title = "Http Soap transaction not clear when using Follow Streem"
description = '''Hi, I am tring to debug a webservice, I use SoapUI to send the request to a webservice, the response message is readable XML in SoapUI, but in wireshark using follow streem, request is readable , response is in binary.  Request: POST /fndint/soapgateway HTTP/1.1 Accept-Encoding: gzip,deflate Content...'''
date = "2014-08-19T02:47:00Z"
lastmod = "2014-08-19T04:29:00Z"
weight = 35557
keywords = [ "follow", "streem" ]
aliases = [ "/questions/35557" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Http Soap transaction not clear when using Follow Streem](/questions/35557/http-soap-transaction-not-clear-when-using-follow-streem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am tring to debug a webservice, I use SoapUI to send the request to a webservice, the response message is readable XML in SoapUI, but in wireshark using follow streem, request is readable , response is in binary.</p><p><code> Request: POST /fndint/soapgateway HTTP/1.1 Accept-Encoding: gzip,deflate Content-Type: text/xml;charset=UTF-8 SOAPAction: "urn:soap_access_provider:MoboffHandlePurchReq:ReceiveRetailPurchReq/post" Content-Length: 11099 Host: lkpvmpe1767.corpnet.ifsworld.com:58080 Connection: Keep-Alive User-Agent: Apache-HttpClient/4.1.1 (java 1.5) Authorization: Basic aWZzYXBwOmlmc2FwcGJudA==</code></p><code></code><p>Response: HTTP/1.1 200 OK Date: Tue, 19 Aug 2014 07:31:05 GMT Server: Oracle-Application-Server-12c Set-Cookie: JSESSIONID=WKztLShFU8Avi6L7BrGNOPAofrYIqVqmoqQw7DVmYQEBcfhV8D63!807751062; path=/; HttpOnly X-Powered-By: Servlet/3.0 JSP/2.2 Vary: Accept-Encoding Content-Encoding: gzip Keep-Alive: timeout=5, max=99 Connection: Keep-Alive Transfer-Encoding: chunked Content-Type: text/xml; charset="UTF-8" Content-Language: en</p><p>d6 [email protected](.....*./fA.-..m.}S.PHn...</p><h1 id="q38.hb.....n....x....u.r.i..r3.....gh..m...s......66d.._..r.....b........f.8...">..q`38.hb.!.|...N.&gt;...,x....U.R.i..R3.....gH..;M...S{......66D.._..R.....b......"..?f.}8#..&gt;.</h1></code><p><code>]..(.P...k.d..xj.DM.l..z...ib.i..M...bSge..K~.P..L..c...... a ...(...... 0</code></p><p>Why is that ?</p><p>Many thanks in advance!</p><p>George</p></div><div id="question-tags" class="tags-container tags">follow streem</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/6f337ee7d0b098b525d194d5238c9939?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeX&#39;s gravatar image" /><p>GeorgeX<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeX has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '14, 03:28</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35557" class="comments-container"><span id="35558"></span><div id="comment-35558" class="comment"><div id="post-35558-score" class="comment-score"></div><div class="comment-text"><p>I have omitted the request XML since it will not show the element names in the forum posts, could not fins a plain text mode ...</p></div><div id="comment-35558-info" class="comment-info"><span class="comment-age">(19 Aug '14, 02:50)</span> GeorgeX</div></div><span id="35562"></span><div id="comment-35562" class="comment"><div id="post-35562-score" class="comment-score"></div><div class="comment-text"><p>The tags &lt; code &gt;&lt; /code &gt; format text as code, but still don't get it all correct. Note that there are no spaces in the real tags.</p></div><div id="comment-35562-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:29)</span> grahamb ♦</div></div><span id="35566"></span><div id="comment-35566" class="comment"><div id="post-35566-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the information, however, the request XML is not important to show in this post since the main problem is why wire shark does not interpret the response XML message correct and Soap UI gives a clear response message ? Is there a decoding flag that I should enable in WireShar to decode the response ?</p><p>Thanks</p></div><div id="comment-35566-info" class="comment-info"><span class="comment-age">(19 Aug '14, 04:06)</span> GeorgeX</div></div></div><div id="comment-tools-35557" class="comment-tools"></div><div class="clear"></div><div id="comment-35557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35569"></span>

<div id="answer-container-35569" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35569-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Coz it's gzipped?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35569" class="comments-container"><span id="35572"></span><div id="comment-35572" class="comment"><div id="post-35572-score" class="comment-score"></div><div class="comment-text"><p>Yes, it can be, is there any option in WireShark to show it unzipped?</p></div><div id="comment-35572-info" class="comment-info"><span class="comment-age">(19 Aug '14, 05:28)</span> GeorgeX</div></div><span id="35573"></span><div id="comment-35573" class="comment"><div id="post-35573-score" class="comment-score"></div><div class="comment-text"><p>PaulOfford: You are right! content is gzipped according to the http Content-Encoding parameter. Thanks for that. I am not sure if it is possible to show the gazipped content in WireShark ??</p><p>George</p></div><div id="comment-35573-info" class="comment-info"><span class="comment-age">(19 Aug '14, 05:34)</span> GeorgeX</div></div><span id="35574"></span><div id="comment-35574" class="comment"><div id="post-35574-score" class="comment-score"></div><div class="comment-text"><p>Solved: I set Response Compression = False in SoapUI in the request so that the response comes in plain XML!</p><p>Thanks all!</p></div><div id="comment-35574-info" class="comment-info"><span class="comment-age">(19 Aug '14, 05:53)</span> GeorgeX</div></div></div><div id="comment-tools-35569" class="comment-tools"></div><div class="clear"></div><div id="comment-35569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

