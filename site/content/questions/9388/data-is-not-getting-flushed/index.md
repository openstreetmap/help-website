+++
type = "question"
title = "Data is not getting flushed"
description = '''Hello  I have added a .CSV parser and a dissector. It is observed that if my .CSV file is opened as the first file in wireshark, then packet dump is proper as expected. But if an other file is opened first and then my .CSV file is opened then packet dump is of the previous data. This is not the beha...'''
date = "2012-03-06T01:11:00Z"
lastmod = "2012-03-11T22:28:00Z"
weight = 9388
keywords = [ "data", "flushing" ]
aliases = [ "/questions/9388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data is not getting flushed](/questions/9388/data-is-not-getting-flushed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have added a .CSV parser and a dissector. It is observed that if my .CSV file is opened as the first file in wireshark, then packet dump is proper as expected.</p><p>But if an other file is opened first and then my .CSV file is opened then packet dump is of the previous data. This is not the behaviour with other sample files.</p><p>I have verified that the frame buffer is getting filled with data properly from my XXX_read and XXX_seek functions.</p><p>It looks like some flag issue.</p><p>Can anyone help me to resolve my issue?</p><p>thanks in advance krithiga</p></div><div id="question-tags" class="tags-container tags">data flushing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/58a0b723193dca931ba99c422c8a0e74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krithiga&#39;s gravatar image" /><p>krithiga<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krithiga has no accepted answers">0%</span></p></div></div><div id="comments-container-9388" class="comments-container"></div><div id="comment-tools-9388" class="comment-tools"></div><div class="clear"></div><div id="comment-9388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9483"></span>

<div id="answer-container-9483" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9483-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>issue resolved by doing changes in XXX_seek() w.r.t to offset handling</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '12, 22:28</strong></p><img src="https://secure.gravatar.com/avatar/58a0b723193dca931ba99c422c8a0e74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krithiga&#39;s gravatar image" /><p>krithiga<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krithiga has no accepted answers">0%</span></p></div></div><div id="comments-container-9483" class="comments-container"></div><div id="comment-tools-9483" class="comment-tools"></div><div class="clear"></div><div id="comment-9483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

