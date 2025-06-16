+++
type = "question"
title = "Mapnik with British Coordinates"
description = '''I am trying to create a slippy map of the area of Wrexham, but using the British Coordinate System (by following https://wiki.openstreetmap.org/wiki/Mapnik_GB_Projection) I can produce the maps in the standard spherical projection, using osm2psql to upload the vectors in a box (-b -3.4,52.85,-2.7,53....'''
date = "2011-03-31T20:27:00Z"
lastmod = "2017-01-05T20:17:00Z"
weight = 4234
keywords = [ "coordinate", "mapnik", "british", "system" ]
aliases = [ "/questions/4234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik with British Coordinates](/questions/4234/mapnik-with-british-coordinates)

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
<span id="post-4234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a slippy map of the area of Wrexham, but using the British Coordinate System (by following <a href="https://wiki.openstreetmap.org/wiki/Mapnik_GB_Projection">https://wiki.openstreetmap.org/wiki/Mapnik_GB_Projection</a>)</p>
<p>I can produce the maps in the standard spherical projection, using osm2psql to upload the vectors in a box (-b -3.4,52.85,-2.7,53.15) to PostgreSQL, and create the tiles defining the same box in generate_tiles.py.</p>
<p>I then change the coordinate system in PostgreSQL with PostGIS extension using the command <code>sudo osm2pgsql -v -H localhost -P 5433 -U gisuser -W -C 4096 -b -3.4,52.85,-2.7,53.15 -S /home/m/bin/welsh.style united_kingdom.osm.bz2</code></p>
<p>Checking the data in Qgis shows everything looks fine and the coordinates are what would be expected. For mapnik, I have changed the srs attribute in osm.xml to <code>+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.999601 +x_0=400000 +y_0=-100000 +ellps=airy +units=m +towgs84=446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894 +units=m +nodefs</code></p>
<p>In generate_tiles.py what coordinate system should bbox be in? Both bbox = (300000,300000,335449,351718) and bbox = (-2.0,52.043,-0.896,54.047) just give me blank tiles.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinate" rel="tag" title="see questions tagged &#39;coordinate&#39;">coordinate</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-british" rel="tag" title="see questions tagged &#39;british&#39;">british</span> <span class="post-tag tag-link-system" rel="tag" title="see questions tagged &#39;system&#39;">system</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '11, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a13d9b2e07a0c07e8c32aed60f4e5886?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pingu512&#39;s gravatar image" />
<p><span>pingu512</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pingu512 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '11, 23:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span></p>
</div>
</div>
<div id="comments-container-4234" class="comments-container">
&#10;</div>
<div id="comment-tools-4234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4234-form-container" class="comment-form-container">
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

<span id="53883"></span>

<div id="answer-container-53883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53883-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question is pretty ancient, but I'm hoping the answer might be useful to someone!</p>
<p>You might want to try using my Python script <a href="https://github.com/gregrs-uk/gb-leisure-carto/blob/master/print-osgb.py">print-osgb.py</a>, which I wrote for this purpose. You set various options at the top of the Python file rather than providing arguments when running the script.</p>
<p>IIRC, the data in PostGIS can be in whatever projection you like as long as this is reflected in the section of the Mapnik XML file that defines the data source. However, the srs at the top of the XML file should reflect the OSGB projection. I normally just use <code>srs="+init=epsg:27700"</code> for this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '17, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96c2522da1dee70df309c3bf9d279ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greg&#39;s gravatar image" />
<p><span>Greg</span><br />
<span class="score" title="141 reputation points">141</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greg has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-53883" class="comments-container">
&#10;</div>
<div id="comment-tools-53883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53883-form-container" class="comment-form-container">
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

