+++
type = "question"
title = "real time link utilization"
description = '''Hi, I&#x27;m still learning WireShark but have used Network General Sniffers years ago. They had a nice feature on the main screen that displayed real-time link utilization. Is there any way to get link utilization with WireShark? Thanks.'''
date = "2011-03-29T15:23:00Z"
lastmod = "2011-03-29T16:38:00Z"
weight = 3215
keywords = [ "utilization" ]
aliases = [ "/questions/3215" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [real time link utilization](/questions/3215/real-time-link-utilization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3215-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm still learning WireShark but have used Network General Sniffers years ago. They had a nice feature on the main screen that displayed real-time link utilization. Is there any way to get link utilization with WireShark?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">utilization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '11, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p>eelarry<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '11, 15:23</p></div></div><div id="comments-container-3215" class="comments-container"></div><div id="comment-tools-3215" class="comment-tools"></div><div class="clear"></div><div id="comment-3215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3217"></span>

<div id="answer-container-3217" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3217-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could start the I/O Graph from the statistics menu. It will paint a utilization graph while the capture is running, but keep in mind that it might have an impact on capture performance. You'll probably want to set the Unit to "Bits/Tick" and the Tick to whatever resolution you like. Sometimes the graph doesn't show anything at first, until you play around with the Axis controls.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '11, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3217" class="comments-container"><span id="3238"></span><div id="comment-3238" class="comment"><div id="post-3238-score" class="comment-score"></div><div class="comment-text"><p>Thanks much. I didn't know about that.</p><p>I just downloaded the Pilot demo and it has a lot of nice features but is very expensive.</p></div><div id="comment-3238-info" class="comment-info"><span class="comment-age">(30 Mar '11, 18:42)</span> eelarry</div></div></div><div id="comment-tools-3217" class="comment-tools"></div><div class="clear"></div><div id="comment-3217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

