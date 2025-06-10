+++
type = "question"
title = "Rules around multipolygons processing (JOSM vs OSM InspectorAreas)"
description = '''I am updating an area I mapped a few years ago (thank to a recent and accurate Esri World Imagery). On multiple occasions I found that multipolygons I created were converted into simple features (areas), duplicating all their ways.  The comments of the changesets in which they were replaced often re...'''
date = "2020-12-16T23:21:00Z"
lastmod = "2020-12-19T22:54:00Z"
weight = 77960
keywords = [ "rules", "josm", "inspectorareas", "multipolygon" ]
aliases = [ "/questions/77960" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rules around multipolygons processing (JOSM vs OSM InspectorAreas)](/questions/77960/rules-around-multipolygons-processing-josm-vs-osm-inspectorareas)

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
<span id="post-77960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77960-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am updating an area I mapped a few years ago (thank to a recent and accurate Esri World Imagery). On multiple occasions I found that multipolygons I created were converted into simple features (areas), duplicating all their ways.</p>
<p>The comments of the changesets in which they were replaced often refer to “OSM InspectorAreas ring_not_closed”. Since I always check my polygons using JOSM. I wonder if… - Is there a conflict/problem between OSM InspectorAreas and JOSM? - If I forgot to checked OSM, should I have expected the rings being closed in the multipolygon instead of having all those lines duplicated?</p>
<p>The most recent example is changeset 92270556 where I remember having created multipolygons for a group of natural=wood, natural=scrub, natural=water and landuse=commercial.</p>
<p>thank you to enlighten me</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-inspectorareas" rel="tag" title="see questions tagged &#39;inspectorareas&#39;">inspectorareas</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '20, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77960" class="comments-container">
&#10;</div>
<div id="comment-tools-77960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77960-form-container" class="comment-form-container">
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

<span id="77976"></span>

<div id="answer-container-77976" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77976-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen the same thing happen near me, done by the same contributor.</p>
<p>I think what's happening is someone makes a change that breaks a multipolygon, such as inadvertently deleting a way or otherwise disrupting the geometry. Then, kartler175 comes along and changes the multipolygon's outer way to a single closed way, rather than actually fixing the multipolygon.</p>
<p>So, in the end, what's happening is that a contributor is trying to be helpful, but going about it in a less-than-ideal way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '20, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-77976" class="comments-container">
<span id="77977"></span>
<div id="comment-77977" class="comment">
<div id="post-77977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank, it's entirely possible, but since the contributor didn't respond to my comment (on the changeset), I wondered if there was a rule I didn't know about multipolygons, or if there were any known issues with JOSM or OSM Inspector.</p>
</div>
<div id="comment-77977-info" class="comment-info">
<span class="comment-age">(17 Dec '20, 18:47)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
<span id="78011"></span>
<div id="comment-78011" class="comment">
<div id="post-78011-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FWIW, they have replied to some changeset discussion comments. If it looks like they need a nudge to reply to more, ask the DWG to help (mail data@osmfoundation.org ).</p>
</div>
<div id="comment-78011-info" class="comment-info">
<span class="comment-age">(19 Dec '20, 22:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77976-form-container" class="comment-form-container">
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

