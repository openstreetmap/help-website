+++
type = "question"
title = "How to specify multiple style file with osm2pgsql query"
description = '''I have imported entire planet data using the following query. sudo osm2pgsql --drop --hstore --slim -r pbf -C 32000 --flat-nodes node.cache --number-processes 8 -d gis -U root /mnt/data/planetdata/planet-latest.osm.pbf  But whenever I am testing rendered using- renderd -f -c /usr/local/etc/renderd.c...'''
date = "2018-07-09T15:16:00Z"
lastmod = "2018-07-10T06:32:00Z"
weight = 64602
keywords = [ "openstreetmap-carto", "mapbox_osm-bright", "renderd", "osm", "osm2pgsql" ]
aliases = [ "/questions/64602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to specify multiple style file with osm2pgsql query](/questions/64602/how-to-specify-multiple-style-file-with-osm2pgsql-query)

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
<span id="post-64602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have imported entire planet data using the following query.</p>
<pre><code>sudo osm2pgsql --drop --hstore --slim -r pbf -C 32000 --flat-nodes node.cache --number-processes 8 -d gis -U root /mnt/data/planetdata/planet-latest.osm.pbf</code></pre>
<p>But whenever I am testing rendered using-</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>It is logging the following errors-</p>
<pre><code>renderd[17978]: An error occurred while loading the map layer &#39;osm&#39;: Postgis Plugin: ERROR:  COALESCE types text and integer cannot be matched
LINE 18:   ORDER BY COALESCE(layer,0), way_area DESC
                               ^
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
way,
&quot;natural&quot;,
waterway,
landuse,
name,
way_area/NULLIF(0::real*0::real,0) AS way_pixels,
CASE WHEN tags-&gt;&#39;intermittent&#39; IN (&#39;yes&#39;)
  OR tags-&gt;&#39;seasonal&#39; IN (&#39;yes&#39;, &#39;spring&#39;, &#39;summer&#39;, &#39;autumn&#39;, &#39;winter&#39;, &#39;wet_season&#39;, &#39;dry_season&#39;)
  THEN &#39;yes&#39; ELSE &#39;no&#39; END AS int_intermittent
FROM planet_osm_polygon
WHERE
(waterway IN (&#39;dock&#39;, &#39;riverbank&#39;)
  OR landuse IN (&#39;reservoir&#39;, &#39;basin&#39;)
  OR &quot;natural&quot; IN (&#39;water&#39;, &#39;glacier&#39;))
AND building IS NULL
AND way_area &gt; 1*0::real*0::real
ORDER BY COALESCE(layer,0), way_area DESC
) AS water_areas LIMIT 0&#39;
encountered during parsing of layer &#39;water-areas&#39; in Layer at line 8298 of 
&#39;/mnt/data/styles/osm/openstreetmap-carto-master/osm.xml&#39;
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[17978]: Loading parameterization function for 
renderd[17978]: An error occurred while loading the map layer &#39;osm&#39;: Postgis Plugin: ERROR:  COALESCE 
types text and integer cannot be matched
LINE 18:   ORDER BY COALESCE(layer,0), way_area DESC
                               ^
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
way,
&quot;natural&quot;,
waterway,
landuse,
name,
way_area/NULLIF(0::real*0::real,0) AS way_pixels,
CASE WHEN tags-&gt;&#39;intermittent&#39; IN (&#39;yes&#39;)
  OR tags-&gt;&#39;seasonal&#39; IN (&#39;yes&#39;, &#39;spring&#39;, &#39;summer&#39;, &#39;autumn&#39;, &#39;winter&#39;, &#39;wet_season&#39;, &#39;dry_season&#39;)
  THEN &#39;yes&#39; ELSE &#39;no&#39; END AS int_intermittent
FROM planet_osm_polygon
WHERE
(waterway IN (&#39;dock&#39;, &#39;riverbank&#39;)
  OR landuse IN (&#39;reservoir&#39;, &#39;basin&#39;)
  OR &quot;natural&quot; IN (&#39;water&#39;, &#39;glacier&#39;))
AND building IS NULL
AND way_area &gt; 1*0::real*0::real
ORDER BY COALESCE(layer,0), way_area DESC
) AS water_areas LIMIT 0&#39;
encountered during parsing of layer &#39;water-areas&#39; in Layer at line 8298 of 
&#39;/mnt/data/styles/osm/openstreetmap-carto-master/osm.xml&#39;</code></pre>
<p>When I googled for this error.I found a this link referencing the same issue- <a href="https://github.com/kosmtik/kosmtik/issues/256">link</a></p>
<p>But I am using style from openstreetmap-carto-master and mapbox-carto(osm-bright) both.</p>
<p>openstreetmap-carto-master - <a href="https://github.com/gravitystorm/openstreetmap-carto/archive/master.zip">link</a></p>
<p>mapbox-carto - <a href="https://github.com/mapbox/osm-bright/archive/master.zip">link</a></p>
<p>So, In my case how can I specify two style file in my query? Or How can I solve this issue?</p>
<p>If anyone have solved this issue ,please let me know.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-mapbox_osm-bright" rel="tag" title="see questions tagged &#39;mapbox_osm-bright&#39;">mapbox_osm-bright</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '18, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '18, 11:34</strong> </span></p>
</div>
</div>
<div id="comments-container-64602" class="comments-container">
<span id="64606"></span>
<div id="comment-64606" class="comment">
<div id="post-64606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what you mean by "I am using style from openstreetmap-carto-master and maknik-carto both"? Can you link to both styles?</p>
</div>
<div id="comment-64606-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 16:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64608"></span>
<div id="comment-64608" class="comment">
<div id="post-64608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean my tileserver can supply multiple carto styles as base map.</p>
</div>
<div id="comment-64608-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 16:59)</span> <span class="comment-user userinfo">anuranpal</span>
</div>
</div>
<span id="64610"></span>
<div id="comment-64610" class="comment">
<div id="post-64610-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you link to both styles? That'll help people tell if they can share a database or not.</p>
</div>
<div id="comment-64610-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 17:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64622"></span>
<div id="comment-64622" class="comment">
<div id="post-64622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have updated the question. <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
</div>
<div id="comment-64622-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 06:32)</span> <span class="comment-user userinfo">anuranpal</span>
</div>
</div>
</div>
<div id="comment-tools-64602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

