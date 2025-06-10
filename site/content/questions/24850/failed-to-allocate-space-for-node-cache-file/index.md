+++
type = "question"
title = "Failed to allocate space for node cache file"
description = '''Hi, it&#x27;s my first time trying to set up a OSM server. I have been following this tutorial: https://github.com/AnderPijoan/vectorosm (with node why i need to change how the maps are rendered for some specific requirements of my project). i made everything, except that i installed the osm2pgsql from s...'''
date = "2013-08-02T21:21:00Z"
lastmod = "2013-08-02T23:23:00Z"
weight = 24850
keywords = [ "import", "osm2pgsql", "database" ]
aliases = [ "/questions/24850" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to allocate space for node cache file](/questions/24850/failed-to-allocate-space-for-node-cache-file)

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
<span id="post-24850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>it's my first time trying to set up a OSM server. I have been following this tutorial:</p>
<p><a href="https://github.com/AnderPijoan/vectorosm">https://github.com/AnderPijoan/vectorosm</a> (with node why i need to change how the maps are rendered for some specific requirements of my project).</p>
<p>i made everything, except that i installed the osm2pgsql from source why the repository version is too old.</p>
<p>but i get stuck at the importing of the DB, i'm using:</p>
<pre><code>  osm2pgsql -m -s -c  -j -v --cache-strategy dense --flat-nodes tempFileErase -d osm -U osmuser --unlogged  --hstore-add-index --exclude-invalid-polygon -r pbf planet-latest.osm.pbf</code></pre>
<p>but i get:</p>
<pre><code>osm2pgsql SVN version 0.83.0 (64bit id space)
&#10;Using projection SRS 900913 (Spherical Mercator)
Setting up table: planet_osm_point
NOTICE:  table &quot;planet_osm_point&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_point_tmp&quot; does not exist, skipping
Setting up table: planet_osm_line
NOTICE:  table &quot;planet_osm_line&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_line_tmp&quot; does not exist, skipping
Setting up table: planet_osm_polygon
NOTICE:  table &quot;planet_osm_polygon&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_polygon_tmp&quot; does not exist, skipping
Setting up table: planet_osm_roads
NOTICE:  table &quot;planet_osm_roads&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_roads_tmp&quot; does not exist, skipping
Using built-in tag processing pipeline
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Node-cache: cache=800MB, maxblocks=0*102401, allocation method=8192
Mid: loading persistent node cache from tempFileErase
Failed to allocate space for node cache file: Success
Error occurred, cleaning up</code></pre>
<p>any idea of how i can fix it?</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '13, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/608cb2ec998f3113dbc90093cb4bb552?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ipsilondev&#39;s gravatar image" />
<p><span>ipsilondev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ipsilondev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24850" class="comments-container">
&#10;</div>
<div id="comment-tools-24850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24850-form-container" class="comment-form-container">
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

<span id="24852"></span>

<div id="answer-container-24852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24852-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most likely the drive you are running this on has less than 20 GB of free space available. The fact that osm2pgsql reports "Failed... Success" is due to a small bug in osm2pgsql (<a href="https://github.com/openstreetmap/osm2pgsql/issues/55)">https://github.com/openstreetmap/osm2pgsql/issues/55)</a> but the failure is real. Unless you are importing a very large data set, simply dropping the --flat-nodes is probably the best solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '13, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '13, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-24852" class="comments-container">
&#10;</div>
<div id="comment-tools-24852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24852-form-container" class="comment-form-container">
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

