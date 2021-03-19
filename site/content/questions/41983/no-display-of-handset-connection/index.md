+++
type = "question"
title = "no display of handset connection"
description = '''got an USB dougle connected on the laptop, but the connection is not displayed in the window. in fact, i wanted to capture the packet from the handset. same thing happend on the other laptop. not sure if an USB loader or smilar thing is required? thanks for the help in advance'''
date = "2015-04-30T09:42:00Z"
lastmod = "2015-05-01T03:32:00Z"
weight = 41983
keywords = [ "handset" ]
aliases = [ "/questions/41983" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no display of handset connection](/questions/41983/no-display-of-handset-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>got an USB dougle connected on the laptop, but the connection is not displayed in the window. in fact, i wanted to capture the packet from the handset. same thing happend on the other laptop. not sure if an USB loader or smilar thing is required?</p><p>thanks for the help in advance</p></div><div id="question-tags" class="tags-container tags">handset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '15, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/876d82bb2028dffd8b968a5163e449fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sibo%20%20Lee&#39;s gravatar image" /><p>Sibo Lee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sibo  Lee has no accepted answers">0%</span></p></div></div><div id="comments-container-41983" class="comments-container"></div><div id="comment-tools-41983" class="comment-tools"></div><div class="clear"></div><div id="comment-41983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41995"></span>

<div id="answer-container-41995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If this is Windows, a better operating system is required. Those devices are PPP devices, and, currently, <a href="https://www.winpcap.org/misc/faq.htm#Q-5">those don't work with WinPcap with current versions of Windows</a>, and Wireshark requires WinPcap, on Windows, to capture traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41995" class="comments-container"></div><div id="comment-tools-41995" class="comment-tools"></div><div class="clear"></div><div id="comment-41995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41999"></span>

<div id="answer-container-41999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41999-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Instead of changing the OS, when it's simply a capture mechanism issue, you could try <a href="">Message Analyzer</a> from Microsoft. Not the easiest program to work with, but if you can get it to capture, then you may can export the capture to .cap format that Wireshark might then able to read.</p><p>Note the "if's" and "mights".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41999" class="comments-container"></div><div id="comment-tools-41999" class="comment-tools"></div><div class="clear"></div><div id="comment-41999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

