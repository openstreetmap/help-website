+++
type = "question"
title = "is there a  datum shift between OSM  and true WGS84"
description = '''Hi I&#x27;ve converted some OSM data of Cambridgeshire UK into POSTGIS using osm2pgsql like this.  createDB osm  createlang plpgsql osm –U username   psql –U username –d osm -f /path/to/postgis1.5/postgis.sql  psql –U username –d osm -f /path/to/postgis1.5/spatial_ref_sys.sql  osm2pgsql –S /path/to/osm2p...'''
date = "2012-06-11T17:59:00Z"
lastmod = "2015-03-13T16:23:00Z"
weight = 13428
keywords = [ "wgs84", "osm2pgsql", "postgis" ]
aliases = [ "/questions/13428" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [is there a datum shift between OSM and true WGS84](/questions/13428/is-there-a-datum-shift-between-osm-and-true-wgs84)

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
<span id="post-13428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've converted some OSM data of Cambridgeshire UK into POSTGIS using osm2pgsql like this.</p>
<pre><code> createDB osm
 createlang plpgsql osm –U username 
 psql –U username –d osm  -f /path/to/postgis1.5/postgis.sql
 psql –U username –d osm  -f /path/to/postgis1.5/spatial_ref_sys.sql
 osm2pgsql –S /path/to/osm2pgsql/default.style –U username –d osm  -l –c /path/to/ cambridgeshire.osm.bz2</code></pre>
<p>I've overlayed it on some imagery of the area. The image has been orthorectified to WGS84 Geographical &amp; fits all other data sets used. In QuantumGis both the image and the OSM data are showing the same datum but the OSM vectors are approximately 25m -30m North East of the image.</p>
<pre><code> QGIS Layer spatial referance system
 +proj=longlat +ellps=WGS84 +datum=WG84 +no_defs</code></pre>
<p>How might I get the OSM data to fit the image? Please note once i've worked out how to do this i'll be moving on to a larger dataset Thanx Holly</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wgs84" rel="tag" title="see questions tagged &#39;wgs84&#39;">wgs84</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '12, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/4d0ecaa0e9d043e9a58a7a4896a9fc2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HollyG&#39;s gravatar image" />
<p><span>HollyG</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HollyG has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13428" class="comments-container">
<span id="13459"></span>
<div id="comment-13459" class="comment">
<div id="post-13459-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you add a permalink to the area (zoom the map on www.openstreetmap.org to the area and select the "Permalink" link) to your question? Thanks</p>
</div>
<div id="comment-13459-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 14:08)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="13472"></span>
<div id="comment-13472" class="comment">
<div id="post-13472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using a standalone system</p>
</div>
<div id="comment-13472-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 18:17)</span> <span class="comment-user userinfo">HollyG</span>
</div>
</div>
</div>
<div id="comment-tools-13428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13428-form-container" class="comment-form-container">
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

<span id="13461"></span>

<div id="answer-container-13461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13461-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data is true WGS84. Without any links to the area in question I can not tell exactly what is going on. When I look at Camebridge OSM matches bing areal, google maps and even the raw gps data collected. If you open an editor for the area you can select other sources to add as layers and view the accuracy. It might be that there are some errors in the osm data, that there are some errors in your setup or that your orthorectified sources are wrong. I can not tell.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '12, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13461" class="comments-container">
<span id="13476"></span>
<div id="comment-13476" class="comment">
<div id="post-13476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not suggesting OSM is wrong it uses google Mercator projection 900913 which is aligned to WGS84 we use unprojeted WGS84 datum EPSG:4326 all the imagery sources you quot use the same google Mercator projection so they will fit what i'm after is a trigonometric function that when applied to the coordinates of OSM 900913 data to shift them to EPSG:4326</p>
</div>
<div id="comment-13476-info" class="comment-info">
<span class="comment-age">(12 Jun '12, 19:11)</span> <span class="comment-user userinfo">HollyG</span>
</div>
</div>
<span id="13488"></span>
<div id="comment-13488" class="comment">
<div id="post-13488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Again in Qgis I've inserted the raw osm file I then overlayed the PostGIS layers they align perfectly. I had assumed there would be differences between the 900913 projected osm vectors and the unprojected WGS84 datum EPSG:4326.</p>
</div>
<div id="comment-13488-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 07:07)</span> <span class="comment-user userinfo">HollyG</span>
</div>
</div>
<span id="13524"></span>
<div id="comment-13524" class="comment">
<div id="post-13524-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to realise that OSM data is recorded in WGS84, and that's what you receive when you download any osm.bz2 files. Sure, the maps and the editing interface is (often, but not always) shown in 900913, but underneath it's all pure WGS84.</p>
</div>
<div id="comment-13524-info" class="comment-info">
<span class="comment-age">(14 Jun '12, 09:49)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-13461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41688"></span>

<div id="answer-container-41688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An extremely late (archival) answer!</p>
<p>There were some bugs in various OSGeo products in transforming in and out of the OSGB NT36 (EPSG code 27700). In addition failure to specify a complete Helmert Transformation in WKT or proj4 or in ESRI projection files often results in this type of error. (I would have to find a 3 year old installation of PostGIS to demonstrate this properly, but one could put in a known British National Grid co-ordinate and convert to WGS, or ECTS or Google Spherical Mercator and back and the point would be dislocated a few metres). (This caused me quite a few problems when preparing my SotM-EU presentation in 2011).</p>
<p>In conclusion it was probably the orthorectified images transformed to either WGS84 or Spherical Mercator which were misaligned.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '15, 16:23</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-41688" class="comments-container">
&#10;</div>
<div id="comment-tools-41688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41688-form-container" class="comment-form-container">
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

