+++
type = "question"
title = "dissector onDoubleClick"
description = '''Hi,  is it possible to know about, why the dissector was called ?  Here is the description of my problem :   - The complete decoding of the packet takes to long while capturing so i wish do decode the tcp packet only if the details window will open ( double click on the packet).'''
date = "2012-08-30T13:15:00Z"
lastmod = "2012-08-30T15:33:00Z"
weight = 13966
keywords = [ "development", "dissector" ]
aliases = [ "/questions/13966" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissector onDoubleClick](/questions/13966/dissector-ondoubleclick)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13966-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, is it possible to know about, why the dissector was called ? Here is the description of my problem : - The complete decoding of the packet takes to long while capturing so i wish do decode the tcp packet only if the details window will open ( double click on the packet).</p></div><div id="question-tags" class="tags-container tags">development dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '12, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/4c757ab26b58a1fb7b157a8bcd721a0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="derinicehand&#39;s gravatar image" /><p>derinicehand<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="derinicehand has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '12, 13:23</p></div></div><div id="comments-container-13966" class="comments-container"></div><div id="comment-tools-13966" class="comment-tools"></div><div class="clear"></div><div id="comment-13966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13968"></span>

<div id="answer-container-13968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13968-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ehm, no you cannot. The only thing you can do is look at the tree you get. If it's NULL you can forgo the creation of the proto items, BUT NOT THE REST. You must do column fills, reassembly, call subdissectors, etc.</p><p>Have you played with the Display options in the capture dialog? Does unchecking 'Update packet list in real time' help?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '12, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13968" class="comments-container"></div><div id="comment-tools-13968" class="comment-tools"></div><div class="clear"></div><div id="comment-13968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

