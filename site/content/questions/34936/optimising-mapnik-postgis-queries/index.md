+++
type = "question"
title = "Optimising Mapnik PostGIS queries"
description = '''In my Mapnik stylesheet, I have a number of PostGIS queries like this: SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;highway&quot;,&quot;ref&quot; FROM (   SELECT way, highway, ref FROM planet_osm_line  WHERE highway IN (&#x27;motorway&#x27;,&#x27;trunk&#x27;,&#x27;motorway_link&#x27;,&#x27;trunk_link&#x27;,&#x27;primary&#x27;,&#x27;primary_link&#x27;)  ORDER BY z_order ) AS data WHE...'''
date = "2014-07-16T23:39:00Z"
lastmod = "2014-07-16T23:39:00Z"
weight = 34936
keywords = [ "performance", "mapnik", "postgis" ]
aliases = [ "/questions/34936" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Optimising Mapnik PostGIS queries](/questions/34936/optimising-mapnik-postgis-queries)

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
<span id="post-34936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34936-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-34936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my Mapnik stylesheet, I have a number of PostGIS queries like this:</p>
<p><code>SELECT ST_AsBinary("way") AS geom,"highway","ref" FROM ( SELECT way, highway, ref FROM planet_osm_line WHERE highway IN ('motorway','trunk','motorway_link','trunk_link','primary','primary_link') ORDER BY z_order ) AS data WHERE "way" &amp;&amp; ST_SetSRID('BOX3D(616388.1960919927 5938851.34964824,792499.1092611345 6114962.262817382)'::box3d, 900913);</code></p>
<p>I can partly optimise this by creating an index on <code>way</code> and <code>highway</code>:</p>
<p><code>CREATE INDEX geo_z11 ON planet_osm_line USING gist(way) WHERE highway IN ('motorway','trunk','motorway_link','trunk_link','primary','primary_link')</code></p>
<p>However, the <code>ORDER BY z_order</code> is still slow, particularly in metatiles with large amounts of data.</p>
<p>Ideally I would like to change the index to <code>USING GIST(way, z_order ASC) WHERE...</code>. Unfortunately the btree_gist extension (required for this) doesn't support ASC/DESC.</p>
<p>Are there any other ways to speed the sorting?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '14, 23:39</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-34936" class="comments-container">
&#10;</div>
<div id="comment-tools-34936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34936-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

