+++
type = "question"
title = "Find search request"
description = '''I would like to find the request that gets the results of a search in the website http://www.paginasamarillas.es, how is this possible with wireshark?'''
date = "2013-08-05T18:24:00Z"
lastmod = "2013-08-05T22:58:00Z"
weight = 23567
keywords = [ "filter", "capture", "request", "results", "wireshark" ]
aliases = [ "/questions/23567" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find search request](/questions/23567/find-search-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23567-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to find the request that gets the results of a search in the website <a href="http://www.paginasamarillas.es"></a><a href="http://www.paginasamarillas.es">http://www.paginasamarillas.es</a>, how is this possible with wireshark?</p></div><div id="question-tags" class="tags-container tags">filter capture request results wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '13, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/c040ea3524f4f624cd1956702651afd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cricobs&#39;s gravatar image" /><p>cricobs<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cricobs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '13, 18:29</p></div></div><div id="comments-container-23567" class="comments-container"></div><div id="comment-tools-23567" class="comment-tools"></div><div class="clear"></div><div id="comment-23567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23572"></span>

<div id="answer-container-23572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23572-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would start with a</p><pre><code>frame matches paginasamarillas.es</code></pre><p>This gives you all packets that contain this string, also DNS queries and responses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-23572" class="comments-container"></div><div id="comment-tools-23572" class="comment-tools"></div><div class="clear"></div><div id="comment-23572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

