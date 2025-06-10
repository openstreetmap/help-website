+++
type = "question"
title = "How to setup GIS Server on Debian"
description = '''Hi everyone, I tried to setup an GIS-Server on Debian 6 with some installation guides, but it does not work. I&#x27;ve installed PostgreSQL 8.4, PostGIS &amp;amp; osm2pgsql. But when I start osm2pgsql, it gives an error that some tables are not available: osm2pgsql -c -s duesseldorf.osm  and the return is os...'''
date = "2011-08-22T13:30:00Z"
lastmod = "2011-08-22T14:05:00Z"
weight = 7255
keywords = [ "gis", "osm", "postgresql", "debian" ]
aliases = [ "/questions/7255" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to setup GIS Server on Debian](/questions/7255/how-to-setup-gis-server-on-debian)

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
<span id="post-7255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7255-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I tried to setup an GIS-Server on Debian 6 with some installation guides, but it does not work.</p>
<p>I've installed PostgreSQL 8.4, PostGIS &amp; osm2pgsql. But when I start osm2pgsql, it gives an error that some tables are not available:</p>
<pre><code>osm2pgsql -c -s duesseldorf.osm</code></pre>
<p>and the return is</p>
<pre><code>osm2pgsql SVN version 0.69-
Using projection SRS 900913 (Spherical Mercator)
Setting up table: planet_osm_point
NOTICE:  table &quot;planet_osm_point&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_point_tmp&quot; does not exist, skipping
SELECT AddGeometryColumn(&#39;planet_osm_point&#39;, &#39;way&#39;, 900913, &#39;POINT&#39;, 2 );
 failed: ERROR:  function addgeometrycolumn(unknown, unknown, integer, unknown, integer) does not exist
LINE 1: SELECT AddGeometryColumn(&#39;planet_osm_point&#39;, &#39;way&#39;, 900913, ...
               ^
HINT:  No function matches the given name and argument types. You might need to add explicit type casts.
&#10;Error occurred, cleaning up</code></pre>
<p>So - where can I get the database-tables?</p>
<p>Thanks,</p>
<p>Alex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gis" rel="tag" title="see questions tagged &#39;gis&#39;">gis</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '11, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/05f98dd7150753c7b90dfe13775879fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="icewave&#39;s gravatar image" />
<p><span>icewave</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="icewave has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '11, 14:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-7255" class="comments-container">
&#10;</div>
<div id="comment-tools-7255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7255-form-container" class="comment-form-container">
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

<span id="7259"></span>

<div id="answer-container-7259" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7259-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="icewave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You forgot to actually activate PostGIS features for your database. Check the <a href="http://wiki.openstreetmap.org/wiki/Mapnik/PostGIS">wiki page on Mapnik/PostGIS installation</a>. You are missing something like</p>
<pre><code>psql -d gis -f /usr/share/postgresql/8.4/contrib/postgis-1.5/postgis.sql
psql -d gis -f /usr/share/postgresql/8.4/contrib/postgis-1.5/spatial_ref_sys.sql</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '11, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '11, 14:38</strong> </span></p>
</div>
</div>
<div id="comments-container-7259" class="comments-container">
&#10;</div>
<div id="comment-tools-7259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7259-form-container" class="comment-form-container">
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

