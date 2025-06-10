+++
type = "question"
title = "osm sql query with node and zip code shape files using ST_Intersects"
description = '''Hi, I have two tables, one containing polygons of building and one containing polygons of German zipcodes. The idea is to identify and matching the building to its zipcode. But I am not getting any matching results. Can someone pls point me to the right direction. My SQL code is blow.  SELECT a.osm_...'''
date = "2017-08-09T00:20:00Z"
lastmod = "2017-08-11T14:32:00Z"
weight = 57522
keywords = [ "postgresql", "osm", "osm2pgsql", "query" ]
aliases = [ "/questions/57522" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm sql query with node and zip code shape files using ST_Intersects](/questions/57522/osm-sql-query-with-node-and-zip-code-shape-files-using-st_intersects)

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
<span id="post-57522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57522-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have two tables, one containing polygons of building and one containing polygons of German zipcodes. The idea is to identify and matching the building to its zipcode. But I am not getting any matching results. Can someone pls point me to the right direction. My SQL code is blow.</p>
<p>SELECT a.osm_id,a.geo, b.plz FROM building_check2 a LEFT JOIN plz_gebiete b on ST_Intersects(a.geo, b.geom);</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '17, 00:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ac18356019d6ebeea5c9c8e33414ed74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrparadox&#39;s gravatar image" />
<p><span>mrparadox</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrparadox has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57522" class="comments-container">
<span id="57530"></span>
<div id="comment-57530" class="comment">
<div id="post-57530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not enough info to answer the question. Are the two tables in the same co-ordinate system for instance.</p>
</div>
<div id="comment-57530-info" class="comment-info">
<span class="comment-age">(09 Aug '17, 16:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57556"></span>
<div id="comment-57556" class="comment">
<div id="post-57556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I manged to get the right results after setting the co-ordinate systems. But the performance is very slow. I have about 8000 postcodes polygons and 26 Mil nodes. search for one node takes about 0.3 seconds. ST_Within reduces it to about 0.25s. Is there a way to improve the search or an alternative way? My aim is to get the number of buildings for each German postcode.</p>
</div>
<div id="comment-57556-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 11:28)</span> <span class="comment-user userinfo">mrparadox</span>
</div>
</div>
<span id="57558"></span>
<div id="comment-57558" class="comment">
<div id="post-57558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What indices do you have on the tables?</p>
</div>
<div id="comment-57558-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 12:06)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="57559"></span>
<div id="comment-57559" class="comment">
<div id="post-57559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have any.</p>
<p>Building and post code table have name and coordinates. Building is single node and post code contain a polygon as coordinates.</p>
</div>
<div id="comment-57559-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 12:11)</span> <span class="comment-user userinfo">mrparadox</span>
</div>
</div>
<span id="57561"></span>
<div id="comment-57561" class="comment">
<div id="post-57561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well then I wouldn't be surprised that it is slow :-)</p>
</div>
<div id="comment-57561-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 12:45)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="57562"></span>
<div id="comment-57562" class="comment not_top_scorer">
<div id="post-57562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem is that most buildings don't have any tags and i cannot figure a good way to index them. Do you have any idea how I could improve the search?</p>
</div>
<div id="comment-57562-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 12:54)</span> <span class="comment-user userinfo">mrparadox</span>
</div>
</div>
<span id="57563"></span>
<div id="comment-57563" class="comment not_top_scorer">
<div id="post-57563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Add a GIST index on a.geo and another on b.geom.</p>
</div>
<div id="comment-57563-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 13:40)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="57564"></span>
<div id="comment-57564" class="comment not_top_scorer">
<div id="post-57564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately didn't make much of a difference.</p>
</div>
<div id="comment-57564-info" class="comment-info">
<span class="comment-age">(11 Aug '17, 14:32)</span> <span class="comment-user userinfo">mrparadox</span>
</div>
</div>
</div>
<div id="comment-tools-57522" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-57522-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

