+++
type = "question"
title = "How to find the polygon?"
description = '''I have a PostGIS database in the &quot;Osm2pgsql/schema&quot;. I get a 7 rows when I query the planet_osm_polygon table with this: select * from planet_osm_polygon where boundary=&#x27;administrative&#x27; and admin_level = &#x27;2&#x27; and name = &#x27;Deutschland&#x27; Only 3 of them have a geometry. Unfortunately none of them is the b...'''
date = "2012-05-30T14:50:00Z"
lastmod = "2012-05-31T10:17:00Z"
weight = 13124
keywords = [ "geometry", "postgresql", "osm2pgsql", "postgis", "polygon" ]
aliases = [ "/questions/13124" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find the polygon?](/questions/13124/how-to-find-the-polygon)

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
<span id="post-13124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a PostGIS database in the "Osm2pgsql/schema".</p>
<p>I get a 7 rows when I query the <code>planet_osm_polygon</code> table with this:</p>
<p><code>select * from planet_osm_polygon where boundary='administrative' and admin_level = '2' and name = 'Deutschland'</code></p>
<p>Only 3 of them have a geometry. Unfortunately none of them is the big Germany polygon. They are all enclaves in Belgium or Switzerland. Every single on has an way_area (real type) information. Should I work with this? How?</p>
<p>Or what am I doing wrong? If I do the same for states in Germany, I can't find a single state polygon :(</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '12, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/49f0c5218671e039c889fc520ea55a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="np00&#39;s gravatar image" />
<p><span>np00</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="np00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13124" class="comments-container">
&#10;</div>
<div id="comment-tools-13124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13124-form-container" class="comment-form-container">
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

<span id="13147"></span>

<div id="answer-container-13147" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="np00 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM, polygons, especially large ones, often break because someone makes a small edit somewhere that causes the boundary to be incomplete or self-intersecting, and osm2pgsql may not then be able to build the geometry. It is also possible that the data extract you were using did non contain everything required to build the boundary.</p>
<p>Depending on what you need the polygon for, there are various things you could do.</p>
<ul>
<li>try a different importer, e.g. imposm</li>
<li>use a different data processing toolchain altogehter, e.g. osmjs which also builds polygons for you</li>
<li>manually retrieve the relation (use a search engine to find "osm relation germany", then issue an API call for /relation/1234/full, then post-process the resulting data - again, depending on what your use case is, perhaps with rel2poly/poly2wkt or something</li>
<li>use a third-party web site that assembles relations for you, e.g. for the area of Germany try ags.misterboo.de where you can download any boundary as GeoJSON.</li>
</ul>
<p>Having said that, on my osm2pgsql-imported database I get exactly one result for e.g. "admin_level='4' and name='Bayern'", and for "admin_level='2' and boundary='administrative' and name='Deutschland'" I get the following list:</p>
<pre><code> osm_id | way_area 
--------+----------
 -51477 |  49.2627
 -51477 | 0.001543
 -51477 | 0.000241
 -51477 | 0.000123
 -51477 |    2e-06
 -51477 | 0.001275
 -51477 | 0.000915</code></pre>
<p>Indeed the way_area column can be used as an indicator which of those is the "big Germany polygon".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '12, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13147" class="comments-container">
&#10;</div>
<div id="comment-tools-13147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13147-form-container" class="comment-form-container">
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

