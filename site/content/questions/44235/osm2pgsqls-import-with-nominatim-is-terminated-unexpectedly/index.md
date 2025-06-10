+++
type = "question"
title = "osm2pgsql&#x27;s import with Nominatim is terminated unexpectedly."
description = '''Hi guys! I try to upload a large pbf file(Netherland) from Geofabrik into Nominatim db (with small area import works fine). What I&#x27;m doing: 1)Start this script: ./utils/setup.php --osm-file maps/netherlands-latest.osm.pbf --all --osm2pgsql-cache 6000 2&amp;gt;&amp;amp;1 | tee /opt/Nominatim/setup.log 2) I&#x27;m...'''
date = "2015-07-17T10:34:00Z"
lastmod = "2015-07-17T10:34:00Z"
weight = 44235
keywords = [ "nominatim", "postgresql", "osm2pgsql", "linux" ]
aliases = [ "/questions/44235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql's import with Nominatim is terminated unexpectedly.](/questions/44235/osm2pgsqls-import-with-nominatim-is-terminated-unexpectedly)

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
<span id="post-44235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44235-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys! I try to upload a large pbf file(Netherland) from Geofabrik into Nominatim db (with small area import works fine). What I'm doing:</p>
<p>1)Start this script: ./utils/setup.php --osm-file maps/netherlands-latest.osm.pbf --all --osm2pgsql-cache 6000 2&gt;&amp;1 | tee /opt/Nominatim/setup.log</p>
<p>2) I'm waiting until proceess terminates unexpectedly. here pg_log file: <a href="http://pastebin.com/auzWXxbP">http://pastebin.com/auzWXxbP</a> Also I get errors in setup.log</p>
<blockquote>
<p>CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF); failed: server closed the connection unexpectedly This probably means the server terminated abnormally before or while processing the request.</p>
<p>Error occurred, cleaning up ERROR: Error executing external command: /opt/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 6000 -P 5432 -d nominatim /opt/Nominatim/maps/netherlands-latest.osm.pbf Error executing external command: /opt/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 6000 -P 5432 -d nominatim /opt/Nominatim/maps/netherlands-latest.osm.pbf ~</p>
</blockquote>
<p>What am I doing wrong? is that hardware issue (mem 8Gb) or something else? Any ideas will be appreciated.</p>
<p><strong>Update:</strong> pg_log: <a href="http://pastebin.com/CGSAchit">http://pastebin.com/CGSAchit</a> it is crashed on "Failed process was running: CREATE INDEX planet_osm_ways_nodes ON planet_osm_ways USING gin (nodes) WITH (FASTUPDATE=OFF);" and I don't know what's going wrong with it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '15, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c14774eb4c4f7361a4e908fa59d9827d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silentium&#39;s gravatar image" />
<p><span>Silentium</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silentium has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '15, 13:03</strong> </span></p>
</div>
</div>
<div id="comments-container-44235" class="comments-container">
&#10;</div>
<div id="comment-tools-44235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

