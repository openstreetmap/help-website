+++
type = "question"
title = "How to draw invalid polygons?"
description = '''I want to use Mapnik to draw custom styled maps from OSM. I have used Osmosis to import the Europe extract (from geofabric). I used the database schema with linestrings geometries for ways. Now, for performance and convinience reasons (work in QGIS) I want to build materialized views for polygon fea...'''
date = "2016-06-29T09:01:00Z"
lastmod = "2016-06-29T14:27:00Z"
weight = 50517
keywords = [ "data", "postgresql", "postgis" ]
aliases = [ "/questions/50517" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to draw invalid polygons?](/questions/50517/how-to-draw-invalid-polygons)

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
<span id="post-50517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50517-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use Mapnik to draw custom styled maps from OSM. I have used Osmosis to import the Europe extract (from geofabric). I used the database schema with linestrings geometries for ways. Now, for performance and convinience reasons (work in QGIS) I want to build materialized views for polygon features, such as water areas. So, for example, for riverbanks I am trying something like this:</p>
<pre><code>SELECT st_buildarea(st_collect(w.linestring)) AS geom
FROM relations r
JOIN relation_members rm ON r.id = rm.relation_id AND rm.member_type = &#39;W&#39; AND rm.member_role IN (&#39;outer&#39;, &#39;inner&#39;)
JOIN ways w ON w.id = rm.member_id
WHERE r.tags-&gt;&#39;waterway&#39;=&#39;riverbank&#39;
GROUP BY r.id</code></pre>
<p>And the result is:</p>
<pre><code>LWGEOM_GEOS_buildArea: TopologyException: Input geom 1 is invalid: Self-intersection at or near point 0.68302757542791204 46.349042878781603 at 0.68302757542791204 46.349042878781603</code></pre>
<p>And the PostGIS is right, the relation 1085106 is self-intersecting ("inner" way intersects "outer" way). But OSM got it drawn anyway: <a href="https://www.openstreetmap.org/#map=20/46.34904/0.68303">https://www.openstreetmap.org/#map=20/46.34904/0.68303</a> As far as I know, Mapnik needs polygons, so the official map have to "fix" these data somehow to draw them. How is this done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '16, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d4d477cb8209710d5e5f912f51c78d16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rouen_sk&#39;s gravatar image" />
<p><span>rouen_sk</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rouen_sk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50517" class="comments-container">
<span id="50520"></span>
<div id="comment-50520" class="comment">
<div id="post-50520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why not use osm2pgsql which already does the polygon processing?</p>
</div>
<div id="comment-50520-info" class="comment-info">
<span class="comment-age">(29 Jun '16, 14:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

