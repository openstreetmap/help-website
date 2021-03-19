+++
type = "question"
title = "Logging End Point  Data"
description = '''I want to write a batch script that automatically creates a log periodically with the endpoint communication data which is found on Statistics &amp;gt; EndPoints &amp;gt; ipv4'''
date = "2013-02-20T23:10:00Z"
lastmod = "2013-02-20T23:34:00Z"
weight = 18793
keywords = [ "automated", "endpoints", "logging", "periodic" ]
aliases = [ "/questions/18793" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Logging End Point Data](/questions/18793/logging-end-point-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18793-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a batch script that automatically creates a log periodically with the endpoint communication data which is found on Statistics &gt; EndPoints &gt; ipv4</p></div><div id="question-tags" class="tags-container tags">automated endpoints logging periodic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/0752849c661ba26916da497635abb5c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AshwinSethi&#39;s gravatar image" /><p>AshwinSethi<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AshwinSethi has no accepted answers">0%</span></p></div></div><div id="comments-container-18793" class="comments-container"></div><div id="comment-tools-18793" class="comment-tools"></div><div class="clear"></div><div id="comment-18793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18795"></span>

<div id="answer-container-18795" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18795-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at tshark statistics. If that provides what you need then setup a loop with dumpcap with ringbuffer set to duration to write a file and have tshark process it for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18795" class="comments-container"><span id="18798"></span><div id="comment-18798" class="comment"><div id="post-18798-score" class="comment-score"></div><div class="comment-text"><p>Superb... Will just need to get a little more familiar with tshark commands and options. But got the concept. Thanks</p></div><div id="comment-18798-info" class="comment-info"><span class="comment-age">(21 Feb '13, 06:16)</span> AshwinSethi</div></div><span id="18801"></span><div id="comment-18801" class="comment"><div id="post-18801-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-18801-info" class="comment-info"><span class="comment-age">(21 Feb '13, 08:01)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18795" class="comment-tools"></div><div class="clear"></div><div id="comment-18795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

