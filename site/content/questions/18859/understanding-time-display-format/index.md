+++
type = "question"
title = "Understanding Time display format"
description = '''Can anyone please explain me what a wireshark user can achieve setting these parameters separately? Seconds since beginning of the capture Seconds since previous captured packet Seconds since previous displayed packet The first option is straight forward but i would like to know the difference betwe...'''
date = "2013-02-25T12:21:00Z"
lastmod = "2013-02-25T22:01:00Z"
weight = 18859
keywords = [ "timedisplayformat" ]
aliases = [ "/questions/18859" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding Time display format](/questions/18859/understanding-time-display-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18859-score" class="post-score" title="current number of votes">0</div><span id="post-18859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone please explain me what a wireshark user can achieve setting these parameters separately? Seconds since beginning of the capture Seconds since previous captured packet Seconds since previous displayed packet</p><p>The first option is straight forward but i would like to know the difference between displayed packet vs captured packet.</p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timedisplayformat" rel="tag" title="see questions tagged &#39;timedisplayformat&#39;">timedisplayformat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '13, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-18859" class="comments-container"></div><div id="comment-tools-18859" class="comment-tools"></div><div class="clear"></div><div id="comment-18859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18862"></span>

<div id="answer-container-18862" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18862-score" class="post-score" title="current number of votes">2</div><span id="post-18862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using the display filters you can (temporarily) remove frames from display. The 'Seconds since previous displayed packet' setting makes it so that the times presented on the displayed frames are the times between those displayed frames, not taking into account the frames removed from display.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '13, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18862" class="comments-container"><span id="18864"></span><div id="comment-18864" class="comment"><div id="post-18864-score" class="comment-score"></div><div class="comment-text"><p>Assume that i didn't sorted out any packets(not applied any display filter) in that case will seconds since previous displayed packet is equal to seconds since previous captured packet?</p></div><div id="comment-18864-info" class="comment-info"><span class="comment-age">(25 Feb '13, 14:21)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="18865"></span><div id="comment-18865" class="comment"><div id="post-18865-score" class="comment-score"></div><div class="comment-text"><p>If there's no display filter, captured packets and displayed packets are the same, so, yes, seconds since previous displayed packet will be equal to seconds since previous captured packet.</p></div><div id="comment-18865-info" class="comment-info"><span class="comment-age">(25 Feb '13, 14:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18866"></span><div id="comment-18866" class="comment"><div id="post-18866-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy and Jaap.</p></div><div id="comment-18866-info" class="comment-info"><span class="comment-age">(25 Feb '13, 15:10)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="18875"></span><div id="comment-18875" class="comment"><div id="post-18875-score" class="comment-score"></div><div class="comment-text"><p><span>@kserasera</span>: If you like the answer and accept it, please click the tick besides the answer, so it's marked that way.</p></div><div id="comment-18875-info" class="comment-info"><span class="comment-age">(25 Feb '13, 22:01)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-18862" class="comment-tools"></div><div class="clear"></div><div id="comment-18862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

