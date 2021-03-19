+++
type = "question"
title = "SSL handshake fails when TLS V1.2 is used but passes in SSLv3"
description = '''Hello,  When a SSL Handshake is made using SSLV3 protocol, the handshake passes and data is transmitted successfully. When I change the protocol to TLSV1.2, the handshake fails. To make it work, I used a different server certificate and the TLS V1.2 handshake passes.  The difference between the cert...'''
date = "2014-06-20T00:36:00Z"
lastmod = "2014-06-21T17:21:00Z"
weight = 33981
keywords = [ "ssl_connection" ]
aliases = [ "/questions/33981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL handshake fails when TLS V1.2 is used but passes in SSLv3](/questions/33981/ssl-handshake-fails-when-tls-v12-is-used-but-passes-in-sslv3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33981-score" class="post-score" title="current number of votes">0</div><span id="post-33981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, When a SSL Handshake is made using SSLV3 protocol, the handshake passes and data is transmitted successfully. When I change the protocol to TLSV1.2, the handshake fails. To make it work, I used a different server certificate and the TLS V1.2 handshake passes. The difference between the certificate is that, the earlier certificate had non ascii characters in the Issuer DN which were encoded in BMPString. The new certificate I use does not have special characters in Issuer DN.</p><p>Can anybody of you provide me a clue as to what could be wrong here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_connection" rel="tag" title="see questions tagged &#39;ssl_connection&#39;">ssl_connection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/9c79946fe752bba30b502620de06fded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="priya&#39;s gravatar image" /><p><span>priya</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="priya has no accepted answers">0%</span></p></div></div><div id="comments-container-33981" class="comments-container"></div><div id="comment-tools-33981" class="comment-tools"></div><div class="clear"></div><div id="comment-33981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34025"></span>

<div id="answer-container-34025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34025-score" class="post-score" title="current number of votes">0</div><span id="post-34025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The difference between the certificate is that, the earlier certificate had non ascii characters in the Issuer DN which were encoded in BMPString.</p></blockquote><p>Sounds like a problem in your clients TLS1.2 implementation that does not like a BMPstring in the issuer DN.</p><p>Some questions about your client</p><ul><li>OS and OS version</li><li>Client software and version</li></ul><p>BTW: There has been a similar question recently, also related to BMPstring encoded characters in the issuer DN:</p><blockquote><p><a href="http://ask.wireshark.org/questions/33236/ssl-handshake-failure-when-using-a-certificate-that-contains-non-ascii-characters-in-issuer-dn">http://ask.wireshark.org/questions/33236/ssl-handshake-failure-when-using-a-certificate-that-contains-non-ascii-characters-in-issuer-dn</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '14, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34025" class="comments-container"></div><div id="comment-tools-34025" class="comment-tools"></div><div class="clear"></div><div id="comment-34025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

