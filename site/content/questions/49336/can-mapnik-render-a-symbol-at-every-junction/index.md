+++
type = "question"
title = "Can Mapnik render a symbol at every junction?"
description = '''Is there a way for Mapnik to render a symbol at every junction? I can&#x27;t find an obvious rule. I don&#x27;t mean each node along a line - just where two lines properly intersect at a junction, on the same level with a joining node (i.e. not say at a bridge). Mapnik seems to have &amp;lt;Filter&amp;gt;[mapnik::geo...'''
date = "2016-04-21T12:54:00Z"
lastmod = "2016-04-21T18:08:00Z"
weight = 49336
keywords = [ "mapnik" ]
aliases = [ "/questions/49336" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can Mapnik render a symbol at every junction?](/questions/49336/can-mapnik-render-a-symbol-at-every-junction)

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
<span id="post-49336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way for Mapnik to render a symbol at every junction? I can't find an obvious rule.</p>
<p>I don't mean each node along a line - just where two lines properly intersect at a junction, on the same level with a joining node (i.e. not say at a bridge).</p>
<p>Mapnik seems to have</p>
<pre><code>&lt;Filter&gt;[mapnik::geometry_type]=point&lt;/Filter&gt;</code></pre>
<p>but that will presumably give me every node, not purely the junctions.</p>
<p>I'm trying to create a rendering showing where there are proper junctions, not things which appear to be junctions but aren't actually connected properly. (I'm aware that there are great tools like KeepRight for this, but I'm working on custom data that needs such a debugging layer.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '16, 12:54</strong></p>
<img src="https://secure.gravatar.com/avatar/354d4e3cc1b448abb29eb4f1bbac395c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fooquency&#39;s gravatar image" />
<p><span>fooquency</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fooquency has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49336" class="comments-container">
&#10;</div>
<div id="comment-tools-49336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49336-form-container" class="comment-form-container">
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

<span id="49338"></span>

<div id="answer-container-49338" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49338-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fooquency has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a question of Mapnik being able to do something; the question is whether you can get your data source to compute these locations. (Mapnik's responsibility would then consist of placing an icon there, no more.)</p>
<p>If the data comes from shape files then you're out of luck since there's no geo processing available.</p>
<p>If the data comes from a PostGIS database then you could mark all intersections between two bits of road like this:</p>
<pre><code>SELECT st_intersection(a, b) AS geom
FROM planet_osm_line a, planet_osm_line b
WHERE a.highway IS NOT NULL
AND b.highway IS NOT NULL
AND st_intersects(a,b);</code></pre>
<p>or substitute your own table and attributes instead of <code>planet_osm_line</code> and <code>highway</code>. Note that while this will be correct in one direction (a road that ends near, instead of on, another road will never show an icon) it is not necessarily correct in the other (an icon shown on the map does not necessarily mean that you can turn into the other road there). That's because the "simple feature" geometries don't have topology and cannot differentiate between two streets actually being connected (i.e. same node id in OSM) and two streets just incidentally being in the same location without being connected (e.g. due to a different z order).</p>
<p>You can correct for some of that by adding stuff like <code>and ((a.bridge is null and b.bridge is null) or (a.bridge=b.bridge))</code> etc but it is always going to be guesswork.</p>
<p>In the OSM world you could get perfect results by evaluating the planet_osm_ways table which is generated when you run osm2pgsql with <code>--slim</code>, however this is a bit complicated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '16, 13:09</strong> </span></p>
</div>
</div>
<div id="comments-container-49338" class="comments-container">
<span id="49343"></span>
<div id="comment-49343" class="comment">
<div id="post-49343-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could probably extend this slightly by, after the intersection test on the lines, take the sets of vertices in the linestrings (st_dumppoints) and see if the sets include a common member. That will still have some false positives where OSM ways have independent nodes with identical coordinates, but at least remove almost all the bridges and tunnels where nodes aren't coincident.</p>
</div>
<div id="comment-49343-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 14:26)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="49347"></span>
<div id="comment-49347" class="comment">
<div id="post-49347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Frederik and Andy - this is most useful.</p>
</div>
<div id="comment-49347-info" class="comment-info">
<span class="comment-age">(21 Apr '16, 17:47)</span> <span class="comment-user userinfo">fooquency</span>
</div>
</div>
</div>
<div id="comment-tools-49338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49338-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49348"></span>

<div id="answer-container-49348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49348-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I recently put together a little tool to identify junctions, defined as "any node with more than two highways calling at it". It takes an .osm.pbf as input, and outputs a CSV of lat, lon, and junction type (a compound string enumerating the highway values). It may not slot into your workflow, and it almost certainly requires some tweaking to suit, but you may find it useful: <a href="https://github.com/systemed/intersector">https://github.com/systemed/intersector</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '16, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-49348" class="comments-container">
&#10;</div>
<div id="comment-tools-49348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49348-form-container" class="comment-form-container">
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

