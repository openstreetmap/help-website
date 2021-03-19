+++
type = "question"
title = "Does Wireshark have Chattiness and/or Round Trip Counter?"
description = '''Hi. In diagnosing application performance problems, I am very often faced with transactions that are slow because they are &quot;chatty&quot; - that is, requiring a large number of round trips to complete the transaction. (Of course, the impact of the chattiness is also dependent on the end-to-end latency bet...'''
date = "2011-07-04T07:30:00Z"
lastmod = "2011-07-06T13:32:00Z"
weight = 4899
keywords = [ "roundtrips", "chattiness" ]
aliases = [ "/questions/4899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark have Chattiness and/or Round Trip Counter?](/questions/4899/does-wireshark-have-chattiness-andor-round-trip-counter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4899-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. In diagnosing application performance problems, I am very often faced with transactions that are slow because they are "chatty" - that is, requiring a large number of round trips to complete the transaction. (Of course, the impact of the chattiness is also dependent on the end-to-end latency between the endpoints.)</p><p>In the past, I have used another diagnostic tool - Opnet. This tool does a good job of reporting on the chattiness / round trip count, and its precise contribution to the transaction duration. But, Opnet is an expensive tool, not available to many of us packeteers.</p><p>So my question is... What features and/or techniques are recommended for measuring the impact of chattiness with Wireshark?</p><p>One technique, I suppose (thinking out loud now), would be to filter on packets between the 2 endpoints, and exclude those non-data-bearing packets, and then count the number of packets and the elapsed time between the first and last packets. This should give you number of round trips (half the packet count), and the duration of the transaction. This would give you an IDEA of the impact of chattiness, but the elapsed time would also include time spent on either end processing between packet exchanges, so you would have to be careful how to interpret this.</p><p>Anyway, does anyone have other suggestions? Or, is there a feature/option of Wireshark that I have ignored?</p><p>Thx all, feenyman99</p></div><div id="question-tags" class="tags-container tags">roundtrips chattiness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-4899" class="comments-container"></div><div id="comment-tools-4899" class="comment-tools"></div><div class="clear"></div><div id="comment-4899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4931"></span>

<div id="answer-container-4931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4931-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you can get a good idea by looking at the conversation summary. Just go to statistics - conversations and click the appropriate tab (usually TCP) you can then gat an idea of duration, avg packet size, etc.</p><p>Hope it helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/bdbf9eb175760c2fdcab4d7a2187945c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ericinsd&#39;s gravatar image" /><p>ericinsd<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ericinsd has no accepted answers">0%</span></p></div></div><div id="comments-container-4931" class="comments-container"></div><div id="comment-tools-4931" class="comment-tools"></div><div class="clear"></div><div id="comment-4931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

