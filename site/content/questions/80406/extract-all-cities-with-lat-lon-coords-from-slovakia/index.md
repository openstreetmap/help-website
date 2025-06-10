+++
type = "question"
title = "Extract all cities with lat lon coords from Slovakia"
description = '''I need to extract all cities with lat lon coords from Slovakia OSM. This is how I imported OSM file downloaded from Geofabrik: osm2pgsql --slim --username postgres --database gis --hstore slovakia-latest.osm psql -U postgres -d gis CREATE EXTENSION hstore;  Import went without errors. What SELECT qu...'''
date = "2021-06-03T18:10:00Z"
lastmod = "2021-09-21T16:04:00Z"
weight = 80406
keywords = [ "city", "postgresql", "postgis" ]
aliases = [ "/questions/80406" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract all cities with lat lon coords from Slovakia](/questions/80406/extract-all-cities-with-lat-lon-coords-from-slovakia)

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
<span id="post-80406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to extract all cities with lat lon coords from Slovakia OSM.</p>
<p>This is how I imported OSM file downloaded from Geofabrik:</p>
<pre><code>osm2pgsql --slim --username postgres --database gis --hstore slovakia-latest.osm
psql -U postgres -d gis
CREATE EXTENSION hstore;</code></pre>
<p>Import went without errors.</p>
<p>What SELECT query should be to see 3 tables (city, latitude, longitude)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '21, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/1aeb86ca63b3378f4f80751ca910ec2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akulin&#39;s gravatar image" />
<p><span>akulin</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akulin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80406" class="comments-container">
&#10;</div>
<div id="comment-tools-80406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80406-form-container" class="comment-form-container">
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

<span id="81845"></span>

<div id="answer-container-81845" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>SELECT name, st_astext(st_transform(way, 4326)) FROM planet_osm_point WHERE place=&#39;city&#39; OR place=&#39;town&#39; ORDER BY name;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '21, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/1aeb86ca63b3378f4f80751ca910ec2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akulin&#39;s gravatar image" />
<p><span>akulin</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akulin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '21, 11:35</strong> </span></p>
</div>
</div>
<div id="comments-container-81845" class="comments-container">
&#10;</div>
<div id="comment-tools-81845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81845-form-container" class="comment-form-container">
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

