+++
type = "question"
title = "Websocket deflate decode"
description = '''How could I see the websocket payload when deflate extension is enabled and data is compressed. Is there any plugin for that? Thanks'''
date = "2016-05-30T19:13:00Z"
lastmod = "2016-05-31T01:06:00Z"
weight = 53058
keywords = [ "websocket", "deflate" ]
aliases = [ "/questions/53058" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Websocket deflate decode](/questions/53058/websocket-deflate-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53058-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How could I see the websocket payload when deflate extension is enabled and data is compressed. Is there any plugin for that?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">websocket deflate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '16, 19:13</strong></p><img src="https://secure.gravatar.com/avatar/52cd9641471001e7cea6e70303b14282?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emonsef&#39;s gravatar image" /><p>emonsef<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emonsef has no accepted answers">0%</span></p></div></div><div id="comments-container-53058" class="comments-container"></div><div id="comment-tools-53058" class="comment-tools"></div><div class="clear"></div><div id="comment-53058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53061"></span>

<div id="answer-container-53061" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53061-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A quick look at the dissector code (for both HTTP and WebSocket) shows no sign of deflate support. Also, reading from <a href="http://www.lenholgate.com/blog/2011/07/websockets---the-deflate-stream-extension-is-broken-and-badly-designed.html">this</a>, it might prove tricky to implement, since it changes the wire format of WebSocket.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '16, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53061" class="comments-container"></div><div id="comment-tools-53061" class="comment-tools"></div><div class="clear"></div><div id="comment-53061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

