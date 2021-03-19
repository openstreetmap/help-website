+++
type = "question"
title = "Filter for packets containing &quot;If-Modified-Since&quot;"
description = '''I am trying to figure out a display filter to find any packets containing &quot;If-Modified-Since&quot; indicating they have the element they are looking for in cache. I did a right-click, Aplly as Filter, Selected, but this is ineffective since it applies a very long filter looking for the If-Modified-Since ...'''
date = "2013-11-07T08:45:00Z"
lastmod = "2013-11-07T11:24:00Z"
weight = 26723
keywords = [ "http", "display-filter" ]
aliases = [ "/questions/26723" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filter for packets containing "If-Modified-Since"](/questions/26723/filter-for-packets-containing-if-modified-since)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26723-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to figure out a display filter to find any packets containing "If-Modified-Since" indicating they have the element they are looking for in cache. I did a right-click, Aplly as Filter, Selected, but this is ineffective since it applies a <em>very</em> long filter looking for the If-Modified-Since and the full time-stamp. An example looks like:</p><pre><code>frame[804:50] == 49:66:2d:4d:6f:64:69:66:69:65:64:2d:53:69:6e:63:65:3a:20:54:75:65:2c:20:30:34:20:41:75:67:20:32:30:30:39:20:32:31:3a:32:33:3a:30:39:20:47:4d:54:0d:0a</code></pre><p>Other display filters I have tried:</p><p>data contains "If-Modified-Since"</p><p>data matches "If-Modified-Since"</p><p>data-text-lines matches "If-Modified-Since"</p><p>data-text-lines contains "If-Modified-Since"</p><p>And I have experimented with the "text" display filter (which I cannot find in the Display Filter Reference or in the expressions window).</p><p>I'm stumped. Anybody have an idea how to find If-Modified-Since in any packet that contains it?</p><p>Thanks in advance...</p></div><div id="question-tags" class="tags-container tags">http display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span></p></div></div><div id="comments-container-26723" class="comments-container"></div><div id="comment-tools-26723" class="comment-tools"></div><div class="clear"></div><div id="comment-26723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26728"></span>

<div id="answer-container-26728" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26728-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>http matches "If-Modified-Since"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-26728" class="comments-container"><span id="26729"></span><div id="comment-26729" class="comment"><div id="post-26729-score" class="comment-score"></div><div class="comment-text"><p>Excellent! Thank you.</p></div><div id="comment-26729-info" class="comment-info"><span class="comment-age">(07 Nov '13, 11:32)</span> kpalmgren</div></div></div><div id="comment-tools-26728" class="comment-tools"></div><div class="clear"></div><div id="comment-26728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

