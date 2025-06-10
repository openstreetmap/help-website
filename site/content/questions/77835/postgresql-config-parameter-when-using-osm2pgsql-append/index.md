+++
type = "question"
title = "PostgreSql .config parameter when using Osm2pgsql --append"
description = '''I have already imported the OSM Planet to the database. And I want to update the database regularly. The update command I use is osm2pgsql --append -slim with 6GB cache. However, the update process is still too slow. Hardware: 32G memory, 1.7TB SSD. Database config: shared_buffers = 2GB work_mem = 1...'''
date = "2020-12-02T20:38:00Z"
lastmod = "2020-12-04T19:53:00Z"
weight = 77835
keywords = [ "postgresql", "osm2pgsql", "mapping" ]
aliases = [ "/questions/77835" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PostgreSql .config parameter when using Osm2pgsql --append](/questions/77835/postgresql-config-parameter-when-using-osm2pgsql-append)

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
<span id="post-77835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have already imported the OSM Planet to the database. And I want to update the database regularly. The update command I use is osm2pgsql --append -slim with 6GB cache. However, the update process is still too slow.</p>
<p>Hardware: 32G memory, 1.7TB SSD.</p>
<p>Database config:</p>
<pre><code>shared_buffers = 2GB
work_mem = 1000MB
effective_io_concurrency = 2
fsync = on
synchronous_commit = off
full_page_writes = off
checkpoint_segments = 100
checkpoint_completion_target = 0.9
autovacuum = on
effective_cache_size = 4GB
maintenance_work_mem = 2GB
max_worker_process = 12</code></pre>
<p>On average it took 1 hour to process 6 hours worth of new OSM updates. (Screenshot is the log printed by the script openstreetmap-tiles-update-expire. Inside the script, it calls osm2pgsql --append -slim) <img src="https://help.openstreetmap.org/upfiles/MicrosoftTeams-image_(2).png" alt="alt text" /></p>
<p>I remember when bulk loading OSM Planet to the database, a lot of articles suggest modifying postgresql.conf</p>
<p>Such as:</p>
<p>fsync = off (import only!)</p>
<p>autovacuum = off (import only!)</p>
<p>Since the database is keep updating, should I change the postgresql config settings back to these import settings to increase performance?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '20, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/40e60a70ee29b8df762ecd6168503655?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yingcai&#39;s gravatar image" />
<p><span>Yingcai</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yingcai has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '20, 14:41</strong> </span></p>
</div>
</div>
<div id="comments-container-77835" class="comments-container">
<span id="77837"></span>
<div id="comment-77837" class="comment">
<div id="post-77837-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you indicate what hardware this is running on and your original import parameters?</p>
</div>
<div id="comment-77837-info" class="comment-info">
<span class="comment-age">(03 Dec '20, 06:47)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="77844"></span>
<div id="comment-77844" class="comment">
<div id="post-77844-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(for completeness - that screenshot looks like output from openstreetmap-tiles-update-expire)</p>
</div>
<div id="comment-77844-info" class="comment-info">
<span class="comment-age">(03 Dec '20, 22:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77851"></span>
<div id="comment-77851" class="comment">
<div id="post-77851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/2053/simonpoole">@simonPoole</a> and <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. The post has been updated.</p>
</div>
<div id="comment-77851-info" class="comment-info">
<span class="comment-age">(04 Dec '20, 14:42)</span> <span class="comment-user userinfo">Yingcai</span>
</div>
</div>
</div>
<div id="comment-tools-77835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77835-form-container" class="comment-form-container">
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

<span id="77839"></span>

<div id="answer-container-77839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77839-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure what screen shot is about, this doesn't look like osm2pgsql output!?</p>
<p>There is some advice on how to tune your database for osm2pgsql in the osm2pgsql manual at <a href="https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server">https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '20, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-77839" class="comments-container">
<span id="77853"></span>
<div id="comment-77853" class="comment">
<div id="post-77853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The screenshot is the log printed by the script openstreetmap-tiles-update-expire (mod_tile <a href="https://github.com/SomeoneElseOSM/mod_tile/tree/switch2osm">https://github.com/SomeoneElseOSM/mod_tile/tree/switch2osm</a> ). Inside the script, it calls osm2pgsql --append -slim</p>
</div>
<div id="comment-77853-info" class="comment-info">
<span class="comment-age">(04 Dec '20, 19:53)</span> <span class="comment-user userinfo">Yingcai</span>
</div>
</div>
</div>
<div id="comment-tools-77839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77839-form-container" class="comment-form-container">
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

