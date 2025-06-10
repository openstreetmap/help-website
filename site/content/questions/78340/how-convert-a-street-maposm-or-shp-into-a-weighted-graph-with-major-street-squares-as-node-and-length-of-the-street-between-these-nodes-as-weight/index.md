+++
type = "question"
title = "How convert a street map(.osm or .shp) into a weighted graph with major street squares as node and length of the street between these nodes as weight?"
description = '''To apply algorithms like Dijkstra on a graph, we need nodes and the distance between each node as weights. In real world these weighted graphs are actual maps and the weights are distance of road. We are looking for a library or a tool which we can be used to convert these map files(.shp or .osm) in...'''
date = "2021-01-13T06:27:00Z"
lastmod = "2021-02-03T16:02:00Z"
weight = 78340
keywords = [ "maptograph", "dijkstra", "roaddistance", "streetdistance", "distance" ]
aliases = [ "/questions/78340" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How convert a street map(.osm or .shp) into a weighted graph with major street squares as node and length of the street between these nodes as weight?](/questions/78340/how-convert-a-street-maposm-or-shp-into-a-weighted-graph-with-major-street-squares-as-node-and-length-of-the-street-between-these-nodes-as-weight)

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
<span id="post-78340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78340-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>To apply algorithms like Dijkstra on a graph, we need nodes and the distance between each node as weights. In real world these weighted graphs are actual maps and the weights are distance of road. We are looking for a library or a tool which we can be used to convert these map files(.shp or .osm) into a weighted graph or an adjacency matix?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maptograph" rel="tag" title="see questions tagged &#39;maptograph&#39;">maptograph</span> <span class="post-tag tag-link-dijkstra" rel="tag" title="see questions tagged &#39;dijkstra&#39;">dijkstra</span> <span class="post-tag tag-link-roaddistance" rel="tag" title="see questions tagged &#39;roaddistance&#39;">roaddistance</span> <span class="post-tag tag-link-streetdistance" rel="tag" title="see questions tagged &#39;streetdistance&#39;">streetdistance</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '21, 06:27</strong></p>
<img src="https://secure.gravatar.com/avatar/76b70ea75f46003eb94b8e2b4809d918?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartikeya&#39;s gravatar image" />
<p><span>Kartikeya</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartikeya has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78340" class="comments-container">
&#10;</div>
<div id="comment-tools-78340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78340-form-container" class="comment-form-container">
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

<span id="78342"></span>

<div id="answer-container-78342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78342-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of tools which will populate the pgrouting schema in PostGIS from OSM data too: <a href="https://github.com/pgRouting/osm2pgrouting">osm2pgrouting</a> and <a href="http://osm2po.de/">osm2po</a> (latter is closed source proprietary software). You can readily interrogate the pgrouting tables with SQL queries and use different algorithms &amp; weights for routing, so although not the most efficient routing method it's quite a good set-up for experimentation.</p>
<p>Anita Graser has written a number of <a href="https://anitagraser.com/2011/02/07/a-beginners-guide-to-pgrouting/">tutorials</a> about pgrouting itself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '21, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-78342" class="comments-container">
<span id="78647"></span>
<div id="comment-78647" class="comment">
<div id="post-78647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. We just wanted to find the shortest path by a* or dijkstra, but not by any API. We have an osm file and want to extract nodes, edges and the distance between nodes from the same file(python preferably).</p>
</div>
<div id="comment-78647-info" class="comment-info">
<span class="comment-age">(03 Feb '21, 16:02)</span> <span class="comment-user userinfo">Kartikeya</span>
</div>
</div>
</div>
<div id="comment-tools-78342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78342-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78341"></span>

<div id="answer-container-78341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78341-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/Tristramg/osm4routing2">https://github.com/Tristramg/osm4routing2</a> is the easiest I've found to create a routing graph from OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '21, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-78341" class="comments-container">
&#10;</div>
<div id="comment-tools-78341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78341-form-container" class="comment-form-container">
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

