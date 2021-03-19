+++
type = "question"
title = "Auto Start Wireshark Linux"
description = '''Hello, I am fairly new to Wireshark and need some help. In the past I have installed Wireshark on Windows, created a scheduled task, that ran a command similar to this: c:&#92;Program Files&#92;Wireshark&amp;gt;tshark -i 1 -a duration:3600 -w c:&#92;WiresharkCapture&#92;test What this did was at a specified time, it wo...'''
date = "2016-04-19T10:34:00Z"
lastmod = "2016-04-19T13:29:00Z"
weight = 51797
keywords = [ "scheduled", "command", "automatically", "linux" ]
aliases = [ "/questions/51797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Auto Start Wireshark Linux](/questions/51797/auto-start-wireshark-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am fairly new to Wireshark and need some help. In the past I have installed Wireshark on Windows, created a scheduled task, that ran a command similar to this: c:\Program Files\Wireshark&gt;tshark -i 1 -a duration:3600 -w c:\WiresharkCapture\test</p><p>What this did was at a specified time, it would start a Wireshark scan and break it up into a bunch of files every so many minutes and then dump it into a folder.</p><p>This worked great. However, I am on a Linux (Debian) machine, and don't know how to go about creating the same type of results. Can someone please help?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">scheduled command automatically linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '16, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/03d7a35a481717f0a4665cff06e84d97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darmstrong&#39;s gravatar image" /><p>darmstrong<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darmstrong has no accepted answers">0%</span></p></div></div><div id="comments-container-51797" class="comments-container"></div><div id="comment-tools-51797" class="comment-tools"></div><div class="clear"></div><div id="comment-51797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51799"></span>

<div id="answer-container-51799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and don't know how to go about creating the same type of results.</p></blockquote><p>You would do (almost) the same as on Windows, with the difference, that the scheduler on Linux is cron.</p><blockquote><p><a href="https://help.ubuntu.com/community/CronHowto">https://help.ubuntu.com/community/CronHowto</a><br />
</p></blockquote><p>Please read that and then add a cron job with similar tshark parameters as shown in your question. You'll have to change the path to something Linux like (-w /var/tmp/test).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '16, 13:29</p></div></div><div id="comments-container-51799" class="comments-container"></div><div id="comment-tools-51799" class="comment-tools"></div><div class="clear"></div><div id="comment-51799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

