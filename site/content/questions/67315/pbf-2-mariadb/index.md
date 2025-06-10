+++
type = "question"
title = "pbf 2 mariadb"
description = '''I need to write a pbf 2 mariadb conversion tool. I am looking for some sample code to work from. Know where I can get source code? Thanks.'''
date = "2018-12-21T22:28:00Z"
lastmod = "2018-12-26T06:11:00Z"
weight = 67315
keywords = [ "conversion", "pbf", "mariadb", "mysql" ]
aliases = [ "/questions/67315" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pbf 2 mariadb](/questions/67315/pbf-2-mariadb)

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
<span id="post-67315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67315-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to write a pbf 2 mariadb conversion tool. I am looking for some sample code to work from. Know where I can get source code? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-mariadb" rel="tag" title="see questions tagged &#39;mariadb&#39;">mariadb</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Dec '18, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/7aab3262d316b81e858a79dfa5696c13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ant&#39;s gravatar image" />
<p><span>Ant</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67315" class="comments-container">
&#10;</div>
<div id="comment-tools-67315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67315-form-container" class="comment-form-container">
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

<span id="67316"></span>

<div id="answer-container-67316" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67316-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM data can be represented in many different ways. If you're interested in a relatively basic, non-geometry representation then you should be using <code>osmosis</code> which can write MySQL with its "apidb" tasks. If you are not so interested in the basic OSM building blocks (nodes, ways, relations) but instead would like to work with geometry objects, then you should look into using <code>ogr2ogr</code> to convert directly from OSM data to MySQL and generate geometries. The canonical program everyone uses the build geometries is <code>osm2pgsql</code> and it works for PostGIS only. A competing implementation in Python (old) or Go (new) is called <code>imposm</code>. A recent newcomer on the database import scene is osmium-tool which can now generate PostGIS "copy" files; I guess it should be relatively easy to modify that to work with MariaDB: <a href="https://github.com/osmcode/osmium-tool/commit/3b0fd2363dce06b9d856c8ba0dfdd83880af6044">https://github.com/osmcode/osmium-tool/commit/3b0fd2363dce06b9d856c8ba0dfdd83880af6044</a></p>
<p>If you were to attempt to write a full-blown MariaDb importer like osm2pgsql from scratch, you'd be looking at perhaps a person-month of coding work. Don't underestimate it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '18, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-67316" class="comments-container">
<span id="67352"></span>
<div id="comment-67352" class="comment">
<div id="post-67352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik, isn't that a little over-optimistic "a person-month of coding work" for writing an osm2pgsql like converter from scratch? There is +10 years of development work in osm2pgsql by many contributors. Top contributors Ionvia and Twain47 alone seem to have both submitted around 100k code lines (<a href="https://github.com/openstreetmap/osm2pgsql/graphs/contributors),">https://github.com/openstreetmap/osm2pgsql/graphs/contributors),</a> there may be well over 300k code lines in total, if I look at all the contributors... Of course, you can cut some corners by doing away with things like (minutely) updates, tag transform, multipolygon processing, but all in all, I'd say a "one person-year of coding work" seems more realistic for anything close to what osm2pgsql really does...</p>
</div>
<div id="comment-67352-info" class="comment-info">
<span class="comment-age">(25 Dec '18, 09:58)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="67354"></span>
<div id="comment-67354" class="comment">
<div id="post-67354-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What about just osm2pgsql backend? This could be much easier:</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql#alternate-backends">https://github.com/openstreetmap/osm2pgsql#alternate-backends</a></p>
</div>
<div id="comment-67354-info" class="comment-info">
<span class="comment-age">(26 Dec '18, 06:11)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-67316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67316-form-container" class="comment-form-container">
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

