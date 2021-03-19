+++
type = "question"
title = "Time zone issues yet again"
description = '''Hey Gerald: Im not sure if your monitoring this feed or not, but we met at Sharkfest &#x27;17 and discussed the MAC address issue, which you took care of straight away, thank you for that. We discussed another issue concerning my inability to computate time. I really find it difficult to find problems in...'''
date = "2017-07-06T11:19:00Z"
lastmod = "2017-07-06T14:11:00Z"
weight = 62590
keywords = [ "timezone", "veiwing", "offset" ]
aliases = [ "/questions/62590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Time zone issues yet again](/questions/62590/time-zone-issues-yet-again)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62590-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey Gerald:</p><p>Im not sure if your monitoring this feed or not, but we met at Sharkfest '17 and discussed the MAC address issue, which you took care of straight away, thank you for that.</p><p>We discussed another issue concerning my inability to computate time. I really find it difficult to find problems in trace files that have occurred in other times zones. Especially in the west coast, maybe it would be easier if I was on the West Coast looking at trace files from the East coast, it might make more sense to me.</p><p>I call myself time challenged. Well we talked about setting the timezone in a command windows to the time zone in which the trace was made.</p><p>This did work in windows XP, and it still does in never version of windows however, its a global change now. Advisors that I work with that read trace files use monitoring systems that uses time indexing to record voice calls and keystrokes that might not like a global change like that. Their stats are based on the time they take a call, analyze an issue and wrap up a call. If a time zone change is made, the system may record a longer or shorter time instead of the actual duration of the call.</p><p>If you recall, I asked if you could do me a favor and add an offset setting to the UTC time of the capture so that the local time that the issue occurred can be seen when viewing the trace with Wireshark. I remember you discussing some things with Anders, but you then suggested the command window idea, which we can not do or should not do, I'm not sure which one.</p><p>Actually Gerald, I want to give this a hack myself, but I am buried with tractor, laptop and cell phone repairs to the point I cant even get to my own repairs during the off time. I wouldn't even know where to start.</p><p>Thank you</p><p>Paul</p></div><div id="question-tags" class="tags-container tags">timezone veiwing offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/fbe6825b890bc4c637a5160e6fb707a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pauli&#39;s gravatar image" /><p>Pauli<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pauli has no accepted answers">0%</span></p></div></div><div id="comments-container-62590" class="comments-container"><span id="62595"></span><div id="comment-62595" class="comment"><div id="post-62595-score" class="comment-score"></div><div class="comment-text"><p>Curious why you aren't using the "Time Shift" feature already built into Wireshark.</p></div><div id="comment-62595-info" class="comment-info"><span class="comment-age">(06 Jul '17, 18:25)</span> Rooster_50</div></div></div><div id="comment-tools-62590" class="comment-tools"></div><div class="clear"></div><div id="comment-62590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62594"></span>

<div id="answer-container-62594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>This did work in windows XP, and it still does in never[sic] version of windows however, its[sic] a global change now.</em></p><p>I just tried this in a Windows 10 command prompt and it didn't appear to be a global change to me. I am also on the East coast and just captured traffic with local time of 17:05. After setting the timezone according to the format specified <a href="https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html">here</a> for Pacific Daylight Savings Time, the packet time was adjusted to 3 hours prior at 14:05, just as expected:</p><pre><code>C:\set TZ=PST+8PDT
C:\wireshark.exe</code></pre><p>My system time remained on Eastern Daylight Savings Time during this test.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62594" class="comments-container"></div><div id="comment-tools-62594" class="comment-tools"></div><div class="clear"></div><div id="comment-62594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

