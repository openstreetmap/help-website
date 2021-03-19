+++
type = "question"
title = "How to use whole wireshark dissection code as library plugin ?"
description = '''Hi, I am using one accounting software which captures network data from libpcap. I want to dissect all protocols available in wireshark dissection code. Also, I want to use wireshark services like Statistics. Is there any way to use whole wireshark as a library (.so) and plug it into my software whi...'''
date = "2016-06-26T22:51:00Z"
lastmod = "2016-06-27T02:23:00Z"
weight = 53663
keywords = [ "libwireshark" ]
aliases = [ "/questions/53663" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use whole wireshark dissection code as library plugin ?](/questions/53663/how-to-use-whole-wireshark-dissection-code-as-library-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using one accounting software which captures network data from libpcap.</p><p>I want to dissect all protocols available in wireshark dissection code. Also, I want to use wireshark services like Statistics.</p><p>Is there any way to use whole wireshark as a library (.so) and plug it into my software which is written in C ?</p><p>e.g. My software captures data from libpcap. I am using wireshark APIs to classify protocol stream and building statistics accordingly.</p><p>I am working on Ubuntu machine.</p></div><div id="question-tags" class="tags-container tags">libwireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '16, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p>Mehul28<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '16, 22:52</p></div></div><div id="comments-container-53663" class="comments-container"></div><div id="comment-tools-53663" class="comment-tools"></div><div class="clear"></div><div id="comment-53663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53665"></span>

<div id="answer-container-53665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53665-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is libwireshark which contains the dissection functions. The statistics related to the UI, the CLI interface has text output, while the Qt interface has nice graphics.</p><p>In all fairness, all these are considered internal interfaces within Wireshark / Tshark, and not really documented / supported for external program development.</p><p>The use of these functions this way will make GPL applicable to your application, having implications on the conditions for distribution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '16, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53665" class="comments-container"></div><div id="comment-tools-53665" class="comment-tools"></div><div class="clear"></div><div id="comment-53665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

