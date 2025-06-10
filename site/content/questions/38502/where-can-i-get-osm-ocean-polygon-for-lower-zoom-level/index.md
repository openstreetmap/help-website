+++
type = "question"
title = "Where can i get OSM ocean polygon for lower zoom level?"
description = '''i am generating vector tiles from mapnik-vector-tiles which is bundled by avecado. i am in need of ocean polygon for the world. Please refer  http://gis.stackexchange.com/questions/120708/where-can-i-get-osm-water-polygon-for-lower-zoom-level https://github.com/mapbox/mapnik-vector-tile/issues/70 an...'''
date = "2014-11-12T11:51:00Z"
lastmod = "2014-11-15T13:12:00Z"
weight = 38502
keywords = [ "mapbox", "tiles", "vector", "mapnik", "ocean" ]
aliases = [ "/questions/38502" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Where can i get OSM ocean polygon for lower zoom level?](/questions/38502/where-can-i-get-osm-ocean-polygon-for-lower-zoom-level)

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
<span id="post-38502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38502-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am generating vector tiles from mapnik-vector-tiles which is bundled by avecado.</p>
<p>i am in need of ocean polygon for the world.</p>
<p>Please refer <a href="http://gis.stackexchange.com/questions/120708/where-can-i-get-osm-water-polygon-for-lower-zoom-level">http://gis.stackexchange.com/questions/120708/where-can-i-get-osm-water-polygon-for-lower-zoom-level</a></p>
<p><a href="https://github.com/mapbox/mapnik-vector-tile/issues/70">https://github.com/mapbox/mapnik-vector-tile/issues/70</a></p>
<p>and</p>
<p><a href="https://github.com/MapQuest/avecado/issues/37">https://github.com/MapQuest/avecado/issues/37</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-ocean" rel="tag" title="see questions tagged &#39;ocean&#39;">ocean</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '14, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38502" class="comments-container">
&#10;</div>
<div id="comment-tools-38502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38502-form-container" class="comment-form-container">
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

<span id="38547"></span>

<div id="answer-container-38547" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arun kmp has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. If you are still interested in "ocean polygon" here is one option that can maybe help you. From your text I assume that you are interested in the Global Ocean area (everything blue, outside the continents) or maybe in the Planet-sea (as the inverse of the Planet-land areas created from the coastline dataset). The Planet-sea in 11 scale levels you may download (shp format) from here<br />
<a href="https://drive.google.com/file/d/0B6qGm3k2qWHqYVl1NUFRVFQtMEk/view?usp=sharing">https://drive.google.com/file/d/0B6qGm3k2qWHqYVl1NUFRVFQtMEk/view?usp=sharing</a><br />
with a log file suggesting how and when to switch between these levels when doing continuous scaling. If you want only the Global Ocean, just take/extract the largest area object (the first one) from the level files. From my side, you may use these data as you like but in accordance with the OSM licencing rules. The data is from some weeks ago created from the OSM Planet dump. The procedure when and how to create these scale levels is complex and complicated. Yet here are some notes and suggestions (maybe unnecessary).<br />
1.The vector scale levels are created under quite different criteria compared to the usual raster zoom levels. The scale levels provide continuous scaling, with roughly the same amount of data to transmit for any scale factor where the objects spontaneously appear and disappear when zooming in and out.<br />
2.Any data generalisation model (i.e. used here as well) inevitable creates self-crossings and very small areas between such points. If your area rendering algorithm requires simple closed border lines, please try to avoid the usual area splitting up model. This may result in ugly fragmentation. Consider exchanging the poly-line segments between the neighbouring self-crossings and reverse them. In this way self-crossings become just touching points.<br />
3.When tiling sea scale levels I suggest to use uniform square tiles. But please be aware that for a moderate/small tile size for some of the scale levels you may end up with a huge number (hundreds of millions) of tiles. Consider generating only none-trivial tiles (those containing at least one border point) and automatic regeneration of the trivial (pure blue) tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '14, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-38547" class="comments-container">
&#10;</div>
<div id="comment-tools-38547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38547-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38537"></span>

<div id="answer-container-38537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38537-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe from <a href="http://openstreetmapdata.com">OpenStreetMap Data</a> ?</p>
<p>They have special OSM based shapefiles for coastlines etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '14, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-38537" class="comments-container">
&#10;</div>
<div id="comment-tools-38537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38537-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38575"></span>

<div id="answer-container-38575" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38575-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your <a href="http://help.openstreetmap.org/users/99/stephan75"></a><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan</a></a> and <a href="http://help.openstreetmap.org/users/3194/sanser"></a><a href="http://help.openstreetmap.org/users/3194/sanser">@sanser</a></a>. i tried OpenStreetMap Data, its size is 377MB it fits for zoom level above 8 or 9. But what about the scenario for zoom level from 0 to 8. simply if i use openstreetmap Data in zoom level 0 it will take more size in creating vector tiles. so i go with Natural Earth data.</p>
<p>Test Case for Using Natural Earth data.</p>
<p>1) Initially i used shape file directly. it didnt show any error at the same time it didnt show proper result so i checked the pbf file. In geometry same values repeating again and again please see <a href="https://github.com/mapbox/mapnik-vector-tile/issues/70.">https://github.com/mapbox/mapnik-vector-tile/issues/70.</a> so it fails.</p>
<p>2) i convert the shape file to postgis and import the geometry from postgis again i got same output.</p>
<p>3) Later i checked the geometry projection. In new natural_earth table i found geometry is normal latitude and longitude but in planet_osm_node table it is transformed lat long.</p>
<p>so i prefer to change the lat long. this is my new query</p>
<p>select ST_AsText(ST_Transform(geom, 900913)) from ne_110m_ocean</p>
<p>it works fine except poles. yes, st_transform show</p>
<p>error in poles is ERROR: transform: couldn't project point (-180 90 0): tolerance condition error (-20)</p>
<p>Error here is due to poles. srid 900913 did not accept 90. so in geometry instead of 90 change to 89.9999999. then transform the srid to 900913 select ST_AsText(ST_Transform(geom, 900913)) from ne_110m_ocean</p>
<p>it works fine and correct vector tiles also generated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '14, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/672f9138349e062b5fc0a11d50a9ca6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20kmp&#39;s gravatar image" />
<p><span>Arun kmp</span><br />
<span class="score" title="63 reputation points">63</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun kmp has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '14, 13:14</strong> </span></p>
</div>
</div>
<div id="comments-container-38575" class="comments-container">
&#10;</div>
<div id="comment-tools-38575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38575-form-container" class="comment-form-container">
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

