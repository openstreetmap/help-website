+++
type = "question"
title = "ESMC packets (Sync-E) presentation in different WS versions"
description = '''Hi All In parallel to my last question regarding different (MPLS) packet presentation in V2 , i have the same problem with ESMC (Sync-E) packets: in V1 (attached here picture) i can see that these packets are ESMC, and i can also see the clock quality and additional parameters (all is correctly perf...'''
date = "2016-08-31T02:51:00Z"
lastmod = "2016-08-31T03:34:00Z"
weight = 55228
keywords = [ "282", "esmc" ]
aliases = [ "/questions/55228" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ESMC packets (Sync-E) presentation in different WS versions](/questions/55228/esmc-packets-sync-e-presentation-in-different-ws-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55228-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All In parallel to my last question regarding different (MPLS) packet presentation in V2 , i have the same problem with ESMC (Sync-E) packets: in V1 (attached here picture) i can see that these packets are ESMC, and i can also see the clock quality and additional parameters (all is correctly perfect presented by WS V1)</p><p>in V2 i can see these packets only as "slow protocol" without any details regarding the ESMC parameters, you can see the V2 output here: <a href="https://www.cloudshark.org/captures/0f90f2c2de86">https://www.cloudshark.org/captures/0f90f2c2de86</a> can it be that V2 is less advanced as V1 ??</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ESMC-in_WS-V1_j42J6M0.jpg" alt="alt text" /></p><p>Thanks Eyal P</p></div><div id="question-tags" class="tags-container tags">282 esmc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/41b6ff54d99111e1b02f77cd7435f0fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eyalp&#39;s gravatar image" /><p>eyalp<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eyalp has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '16, 02:53</p></div></div><div id="comments-container-55228" class="comments-container"></div><div id="comment-tools-55228" class="comment-tools"></div><div class="clear"></div><div id="comment-55228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55230"></span>

<div id="answer-container-55230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55230-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wouldn't say "V2 is less advanced than V1", I would say "the revision of Slow protocols dissector used in your particular 2.0.x has a bug preventing it from properly recognizing OUI <code>00:19:a7</code> as <code>ITU-T</code>, with the consequence of not being able to dissect properly the rest of the frame". So please check whether the development version still has that bug, and if it does, <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a bug</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '16, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55230" class="comments-container"><span id="55232"></span><div id="comment-55232" class="comment"><div id="post-55232-score" class="comment-score"></div><div class="comment-text"><p>There seems to be an OUI interpretation difference, so indeed, file a bug.</p></div><div id="comment-55232-info" class="comment-info"><span class="comment-age">(31 Aug '16, 04:45)</span> Jaap ♦</div></div><span id="55252"></span><div id="comment-55252" class="comment"><div id="post-55252-score" class="comment-score"></div><div class="comment-text"><p>On your behalf I've filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12801">bug 12801</a> and proposed a solution in <a href="https://code.wireshark.org/review/#/c/17425/1">change 17425</a>.</p></div><div id="comment-55252-info" class="comment-info"><span class="comment-age">(31 Aug '16, 12:10)</span> Jaap ♦</div></div><span id="55255"></span><div id="comment-55255" class="comment"><div id="post-55255-score" class="comment-score"></div><div class="comment-text"><p>It's now solved in upcoming 2.0.6, 2.2.0 and development version.</p></div><div id="comment-55255-info" class="comment-info"><span class="comment-age">(31 Aug '16, 15:08)</span> Jaap ♦</div></div></div><div id="comment-tools-55230" class="comment-tools"></div><div class="clear"></div><div id="comment-55230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

