+++
type = "question"
title = "Renumbering Frames based on time stamps"
description = '''Hi, I am capturing Ethernet traffic from two network adapters, in the same time. Due to some inherent lags in accessing each network adapter, some Frames are numbered in a wrong chronological order, while the time stamps are correct. The Frames can be put in the correct chronological order, by click...'''
date = "2016-11-08T00:25:00Z"
lastmod = "2016-11-08T04:41:00Z"
weight = 57121
keywords = [ "frames", "time" ]
aliases = [ "/questions/57121" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Renumbering Frames based on time stamps](/questions/57121/renumbering-frames-based-on-time-stamps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57121-score" class="post-score" title="current number of votes">0</div><span id="post-57121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am capturing Ethernet traffic from two network adapters, in the same time. Due to some inherent lags in accessing each network adapter, some Frames are numbered in a wrong chronological order, while the time stamps are correct. The Frames can be put in the correct chronological order, by clicking on the Time Column, but the interpretation of the Frames by Wireshark is still done over the Frames Numbers. Now for the question: Is there a way of renumbering the Frames based on time stamps?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frames" rel="tag" title="see questions tagged &#39;frames&#39;">frames</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '16, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/3435498fa796d9dd0413b4aed0c3dad8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c_vasiloiu&#39;s gravatar image" /><p><span>c_vasiloiu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c_vasiloiu has no accepted answers">0%</span></p></div></div><div id="comments-container-57121" class="comments-container"></div><div id="comment-tools-57121" class="comment-tools"></div><div class="clear"></div><div id="comment-57121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57127"></span>

<div id="answer-container-57127" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57127-score" class="post-score" title="current number of votes">2</div><span id="post-57127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="c_vasiloiu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to use "reordercap" command-line utility for that: <a href="https://www.wireshark.org/docs/man-pages/reordercap.html">https://www.wireshark.org/docs/man-pages/reordercap.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div></div><div id="comments-container-57127" class="comments-container"><span id="57148"></span><div id="comment-57148" class="comment"><div id="post-57148-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I have tried it and it works OK for my purpose.</p></div><div id="comment-57148-info" class="comment-info"><span class="comment-age">(08 Nov '16, 04:05)</span> <span class="comment-user userinfo">c_vasiloiu</span></div></div><span id="57150"></span><div id="comment-57150" class="comment"><div id="post-57150-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p><p>Also note, your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-57150-info" class="comment-info"><span class="comment-age">(08 Nov '16, 04:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57127" class="comment-tools"></div><div class="clear"></div><div id="comment-57127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

