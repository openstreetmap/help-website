+++
type = "question"
title = "Just getting my own logs . . ."
description = '''I have a macbook pro mid 2010, ios10.9 I installed Wireshark, and watched the tutorials. It works but only on my computer, but not on any other device. Any suggestions? Oh, I disabled my mac firewall. Good idea?'''
date = "2014-10-03T20:05:00Z"
lastmod = "2014-10-03T20:46:00Z"
weight = 36830
keywords = [ "solo", "pro", "macbook", "wireshark" ]
aliases = [ "/questions/36830" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Just getting my own logs . . .](/questions/36830/just-getting-my-own-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36830-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a macbook pro mid 2010, ios10.9 I installed Wireshark, and watched the tutorials. It works but only on my computer, but not on any other device. Any suggestions? Oh, I disabled my mac firewall. Good idea?</p></div><div id="question-tags" class="tags-container tags">solo pro macbook wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '14, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/351c40af27344bc7cce28dd4b06e162c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fentonnyc&#39;s gravatar image" /><p>fentonnyc<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fentonnyc has no accepted answers">0%</span></p></div></div><div id="comments-container-36830" class="comments-container"></div><div id="comment-tools-36830" class="comment-tools"></div><div class="clear"></div><div id="comment-36830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36831"></span>

<div id="answer-container-36831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36831-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will only "see" traffic that is reaching the interface that you are capturing on. Another computer sending traffic to a common router or switch toward the Internet (for example) is not going to reach your computer's network card, so Wireshark won't see it.</p><p>To get traffic from other systems, you need to get that traffic to your system's network card. One common method is "port mirroring", where traffic to and from one interface on your switch or router is 'mirrored' on a port that your machine is connected to, allowing it to listen in with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 20:46</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-36831" class="comments-container"><span id="36832"></span><div id="comment-36832" class="comment"><div id="post-36832-score" class="comment-score"></div><div class="comment-text"><p>"Port mirroring"? How do I get that?</p></div><div id="comment-36832-info" class="comment-info"><span class="comment-age">(03 Oct '14, 20:52)</span> fentonnyc</div></div><span id="36833"></span><div id="comment-36833" class="comment"><div id="post-36833-score" class="comment-score"></div><div class="comment-text"><p>Network switches often support port mirroring as a configurable feature, though it's not common in home networks.</p><p>Either way, the challenge of how to get a particular type of network traffic to your computer is one that you will need some basic networking knowledge, and knowledge of how your own network works in order to solve.</p></div><div id="comment-36833-info" class="comment-info"><span class="comment-age">(03 Oct '14, 22:00)</span> Quadratic</div></div><span id="36836"></span><div id="comment-36836" class="comment"><div id="post-36836-score" class="comment-score"></div><div class="comment-text"><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> and the appropriate sub pages listed at the bottom for the particular media you are capturing on for more info.</p></div><div id="comment-36836-info" class="comment-info"><span class="comment-age">(04 Oct '14, 01:45)</span> grahamb ♦</div></div></div><div id="comment-tools-36831" class="comment-tools"></div><div class="clear"></div><div id="comment-36831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

