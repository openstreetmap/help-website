+++
type = "question"
title = "Can I see where traffic is coming from"
description = '''I&#x27;m troubleshooting a network where there&#x27;s about 50 users. Some wired some wireless. They are having an issue where not all users can get on the wireless network at once. The switch shows that there is a lot of network traffic. How can I find out where the traffic is coming from using Wireshark?'''
date = "2011-07-26T11:17:00Z"
lastmod = "2011-07-27T01:54:00Z"
weight = 5270
keywords = [ "wireless", "traffic", "network" ]
aliases = [ "/questions/5270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I see where traffic is coming from](/questions/5270/can-i-see-where-traffic-is-coming-from)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm troubleshooting a network where there's about 50 users. Some wired some wireless. They are having an issue where not all users can get on the wireless network at once. The switch shows that there is a lot of network traffic. How can I find out where the traffic is coming from using Wireshark?</p></div><div id="question-tags" class="tags-container tags">wireless traffic network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/bcc6042a0b3b1a599a6cf744f0daa185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ufocomputerservices&#39;s gravatar image" /><p>ufocomputers...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ufocomputerservices has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '11, 11:17</p></div></div><div id="comments-container-5270" class="comments-container"></div><div id="comment-tools-5270" class="comment-tools"></div><div class="clear"></div><div id="comment-5270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5299"></span>

<div id="answer-container-5299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5299-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can show you the frame details of the frames present on the capture interface, sans the filtered frames. So first thing to do is find one or more <a href="http://wiki.wireshark.org/CaptureSetup">relevant capture interfaces</a> to tap the network traffic which provide you insights in what communications are happening. From there on it's based on your interpretation of this traffic to identify problem indications.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5299" class="comments-container"></div><div id="comment-tools-5299" class="comment-tools"></div><div class="clear"></div><div id="comment-5299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

