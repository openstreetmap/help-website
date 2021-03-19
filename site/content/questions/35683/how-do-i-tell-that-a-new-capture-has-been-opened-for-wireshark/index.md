+++
type = "question"
title = "How do I tell that a new capture has been opened for Wireshark?"
description = '''I am building a plugin for Wireshark, and I have several global variables that record and keep track of data from different packets. When a new capture is opened, I want to be able to clear these variables so the previous data isn&#x27;t mixed up with the new data. Is there a function or property in Wire...'''
date = "2014-08-22T18:22:00Z"
lastmod = "2014-08-23T03:32:00Z"
weight = 35683
keywords = [ "plugin", "plugins", "wireshark" ]
aliases = [ "/questions/35683" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I tell that a new capture has been opened for Wireshark?](/questions/35683/how-do-i-tell-that-a-new-capture-has-been-opened-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35683-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am building a plugin for Wireshark, and I have several global variables that record and keep track of data from different packets. When a new capture is opened, I want to be able to clear these variables so the previous data isn't mixed up with the new data.</p><p>Is there a function or property in Wireshark that can alert me that a new capture file has been opened?</p></div><div id="question-tags" class="tags-container tags">plugin plugins wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '14, 18:22</strong></p><img src="https://secure.gravatar.com/avatar/8e15a601ac7f7d65a3c7926934962bd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frankie&#39;s gravatar image" /><p>Frankie<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frankie has no accepted answers">0%</span></p></div></div><div id="comments-container-35683" class="comments-container"></div><div id="comment-tools-35683" class="comment-tools"></div><div class="clear"></div><div id="comment-35683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35684"></span>

<div id="answer-container-35684" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35684-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can register a callback function thanks to the register_init_routine() function that will be called when opening a new capture (or applying a display filter). In your function, clear your data. You can see an example in packet-tcp.c.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '14, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35684" class="comments-container"><span id="35733"></span><div id="comment-35733" class="comment"><div id="post-35733-score" class="comment-score"></div><div class="comment-text"><p>Worked perfectly, thanks!</p></div><div id="comment-35733-info" class="comment-info"><span class="comment-age">(25 Aug '14, 16:04)</span> Frankie</div></div></div><div id="comment-tools-35684" class="comment-tools"></div><div class="clear"></div><div id="comment-35684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

