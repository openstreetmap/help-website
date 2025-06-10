+++
type = "question"
title = "duplicate key value violates unique constraint &quot;planet_osm_nodes_pkey&quot;"
description = '''I&#x27;m building an OSM server using osm2pgsql and mapnik. I began the PostGIS import a couple of days ago, and it was chugging along just fine until sometime overnight, when I got this error: Processing: Node(1312851k 68.0k/s) Way(119415k 0.75k/s) Relation(1230921 11.96/s) parse time: 281588s  Reading ...'''
date = "2012-01-09T20:52:00Z"
lastmod = "2015-04-03T22:55:00Z"
weight = 9875
keywords = [ "planet_osm", "osm2pgsql", "mapnik", "postgis" ]
aliases = [ "/questions/9875" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [duplicate key value violates unique constraint "planet_osm_nodes_pkey"](/questions/9875/duplicate-key-value-violates-unique-constraint-planet_osm_nodes_pkey)

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
<span id="post-9875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm building an OSM server using osm2pgsql and mapnik. I began the PostGIS import a couple of days ago, and it was chugging along just fine until sometime overnight, when I got this error:</p>
<pre><code>Processing: Node(1312851k 68.0k/s) Way(119415k 0.75k/s) Relation(1230921 11.96/s)  parse time: 281588s
&#10;Reading in file: /dev/stdin
Unknown node type 8
insert_node failed: ERROR:  duplicate key value violates unique constraint &quot;planet_osm_nodes_pkey&quot;
DETAIL:  Key (id)=(1) already exists.
(7)
Arguments were: 1, 666549596, 104993388, (null),
Error occurred, cleaning up</code></pre>
<p>Any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '12, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/636c2c1ddba579676493182a648b6bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger%20Weeks&#39;s gravatar image" />
<p><span>Roger Weeks</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger Weeks has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '12, 21:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-9875" class="comments-container">
<span id="33535"></span>
<div id="comment-33535" class="comment">
<div id="post-33535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I recently ran into the same error - anyone have any suggestions?</p>
</div>
<div id="comment-33535-info" class="comment-info">
<span class="comment-age">(28 May '14, 19:19)</span> <span class="comment-user userinfo">aug_aug</span>
</div>
</div>
</div>
<div id="comment-tools-9875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9875-form-container" class="comment-form-container">
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

<span id="42121"></span>

<div id="answer-container-42121" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is this the same issue? <a href="https://github.com/openstreetmap/osm2pgsql/issues/16">https://github.com/openstreetmap/osm2pgsql/issues/16</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '15, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/6b2a727dc28689d7d065c0f53368998d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iqqmuT&#39;s gravatar image" />
<p><span>iqqmuT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iqqmuT has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42121" class="comments-container">
&#10;</div>
<div id="comment-tools-42121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42121-form-container" class="comment-form-container">
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

