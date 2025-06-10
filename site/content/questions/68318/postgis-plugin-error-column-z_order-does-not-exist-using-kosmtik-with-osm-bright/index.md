+++
type = "question"
title = "Postgis Plugin: ERROR:  column &quot;z_order&quot; does not exist - Using Kosmtik with OSM Bright"
description = '''I am trying to create a customized map style with CartoCSS. Originally I was using Kosmtik with the default openstreetmap-carto style, following this tutorial. I was able to set it up and change some styles. I decided to switch to OSM Bright since it is much more lightweight than openstreetmap-carto...'''
date = "2019-03-07T15:01:00Z"
lastmod = "2019-03-07T15:01:00Z"
weight = 68318
keywords = [ "openstreetmap-carto", "mapbox_osm-bright", "osm", "kosmtik", "mapnik" ]
aliases = [ "/questions/68318" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Postgis Plugin: ERROR: column "z_order" does not exist - Using Kosmtik with OSM Bright](/questions/68318/postgis-plugin-error-column-z_order-does-not-exist-using-kosmtik-with-osm-bright)

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
<span id="post-68318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68318-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a customized map style with CartoCSS.</p>
<p>Originally I was using Kosmtik with the default openstreetmap-carto style, following <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">this tutorial</a>. I was able to set it up and change some styles. I decided to switch to OSM Bright since it is much more lightweight than openstreetmap-carto and a better starting point for creating a custom style.</p>
<p>After setting up OSM Bright, when I launch kosmtik, I get the following error:</p>
<pre><code>Trace
    at ProjectServer.raise (/home/renderaccount/src/kosmtik/src/back/ProjectServer.js:267:13)
    at /home/renderaccount/src/kosmtik/src/back/ProjectServer.js:81:30
    at /home/renderaccount/src/kosmtik/node_modules/generic-pool/lib/generic-pool.js:283:11
    at loaded (/home/renderaccount/src/kosmtik/node_modules/mapnik-pool/index.js:23:37)
Postgis Plugin: ERROR:  column &quot;z_order&quot; does not exist
LINE 1: SELECT * FROM ( SELECT way, place AS type, name, z_order, po...
                                                         ^
in executeQuery Full sql was: &#39;SELECT * FROM ( SELECT way, place AS type, name, z_order, population
  FROM planet_osm_point
  WHERE place in (&#39;country&#39;, &#39;state&#39;, &#39;city&#39;, &#39;town&#39;, &#39;village&#39;, &#39;hamlet&#39;, &#39;suburb&#39;, &#39;neighbourhood&#39;, &#39;locality&#39;)
  ORDER BY population DESC NULLS LAST
) AS data LIMIT 0&#39;
  encountered during parsing of layer &#39;place&#39; in Layer</code></pre>
<p>I'm not sure why <code>z_order</code> does not exist. Again, I followed <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">this tutorial</a> by switch2osm to initially set up my tile server.</p>
<p>What should I do to solve this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-mapbox_osm-bright" rel="tag" title="see questions tagged &#39;mapbox_osm-bright&#39;">mapbox_osm-bright</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-kosmtik" rel="tag" title="see questions tagged &#39;kosmtik&#39;">kosmtik</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '19, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68318" class="comments-container">
&#10;</div>
<div id="comment-tools-68318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68318-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

