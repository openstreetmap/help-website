+++
type = "question"
title = "K12 file format timestamp"
description = '''When exporting to a K12 file, how does one decode the timestamp?  14:42:37,686,606 ETHER The file was generated at 9AM which I prove when I dump the file using tshark. Don&#x27;t know how the above timestamp translates to 9AM. What are the comma separated values that follow? Thanks'''
date = "2015-01-29T17:18:00Z"
lastmod = "2015-01-29T17:24:00Z"
weight = 39493
keywords = [ "k12" ]
aliases = [ "/questions/39493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [K12 file format timestamp](/questions/39493/k12-file-format-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When exporting to a K12 file, how does one decode the timestamp?<br />
</p><p>14:42:37,686,606 ETHER</p><p>The file was generated at 9AM which I prove when I dump the file using tshark. Don't know how the above timestamp translates to 9AM. What are the comma separated values that follow?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">k12</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/92c8b7be28bbaf0a3c5031327e786cc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DrDRM&#39;s gravatar image" /><p>DrDRM<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DrDRM has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39493" class="comments-container"></div><div id="comment-tools-39493" class="comment-tools"></div><div class="clear"></div><div id="comment-39493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39494"></span>

<div id="answer-container-39494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39494-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Timestamps in capture files are usually stored as UTC values, so if your PC is not on UTC tshark will "translate" the file timestamp to your local time based on your timezone settings.</p><p>The values behind the 37 seconds are probably milli- and microseconds. 686 milliseconds, 606 microseconds, or 6866060 microseconds in total.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '15, 17:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '15, 17:24</p></div></div><div id="comments-container-39494" class="comments-container"></div><div id="comment-tools-39494" class="comment-tools"></div><div class="clear"></div><div id="comment-39494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

