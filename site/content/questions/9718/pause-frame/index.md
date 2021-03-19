+++
type = "question"
title = "pause frame"
description = '''To filter pause frame in captured pcap file, How do I type filter expression ?'''
date = "2012-03-23T05:17:00Z"
lastmod = "2012-03-23T06:04:00Z"
weight = 9718
keywords = [ "mac-pause" ]
aliases = [ "/questions/9718" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pause frame](/questions/9718/pause-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9718-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To filter pause frame in captured pcap file, How do I type filter expression ?</p></div><div id="question-tags" class="tags-container tags">mac-pause</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '12, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/e953f5875bd7a076ca9969a3c867ea5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mom&#39;s gravatar image" /><p>mom<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mom has no accepted answers">0%</span></p></div></div><div id="comments-container-9718" class="comments-container"></div><div id="comment-tools-9718" class="comment-tools"></div><div class="clear"></div><div id="comment-9718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9719"></span>

<div id="answer-container-9719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display Filters:</p><p><code>macc</code> will filter for all the mac-control frames</p><p><code>macc.opcode == pause</code> will filter for all the mac-control pause frames</p><p>Note: Selecting <code>Expression ! macc</code> in the Wireshark filter bar will show all the possible mac-control filters....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '12, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-9719" class="comments-container"></div><div id="comment-tools-9719" class="comment-tools"></div><div class="clear"></div><div id="comment-9719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

