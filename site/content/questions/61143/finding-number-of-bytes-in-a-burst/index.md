+++
type = "question"
title = "Finding number of bytes in a burst"
description = '''Hi, How can I calculate the total number of bytes transported in a burst? Where there are 0 bytes transported before and after a section of traffic. '''
date = "2017-05-01T14:00:00Z"
lastmod = "2017-05-01T15:23:00Z"
weight = 61143
keywords = [ "bursts", "block-size" ]
aliases = [ "/questions/61143" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Finding number of bytes in a burst](/questions/61143/finding-number-of-bytes-in-a-burst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61143-score" class="post-score" title="current number of votes">0</div><span id="post-61143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, How can I calculate the total number of bytes transported in a burst? Where there are 0 bytes transported before and after a section of traffic.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bursts" rel="tag" title="see questions tagged &#39;bursts&#39;">bursts</span> <span class="post-tag tag-link-block-size" rel="tag" title="see questions tagged &#39;block-size&#39;">block-size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '17, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/eb5865c02f2d8398a2d02f7038b52da3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarah&#39;s gravatar image" /><p><span>Sarah</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarah has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '17, 14:01</strong> </span></p></div></div><div id="comments-container-61143" class="comments-container"></div><div id="comment-tools-61143" class="comment-tools"></div><div class="clear"></div><div id="comment-61143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61145"></span>

<div id="answer-container-61145" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61145-score" class="post-score" title="current number of votes">0</div><span id="post-61145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sarah has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My approach would be:</p><ul><li>Open an IO graph (Statistics &gt; I/O Graph)</li><li>Define "Y Axis" as "Bytes"</li><li>Define "Smoothing" as "None"</li><li>Define "Style" as "Dot"</li><li>Define "Interval" as whatever burst rate you want to measure</li></ul><p>The result should be that every interval (for example 10ms) will have a dot plotted on the graph for the aggregate byte count within the defined time interval, which can be set as low as 1ms. Hit "reset" to align the graph for readabilty, add any display filter you want to drill down on (eg: measure burst rate of particular traffic types), and that should pretty much give you what it sounds like you're looking for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '17, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-61145" class="comments-container"></div><div id="comment-tools-61145" class="comment-tools"></div><div class="clear"></div><div id="comment-61145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

