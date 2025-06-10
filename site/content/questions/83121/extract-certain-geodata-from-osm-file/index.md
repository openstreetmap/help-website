+++
type = "question"
title = "Extract certain geodata from OSM File"
description = '''Hi, is there a way to extract just certain data from a specific country from that massive OSM file? I would like to retrieve the German zip codes, the city names including the parts of town and LAT and LON. Export format maybe something like csv or xml. Is that possible in some sort of automatic way...'''
date = "2022-01-19T13:51:00Z"
lastmod = "2022-01-31T10:37:00Z"
weight = 83121
keywords = [ "geodata", "latitude", "extract", "longitude", "zip-code" ]
aliases = [ "/questions/83121" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract certain geodata from OSM File](/questions/83121/extract-certain-geodata-from-osm-file)

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
<span id="post-83121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is there a way to extract just certain data from a specific country from that massive OSM file?</p>
<p>I would like to retrieve the German zip codes, the city names including the parts of town and LAT and LON. Export format maybe something like csv or xml. Is that possible in some sort of automatic way? There are free databases that provide nearly everything of my desired data but the parts of town and their specific LAT and LON are always missing.</p>
<p>Thank you guys for your ideas.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geodata" rel="tag" title="see questions tagged &#39;geodata&#39;">geodata</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '22, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/613f5a8365ac1b645e5d742c87756857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bingoboy1234&#39;s gravatar image" />
<p><span>Bingoboy1234</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bingoboy1234 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83121" class="comments-container">
&#10;</div>
<div id="comment-tools-83121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83121-form-container" class="comment-form-container">
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

<span id="83122"></span>

<div id="answer-container-83122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can do it but it is not trivial. The easiest way is probably importing the data into a PostGIS database with <code>osm2pgsql</code> (you can make it import only the features you are interested in) and then work with SQL. Thing is that the "parts of town" you're after may be mapped as a single node (<code>place=suburb</code> or <code>place=neighbourhood</code>) in which case they have a straigforward lat/lon, or they might be a polygon in which case you need to compute the centroid (which is easy to do in PostGIS).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '22, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83122" class="comments-container">
<span id="83274"></span>
<div id="comment-83274" class="comment">
<div id="post-83274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, Frederik. That sounds complicated. I need to train myself with PostGIS. By now I am unfortunately only used to MySQL. Can I compute the polygon centroid automatically for the whole of all German parts of towns in one go or do I need to do that by hand for each city? Latter could become a job without an end.</p>
</div>
<div id="comment-83274-info" class="comment-info">
<span class="comment-age">(31 Jan '22, 10:22)</span> <span class="comment-user userinfo">Bingoboy1234</span>
</div>
</div>
</div>
<div id="comment-tools-83122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83275"></span>

<div id="answer-container-83275" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83275-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure what the status of osm-to-mysql importers is. I suspect it will be easier for you to get to grips with PostgreSQL than to try and import to mysql - the difference in terms of SQL should be minuscle. Of course you can compute the centroid for all parts of towns in PostGIS, something like</p>
<pre><code>SELECT 
  st_centroid(way) AS geom,
  name,
  place
INTO
  ortsteile
FROM 
  planet_osm_polygon
WHERE
  place in (&#39;neighbourhood&#39;,&#39;suburb&#39;);</code></pre>
<p>After that, add those that were already present as points</p>
<pre><code>INSERT INTO 
  ortsteile
(SELECT way as geom, name, place FROM 
planet_osm_point WHERE place in (&#39;neighbourhood&#39;,&#39;suburb&#39;);</code></pre>
<p>You might also want to add the admin boundaries on levels above 8 to the mix. And later to find out which city something is in,</p>
<pre><code>ALTER TABLE ortsteile ADD COLUMN ort VARCHAR(64);
UPDATE ortsteile
SET ort = (SELECT name FROM planet_osm_polygon
  WHERE boundary=&#39;administrative&#39; AND admin_level=&#39;8&#39; AND
  st_contains(way, geom));</code></pre>
<p>Because in Germany some cities ("kreisfreie Städte") have an admin_level of 6 you will want to re-run the last query for those points that didn't have an admin_level 8 parent:</p>
<pre><code>UPDATE ortsteile
SET ort = (SELECT name FROM planet_osm_polygon
  WHERE boundary=&#39;administrative&#39; AND admin_level=&#39;6&#39; AND
  st_contains(way, geom)
WHERE ort IS NULL;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '22, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jan '22, 10:38</strong> </span></p>
</div>
</div>
<div id="comments-container-83275" class="comments-container">
&#10;</div>
<div id="comment-tools-83275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83275-form-container" class="comment-form-container">
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

