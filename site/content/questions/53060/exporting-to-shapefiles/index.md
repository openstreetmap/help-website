+++
type = "question"
title = "exporting to shapefiles"
description = '''I want to export powerline location information for Oman that I see in OpenStreetMap as shapefiles. How do I do that. Those powerlines do not seem to be in the gcc-latest-free.shp files available at Geofabrik downloads.'''
date = "2016-11-21T21:18:00Z"
lastmod = "2016-12-04T05:35:00Z"
weight = 53060
keywords = [ "shapefile", "export" ]
aliases = [ "/questions/53060" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [exporting to shapefiles](/questions/53060/exporting-to-shapefiles)

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
<span id="post-53060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53060-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to export powerline location information for Oman that I see in OpenStreetMap as shapefiles. How do I do that. Those powerlines do not seem to be in the gcc-latest-free.shp files available at Geofabrik downloads.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '16, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1cddf3e689b6d0239e07cf264240885f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="McGradyM&#39;s gravatar image" />
<p><span>McGradyM</span><br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="McGradyM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53060" class="comments-container">
&#10;</div>
<div id="comment-tools-53060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53060-form-container" class="comment-form-container">
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

<span id="53062"></span>

<div id="answer-container-53062" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53062-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A simple way to do this is using Overpass Turbo. For example, <a href="http://overpass-turbo.eu/s/keu">this query</a> was generated using the Assistant and typing "power=tower in Oman". You can easily adapt the query to get the lines themselves. Just <a href="https://wiki.openstreetmap.org/wiki/Power_lines">check the wiki</a> to see what exactly you need. You can then export the data to GeoJSON, which you can drag and drop to QGIS. If you really want to use shapefiles, you can simply save as shapefile in QGIS. There is built in support in QGIS (and also the QuickOSM plugin) to do the same without going over a website.</p>
<p>Of course, if you want to do something more advanced, Jochen's answer is more interesting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '16, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-53062" class="comments-container">
<span id="53067"></span>
<div id="comment-53067" class="comment">
<div id="post-53067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK. Thanks. Maybe I am missing something obvious and easy. The map key in OSM says that the power lines they show are "cable cars or chair lifts", so maybe the available shape files are named as such. Anyway, between the two answers, I've got a number of ways forward. Thanks</p>
</div>
<div id="comment-53067-info" class="comment-info">
<span class="comment-age">(22 Nov '16, 10:34)</span> <span class="comment-user userinfo">McGradyM</span>
</div>
</div>
<span id="53097"></span>
<div id="comment-53097" class="comment">
<div id="post-53097-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah, our map key is far from perfect. Ski lifts actually do look like that, it's just that power lines are missing in the map key. There is way more visualized on the map than could fit in a normal sized map key. If you want to know what kind of thing you see on the map, you can try clicking on it with the question mark button (below the map key button). What I do more often is click "Map data" in the Layers button. Then all objects become clickable. With either option, you can then see the raw data behind the thing you see on the map. Then hit the wiki to learn more about it.</p>
</div>
<div id="comment-53097-info" class="comment-info">
<span class="comment-age">(24 Nov '16, 13:49)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="53126"></span>
<div id="comment-53126" class="comment">
<div id="post-53126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. That helps.</p>
</div>
<div id="comment-53126-info" class="comment-info">
<span class="comment-age">(26 Nov '16, 10:43)</span> <span class="comment-user userinfo">McGradyM</span>
</div>
</div>
</div>
<div id="comment-tools-53062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53062-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53061"></span>

<div id="answer-container-53061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53061-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many ways of doing this, they all have their advantages and disadvantages. A lot depends on the amount of data you are dealing with (whole planet vs. small extract) and the system and skills you have. If you are familiar with SQL/PostGIS, for instance, you can use one of the PostGIS importers (like osm2pgsql or imposm) to import OSM data into a PostGIS database and then export into Shapefiles. If you like command lines, try ogr2ogr. If you need something more custom and know C++, you can write your own exporter based on <a href="https://github.com/osmcode/osm-gis-export.">https://github.com/osmcode/osm-gis-export.</a> For smaller files, you can build something with use node-osmium, see the demo here: <a href="https://github.com/osmcode/node-osmium/tree/master/demo/converter.">https://github.com/osmcode/node-osmium/tree/master/demo/converter.</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Shapefiles">https://wiki.openstreetmap.org/wiki/Shapefiles</a> has more options.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '16, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-53061" class="comments-container">
<span id="53066"></span>
<div id="comment-53066" class="comment">
<div id="post-53066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I'll probably nose around some more, and end up asking someone with more skill. That would be the fastest.</p>
</div>
<div id="comment-53066-info" class="comment-info">
<span class="comment-age">(22 Nov '16, 10:30)</span> <span class="comment-user userinfo">McGradyM</span>
</div>
</div>
</div>
<div id="comment-tools-53061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53061-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53235"></span>

<div id="answer-container-53235" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53235-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A little bit more explanation to <a href="https://help.openstreetmap.org/users/2850/joostenmies">@joost</a>-schouppe answer. First you need to find out "Oman" or any other region's OSM relation id.</p>
<p>Use this query in Overpass Turbo</p>
<pre><code>[out:json][timeout:900];
// get a few areas into .myArea
// you can add or remove an area by simply adding or removing
// one line here.
&#10;(
{{geocodeArea:&quot;Oman&quot;}};
)-&gt;.myArea;
&#10;// display .myArea This can be replaced by any query
// on the objects in .myArea
&#10;rel(pivot.myArea);
&#10;// print results
out geom;
&#10;{{style:
node{opacity:0;fill-opacity:0}
}}</code></pre>
<p>Now once you know the OSM relation id then you can extract any layer easily with overpass API. OSM relation id for "Oman" is "305138"</p>
<p>Here is curl command to extract power line using <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Area_clauses">Area clause</a> of overpass API</p>
<pre><code>curl \
  -H &quot;Host: overpass-api.de&quot; -H &quot;Content-Type: text/xml&quot;  \
  -d &#39;(relation[&quot;route&quot;=&quot;power&quot;](area:3600305138););(._;&gt;;);out body;&#39;  \
  http://overpass-api.de/api/interpreter  \
  -o powerline.osm</code></pre>
<p>Now you can use <a href="https://wiki.openstreetmap.org/wiki/OGR">ogr2ogr</a> to convert OSM to shapefile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '16, 05:35</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53235" class="comments-container">
&#10;</div>
<div id="comment-tools-53235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53235-form-container" class="comment-form-container">
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

