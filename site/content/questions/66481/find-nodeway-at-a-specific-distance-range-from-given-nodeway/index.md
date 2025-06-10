+++
type = "question"
title = "Find node/way at a specific distance range from given node/way"
description = '''I&#x27;m using Overpass query to identify the nodes with a specific tag that are located only within a certain distance range from node with another specific tag. This sounds similar to this question related to proxmity search and this other distance calculation between nodes question.  But to tell the d...'''
date = "2018-10-26T09:13:00Z"
lastmod = "2018-10-26T09:13:00Z"
weight = 66481
keywords = [ "distance", "osm", "routing", "overpass-ql" ]
aliases = [ "/questions/66481" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find node/way at a specific distance range from given node/way](/questions/66481/find-nodeway-at-a-specific-distance-range-from-given-nodeway)

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
<span id="post-66481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66481-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using Overpass query to identify the nodes with a specific tag that are located only within a certain distance range from node with another specific tag. This sounds similar to <a href="https://help.openstreetmap.org/questions/33089/proximity-search-node-with-tag1-near-node-with-tag2">this</a> question related to proxmity search and <a href="https://help.openstreetmap.org/questions/32190/calculate-distance-from-one-node-to-several-other-nodes-in-area">this other</a> distance calculation between nodes question.</p>
<p>But to tell the difference, I can try to explain with an example.</p>
<p>Find a cafe within a distance range of 450 m and 550 m from a library or</p>
<p>Find a gas station with a distance range of 9 km and 11 km from IKEA or</p>
<p>Find the railway crossing that is between a distance 900 m and 1100 m from a train station.</p>
<p>Query for 2nd search:</p>
<p><code>[timeout:300]; way[name=IKEA]({{bbox}}) -&gt; .i; ((node[amenity=fuel](around.i:1100); way[amenity=fuel](around.i:1100););); out geom;</code></p>
<p><code>[timeout:300]; way[name=IKEA]({{bbox}}) -&gt; .i; ((node[amenity=fuel](around.i:1100); way[amenity=fuel](around.i:1100););-((node[amenity=fuel](around.i:900); way[amenity=fuel](around.i:900);););); out geom;</code></p>
<p>I have used <code>.around</code> to specify the range limits and used <code>out geom 1</code> to limit my result with only 1 output. For these 3 queries, the distance provided to <code>.around</code> clause will be considered as a direct distance and not the routing distance for a car or a train. How can I make sure that the train travels 0.9 to 1.1 km from station to the rail-crossing.</p>
<p>I wish to know if it is at all possible to achieve such query in Overpass. It would be great if there is confirmation for the same or suggestion to make this work through other method.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '18, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ef1bb309497d56d45a23249ef5fdff4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1894&#39;s gravatar image" />
<p><span>user1894</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1894 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66481" class="comments-container">
&#10;</div>
<div id="comment-tools-66481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66481-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

