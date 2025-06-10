+++
type = "question"
title = "ogr2ogr: convert all closed ways to polygons?"
description = '''I&#x27;m converting an extracted chunk of OSM data to GeoJSON. We can use GDL ogr2ogr commands like: ogr2ogr -f GeoJSON tmp_lines.geojson tmp_osm-solar-withreferenced.pbf lines ogr2ogr -f GeoJSON tmp_mpoly.geojson tmp_osm-solar-withreferenced.pbf multipolygons  By default, ogr2ogr doesn&#x27;t automatically c...'''
date = "2020-04-29T09:27:00Z"
lastmod = "2020-04-29T12:22:00Z"
weight = 74467
keywords = [ "osmtogeojson", "ogr2ogr", "geojson" ]
aliases = [ "/questions/74467" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ogr2ogr: convert all closed ways to polygons?](/questions/74467/ogr2ogr-convert-all-closed-ways-to-polygons)

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
<span id="post-74467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74467-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm converting an extracted chunk of OSM data to GeoJSON. We can use GDL ogr2ogr commands like:</p>
<pre><code>ogr2ogr -f GeoJSON tmp_lines.geojson tmp_osm-solar-withreferenced.pbf lines
ogr2ogr -f GeoJSON tmp_mpoly.geojson tmp_osm-solar-withreferenced.pbf multipolygons</code></pre>
<p>By default, ogr2ogr doesn't automatically convert all closed ways into polygons, only ones with certain tags which can be <a href="https://github.com/OSGeo/gdal/blob/master/gdal/data/osmconf.ini#L7">defined in osmconf.ini</a>. The default is:</p>
<pre><code>closed_ways_are_polygons=aeroway,amenity,boundary,building,craft,geological,historic,landuse,leisure,military,natural,office,place,shop,sport,tourism,highway=platform,public_transport=platform</code></pre>
<p>How can I tell ogr2ogr that I want <strong>ALL</strong> closed ways to be treated as polygons? I know it's not always advisable in general, but in my case it's what I want, and especially I want un-tagged ways to handled like this. The <code>closed_ways_are_polygons</code> flag only seems to accept an explicit list.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmtogeojson" rel="tag" title="see questions tagged &#39;osmtogeojson&#39;">osmtogeojson</span> <span class="post-tag tag-link-ogr2ogr" rel="tag" title="see questions tagged &#39;ogr2ogr&#39;">ogr2ogr</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '20, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/cb99b2abaa73502ace0175863ca12b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcld&#39;s gravatar image" />
<p><span>mcld</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74467" class="comments-container">
&#10;</div>
<div id="comment-tools-74467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74467-form-container" class="comment-form-container">
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

<span id="74474"></span>

<div id="answer-container-74474" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74474-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mcld has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like you can't (the implementation just explicitly checks the listed keys):</p>
<p><a href="https://github.com/OSGeo/gdal/blob/5870c3fc8ccc05ead6b9c8a5dd9fad76969fd890/gdal/ogr/ogrsf_frmts/osm/ogrosmdatasource.cpp#L1895">https://github.com/OSGeo/gdal/blob/5870c3fc8ccc05ead6b9c8a5dd9fad76969fd890/gdal/ogr/ogrsf_frmts/osm/ogrosmdatasource.cpp#L1895</a></p>
<p>I imagine post processing the GeoJSON is going to be the easiest way to get what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '20, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-74474" class="comments-container">
&#10;</div>
<div id="comment-tools-74474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74474-form-container" class="comment-form-container">
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

