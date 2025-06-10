+++
type = "question"
title = "Extremely Variable Rendering Times"
description = '''I have a local global OSM server up and it is running, but the rendering speeds vary drastically. An example:  DEBUG: DONE TILE english 9 216-223 144-151 in 32.009 seconds DONE TILE english 16 74992-74999 11408-11415 in 304.705 seconds  I have run the indexes from here: OSM PostGIS Tuning and it see...'''
date = "2022-04-04T19:09:00Z"
lastmod = "2022-04-06T10:29:00Z"
weight = 84102
keywords = [ "index", "renderd", "osm", "postgres", "postgis" ]
aliases = [ "/questions/84102" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extremely Variable Rendering Times](/questions/84102/extremely-variable-rendering-times)

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
<span id="post-84102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84102-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a local global OSM server up and it is running, but the rendering speeds vary drastically. An example:</p>
<blockquote>
<p>DEBUG: DONE TILE english 9 216-223 144-151 in 32.009 seconds</p>
<p>DONE TILE english 16 74992-74999 11408-11415 in 304.705 seconds</p>
</blockquote>
<p>I have run the indexes from here: <a href="https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning">OSM PostGIS Tuning</a> and it seems to not have made much of a difference. I would say for Z16 the average render time is about 190 seconds. This is sitting on the following hardware:</p>
<ul>
<li>Intel i9-10850K (20 Core)</li>
<li>128GB DDR4</li>
<li>OS is sitting on 1TB NVME</li>
<li>OSM Database is sitting on 4TB NVME</li>
</ul>
<p>Here are my postgres settings (this all sits on postgres 12) some taken from here: <a href="https://osm2pgsql.org/doc/manual.html">osm2pgsql manual</a>:</p>
<ul>
<li><p>max_connections = 300</p></li>
<li><p>shared_buffers = 16GB</p></li>
<li><p>work_mem = 10GB</p></li>
<li><p>maintenance_work_mem = 10GB</p></li>
<li><p>autovacuum = on</p></li>
<li><p>effective_io_concurrency = 300</p></li>
<li><p>wal_level = minimal</p></li>
<li><p>fsync = off</p></li>
<li><p>synchronous_commit = off</p></li>
<li><p>max_wal_size = 10GB</p></li>
<li><p>min_wal_size = 80MB</p></li>
<li><p>checkpoint_completion_target = 0.9</p></li>
<li><p>max_wal_senders = 0</p></li>
<li><p>random_page_cost = 1.1</p></li>
<li><p>effective_cache_size = 70GB</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '22, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0d368c08750719366635c4ff907919da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaredalv&#39;s gravatar image" />
<p><span>jaredalv</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaredalv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84102" class="comments-container">
<span id="84112"></span>
<div id="comment-84112" class="comment">
<div id="post-84112-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Do you have a Postgres slow query log so you can see (assuming the bottleneck is Postgres) what's taking the longest time?</p>
</div>
<div id="comment-84112-info" class="comment-info">
<span class="comment-age">(06 Apr '22, 10:29)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

