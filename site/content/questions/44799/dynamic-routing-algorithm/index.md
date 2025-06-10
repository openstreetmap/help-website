+++
type = "question"
title = "[closed] Dynamic routing algorithm"
description = '''I have a graph extracted from an American city: vertices represent road intersections, edges/arcs represent road segments connecting the intersections. For each road segment, I have the length and allowed driving speed. Furthermore, roads belong to different classes such as highway/residential/prima...'''
date = "2015-08-18T04:32:00Z"
lastmod = "2015-08-18T17:46:00Z"
weight = 44799
keywords = [ "routing", "algorithm" ]
aliases = [ "/questions/44799" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Dynamic routing algorithm](/questions/44799/dynamic-routing-algorithm)

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
<span id="post-44799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44799-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a graph extracted from an American city: vertices represent road intersections, edges/arcs represent road segments connecting the intersections. For each road segment, I have the length and allowed driving speed. Furthermore, roads belong to different classes such as highway/residential/primary roads/....</p>
<p>I am looking for a routing algorithm which does the following:</p>
<ul>
<li>Compute a pairwise travel time matrix for each intersection (i.e how long it would take to travel from intersection i to intersection j.</li>
<li>Query the quickest route from intersection i to j and returns a path (sequence of edges/arcs). The algorithm should be able to take updates into consideration. For instance, if there is a congestion on road segment (x,y) which increases its anticipated travel time, or if road segment (x,y) becomes blocked, the data structures should be updated incrementally, thereby updating all affected shortest paths (i.e. update all shortest paths through (x,y)).</li>
<li>The distance matrix will be queried very often so this should be precomputed, but the actual shortest paths can be computed at a later stage if that's more efficient. The number of nodes in the graph is roughly 5000-10000.</li>
</ul>
<p>I was hoping that people could refer me to literature about this, preferably something that doesn't take weeks to implement. Obviously, simply running Dijkstra for each intersection takes too long. Running Floyd–Warshall all-pairs shortest path algorithm could be a possibility, but I'm not so sure how to update the result if the cost of one of the edges/arcs changes. Furthermore, it seems to be a slow approach since the algorithm ignores that most of the routes go through a small subset of the road segments.</p>
<p>I'm not looking for an exact approach. A good approximation suffices. Any pointers to literature or algorithm descriptions are welcome. I presume that any kind of routing software needs a similar algorithm. I'm mainly interested in something that works; it shouldn't necessarily be state of the art. I'm not sure what would be a good place to ask this question?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '15, 04:32</strong></p>
<img src="https://secure.gravatar.com/avatar/6feb1ed05cdbdc6c0d788f514fd07e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorisK&#39;s gravatar image" />
<p><span>JorisK</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorisK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Aug '15, 12:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-44799" class="comments-container">
<span id="44807"></span>
<div id="comment-44807" class="comment">
<div id="post-44807-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>I'm not sure what would be a good place to ask this question?</p>
</blockquote>
<p>Since I cannot find any immediate connection to OpenStreetMap in your question (maybe you just forgot to mention it?), may I suggest to try on gis.stackexchange.com instead and close this question?</p>
<p>OSM universe offers different routers like OSRM or GraphHopper. Please give the search on this page a try.</p>
</div>
<div id="comment-44807-info" class="comment-info">
<span class="comment-age">(18 Aug '15, 17:46)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-44799" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44799-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant. Generic question with no OSM content, more suitable for GIS StackExchange." by SK53 19 Aug '15, 12:52

</div>

</div>

</div>

