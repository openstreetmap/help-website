+++
type = "question"
title = "Converting shapefile with line layer &amp; point layer to a routable .osm file"
description = '''I&#x27;m working on a project involving historical data, which I&#x27;m wanting to turn into an .osm XML file as a routable network (e.g. using OSRM) and for rendering (using Mapnik/CartoCSS). The data will not be added into OSM. My aim is to convert the Shapefiles into .osm format, and be routable, so that I...'''
date = "2016-05-09T12:42:00Z"
lastmod = "2016-05-10T19:33:00Z"
weight = 49633
keywords = [ "shapefiles", "merging", "osmosis" ]
aliases = [ "/questions/49633" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting shapefile with line layer & point layer to a routable .osm file](/questions/49633/converting-shapefile-with-line-layer-point-layer-to-a-routable-osm-file)

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
<span id="post-49633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a project involving historical data, which I'm wanting to turn into an .osm XML file as a routable network (e.g. using OSRM) and for rendering (using Mapnik/CartoCSS). The data will <strong>not</strong> be added into OSM.</p>
<p>My aim is to convert the Shapefiles into .osm format, and be routable, so that I then get the benefits of the OSM toolsets.</p>
<p>I'm very familiar with OSM and its ecosystem, being a long-time contributor and user. What I'm not so familiar is the GIS world, where a Shapefile (in my case from ArcGIS) has to contain ways and nodes as separate layers.</p>
<p>The main problem I'm having is making the network actually topographically routable.</p>
<p><strong>Can anyone suggest a workflow which would enable the two layers containing lines and junction points to be merged into a single .osm file where the points become nodes actually as properties of the ways?</strong></p>
<p>Currently I am:</p>
<ul>
<li>Taking the Shapefiles from ArcGIS; there are two shapefiles, one with the lines (for the ways) and one for connected junctions</li>
<li>Using <a href="https://sourceforge.net/p/vectormap2garmin/wiki/ogr2osm/">ogr2osm.py</a> to convert from *.shp to .osm (in WGS84)</li>
<li>Then using Osmosis to transform the tags to OSM standards (e.g. <code>waterway=river</code>)</li>
<li>Then using Osmosis to merge the layers, using <code>osmosis --rx Edges.osm --sort --rx Junctions.osm --sort --merge --wx merged.osm</code></li>
<li>Building with OSRM as a proof of routability</li>
<li>Rendering in Mapnik as a proof of data presence. This does confirm that the network is all present and in the right projection.</li>
</ul>
<p>The routability partly works - stretches of route do route, but where there are junctions, the routability stops.</p>
<p>My clear hunch is that the .osm data contains all the ways and nodes but that the ways themselves do not reference the nodes.</p>
<p><strong>Is there some adjustment or different toolchain I could use the merge the two layers properly rather than treat them as two sets of items in the one .osm file?</strong> I'm trying to avoid having to pick through and modify XML directly, which will not fun.</p>
<p>Any pointers would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefiles" rel="tag" title="see questions tagged &#39;shapefiles&#39;">shapefiles</span> <span class="post-tag tag-link-merging" rel="tag" title="see questions tagged &#39;merging&#39;">merging</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '16, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/354d4e3cc1b448abb29eb4f1bbac395c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooquency&#39;s gravatar image" />
<p><span>fooquency</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooquency has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '16, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-49633" class="comments-container">
<span id="49637"></span>
<div id="comment-49637" class="comment">
<div id="post-49637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you elaborate on the role of the "points" shape file. Since the "lines" file will already contain geometries for each road, and could be turned into a routable file by unrolling these geometries into OSM ways and nodes, what purpose does the "points" file have?</p>
</div>
<div id="comment-49637-info" class="comment-info">
<span class="comment-age">(09 May '16, 16:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="49639"></span>
<div id="comment-49639" class="comment">
<div id="post-49639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The points file was created to have the actual junctions in, as distinct from places where the lines simply cross over (e.g. a bridge). However, I will check on whether this is actually needed. I think we previously tried just the lines file and that didn't give us a properly-routable network.</p>
</div>
<div id="comment-49639-info" class="comment-info">
<span class="comment-age">(09 May '16, 16:27)</span> <span class="comment-user userinfo">fooquency</span>
</div>
</div>
<span id="49649"></span>
<div id="comment-49649" class="comment">
<div id="post-49649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems this has worked. Thanks again, Frederik. Turns out the main issue was that I'd chosen highway=motorway in the Osmosis tag conversion, resulting in lots of implied one ways in the router.</p>
</div>
<div id="comment-49649-info" class="comment-info">
<span class="comment-age">(10 May '16, 19:33)</span> <span class="comment-user userinfo">fooquency</span>
</div>
</div>
</div>
<div id="comment-tools-49633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49633-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

