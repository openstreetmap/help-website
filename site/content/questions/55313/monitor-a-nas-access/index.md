+++
type = "question"
title = "Monitor a NAS access"
description = '''Newbie alert Hi, I recently bought a Buffalo NAS, I had , wrongly assumed, that it would have some form of monitoring software package with it. Now I&#x27;m stuck not knowing who has accessed data on the NAS. Is Wireshark capable of monitoring a specific IP and logging the connected IP address, times, an...'''
date = "2016-09-03T02:41:00Z"
lastmod = "2016-09-03T03:02:00Z"
weight = 55313
keywords = [ "nas" ]
aliases = [ "/questions/55313" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor a NAS access](/questions/55313/monitor-a-nas-access)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Newbie alert</p><p>Hi, I recently bought a Buffalo NAS, I had , wrongly assumed, that it would have some form of monitoring software package with it. Now I'm stuck not knowing who has accessed data on the NAS. Is Wireshark capable of monitoring a specific IP and logging the connected IP address, times, and file access?</p></div><div id="question-tags" class="tags-container tags">nas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '16, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/56260d04b442a3fbd4acc92763dd912c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Princy557&#39;s gravatar image" /><p>Princy557<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Princy557 has no accepted answers">0%</span></p></div></div><div id="comments-container-55313" class="comments-container"></div><div id="comment-tools-55313" class="comment-tools"></div><div class="clear"></div><div id="comment-55313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55314"></span>

<div id="answer-container-55314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55314-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a network analysis power tool. That means that it drills down into every network packet and gets down to the bit level showing all protocol details. What you're looking for is a more high level view of application access. So even though it can be done, it may prove highly unpractical. Other tools may be more practical for day to day use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '16, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55314" class="comments-container"><span id="55315"></span><div id="comment-55315" class="comment"><div id="post-55315-score" class="comment-score"></div><div class="comment-text"><p>Thanks for an extremely quick response. Well that is what I had thought, But really wanted to check before installing it. Only other question is, Do you (or anyone reading this) know of a suitable package to monitor a NAS access software package Thanks again Princy557</p></div><div id="comment-55315-info" class="comment-info"><span class="comment-age">(03 Sep '16, 03:07)</span> Princy557</div></div><span id="55319"></span><div id="comment-55319" class="comment"><div id="post-55319-score" class="comment-score"></div><div class="comment-text"><p>From this <a href="https://ask.wireshark.org/questions/54064/endpoint-statistics-how-can-i-find-a-computer-abusing-network-bandwidth?page=1&amp;focusedAnswerId=54083#54083">answer</a>, perhaps one of these options will meet your needs or at least get you started? No file access information would be available as these are network tools, not application layer tools. To get file access you likely the need the OS to do it. I'm sure any main stream OS used for file serving has this capability, but when you buy the NAS it is a canned application that may or may not contain that level of detail. I am guessing it doesn't since you are asking here...</p><p>A nice <a href="http://unix.stackexchange.com/questions/12247/linux-file-access-monitoring">link</a> on some options going forward if you use Linux, but I realize this does not help you here with the device you purchased.</p></div><div id="comment-55319-info" class="comment-info"><span class="comment-age">(03 Sep '16, 09:21)</span> Bob Jones</div></div></div><div id="comment-tools-55314" class="comment-tools"></div><div class="clear"></div><div id="comment-55314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

