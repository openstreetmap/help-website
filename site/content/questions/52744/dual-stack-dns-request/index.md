+++
type = "question"
title = "Dual stack DNS request"
description = '''Let&#x27;s assume the DNS resolver and the target server both support dual stack configuration. The resolver will then send DNS queries for A and AAAA RRs. As the server supports both, it will replies with the A RR and the AA RR. So which IP adressing will be used for the connection ? The first one that ...'''
date = "2016-05-18T11:53:00Z"
lastmod = "2016-05-18T14:52:00Z"
weight = 52744
keywords = [ "dns", "stack", "dual" ]
aliases = [ "/questions/52744" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dual stack DNS request](/questions/52744/dual-stack-dns-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52744-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let's assume the DNS resolver and the target server both support dual stack configuration. The resolver will then send DNS queries for A and AAAA RRs. As the server supports both, it will replies with the A RR and the AA RR.</p><p>So which IP adressing will be used for the connection ? The first one that responses ? Can it be defined/configured ?</p></div><div id="question-tags" class="tags-container tags">dns stack dual</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></div></div><div id="comments-container-52744" class="comments-container"></div><div id="comment-tools-52744" class="comment-tools"></div><div class="clear"></div><div id="comment-52744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52746"></span>

<div id="answer-container-52746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52746-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Depends on the stack and the application. Usually IPv6 has preference, which means the AAAA record is used (if an answer record is returned), otherwise it'll use IPv4 (again, if the answer record is returned). There are applications like web browsers who support "Happy Eyeballs" (<a href="https://tools.ietf.org/html/rfc6555">RFC 6555</a>), which then tries to use the faster connection by trying to send a SYN to both IPv4 and IPv6.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52746" class="comments-container"></div><div id="comment-tools-52746" class="comment-tools"></div><div class="clear"></div><div id="comment-52746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

