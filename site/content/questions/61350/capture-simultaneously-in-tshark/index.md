+++
type = "question"
title = "capture simultaneously in tshark"
description = '''is it possible to read 2 captured file in tshark simultaneously? or is it possible to capture simultaneously from multiple interfaces at once?'''
date = "2017-05-11T00:40:00Z"
lastmod = "2017-05-11T00:43:00Z"
weight = 61350
keywords = [ "capture", "simultaneously", "tshark" ]
aliases = [ "/questions/61350" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture simultaneously in tshark](/questions/61350/capture-simultaneously-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61350-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is it possible to read 2 captured file in tshark simultaneously? or is it possible to capture simultaneously from multiple interfaces at once?</p></div><div id="question-tags" class="tags-container tags">capture simultaneously tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '17, 00:40</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div></div><div id="comments-container-61350" class="comments-container"></div><div id="comment-tools-61350" class="comment-tools"></div><div class="clear"></div><div id="comment-61350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61351"></span>

<div id="answer-container-61351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61351-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>yes, with two tshark instances running at the same time. You cannot read 2 capture files into the same tshark instance unless you merge them first via mergecap.</li><li>yes, either capturing on two (or more) interfaces into a single pcap, or with multiple tshark instances capturing on single interfaces</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '17, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61351" class="comments-container"></div><div id="comment-tools-61351" class="comment-tools"></div><div class="clear"></div><div id="comment-61351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

