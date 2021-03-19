+++
type = "question"
title = "search for a pattern of consecutive packets"
description = '''Hi, I&#x27;m trying to find a pattern of multiple consecutive RTS packets. mainly ~10 or more without CTS following them. is there a way to find such a pattern? Thanks!'''
date = "2016-02-01T05:17:00Z"
lastmod = "2016-02-01T18:34:00Z"
weight = 49682
keywords = [ "consecutive", "display-filter", "pattern" ]
aliases = [ "/questions/49682" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [search for a pattern of consecutive packets](/questions/49682/search-for-a-pattern-of-consecutive-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49682-score" class="post-score" title="current number of votes">0</div><span id="post-49682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to find a pattern of multiple consecutive RTS packets. mainly ~10 or more without CTS following them. is there a way to find such a pattern?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-consecutive" rel="tag" title="see questions tagged &#39;consecutive&#39;">consecutive</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-pattern" rel="tag" title="see questions tagged &#39;pattern&#39;">pattern</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '16, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/d99042505f18527a1706c9f9d52122a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HananB&#39;s gravatar image" /><p><span>HananB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HananB has no accepted answers">0%</span></p></div></div><div id="comments-container-49682" class="comments-container"></div><div id="comment-tools-49682" class="comment-tools"></div><div class="clear"></div><div id="comment-49682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49684"></span>

<div id="answer-container-49684" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49684-score" class="post-score" title="current number of votes">0</div><span id="post-49684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="HananB has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Packet dependency filtering isn't possible. The only exception is when Wireshark does the relationship calculation for you and adds meta info to the packets. E.g. if the RTS packets have a field telling you where the related CTS packet is, you could filter on that. That way you'd find all that have a CTS, and then negate the filter to get the opposite.</p><p>See also <a href="https://blog.packet-foo.com/2015/03/advanced-display-filtering/">https://blog.packet-foo.com/2015/03/advanced-display-filtering/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-49684" class="comments-container"><span id="49685"></span><div id="comment-49685" class="comment"><div id="post-49685-score" class="comment-score"></div><div class="comment-text"><p>what a drag... Thanks for the answer though</p></div><div id="comment-49685-info" class="comment-info"><span class="comment-age">(01 Feb '16, 05:52)</span> <span class="comment-user userinfo">HananB</span></div></div><span id="49705"></span><div id="comment-49705" class="comment"><div id="post-49705-score" class="comment-score"></div><div class="comment-text"><p>It might be a nice feature - and might be implementable using <a href="https://wiki.wireshark.org/Mate">MATE</a> - but it's more complicated than doing "memory-free" filtering.</p></div><div id="comment-49705-info" class="comment-info"><span class="comment-age">(01 Feb '16, 18:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-49684" class="comment-tools"></div><div class="clear"></div><div id="comment-49684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

