+++
type = "question"
title = "Slow Performance and Application Crash"
description = '''I&#x27;m noticing slow performance between a SQL server and a Windows client, with the occasional crash of the application on the client side. I have a capture from the SQL server and from the client side. So far I have noticed some high delta times, but not sure where to look next for the root cause. Th...'''
date = "2014-10-14T04:35:00Z"
lastmod = "2014-10-17T13:29:00Z"
weight = 37035
keywords = [ "application", "slow", "crash", "sql" ]
aliases = [ "/questions/37035" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Performance and Application Crash](/questions/37035/slow-performance-and-application-crash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37035-score" class="post-score" title="current number of votes">0</div><span id="post-37035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm noticing slow performance between a SQL server and a Windows client, with the occasional crash of the application on the client side. I have a capture from the SQL server and from the client side. So far I have noticed some high delta times, but not sure where to look next for the root cause. There is an app server that sits between the SQL server and the client as this is how the application is being used. The high delta times also show up between the app server and the SQL server as well as the app server to the client. Any thoughts on where to look next, other than the event logs?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '14, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/30ffd6f177b036b37b615a93aebceef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studentofsecurity&#39;s gravatar image" /><p><span>studentofsec...</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studentofsecurity has no accepted answers">0%</span></p></div></div><div id="comments-container-37035" class="comments-container"></div><div id="comment-tools-37035" class="comment-tools"></div><div class="clear"></div><div id="comment-37035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37139"></span>

<div id="answer-container-37139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37139-score" class="post-score" title="current number of votes">0</div><span id="post-37139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>The best way to investigate this is to identify an instance of the slow response time in the client trace and then analyze the other trace data tier-by-tier. You can find a complete guide to help you do this at <a href="http://www.tribelabzero.com/resources">http://www.tribelabzero.com/resources</a></p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '14, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37139" class="comments-container"></div><div id="comment-tools-37139" class="comment-tools"></div><div class="clear"></div><div id="comment-37139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

