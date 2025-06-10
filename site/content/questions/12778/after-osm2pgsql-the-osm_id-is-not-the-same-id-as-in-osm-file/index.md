+++
type = "question"
title = "after osm2pgsql the osm_id is not the same id as in .osm file"
description = '''Hi, I&#x27;m trying to put my .osm file into postgres db using osm2pgsql. I&#x27;ve tried: $ osm2pgsql -U postgres -d OSM ./my_country.osm  The problem is that the osm_id of the table &quot;planet_osm_roads&quot; on db is not the same id of the &quot;way&quot; tag on .osm file. For example, I took an id x of some way from the .o...'''
date = "2012-05-17T23:18:00Z"
lastmod = "2012-05-18T00:25:00Z"
weight = 12778
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/12778" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [after osm2pgsql the osm_id is not the same id as in .osm file](/questions/12778/after-osm2pgsql-the-osm_id-is-not-the-same-id-as-in-osm-file)

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
<span id="post-12778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12778-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to put my .osm file into postgres db using osm2pgsql. I've tried:</p>
<pre><code>$ osm2pgsql -U postgres -d OSM ./my_country.osm</code></pre>
<p>The problem is that the osm_id of the table "planet_osm_roads" on db is not the same id of the "way" tag on .osm file. For example, I took an id x of some way from the .osm file and then query the db by</p>
<pre><code>&quot;SELECT * FROM planet_osm_roads WHERE osm_id=x&quot;</code></pre>
<p>and I got nothing.</p>
<p>I want to get ways from db by thier ids on .osm file. After that I want to get all nodes of this way. There is any way to do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '12, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7d67503ae4b9ae071c3ac2473c379935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uriel&#39;s gravatar image" />
<p><span>uriel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uriel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12778" class="comments-container">
&#10;</div>
<div id="comment-tools-12778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12778-form-container" class="comment-form-container">
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

<span id="12779"></span>

<div id="answer-container-12779" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="uriel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>planet_osm_roads will only contain a selection of geometries (large streets and railways mostly). Use planet_osm_line to find smaller line geometries.</p>
<p>You will not find the way/node link in these tables however as they contain pre-computed geometries. If you really need node IDs then you have to look them up in the planet_osm_ways table (which you will only get with the <code>--slim</code> flag) but osm2pgsql is not optimised for that kind of query and will, for example, not even have all ways stored. If you really want to play with the "raw" OSM data then it is better to import with Osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '12, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12779" class="comments-container">
<span id="12780"></span>
<div id="comment-12780" class="comment">
<div id="post-12780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. osmosis helped.</p>
</div>
<div id="comment-12780-info" class="comment-info">
<span class="comment-age">(18 May '12, 00:25)</span> <span class="comment-user userinfo">uriel</span>
</div>
</div>
</div>
<div id="comment-tools-12779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12779-form-container" class="comment-form-container">
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

