+++
type = "question"
title = "Out of order on point-to-point connection"
description = '''Is it possible to have out of order packets in wireshark ok point to point connection? I mean, no switch, no router between hosts. Simply two server connected each other by 10Gb ethernet cable. Thank you.'''
date = "2014-07-08T22:13:00Z"
lastmod = "2014-07-09T01:31:00Z"
weight = 34491
keywords = [ "tcp", "outoforder" ]
aliases = [ "/questions/34491" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Out of order on point-to-point connection](/questions/34491/out-of-order-on-point-to-point-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34491-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to have out of order packets in wireshark ok point to point connection? I mean, no switch, no router between hosts. Simply two server connected each other by 10Gb ethernet cable.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">tcp outoforder</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '14, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/e1f10dfea2a6a0469adb5ad9fefda1a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="becco981&#39;s gravatar image" /><p>becco981<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="becco981 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34491" class="comments-container"></div><div id="comment-tools-34491" class="comment-tools"></div><div class="clear"></div><div id="comment-34491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34495"></span>

<div id="answer-container-34495" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34495-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess that's being caused by the NIC driver. As you mentioned 10Gb, chances are good that there is at lease some 'intelligence' in the NIC and who knows how the driver decides in which order to deliver the received frames to the OS, especially on a multi CPU system and also considering checksum offloading and TCP segment offloading.</p><p>So, yes packet reordering (as shown by Wireshark) can happen on a direct link. My bet for the most likely reason: the NIC driver</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '14, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '14, 01:32</p></div></div><div id="comments-container-34495" class="comments-container"><span id="34532"></span><div id="comment-34532" class="comment"><div id="post-34532-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Just one more clarification: in wireshark I can see out of order packets only after "Previous segment not captured". Are they really out of order or they're just a consequence of not captured packets?</p></div><div id="comment-34532-info" class="comment-info"><span class="comment-age">(09 Jul '14, 21:47)</span> becco981</div></div><span id="34540"></span><div id="comment-34540" class="comment"><div id="post-34540-score" class="comment-score"></div><div class="comment-text"><p>More likely the later one.</p></div><div id="comment-34540-info" class="comment-info"><span class="comment-age">(10 Jul '14, 01:05)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34495" class="comment-tools"></div><div class="clear"></div><div id="comment-34495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

