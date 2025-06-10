+++
type = "question"
title = "Performance problem rendering tiles using the openstreetmap-carto stylesheet"
description = '''Hi, We have started to build a tile server. I have installed Mapnik and mod_tile on the server (Fedora 21, 64GB RAM, 8 Cores 2.5GHz) and the standard openstreetmap-carto stylesheet is used for rendering tiles.  The problem is, openstreetmap-carto stylesheet&#x27;s quries are really slow on our database. ...'''
date = "2015-11-10T17:29:00Z"
lastmod = "2015-12-15T16:18:00Z"
weight = 46499
keywords = [ "performance", "rendering", "style", "mapnik", "mod_tile" ]
aliases = [ "/questions/46499" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Performance problem rendering tiles using the openstreetmap-carto stylesheet](/questions/46499/performance-problem-rendering-tiles-using-the-openstreetmap-carto-stylesheet)

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
<span id="post-46499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46499-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We have started to build a tile server. I have installed Mapnik and mod_tile on the server (Fedora 21, 64GB RAM, 8 Cores 2.5GHz) and the standard openstreetmap-carto stylesheet is used for rendering tiles.</p>
<p><strong>The problem is, openstreetmap-carto stylesheet's quries are really slow on our database. Some of the queries take few seconds to complete!</strong></p>
<p>Here are few examples queries from postgresql log file with a very long duration time: <a href="http://pastebin.com/HFxccuJB" title="queries">log file</a><br />
And here is "Explain Analyze" output for the two most expensive queries <a href="http://pastebin.com/z7Bncin4" title="explain analyze output">explain analyze output</a></p>
<p>For some queries (for instance <a href="http://pastebin.com/Xa2NP49a" title="big result set">this one</a>) the result set contains more than 120K records! does standard layout really need to fetch this many records to render some of the tiles?</p>
<p>Here are more details about the steps I took to build the map server:</p>
<p>I used this command to import data into database: <em>osm2pgsql --create --slim --latlong --hstore --hstore-match-only --number-processes 4 --cache 20000 --style default.style --input-reader pbf planet-latest.osm.pbf</em></p>
<p>All the indexes are in place (I added few more indexes suggested <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/207" title="index">here</a> which helped a bit but still queries are too slow)</p>
<p>I also ran <em>vacuum(analyze, verbose);</em></p>
<p>kernel.shmmax is 8589934592</p>
<p>In postgres.config file we have:<br />
shared_buffers = 12GB<br />
work_mem = 4096MB<br />
maintenance_work_mem = 4096MB<br />
wal_buffers = 16MB<br />
checkpoint_segments = 512<br />
checkpoint_completion_target = 0.9<br />
cpu_tuple_cost = 0.05<br />
autovacuum=on<br />
autovacuum_vacuum_scale_factor = 0.05<br />
autovacuum_analyze_scale_factor = 0.2<br />
track_counts=on</p>
<p>I really appriciate any help!<br />
/Reza</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '15, 17:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '16, 10:09</strong> </span></p>
</div>
</div>
<div id="comments-container-46499" class="comments-container">
&#10;</div>
<div id="comment-tools-46499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46499-form-container" class="comment-form-container">
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

<span id="47170"></span>

<div id="answer-container-47170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have a similar issue, it turned out that in the osm carto style the srid parameter is missing and mapnik run an expensive query to find it.</p>
<p>Adding the line "srid: 900913" under "osm2pgsql" section of project.yaml improved the performances dramatically.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '15, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c267aafb46ae47bc6e8b3e47b34220c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stefano%20Salvador&#39;s gravatar image" />
<p><span>Stefano Salv...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stefano Salvador has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-47170" class="comments-container">
&#10;</div>
<div id="comment-tools-47170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47170-form-container" class="comment-form-container">
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

