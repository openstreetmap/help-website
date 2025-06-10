+++
type = "question"
title = "Software/Libraries to Convert OSM Data to Geojson (without using API)"
description = '''I have some geospatial data in .osm format (edited, conflated in josm) that I&#x27;d like to export that into GeoJSON.  Are there any libraries or software that enable me to directly do this ?  I&#x27;ve read that it&#x27;s possible to export osm data via the API to JSON but some of my data isn&#x27;t able to uploaded ...'''
date = "2012-12-06T16:44:00Z"
lastmod = "2013-10-21T10:54:00Z"
weight = 18255
keywords = [ "json", "export", "conversion", "geojson" ]
aliases = [ "/questions/18255" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Software/Libraries to Convert OSM Data to Geojson (without using API)](/questions/18255/softwarelibraries-to-convert-osm-data-to-geojson-without-using-api)

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
<span id="post-18255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18255-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some geospatial data in .osm format (edited, conflated in josm) that I'd like to export that into GeoJSON.</p>
<p>Are there any libraries or software that enable me to directly do this ?</p>
<p>I've read that it's possible to export osm data via the API to JSON but some of my data isn't able to uploaded to OSM and thus, not looking for an API-based solution.</p>
<p>(<a href="http://vallandingham.me/shapefile_to_geojson.html">I've also found this tutorial where I'd have to first convert the data into a shp and then into geoJSON)</a> but I'd prefer a more direct solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '12, 16:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-18255" class="comments-container">
&#10;</div>
<div id="comment-tools-18255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18255-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="27378"></span>

<div id="answer-container-27378" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27378-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-27378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="skorasaurus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://github.com/tyrasd/osmtogeojson/">osmtogeojson</a> is yet another OSM-to-GeoJSON converter. It's written as a javascript library, but can also be used as a command line tool: After installing it via <code>npm install -g osmtogeojson</code> you can use it like this:</p>
<pre><code>osmtogeojson in.osm &gt; out.geojson</code></pre>
<p>But one can also use the library in javascript (browser or nodejs) projects. Take a look at the <a href="http://tyrasd.github.io/osmtogeojson/">demo page</a>.</p>
<p>The converter is quite feature-complete. It supports multipolygons, has sophisticated <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Polygon_Features">polygon detection</a> and can cope with incomplete OSM data.</p>
<p>The code is already in use on <a href="http://geojson.io">geojson.io</a> as well as <a href="http://overpass-turbo.eu">overpass-turbo.eu</a> (of which it is a spin-off, actually). The sources are found on <a href="https://github.com/tyrasd/osmtogeojson">github</a> (MIT licensed).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-27378" class="comments-container">
&#10;</div>
<div id="comment-tools-27378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27378-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18275"></span>

<div id="answer-container-18275" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18275-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One possible workaround that I've found is that I can open an .osm in qgis (using the OSM plugin, in the default qgis repository. Install by just searching for openstreetmap in the 'manage plugins'). and then saving it as a geojson.</p>
<p>(Still looking for a direct, command line option).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '12, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-18275" class="comments-container">
&#10;</div>
<div id="comment-tools-18275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18275-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18367"></span>

<div id="answer-container-18367" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18367-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM is able to export to GeoJSON, but it depends on what you need. There's no support for relations (that I know of).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '12, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-18367" class="comments-container">
&#10;</div>
<div id="comment-tools-18367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18367-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20512"></span>

<div id="answer-container-20512" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20512-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://gist.github.com/tecoholic/1396990">I've found this javascript that converts OSM to geojson.</a> Excellent.</p>
<p>The newest version of ogr2ogr (v. 1.10) also supports conversion from osm to geospatial formats including geojson.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '13, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/3f2a3925f19f9684808db864d290682c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorasaurus&#39;s gravatar image" />
<p><span>skorasaurus</span><br />
<span class="score" title="1398 reputation points"><span>1.4k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorasaurus has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '13, 18:03</strong> </span></p>
</div>
</div>
<div id="comments-container-20512" class="comments-container">
<span id="27377"></span>
<div id="comment-27377" class="comment">
<div id="post-27377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2geo is actually a javascript script, not python. ;)</p>
<p>Unfortunately, it only does a very basic data conversion (no multipolygons, tag agnostic polygons, etc.).</p>
</div>
<div id="comment-27377-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 10:44)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
</div>
<div id="comment-tools-20512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20512-form-container" class="comment-form-container">
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

