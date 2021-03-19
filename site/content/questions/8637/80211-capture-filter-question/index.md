+++
type = "question"
title = "802.11 Capture Filter Question"
description = '''I am using Wireshark with the AirPcapNx adapter to capture 802.11 packets. Is there a Wireshark CAPTURE filter that can be utilized to filter out (NOT capture) particular packet types/subtypes? More specifically, I would like to capture no data frames (type 10) except for null data frames (subtype 0...'''
date = "2012-01-26T14:15:00Z"
lastmod = "2012-01-26T19:18:00Z"
weight = 8637
keywords = [ "capture-filter" ]
aliases = [ "/questions/8637" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 Capture Filter Question](/questions/8637/80211-capture-filter-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8637-score" class="post-score" title="current number of votes">0</div><span id="post-8637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark with the AirPcapNx adapter to capture 802.11 packets. Is there a Wireshark CAPTURE filter that can be utilized to filter out (NOT capture) particular packet types/subtypes? More specifically, I would like to capture no data frames (type 10) except for null data frames (subtype 0100).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p><span>S_P</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-8637" class="comments-container"><span id="8640"></span><div id="comment-8640" class="comment"><div id="post-8640-score" class="comment-score"></div><div class="comment-text"><p>I tried using: "not type data". No 802.11 data packets appear to have been captured. Without running a simultaneous non-filtered capture for comparison, which I am not presently capable of doing, it is difficult to know which packets were filtered out. Does anyone have any experience with this filter expression when used for an 802.11 packet capture?</p></div><div id="comment-8640-info" class="comment-info"><span class="comment-age">(26 Jan '12, 17:01)</span> <span class="comment-user userinfo">S_P</span></div></div></div><div id="comment-tools-8637" class="comment-tools"></div><div class="clear"></div><div id="comment-8637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8643"></span>

<div id="answer-container-8643" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8643-score" class="post-score" title="current number of votes">0</div><span id="post-8643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nevermind. After some searching and experimenting, it looks like "type" and "subtype" will do the trick. For example, "(not type data) or (type data and subtype null)" will filter out all data packets except for the null data packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p><span>S_P</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-8643" class="comments-container"></div><div id="comment-tools-8643" class="comment-tools"></div><div class="clear"></div><div id="comment-8643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

