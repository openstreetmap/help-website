+++
type = "question"
title = "LTE decoding options."
description = '''I wanted to know if theres a Tshark script (or i can create one and some how build a way to see if something isnt right Look at it) LIke Low latency issues / Or Its not talking to MME/SGW or issues.  unless theres cool ways or place i can look online.'''
date = "2014-09-24T17:37:00Z"
lastmod = "2014-09-24T21:26:00Z"
weight = 36577
keywords = [ "capture-filters", "lte" ]
aliases = [ "/questions/36577" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LTE decoding options.](/questions/36577/lte-decoding-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36577-score" class="post-score" title="current number of votes">0</div><span id="post-36577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to know if theres a Tshark script (or i can create one and some how build a way to see if something isnt right Look at it)</p><p>LIke Low latency issues / Or Its not talking to MME/SGW or issues.</p><p>unless theres cool ways or place i can look online.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filters" rel="tag" title="see questions tagged &#39;capture-filters&#39;">capture-filters</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/176aadd93f435aa0a389cb81549f928f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudoritz&#39;s gravatar image" /><p><span>sudoritz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudoritz has no accepted answers">0%</span></p></div></div><div id="comments-container-36577" class="comments-container"></div><div id="comment-tools-36577" class="comment-tools"></div><div class="clear"></div><div id="comment-36577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36579"></span>

<div id="answer-container-36579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36579-score" class="post-score" title="current number of votes">0</div><span id="post-36579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a pretty open-ended question. Assuming you're coming from the radio side based on the viewpoint of your question:</p><p>For "not talking to MME/SGw issues", if you mean at a UE Context level or bearer level, you can create all sorts of stats out of packet captures (especially with tshark -z options), though usually the eNodeB would have these kinds of success rate info in KPIs also (I can't imagine an eNodeB supplier who wouldn't support that). Stats at the eNodeB level are probably more practical since they're also going to have stats on far more common problems like handover failures, pilot pollution indicators, etc. While packet captures in theory can get most of that, X2AP traces are a challenge to capture across a network due their extremely distributed, multipoint nature across geographic areas whereas S1 interfaces would be terminating in operator COs. If really limited to just captures, S1-MME can serve as a poor man's X2 since you can use path switch indicators to indirectly determine handover rates.</p><p>At a node level, MME connections from the EUTRAN are all carried over SCTP, in always-on stateful sessions or 'associations'. Any MME worth its salt will have some kind of PM or alarming functionality for detecting that type of failure, even if the eNodeB isn't still alive to tell the tale. To the question on-point, again yes in concept scripted tshark reads could look for error indicators (eg:S1AP setup procedure attempts, SCTP-level INIT/Abort/Shutdown chunks).</p><p>At an individual UE level, usually when troubleshooting in the EPS it's very call flow driven. So, if the UE can't register The first thing to do is grab the NAS exchanges to the MME(s) and confirm if it is even requesting an attach. If it is, move on to authentication over S6a, then gateway selection and so on. 99% of the time if it is a problem beyond the EUTRAN you will eventually trace the normal call flow out to a tangible error code between one node or another.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '14, 21:26</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '14, 21:26</strong> </span></p></div></div><div id="comments-container-36579" class="comments-container"></div><div id="comment-tools-36579" class="comment-tools"></div><div class="clear"></div><div id="comment-36579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

