+++
type = "question"
title = "Certificate Request Size Change"
description = '''I have two deployments, one is a Virtual Machine, and other is a desktop. I am using WireShark to capture the certificate handshake traffic between a mobile device using SSL to each deployment one at a time.  For the virtual machine deployment on cloud --&amp;gt; Device Certificate handshake the size of...'''
date = "2013-08-21T13:49:00Z"
lastmod = "2013-08-26T06:09:00Z"
weight = 23929
keywords = [ "tls", "ssl", "network", "certificate" ]
aliases = [ "/questions/23929" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Certificate Request Size Change](/questions/23929/certificate-request-size-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23929-score" class="post-score" title="current number of votes">0</div><span id="post-23929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two deployments, one is a Virtual Machine, and other is a desktop. I am using WireShark to capture the certificate handshake traffic between a mobile device using SSL to each deployment one at a time. For the virtual machine deployment on cloud --&gt; Device Certificate handshake the size of "certificate Request" is 2374 Bytes. For Desktop connected via LAN to device size of ceritificate is 16000 Bytes.</p><p>Why is there a huge size difference?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/389ef5755273f1efbae2adbcc75e45cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mustafa%20El-Hilo&#39;s gravatar image" /><p><span>Mustafa El-Hilo</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mustafa El-Hilo has no accepted answers">0%</span></p></div></div><div id="comments-container-23929" class="comments-container"><span id="23932"></span><div id="comment-23932" class="comment"><div id="post-23932-score" class="comment-score"></div><div class="comment-text"><p>Certificate Request is NOT the same as Certificate. Without seeing the actual packets it's hard to explain the difference. How about loading it to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a></p></div><div id="comment-23932-info" class="comment-info"><span class="comment-age">(21 Aug '13, 14:09)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="23953"></span><div id="comment-23953" class="comment"><div id="post-23953-score" class="comment-score"></div><div class="comment-text"><p>I understand the difference between certificate and certificate request. Why is the certificate request change in size? should they be the same?</p></div><div id="comment-23953-info" class="comment-info"><span class="comment-age">(22 Aug '13, 05:34)</span> <span class="comment-user userinfo">Mustafa El-Hilo</span></div></div><span id="23974"></span><div id="comment-23974" class="comment"><div id="post-23974-score" class="comment-score"></div><div class="comment-text"><p>Ok, so you're saying the 'Certificate Request' is 2374 bytes in size when your server runs in the cloud? Or is it the server "Certificate (chain)"?</p><p>And when the server runs on a desktop, the "Certificate (chain)" is 16000 bytes?</p><p>Instead of guessing it would really help if you'd paste a trace snippet or hardcopy of the SSL Handshake...</p><p>BTW. Does the handshake succeed?</p></div><div id="comment-23974-info" class="comment-info"><span class="comment-age">(23 Aug '13, 04:14)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="23977"></span><div id="comment-23977" class="comment"><div id="post-23977-score" class="comment-score"></div><div class="comment-text"><p>Page 47 in <a href="http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf">http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf</a> shows a Certificate Request with a reasonable length of 159 bytes</p></div><div id="comment-23977-info" class="comment-info"><span class="comment-age">(23 Aug '13, 05:35)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="23980"></span><div id="comment-23980" class="comment"><div id="post-23980-score" class="comment-score"></div><div class="comment-text"><p>The certificate Request specifically, and i can't post any wireshark snippets due to security reasons. And for both cases the ssl is completed successfully. I am wonderning if on the VM, since it has a virtual network card, it is not capturing all packets.</p></div><div id="comment-23980-info" class="comment-info"><span class="comment-age">(23 Aug '13, 06:30)</span> <span class="comment-user userinfo">Mustafa El-Hilo</span></div></div></div><div id="comment-tools-23929" class="comment-tools"></div><div class="clear"></div><div id="comment-23929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23988"></span>

<div id="answer-container-23988" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23988-score" class="post-score" title="current number of votes">1</div><span id="post-23988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mustafa El-Hilo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The certificate request advertises CA's for the client to pick the right client certificate. This is done by listing the Distinguished Name (DN) of each certificate in the certificate bundle that was configured on the server.</p><p>So I suspect that the configuration of the webserver in the cloud is listing just a couple of CA's which are under it's administrative domain and the webserver on your own system is listing all the Root CA's in your trust store.</p><p>Have a look at the CertficateRequest and look at the DN's to see if they indeed take up most space of the SSL record.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '13, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23988" class="comments-container"><span id="24058"></span><div id="comment-24058" class="comment"><div id="post-24058-score" class="comment-score"></div><div class="comment-text"><p>That was the answer i was looking for. Thanks.</p></div><div id="comment-24058-info" class="comment-info"><span class="comment-age">(26 Aug '13, 06:09)</span> <span class="comment-user userinfo">Mustafa El-Hilo</span></div></div></div><div id="comment-tools-23988" class="comment-tools"></div><div class="clear"></div><div id="comment-23988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23986"></span>

<div id="answer-container-23986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23986-score" class="post-score" title="current number of votes">0</div><span id="post-23986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So to summarize: the TLS handshake succeeds in both cases, the server running on a desktop and the server running in the clud (VM). The difference is in the size of Certifcate Request (or is it the certificate chain) and the question(s) is (are)<br />
</p><ul><li>Why is there a huge difference in size? Why (is) does the certificate request change in size?</li><li>Should they be the same?</li></ul><p>Since you can't provide the two "certificate requests" due to security/privacy concerns I (we) can not comment on question number one.</p><p>As for question number 2, the answer is 'No' as the handshake succeeds either way so obviously it is a valid TLS/SSL handshake procedure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '13, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-23986" class="comments-container"></div><div id="comment-tools-23986" class="comment-tools"></div><div class="clear"></div><div id="comment-23986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

