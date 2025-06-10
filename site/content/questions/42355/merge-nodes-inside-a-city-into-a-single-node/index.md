+++
type = "question"
title = "Merge nodes inside a city into a single node"
description = '''I&#x27;ve been using osm4routing to filter and formate OSM data as a graph and process it. However for my application (see 1) I don&#x27;t care about the &quot;insides&quot; of cities (/towns/villages/..), all I need is the fact that there is a city. Filtering out residential streets from osm4routing output is easy (se...'''
date = "2015-04-15T18:36:00Z"
lastmod = "2015-04-16T08:30:00Z"
weight = 42355
keywords = [ "cities" ]
aliases = [ "/questions/42355" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Merge nodes inside a city into a single node](/questions/42355/merge-nodes-inside-a-city-into-a-single-node)

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
<span id="post-42355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42355-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been using <a href="https://github.com/Tristramg/osm4routing">osm4routing</a> to filter and formate OSM data as a graph and process it. However for my application (see 1) I don't care about the "insides" of cities (/towns/villages/..), all I need is the fact that there is a city. Filtering out residential streets from osm4routing output is easy (see 2) but this still leaves nodes which represent road junctions and similar. How can I merge all the nodes inside a city to a single node? This node should be incident to all the edges which were connected to the city. I was hoping that there was something which would help me distinguish which node belongs to a city. I tried looking at the addr key but I am not sure whether all objects inside a city have this properly assigned. The boundary information seems also plausible but again I don't know about the reliability and also this seems to be harder to do. Due to the size of the data I am of course looking for a general rule (since I can't do this manually).</p>
<p>1) Analysis of road network on state, or continental level, not city infrastructural level.</p>
<p>2) just select the lines of the edges file s.t. they have number &gt;1 in the fifth column</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '15, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/00064d48f1015dcb9bbd41d83c4c3ee5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ondrejsl&#39;s gravatar image" />
<p><span>ondrejsl</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ondrejsl has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '15, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-42355" class="comments-container">
&#10;</div>
<div id="comment-tools-42355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42355-form-container" class="comment-form-container">
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

<span id="42372"></span>

<div id="answer-container-42372" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42372-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-42372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ondrejsl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an interesting question about how to generalise OSM data. In practice there is no easy way.</p>
<p>You could use one of the following ways to try &amp; identify built-up areas:</p>
<ul>
<li>Merge certain landuse classes (residential, commercial, industrial, retail,etc) together with some amenity areas (hospital, university, college, school) and some leisure areas (park, recreation_ground) to create a proxy for built-up areas. This will only work when landuse has been mapped, and it becomes harder when landuse has been mapped in detail.</li>
<li>Use the density of residential streets. This has been done using RapidMiner by the GIS group at Heidelberg University.</li>
<li>Simply use a standard size buffer around place nodes (say 5km for cities, 2km for towns &amp; 1 or 0.5 km for villages). This could be refined by using voronoi triangles to handle cases where places are distinct but their buffer zones would overlap.</li>
</ul>
<p>I presume you are ignoring residential streets, so once you have some approximation of built-up areas linked to the actual OSM element describing the place, you need to clip the road network using the built-up areas. It is important that you identify which place a given road belongs to before clipping. This can be done by identifying which roads intersect the perimeter of each built-up area.</p>
<p>The dangling ends of the roads are then connected to a single node representing the city (typically I'd use the existing OSM node or centroid of other elements for this).</p>
<p>This represents a considerable amount of post-processing of OSM data, which requires knowledge of geometries. Personally I'd do this in a database such as PostgreSQL with PostGIS. An additional problem then arises because you may want the data in OSM XML format for building your graph. Mainly this involves re-working the way_nodes table for truncated ways. All additional artificial path links are not really a problem as these can be created with negative ids outside the range of ids in use.</p>
<p>For other post-processing of OSM data for routing take a look at some other applications.</p>
<p><strong>Note</strong> the process as described may create inaccurate graphs (specifically a road which loops into a 'city' area and out again may be incorrectly connected to that city.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '15, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-42372" class="comments-container">
&#10;</div>
<div id="comment-tools-42372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42372-form-container" class="comment-form-container">
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

