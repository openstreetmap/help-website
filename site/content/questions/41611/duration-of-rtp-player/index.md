+++
type = "question"
title = "Duration of RTP Player"
description = '''How does wireshark calculate &quot;Duration&quot; of RTP Player? Does duration means delay time from SIP endpoint to endpoint?'''
date = "2015-04-20T22:39:00Z"
lastmod = "2015-04-22T23:05:00Z"
weight = 41611
keywords = [ "duration", "delay", "jitter", "calculate", "rtp" ]
aliases = [ "/questions/41611" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Duration of RTP Player](/questions/41611/duration-of-rtp-player)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41611-score" class="post-score" title="current number of votes">0</div><span id="post-41611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does wireshark calculate "Duration" of RTP Player? Does duration means delay time from SIP endpoint to endpoint?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span> <span class="post-tag tag-link-calculate" rel="tag" title="see questions tagged &#39;calculate&#39;">calculate</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '15, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/fce8b52d0ce4b8e3ac1151353f022a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="med&#39;s gravatar image" /><p><span>med</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="med has no accepted answers">0%</span></p></div></div><div id="comments-container-41611" class="comments-container"></div><div id="comment-tools-41611" class="comment-tools"></div><div class="clear"></div><div id="comment-41611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41613"></span>

<div id="answer-container-41613" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41613-score" class="post-score" title="current number of votes">1</div><span id="post-41613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="med has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The contents of the RTP stream is a certain amount of speech samples, which, depending on the sample clock, represents a certain duration of speech. The codec used for the encoding of the speech defines the sample clock (in case of G.711 an 8 kHz clock), so you can easily calculate the duration through the sizes of the packets and the sample clock.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '15, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41613" class="comments-container"><span id="41713"></span><div id="comment-41713" class="comment"><div id="post-41713-score" class="comment-score"></div><div class="comment-text"><p>I was able to understand, Thanks for your explanation. I took duration to mean "delay time".</p></div><div id="comment-41713-info" class="comment-info"><span class="comment-age">(22 Apr '15, 20:53)</span> <span class="comment-user userinfo">med</span></div></div><span id="41714"></span><div id="comment-41714" class="comment"><div id="post-41714-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41714-info" class="comment-info"><span class="comment-age">(22 Apr '15, 23:05)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-41613" class="comment-tools"></div><div class="clear"></div><div id="comment-41613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

