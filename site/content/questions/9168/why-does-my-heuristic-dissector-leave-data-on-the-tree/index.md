+++
type = "question"
title = "Why does my heuristic dissector leave &quot;Data&quot; on the tree?"
description = '''I have a heuristic dissector which works perfectly, but the tree still contains a &quot;data&quot; field which contains the same number of bytes as the dissector decoded. The tree appears as:  IP TCP &amp;lt;my protocol&amp;gt; Data &amp;lt;x bytes&amp;gt;  Is there a way to remove or block that Data leaf from binding to the...'''
date = "2012-02-21T11:56:00Z"
lastmod = "2012-02-21T12:20:00Z"
weight = 9168
keywords = [ "development", "heuristic", "dissector", "data", "tree" ]
aliases = [ "/questions/9168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why does my heuristic dissector leave "Data" on the tree?](/questions/9168/why-does-my-heuristic-dissector-leave-data-on-the-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a heuristic dissector which works perfectly, but the tree still contains a "data" field which contains the same number of bytes as the dissector decoded. The tree appears as:<br />
</p><p>IP<br />
TCP<br />
&lt;my protocol&gt;<br />
Data &lt;x bytes&gt;<br />
</p><p>Is there a way to remove or block that Data leaf from binding to the tree?</p></div><div id="question-tags" class="tags-container tags">development heuristic dissector data tree</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '12, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/492460a2d6b7a5cfbe814f16f86686e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clifford%20Haas&#39;s gravatar image" /><p>Clifford Haas<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clifford Haas has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '12, 14:10</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></br></p></div></div><div id="comments-container-9168" class="comments-container"></div><div id="comment-tools-9168" class="comment-tools"></div><div class="clear"></div><div id="comment-9168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9169"></span>

<div id="answer-container-9169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9169-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Make sure to return TRUE from your heuristic dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '12, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-9169" class="comments-container"><span id="9190"></span><div id="comment-9190" class="comment"><div id="post-9190-score" class="comment-score"></div><div class="comment-text"><p>I have verified that the dissector does return TRUE. I even placed a "return (TRUE)" near the top of the dissector, right after I change the column info. This still left DATA on the tree. 8-(</p></div><div id="comment-9190-info" class="comment-info"><span class="comment-age">(24 Feb '12, 06:34)</span> Clifford Haas</div></div><span id="9193"></span><div id="comment-9193" class="comment"><div id="post-9193-score" class="comment-score"></div><div class="comment-text"><p>Is it possible that using tcp_dissect_pdus to reassemble is conflicting with pure TCP heuristic?</p></div><div id="comment-9193-info" class="comment-info"><span class="comment-age">(24 Feb '12, 07:08)</span> Clifford Haas</div></div></div><div id="comment-tools-9169" class="comment-tools"></div><div class="clear"></div><div id="comment-9169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

