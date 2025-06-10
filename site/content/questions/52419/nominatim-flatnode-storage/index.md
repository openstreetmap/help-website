+++
type = "question"
title = "Nominatim flatnode storage"
description = '''Hello, I have installed Nominatim on CentOS and imported a small set of data for test, everything works nicely. I have enabled flatnode storage of node locations. After my test I deleted the Nominatim db (sudo -u postgres dropdb nominatim) but I didn&#x27;t delete the flatnode file. Yesterday I started t...'''
date = "2016-10-09T11:37:00Z"
lastmod = "2016-10-09T16:39:00Z"
weight = 52419
keywords = [ "nominatim", "flatnode" ]
aliases = [ "/questions/52419" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim flatnode storage](/questions/52419/nominatim-flatnode-storage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52419-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have installed Nominatim on CentOS and imported a small set of data for test, everything works nicely. I have enabled flatnode storage of node locations. After my test I deleted the Nominatim db (sudo -u postgres dropdb nominatim) but I didn't delete the flatnode file. Yesterday I started to import a large set of data (Europe) and obviously the operation is still running. Please, I would like to know if I had to delete the flatnode file before to start the new big import. In the odd case I have to repeat my import, please, which are the steps to clean everything and free space on disk.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-flatnode" rel="tag" title="see questions tagged &#39;flatnode&#39;">flatnode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '16, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b30d5cc7555044db0eac4e20798ae212?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sramp&#39;s gravatar image" />
<p><span>sramp</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sramp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52419" class="comments-container">
&#10;</div>
<div id="comment-tools-52419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52419-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52426"></span>

<div id="answer-container-52426" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52426-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-52426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sramp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not necessary to delete the flatnode storage; it will simply be overwritten with your newly imported data. From my experience, the flatnode storage will approximately be even with normal database storage in the Europe case; it will save space if you import more than Europe, and waste space if you import less. But it will usually be a little faster than the database storage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '16, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52426" class="comments-container">
&#10;</div>
<div id="comment-tools-52426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52426-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

