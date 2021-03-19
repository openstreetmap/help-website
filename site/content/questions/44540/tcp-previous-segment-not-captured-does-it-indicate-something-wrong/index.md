+++
type = "question"
title = "[TCP Previous segment not captured] Does it indicate something wrong?"
description = '''Based on my understanding, [TCP Previous segment not captured] means the following:  I receive packet 1. Now instead of receiving packet 2, I receive packet 3 (so packet 3 will be marked with [TCP Previous segment not captured]).  But does [TCP Previous segment not captured] indicates that something...'''
date = "2015-07-27T12:33:00Z"
lastmod = "2015-07-27T13:01:00Z"
weight = 44540
keywords = [ "windows", "tcp", "wireshark" ]
aliases = [ "/questions/44540" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[TCP Previous segment not captured\] Does it indicate something wrong?](/questions/44540/tcp-previous-segment-not-captured-does-it-indicate-something-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44540-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Based on my understanding, [TCP Previous segment not captured] means the following:</p><ol><li>I receive <strong>packet 1</strong>.</li><li>Now instead of receiving <strong>packet 2</strong>, I receive <strong>packet 3</strong> (so <strong>packet 3</strong> will be marked with [TCP Previous segment not captured]).</li></ol><p>But does [TCP Previous segment not captured] indicates that something went wrong? I mean isn't it normal for the packets not to arrive in order, and it's the job of TCP to reorder them?</p></div><div id="question-tags" class="tags-container tags">windows tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/e15d1d4db326472a053064f3e26fc079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_857&#39;s gravatar image" /><p>John_857<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_857 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '15, 12:33</p></div></div><div id="comments-container-44540" class="comments-container"></div><div id="comment-tools-44540" class="comment-tools"></div><div class="clear"></div><div id="comment-44540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44544"></span>

<div id="answer-container-44544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44544-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes and no. If you see a TCP Out-Of-Order within one RTT or so, then generally speaking it is a bit annoying but not the end of the world. If you don't, then you should start looking further.</p><p>To see if it is really causing you an issue you can look at the throughput (Statistics / IO Graph.) If there is a sudden drop or pause in throughput at the same time, you may have an issue, other than that I wouldn't worry too much.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44544" class="comments-container"></div><div id="comment-tools-44544" class="comment-tools"></div><div class="clear"></div><div id="comment-44544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

