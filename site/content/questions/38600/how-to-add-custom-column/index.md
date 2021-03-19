+++
type = "question"
title = "How to add custom Column?"
description = '''Hi, In Wireshark, can I add a column which indicates diff between two other columns of same/diff packet? For ex: In a packet I see two fields: Timestamp-1 &amp;amp; Timestamp-2. Now I can add them as two columns. And I want third column = Timestamp-2 - Timestamp-1. Please let me know if it&#x27;s possible? R...'''
date = "2014-12-16T09:12:00Z"
lastmod = "2014-12-19T11:26:00Z"
weight = 38600
keywords = [ "columns", "wireshark" ]
aliases = [ "/questions/38600" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to add custom Column?](/questions/38600/how-to-add-custom-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38600-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In Wireshark, can I add a column which indicates diff between two other columns of same/diff packet?</p><p>For ex:</p><p>In a packet I see two fields: Timestamp-1 &amp; Timestamp-2. Now I can add them as two columns. And I want third column = Timestamp-2 - Timestamp-1. Please let me know if it's possible?</p><p>Regards, Ramprasad</p></div><div id="question-tags" class="tags-container tags">columns wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '14, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p>Ramprasad<br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-38600" class="comments-container"></div><div id="comment-tools-38600" class="comment-tools"></div><div class="clear"></div><div id="comment-38600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38601"></span>

<div id="answer-container-38601" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38601-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't add custom columns that do calculations on frame contents, you can only display values that are already available in the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '14, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38601" class="comments-container"></div><div id="comment-tools-38601" class="comment-tools"></div><div class="clear"></div><div id="comment-38601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38639"></span>

<div id="answer-container-38639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had to do something similar, had to export the captures to CSV for analysis in excel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '14, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/700c3d847f93cb9934f2d4f92a3073b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziggy&#39;s gravatar image" /><p>Ziggy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziggy has no accepted answers">0%</span></p></div></div><div id="comments-container-38639" class="comments-container"></div><div id="comment-tools-38639" class="comment-tools"></div><div class="clear"></div><div id="comment-38639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

