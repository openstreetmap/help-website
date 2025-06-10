+++
type = "question"
title = "find max speed of road using lat lon"
description = '''I migrated osm data using osm2pgsql. I am using the following query to get road information from lat lon values.  SELECT   osm_id,  highway,  name,  ref,   ST_X(ST_ClosestPoint(ST_Transform(r.way, 4326), point.geom)),   ST_Y(ST_ClosestPoint(ST_Transform(r.way, 4326), point.geom)),  ST_Distance_Spher...'''
date = "2017-07-27T13:49:00Z"
lastmod = "2017-08-06T13:26:00Z"
weight = 57311
keywords = [ "maxspeed", "osm2pgsql", "postgis" ]
aliases = [ "/questions/57311" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [find max speed of road using lat lon](/questions/57311/find-max-speed-of-road-using-lat-lon)

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
<span id="post-57311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57311-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I migrated osm data using osm2pgsql. I am using the following query to get road information from lat lon values.</p>
<pre><code> SELECT 
 osm_id,
 highway,
 name,
 ref, 
 ST_X(ST_ClosestPoint(ST_Transform(r.way, 4326), point.geom)),      
 ST_Y(ST_ClosestPoint(ST_Transform(r.way, 4326), point.geom)),
 ST_Distance_Sphere(ST_ClosestPoint(ST_Transform(r.way, 4326), point.geom), point.geom)
FROM 
  planet_osm_roads r,
  (Select ST_SetSRID(ST_MakePoint(-104.718649, 39.201070), 4326) as geom) point
ORDER BY 7 ASC
LIMIT 1;</code></pre>
<p>where -104.718649, 39.201070 are lon and lat values. Now I also need the maxspeed of that road. how can i get the maxspeed of a road given lat lon values?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '17, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57311" class="comments-container">
&#10;</div>
<div id="comment-tools-57311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57311-form-container" class="comment-form-container">
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

<span id="57480"></span>

<div id="answer-container-57480" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57480-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just had to add the following line to the style file</p>
<p><code>way maxspeed text linear</code></p>
<p>and it added maxspeed to each record.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '17, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57480" class="comments-container">
&#10;</div>
<div id="comment-tools-57480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57480-form-container" class="comment-form-container">
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

