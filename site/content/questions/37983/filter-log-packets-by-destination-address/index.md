+++
type = "question"
title = "Filter log packets by destination address"
description = '''I&#x27;m generating a log from wireshark but I&#x27;m only interested about incoming packets of a node. As far a s I know, the only way to do it is to look at the IPv6 address in the destination field of 802.15.4, which is what I am capturing.  Is there a way to filter based on 802.15.4 destination address?'''
date = "2014-11-19T15:55:00Z"
lastmod = "2014-11-20T01:51:00Z"
weight = 37983
keywords = [ "802.15.4", "capture-filter", "address" ]
aliases = [ "/questions/37983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter log packets by destination address](/questions/37983/filter-log-packets-by-destination-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37983-score" class="post-score" title="current number of votes">0</div><span id="post-37983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm generating a log from wireshark but I'm only interested about incoming packets of a node. As far a s I know, the only way to do it is to look at the IPv6 address in the destination field of 802.15.4, which is what I am capturing.<br />
</p><p>Is there a way to filter based on 802.15.4 destination address?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.15.4" rel="tag" title="see questions tagged &#39;802.15.4&#39;">802.15.4</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/1e5ba80037e29a8e5a58235b24f2447f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob3280&#39;s gravatar image" /><p><span>Bob3280</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob3280 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37983" class="comments-container"></div><div id="comment-tools-37983" class="comment-tools"></div><div class="clear"></div><div id="comment-37983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38002"></span>

<div id="answer-container-38002" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38002-score" class="post-score" title="current number of votes">0</div><span id="post-38002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't have a 802.15.4 capture file, that contains IPv6 addresses. However, if Wireshark is able to decode and view that address, just go to that field, right click it and select "Apply as Column". You will then see the filter syntax in the Filter field. Take that as an example to build your own filter.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38002" class="comments-container"></div><div id="comment-tools-38002" class="comment-tools"></div><div class="clear"></div><div id="comment-38002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

