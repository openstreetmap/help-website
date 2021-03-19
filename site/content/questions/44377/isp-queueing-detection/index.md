+++
type = "question"
title = "ISP Queueing - Detection"
description = '''If one suspects that their ISP (a business line) is queueing packets can this be detected with Wireshark? Are there markers or tags to look for within a capture that would indicate a types of queueing? thx, J'''
date = "2015-07-22T09:55:00Z"
lastmod = "2015-07-22T19:27:00Z"
weight = 44377
keywords = [ "isp" ]
aliases = [ "/questions/44377" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ISP Queueing - Detection](/questions/44377/isp-queueing-detection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44377-score" class="post-score" title="current number of votes">0</div><span id="post-44377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If one suspects that their ISP (a business line) is queueing packets can this be detected with Wireshark? Are there markers or tags to look for within a capture that would indicate a types of queueing?</p><p>thx,</p><p>J</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-isp" rel="tag" title="see questions tagged &#39;isp&#39;">isp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '15, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p><span>JTech_17</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-44377" class="comments-container"></div><div id="comment-tools-44377" class="comment-tools"></div><div class="clear"></div><div id="comment-44377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44401"></span>

<div id="answer-container-44401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44401-score" class="post-score" title="current number of votes">0</div><span id="post-44401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Traffic shaping or policing wouldn't normally be as detectable as a tag or marker. For a business line, one suggestion is to confirm the committed information rate (CIR) and do a performance test to prove you aren't receiving it. A tool such as iPerf comes to mind.</p><p>Policers in particular can be detected sometimes with a rapid ping stream. If you see pings being dropped on relatively fixed time intervals, that can indicate a policer which is hitting its byte quota within its set time interval, then refreshing the quota at the beginning of the next interval.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-44401" class="comments-container"></div><div id="comment-tools-44401" class="comment-tools"></div><div class="clear"></div><div id="comment-44401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

