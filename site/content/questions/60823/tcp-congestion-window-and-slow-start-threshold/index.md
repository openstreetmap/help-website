+++
type = "question"
title = "TCP congestion window and slow-start threshold"
description = '''I am working on analyzing TCP congestion window for different TCP congestion algorithms but why is the congestion window (cwnd) below the slow-start threshold (ssthresh)?'''
date = "2017-04-13T17:35:00Z"
lastmod = "2017-04-14T01:20:00Z"
weight = 60823
keywords = [ "congestion-control", "congestion-avoidance", "slow-start", "tcp", "congestion" ]
aliases = [ "/questions/60823" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP congestion window and slow-start threshold](/questions/60823/tcp-congestion-window-and-slow-start-threshold)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60823-score" class="post-score" title="current number of votes">0</div><span id="post-60823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on analyzing TCP congestion window for different TCP congestion algorithms but why is the congestion window (cwnd) below the slow-start threshold (ssthresh)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-congestion-control" rel="tag" title="see questions tagged &#39;congestion-control&#39;">congestion-control</span> <span class="post-tag tag-link-congestion-avoidance" rel="tag" title="see questions tagged &#39;congestion-avoidance&#39;">congestion-avoidance</span> <span class="post-tag tag-link-slow-start" rel="tag" title="see questions tagged &#39;slow-start&#39;">slow-start</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '17, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '17, 16:38</strong> </span></p></div></div><div id="comments-container-60823" class="comments-container"></div><div id="comment-tools-60823" class="comment-tools"></div><div class="clear"></div><div id="comment-60823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60825"></span>

<div id="answer-container-60825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60825-score" class="post-score" title="current number of votes">0</div><span id="post-60825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is normally normal. The smaller one of the values for going into slow start again or going into congestion avoidandance mode. Both values are decreased by packet loss and increased by normal ACKs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '17, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-60825" class="comments-container"></div><div id="comment-tools-60825" class="comment-tools"></div><div class="clear"></div><div id="comment-60825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

