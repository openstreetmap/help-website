+++
type = "question"
title = "RST+ACK That is NOT Response to SYN on Closed Port"
description = '''I&#x27;m seeing RST+ACK received at a PC, often, and it is not a response to a SYN sent to a closed port. In one case, the PC opened a TCP session, sent HTTP 1.1 traffic in a TLS session, got a response, ACKed the response. The connection sat idle for 130 seconds and then the host sent RST+ACK. In anothe...'''
date = "2012-03-20T13:31:00Z"
lastmod = "2012-03-20T14:15:00Z"
weight = 9659
keywords = [ "rst", "ack" ]
aliases = [ "/questions/9659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RST+ACK That is NOT Response to SYN on Closed Port](/questions/9659/rstack-that-is-not-response-to-syn-on-closed-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing RST+ACK received at a PC, often, and it is <em>not</em> a response to a SYN sent to a closed port.</p><p>In one case, the PC opened a TCP session, sent HTTP 1.1 traffic in a TLS session, got a response, ACKed the response. The connection sat idle for 130 seconds and then the host sent RST+ACK.</p><p>In another case, the server sends data in a TLS session, the PC ACKs it, and then the PC sends FIN+ACK. The server responds with RST+ACK.</p><p>If the server were unhappy with the TCP session, I'd expect RST without ACK. It appears to be using RST+ACK instead of FIN+ACK. There are firewalls/load-balancer between the PC and the server.</p><p>This doesn't look like a half-open session. What would cause RST+ACK in the absence of an attempt to connect to a closed port?</p></div><div id="question-tags" class="tags-container tags">rst ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '12, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/85e9029cdf9f984bb439da542ea514fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kleinfelter&#39;s gravatar image" /><p>Kleinfelter<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kleinfelter has no accepted answers">0%</span></p></div></div><div id="comments-container-9659" class="comments-container"></div><div id="comment-tools-9659" class="comment-tools"></div><div class="clear"></div><div id="comment-9659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9663"></span>

<div id="answer-container-9663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9663-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seeing TCP/RST packets in SSL traffic is not uncommon. While "the world shouldn't be like that", fact is that Microsoft Internet Explorer used to be not-so-great in handling persistent SSL sessions, so webservers started to use the "unclean-shutdown" option to not frustrate the MS-IE users (instead of making sure MS solved the bug in their browser. The unclean shutdown meant to no use the SSL CloseNotify Alert to close the SSL session before tearing down the TCP session with a FIN, but the kill the session straight away with a RST.</p><p>Have a search on ssl-unclean-shutdown or take a look at the <a href="http://httpd.apache.org/docs/2.0/ssl/ssl_faq.html">Apache SSL FAQ</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9663" class="comments-container"></div><div id="comment-tools-9663" class="comment-tools"></div><div class="clear"></div><div id="comment-9663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

