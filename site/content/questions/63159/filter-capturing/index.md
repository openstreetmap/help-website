+++
type = "question"
title = "Filter Capturing"
description = '''Hello i have some problems with filter capturing. is it possible to capture only one ip address for example, i want to capture ip 10.10.10.1 or www.youtube.com, how can i do with it ?'''
date = "2017-07-26T23:57:00Z"
lastmod = "2017-07-27T00:11:00Z"
weight = 63159
keywords = [ "capture-filter" ]
aliases = [ "/questions/63159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Capturing](/questions/63159/filter-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63159-score" class="post-score" title="current number of votes">0</div><span id="post-63159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i have some problems with filter capturing. is it possible to capture only one ip address for example, i want to capture ip 10.10.10.1 or www.youtube.com, how can i do with it ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '17, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/4f4ad0afe443c29cea2e036509acb2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Samann&#39;s gravatar image" /><p><span>Samann</span><br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Samann has no accepted answers">0%</span></p></div></div><div id="comments-container-63159" class="comments-container"></div><div id="comment-tools-63159" class="comment-tools"></div><div class="clear"></div><div id="comment-63159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63160"></span>

<div id="answer-container-63160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63160-score" class="post-score" title="current number of votes">0</div><span id="post-63160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filter syntax differs from display filter syntax, so to capture only 10.10.10.1, you need to use <code>host 10.10.10.1</code>.</p><p>However, there is no capture syntax for fqdn (like www.youtube.com) for many reasons:</p><ul><li><p>translation of fqdn to IP address is done using DNS, and there is no feedback from the dissection of the DNS response to the capture filter, leaving aside that the DNS responses are locally cached</p></li><li><p>a single fqdn may translate to several IP addresses (for load sharing and reliability purposes)</p></li><li><p>several fqdns may be hosted on a single IP address so you cannot determine which flow belongs to which fqdn by just the IP address.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63160" class="comments-container"></div><div id="comment-tools-63160" class="comment-tools"></div><div class="clear"></div><div id="comment-63160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

