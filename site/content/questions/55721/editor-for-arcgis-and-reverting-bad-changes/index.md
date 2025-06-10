+++
type = "question"
title = "Editor for ArcGIS and reverting bad changes"
description = '''I am trying to update OSM with custom tags for bicycle-specific data as part of a project my city is working on. I am using ArcGIS Editor for OSM 10.4. My changes have messed some things up, including removing almost all of the tags from several street segments and adding duplicates of split segment...'''
date = "2017-04-20T22:29:00Z"
lastmod = "2017-04-21T00:00:00Z"
weight = 55721
keywords = [ "arcgis", "revert" ]
aliases = [ "/questions/55721" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Editor for ArcGIS and reverting bad changes](/questions/55721/editor-for-arcgis-and-reverting-bad-changes)

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
<span id="post-55721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to update OSM with custom tags for bicycle-specific data as part of a project my city is working on. I am using ArcGIS Editor for OSM 10.4. My changes have messed some things up, including removing almost all of the tags from several street segments and adding duplicates of split segments instead of replacing the old segments (see changeset 47885657). I'm new to OSM and I was following directions on how to make these kinds of edits, so I don't know how any of this happened. Any insight anyone can provide?</p>
<p>I could use help reverting my changes to start with, since I don't trust myself or ArcGIS at this point, but mostly because I don't know how to recover tag values that are now missing. Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arcgis" rel="tag" title="see questions tagged &#39;arcgis&#39;">arcgis</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Apr '17, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e8a4d676f8784e58d1839a4a54b905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryan%20Fagan&#39;s gravatar image" />
<p><span>Ryan Fagan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryan Fagan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55721" class="comments-container">
&#10;</div>
<div id="comment-tools-55721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55721-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="55722"></span>

<div id="answer-container-55722" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55722-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have reverted your changes with a script; I am not familiar with the Editor for ArcGIS and I'm afraid I don't have insights on how the problem happened! If using a different editor is an option for you, I'd recommend switching to the in-browser "ID" editor or to the standalone JOSM; both are much more widely used and therefore also more mature than the Editor for ArcGIS. JOSM also has a "reverter" plugin with which you would have been able to undo the changeset yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '17, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55722" class="comments-container">
<span id="55723"></span>
<div id="comment-55723" class="comment">
<div id="post-55723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much. I'll see if the in-browser editor will work for what we're trying to do. So far using the editor for ArcGIS has been a nightmare so if I can avoid it I will.</p>
</div>
<div id="comment-55723-info" class="comment-info">
<span class="comment-age">(20 Apr '17, 23:31)</span> <span class="comment-user userinfo">Ryan Fagan</span>
</div>
</div>
</div>
<div id="comment-tools-55722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55722-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55725"></span>

<div id="answer-container-55725" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55725-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, thank you so much for updating the cycling data, it is really appreciated,</p>
<p>I wasn't aware that there was a ArcGIS Editor however at version 14 it should be working fairly well.</p>
<p>Consider installing JOSM (if you can in your corporate environment) and there is a plug in you can install called "reverter" that will revert most changesets if you do it sooner rather than later.</p>
<p>Then try a really small changeset after noting what values and see if you can get it working correctly. Also be careful of multipolygons that may not translate as nicely as they should. Hopefully you will be able to see what the issue is. All the best with the project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '17, 00:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a8dbda930e9da736915267cbe67e5f05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewen%20Hill&#39;s gravatar image" />
<p><span>Ewen Hill</span><br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewen Hill has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55725" class="comments-container">
&#10;</div>
<div id="comment-tools-55725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55725-form-container" class="comment-form-container">
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

