+++
type = "question"
title = "Using osmosis update OSM Planet extreamly slow."
description = ''' osmosis version: 0.46-2 osm2pgsql version: 0.94 Ubuntu version: 18.04.2  PostgreSQL config:  shared_buffers = 12G work_mem = 1000MB effective_io_concurrency = 2 fsync = on autovacuum = on effective_cache_size = 12GB maintenance_work_mem = 2GB  Using osmosis to update the planet osm database. Based ...'''
date = "2020-12-09T18:52:00Z"
lastmod = "2020-12-09T18:52:00Z"
weight = 77874
keywords = [ "planet", "osm2pgsql", "osmosis", "mod_tile" ]
aliases = [ "/questions/77874" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using osmosis update OSM Planet extreamly slow.](/questions/77874/using-osmosis-update-osm-planet-extreamly-slow)

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
<span id="post-77874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<ul>
<li>osmosis version: 0.46-2</li>
<li>osm2pgsql version: 0.94</li>
<li>Ubuntu version: 18.04.2</li>
</ul>
<p>PostgreSQL config:</p>
<ul>
<li>shared_buffers = 12G</li>
<li>work_mem = 1000MB</li>
<li>effective_io_concurrency = 2</li>
<li>fsync = on</li>
<li>autovacuum = on</li>
<li>effective_cache_size = 12GB</li>
<li>maintenance_work_mem = 2GB</li>
</ul>
<p>Using osmosis to update the planet osm database. Based on this tutorial:<a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">Updating your database as people edit OpenStreetMap</a></p>
<p>I modified the <strong>osm2pgsql</strong> script in <strong>mod_tile/openstreetmap-tiles-update-expire</strong> to this</p>
<p><code>osm2pgsql -slim -a --flat-nodes /node.cache --cache 3000 -e 13-20 &lt;database config, user, host etc&gt; -o /dirty_tiles /changes.osc.gz</code></p>
<p>Is the "<strong>-e</strong> (expire tiles)" slows down the importing? If I only want to update the database but don't want to update the image tiles, can I just remove the <strong>-e</strong> and <strong>-o</strong> argument?</p>
<p><img src="https://help.openstreetmap.org/upfiles/2020-12-09_12-57-19.jpg" alt="alt text" /></p>
<p>You can see the processing speed is really slow!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Dec '20, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/40e60a70ee29b8df762ecd6168503655?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yingcai&#39;s gravatar image" />
<p><span>Yingcai</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yingcai has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '20, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-77874" class="comments-container">
&#10;</div>
<div id="comment-tools-77874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77874-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

