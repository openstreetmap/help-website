+++
type = "question"
title = "Slow query for landcover layer"
description = '''When I run the specified query for landcover layer from the default.style (z = 8), It takes about half a minute to get the result set, and there are more than 100K records in the result set. Is it supposed to be this slow? here is the query:  SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;landuse&quot;,&quot;military&quot;,&quot;n...'''
date = "2015-11-11T09:04:00Z"
lastmod = "2015-11-11T10:48:00Z"
weight = 46524
keywords = [ "rendering", "default.style", "performance" ]
aliases = [ "/questions/46524" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Slow query for landcover layer](/questions/46524/slow-query-for-landcover-layer)

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
<span id="post-46524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I run the specified query for landcover layer from the default.style (z = 8), It takes about half a minute to get the result set, and there are more than 100K records in the result set.</p>
<p>Is it supposed to be this slow? here is the query:</p>
<pre><code>SELECT ST_AsBinary(&quot;way&quot;) AS geom,&quot;landuse&quot;,&quot;military&quot;,&quot;natural&quot; FROM (select way,aeroway,amenity,landuse,leisure,man_made,military,&quot;natural&quot;,power,tourism,name,highway,
case when religion in (&#39;christian&#39;,&#39;jewish&#39;) then religion else &#39;INT-generic&#39;::text end as religion
from planet_osm_polygon where landuse is not null or leisure is not null or aeroway in (&#39;apron&#39;,&#39;aerodrome&#39;)
or amenity in &#39;parking&#39;,&#39;university&#39;,&#39;college&#39;,&#39;school&#39;,&#39;hospital&#39;,&#39;kindergarten&#39;,&#39;grave_yard&#39;,&#39;prison&#39;) or military in (&#39;barracks&#39;,&#39;danger_area&#39;) or &quot;natural&quot; in (&#39;field&#39;,&#39;beach&#39;,&#39;desert&#39;,&#39;heath&#39;,&#39;mud&#39;,&#39;grassland&#39;,&#39;wood&#39;,&#39;sand&#39;,&#39;scrub&#39;) or power in (&#39;station&#39;,&#39;sub_station&#39;,&#39;generator&#39;) or tourism in (&#39;attraction&#39;,&#39;camp_site&#39;,&#39;caravan_site&#39;,&#39;picnic_site&#39;,&#39;zoo&#39;) or highway in (&#39;services&#39;,&#39;rest_area&#39;)  order by z_order,way_area desc) as leisure WHERE &quot;way&quot; &amp;&amp; ST_SetSRID(&#39;BOX3D(-90.35156250000171 40.71395582622718,-84.02343749999829 45.33670190991032)&#39;::box3d, 4326)</code></pre>
<p>and here is the explain analyze of the same query</p>
<pre><code>Subquery Scan on leisure  (cost=660012.22..666569.32 rows=119220 width=288) (actual time=795.469..963.086 rows=109992 loops=1)  
  -&gt;  Sort  (cost=660012.22..660310.27 rows=119220 width=383) (actual time=795.434..838.050 rows=109992 loops=1)  
        Sort Key: planet_osm_polygon.z_order, planet_osm_polygon.way_area  
        Sort Method: quicksort  Memory: 66602kB  
          -&gt;  Bitmap Heap Scan on planet_osm_polygon  (cost=6604.80..649960.03 rows=119220 width=383) (actual time=54.657..271.586 rows=109992 loops=1)  
              Recheck Cond: ((way &amp;&amp; &#39;0103000020E6100000010000000500000078000000809656C09A378EE7625B444078000000809656C064C8550C19AB464088FFFFFF7F0155C064C8550C19AB464088FFFFFF7F0155C09A378EE7625B444078000000809656C09A378EE7625B4440&#39;::geometry) AND ((landuse IS NOT NULL) OR (leisure IS NOT NULL) OR (aeroway IS NOT NULL) OR (amenity IS NOT NULL) OR (military IS NOT NULL) OR (&quot;natural&quot; IS NOT NULL) OR (power IS NOT NULL) OR (tourism IS NOT NULL) OR (highway IS NOT NULL)))  
              Filter: ((landuse IS NOT NULL) OR (leisure IS NOT NULL) OR (aeroway = ANY (&#39;{apron,aerodrome}&#39;::text[])) OR (amenity = ANY (&#39;{parking,university,college,school,hospital,kindergarten,grave_yard,prison}&#39;::text[])) OR (military = ANY (&#39;{barracks,danger_area}&#39;::text[])) OR (&quot;natural&quot; = ANY (&#39;{field,beach,desert,heath,mud,grassland,wood,sand,scrub}&#39;::text[])) OR (power = ANY (&#39;{station,sub_station,generator}&#39;::text[])) OR (tourism = ANY (&#39;{attraction,camp_site,caravan_site,picnic_site,zoo}&#39;::text[])) OR (highway = ANY (&#39;{services,rest_area}&#39;::text[])))  
              Rows Removed by Filter: 52924  
              -&gt;  Bitmap Index Scan on planet_osm_polygon_leisure  (cost=0.00..6574.99 rows=177410 width=0) (actual time=36.457..36.457 rows=162916 loops=1)  
                    Index Cond: (way &amp;&amp; &#39;0103000020E6100000010000000500000078000000809656C09A378EE7625B444078000000809656C064C8550C19AB464088FFFFFF7F0155C064C8550C19AB464088FFFFFF7F0155C09A378EE7625B444078000000809656C09A378EE7625B4440&#39;::geometry)  
Total runtime: 986.102 ms</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-default.style" rel="tag" title="see questions tagged &#39;default.style&#39;">default.style</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '15, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '15, 09:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-46524" class="comments-container">
&#10;</div>
<div id="comment-tools-46524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46524-form-container" class="comment-form-container">
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

<span id="46525"></span>

<div id="answer-container-46525" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46525-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="khamooshi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if it is "supposed" to be slow but I can confirm that it usually is. I suggest you do a</p>
<pre><code>CREATE INDEX run_faster_dammit 
   ON planet_osm_polygon 
   USING gist(way) 
   WHERE landuse is not null 
      OR leisure is not null
      OR aeroway in (&#39;apron&#39;,&#39;aerodrome&#39;) 
      OR amenity in (&#39;parking&#39;,&#39;university&#39;,&#39;college&#39;,&#39;school&#39;,&#39;hospital&#39;,&#39;kindergarten&#39;,&#39;grave_yard&#39;,&#39;prison&#39;) 
      OR military in (&#39;barracks&#39;,&#39;danger_area&#39;) 
      OR &quot;natural&quot; in (&#39;field&#39;,&#39;beach&#39;,&#39;desert&#39;,&#39;heath&#39;,&#39;mud&#39;,&#39;grassland&#39;,&#39;wood&#39;,&#39;sand&#39;,&#39;scrub&#39;) 
      OR power in (&#39;station&#39;,&#39;sub_station&#39;,&#39;generator&#39;) 
      OR tourism in (&#39;attraction&#39;,&#39;camp_site&#39;,&#39;caravan_site&#39;,&#39;picnic_site&#39;,&#39;zoo&#39;)
      OR highway in (&#39;services&#39;,&#39;rest_area&#39;);</code></pre>
<p>which will speed things up significantly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '15, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46525" class="comments-container">
<span id="46527"></span>
<div id="comment-46527" class="comment">
<div id="post-46527-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for the answer and your helpful presentation :)(<a href="http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf)">http://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf)</a></p>
<p>It is better now, but still takes few seconds to complete. I think because there are 100K+ records in the result set.</p>
<p>would you send a list of all indexes you added to the database.</p>
</div>
<div id="comment-46527-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 09:55)</span> <span class="comment-user userinfo">khamooshi</span>
</div>
</div>
<span id="46530"></span>
<div id="comment-46530" class="comment">
<div id="post-46530-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, that won't help you because the indexes you need are different depending on the style you are using, and even different versions of the same style will have different queries and therefore need different indexes. Essentially, you use the <code>log_min_duration</code> setting in your postgresql config and then create indexes that mimic exactly the WHERE clause of the slowest queries.</p>
</div>
<div id="comment-46530-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 10:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46525-form-container" class="comment-form-container">
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

