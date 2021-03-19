+++
type = "question"
title = "Cannot capture packet transfer between other PCs"
description = '''HI I have installed wireshark in a PC (lets say PC-A). PC-A, PC-B and PC-C are all connected through an ethernet switch. When i run wireshark, it shows capture of packets from/to PC-A only. it does not capture interactions between PC-B and PC-C. Is there any way i can capture this by wireshark? Plea...'''
date = "2011-10-30T19:05:00Z"
lastmod = "2011-10-30T23:32:00Z"
weight = 7165
keywords = [ "capture", "other", "interactions", "pc" ]
aliases = [ "/questions/7165" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture packet transfer between other PCs](/questions/7165/cannot-capture-packet-transfer-between-other-pcs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI I have installed wireshark in a PC (lets say PC-A). PC-A, PC-B and PC-C are all connected through an ethernet switch. When i run wireshark, it shows capture of packets from/to PC-A only. it does not capture interactions between PC-B and PC-C. Is there any way i can capture this by wireshark? Please do help.</p><p>Bijoy</p></div><div id="question-tags" class="tags-container tags">capture other interactions pc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '11, 19:05</strong></p><img src="https://secure.gravatar.com/avatar/7facc0c0384cfe002cfca8db766eadbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bijoy&#39;s gravatar image" /><p>bijoy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bijoy has no accepted answers">0%</span></p></div></div><div id="comments-container-7165" class="comments-container"></div><div id="comment-tools-7165" class="comment-tools"></div><div class="clear"></div><div id="comment-7165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7167"></span>

<div id="answer-container-7167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7167-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have to look into your <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">capture setup</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7167" class="comments-container"></div><div id="comment-tools-7167" class="comment-tools"></div><div class="clear"></div><div id="comment-7167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7168"></span>

<div id="answer-container-7168" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7168-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, Due to the switch A will not "see" packets between B and C. See http://wiki.wireshark.org/CaptureSetup/Ethernet</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7168" class="comments-container"></div><div id="comment-tools-7168" class="comment-tools"></div><div class="clear"></div><div id="comment-7168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

