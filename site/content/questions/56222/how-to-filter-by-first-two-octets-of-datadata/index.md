+++
type = "question"
title = "how to filter by first two octets of data.data"
description = '''Hi, i want to know how to filter by first two octets of data.data Example: I have TCP header with the next data.data: Data: 01:02:06:a1:05:a1:0d:0c:6c... and i want to display only the next data.data: 01:02:[any:any:any...] Thanks,'''
date = "2016-10-07T07:23:00Z"
lastmod = "2016-10-07T08:37:00Z"
weight = 56222
keywords = [ "wireshark" ]
aliases = [ "/questions/56222" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to filter by first two octets of data.data](/questions/56222/how-to-filter-by-first-two-octets-of-datadata)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56222-score" class="post-score" title="current number of votes">0</div><span id="post-56222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i want to know how to filter by first two octets of data.data</p><p>Example:</p><p>I have TCP header with the next data.data: Data: 01:02:06:a1:05:a1:0d:0c:6c...</p><p>and i want to display only the next data.data: 01:02:[any:any:any...]</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '16, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/1ce4fe2b91a61d892d4c9b6a373704eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shlomig&#39;s gravatar image" /><p><span>shlomig</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shlomig has no accepted answers">0%</span></p></div></div><div id="comments-container-56222" class="comments-container"></div><div id="comment-tools-56222" class="comment-tools"></div><div class="clear"></div><div id="comment-56222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56223"></span>

<div id="answer-container-56223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56223-score" class="post-score" title="current number of votes">0</div><span id="post-56223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try <code>data.data[0,1] == 01:02</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '16, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56223" class="comments-container"></div><div id="comment-tools-56223" class="comment-tools"></div><div class="clear"></div><div id="comment-56223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

