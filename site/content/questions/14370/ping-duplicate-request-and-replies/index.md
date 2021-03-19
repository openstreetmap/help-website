+++
type = "question"
title = "ping duplicate request and replies ?"
description = '''Hello, I am sending a PING between one two computers. I am finding that Wireshark is detecting duplicate frames of each ping request and reply. I notice each of the duplicates has a different source value e.g. one is: Source: Cisco4f:b1:05 (00:21:a0:4f:b1:05) the other is: Source: DigitalD99:0a:3d (...'''
date = "2012-09-19T01:18:00Z"
lastmod = "2012-09-19T01:24:00Z"
weight = 14370
keywords = [ "duplicate", "ping" ]
aliases = [ "/questions/14370" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ping duplicate request and replies ?](/questions/14370/ping-duplicate-request-and-replies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14370-score" class="post-score" title="current number of votes">0</div><span id="post-14370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am sending a PING between one two computers. I am finding that Wireshark is detecting duplicate frames of each ping request and reply. I notice each of the duplicates has a different source value e.g. one is: Source: Cisco4f:b1:05 (00:21:a0:4f:b1:05) the other is: Source: DigitalD99:0a:3d (00:11:6b:99:0a:3d)</p><p>Is this because of multiple interfaces on my routers, or is it some other reason ? Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/e381bb527a7ce22531c6e55d4f72e048?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fran1942&#39;s gravatar image" /><p><span>fran1942</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fran1942 has no accepted answers">0%</span></p></div></div><div id="comments-container-14370" class="comments-container"></div><div id="comment-tools-14370" class="comment-tools"></div><div class="clear"></div><div id="comment-14370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14372"></span>

<div id="answer-container-14372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14372-score" class="post-score" title="current number of votes">0</div><span id="post-14372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're seeing the same packet twice: before and after it has been routed. You can tell by looking at the TTL value in the IP header - it should be one lower in the duplicate than in the original. You can use the TTL to filter on only the origial packets if you want to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '12, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14372" class="comments-container"></div><div id="comment-tools-14372" class="comment-tools"></div><div class="clear"></div><div id="comment-14372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

