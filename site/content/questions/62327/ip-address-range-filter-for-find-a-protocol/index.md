+++
type = "question"
title = "ip address range filter for find a protocol"
description = '''I am looking for bittorrent application is used in my network, i want to find out the particular node how can i capture packet from network my network range start from 192.168.9.0/24 to 192.168.43.0/24 Please help?'''
date = "2017-06-27T04:26:00Z"
lastmod = "2017-06-27T10:03:00Z"
weight = 62327
keywords = [ "range", "capture-filter" ]
aliases = [ "/questions/62327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ip address range filter for find a protocol](/questions/62327/ip-address-range-filter-for-find-a-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62327-score" class="post-score" title="current number of votes">0</div><span id="post-62327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for bittorrent application is used in my network, i want to find out the particular node how can i capture packet from network my network range start from 192.168.9.0/24 to 192.168.43.0/24 Please help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-range" rel="tag" title="see questions tagged &#39;range&#39;">range</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '17, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/1ea772534331f9e7a6dff72900cc7e61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ranveersingh&#39;s gravatar image" /><p><span>ranveersingh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ranveersingh has no accepted answers">0%</span></p></div></div><div id="comments-container-62327" class="comments-container"></div><div id="comment-tools-62327" class="comment-tools"></div><div class="clear"></div><div id="comment-62327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62341"></span>

<div id="answer-container-62341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62341-score" class="post-score" title="current number of votes">1</div><span id="post-62341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>net 192.168.0.0/18 and not (net 192.168.0.0/21 or 192.168.8.0/24 or 192.168.44.0/22 or 192.168.48.0/20)</code>, but better check. For <strong>capture</strong> filters, there is no simpler way than to compose ranges from prefixes. Sometimes (like in this case), excluding longer (more narrow) prefixes from shorter (wider) one causes less typing than doing it the other way round.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62341" class="comments-container"></div><div id="comment-tools-62341" class="comment-tools"></div><div class="clear"></div><div id="comment-62341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

