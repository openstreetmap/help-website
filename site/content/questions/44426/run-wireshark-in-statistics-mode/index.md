+++
type = "question"
title = "Run Wireshark in &quot;statistics mode&quot;"
description = '''Hi, is there any way to run Wireshark in &quot;statistics mode&quot;, I mean without actually capturing large files? I am only interested in statistics and conversations (who is talking with each other on the network) and I don&#x27;t want to capture all packets in large files. I plan to run Wireshark in &quot;statisti...'''
date = "2015-07-24T02:28:00Z"
lastmod = "2015-07-24T03:21:00Z"
weight = 44426
keywords = [ "conversations", "statistics", "mode" ]
aliases = [ "/questions/44426" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Run Wireshark in "statistics mode"](/questions/44426/run-wireshark-in-statistics-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44426-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is there any way to run Wireshark in "statistics mode", I mean without actually capturing large files? I am only interested in statistics and conversations (who is talking with each other on the network) and I don't want to capture all packets in large files.</p><p>I plan to run Wireshark in "statistic mode" for a day or even longer, so a dumpfile would become very large.</p><p>Best regards, Volker</p></div><div id="question-tags" class="tags-container tags">conversations statistics mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/bbd783f3d0484226c2d906224d95d53f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peteshark&#39;s gravatar image" /><p>peteshark<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peteshark has no accepted answers">0%</span></p></div></div><div id="comments-container-44426" class="comments-container"></div><div id="comment-tools-44426" class="comment-tools"></div><div class="clear"></div><div id="comment-44426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44427"></span>

<div id="answer-container-44427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44427-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark (actually, dumpcap) always writes packets to disk. If you need statistics you might want to look at <a href="https://en.wikipedia.org/wiki/NetFlow">NetFlow</a> collection, which seems to be more what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44427" class="comments-container"></div><div id="comment-tools-44427" class="comment-tools"></div><div class="clear"></div><div id="comment-44427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

