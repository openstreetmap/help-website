+++
type = "question"
title = "Identify &#x27;transit highways&#x27; in Germany"
description = '''So I have imported the map of OSM map of Austria into my PostGIS database using the osm2pgsql tool. My problem is the identification of transit highways in Austria.  There is an attribute called highway within the planet_osm_line (and also the planet_osm_roads) table. The highway tag used with the v...'''
date = "2019-05-29T05:30:00Z"
lastmod = "2019-05-29T10:03:00Z"
weight = 69358
keywords = [ "motorway", "germany", "osm", "osm2pgsql", "highway" ]
aliases = [ "/questions/69358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Identify 'transit highways' in Germany](/questions/69358/identify-transit-highways-in-germany)

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
<span id="post-69358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69358-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I have imported the map of OSM map of Austria into my PostGIS database using the osm2pgsql tool.</p>
<p>My problem is the identification of <strong>transit highways</strong> in Austria.</p>
<p>There is an attribute called highway within the planet_osm_line (and also the planet_osm_roads) table. The highway tag used with the value 'motorway' can be used to isolate an Austrian/German <strong>Autobahn</strong>.</p>
<p>The definition of transit highways is this - "..<strong>highways dedicated to publically accessible transit buses</strong>..".</p>
<p>In other words, it is a dedicated right-of-way or roadway used by transit vehicles, usually buses.</p>
<p>Could you please help me select/identify the right attributes from the 'planet_osm_roads' table that can selectively identify <strong>transit highways</strong>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '19, 05:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0f1df60051a6f0ba2d7aeaac57441c49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sujay&#39;s gravatar image" />
<p><span>Sujay</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sujay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69358" class="comments-container">
&#10;</div>
<div id="comment-tools-69358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69358-form-container" class="comment-form-container">
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

<span id="69361"></span>

<div id="answer-container-69361" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69361-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not aware of many such highways in Germany. What we have a lot are lanes dedicated to buses and/or public transport in general.</p>
<p>You'll find that they are probably tagged in different ways. A highway only dedicated to buses could be tagged with access=no, psv=yes/designated or bus=yes/designated. For lanes it would be something like <a href="https://wiki.openstreetmap.org/wiki/Key:access#Lane_dependent_restrictions">vehicle:lanes=yes|yes|no + psv:lanes=yes|yes|designated</a>.</p>
<p>There is also a key <a href="https://wiki.openstreetmap.org/wiki/DE:Key:busway">busway</a> but I have never seen it being used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69361" class="comments-container">
&#10;</div>
<div id="comment-tools-69361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69361-form-container" class="comment-form-container">
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

