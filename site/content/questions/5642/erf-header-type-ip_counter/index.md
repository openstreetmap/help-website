+++
type = "question"
title = "ERF header type IP_COUNTER"
description = '''Hi All ! In erf.h at the list of ERF headers, there is: #define ERF_TYPE_IP_COUNTER 13  Does anyone know what it is? What is it for? Thanks, Hagay'''
date = "2011-08-10T22:37:00Z"
lastmod = "2012-01-28T11:07:00Z"
weight = 5642
keywords = [ "development" ]
aliases = [ "/questions/5642" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ERF header type IP\_COUNTER](/questions/5642/erf-header-type-ip_counter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5642-score" class="post-score" title="current number of votes">0</div><span id="post-5642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All !</p><p>In erf.h at the list of ERF headers, there is:</p><pre><code>#define ERF_TYPE_IP_COUNTER         13</code></pre><p>Does anyone know what it is? What is it for?</p><p>Thanks,</p><p>Hagay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '11, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/7b112d04b03a7af51932565f4a417d98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Halili&#39;s gravatar image" /><p><span>Halili</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Halili has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Aug '11, 23:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5642" class="comments-container"></div><div id="comment-tools-5642" class="comment-tools"></div><div class="clear"></div><div id="comment-5642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8674"></span>

<div id="answer-container-8674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8674-score" class="post-score" title="current number of votes">1</div><span id="post-8674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, <a href="http://www.endace.com/">Endace</a>, the creator of the ERF file format and thus of the ERF header, does. Unfortunately, they haven't done a very good job of keeping their description of that file format online (it's labeled as "Confidential" in the page footer, the fact that they contribute GPLed code to handle a lot of it nonwithstanding).</p><p>The description in their document isn't entirely clear, but it looks as if an <code>ERF_TYPE_IP_COUNTER</code> record has a list of IPv4 addresses and 32-bit counts of packets seen with that address as a source address and with that address as a destination address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '12, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8674" class="comments-container"></div><div id="comment-tools-8674" class="comment-tools"></div><div class="clear"></div><div id="comment-8674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

