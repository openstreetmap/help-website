+++
type = "question"
title = "Using raw ways as arcs of road network (graph)"
description = '''I&#x27;m looking for algorithm which could help me with building my own road network (for routing) from OSM data. I chose Spatialite DB for this, but here I have only one problem: Spatialite provides interface for build road network, but prepared road graph is saved in BLOBS so I can&#x27;t get any informatio...'''
date = "2013-11-20T10:25:00Z"
lastmod = "2013-11-21T09:40:00Z"
weight = 28270
keywords = [ "ways", "junction", "network", "highway", "routing" ]
aliases = [ "/questions/28270" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using raw ways as arcs of road network (graph)](/questions/28270/using-raw-ways-as-arcs-of-road-network-graph)

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
<span id="post-28270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for algorithm which could help me with building my own road network (for routing) from OSM data.</p>
<p>I chose Spatialite DB for this, but here I have only one problem: Spatialite provides interface for build road network, but prepared road graph is saved in BLOBS so I can't get any information about it (of course, I can write queries to DB for routing facilities) but I want to draw all links on my map, so I need to get their coordinates.</p>
<p>Actually, I'm not sure if Spatialite could provide such API or smith like that.</p>
<p>I don't understand how to define junctions(links) between roads through all this data. <em>My first idea was that all ways could be used as the arcs of graph. But I'm not sure if they doesn't consist links inside them. I mean that in &lt;way&gt; first and last nodes always links and only they, whereas other nodes mentioned in this &lt;way&gt; is used only for geometry of they way</em></p>
<p>Is that statement right ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '13, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ae0b6110ad187821727e0f4e400c09ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TemaKrukovets&#39;s gravatar image" />
<p><span>TemaKrukovets</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TemaKrukovets has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28270" class="comments-container">
<span id="28271"></span>
<div id="comment-28271" class="comment">
<div id="post-28271-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is not quite correct. The first and the last node don't have to be links, a way can have one or even two open ends. Furthermore <em>every</em> node in the way can be part of one or more other ways, thus creating a junction. This is not limited to the first and last node.</p>
</div>
<div id="comment-28271-info" class="comment-info">
<span class="comment-age">(20 Nov '13, 10:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="28272"></span>
<div id="comment-28272" class="comment">
<div id="post-28272-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> , So, how can i define links to build graph? Manually look for nodes which mentioned in 2 or more ways ?</p>
</div>
<div id="comment-28272-info" class="comment-info">
<span class="comment-age">(20 Nov '13, 10:44)</span> <span class="comment-user userinfo">TemaKrukovets</span>
</div>
</div>
<span id="28273"></span>
<div id="comment-28273" class="comment">
<div id="post-28273-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Yes. But you wouldn't do that manually. Enter the term "graph" in the search box above and read some of the results.</p>
</div>
<div id="comment-28273-info" class="comment-info">
<span class="comment-age">(20 Nov '13, 10:51)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28270-form-container" class="comment-form-container">
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

<span id="28332"></span>

<div id="answer-container-28332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28332-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The preprocessing of OSM data for routing can be very tricky, as you have to take a lot of stuff into account (access and surface tags, restrictions, defaults per country, ...).</p>
<p>If you just like to create/try an routing algorithm, you might try <strong>this framework</strong>, that creates already a graph for you: <a href="http://code.google.com/p/trafficmining/">http://code.google.com/p/trafficmining/</a>. You might also consider other existing solutions as <strong>osm2pgrouting</strong> if you aren't tied to Spatiallite DB <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-28332" class="comments-container">
&#10;</div>
<div id="comment-tools-28332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28332-form-container" class="comment-form-container">
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

