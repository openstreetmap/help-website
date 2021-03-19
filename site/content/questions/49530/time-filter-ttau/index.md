+++
type = "question"
title = "Time Filter = t+tau"
description = '''Hi, I want to create a filter where it capture packet from X time to X+10 secs Example: The packet i click, it take its time and add 10 secs to its time and show only those packets that are only in this time range. Scope_:   * How i can get automatically the time of packet where i click. %%frame.tim...'''
date = "2016-01-27T02:19:00Z"
lastmod = "2016-01-27T06:01:00Z"
weight = 49530
keywords = [ "frame.time" ]
aliases = [ "/questions/49530" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Time Filter = t+tau](/questions/49530/time-filter-ttau)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49530-score" class="post-score" title="current number of votes">0</div><span id="post-49530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to create a filter where it capture packet from X time to X+10 secs Example: The packet i click, it take its time and add 10 secs to its time and show only those packets that are only in this time range.</p><p>Scope_: * How i can get automatically the time of packet where i click. %%frame.time is static if i save the filter. i need to create dynamic filter * How to add 10 secs from above mentioned time</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame.time" rel="tag" title="see questions tagged &#39;frame.time&#39;">frame.time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '16, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/e57ca27b0c054972a3bc8e5329413614?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mi121647&#39;s gravatar image" /><p><span>mi121647</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mi121647 has no accepted answers">0%</span></p></div></div><div id="comments-container-49530" class="comments-container"></div><div id="comment-tools-49530" class="comment-tools"></div><div class="clear"></div><div id="comment-49530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49536"></span>

<div id="answer-container-49536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49536-score" class="post-score" title="current number of votes">0</div><span id="post-49536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The highest degree of automation I know about is the following:</p><ul><li>click the packet in the packet <em>list</em> pane</li><li>in packet <em>dissection</em> pane, unfold the frame layer</li><li>right-click the <code>Arrival Time</code> or <code>Time since reference or first frame</code> line, whichever suits your way of thinking better (but the latter is easier to increase by your desired τ value), and choose <code>Apply as Filter -&gt; Selected</code> from the context menu</li><li>do the same again, except that you choose <code>Apply as Filter -&gt; ...and Selected</code></li><li>manually modify the two <code>==</code> in the display filter field to <code>&gt;=</code> and <code>&lt;=</code> and add τ to the correct one</li><li>re-apply the display filter</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '16, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49536" class="comments-container"><span id="49537"></span><div id="comment-49537" class="comment"><div id="post-49537-score" class="comment-score"></div><div class="comment-text"><p>Thank you Sindy,</p><p>Yes you are right. But i want to automate beyond the above mentioned solution.</p></div><div id="comment-49537-info" class="comment-info"><span class="comment-age">(27 Jan '16, 04:10)</span> <span class="comment-user userinfo">mi121647</span></div></div><span id="49539"></span><div id="comment-49539" class="comment"><div id="post-49539-score" class="comment-score"></div><div class="comment-text"><p>Sounds like you need a compiler and the source code then ;-)</p></div><div id="comment-49539-info" class="comment-info"><span class="comment-age">(27 Jan '16, 04:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="49545"></span><div id="comment-49545" class="comment"><div id="post-49545-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, I am beginner. can you guide me to some thread/ thing where i get guidance on it :)</p></div><div id="comment-49545-info" class="comment-info"><span class="comment-age">(27 Jan '16, 06:01)</span> <span class="comment-user userinfo">mi121647</span></div></div></div><div id="comment-tools-49536" class="comment-tools"></div><div class="clear"></div><div id="comment-49536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

