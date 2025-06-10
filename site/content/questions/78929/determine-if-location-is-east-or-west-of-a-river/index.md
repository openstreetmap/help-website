+++
type = "question"
title = "Determine if location is east or west of a river"
description = '''I have a big list of locations with their coordinates in a city that is fully divided by a river that&#x27;s running from north to south.  Now I want to determine for each location if it is located east or west of that river.  If it was possible to get the coordinates of the river in a granular enough ma...'''
date = "2021-02-18T14:55:00Z"
lastmod = "2021-02-22T18:21:00Z"
weight = 78929
keywords = [ "river", "coordinates" ]
aliases = [ "/questions/78929" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Determine if location is east or west of a river](/questions/78929/determine-if-location-is-east-or-west-of-a-river)

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
<span id="post-78929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78929-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a big list of locations with their coordinates in a city that is fully divided by a river that's running from north to south. Now I want to determine for each location if it is located east or west of that river. If it was possible to get the coordinates of the river in a granular enough manner, I could achieve that goal by comparing coordinates between location and the river.</p>
<p>I have not found a way to get these coordinates so far. I'm new to OSM, however, and would be thrilled if someone could point me in the right direction here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '21, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/88e2e6e0cf86ece948ac915f94d3c640?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RedAlakazam&#39;s gravatar image" />
<p><span>RedAlakazam</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RedAlakazam has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '21, 14:56</strong> </span></p>
</div>
</div>
<div id="comments-container-78929" class="comments-container">
&#10;</div>
<div id="comment-tools-78929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78929-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="78932"></span>

<div id="answer-container-78932" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78932-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RedAlakazam has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you use osm2pgsql to load the OSM data into PostGIS database (based on postsql) then you can use use the ST_closestpoint() function to find the closest point on a way (your river) to a point. You can then take the two points (one on the river and the one you are interested in) and use the ST_Azimuth() function to determine the direction of travel between the two points.</p>
<p>If the the river is serpentine you may get a result other than what you wish for (if the point is within a loop or near a curve in the river the azimuth could be quite different than you want). I don’t have enough experience with this stuff to suggest a way around that issue though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '21, 02:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-78932" class="comments-container">
&#10;</div>
<div id="comment-tools-78932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78932-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78992"></span>

<div id="answer-container-78992" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78992-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-78992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up using <a href="https://help.openstreetmap.org/users/5918/stf">@stf</a>'s suggestion of using the ST_AZIMUTH() function.</p>
<p><code>SELECT CASE WHEN DEGREES(ST_AZIMUTH(pt, cl_pt)) &gt; 180 THEN 'right' ELSE 'left' END AS RIVER_ORIENTATION, ROUND(ST_DISTANCE(pt, cl_pt)) AS RIVER_DISTANCE, name FROM ( SELECT name, ST_ClosestPoint(pt, line) AS pt, ST_CLOSESTPOINT(line, pt) AS cl_pt, line as river FROM (SELECT name, ST_TRANSFORM(ST_setSRID(ST_MAKEPOINT(longitude, latitude), 4326), 3857) AS pt FROM location_information) tmp1, (SELECT ST_UNION(way) AS FROM planet_osm_line WHERE name='INSERT RIVER NAME') tmp2 ) tmp3</code></p>
<p>Making the left/right distinction at 180 degrees worked out perfectly in this case. <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a>'s suggestion of splitting the map in two using the river would've lead to a more robust solution but the river had some arms with the same name which made it inconvenient in my case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '21, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/88e2e6e0cf86ece948ac915f94d3c640?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RedAlakazam&#39;s gravatar image" />
<p><span>RedAlakazam</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RedAlakazam has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78992" class="comments-container">
&#10;</div>
<div id="comment-tools-78992" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78992-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78947"></span>

<div id="answer-container-78947" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78947-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another computational option would be: 1. Create polygon around whole city. 2. Get river geometry as a line. 3. split polygon in two along that line. 4. for every point, ask "is this point in the left-land polygon", if not it'll be on the right.</p>
<p>If I understand the question correctly, the main issue is extracting the river's coordinates. This could potentially be done in PostGIS if the data is loaded (something along the lines of <code>SELECT ST_UNION(way) FROM planet_osm_line WHERE "natural"='river' AND name="XYZ River")</code>. This query would also take care of combining several "pieces" of river into one, but would yield unwanted results if the river should have "arms" that share the same name! If you don't want to load the data into PostGIS first, the Overpass service can be used to request all things tagged natural=river with a certain name in a certain bounding box, however additional libraries would then have to be used to combine river parts into one, to split a polygon, or to determine wheter a point is inside a polygon. If you're attempting to do it all in Javascript then Turf.js is an option for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '21, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78947" class="comments-container">
&#10;</div>
<div id="comment-tools-78947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78947-form-container" class="comment-form-container">
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

