+++
type = "question"
title = "osmfilter - is it possible to filter out &quot;highway=footway&quot; but keep ones with &quot;bicycle=yes&quot;?"
description = '''I want to keep all other objects unchanged.'''
date = "2013-09-22T17:12:00Z"
lastmod = "2013-09-25T22:07:00Z"
weight = 26622
keywords = [ "osmfilter" ]
aliases = [ "/questions/26622" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmfilter - is it possible to filter out "highway=footway" but keep ones with "bicycle=yes"?](/questions/26622/osmfilter-is-it-possible-to-filter-out-highwayfootway-but-keep-ones-with-bicycleyes)

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
<span id="post-26622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to keep all other objects unchanged.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '13, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-26622" class="comments-container">
<span id="26637"></span>
<div id="comment-26637" class="comment">
<div id="post-26637-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You haven't explained your purpose but if you want to extract/keep only cycleways then keep in mind that there are <a href="http://taginfo.openstreetmap.org/keys/bicycle#values">other important combinations</a> like bicycle=designated and bicycle=official, too.</p>
</div>
<div id="comment-26637-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 10:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="26655"></span>
<div id="comment-26655" class="comment">
<div id="post-26655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> - thanks for info about official and other weird tags.</p>
</div>
<div id="comment-26655-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 18:58)</span> <span class="comment-user userinfo">Bulwersator</span>
</div>
</div>
</div>
<div id="comment-tools-26622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26622-form-container" class="comment-form-container">
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

<span id="26738"></span>

<div id="answer-container-26738" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26738-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bulwersator has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This should work:</p>
<p>osmfilter input.o5m --drop-ways="highway=footway and bicycle!=yes" -o=output.o5m</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '13, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-26738" class="comments-container">
&#10;</div>
<div id="comment-tools-26738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26738-form-container" class="comment-form-container">
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

