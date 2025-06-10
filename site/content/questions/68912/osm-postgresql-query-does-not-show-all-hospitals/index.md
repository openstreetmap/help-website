+++
type = "question"
title = "OSM postgresql query does not show all hospitals?"
description = '''Hi, I have OSM dataset on Postgresql via osm2pgsql. Now I am trying to query all public buildings in UK such as hospitals, schools, fire stations and churches. In order to do that, I use something like this query: SELECT * FROM planet_osm_point pop WHERE pop.amenity IN (&#x27;hospital&#x27;,&#x27;fire_station&#x27;,&#x27;pl...'''
date = "2019-04-24T10:18:00Z"
lastmod = "2019-04-24T13:19:00Z"
weight = 68912
keywords = [ "openstreetmap", "hospital", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/68912" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM postgresql query does not show all hospitals?](/questions/68912/osm-postgresql-query-does-not-show-all-hospitals)

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
<span id="post-68912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68912-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have OSM dataset on Postgresql via osm2pgsql. Now I am trying to query all public buildings in UK such as hospitals, schools, fire stations and churches. In order to do that, I use something like this query:</p>
<pre><code>SELECT *
FROM planet_osm_point pop
WHERE pop.amenity IN (&#39;hospital&#39;,&#39;fire_station&#39;,&#39;place_of_worship&#39;,&#39;school&#39;)</code></pre>
<p>By looking at the results, it just extracts some of the hospitals. I can see the red plus logo for hospitals that I also know that they exist there. But it does not show them in the query results.</p>
<p>How can I include all of these buildings?</p>
<p>Here is the example picture: <a href="https://imgur.com/a/jjTlZ4N">https://imgur.com/a/jjTlZ4N</a></p>
<p>Blue color is from the results. But the red circle hsopitals are not included in the query results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-hospital" rel="tag" title="see questions tagged &#39;hospital&#39;">hospital</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '19, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5c933e9eefe555dc498e2ec55f744728?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sypolt&#39;s gravatar image" />
<p><span>sypolt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sypolt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '19, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-68912" class="comments-container">
&#10;</div>
<div id="comment-tools-68912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68912-form-container" class="comment-form-container">
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

<span id="68913"></span>

<div id="answer-container-68913" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68913-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem likely is that you're missing those hospitals mapped as areas. You have to run the same query on planet_osm_polygon as well, or you could construct a "union" query that gives you the centrepoints of polygons in addition to the points.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '19, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68913" class="comments-container">
<span id="68914"></span>
<div id="comment-68914" class="comment">
<div id="post-68914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I tried this. I got the amenity = 'hospital' from polygon table and unioned all with the points. It only gives a few more hospitals. Still, I see many red plus signs that are not included in the query result.</p>
</div>
<div id="comment-68914-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 10:41)</span> <span class="comment-user userinfo">sypolt</span>
</div>
</div>
<span id="68915"></span>
<div id="comment-68915" class="comment">
<div id="post-68915-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your next step needs to be to find out the node, way or relation ID of a hospital that you're missing and query your database for it. If you can give an example object ID that you are missing people will be able to offer more help.</p>
</div>
<div id="comment-68915-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 11:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68916"></span>
<div id="comment-68916" class="comment">
<div id="post-68916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. May I ask how I can find node/way id? For example, I know this particular hospital does not appear in the results: "St thomas hospital, London". So I queried the points which have the name of "%St Thomas%". And there are results for surrounding bus stops and bike parking around the hospital. But still, there is no results for the hospital.</p>
</div>
<div id="comment-68916-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 11:57)</span> <span class="comment-user userinfo">sypolt</span>
</div>
</div>
<span id="68917"></span>
<div id="comment-68917" class="comment">
<div id="post-68917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This would be <a href="https://www.openstreetmap.org/way/122227536">way 122227536</a>. This information can be obtained by using the search function or the query features tool (button 11 at <a href="https://wiki.openstreetmap.org/wiki/Browsing">Browsing</a>).</p>
</div>
<div id="comment-68917-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 12:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68918"></span>
<div id="comment-68918" class="comment">
<div id="post-68918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an example, here's what I did to check that it was in a local database:</p>
<pre><code>psql -c &quot;select osm_id,name from planet_osm_polygon where osm_id = &#39;122227536&#39;&quot; gis</code></pre>
<p>I got back:</p>
<pre><code>  osm_id   |                              name
-----------+-----------------------------------------------------------------
 122227536 | St Thomas&#39; Hospital (Guy&#39;s and St Thomas&#39; NHS Foundation Trust)
(1 row)</code></pre>
</div>
<div id="comment-68918-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 12:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68919"></span>
<div id="comment-68919" class="comment not_top_scorer">
<div id="post-68919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for providing the osm_id. I found this osm id only in "planet_osm_ways" table. And this table has these columns: nodes, tags, pending. And Pending = True for this hospital. What does that mean? Do I use an older version of OSM maybe?</p>
</div>
<div id="comment-68919-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 13:11)</span> <span class="comment-user userinfo">sypolt</span>
</div>
</div>
<span id="68920"></span>
<div id="comment-68920" class="comment not_top_scorer">
<div id="post-68920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16588/sypolt">@sypolt</a> I think you need to tell us what you actually did. Did the import process actually complete?</p>
</div>
<div id="comment-68920-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 13:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68921"></span>
<div id="comment-68921" class="comment not_top_scorer">
<div id="post-68921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. So I downloaded this dataset: download.geofabrik.de/europe/british-isles.html. and then used osm2pgsql to import to database. The process was completed. I did this task a long time ago.</p>
</div>
<div id="comment-68921-info" class="comment-info">
<span class="comment-age">(24 Apr '19, 13:19)</span> <span class="comment-user userinfo">sypolt</span>
</div>
</div>
</div>
<div id="comment-tools-68913" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-68913-form-container" class="comment-form-container">
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

