+++
type = "question"
title = "Source and Destination Numbers"
description = '''I sometimes see strange looking numbers in Wireshark. For example: Destination: 2630:1004:b002:1a89:235:ffff:fe01:275 Source: 4007:69c:27f4:: This happens when I block a protocol (like UDP).  What do these numbers mean?'''
date = "2014-04-05T04:20:00Z"
lastmod = "2014-04-05T04:45:00Z"
weight = 31541
keywords = [ "source", "destination" ]
aliases = [ "/questions/31541" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Source and Destination Numbers](/questions/31541/source-and-destination-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31541-score" class="post-score" title="current number of votes">0</div><span id="post-31541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I sometimes see strange looking numbers in Wireshark. For example:</p><p>Destination: 2630:1004:b002:1a89:235:ffff:fe01:275</p><p>Source: 4007:69c:27f4::</p><p>This happens when I block a protocol (like UDP).</p><p>What do these numbers mean?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '14, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/a4a051f9150879cadeb43dcaecedc492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mushroom555&#39;s gravatar image" /><p><span>mushroom555</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mushroom555 has no accepted answers">0%</span></p></div></div><div id="comments-container-31541" class="comments-container"></div><div id="comment-tools-31541" class="comment-tools"></div><div class="clear"></div><div id="comment-31541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31542"></span>

<div id="answer-container-31542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31542-score" class="post-score" title="current number of votes">0</div><span id="post-31542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like IPv6 addresses to me, even though the one starting with 4007 is not exactly a valid prefix at the moment. You might want to take a look at IPv6 since it is now really becoming relevant - slowly but steadily :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31542" class="comments-container"><span id="31544"></span><div id="comment-31544" class="comment"><div id="post-31544-score" class="comment-score"></div><div class="comment-text"><p>I'll be honest with you. I fudged some of the numbers (for privacy reasons, as I do not know what they mean. The actual number is not "4007". I only see these types of numbers when I block a protocol, never when I don't. So you think IPv6?</p></div><div id="comment-31544-info" class="comment-info"><span class="comment-age">(05 Apr '14, 04:31)</span> <span class="comment-user userinfo">mushroom555</span></div></div><span id="31545"></span><div id="comment-31545" class="comment"><div id="post-31545-score" class="comment-score"></div><div class="comment-text"><p>yes, most certainly.</p></div><div id="comment-31545-info" class="comment-info"><span class="comment-age">(05 Apr '14, 04:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-31542" class="comment-tools"></div><div class="clear"></div><div id="comment-31542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

