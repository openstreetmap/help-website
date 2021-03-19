+++
type = "question"
title = "What is the vertical line with &quot;W&quot; on VOIP decoded RTP streams?"
description = '''When I decode a VOIP call, I see vertical lines in the RTP player. Most of them are yellow with a &quot;W&quot; beside it. Some are red with a &quot;D&quot; (I believ) beside it. They are obviously located where the sound quality is bad. How do I learn more about those errors?  Thanks Dan'''
date = "2011-12-08T15:37:00Z"
lastmod = "2011-12-08T15:49:00Z"
weight = 7854
keywords = [ "decode", "player", "rtp", "voip" ]
aliases = [ "/questions/7854" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the vertical line with "W" on VOIP decoded RTP streams?](/questions/7854/what-is-the-vertical-line-with-w-on-voip-decoded-rtp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I decode a VOIP call, I see vertical lines in the RTP player. Most of them are yellow with a "W" beside it. Some are red with a "D" (I believ) beside it. They are obviously located where the sound quality is bad. How do I learn more about those errors? Thanks Dan</p></div><div id="question-tags" class="tags-container tags">decode player rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '11, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/c1c349f269892c3b94a854a18a4d6b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="piuslor&#39;s gravatar image" /><p>piuslor<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="piuslor has one accepted answer">100%</span></p></div></div><div id="comments-container-7854" class="comments-container"></div><div id="comment-tools-7854" class="comment-tools"></div><div class="clear"></div><div id="comment-7854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7856"></span>

<div id="answer-container-7856" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7856-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>W wrong timestamp,</p><p>D dropped by jitter...,</p><p>S silence inserted (did not have that in my example)</p><p>just <a href="http://ask.wireshark.org/questions/7240/is-there-a-legend-for-the-symbols-used-in-rtp-player/7241" title="link">found</a> it myself.. shame on me.. dan</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '11, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/c1c349f269892c3b94a854a18a4d6b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="piuslor&#39;s gravatar image" /><p>piuslor<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="piuslor has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '11, 15:54</p></div></div><div id="comments-container-7856" class="comments-container"></div><div id="comment-tools-7856" class="comment-tools"></div><div class="clear"></div><div id="comment-7856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7857"></span>

<div id="answer-container-7857" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7857-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://ask.wireshark.org/questions/7240/is-there-a-legend-for-the-symbols-used-in-rtp-player">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '11, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7857" class="comments-container"></div><div id="comment-tools-7857" class="comment-tools"></div><div class="clear"></div><div id="comment-7857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

