+++
type = "question"
title = "[closed] ST_Within vs ST_Intersects slow performance and alternatives"
description = '''Hi all, I am trying to query the total number of building for each German postcode. I am using the the center point of the buildings and postcode shape files. There are around 26 Mil buildings and around 8K postcodes. I am using the most simplest shape file (less points) but the search still takes d...'''
date = "2017-08-10T15:22:00Z"
lastmod = "2017-08-10T19:02:00Z"
weight = 57547
keywords = [ "postgresql", "osm", "osm2pgsql", "postgis", "query" ]
aliases = [ "/questions/57547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] ST_Within vs ST_Intersects slow performance and alternatives](/questions/57547/st_within-vs-st_intersects-slow-performance-and-alternatives)

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
<span id="post-57547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to query the total number of building for each German postcode. I am using the the center point of the buildings and postcode shape files. There are around 26 Mil buildings and around 8K postcodes. I am using the most simplest shape file (less points) but the search still takes days. Although, ST_Within performs faster than ST_Intersects it still takes 0.24 seconds for one search. 26 Mil will take weeks. Any suggestions to improve the performance or alternative solutions? My sql is below. Thanks.</p>
<p>SELECT a.osm_id b.plz FROM building_check a LEFT JOIN plz_test b on ST_Within(a.geo, b.geom);</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '17, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ac18356019d6ebeea5c9c8e33414ed74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrparadox&#39;s gravatar image" />
<p><span>mrparadox</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrparadox has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>10 Aug '17, 19:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-57547" class="comments-container">
<span id="57553"></span>
<div id="comment-57553" class="comment">
<div id="post-57553-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not informative, you need to add more info: "hat indexes are placed on the tables? What does a query plan look like? Also this is a generic PostGIS query &amp; may be more appropriate for GIS StackExchange.</p>
</div>
<div id="comment-57553-info" class="comment-info">
<span class="comment-age">(10 Aug '17, 19:02)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57547-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question: Asked in similar form https://help.openstreetmap.org/questions/57522/osm-sql-query-with-node-and-zip-code-shape-files-using-st_intersects" by SK53 10 Aug '17, 19:04

</div>

</div>

</div>

