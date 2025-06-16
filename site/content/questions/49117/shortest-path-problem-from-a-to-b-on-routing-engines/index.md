+++
type = "question"
title = "[closed] Shortest path problem from A to B on routing engines"
description = '''I am in the process of creating a routing engine. I have encountered the following problem. Lets say the user gives a point A and point B and expects to get the A-&amp;gt;B shortest path. I am using simple Dijkstra for now. Let&#x27;s say that I can somehow find the (latitudeA, longitudeA) and (latitudeB, lo...'''
date = "2016-04-08T19:07:00Z"
lastmod = "2016-04-09T17:20:00Z"
weight = 49117
keywords = [ "engine", "path", "dijkstra", "routing", "shortest" ]
aliases = [ "/questions/49117" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Shortest path problem from A to B on routing engines](/questions/49117/shortest-path-problem-from-a-to-b-on-routing-engines)

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
<span id="post-49117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49117-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am in the process of creating a routing engine. I have encountered the following problem. Lets say the user gives a point A and point B and expects to get the A-&gt;B shortest path. I am using simple Dijkstra for now.</p>
<p>Let's say that I can somehow find the <code>(latitudeA, longitudeA)</code> and <code>(latitudeB, longitudeB)</code> coordinates, which are the closest coordinates to the A and B points that the user inputted. From those coordinates I could then also find the <code>nodeA_ID</code> and <code>nodeB_ID</code> on the graph. The problem is that for those nodes it is very likely that the A-&gt;B path doesn't exist at all. For example, if node A was only part of a one-way road that went to the opposite direction that the user wanted to go to.</p>
<p>However, a <strong>A'</strong> and <strong>B'</strong> must exist, <em>very close</em> to A and B respectively, so that the <strong>A'-&gt;B'</strong> path exists. So the routing engine should try and find that <strong>A'-&gt;B'</strong> path instead.</p>
<p>Also, that <strong>A'-&gt;B'</strong> path might not even be <strong>optimal</strong>. There could have been a <strong>A''-&gt;B''</strong> path, where A'' and B'' were only a couple of meters away from A and B. So the routing engine should find the <strong>A''-&gt;B''</strong> optimal path instead.</p>
<p>How do routing engines handle this situation ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-engine" rel="tag" title="see questions tagged &#39;engine&#39;">engine</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-dijkstra" rel="tag" title="see questions tagged &#39;dijkstra&#39;">dijkstra</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-shortest" rel="tag" title="see questions tagged &#39;shortest&#39;">shortest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '16, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/029b463e5af8b5dc5d6094a7a4686c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shiro900&#39;s gravatar image" />
<p><span>shiro900</span><br />
<span class="score" title="54 reputation points">54</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shiro900 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>09 Apr '16, 17:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-49117" class="comments-container">
<span id="49121"></span>
<div id="comment-49121" class="comment">
<div id="post-49121-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"The problem is that for those nodes it is very likely that the A-&gt;B path doesn't exist at all. For example, if that node was part of a one-way road that went to the opposite direction that the user wanted to go to."</p>
<p>In such a case, the shortest route would still exist but just go in a different direction. A dead-end oneway should never exist on the ground and only rarely occur in the data as a tagging error, so I wouldn't call it "likely". Assuming the data is generally correctly-connected, there should almost always be some way to route.</p>
</div>
<div id="comment-49121-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 19:29)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="49122"></span>
<div id="comment-49122" class="comment">
<div id="post-49122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> It doesn't have to be a dead-end. It could be a very long oneway road that would make you drive twice as long to go to your target location</p>
</div>
<div id="comment-49122-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 19:32)</span> <span class="comment-user userinfo">shiro900</span>
</div>
</div>
<span id="49124"></span>
<div id="comment-49124" class="comment">
<div id="post-49124-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well if your car <em>is</em> on the very long oneway road going in the wrong direction then it is little use to you if the routing engine says "hey, I found a point A' very near the point you are at, and from there the way is much shorter".</p>
</div>
<div id="comment-49124-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 20:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="49125"></span>
<div id="comment-49125" class="comment">
<div id="post-49125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@FrederikRamm I think you might be right here. I will see how good my routing engine works once I implement it successfully so that I can visualize the results with google maps.</p>
</div>
<div id="comment-49125-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 21:46)</span> <span class="comment-user userinfo">shiro900</span>
</div>
</div>
<span id="49126"></span>
<div id="comment-49126" class="comment not_top_scorer">
<div id="post-49126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12082/shiro900">@shiro900</a>: why "google maps"? Did you hear of OSM already? ;-) Please use OSM!</p>
</div>
<div id="comment-49126-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 22:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49129"></span>
<div id="comment-49129" class="comment not_top_scorer">
<div id="post-49129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@seerel4c26 Oh yes, I will definitely try OSM! I just had the google maps already set up.</p>
</div>
<div id="comment-49129-info" class="comment-info">
<span class="comment-age">(09 Apr '16, 09:30)</span> <span class="comment-user userinfo">shiro900</span>
</div>
</div>
<span id="49133"></span>
<div id="comment-49133" class="comment">
<div id="post-49133-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Same question was also posted here: <a href="http://gis.stackexchange.com/questions/188677/shortest-path-problem-from-a-to-b-on-routing-engines">http://gis.stackexchange.com/questions/188677/shortest-path-problem-from-a-to-b-on-routing-engines</a></p>
</div>
<div id="comment-49133-info" class="comment-info">
<span class="comment-age">(09 Apr '16, 17:20)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-49117" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49117-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question: another answer for the exact same question was already accepted on GIS StackExchange." by mmd 09 Apr '16, 17:22

</div>

</div>

</div>

