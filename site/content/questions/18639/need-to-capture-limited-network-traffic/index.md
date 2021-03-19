+++
type = "question"
title = "Need to capture limited network traffic"
description = '''I am trying to monitor traffic on a specific subnet. How can I only monitor/save packets from that subnet and only record packets headed to a specific destination IP or IPs. Thanks Michael Smith'''
date = "2013-02-14T13:02:00Z"
lastmod = "2013-02-14T13:11:00Z"
weight = 18639
keywords = [ "subnet" ]
aliases = [ "/questions/18639" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to capture limited network traffic](/questions/18639/need-to-capture-limited-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18639-score" class="post-score" title="current number of votes">0</div><span id="post-18639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to monitor traffic on a specific subnet. How can I only monitor/save packets from that subnet and only record packets headed to a specific destination IP or IPs.</p><p>Thanks</p><p>Michael Smith</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-subnet" rel="tag" title="see questions tagged &#39;subnet&#39;">subnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/3c6ce8f2170bd81b936942b726fb7cca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="enochgenesis&#39;s gravatar image" /><p><span>enochgenesis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="enochgenesis has no accepted answers">0%</span></p></div></div><div id="comments-container-18639" class="comments-container"></div><div id="comment-tools-18639" class="comment-tools"></div><div class="clear"></div><div id="comment-18639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18640"></span>

<div id="answer-container-18640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18640-score" class="post-score" title="current number of votes">0</div><span id="post-18640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a> page on the wiki.</p><p>For a subnet use something like <code>net 192.168.0.0/24</code>.</p><p>For specific hosts use something like <code>host 192.168.0.1</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18640" class="comments-container"></div><div id="comment-tools-18640" class="comment-tools"></div><div class="clear"></div><div id="comment-18640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

