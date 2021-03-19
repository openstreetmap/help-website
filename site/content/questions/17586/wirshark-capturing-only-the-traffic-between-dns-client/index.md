+++
type = "question"
title = "Wirshark capturing only the traffic between DNS &amp; Client"
description = '''While capturing the traffic using Wireshark, it captures only the traffic between the Client &amp;amp; the DNS server. We want to capture the traffic between the Client and the actual application server.  In addition to that, the application we are trying to capture is SSL, in this case, we need to prov...'''
date = "2013-01-08T21:16:00Z"
lastmod = "2013-01-10T13:18:00Z"
weight = 17586
keywords = [ "ssl", "dns" ]
aliases = [ "/questions/17586" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wirshark capturing only the traffic between DNS & Client](/questions/17586/wirshark-capturing-only-the-traffic-between-dns-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While capturing the traffic using Wireshark, it captures only the traffic between the Client &amp; the DNS server. We want to capture the traffic between the Client and the actual application server. In addition to that, the application we are trying to capture is SSL, in this case, we need to provide the certificate of the application server or the DNS server. I'm confused.</p></div><div id="question-tags" class="tags-container tags">ssl dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '13, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/93be616bb452d0870e102f45c1dd7bf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="madan&#39;s gravatar image" /><p>madan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="madan has no accepted answers">0%</span></p></div></div><div id="comments-container-17586" class="comments-container"></div><div id="comment-tools-17586" class="comment-tools"></div><div class="clear"></div><div id="comment-17586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17588"></span>

<div id="answer-container-17588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17588-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where did you capture? At the client? On the client? On the DNS server? Sounds like you were capturing at a spot where you only see the DNS communication, so maybe your capture setup wasn't good enough. Or maybe you had a capture filter set on your network card.</p><p>If you need to decode SSL you need the private key of the application server (or the session key). The DNS server has nothing to do with the SSL session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '13, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17588" class="comments-container"></div><div id="comment-tools-17588" class="comment-tools"></div><div class="clear"></div><div id="comment-17588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

