+++
type = "question"
title = "Delaying Capture"
description = '''I would like to be able to have Wireshark do a capture at 0200 for approx 2 minutes to see where a 4MB stream is coming from. Is there a way to start and stop Wireshark at certain time of day?'''
date = "2010-12-07T09:53:00Z"
lastmod = "2010-12-07T10:36:00Z"
weight = 1273
keywords = [ "delay" ]
aliases = [ "/questions/1273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Delaying Capture](/questions/1273/delaying-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to be able to have Wireshark do a capture at 0200 for approx 2 minutes to see where a 4MB stream is coming from. Is there a way to start and stop Wireshark at certain time of day?</p></div><div id="question-tags" class="tags-container tags">delay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '10, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/4907231fc424e520b785cadeffb34130?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mach%20One&#39;s gravatar image" /><p>Mach One<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mach One has no accepted answers">0%</span></p></div></div><div id="comments-container-1273" class="comments-container"></div><div id="comment-tools-1273" class="comment-tools"></div><div class="clear"></div><div id="comment-1273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1274"></span>

<div id="answer-container-1274" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1274-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure: Schedule a 'dumpcap' job for 02:00 (method depending upon your OS: windows/at; linux/cron, etc).</p><p>(Dumpcap is the Wireshark component which actually does a capture).</p><p>See the dumpcap man pages for info on limiting the amount of data which is captured.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '10, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-1274" class="comments-container"></div><div id="comment-tools-1274" class="comment-tools"></div><div class="clear"></div><div id="comment-1274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

