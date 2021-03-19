+++
type = "question"
title = "unknown codec within GSM I/F BSSMAP &quot;Assignment Complete&quot; message"
description = '''In some cases I see the following field description within a GSM I/F BSSMAP &quot;Assignment Complete&quot; message: &quot;Unknown codec - the rest of the dissection my be suspect&quot;. I think that this is a wireshark application terminology (and not GSM...). Under what conditions we are to get this field description...'''
date = "2012-10-21T15:47:00Z"
lastmod = "2012-10-22T06:28:00Z"
weight = 15137
keywords = [ "bssmap", "codec", "type" ]
aliases = [ "/questions/15137" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [unknown codec within GSM I/F BSSMAP "Assignment Complete" message](/questions/15137/unknown-codec-within-gsm-if-bssmap-assignment-complete-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In some cases I see the following field description within a GSM I/F BSSMAP "Assignment Complete" message: "Unknown codec - the rest of the dissection my be suspect". I think that this is a wireshark application terminology (and not GSM...).</p><p>Under what conditions we are to get this field description?Is this a bug?</p></div><div id="question-tags" class="tags-container tags">bssmap codec type</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '12, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/59f06448a9e796a07d480e45686f2cee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HRHR&#39;s gravatar image" /><p>HRHR<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HRHR has no accepted answers">0%</span></p></div></div><div id="comments-container-15137" class="comments-container"></div><div id="comment-tools-15137" class="comment-tools"></div><div class="clear"></div><div id="comment-15137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15156"></span>

<div id="answer-container-15156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15156-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It may be a Wireshark bug, whar version are you using? as Wireshark fails to dissect a mandatory elemet it may be off on the byte count and the rest of the dissection may be incorrect. If you get thet result on 1.8.3 yo should open a bug attaching a sample trace with the message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '12, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-15156" class="comments-container"><span id="15168"></span><div id="comment-15168" class="comment"><div id="post-15168-score" class="comment-score"></div><div class="comment-text"><p>Correct. I had an older version. In 1.8.3 looks OK. Thank you.</p></div><div id="comment-15168-info" class="comment-info"><span class="comment-age">(22 Oct '12, 08:46)</span> HRHR</div></div></div><div id="comment-tools-15156" class="comment-tools"></div><div class="clear"></div><div id="comment-15156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

