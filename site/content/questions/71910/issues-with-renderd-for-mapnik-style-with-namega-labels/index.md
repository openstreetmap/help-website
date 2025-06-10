+++
type = "question"
title = "issues with renderd for mapnik style with name:ga labels"
description = '''I&#x27;m in the process of rebuilding the maps and overlays for maps.openstreetmap.ie but running into some issues with existing style sheets. I&#x27;ve already done this once in the past year but had to redo it again recently and running into issues. It&#x27;s worth noting that most of the styles are still based ...'''
date = "2019-11-30T18:47:00Z"
lastmod = "2019-12-05T01:36:00Z"
weight = 71910
keywords = [ "openstreetmap-carto", "multilingual", "ireland", "mapnik", "tileserver" ]
aliases = [ "/questions/71910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [issues with renderd for mapnik style with name:ga labels](/questions/71910/issues-with-renderd-for-mapnik-style-with-namega-labels)

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
<span id="post-71910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71910-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm in the process of rebuilding the maps and overlays for maps.openstreetmap.ie but running into some issues with existing style sheets. I've already done this once in the past year but had to redo it again recently and running into issues. It's worth noting that most of the styles are still based on the old XML format (that's what I inherited) and don't use the newer CartoCSS.</p>
<p>I've followed the <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">guide</a> on switch2osm with a view deviations (we have more than 10 layers to render so have compile some things from source).</p>
<p>The style file I used for the import is <a href="https://github.com/osmie/openstreetmapIE/blob/master/osm2pgsql/default.style.IE">here</a>.</p>
<p>The XML renderd config I'm using the for the name:ga map tiles is <a href="https://github.com/osmie/openstreetmapIE/blob/master/mapnik/ireland/osm-ga.xml">here</a></p>
<p>The command line for the initial import I did is as follows:</p>
<pre><code>osm2pgsql   \
  --database gis \
  --create \
  --slim \
  --multi-geometry \
  --hstore \
  --tag-transform-script /data/src/openstreetmap-carto/openstreetmap-carto.lua \
  --cache 2500 \
  --number-processes 1 \
  --style /usr/local/share/osm2pgsql/default.style.IE \
  /home/roles/planet/data/ireland-and-northern-ireland-2019-11-23T21\:19\:02Z.osm.pbf</code></pre>
<p>The errors I'm getting are as follows:</p>
<pre><code>Nov 30 17:32:02 hostname renderd[9961]: An error occurred while loading the map layer &#39;osm-ga&#39;: Postgis Plugin: ERROR:  COALESCE types text and integer cannot be matched#012LINE 18:   ORDER BY COALESCE(layer,0), way_area DESC#012^#012in executeQuery Full sql was: &#39;SELECT * FROM (SELECT#012    way,#012    &quot;natural&quot;,#012    waterway,#012    landuse,#012    COALESCE(tags-&gt;&#39;name:ga&#39;, &#39;&#39;) as name,#012    way_area/NULLIF(0::real*0::real,0) AS way_pixels,#012    CASE WHEN tags-&gt;&#39;intermittent&#39; IN (&#39;yes&#39;)#012      OR tags-&gt;&#39;seasonal&#39; IN (&#39;yes&#39;, &#39;spring&#39;, &#39;summer&#39;, &#39;autumn&#39;, &#39;winter&#39;, &#39;wet_season&#39;, &#39;dry_season&#39;)#012      THEN &#39;yes&#39; ELSE &#39;no&#39; END AS int_intermittent#012  FROM planet_osm_polygon#012  WHERE#012    (waterway IN (&#39;dock&#39;, &#39;riverbank&#39;)#012      OR landuse IN (&#39;reservoir&#39;, &#39;basin&#39;)#012      OR &quot;natural&quot; IN (&#39;water&#39;, &#39;glacier&#39;))#012    AND building IS NULL#012    AND way_area &gt; 1*0::real*0::real#012  ORDER BY COALESCE(layer,0), way_area DESC#012) AS water_areas LIMIT 0&#39;#012  encountered during parsing of layer &#39;water-areas&#39; in Layer at line 8462 of &#39;/data/maps/mapnik/osm-ga.xml&#39;</code></pre>
<p>It specifically seems to be barfing on:</p>
<pre><code>ORDER BY COALESCE(layer,0), way_area) AS water_areas</code></pre>
<p>I'm hoping this is something simple and someone with more experience has encountered this before and can point me in the right direction before I go down the "trial and error" rabbit hole... :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-multilingual" rel="tag" title="see questions tagged &#39;multilingual&#39;">multilingual</span> <span class="post-tag tag-link-ireland" rel="tag" title="see questions tagged &#39;ireland&#39;">ireland</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '19, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/dabc2477fcb5006a22c9eefb48d75b90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d%C3%B3nal&#39;s gravatar image" />
<p><span>dónal</span><br />
<span class="score" title="156 reputation points">156</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dónal has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-71910" class="comments-container">
&#10;</div>
<div id="comment-tools-71910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71910-form-container" class="comment-form-container">
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

<span id="71911"></span>

<div id="answer-container-71911" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71911-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Answering my own question...</p>
<p>This was indeed the issue:</p>
<pre><code>ORDER BY COALESCE(layer,0)</code></pre>
<p>previously it appears the layer column was declared as an int in the osm_line table but nows it's text... Still investigating what caused the change (I may have missed a step somewhere).</p>
<p>I reviewed the XML change and ensured any 0s were enclosed in single quotes.</p>
<p>e.g.</p>
<pre><code>ORDER BY COALESCE(layer,&#39;0&#39;)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '19, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/dabc2477fcb5006a22c9eefb48d75b90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d%C3%B3nal&#39;s gravatar image" />
<p><span>dónal</span><br />
<span class="score" title="156 reputation points">156</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dónal has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '19, 19:41</strong> </span></p>
</div>
</div>
<div id="comments-container-71911" class="comments-container">
<span id="72003"></span>
<div id="comment-72003" class="comment">
<div id="post-72003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've marked your answer as an answer - hope you don't mind!</p>
<p>As an aside - if you did want to deploy a map style "like OpenStreetMap.org standard tiles but with Irish names" it would be relatively straightforward to do that via the lua scripting that osm2pgsql supports. Not that I'm saying that you need to change; but if you did want to, it needn't be that difficult. Let me know if you're thinking about going down that route and would like a nudge in the right direction.</p>
</div>
<div id="comment-72003-info" class="comment-info">
<span class="comment-age">(05 Dec '19, 01:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71911-form-container" class="comment-form-container">
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

