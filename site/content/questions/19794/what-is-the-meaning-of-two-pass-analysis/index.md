+++
type = "question"
title = "What is the meaning of two-pass analysis?"
description = '''Hi, In Wireshark 1.8 and later version,Tshark added a option -2(perform a two-pass analysis). What is the meaning of two-pass analysis? Who can introduce it for me?'''
date = "2013-03-25T00:01:00Z"
lastmod = "2013-03-25T00:08:00Z"
weight = 19794
keywords = [ "two-pass", "tshark", "analysis" ]
aliases = [ "/questions/19794" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the meaning of two-pass analysis?](/questions/19794/what-is-the-meaning-of-two-pass-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19794-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, In Wireshark 1.8 and later version,Tshark added a option -2(perform a two-pass analysis). What is the meaning of two-pass analysis? Who can introduce it for me?</p></div><div id="question-tags" class="tags-container tags">two-pass tshark analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '13, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/b9365e4208e4c3183bbc3376ec9030ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qqgeet&#39;s gravatar image" /><p>qqgeet<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qqgeet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '13, 00:03</p></div></div><div id="comments-container-19794" class="comments-container"></div><div id="comment-tools-19794" class="comment-tools"></div><div class="clear"></div><div id="comment-19794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19797"></span>

<div id="answer-container-19797" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19797-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>In a single (linear) pass through a capture file you can only carry information forwards. That is enough in most cases, but for some higher level analysis this isn't enough. Think of things like request/response tracking. In a single pass you cannot annotate a request with the frame number of the corresponding response. With two-pass analysis you can, because you note the corresponding request and response frame numbers together, and with the second pass make the annotations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19797" class="comments-container"></div><div id="comment-tools-19797" class="comment-tools"></div><div class="clear"></div><div id="comment-19797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

