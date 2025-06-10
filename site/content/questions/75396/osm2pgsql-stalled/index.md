+++
type = "question"
title = "osm2pgsql stalled"
description = '''Below is the stalled process $ osm2pgsql -a --slim -e10-15 -d gis --flat-nodes /var/data/flat_nodes.bin --cache 2000 --number-processes 8 -G --hstore --tag-transform-script /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/postgresql/osm/openstreetmap-carto/openstreetmap...'''
date = "2020-06-22T14:13:00Z"
lastmod = "2020-06-24T06:36:00Z"
weight = 75396
keywords = [ "osm", "osm2pgsql" ]
aliases = [ "/questions/75396" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql stalled](/questions/75396/osm2pgsql-stalled)

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
<span id="post-75396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75396-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Below is the stalled process<br />
</p>
<p>$ osm2pgsql -a --slim -e10-15 -d gis --flat-nodes /var/data/flat_nodes.bin --cache 2000 --number-processes 8 -G --hstore --tag-transform-script /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.style --multi-geometry -o /var/lib/mod_tile/dirty_tiles.19005 /var/lib/mod_tile/changes.osc.gz</p>
<p>$ /usr/local/bin/osm2pgsql --version<br />
osm2pgsql version 0.96.0 (64 bit id space)<br />
Compiled using the following library versions:<br />
Libosmium 2.14.2<br />
Lua 5.2.4<br />
</p>
<p>============================================================================</p>
<p>osm2pgsql stalled at below line since two days. Please help.</p>
<p>$ tail osm2pgsql.log<br />
Large polygon (97346 x 61883 metres, OSM ID -956714) - only expiring perimeter<br />
Large polygon (97346 x 61883 metres, OSM ID -956714) - only expiring perimeter<br />
Large polygon (52394 x 48081 metres, OSM ID -961523) - only expiring perimeter<br />
Large polygon (52394 x 48081 metres, OSM ID -961523) - only expiring perimeter<br />
Large polygon (50878 x 50663 metres, OSM ID -968952) - only expiring perimeter<br />
Large polygon (50878 x 50663 metres, OSM ID -968952) - only expiring perimeter<br />
Large polygon (118902 x 77508 metres, OSM ID -971999) - only expiring perimeter<br />
Large polygon (24708 x 28965 metres, OSM ID -971999) - only expiring perimeter<br />
Large polygon (81901 x 54346 metres, OSM ID -971999) - only expiring perimeter<br />
Large polygon (99888 x 62677 metres, OSM ID -971999) - only expiring perimeter<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '20, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '20, 06:24</strong> </span></p>
</div>
</div>
<div id="comments-container-75396" class="comments-container">
<span id="75397"></span>
<div id="comment-75397" class="comment">
<div id="post-75397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What were you using it to do? It looks like it's expiring tiles, but much more information is needed before anyone can take a guess about what the problem might be.</p>
</div>
<div id="comment-75397-info" class="comment-info">
<span class="comment-age">(22 Jun '20, 14:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="75399"></span>
<div id="comment-75399" class="comment">
<div id="post-75399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is triggered through a crontab task which runs everyday and updates the Tile server. It has been running fine since many months but suddenly it stalled.</p>
</div>
<div id="comment-75399-info" class="comment-info">
<span class="comment-age">(22 Jun '20, 14:22)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="75401"></span>
<div id="comment-75401" class="comment">
<div id="post-75401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it safe to upgrade osm2pgsql ? I had setup this server around 2 years back.</p>
</div>
<div id="comment-75401-info" class="comment-info">
<span class="comment-age">(22 Jun '20, 14:34)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="75402"></span>
<div id="comment-75402" class="comment">
<div id="post-75402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which command, with which options, was run via crontab? How much data were you trying to process? What tile zoom levels were you trying to expire?</p>
<p>To answer the other question, a later version of the same branch of osm2pgsql should be compatible with previous versions (apart from caveats around, say, old-style multipolygons). If you're consuming "normal" OSM data it shouldn't be a problem.</p>
</div>
<div id="comment-75402-info" class="comment-info">
<span class="comment-age">(22 Jun '20, 15:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="75427"></span>
<div id="comment-75427" class="comment">
<div id="post-75427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Below is the stalled process:</p>
<p>$ osm2pgsql -a --slim -e10-15 -d gis --flat-nodes /var/data/flat_nodes.bin --cache 2000 --number-processes 8 -G --hstore --tag-transform-script /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.style --multi-geometry -o /var/lib/mod_tile/dirty_tiles.19005 /var/lib/mod_tile/changes.osc.gz</p>
<p>More details:<br />
maxInterval = 259200<br />
baseUrl=<a href="https://planet.openstreetmap.org/replication/minute">https://planet.openstreetmap.org/replication/minute</a><br />
</p>
</div>
<div id="comment-75427-info" class="comment-info">
<span class="comment-age">(24 Jun '20, 06:36)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
</div>
<div id="comment-tools-75396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75396-form-container" class="comment-form-container">
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

<span id="75398"></span>

<div id="answer-container-75398" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75398-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="augustusj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely a problem with osm2pgsql's handling of complex multipolygons. If you can, upgrade to osm2pgsql 1.2 and the latest osmium version for building it, that should solve the issue.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '20, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-75398" class="comments-container">
&#10;</div>
<div id="comment-tools-75398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75398-form-container" class="comment-form-container">
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

