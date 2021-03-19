+++
type = "question"
title = "Determine Physical Port on a Switch"
description = '''Is there any way to use Wireshark to identify which physical port on a switch or, even better, the jack that the computer is plugged into?&#x27;'''
date = "2015-01-30T15:59:00Z"
lastmod = "2015-01-30T16:05:00Z"
weight = 39515
keywords = [ "router", "switch" ]
aliases = [ "/questions/39515" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Determine Physical Port on a Switch](/questions/39515/determine-physical-port-on-a-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to use Wireshark to identify which physical port on a switch or, even better, the jack that the computer is plugged into?'</p></div><div id="question-tags" class="tags-container tags">router switch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/ffaff08b74286144557e74c0e83dbf02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SecurityPlus&#39;s gravatar image" /><p>SecurityPlus<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SecurityPlus has no accepted answers">0%</span></p></div></div><div id="comments-container-39515" class="comments-container"></div><div id="comment-tools-39515" class="comment-tools"></div><div class="clear"></div><div id="comment-39515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39516"></span>

<div id="answer-container-39516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39516-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the port on the switch is running CDP or LLDP, those protocols advertize the physical interface details on the wire which Wireshark can then decode.</p><p>As for the actual wire jack, basically there would need to be some information about it conveyed on the wire in order for it to show up in Wireshark so I would say not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '15, 16:07</p></div></div><div id="comments-container-39516" class="comments-container"></div><div id="comment-tools-39516" class="comment-tools"></div><div class="clear"></div><div id="comment-39516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

