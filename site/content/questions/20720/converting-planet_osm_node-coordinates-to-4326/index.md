+++
type = "question"
title = "converting planet_osm_node coordinates to 4326"
description = '''Hi I am trying to convert the coordinates stored in the planet_osm_nodes table in my GIS database to normal latitude/longitude coordinates (4326). Here is an example of what the coordinates in the table look like:  lat | lon  -----------+-----------  754030751 | -39701762  Here is an SQL query that ...'''
date = "2013-03-15T15:24:00Z"
lastmod = "2020-03-05T12:57:00Z"
weight = 20720
keywords = [ "conversion", "osm", "planet_osm", "coordinates" ]
aliases = [ "/questions/20720" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [converting planet_osm_node coordinates to 4326](/questions/20720/converting-planet_osm_node-coordinates-to-4326)

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
<span id="post-20720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20720-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am trying to convert the coordinates stored in the <code>planet_osm_nodes</code> table in my GIS database to normal latitude/longitude coordinates (4326).</p>
<p>Here is an example of what the coordinates in the table look like:</p>
<pre><code> lat    |    lon    
-----------+-----------
 754030751 | -39701762</code></pre>
<p>Here is an SQL query that I am using for the conversion:</p>
<pre><code>select ST_AsText(ST_Transform(ST_GeomFromEWKT(&#39;SRID=900913;POINT(&#39; || lon || &#39; &#39; || lat || &#39;)&#39;), 4326)) from planet_osm_nodes;</code></pre>
<p>However the coordinates are like:</p>
<pre><code>POINT(40.5500029995757 90)</code></pre>
<p>When they should be more like <code>(55.3, -3.10)</code></p>
<p>Is the SRID that the latitude and longitude in the <code>planet_osm_nodes</code> table 900913 or is it something different?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '13, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20720" class="comments-container">
&#10;</div>
<div id="comment-tools-20720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20720-form-container" class="comment-form-container">
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

<span id="20789"></span>

<div id="answer-container-20789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20789-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The coordinates in the planet_osm_nodes table aren't in any proper spatial reference system. They are stored as integers, not as coordinate values, and are manipulated when converted to the spatial tables. If you look closely, they are too large to be spherical mercator coordinates (hence the clipping to 90), and the fact that they are in integer columns would otherwise suggest a large amount of rounding!</p>
<p>Instead, you should grab the coordinates from the geometry ("way") column of the planet_osm_point table, which are indeed actual coordinates. If for some reason you must use the nodes table (which is unusual) then <a href="https://trac.openstreetmap.org/browser/subversion/applications/utils/export/osm2pgsql/osm2pgsql.c?rev=29369#L623">divide the integers by 100</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '13, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-20789" class="comments-container">
&#10;</div>
<div id="comment-tools-20789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20789-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44910"></span>

<div id="answer-container-44910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44910-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi! I'm looking for the same answer and I wrote this code, in C:</p>
<pre><code>const double R_TERRA = 6378137;
struct node {
   float latitude;
   float longitude;
};
&#10;void mercatorSphericalToLatLon(long mercX, long mercY, struct node *point) {
&#10;   double lon = (mercX / 100.0) / (M_PI * R_TERRA) * 180.0;
   double lat = (mercY / 100.0) / (M_PI * R_TERRA) * 180.0;
   lat = 180.0 / M_PI * (2.0 * atan(exp(lat * M_PI / 180.0)) - M_PI / 2.0);
&#10;   point-&gt;longitude = (float)lon;
   point-&gt;latitude = (float)lat;
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '15, 21:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2bc5e99e754fc7cfaf4037cad7495cac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a_manfrinati&#39;s gravatar image" />
<p><span>a_manfrinati</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a_manfrinati has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '15, 21:32</strong> </span></p>
</div>
</div>
<div id="comments-container-44910" class="comments-container">
&#10;</div>
<div id="comment-tools-44910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44910-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73393"></span>

<div id="answer-container-73393" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends on how the values were imported. My data was created by Nominatim which simply converts lat/lon to an integer by multiplying by 10000000.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '20, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/4f377b36e190cbd3b5a0c57d981e38b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neilireson&#39;s gravatar image" />
<p><span>neilireson</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neilireson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73393" class="comments-container">
&#10;</div>
<div id="comment-tools-73393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73393-form-container" class="comment-form-container">
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

