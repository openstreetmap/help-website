+++
type = "question"
title = "Wireshark Debug Console buffer size"
description = '''I&#x27;m printing certain messages to the debug console to decode a small section of my code. I print specific messages everytime certain dissectors are called (most are called for each packet), however some of the earlier messages get cut off because the debug console doesn&#x27;t scroll up to the place wher...'''
date = "2012-09-24T22:07:00Z"
lastmod = "2012-09-25T21:36:00Z"
weight = 14493
keywords = [ "buffer", "debug_console" ]
aliases = [ "/questions/14493" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Debug Console buffer size](/questions/14493/wireshark-debug-console-buffer-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14493-score" class="post-score" title="current number of votes">0</div><span id="post-14493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm printing certain messages to the debug console to decode a small section of my code. I print specific messages everytime certain dissectors are called (most are called for each packet), however some of the earlier messages get cut off because the debug console doesn't scroll up to the place where they've been printed. And I don't want to write to file because it slows down my work. Is there some way to increase the buffer size of the debug console so that I can see the them?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span> <span class="post-tag tag-link-debug_console" rel="tag" title="see questions tagged &#39;debug_console&#39;">debug_console</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '12, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-14493" class="comments-container"></div><div id="comment-tools-14493" class="comment-tools"></div><div class="clear"></div><div id="comment-14493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14494"></span>

<div id="answer-container-14494" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14494-score" class="post-score" title="current number of votes">0</div><span id="post-14494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Never mind. I figured it out. Properties-&gt;Layout-&gt;(Increase height of Screen Buffer Size). Sorry for the silly question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '12, 22:16</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-14494" class="comments-container"><span id="14527"></span><div id="comment-14527" class="comment"><div id="post-14527-score" class="comment-score"></div><div class="comment-text"><p>It's OK if you figured it on your own. No need to delete the question. Who knows, someone else might find your answer helpful someday.</p></div><div id="comment-14527-info" class="comment-info"><span class="comment-age">(25 Sep '12, 21:36)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-14494" class="comment-tools"></div><div class="clear"></div><div id="comment-14494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

