+++
type = "question"
title = "How can Wireshark indicate SSL Application Data as HTTP?"
description = '''Hi all I am analyzing a captured TLS/SSL session with Wireshark. Although I know that its a HTTPS session I wonder how Wireshark can indicate the Application Data as HTTP too. Every since the record structure for Application Data provides Content Type (23) and Application Data Length only! Example: ...'''
date = "2012-08-14T07:08:00Z"
lastmod = "2012-08-14T08:05:00Z"
weight = 13612
keywords = [ "tlsv1", "https" ]
aliases = [ "/questions/13612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can Wireshark indicate SSL Application Data as HTTP?](/questions/13612/how-can-wireshark-indicate-ssl-application-data-as-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13612-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I am analyzing a captured TLS/SSL session with Wireshark. Although I <em>know</em> that its a HTTPS session I wonder how Wireshark can indicate the Application Data as HTTP too. Every since the record structure for Application Data provides Content Type (23) and Application Data Length only!</p><p>Example: SSLv3 Record Layer: Application Data Protocol: http</p><p>Any help on this is very much appreciated! Thanks</p></div><div id="question-tags" class="tags-container tags">tlsv1 https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/61c95efeac4800444afcb238010de35f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sky21&#39;s gravatar image" /><p>sky21<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sky21 has no accepted answers">0%</span></p></div></div><div id="comments-container-13612" class="comments-container"></div><div id="comment-tools-13612" class="comment-tools"></div><div class="clear"></div><div id="comment-13612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13615"></span>

<div id="answer-container-13615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13615-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I wonder how Wireshark can indicate the Application Data as HTTP too</p></blockquote><p>it cannot. That peace of information is just added by the HTTP dissector while registering the SSL dissector to handle SSL/TLS sessions.</p><p>See:</p><blockquote><p><code>packet-http.c -&gt; range_add_http_ssl_callback()</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '12, 08:07</p></div></div><div id="comments-container-13615" class="comments-container"><span id="13670"></span><div id="comment-13670" class="comment"><div id="post-13670-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt and thanks for the information so far!</p><p>But... how DOES the SSL dissector know, that it encapsulates an encrypted HTTP content? Is it because of the target tcp port 443 (...which might indicate that HTTPS service is used)?</p></div><div id="comment-13670-info" class="comment-info"><span class="comment-age">(15 Aug '12, 22:32)</span> sky21</div></div><span id="13673"></span><div id="comment-13673" class="comment"><div id="post-13673-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment, please reread the FAQ)</p><p>Yes, Identification is done based on the port number. The HTTP dissector tells the SSL dissector that all traffic on port 443 is encrypted HTTP traffic. Even though it might not be.</p></div><div id="comment-13673-info" class="comment-info"><span class="comment-age">(15 Aug '12, 23:50)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13615" class="comment-tools"></div><div class="clear"></div><div id="comment-13615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

