+++
type = "question"
title = "Wireshark &amp; Lan-party"
description = '''We&#x27;re gonna have LAN-party with around 160 people and we thought using WireShark to monitor what is going on in our network, for example is there any BitTorrent-traffic or if someone using large amount of bandwith. Can WireShark handle that much data or will it run out of memory in 5 seconds? We don...'''
date = "2012-01-18T10:54:00Z"
lastmod = "2012-01-18T11:04:00Z"
weight = 8456
keywords = [ "lan", "memory" ]
aliases = [ "/questions/8456" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark & Lan-party](/questions/8456/wireshark-lan-party)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We're gonna have LAN-party with around 160 people and we thought using WireShark to monitor what is going on in our network, for example is there any BitTorrent-traffic or if someone using large amount of bandwith. Can WireShark handle that much data or will it run out of memory in 5 seconds? We dont have capacity to test this before the actual event.</p><p>Thank you for great program!</p><p>Best regards, jere.</p></div><div id="question-tags" class="tags-container tags">lan memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '12, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/3e51c710872bfe32a11e4ad0a6f8acee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="riitti&#39;s gravatar image" /><p>riitti<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="riitti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jan '12, 10:55</p></div></div><div id="comments-container-8456" class="comments-container"></div><div id="comment-tools-8456" class="comment-tools"></div><div class="clear"></div><div id="comment-8456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8457"></span>

<div id="answer-container-8457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8457-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can, technically, do this, but it's not the optimal solution. Depending on your equipment and your level of expertise I'd check out ntop.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '12, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-8457" class="comments-container"><span id="8458"></span><div id="comment-8458" class="comment"><div id="post-8458-score" class="comment-score"></div><div class="comment-text"><p>This is my first time monitoring network. Last year we used utangle, but I wasn't monitoring network that time. This year we're running 2x Netgear routers and 8x HP Switches. We still dont have that actual computer where we would run Wireshark (or any else program) because we are not sure how much of RAM or CPU it would use. Gonna check that ntop tomorrow, thanks for you answer!</p></div><div id="comment-8458-info" class="comment-info"><span class="comment-age">(18 Jan '12, 11:15)</span> riitti</div></div><span id="8462"></span><div id="comment-8462" class="comment"><div id="post-8462-score" class="comment-score"></div><div class="comment-text"><p>Ntop provides only "demo"-version for Windows-computers, it is limited to 2000 packets capture. Seems like we need to install ubuntu :-)</p></div><div id="comment-8462-info" class="comment-info"><span class="comment-age">(19 Jan '12, 01:15)</span> riitti</div></div><span id="8464"></span><div id="comment-8464" class="comment"><div id="post-8464-score" class="comment-score">1</div><div class="comment-text"><p>Yep, Ubuntu would be the easy way to go https://help.ubuntu.com/community/Ntop</p></div><div id="comment-8464-info" class="comment-info"><span class="comment-age">(19 Jan '12, 04:55)</span> GeonJay</div></div></div><div id="comment-tools-8457" class="comment-tools"></div><div class="clear"></div><div id="comment-8457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

