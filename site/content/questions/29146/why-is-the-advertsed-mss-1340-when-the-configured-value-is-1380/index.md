+++
type = "question"
title = "Why is the advertsed MSS 1340 when the configured value is 1380?"
description = '''During the course of a prolonged mail server performance issue we determined that we needed to make sure the mail server was sending smaller packets to get the best performance. We manually reduced the MSS setting on the server to 1380 but I am seeing in the 3 way handshake that the server is advert...'''
date = "2014-01-24T15:10:00Z"
lastmod = "2014-01-24T15:30:00Z"
weight = 29146
keywords = [ "mss" ]
aliases = [ "/questions/29146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the advertsed MSS 1340 when the configured value is 1380?](/questions/29146/why-is-the-advertsed-mss-1340-when-the-configured-value-is-1380)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29146-score" class="post-score" title="current number of votes">0</div><span id="post-29146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During the course of a prolonged mail server performance issue we determined that we needed to make sure the mail server was sending smaller packets to get the best performance. We manually reduced the MSS setting on the server to 1380 but I am seeing in the 3 way handshake that the server is advertising MSS = 1340.</p><p>Thanks, Steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '14, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/9f6a6dca6af7b0f8a0161945a70eb891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skrall1965&#39;s gravatar image" /><p><span>skrall1965</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skrall1965 has no accepted answers">0%</span></p></div></div><div id="comments-container-29146" class="comments-container"></div><div id="comment-tools-29146" class="comment-tools"></div><div class="clear"></div><div id="comment-29146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29147"></span>

<div id="answer-container-29147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29147-score" class="post-score" title="current number of votes">3</div><span id="post-29147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you actually configure the MSS on the server, or was it the MTU? The difference between the two values you listed is 40 bytes, and that's usually the difference between MTU and MSS. The MSS is usually the MTU minus 20 bytes for the IP headers and 20 bytes for the TCP headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '14, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-29147" class="comments-container"></div><div id="comment-tools-29147" class="comment-tools"></div><div class="clear"></div><div id="comment-29147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

