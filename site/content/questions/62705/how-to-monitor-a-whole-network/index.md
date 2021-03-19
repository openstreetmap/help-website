+++
type = "question"
title = "How to Monitor a whole network"
description = '''I work with industrial control systems. I often use an old non switching hub to monitor traffic between several devices, but I now have a problem where this would not be appropriate. It is a network with bandwidth problems, and the central 100MB switch is routing raw ethernet packets between several...'''
date = "2017-07-12T07:35:00Z"
lastmod = "2017-07-12T07:47:00Z"
weight = 62705
keywords = [ "analysis", "switch", "bandwidth", "monitor", "hub" ]
aliases = [ "/questions/62705" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to Monitor a whole network](/questions/62705/how-to-monitor-a-whole-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I work with industrial control systems. I often use an old non switching hub to monitor traffic between several devices, but I now have a problem where this would not be appropriate.</p><p>It is a network with bandwidth problems, and the central 100MB switch is routing raw ethernet packets between several different ports, as well as some ordinary IP traffic.</p><p>I need to find the bottlenecks and who is using most bandwidth etc...putting a hub in place of a switch is going to completely change the situation.</p><p>I know 'managed' switch have a lot of extra config possibilities, is there any way I could eg. monitor traffic on a GB managed switch with one port specially configured to output to WireShark?</p><p>Would it be realistic?</p></div><div id="question-tags" class="tags-container tags">analysis switch bandwidth monitor hub</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '17, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/1891e78e7bad6bbc6c00135a398f30c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogerIrwin&#39;s gravatar image" /><p>RogerIrwin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogerIrwin has no accepted answers">0%</span></p></div></div><div id="comments-container-62705" class="comments-container"></div><div id="comment-tools-62705" class="comment-tools"></div><div class="clear"></div><div id="comment-62705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62706"></span>

<div id="answer-container-62706" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62706-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is called port mirroring or spanning, see <a href="https://en.wikipedia.org/wiki/Port_mirroring">here</a> for info and have a look at the Wireshark wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">Ethernet Capture</a> for info on how to capture on a mirror port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '17, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62706" class="comments-container"><span id="62707"></span><div id="comment-62707" class="comment"><div id="post-62707-score" class="comment-score"></div><div class="comment-text"><p>Thanks, some very clear explanations at the end of those links.</p></div><div id="comment-62707-info" class="comment-info"><span class="comment-age">(12 Jul '17, 08:14)</span> RogerIrwin</div></div></div><div id="comment-tools-62706" class="comment-tools"></div><div class="clear"></div><div id="comment-62706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

