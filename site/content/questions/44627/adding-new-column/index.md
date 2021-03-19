+++
type = "question"
title = "Adding new column"
description = '''Can I add a new column with the difference (or another arithmetic operation) of values from two other columns? Or maybe with the help of tshark it could be done?'''
date = "2015-07-30T05:20:00Z"
lastmod = "2015-08-01T10:03:00Z"
weight = 44627
keywords = [ "difference", "values", "custom_column" ]
aliases = [ "/questions/44627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding new column](/questions/44627/adding-new-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I add a new column with the difference (or another arithmetic operation) of values from two other columns?</p><p>Or maybe with the help of tshark it could be done?</p></div><div id="question-tags" class="tags-container tags">difference values custom_column</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/85baeeab4c9c9daa8290a8d7304dec88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abatian&#39;s gravatar image" /><p>abatian<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abatian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jul '15, 05:27</p></div></div><div id="comments-container-44627" class="comments-container"></div><div id="comment-tools-44627" class="comment-tools"></div><div class="clear"></div><div id="comment-44627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44724"></span>

<div id="answer-container-44724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44724-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark always displays values taking from one frame, and one frame only. So if the dissectors do not provide such a calculated value (e.g. "TCP Next expected Sequence number") you cannot filter on it neither build a column based on that filter.</p><p>Most of us use the export function "Export Packet Dissections" -&gt; "as CSV" -&gt; "Packet summary line only" to export the packet list to CSV, and then run Excel (or any other spreadsheet software) to do the calculations for us.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '15, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44724" class="comments-container"></div><div id="comment-tools-44724" class="comment-tools"></div><div class="clear"></div><div id="comment-44724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

