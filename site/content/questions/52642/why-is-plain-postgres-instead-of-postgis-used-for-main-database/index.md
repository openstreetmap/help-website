+++
type = "question"
title = "Why is plain Postgres instead of PostGIS used for main database?"
description = '''From the component overview on the wiki I see that a plain Postgres is used for the main database (marked as &quot;PostgreSQL backend&quot;). What is the reason no GIS database (like PostGIS) is used? Would it not bring any advantages? I see PostGIS being used in the rendering part of the system. Can someone ...'''
date = "2016-10-22T20:04:00Z"
lastmod = "2016-10-22T22:27:00Z"
weight = 52642
keywords = [ "servers", "postgresql", "postgres", "postgis", "database" ]
aliases = [ "/questions/52642" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is plain Postgres instead of PostGIS used for main database?](/questions/52642/why-is-plain-postgres-instead-of-postgis-used-for-main-database)

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
<span id="post-52642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52642-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>From the <a href="https://wiki.openstreetmap.org/wiki/Component_overview">component overview</a> on the wiki I see that a plain Postgres is used for the main database (marked as "PostgreSQL backend"). What is the reason no GIS database (like PostGIS) is used? Would it not bring any advantages?</p>
<p>I see PostGIS being used in the rendering part of the system. Can someone explain why is it used there?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-servers" rel="tag" title="see questions tagged &#39;servers&#39;">servers</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '16, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-52642" class="comments-container">
&#10;</div>
<div id="comment-tools-52642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52642-form-container" class="comment-form-container">
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

<span id="52644"></span>

<div id="answer-container-52644" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52644-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kozuch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The strength of PostGIS is geometry operations with "simple features" - points, lines, and polygons. PostGIS offers functionality to compute the geometric relation between such features (whether they intersect or touch or contain each other, for example). All this is not required for the central OSM database because in that database, the only geometries that exist are nodes. While ways and relations can be used to form lines and polygons, this is a geometric interpretation that the database is fully ignorant of.</p>
<p>Using PostGIS in the backend would add an unnecessary layer of complexity, and the additional functionality is not useful there.</p>
<p>This is different in the rendering database, where OSM objects are transformed into "simple features" when imported by osm2pgsql (a misnomer really - it should be osm2postgis).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '16, 22:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52644" class="comments-container">
&#10;</div>
<div id="comment-tools-52644" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52644-form-container" class="comment-form-container">
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

