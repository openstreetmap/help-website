+++
type = "question"
title = "Increasing the size of an array (realloc)"
description = '''Can you use realloc to resize an array? or do i have to do it the manual way??. At the moment realloc crashes wireshark but i may be using incorrectly'''
date = "2013-02-05T19:55:00Z"
lastmod = "2013-02-05T20:21:00Z"
weight = 18348
keywords = [ "array", "resize" ]
aliases = [ "/questions/18348" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Increasing the size of an array (realloc)](/questions/18348/increasing-the-size-of-an-array-realloc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18348-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can you use realloc to resize an array? or do i have to do it the manual way??. At the moment realloc crashes wireshark but i may be using incorrectly</p></div><div id="question-tags" class="tags-container tags">array resize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '13, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p>StealthUE<br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div></div><div id="comments-container-18348" class="comments-container"></div><div id="comment-tools-18348" class="comment-tools"></div><div class="clear"></div><div id="comment-18348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18349"></span>

<div id="answer-container-18349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18349-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean by "array"? A C array defined as, say <code>int foo[20]</code> cannot be resized at all. C99 supports variable-length arrays, as do pre-C99 versions of GCC, but those arrays aren't resizable - the size is fixed at the time the array is allocated.</p><p>If you use <code>malloc()</code> to allocate an array at run time, you can use <code>realloc()</code> to resize it. If that's crashing, you might be using it wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 20:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18349" class="comments-container"></div><div id="comment-tools-18349" class="comment-tools"></div><div class="clear"></div><div id="comment-18349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

