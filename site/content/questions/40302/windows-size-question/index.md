+++
type = "question"
title = "Windows size question"
description = '''I am new to Wireshark but trying to learn : ) I created a column to display Windows size but after some time I noticed the Windows size being reported was very low e.g 258. After looking through the byte details I can see there is also an [estimated windows size] which is far greater. Is this estima...'''
date = "2015-03-05T13:47:00Z"
lastmod = "2015-03-05T14:56:00Z"
weight = 40302
keywords = [ "windows", "tcpwindowsize" ]
aliases = [ "/questions/40302" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Windows size question](/questions/40302/windows-size-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40302-score" class="post-score" title="current number of votes">0</div><span id="post-40302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark but trying to learn : ) I created a column to display Windows size but after some time I noticed the Windows size being reported was very low e.g 258. After looking through the byte details I can see there is also an [estimated windows size] which is far greater. Is this estimated Windows size Wireshark taking the 258 and multiplying it by what ever Windows scaling is employed or is it something else? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/68ce515bc08f1da09ed2200c8aca252c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Costello&#39;s gravatar image" /><p><span>Costello</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Costello has no accepted answers">0%</span></p></div></div><div id="comments-container-40302" class="comments-container"></div><div id="comment-tools-40302" class="comment-tools"></div><div class="clear"></div><div id="comment-40302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40304"></span>

<div id="answer-container-40304" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40304-score" class="post-score" title="current number of votes">1</div><span id="post-40304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Costello has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, correct, you're seeing the 16 bit window value of 258, but it gets multiplied by the scale factor. It's better to look at the calculated window size, because that's the "real" window size. Keep in mind that this only works if the conversation was captured including the three way handshake, because that's where the scale factor is set - if you miss the handshake, you (and Wireshark) don't know the multiplier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40304" class="comments-container"><span id="40307"></span><div id="comment-40307" class="comment"><div id="post-40307-score" class="comment-score"></div><div class="comment-text"><p>Great, thank you very much</p></div><div id="comment-40307-info" class="comment-info"><span class="comment-age">(05 Mar '15, 14:56)</span> <span class="comment-user userinfo">Costello</span></div></div></div><div id="comment-tools-40304" class="comment-tools"></div><div class="clear"></div><div id="comment-40304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

