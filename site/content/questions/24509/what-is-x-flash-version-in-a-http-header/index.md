+++
type = "question"
title = "What is x-flash-version in a HTTP header?"
description = '''I am analysing a PCAP file and it contains a field &quot;x-flash-version: 10,0,32,18&quot;. What is this field? Does it refer to the flash version on the PC? Where can I find more info about this field?'''
date = "2013-09-10T00:26:00Z"
lastmod = "2013-09-10T02:04:00Z"
weight = 24509
keywords = [ "capture", "http" ]
aliases = [ "/questions/24509" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is x-flash-version in a HTTP header?](/questions/24509/what-is-x-flash-version-in-a-http-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24509-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analysing a PCAP file and it contains a field "x-flash-version: 10,0,32,18". What is this field? Does it refer to the flash version on the PC? Where can I find more info about this field?</p></div><div id="question-tags" class="tags-container tags">capture http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '13, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/a12160c79489f265830c301827815b97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheRookieLearner&#39;s gravatar image" /><p>TheRookieLea...<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheRookieLearner has no accepted answers">0%</span></p></div></div><div id="comments-container-24509" class="comments-container"></div><div id="comment-tools-24509" class="comment-tools"></div><div class="clear"></div><div id="comment-24509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24515"></span>

<div id="answer-container-24515" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24515-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Prior to the deprecation of the "X-" format (see <a href="http://tools.ietf.org/html/rfc6648">RFC 6648</a>) any X- prefixed header is an eXperimental or non-standard additional header. In this case it would seem that some application is reporting the version of flash in use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24515" class="comments-container"><span id="24517"></span><div id="comment-24517" class="comment"><div id="post-24517-score" class="comment-score"></div><div class="comment-text"><p>thanks for the hint about RFC 6648. I was not aware of that !?!</p></div><div id="comment-24517-info" class="comment-info"><span class="comment-age">(10 Sep '13, 03:52)</span> Kurt Knochner ♦</div></div><span id="24518"></span><div id="comment-24518" class="comment"><div id="post-24518-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Where can I find more info about this field?</p></blockquote><p>@TheRookieLea...: Maybe at google?: <a href="http://bit.ly/13EFiIJ">http://bit.ly/13EFiIJ</a></p></div><div id="comment-24518-info" class="comment-info"><span class="comment-age">(10 Sep '13, 03:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24515" class="comment-tools"></div><div class="clear"></div><div id="comment-24515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

