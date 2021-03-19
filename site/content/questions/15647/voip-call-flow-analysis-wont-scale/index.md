+++
type = "question"
title = "VoIP call flow analysis won&#x27;t scale"
description = '''When looking at graphical flow analysis the vertical dividers are selectable as if they would scale to the width of available text but nothing happens. As a result the text overlaps, gets cut off, and is very difficult to read. Is there any solution for this?'''
date = "2012-11-07T07:37:00Z"
lastmod = "2012-12-14T07:31:00Z"
weight = 15647
keywords = [ "flow", "display", "voip" ]
aliases = [ "/questions/15647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP call flow analysis won't scale](/questions/15647/voip-call-flow-analysis-wont-scale)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15647-score" class="post-score" title="current number of votes">0</div><span id="post-15647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When looking at graphical flow analysis the vertical dividers are selectable as if they would scale to the width of available text but nothing happens. As a result the text overlaps, gets cut off, and is very difficult to read.<br />
Is there any solution for this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/494c8789f937dede544fbd1fe319e075?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomEverett&#39;s gravatar image" /><p><span>TomEverett</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomEverett has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-15647" class="comments-container"></div><div id="comment-tools-15647" class="comment-tools"></div><div class="clear"></div><div id="comment-15647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15651"></span>

<div id="answer-container-15651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15651-score" class="post-score" title="current number of votes">0</div><span id="post-15651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It works in Wireshark 1.8.3 (Win XP). What is your Wireshark version?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '12, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15651" class="comments-container"><span id="16834"></span><div id="comment-16834" class="comment"><div id="post-16834-score" class="comment-score"></div><div class="comment-text"><p>Version 1.8.3 (SVN Rev 45256 from /trunk-1.8) I works sometimes and not others. From what I recall it woks when I diagram many calls, but on a single call I can not open the width to clearly see notations on each step of the call.</p></div><div id="comment-16834-info" class="comment-info"><span class="comment-age">(13 Dec '12, 05:18)</span> <span class="comment-user userinfo">TomEverett</span></div></div><span id="16885"></span><div id="comment-16885" class="comment"><div id="post-16885-score" class="comment-score"></div><div class="comment-text"><p>Hm.., I can't confirm that. It works with single call on my system.</p></div><div id="comment-16885-info" class="comment-info"><span class="comment-age">(14 Dec '12, 07:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15651" class="comment-tools"></div><div class="clear"></div><div id="comment-15651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

