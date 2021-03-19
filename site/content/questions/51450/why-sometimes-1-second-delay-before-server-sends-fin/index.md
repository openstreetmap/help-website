+++
type = "question"
title = "Why sometimes 1 second delay before server sends fin?"
description = '''Hi, Does anyone have an idea what could cause the delay of one second in the below screenshot? It doesn&#x27;t happen for all requests to the server, but it does so frequently enough. The client uses HTTP 1.0 &amp;amp; doesn&#x27;t send a keep-alive header, so it is correct the server initiates the closing of the...'''
date = "2016-04-07T01:01:00Z"
lastmod = "2016-04-19T13:58:00Z"
weight = 51450
keywords = [ "delay", "fin", "server" ]
aliases = [ "/questions/51450" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why sometimes 1 second delay before server sends fin?](/questions/51450/why-sometimes-1-second-delay-before-server-sends-fin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51450-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Does anyone have an idea what could cause the delay of one second in the below screenshot? It doesn't happen for all requests to the server, but it does so frequently enough. The client uses HTTP 1.0 &amp; doesn't send a keep-alive header, so it is correct the server initiates the closing of the connection. But why does it wait for 1 second before doing that? The server is an IBM HTTP server. Since it isn't 100% doing that, I doubt it's a setting, but I was wondering if there's a way to avoid it or at least understand why it's happening.</p><p>Thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/delayedFIN.png" alt="1 second delay fin" /></p></div><div id="question-tags" class="tags-container tags">delay fin server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/36cefd7fb81fafd121456564a2efbe59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sebbe&#39;s gravatar image" /><p>Sebbe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sebbe has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51450" class="comments-container"></div><div id="comment-tools-51450" class="comment-tools"></div><div class="clear"></div><div id="comment-51450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51804"></span>

<div id="answer-container-51804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51804-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but I was wondering if there's a way to avoid it or <strong>at least understand why it's happening</strong>.</p></blockquote><p>Well, the capture file won't tell you. So, one option would be to enable debug logging on the server to figure out whats going on. My best guess would be: It's busy for whatever reason and thus it does not send the FIN earlier.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-51804" class="comments-container"></div><div id="comment-tools-51804" class="comment-tools"></div><div class="clear"></div><div id="comment-51804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

