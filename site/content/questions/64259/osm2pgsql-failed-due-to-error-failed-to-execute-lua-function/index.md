+++
type = "question"
title = "Osm2pgsql failed due to ERROR: Failed to execute lua function"
description = '''hello  i am following this  https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site but getting bellow error , how can i fix this ? yuma@bdmap:~/data$ osm2pgsql -d gis --create --slim -C 2500 --number-processes 4 -S ~/src/openstreetmap-carto-AJT/openstreetmap...'''
date = "2018-06-19T16:50:00Z"
lastmod = "2018-06-21T11:18:00Z"
weight = 64259
keywords = [ "osm" ]
aliases = [ "/questions/64259" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Osm2pgsql failed due to ERROR: Failed to execute lua function](/questions/64259/osm2pgsql-failed-due-to-error-failed-to-execute-lua-function)

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
<span id="post-64259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64259-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello i am following this <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site</a></p>
<p>but getting bellow error , how can i fix this ?</p>
<pre><code>yuma@bdmap:~/data$ osm2pgsql -d gis --create --slim -C 2500 --number-processes 4 -S ~/src/openstreetmap-carto-AJT/openstreetmap-carto.style --multi-geometry --tag-transform-script ~/src/SomeoneElse-style/style.lua ~/data/bangladesh-latest.osm.pbf
osm2pgsql version 0.96.0 (64 bit id space)
&#10;Using lua based tag processing pipeline with script /home/yuma/src/SomeoneElse-style/style.lua
Using projection SRS 3857 (Spherical Mercator)
Setting up table: planet_osm_point
Setting up table: planet_osm_line
Setting up table: planet_osm_polygon
Setting up table: planet_osm_roads
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2500MB, maxblocks=40000*65536, allocation method=11
Mid: pgsql, cache=2500
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
&#10;Reading in file: /home/yuma/data/bangladesh-latest.osm.pbf
Using PBF parser.
Processing: Node(30674k 45.2k/s) Way(38k 4.75k/s) Relation(0 0.00/s)node cache:                                                                                         stored: 30674137(100.00%), storage efficiency: 50.51% (dense blocks: 400, sparse                                                                                         nodes: 28723161), hit rate: 100.00%
Osm2pgsql failed due to ERROR: Failed to execute lua function for basic tag proc                                                                                        essing: /home/yuma/src/SomeoneElse-style/style.lua:16: attempt to perform arithm                                                                                        etic on field &#39;layer&#39; (a string value)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '18, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-64259" class="comments-container">
&#10;</div>
<div id="comment-tools-64259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64259-form-container" class="comment-form-container">
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

<span id="64302"></span>

<div id="answer-container-64302" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64302-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This was caused by a <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/issues/5#issuecomment-398679696">bug</a> in the lua style which was exposed when osm2pgsql was <a href="https://github.com/openstreetmap/osm2pgsql/pull/845#issuecomment-398529869">changed</a> to not ignore the problem.</p>
<p>What I don't understand was why the problem was visible when Bangladesh was loaded but not other areas with invalid layer data, but it's now fixed for everywhere (thanks to <a href="https://www.openstreetmap.org/user/mmd">mmd</a> for pointing that out).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '18, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-64302" class="comments-container">
&#10;</div>
<div id="comment-tools-64302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64302-form-container" class="comment-form-container">
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

