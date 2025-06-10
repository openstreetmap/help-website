+++
type = "question"
title = "How capture  zooming operation JMapViewer"
description = '''Does Anyone know how I can capture zooming operation? I need to scale an image according to the zoom. how is called this operation and how can I capture it?'''
date = "2014-10-05T00:58:00Z"
lastmod = "2014-10-05T08:52:00Z"
weight = 37305
keywords = [ "josm", "jmapviewer", "osm" ]
aliases = [ "/questions/37305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How capture zooming operation JMapViewer](/questions/37305/how-capture-zooming-operation-jmapviewer)

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
<span id="post-37305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37305-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does Anyone know how I can capture zooming operation? I need to scale an image according to the zoom. how is called this operation and how can I capture it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-jmapviewer" rel="tag" title="see questions tagged &#39;jmapviewer&#39;">jmapviewer</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '14, 00:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3f61c27a1a925da107eb8c38d3392b6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scupetta18&#39;s gravatar image" />
<p><span>scupetta18</span><br />
<span class="score" title="-3 reputation points">-3</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scupetta18 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37305" class="comments-container">
&#10;</div>
<div id="comment-tools-37305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37305-form-container" class="comment-form-container">
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

<span id="37307"></span>

<div id="answer-container-37307" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So you mean something like this <a href="http://openlayers.org/en/v3.0.0/examples/animation.html">animated example</a> in Openlayers3 ? (choose "Fly to Bern" there)</p>
<p>Getting such a captured animation based on OSM map graphic is a task that I am <em>looking for years</em> already.</p>
<p>Marble is said to have such a feature: you can define at least two bookmarks for two position, choose right animation parameters in Marble's settings, and by choosing each bookmark you get an animation with zooming out and in again. And in recent releases Marble has a video catpture feature. But it <em>does not work</em> on my Win7 machine.</p>
<p>(So anybode here who manages to capture a video in Marble on windows (also Linux reports would be nice) please give a step-by-step how-to here.)</p>
<p>Then: via <a href="http://wiki.openstreetmap.org/wiki/Party_render">Party-Renderer</a> I came across <a href="http://zdila.github.io/gpx-animator/">GPX-animator</a> ... but no panning / zooming features there?</p>
<p>Some guys in the <a href="http://forum.openstreetmap.org/viewforum.php?id=42">OSM 3D forum</a> (see also <a href="http://wiki.openstreetmap.org/wiki/3D_Development">3D Development</a>) are doing things with <a href="http://wiki.openstreetmap.org/wiki/Blender">Blender</a> ... maybe we can feed blender with a simple OSM based map and capture any zooming/panning? Just seen: there is an OSM import plugin!!</p>
<p>Furthermore there are noumerous frameworks that are able to display OSM based maps via WebGL or OpenGL ... search for Tangram, Avecado, MapBox GL or others (search OSM wiki) ... maybe they can do the required rendering and animation that is captured then easily.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '14, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '14, 08:53</strong> </span></p>
</div>
</div>
<div id="comments-container-37307" class="comments-container">
&#10;</div>
<div id="comment-tools-37307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37307-form-container" class="comment-form-container">
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

