+++
type = "question"
title = "Is it possible to change location for data storage for a capture?"
description = '''OS: Windows 7; I have about 100 Mb of free space on disk C. When I launch capture in Wireshark, this space decreases fast (because of temporary data buffering on hard disk). Through several minutes space is exhausted and capture stops. Can I tell Wireshark to store data to other disk (say, disk D wi...'''
date = "2011-11-24T03:46:00Z"
lastmod = "2011-11-24T04:18:00Z"
weight = 7607
keywords = [ "capture", "storage", "data" ]
aliases = [ "/questions/7607" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to change location for data storage for a capture?](/questions/7607/is-it-possible-to-change-location-for-data-storage-for-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7607-score" class="post-score" title="current number of votes">0</div><span id="post-7607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OS: Windows 7;</p><p>I have about 100 Mb of free space on disk C. When I launch capture in Wireshark, this space decreases fast (because of temporary data buffering on hard disk). Through several minutes space is exhausted and capture stops. Can I tell Wireshark to store data to other disk (say, disk D with much free space).</p><p>Thank You!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-storage" rel="tag" title="see questions tagged &#39;storage&#39;">storage</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/8254c5f351b65b722dfcf6cfa648f6ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gistereziz&#39;s gravatar image" /><p><span>Gistereziz</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gistereziz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '11, 10:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7607" class="comments-container"></div><div id="comment-tools-7607" class="comment-tools"></div><div class="clear"></div><div id="comment-7607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7608"></span>

<div id="answer-container-7608" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7608-score" class="post-score" title="current number of votes">2</div><span id="post-7608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark stores the temporary capture files in the system temp directory. If you could change your system settings to use a temp folder on D: you're good to go.</p><p>The other solution - if you can't change your system temp path permanently - is, to start Wireshark from a batch file that sets a "temporary" temp path before calling the wireshark executable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '11, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7608" class="comments-container"></div><div id="comment-tools-7608" class="comment-tools"></div><div class="clear"></div><div id="comment-7608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

