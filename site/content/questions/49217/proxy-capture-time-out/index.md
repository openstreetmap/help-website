+++
type = "question"
title = "proxy capture time out"
description = '''we are seeing smtp connection time outs. the connection hits first the device that will proxy the connection to the mail srv. the proxy server opens a secondary connection to the configured mail relay when itself receives a new connection. After the initial connection it mirrors all the SMTP command...'''
date = "2016-01-14T06:37:00Z"
lastmod = "2016-01-14T08:01:00Z"
weight = 49217
keywords = [ "proxy" ]
aliases = [ "/questions/49217" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [proxy capture time out](/questions/49217/proxy-capture-time-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49217-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we are seeing smtp connection time outs. the connection hits first the device that will proxy the connection to the mail srv. the proxy server opens a secondary connection to the configured mail relay when itself receives a new connection. After the initial connection it mirrors all the SMTP commands from the primary connection to the secondary connection to the mail relay. It then receives the mail, processes it and forwards it via the secondary connection. we see errors on the proxy that would indicate that the processing can take more than the connection timeout of the mail relay on the secondary connection. i would have to prove that.</p><p>where to capture ?</p><p>thx</p></div><div id="question-tags" class="tags-container tags">proxy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '16, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/58a3131e1e35c49df01ec1a70c442d9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="proxyguy&#39;s gravatar image" /><p>proxyguy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="proxyguy has no accepted answers">0%</span></p></div></div><div id="comments-container-49217" class="comments-container"></div><div id="comment-tools-49217" class="comment-tools"></div><div class="clear"></div><div id="comment-49217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49219"></span>

<div id="answer-container-49219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49219-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to capture both connections, the one between client and proxy, and the other one between proxy and server. If the proxy has only one interface, capture that link. If it has two or more, capture all of them at the same time if the connections use them.</p><p>You basically need to compare what the two connections are doing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '16, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-49219" class="comments-container"><span id="49249"></span><div id="comment-49249" class="comment"><div id="post-49249-score" class="comment-score"></div><div class="comment-text"><p>how would I be able to match the packets arriving at the proxy to the packets leaving it towards our mail server?</p><p>there's a NAT in front of the proxy so all packets that arrive at the proxy will always have the same src address.</p><p>thx</p></div><div id="comment-49249-info" class="comment-info"><span class="comment-age">(15 Jan '16, 03:39)</span> proxyguy</div></div><span id="49250"></span><div id="comment-49250" class="comment"><div id="post-49250-score" class="comment-score">1</div><div class="comment-text"><p>you can try matching by TCP payloads of the packets - it's time consuming, but it might be the only option.</p></div><div id="comment-49250-info" class="comment-info"><span class="comment-age">(15 Jan '16, 03:42)</span> Jasper ♦♦</div></div></div><div id="comment-tools-49219" class="comment-tools"></div><div class="clear"></div><div id="comment-49219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

