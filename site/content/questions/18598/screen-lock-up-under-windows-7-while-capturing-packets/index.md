+++
type = "question"
title = "Screen lock up under Windows 7 while capturing packets"
description = '''I am running Wireshark ver 1.8.0rc2 (SVN Rev 43337 from /trunk-1.8) under Windows 7 SP 1. While capturing GOOSE packets, if I try to move the window, the screen locks up. I have to pop up the task manager to either kill it (sometimes it frees up and becomes responsive again).'''
date = "2013-02-13T09:10:00Z"
lastmod = "2013-02-13T15:06:00Z"
weight = 18598
keywords = [ "lock", "screen", "up", "capturing", "while" ]
aliases = [ "/questions/18598" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Screen lock up under Windows 7 while capturing packets](/questions/18598/screen-lock-up-under-windows-7-while-capturing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18598-score" class="post-score" title="current number of votes">0</div><span id="post-18598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark ver 1.8.0rc2 (SVN Rev 43337 from /trunk-1.8) under Windows 7 SP 1. While capturing GOOSE packets, if I try to move the window, the screen locks up. I have to pop up the task manager to either kill it (sometimes it frees up and becomes responsive again).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lock" rel="tag" title="see questions tagged &#39;lock&#39;">lock</span> <span class="post-tag tag-link-screen" rel="tag" title="see questions tagged &#39;screen&#39;">screen</span> <span class="post-tag tag-link-up" rel="tag" title="see questions tagged &#39;up&#39;">up</span> <span class="post-tag tag-link-capturing" rel="tag" title="see questions tagged &#39;capturing&#39;">capturing</span> <span class="post-tag tag-link-while" rel="tag" title="see questions tagged &#39;while&#39;">while</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/4025240b8c0475c260d9cb7529e827c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecs1749&#39;s gravatar image" /><p><span>ecs1749</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecs1749 has no accepted answers">0%</span></p></div></div><div id="comments-container-18598" class="comments-container"></div><div id="comment-tools-18598" class="comment-tools"></div><div class="clear"></div><div id="comment-18598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18608"></span>

<div id="answer-container-18608" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18608-score" class="post-score" title="current number of votes">0</div><span id="post-18608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ecs1749 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try running the <em>current</em> 1.8 version, 1.8.5, instead. The "Development release" shouldn't even be offered - it was Release Candidate 2 for 1.8.0, but it was obsolete when 1.8.0 was released, and we're now up to 1.8.5.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18608" class="comments-container"><span id="18614"></span><div id="comment-18614" class="comment"><div id="post-18614-score" class="comment-score"></div><div class="comment-text"><p>Thanks. That did solve the problem.</p></div><div id="comment-18614-info" class="comment-info"><span class="comment-age">(13 Feb '13, 15:06)</span> <span class="comment-user userinfo">ecs1749</span></div></div></div><div id="comment-tools-18608" class="comment-tools"></div><div class="clear"></div><div id="comment-18608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

