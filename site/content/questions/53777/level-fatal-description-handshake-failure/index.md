+++
type = "question"
title = "Level: Fatal Description Handshake Failure"
description = '''hi all, Question. An application is connecting via a proxy to the application server that is handling clients requests. The server got updated, now when client connects to server (still via proxy) we get &quot;connection to server failed&quot;. If you disable on client to go via the proxy it works. We can see...'''
date = "2016-07-01T13:36:00Z"
lastmod = "2016-07-02T02:17:00Z"
weight = 53777
keywords = [ "tls", "ssl", "failure" ]
aliases = [ "/questions/53777" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Level: Fatal Description Handshake Failure](/questions/53777/level-fatal-description-handshake-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53777-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>Question. An application is connecting via a proxy to the application server that is handling clients requests. The server got updated, now when client connects to server (still via proxy) we get "connection to server failed". If you disable on client to go via the proxy it works. We can see in the trace file from proxy appliance that 3 way handshake is successful, the client sends it's CLIENT HELLO but the response is <img src="https://osqa-ask.wireshark.org/upfiles/snip.JPG" alt="alt text" /></p><p>Would it be better to capture on the proxy and server at same time ? Does the client negotiate the SSL/TLS session with the server directly or client --&gt; proxy and proxy --&gt; server ?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">tls ssl failure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '16, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53777" class="comments-container"></div><div id="comment-tools-53777" class="comment-tools"></div><div class="clear"></div><div id="comment-53777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53783"></span>

<div id="answer-container-53783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53783-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're asking al the right questions yourself already. Have a look at the proxy -&gt; server connection setup, which seems to fail.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '16, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53783" class="comments-container"></div><div id="comment-tools-53783" class="comment-tools"></div><div class="clear"></div><div id="comment-53783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

