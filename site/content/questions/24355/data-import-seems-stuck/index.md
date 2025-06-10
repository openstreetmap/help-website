+++
type = "question"
title = "Data import seems stuck"
description = '''Hi guys, I am using the command  ./utils/setup.php --osm-file north-america-latest.osm.bz2 --all --osm2pgsql-cache 5000  to import data. It seems having loaded all the Node, Way, and Relation overnight. However, it seems stuck at stopped table: planet_osm_rels. The following is the latest log info: ...'''
date = "2013-07-18T14:03:00Z"
lastmod = "2013-07-18T15:59:00Z"
weight = 24355
keywords = [ "imports", "nominatim", "data" ]
aliases = [ "/questions/24355" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Data import seems stuck](/questions/24355/data-import-seems-stuck)

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
<span id="post-24355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24355-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I am using the command ./utils/setup.php --osm-file north-america-latest.osm.bz2 --all --osm2pgsql-cache 5000 to import data. It seems having loaded all the Node, Way, and Relation overnight. However, it seems stuck at stopped table: planet_osm_rels. The following is the latest log info:</p>
<pre><code>Node stats: total(607580357), ma(2386741811) in 6971s
Way stats: total(39333613), max(230146048) in 21023s
Relation stats: total(309747), max(3085766) in 1978s
node cache: stored: 483765898(79.62%), storage efficiency: 73.82% (dense blocks: 433893, sparse nodes: 105527130), hit rate: 80.58%
Stopping table: planet_osm_nodes
Stopping table: planet_osm_ways
Stopping table: planet_osm_rels
Building index on table: planet_osm_ways (fastupdate=off)
Building index on table: planet_osm_rels (fastupdate=off)
Stopped table: planet_osm_nodes in 0s
Stopped table: planet_osm_rels in 14s</code></pre>
<p>Is it really stuck, or it is normal, just super slow? Thanks in advance! TJ</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imports" rel="tag" title="see questions tagged &#39;imports&#39;">imports</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jul '13, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '13, 17:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span></p>
</div>
</div>
<div id="comments-container-24355" class="comments-container">
<span id="24356"></span>
<div id="comment-24356" class="comment">
<div id="post-24356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK guys, I think it is still running -- It is slowly consuming the hard disk. But is it normal, I mean, is it expected to slow down at this stage?</p>
<p>Thanks again. TJ</p>
</div>
<div id="comment-24356-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 14:36)</span> <span class="comment-user userinfo">OSM-TJ2013</span>
</div>
</div>
</div>
<div id="comment-tools-24355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24355-form-container" class="comment-form-container">
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

<span id="24357"></span>

<div id="answer-container-24357" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24357-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OSM-TJ2013 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can see what postgresql is doing by using:</p>
<pre><code>psql nominatim
nominatim=# select * from pg_stat_activity;</code></pre>
<p>Probably it is creating indexes which depending on the amount of maintenance memory can be quite slow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '13, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jul '13, 15:35</strong> </span></p>
</div>
</div>
<div id="comments-container-24357" class="comments-container">
<span id="24358"></span>
<div id="comment-24358" class="comment">
<div id="post-24358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great! Thanks!</p>
</div>
<div id="comment-24358-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 15:54)</span> <span class="comment-user userinfo">OSM-TJ2013</span>
</div>
</div>
<span id="24359"></span>
<div id="comment-24359" class="comment">
<div id="post-24359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you have an answer you are happy with please accept it.</p>
</div>
<div id="comment-24359-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 15:59)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-24357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24357-form-container" class="comment-form-container">
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

