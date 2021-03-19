+++
type = "question"
title = "what is difference between wireshark and wireshark legacy?"
description = '''what is difference between wireshark and wireshark legacy?'''
date = "2016-11-13T06:23:00Z"
lastmod = "2016-11-13T06:30:00Z"
weight = 57358
keywords = [ "legacy" ]
aliases = [ "/questions/57358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is difference between wireshark and wireshark legacy?](/questions/57358/what-is-difference-between-wireshark-and-wireshark-legacy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57358-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what is difference between wireshark and wireshark legacy?</p></div><div id="question-tags" class="tags-container tags">legacy</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '16, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/c5570bae1027298957ad1a42272e0fa0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnabhunia&#39;s gravatar image" /><p>krishnabhunia<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnabhunia has no accepted answers">0%</span></p></div></div><div id="comments-container-57358" class="comments-container"></div><div id="comment-tools-57358" class="comment-tools"></div><div class="clear"></div><div id="comment-57358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57359"></span>

<div id="answer-container-57359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57359-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Wireshark" uses the new QT based GUI, while "Wireshark Legacy" uses the old GTK based GUI. So the GUIs are the difference, and the new GUI may provide new/different features than the old. The internals should still be the same, meaning protocol dissectors and analysis results should be identical (but some core developers may correct me on this)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-57359" class="comments-container"><span id="57360"></span><div id="comment-57360" class="comment"><div id="post-57360-score" class="comment-score"></div><div class="comment-text"><p>...and, due to differences between the two toolkits and the fact that they provide Wireshark with the <strong>u</strong>ser <strong>i</strong>nteface in general, not just the <strong>g</strong>raphical part of it, some functions which depend on more sophisticated features like drawing graphics and playing audio behave different in the two versions. For example, the telephony flow graph in the Qt version (Wireshark) does not draw fat lines for RTP and narrow ones for signalling (which the GTK version/Wireshark legacy did), the RTP player in the Qt version struggles on some soundcards...</p></div><div id="comment-57360-info" class="comment-info"><span class="comment-age">(13 Nov '16, 06:43)</span> sindy</div></div><span id="57366"></span><div id="comment-57366" class="comment"><div id="post-57366-score" class="comment-score"></div><div class="comment-text"><p>@sindy, are there bugs filed for the issues you mentioned (and any other issues you've found)?</p></div><div id="comment-57366-info" class="comment-info"><span class="comment-age">(13 Nov '16, 12:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-57359" class="comment-tools"></div><div class="clear"></div><div id="comment-57359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

