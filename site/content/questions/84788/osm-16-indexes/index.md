+++
type = "question"
title = "OSM 1.6 indexes"
description = '''What indexes are generated in 1.6? my import failed (again. do NOT trust AWS RDS Aurora Postgresql serverless!) during index creation, and was wondering what were necessary to finish the installation. Completed planet_osm_point Stopping table: planet_osm_rels Building index on table: planet_osm_rels...'''
date = "2022-06-16T10:36:00Z"
lastmod = "2022-06-16T10:36:00Z"
weight = 84788
keywords = [ "aws", "aurora", "postgresql" ]
aliases = [ "/questions/84788" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM 1.6 indexes](/questions/84788/osm-16-indexes)

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
<span id="post-84788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84788-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What indexes are generated in 1.6?</p>
<p>my import failed (again. do NOT trust AWS RDS Aurora Postgresql serverless!) during index creation, and was wondering what were necessary to finish the installation.</p>
<pre><code>Completed planet_osm_point
Stopping table: planet_osm_rels
Building index on table: planet_osm_rels
Stopped table: planet_osm_rels in 634s
Copying planet_osm_line to cluster by geometry finished
Creating geometry index on planet_osm_line
WARNING:  terminating connection because of crash of another server process
DETAIL:  The postmaster has commanded this server process to roll back the current transaction and exit, because another server process exited abnormally and possibly corrupted shared memory.
HINT:  In a moment you should be able to reconnect to the database and repeat your command.
WARNING:  terminating connection because of crash of another server process
DETAIL:  The postmaster has commanded this server process to roll back the current transaction and exit, because another server process exited abnormally and possibly corrupted shared memory.
HINT:  In a moment you should be able to reconnect to the database and repeat your command.</code></pre>
<p>Another user stated that, for 1.4 the indexes needed could likely be completed with:</p>
<pre><code>CREATE INDEX planet_osm_line_osm_id_idx ON public.planet_osm_line USING btree (osm_id);
CREATE INDEX planet_osm_line_way_idx ON public.planet_osm_line USING gist (way);
CREATE INDEX planet_osm_point_osm_id_idx ON public.planet_osm_point USING btree (osm_id);
CREATE INDEX planet_osm_point_way_idx ON public.planet_osm_point USING gist (way);
CREATE INDEX planet_osm_polygon_osm_id_idx ON public.planet_osm_polygon USING btree (osm_id);
CREATE INDEX planet_osm_polygon_way_idx ON public.planet_osm_polygon USING gist (way);
CREATE INDEX planet_osm_rels_parts_idx ON public.planet_osm_rels USING gin (parts) WITH (fastupdate=off);
CREATE INDEX planet_osm_roads_osm_id_idx ON public.planet_osm_roads USING btree (osm_id);
CREATE INDEX planet_osm_roads_way_idx ON public.planet_osm_roads USING gist (way);
CREATE INDEX planet_osm_ways_nodes_idx ON public.planet_osm_ways USING gin (nodes) WITH (fastupdate=off);</code></pre>
<p>I was wondering/hoping that this was still true with 1.6 and/or someone had an updated list available</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aws" rel="tag" title="see questions tagged &#39;aws&#39;">aws</span> <span class="post-tag tag-link-aurora" rel="tag" title="see questions tagged &#39;aurora&#39;">aurora</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '22, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/4f56517242a58c6e37c6421d4b874893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesPep&#39;s gravatar image" />
<p><span>JamesPep</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesPep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84788" class="comments-container">
&#10;</div>
<div id="comment-tools-84788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84788-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

