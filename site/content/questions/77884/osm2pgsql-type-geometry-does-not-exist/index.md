+++
type = "question"
title = "osm2pgsql - type &quot;geometry&quot; does not exist"
description = '''I&#x27;ve only used osm2pgsql a few times with files from downloads.geofabrik.de and I&#x27;ve never run into a problem. Today, I downloaded a PDF file from geofabrik (165 MB), created an empty databse in postgresql, and tried running it through osm2pgsql. This is the only output that I get... C:&#92;AKH_Maps&#92;osm...'''
date = "2020-12-10T03:37:00Z"
lastmod = "2020-12-10T14:05:00Z"
weight = 77884
keywords = [ "postgresql", "osm2pgsql", "geofabrik" ]
aliases = [ "/questions/77884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql - type "geometry" does not exist](/questions/77884/osm2pgsql-type-geometry-does-not-exist)

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
<span id="post-77884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've only used osm2pgsql a few times with files from downloads.geofabrik.de and I've never run into a problem.</p>
<p>Today, I downloaded a PDF file from geofabrik (165 MB), created an empty databse in postgresql, and tried running it through osm2pgsql. This is the only output that I get...</p>
<pre><code>C:\AKH_Maps\osm2pgsql&gt;osm2pgsql -c -d gisdb-mi -U postgres -W -H localhost -S C:\AKH_Maps\osm2pgsql\default.style C:\AKH_Maps\GIS-sources\geofabrik\michigan-latest.osm.pbf
2020-12-09 21:05:16  osm2pgsql version 1.4.0
&#10;Password:
&#10;2020-12-09 21:05:22  Database version: 12.1
2020-12-09 21:05:22  Node-cache: cache=800MB, maxblocks=12800*65536, allocation method=1
2020-12-09 21:05:23  Setting up table &#39;planet_osm_point&#39;
2020-12-09 21:05:23  node cache: stored: 0(0.00%), storage efficiency: 0.00% (dense blocks: 0, sparse nodes: 0), hit rate: 0.00%
2020-12-09 21:05:23  [1m[38;2;255;000;000mERROR: [0m[1m[38;2;255;000;000mDatabase error: ERROR:  type &quot;geometry&quot; does not exist
LINE 1: ... text,&quot;width&quot; text,&quot;wood&quot; text,&quot;z_order&quot; int4,way geometry(P...
                                                             ^
[0m</code></pre>
<p>Any idea what the problem is?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '20, 03:37</strong></p>
<img src="https://secure.gravatar.com/avatar/25004edb25cbd4050be892fd76332323?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndrewNDeBear&#39;s gravatar image" />
<p><span>AndrewNDeBear</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndrewNDeBear has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77884" class="comments-container">
&#10;</div>
<div id="comment-tools-77884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77884-form-container" class="comment-form-container">
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

<span id="77886"></span>

<div id="answer-container-77886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You forgot to run the PostgreSQL command <code>CREATE EXTENSION postgis</code> (or enable the PostGIS extension in another way).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '20, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77886" class="comments-container">
<span id="77891"></span>
<div id="comment-77891" class="comment">
<div id="post-77891-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yup. That was it.</p>
<pre><code>2020-12-10 08:57:23  Osm2pgsql took 129s (2m 9s) overall.</code></pre>
<p>Thanks!</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture1_ENyfDaB.PNG" alt="alt text" /></p>
</div>
<div id="comment-77891-info" class="comment-info">
<span class="comment-age">(10 Dec '20, 14:05)</span> <span class="comment-user userinfo">AndrewNDeBear</span>
</div>
</div>
</div>
<div id="comment-tools-77886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77886-form-container" class="comment-form-container">
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

