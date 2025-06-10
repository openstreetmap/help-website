+++
type = "question"
title = "Postgis Plugin: ERROR: COALESCE types text and integer cannot be matched"
description = '''Hello every body, I am installing a OSM tile server under Strech and I am in trouble : when I run service renderd status I have : ● renderd.service - LSB: Mapnik rendering daemon Loaded: loaded (/etc/init.d/renderd; generated; vendor preset: enabled) Active: active (running) since Thu 2018-11-22 15:...'''
date = "2018-11-22T05:15:00Z"
lastmod = "2018-11-22T05:15:00Z"
weight = 66887
keywords = [ "renderd", "osm2pgsql" ]
aliases = [ "/questions/66887" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Postgis Plugin: ERROR: COALESCE types text and integer cannot be matched](/questions/66887/postgis-plugin-error-coalesce-types-text-and-integer-cannot-be-matched)

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
<span id="post-66887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello every body,</p>
<p>I am installing a OSM tile server under Strech and I am in trouble : when I run service renderd status I have :</p>
<p>● renderd.service - LSB: Mapnik rendering daemon</p>
<p>Loaded: loaded (/etc/init.d/renderd; generated; vendor preset: enabled)</p>
<p>Active: active (running) since Thu 2018-11-22 15:21:30 +11; 3s ago</p>
<pre><code> Docs: man:systemd-sysv-generator(8)</code></pre>
<p>Process: 20598 ExecStop=/etc/init.d/renderd stop (code=exited, status=0/SUCCESS)</p>
<p>Process: 20704 ExecStart=/etc/init.d/renderd start (code=exited, status=0/SUCCESS)</p>
<pre><code>Tasks: 4 (limit: 4915)</code></pre>
<p>CGroup: /system.slice/renderd.service</p>
<pre><code>       └─20711 /usr/local/bin/renderd -c /usr/local/etc/renderd.conf</code></pre>
<p>nov. 22 15:21:30 carto renderd[20710]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Regular.ttf</p>
<p>nov. 22 15:21:30 carto renderd[20710]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf</p>
<p>nov. 22 15:21:30 carto renderd[20710]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Regular.ttf</p>
<p>nov. 22 15:21:30 carto renderd[20704]: Starting Mapnik rendering daemon: renderd.</p>
<p>nov. 22 15:21:30 carto systemd[1]: Started LSB: Mapnik rendering daemon.</p>
<p>nov. 22 15:21:30 carto renderd[20711]: Starting stats thread</p>
<p>nov. 22 15:21:30 carto renderd[20711]: Loading parameterization function for</p>
<p>nov. 22 15:21:30 carto renderd[20711]: Loading parameterization function for</p>
<p>nov. 22 15:21:31 carto renderd[20711]: An error occurred while loading the map layer 'default': Postgis Plugin: ERREUR: les COALESCE types text et integer ne peuvent pas correspondre</p>
<pre><code>                                   LINE 18:   ORDER BY COALESCE(layer,0), way_area DESC
                                                                      ^
                                   in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
&#10;                                       way,
&#10;                                       &quot;natural&quot;,
&#10;                                       waterway,
&#10;                                       landuse,
&#10;                                       name,
&#10;                                       way_area/NULLIF(0::real*0::real,0) AS way_pixels,</code></pre>
<p>To import the data I have tried :</p>
<p>osm2pgsql -d osm --hstore --slim --cache 1000 --number-processes 2 new-caledonia-latest.osm.pbf</p>
<p>and</p>
<p>osm2pgsql -d osm --hstore --slim --cache 1000 --number-processes 2 -S /home/data/osm/styles/openstreetmap-carto/openstreetmap-carto.style --tag-transform-script /home/data/osm/styles/openstreetmap-carto/openstreetmap-carto.lua /home/data/osm/dumps/new-caledonia-latest.osm.pbf</p>
<p>But both are not working</p>
<p>Any ideas ? Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '18, 05:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c678c5c86456016f2fffb941f31d8818?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brunogee&#39;s gravatar image" />
<p><span>brunogee</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brunogee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66887" class="comments-container">
&#10;</div>
<div id="comment-tools-66887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66887-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

