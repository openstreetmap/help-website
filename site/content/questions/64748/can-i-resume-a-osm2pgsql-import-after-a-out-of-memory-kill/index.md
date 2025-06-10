+++
type = "question"
title = "Can I resume a osm2pgsql import after a out-of-memory-kill?"
description = '''I have a lengthy osm2pgsql import that failed due to insufficient memory. I have added 16GB af cache and would like to resume the process if possible. Based on the following, is this possible or do I need to restart? osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstree...'''
date = "2018-07-16T14:09:00Z"
lastmod = "2018-07-16T17:48:00Z"
weight = 64748
keywords = [ "resume", "osm2pgsql", "memory" ]
aliases = [ "/questions/64748" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I resume a osm2pgsql import after a out-of-memory-kill?](/questions/64748/can-i-resume-a-osm2pgsql-import-after-a-out-of-memory-kill)

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
<span id="post-64748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64748-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a lengthy osm2pgsql import that failed due to insufficient memory. I have added 16GB af cache and would like to resume the process if possible. Based on the following, is this possible or do I need to restart?</p>
<pre><code>osm2pgsql -d gis --create --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2000 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/europe-latest.osm.pbf
osm2pgsql version 0.95.0-dev (64 bit id space)
Using lua based tag processing pipeline with script /home/ge/src/openstreetmap-carto/openstreetmap-carto.lua
Using projection SRS 3857 (Spherical Mercator)
Setting up table: planet_osm_point
Setting up table: planet_osm_line
Setting up table: planet_osm_polygon
Setting up table: planet_osm_roads
Allocating memory for dense node cache
Allocating dense node cache in one big chunk
Allocating memory for sparse node cache
Sharing dense sparse
Node-cache: cache=2000MB, maxblocks=32000*65536, allocation method=11
Mid: pgsql, cache=2000
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Reading in file: /home/ge/data/europe-latest.osm.pbf
Using PBF parser.
Processing: Node(2034978k 40.7k/s) Way(248018k 0.15k/s) Relation(3846660 3.73/s)  parse time: 2749907s
Node stats: total(2034978773), max(5396860910) in 49970s
Way stats: total(248018225), max(559553572) in 1668599s
Relation stats: total(3846682), max(7999697) in 1031338s
Committing transaction for planet_osm_point
Committing transaction for planet_osm_line
Committing transaction for planet_osm_polygon
Committing transaction for planet_osm_roads
Setting up table: planet_osm_nodes
Setting up table: planet_osm_ways
Setting up table: planet_osm_rels
Using lua based tag processing pipeline with script /home/ge/src/openstreetmap-carto/openstreetmap-carto.lua
Killed</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-resume" rel="tag" title="see questions tagged &#39;resume&#39;">resume</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '18, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/85c41cfa78ff7048eb6057c641d4746b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacknj&#39;s gravatar image" />
<p><span>Jacknj</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacknj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64748" class="comments-container">
&#10;</div>
<div id="comment-tools-64748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64748-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="64750"></span>

<div id="answer-container-64750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64750-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would definitely switch to <strong>--flat-nodes</strong> if you run out of memory, as this will store the nodes on disk instead of RAM. Especially with SSD, you shouldn't worry about slow imports with --flat-nodes. I recently succeeded to load the whole of Europe on a 12GB RAM virtual machine with plenty of disk space, but only after I dropped inclusion of advanced settings like cache, and simply let osm2pgsql itself figure out its optimal processing setting. It took just some 17 hours on a Core i7 laptop.</p>
<p>See here for a few more details and observations:</p>
<p><a href="https://forum.openstreetmap.org/viewtopic.php?id=62495">https://forum.openstreetmap.org/viewtopic.php?id=62495</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '18, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-64750" class="comments-container">
&#10;</div>
<div id="comment-tools-64750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64750-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64749"></span>

<div id="answer-container-64749" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not easily, no.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '18, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>16 Jul '18, 15:52</strong> </span></p>
</div>
</div>
<div id="comments-container-64749" class="comments-container">
&#10;</div>
<div id="comment-tools-64749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64749-form-container" class="comment-form-container">
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

