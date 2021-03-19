+++
type = "question"
title = "TCp Window scaling"
description = '''Hi All,  I am capturing a network traces for one of my problem debugging.I see that Window size is shown as &quot;70145(scaled)&quot; as soon as I start my application.but after some time it shows me the value of only &quot;1525&quot;. can anyone please help me understand why it is falling to that value.Also why it is ...'''
date = "2011-08-16T00:29:00Z"
lastmod = "2011-08-16T11:33:00Z"
weight = 5708
keywords = [ "tcp" ]
aliases = [ "/questions/5708" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCp Window scaling](/questions/5708/tcp-window-scaling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5708-score" class="post-score" title="current number of votes">0</div><span id="post-5708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am capturing a network traces for one of my problem debugging.I see that Window size is shown as "70145(scaled)" as soon as I start my application.but after some time it shows me the value of only "1525". can anyone please help me understand why it is falling to that value.Also why it is not showing "scaled" in after few minutes of restarting the window. Window scaling is on in my machine with value set as 1.</p><p>Thanks, Parveen Jain</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '11, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/6a3ac50a1168828469c74e3f626c038e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjain&#39;s gravatar image" /><p><span>pjain</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjain has no accepted answers">0%</span></p></div></div><div id="comments-container-5708" class="comments-container"></div><div id="comment-tools-5708" class="comment-tools"></div><div class="clear"></div><div id="comment-5708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5715"></span>

<div id="answer-container-5715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5715-score" class="post-score" title="current number of votes">0</div><span id="post-5715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Parveen, I seems that you may be capturing multiple TCP sessions, but have only seen the initialization of one of them. If you capture the three-way handshake then WireShark will be aware of the endpoints' use of Window Scaling and will calculate the actual window size, and add "(scaled)" to the it. If you don't capture the three-way handshake then WireShark will just read the bits in the Options field. If you looked at the individual packet that has "70145(scaled)" as the window size, and looked at the actual bits you'd see that it probably lists something similar to the other packets (ie: 1525).</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '11, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-5715" class="comments-container"></div><div id="comment-tools-5715" class="comment-tools"></div><div class="clear"></div><div id="comment-5715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

