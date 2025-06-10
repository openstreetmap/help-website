+++
type = "question"
title = "Osm2pgsql failed due to ERROR: stop COPY_END"
description = '''We are facing a problem with a closed connection with osm2pgsql when performing the daily update of the database from &quot;download.geofabrik.de&quot;, and the region in question is Brazil. We have three environments with the same settings (CPU, memory and disk), but the problem only occurs in one of them, w...'''
date = "2022-06-02T18:20:00Z"
lastmod = "2022-06-02T20:56:00Z"
weight = 84682
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/84682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2pgsql failed due to ERROR: stop COPY_END](/questions/84682/osm2pgsql-failed-due-to-error-stop-copy_end)

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
<span id="post-84682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84682-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are facing a problem with a closed connection with osm2pgsql when performing the daily update of the database from "download.geofabrik.de", and the region in question is Brazil. We have three environments with the same settings (CPU, memory and disk), but the problem only occurs in one of them, which is stage, dev and pro work well.</p>
<p>Command:</p>
<p>osm2pgsql -a --slim -e13-20 -d dbhom --number-processes 4 --cache 3042 --tag-transform-script /opt/programs/openstreetmap-carto/5.3.1/hom_openstreetmap/openstreetmap-carto/openstreetmap -carto.lua -S /opt/programas/openstreetmap-carto/5.3.1/hom_openstreetmap/openstreetmap-carto/openstreetmap-carto.style -o /opt/appfiles/hom_openstreetmap/dirty_tiles.38216 /opt/appfiles/hom_openstreetmap/changes .osc.gz</p>
<p>Log:</p>
<p>osm2pgsql version 0.92.0 (64 bit id space) ... Reading in file: /opt/appfiles/hom_openstreetmap/changes.osc.gz Using XML parser. Processing: Node(60k 0.2k/s) Way(0k 0.00k/s) Relation(0 0.00/s)node cache: stored: 63588(100.00%), storage efficiency: 48.50% (dense blocks: 2, sparse nodes: 57356), hit rate: -nan% Osm2pgsql failed due to ERROR: stop COPY_END for planet_osm_roads failed: server closed the connection unexpectedly This probably means the server terminated abnormally before or while processing the request.</p>
<p>On the PostgreSQL side, we have this message below with a few minutes after the connection with the database started. However, the execution in the application part continues and is only finished minutes later.</p>
<p>2022-06-02 09:36:38 -03 [35713]: [1-1] user=usr,db=dbhom LOG: could not receive data from client: Connection reset by peer</p>
<p>We have the application server, where osm2pgsql runs, and we have the database with the same settings both.</p>
<ul>
<li>4 CPUs</li>
<li>8 GB RAM</li>
<li>PostgreSQL 12</li>
<li>PostGIS 3.1</li>
</ul>
<p>The software versions used in the 3 environments are the same and have been recently revised.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '22, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/75861b5236ce6ac694421f92da06cadd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asuzano&#39;s gravatar image" />
<p><span>asuzano</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asuzano has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84682" class="comments-container">
&#10;</div>
<div id="comment-tools-84682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84682-form-container" class="comment-form-container">
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

<span id="84684"></span>

<div id="answer-container-84684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84684-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd start with upgrading your osm2pgsql version to the latest one. You say the environment was "revised", but osm2pgsql 0.92 is from December 2016, and is by now heavily outdated.</p>
<p>If you upgrade to 1.6.0, you'll get the added benefit of the new "flex" configuration options of osm2pgsql (see <a href="https://osm2pgsql.org/doc/manual.html">https://osm2pgsql.org/doc/manual.html</a> and <a href="https://osm2pgsql.org/doc/manual.html#the-flex-output),">https://osm2pgsql.org/doc/manual.html#the-flex-output),</a> which gives much greater flexibility in defining the output database schema.</p>
<p>Also, 8GB RAM is low end nowadays. Although your Brazil extract may not be that taxing, as being still quite modest in size at 1.4GB PBF, more RAM never hurts for caching purposes on the OS and database level.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '22, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-84684" class="comments-container">
&#10;</div>
<div id="comment-tools-84684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84684-form-container" class="comment-form-container">
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

