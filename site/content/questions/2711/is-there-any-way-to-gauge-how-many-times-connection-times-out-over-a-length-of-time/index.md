+++
type = "question"
title = "Is there any way to gauge how many times connection times out over a length of time?"
description = '''I&#x27;ve been &quot;suffering&quot; from an extremely unstable ISP for the past several years and its just been getting worse and worse. It&#x27;s impossible to play games online now because every 2 minutes or so I will &quot;lag&quot; and be unable to move for 5-10 seconds and this happens constantly. Is there any way with thi...'''
date = "2011-03-08T01:10:00Z"
lastmod = "2011-03-08T10:39:00Z"
weight = 2711
keywords = [ "lost", "connection", "disconnect", "packet", "timeout" ]
aliases = [ "/questions/2711" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to gauge how many times connection times out over a length of time?](/questions/2711/is-there-any-way-to-gauge-how-many-times-connection-times-out-over-a-length-of-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been "suffering" from an extremely unstable ISP for the past several years and its just been getting worse and worse. It's impossible to play games online now because every 2 minutes or so I will "lag" and be unable to move for 5-10 seconds and this happens constantly. Is there any way with this program to measure how many times this "lag" period happens over night? I apologize for using rough vocabulary but I don't know the technical terms for networking stuff.</p></div><div id="question-tags" class="tags-container tags">lost connection disconnect packet timeout</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '11, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/f8ddf18ef20417ffc2fc1f6fab2a3344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryan%20Bamford&#39;s gravatar image" /><p>Ryan Bamford<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryan Bamford has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Mar '11, 01:10</p></div></div><div id="comments-container-2711" class="comments-container"></div><div id="comment-tools-2711" class="comment-tools"></div><div class="clear"></div><div id="comment-2711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2713"></span>

<div id="answer-container-2713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2713-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can measure lag periods, but it might require a solid understanding of the network protocols you want to examine for lags. The easiest part is to capture the data, usually by going for a "capture to disk" kind of setup using the "Capture Options" dialog and saving the data to multiple trace files.</p><p>Then, you need to examine your captured trace files for lags by looking at the delta times between request and answer packets. First of all you need to set a column to "delta time displayed" mode, and then figure out where it shows higher values than it should. This is the hard part since there are network protocols where delays are sometimes higher without indicating a problem, while with others any delay means trouble.</p><p>Without knowledge about the protocol behavior you could try a statistical approach and gather data when everything is running fine and compare timings to problematic hours. If the delta time readings differ significantly your connection is in trouble - but keep in mind that it might still not be the ISP's fault. Maybe somebody in your location is using the line at the same time to download some large files, which will cause your real time communication to get delayed.</p><p>On the other hand - if your ISP is unstable you might want to look at this from a different angle. We had trouble with the line in our office a few years ago but we had a pretty decent router that could get us physical link statistics, like the "Signal to Noise Ratio" which is very important. In our case our 6MBit line had a SnR of about 6.5db, which was a catastrophic value. We ordered a different ISP line and downgraded the 6MBit line to 1MBit (because it had a static IP we still needed), and the SnR went up to 32db. Maybe your router/cable modem can give you statistics like that, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '11, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2713" class="comments-container"></div><div id="comment-tools-2713" class="comment-tools"></div><div class="clear"></div><div id="comment-2713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

