+++
type = "question"
title = "Optimize fetching road data"
description = '''I am using the following query to fetch road data from planet_osm_line select maxspeed, highway, ref, name, ST_Distance(ST_SetSRID(ST_Point(-98.224861, 38.811898),4326), ST_Transform(way, 4326)) as distance from planet_osm_line where highway is not null and ST_DWithin(ST_SetSRID(ST_Point(-98.224861,...'''
date = "2017-08-07T13:51:00Z"
lastmod = "2017-08-08T08:04:00Z"
weight = 57491
keywords = [ "optimization", "osm", "osm2pgsql", "planet_osm" ]
aliases = [ "/questions/57491" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Optimize fetching road data](/questions/57491/optimize-fetching-road-data)

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
<span id="post-57491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57491-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the following query to fetch road data from <code>planet_osm_line</code></p>
<pre><code>select   maxspeed,   highway,   ref,   name,   ST_Distance(ST_SetSRID(ST_Point(-98.224861,
38.811898),4326), ST_Transform(way, 4326)) as distance   from planet_osm_line   where highway is not null    and ST_DWithin(ST_SetSRID(ST_Point(-98.224861,
38.811898),4326), ST_Transform(way, 4326), 0.0009)   order by              ST_Distance(ST_SetSRID(ST_Point(-98.224861,
38.811898),4326), ST_Transform(way, 4326)) limit 1;</code></pre>
<p>Since i am using north-america database imported with osm2pgsql its taking upto 12 seconds. is there a way where i can optimize this and bring the time close to 1s?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '17, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57491" class="comments-container">
<span id="57499"></span>
<div id="comment-57499" class="comment">
<div id="post-57499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/251246/optimize-fetching-road-information-from-osm">https://gis.stackexchange.com/questions/251246/optimize-fetching-road-information-from-osm</a></p>
</div>
<div id="comment-57499-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 07:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57491-form-container" class="comment-form-container">
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

<span id="57495"></span>

<div id="answer-container-57495" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57495-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-57495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aitizazk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're unnecessarily computing the distance twice, but that's the least of your problems. Your query cannot make use of the geometry index on planet_osm_line because you are applying a geometry transformation to the way column. Every time you make this query, every single highway in North America is converted to EPSG:4326 by PostGIS.</p>
<p>Instead, transform the reference point before you let PostGIS find nearby roads. Assuming your database is in EPSG:900913, that would be</p>
<pre><code>SELECT 
  maxspeed, highway, ref, name,   
  ST_Distance(ST_Transform(ST_SetSRID(ST_Point(-98.224861,38.811898),4326), 900913), way) as distance
FROM 
  planet_osm_line
WHERE
  highway is not null and 
  ST_DWithin(ST_Transform(ST_SetSRID(ST_Point(-98.224861,38.811898),4326), 900913), way, 100)
ORDER BY
  distance 
LIMIT 1;</code></pre>
<p>This query returns near-instantly and gives you the same result. Note I have converted your 0.0009 degrees to approxmiately 100 Mercator units, YMMV.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '17, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '17, 18:01</strong> </span></p>
</div>
</div>
<div id="comments-container-57495" class="comments-container">
<span id="57500"></span>
<div id="comment-57500" class="comment">
<div id="post-57500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Woow thanks alot it drastically improved the performance and now results are returned in less than a second.. Awesome</p>
</div>
<div id="comment-57500-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 08:04)</span> <span class="comment-user userinfo">aitizazk</span>
</div>
</div>
</div>
<div id="comment-tools-57495" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57495-form-container" class="comment-form-container">
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

