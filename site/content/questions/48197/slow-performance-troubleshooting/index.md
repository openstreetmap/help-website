+++
type = "question"
title = "Slow performance troubleshooting"
description = '''I&#x27;m wondering can somebody give me some pointers on troubleshooting steps when deal with an enterprise network that we can only span the traffic off a switch to a pc which has wireshark installed on it to troubleshoot a slow network that the clients are stating everything is slow? I have access to t...'''
date = "2015-12-02T06:49:00Z"
lastmod = "2015-12-02T07:25:00Z"
weight = 48197
keywords = [ "performance", "slow" ]
aliases = [ "/questions/48197" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow performance troubleshooting](/questions/48197/slow-performance-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48197-score" class="post-score" title="current number of votes">0</div><span id="post-48197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering can somebody give me some pointers on troubleshooting steps when deal with an enterprise network that we can only span the traffic off a switch to a pc which has wireshark installed on it to troubleshoot a slow network that the clients are stating everything is slow? I have access to the router and switches on the network and not seeing any physical problems. These are 4megs, 8megs,10megs and 1gigs links. I tell the customer to call me when they have a problem but they never do. I know this is a broad question but the trace files are long so trying to get a game plan together. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/1ace388d473a7dc2c6ffb774562b02ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrickwill&#39;s gravatar image" /><p><span>patrickwill</span><br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrickwill has no accepted answers">0%</span></p></div></div><div id="comments-container-48197" class="comments-container"></div><div id="comment-tools-48197" class="comment-tools"></div><div class="clear"></div><div id="comment-48197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48201"></span>

<div id="answer-container-48201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48201-score" class="post-score" title="current number of votes">0</div><span id="post-48201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd recommend to start from the people, not from the machines, by asking first the end users to show me what they deem "slow" and what they deem "fast", as this would also identify to you the particular service you should concentrate at when analysing the trace. Doing the analysis for that service may lead to identification of an issue in the network itself, meaning that "everything" would be fixed by fixing the network problem found, as well as to identification of the root cause of the slowness outside the network and as related to that service alone, meaning that "everything" in fact meant "the service I use most often".</p><p>Because the slowness may come from insufficient performance of the workstations as well as from overbooked 4 meg links (depending on the volume of data which the client's applications exchange with central servers) as well as overload of the servers to which the workstations connect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48201" class="comments-container"></div><div id="comment-tools-48201" class="comment-tools"></div><div class="clear"></div><div id="comment-48201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

