+++
type = "question"
title = "create display filter based on frame.time_delta_displayed field"
description = '''hi, I am trying to create a display filter which will select all packets that have a specific time delta to the previously displayed packet. I have tried for example frame.time_delta_displayed &amp;gt; 0.1 or  frame.time_delta_displayed==0.00472000 which is a value I can see in one of the packets in the...'''
date = "2017-05-05T23:14:00Z"
lastmod = "2017-05-09T05:24:00Z"
weight = 61263
keywords = [ "display", "display-filter" ]
aliases = [ "/questions/61263" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [create display filter based on frame.time\_delta\_displayed field](/questions/61263/create-display-filter-based-on-frametime_delta_displayed-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61263-score" class="post-score" title="current number of votes">0</div><span id="post-61263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I am trying to create a display filter which will select all packets that have a specific time delta to the previously displayed packet. I have tried for example frame.time_delta_displayed &gt; 0.1 or frame.time_delta_displayed==0.00472000 which is a value I can see in one of the packets in the capture, yet it still does not select anything. What am I missing?</p><p>Any help appreciated.</p><p>Jeannette</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '17, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/9846e79cded4643917c83c2d2ff1d993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeannette54365&#39;s gravatar image" /><p><span>Jeannette54365</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeannette54365 has no accepted answers">0%</span></p></div></div><div id="comments-container-61263" class="comments-container"></div><div id="comment-tools-61263" class="comment-tools"></div><div class="clear"></div><div id="comment-61263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61264"></span>

<div id="answer-container-61264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61264-score" class="post-score" title="current number of votes">1</div><span id="post-61264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a close look at frame 1. There the time_delta_displayed is 0, so doesn't match, so isn't displayed. Now frame 2. Since frame 1 isn't displayed, the time_delta_displayed is 0, so isn't displayed. Now frame 3, ... ad infinitum.</p><p>So you have to get things started by at least displaying the first frame, e.g. prefix the filter by "<code>frame.number==1 ||</code>"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '17, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61264" class="comments-container"><span id="61304"></span><div id="comment-61304" class="comment"><div id="post-61304-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap, that looks a bit better, still not a 100% there, but haven't got time right not to progress further.</p><p>Wasn't able to vote, I don't have enough points apparently.</p></div><div id="comment-61304-info" class="comment-info"><span class="comment-age">(09 May '17, 05:21)</span> <span class="comment-user userinfo">Jeannette54365</span></div></div><span id="61305"></span><div id="comment-61305" class="comment"><div id="post-61305-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61305-info" class="comment-info"><span class="comment-age">(09 May '17, 05:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61264" class="comment-tools"></div><div class="clear"></div><div id="comment-61264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

