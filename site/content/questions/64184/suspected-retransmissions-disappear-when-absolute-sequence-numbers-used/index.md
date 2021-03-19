+++
type = "question"
title = "Suspected Retransmissions disappear when Absolute Sequence Numbers used."
description = '''Hi all you Sharkies... I had an interesting occurrence yesterday. I opened up a trace file and roughly half of the 500+ packets were marked as Suspected Retransmissions. I looked at a few of them closely, and I could not see any reason for the &quot;suspicion&quot; :-). Then, on a whim, I unchecked &quot;Relative ...'''
date = "2017-10-25T06:27:00Z"
lastmod = "2017-10-25T10:46:00Z"
weight = 64184
keywords = [ "suspected", "retransmission" ]
aliases = [ "/questions/64184" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Suspected Retransmissions disappear when Absolute Sequence Numbers used.](/questions/64184/suspected-retransmissions-disappear-when-absolute-sequence-numbers-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64184-score" class="post-score" title="current number of votes">0</div><span id="post-64184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all you Sharkies...</p><p>I had an interesting occurrence yesterday. I opened up a trace file and roughly half of the 500+ packets were marked as Suspected Retransmissions. I looked at a few of them closely, and I could not see any reason for the "suspicion" :-).</p><p>Then, on a whim, I unchecked "Relative sequence numbers" and all of those Suspected Retransmission warnings went away. And then, being curious, I re-checked "Relative sequence numbers", but the Suspected Retransmissions did NOT reappear, even after closing and re-opening the trace file.</p><p>So, it's a non-issue for me now, but I wondered if anyone else has seen this, and thought maybe I should mention it in this forum.</p><p>I'm using Version 2.2.7 (v2.2.7-0-g1861a96).</p><p>Thx,</p><p>feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-suspected" rel="tag" title="see questions tagged &#39;suspected&#39;">suspected</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '17, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-64184" class="comments-container"></div><div id="comment-tools-64184" class="comment-tools"></div><div class="clear"></div><div id="comment-64184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64195"></span>

<div id="answer-container-64195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64195-score" class="post-score" title="current number of votes">0</div><span id="post-64195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That sounds like a bug. Please file it on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach a trace file that shows this behavior. (You can mark the bug as private if you don't want the trace file to be public.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '17, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-64195" class="comments-container"></div><div id="comment-tools-64195" class="comment-tools"></div><div class="clear"></div><div id="comment-64195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

