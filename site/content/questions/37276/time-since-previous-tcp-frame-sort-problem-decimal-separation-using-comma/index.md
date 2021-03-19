+++
type = "question"
title = "Time since previous TCP frame sort problem (decimal separation using comma)"
description = '''Hi. After adding a column for &quot;Time since previous frame in this TCP stream&quot; there is a problem to sort that column. This is because of the use of comma as the decimal separation sign (which many countries use in Europe). One solution, which I don&#x27;t want to do each time (or should have to do), is to...'''
date = "2014-10-22T05:31:00Z"
lastmod = "2014-10-22T06:47:00Z"
weight = 37276
keywords = [ "sort", "problem", "comma", "decimal" ]
aliases = [ "/questions/37276" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Time since previous TCP frame sort problem (decimal separation using comma)](/questions/37276/time-since-previous-tcp-frame-sort-problem-decimal-separation-using-comma)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37276-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>After adding a column for "Time since previous frame in this TCP stream" there is a problem to sort that column. This is because of the use of comma as the decimal separation sign (which many countries use in Europe).</p><p>One solution, which I don't want to do each time (or should have to do), is to go to Windows Regional Settings and Additional settings and change the Decimal symbol from , (comma) to . (point), then Wireshark sort the column correctly. Is there any way to set this in Wireshark? (because other stuff doesn't work as normal when I've changed the Regional settings)</p><p>Thanks,</p><p>Daniel, Sweden.</p></div><div id="question-tags" class="tags-container tags">sort problem comma decimal</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '14, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/09f8ad2f9562d6fb87e5d5c97f79c1ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hagel666&#39;s gravatar image" /><p>hagel666<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hagel666 has no accepted answers">0%</span></p></div></div><div id="comments-container-37276" class="comments-container"></div><div id="comment-tools-37276" class="comment-tools"></div><div class="clear"></div><div id="comment-37276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37278"></span>

<div id="answer-container-37278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37278-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>this is bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8964">8964</a> and we have no known workaround other than changing the Regional Settings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-37278" class="comments-container"><span id="37281"></span><div id="comment-37281" class="comment"><div id="post-37281-score" class="comment-score"></div><div class="comment-text"><p>Pascal, There are a lot of applications who can handle the regional differences (comma and point separator), why shouldn't it be possible to implement in Wireshark? What programming language is used for the failing part in the gui? C++?</p><p>prostetenic, Yes I know (and wrote about it in the second section in my first post).</p></div><div id="comment-37281-info" class="comment-info"><span class="comment-age">(22 Oct '14, 06:54)</span> hagel666</div></div></div><div id="comment-tools-37278" class="comment-tools"></div><div class="clear"></div><div id="comment-37278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37280"></span>

<div id="answer-container-37280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37280-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can reduce the overall damage by just swapping the Comma for a decimal in regional settings. works in German win 7 Enterprise anyway.</p><p>Still annoying, but better than suddenly having $ for currency..</p><p>Edit: As a side note, you might want to consider chnging the list seperator ; for a , as well if you intend to export any columns to CSV format.. Just a tip.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '14, 06:50</p></div></div><div id="comments-container-37280" class="comments-container"></div><div id="comment-tools-37280" class="comment-tools"></div><div class="clear"></div><div id="comment-37280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

