+++
type = "question"
title = "TCP segment of a reassembled PDU ?"
description = '''What does it mean?  TCP segment of a reassembled PDU'''
date = "2016-12-17T07:37:00Z"
lastmod = "2016-12-17T13:53:00Z"
weight = 58186
keywords = [ "pdu", "tcp" ]
aliases = [ "/questions/58186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP segment of a reassembled PDU ?](/questions/58186/tcp-segment-of-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58186-score" class="post-score" title="current number of votes">0</div><span id="post-58186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does it mean?</p><p>TCP segment of a reassembled PDU</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '16, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/b44dffcbc9d550d562a112e2b83e786c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luna&#39;s gravatar image" /><p><span>luna</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luna has no accepted answers">0%</span></p></div></div><div id="comments-container-58186" class="comments-container"></div><div id="comment-tools-58186" class="comment-tools"></div><div class="clear"></div><div id="comment-58186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58197"></span>

<div id="answer-container-58197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58197-score" class="post-score" title="current number of votes">2</div><span id="post-58197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means that</p><ul><li>Wireshark/TShark thinks it knows what protocol is running atop TCP in that TCP segment;</li><li>that TCP segment doesn't contain all of a "protocol data unit" (PDU) for that higher-level protocol, i.e. a packet or protocol message for that higher-level protocol, and doesn't contain the last part of that PDU, so it's trying to reassemble the multiple TCP segments containing that higher-level PDU.</li></ul><p>For example, an HTTP response with a lot of data in it won't fit in a single TCP segment on most networks, so it'll be split over multiple TCP segments; all but the last TCP segment will be marked as "TCP segment of a reassembled PDU".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '16, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58197" class="comments-container"></div><div id="comment-tools-58197" class="comment-tools"></div><div class="clear"></div><div id="comment-58197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

