+++
type = "question"
title = "Can tvb_get_ntoh24 , tvb_get_guint8 take negative offset ?"
description = '''I may sound pretty novice but i just want to avoid any silly mistakes. Do these two functions work properly with negative offset ?   tvb_get_ntoh24 , tvb_get_guint8    Thanks in advance!!'''
date = "2012-08-13T04:13:00Z"
lastmod = "2012-08-13T06:44:00Z"
weight = 13578
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/13578" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can tvb\_get\_ntoh24 , tvb\_get\_guint8 take negative offset ?](/questions/13578/can-tvb_get_ntoh24-tvb_get_guint8-take-negative-offset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13578-score" class="post-score" title="current number of votes">0</div><span id="post-13578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I may sound pretty novice but i just want to avoid any silly mistakes. Do these two functions work properly with negative offset ?</p><blockquote><blockquote><p>tvb_get_ntoh24 , tvb_get_guint8</p></blockquote></blockquote><p>Thanks in advance!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-13578" class="comments-container"></div><div id="comment-tools-13578" class="comment-tools"></div><div class="clear"></div><div id="comment-13578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13581"></span>

<div id="answer-container-13581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13581-score" class="post-score" title="current number of votes">0</div><span id="post-13581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe so, both those functions, and most of the other tvb accessors, take a gint for offset where a negative value indicates bytes from the end of the buffer to start at.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13581" class="comments-container"><span id="13582"></span><div id="comment-13582" class="comment"><div id="post-13582-score" class="comment-score"></div><div class="comment-text"><p>Okay , so if (tvb,0) points to chunk of address from 10 to 20 then (tvb,-1) will point to 19 rather than 9. Am i getting it correct ?</p></div><div id="comment-13582-info" class="comment-info"><span class="comment-age">(13 Aug '12, 04:58)</span> <span class="comment-user userinfo">yogeshg</span></div></div><span id="13587"></span><div id="comment-13587" class="comment"><div id="post-13587-score" class="comment-score"></div><div class="comment-text"><p>Say your tvb has 20 bytes in it, then (tvb, -1) will point to offset 19. You can't "step back" into data before the start of the tvb, that will be held in a different tvb owned by the preceding dissector.</p></div><div id="comment-13587-info" class="comment-info"><span class="comment-age">(13 Aug '12, 06:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-13581" class="comment-tools"></div><div class="clear"></div><div id="comment-13581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

