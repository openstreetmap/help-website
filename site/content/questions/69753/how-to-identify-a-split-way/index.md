+++
type = "question"
title = "how to identify a split way"
description = '''How can I identify if a new way (created tag element) is a result of a split way. What I would like to ultimately to do is flag all ways where nothing changed but only a split occured'''
date = "2019-06-26T13:42:00Z"
lastmod = "2019-06-27T13:06:00Z"
weight = 69753
keywords = [ "split", "way", "history" ]
aliases = [ "/questions/69753" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to identify a split way](/questions/69753/how-to-identify-a-split-way)

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
<span id="post-69753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69753-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I identify if a new way (created tag element) is a result of a split way. What I would like to ultimately to do is flag all ways where nothing changed but only a split occured</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '19, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/821de102b0d4d7379085001df7ee12a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincze&#39;s gravatar image" />
<p><span>Vincze</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincze has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69753" class="comments-container">
&#10;</div>
<div id="comment-tools-69753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69753-form-container" class="comment-form-container">
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

<span id="69754"></span>

<div id="answer-container-69754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69754-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vincze has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not possible to do this "cleanly", but the following logic works in most cases:</p>
<ul>
<li>if the changeset contains one or more new ways (version=1) and one or more modified ways (version &gt; 1),</li>
<li>retrieve previous version of the modified way(s) and check if nodes have been removed from the way;</li>
<li>check if any of new ways contain the nodes that were removed from another way AND old and new way share one node;</li>
<li>if yes, it's a split.</li>
</ul>
<p>Splits into multiple ways (and the reverse, the merging of ways) can be handled similarly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '19, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69754" class="comments-container">
<span id="69765"></span>
<div id="comment-69765" class="comment">
<div id="post-69765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>any chance you got some python code to get me started with this? is there any project that you know of having this thing implemented?</p>
</div>
<div id="comment-69765-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 13:06)</span> <span class="comment-user userinfo">Vincze</span>
</div>
</div>
</div>
<div id="comment-tools-69754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69754-form-container" class="comment-form-container">
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

