+++
type = "question"
title = "Decrypting a WCF response"
description = '''Hi all, What would be the possible reasons for wireshark not showing a decrypted WCF response? I have successfully decrypted the request information from a WCF service for dummies, but can&#x27;t get the response to be decrypted. This are the frames of interest:  74 -60.405045 52.171.130.206 100.75.14.89...'''
date = "2017-07-24T09:29:00Z"
lastmod = "2017-10-17T10:05:00Z"
weight = 63051
keywords = [ "ssl", "decrypt", "wcf" ]
aliases = [ "/questions/63051" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting a WCF response](/questions/63051/decrypting-a-wcf-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63051-score" class="post-score" title="current number of votes">0</div><span id="post-63051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>What would be the possible reasons for wireshark not showing a decrypted WCF response? I have successfully decrypted the request information from a WCF service for dummies, but can't get the response to be decrypted.</p><p>This are the frames of interest:</p><p><code> 74  -60.405045  52.171.130.206  100.75.14.89    HTTP/XML    288 POST /Service1.svc HTTP/1.1  75  -60.404223  100.75.14.89    52.171.130.206  TLSv1   576 [SSL segment of a reassembled PDU], Application Data</code></p><p>Looking at the request frame detail, this is what I get (which is ok):</p><p><code>POST /Service1.svc HTTP/1.1 Content-Type: text/xml; charset=utf-8 SOAPAction: "http://tempuri.org/IService1/GetData" Host: myazurecloudservice2.cloudapp.net Content-Length: 157 Expect: 100-continue Accept-Encoding: gzip, deflate Connection: Keep-Alive</code></p><code></code><p><code>&lt;s:envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"&gt;&lt;s:body&gt;&lt;getdata xmlns="http://tempuri.org/"&gt;&lt;value&gt;0&lt;/value&gt;&lt;/getdata&gt;&lt;/s:body&gt;&lt;/s:envelope&gt;</code></p><p>But I still can't see the decrypted response. What am I missing?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-wcf" rel="tag" title="see questions tagged &#39;wcf&#39;">wcf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '17, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/eb41b13f47ec46a2a36a9d90db519094?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c4rlosmarin&#39;s gravatar image" /><p><span>c4rlosmarin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c4rlosmarin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '17, 10:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-63051" class="comments-container"></div><div id="comment-tools-63051" class="comment-tools"></div><div class="clear"></div><div id="comment-63051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63066"></span>

<div id="answer-container-63066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63066-score" class="post-score" title="current number of votes">0</div><span id="post-63066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some checks you could perform to investigate why the decrypted data is not shown:</p><ol><li>Check the <em>Decrypted SSL</em> byte view tab (normally at the bottom of the screen) for the Content-Length header. From this you will learn how much data to expect. If it is a small value, it will probably fit in a few frames. If there is no <em>Decrypted SSL</em> (or <em>Decrypted SSL data</em> in Wireshark 2.2 and before), then it indicates that decryption failed for some reason.</li><li>"SSL segment of a reassembled PDU" indicates that the response has not been fully received yet, it will be fully reassembled in a later packet. But when TCP segments appear out-of-order, then it will mess up the dissection and decryption state. If this happens, decryption will fail and the response will not be shown.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '17, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-63066" class="comments-container"><span id="63105"></span><div id="comment-63105" class="comment"><div id="post-63105-score" class="comment-score"></div><div class="comment-text"><p>Hi Lekensteyn,</p><p>Decrypted SSL byte view tab is just showing "48 H":</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_u1DGhqW.png" width="640" /></p><p><a href="https://1drv.ms/f/s!AgD0z8JsfL_7gscjy_4HyljWHMO3ng">Here</a> is the information from the SSL debug file</p><p>By the way, that last one (frame 61) is the only frame the server sends for the wcf response, the client successfully gets the response but the trace from the server doesn't show it as a decrypted packet.</p><p>Thanks!</p></div><div id="comment-63105-info" class="comment-info"><span class="comment-age">(25 Jul '17, 13:46)</span> <span class="comment-user userinfo">c4rlosmarin</span></div></div><span id="63216"></span><div id="comment-63216" class="comment"><div id="post-63216-score" class="comment-score"></div><div class="comment-text"><p>I suppose the <code>H</code> is part of the headers, starting with <code>HTTP/1.1 200 OK</code>. Indeed, the decrypted data is shown on the first pass, but not in the second one. Can you file a bug report with the attached pcap?</p></div><div id="comment-63216-info" class="comment-info"><span class="comment-age">(28 Jul '17, 07:21)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="63388"></span><div id="comment-63388" class="comment"><div id="post-63388-score" class="comment-score">1</div><div class="comment-text"><p>Hi Lekensteyn,</p><p>I've submitted a bug with the required information: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13943">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13943</a></p><p>Cheers!</p></div><div id="comment-63388-info" class="comment-info"><span class="comment-age">(03 Aug '17, 13:05)</span> <span class="comment-user userinfo">c4rlosmarin</span></div></div><span id="63975"></span><div id="comment-63975" class="comment"><div id="post-63975-score" class="comment-score"></div><div class="comment-text"><p>Related to bug 13943, version 2.4.2 is actually not showing any wcf response at all. I've attached the screenshot of what I see as well as the trace and the self-signed certificate.</p><p>Since bug 13943 was declared as duplicate, I've submitted the information for bug 13885 (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13885)">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13885)</a></p><p>Cheers!</p></div><div id="comment-63975-info" class="comment-info"><span class="comment-age">(17 Oct '17, 10:05)</span> <span class="comment-user userinfo">c4rlosmarin</span></div></div></div><div id="comment-tools-63066" class="comment-tools"></div><div class="clear"></div><div id="comment-63066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

