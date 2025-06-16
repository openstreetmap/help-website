+++
type = "question"
title = "using OSM.pbf data in TileMill"
description = '''Hi everyone Im trying to create a map in TileMill, I have PostGis but it takes only shapefiles. and I want to use all the data the OSM offers, filter it according to my needs. I read a lot about converting PBF to SHP but I got too confused... too much data can any on help me do it in a good way? Tha...'''
date = "2013-10-17T11:51:00Z"
lastmod = "2013-10-17T16:38:00Z"
weight = 27260
keywords = [ "shapefile", "tilemill", "pbf" ]
aliases = [ "/questions/27260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using OSM.pbf data in TileMill](/questions/27260/using-osmpbf-data-in-tilemill)

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
<span id="post-27260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone Im trying to create a map in TileMill, I have PostGis but it takes only shapefiles. and I want to use all the data the OSM offers, filter it according to my needs. I read a lot about converting PBF to SHP but I got too confused... too much data can any on help me do it in a good way? Thanks a lot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Oct '13, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f4891fcd3cba8f6e43f1b7828e32d8bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shmuli&#39;s gravatar image" />
<p><span>Shmuli</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shmuli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '16, 16:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-27260" class="comments-container">
&#10;</div>
<div id="comment-tools-27260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27260-form-container" class="comment-form-container">
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

<span id="27266"></span>

<div id="answer-container-27266" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27266-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-27266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to load your OSM data into PostGIS using <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '13, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-27266" class="comments-container">
&#10;</div>
<div id="comment-tools-27266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27266-form-container" class="comment-form-container">
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

