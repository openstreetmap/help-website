+++
type = "question"
title = "Storing nodes, roads and intersections"
description = '''I need to be able to populate a database with nodes, ways and intersections/junctions. I&#x27;ve tried a number of approaches so far, without much luck. The closest I&#x27;ve got so far is loading the road shapefile for my region into the database via PostGis. This has given me a table with osm_ids however I&#x27;...'''
date = "2012-12-02T18:03:00Z"
lastmod = "2012-12-02T19:20:00Z"
weight = 18153
keywords = [ "ways", "nodes", "intersection", "junction", "database" ]
aliases = [ "/questions/18153" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Storing nodes, roads and intersections](/questions/18153/storing-nodes-roads-and-intersections)

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
<span id="post-18153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18153-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to be able to populate a database with nodes, ways and intersections/junctions. I've tried a number of approaches so far, without much luck. The closest I've got so far is loading the road shapefile for my region into the database via PostGis. This has given me a table with osm_ids however I'm not entirely sure whether they are node IDs or way IDs.</p>
<p>The issue here is that I require the nodes for the main purpose of the app, however <strong>I believe I need the ways in order to detect road intersections/junctions unless there's a way to find a list of junctions within the vicinity of a given node</strong>.</p>
<p>The idea is to be given a GPS coordinate and to relate it to node nearest to that location. Once detected, the app would find a list of junctions within X radius of this node.</p>
<p>I'm still very new to OSM as well as spatial databases, so I may have easily missed something along the way. Any help would be greatly appreciated as this critical component is the building block for the rest of this project.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '12, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/afbf8ac71c39825569d7ba732a0c304c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JuZeeMan&#39;s gravatar image" />
<p><span>JuZeeMan</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JuZeeMan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18153" class="comments-container">
&#10;</div>
<div id="comment-tools-18153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18153-form-container" class="comment-form-container">
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

<span id="18154"></span>

<div id="answer-container-18154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18154-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the third question you're asking here, and all are quite similar, and are essentially about the basics of spatial data processing. You might want to consider reading a book or introductory web site (this <a href="http://workshops.opengeo.org/postgis-intro/">OpenGeo workshop</a> is said to be excellent), or else pay someone to solve your problem.</p>
<p>I have already explained to you how you can find nearby roads in my <a href="https://help.openstreetmap.org/questions/17977/what-schematool-to-store-osm-gps-node-coordinates-in-database">previous answer;</a> now if you want to find intersections there's a number of different things you could do. The simplest is first extracting the roads in the vicinity of your location and then asking PostGIS for intersections which goes something like this:</p>
<pre><code>SELECT 
    st_intersection(a.geom, b.geom)
FROM 
    myroadstable a,
    myroadstable b
WHERE
    [ conditions to select nearby roads from a, b ]
AND
    st_intersects(a.geom, b.geom)</code></pre>
<p>This works even if your database does not have topology, i.e. if you have simply imported a shape file from somewhere. If you have imported an OSM database using Osmosis or osm2pgsql, you could also formulate a more precise query along the lines of "give me all nodes in the vicinity which are a member of two or more highways", thereby avoiding false positives when a road leads over another road in a tunnel/bridge situation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '12, 19:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18154" class="comments-container">
&#10;</div>
<div id="comment-tools-18154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18154-form-container" class="comment-form-container">
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

