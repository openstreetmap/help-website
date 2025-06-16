+++
type = "question"
title = "How to route origin to destination using only OSM data?"
description = '''Hi, Using a ready made open source API is not an option. All I have to work with is filtered OSM data consisting of only nodes of roads and ways. Can somebody please give me some insight regarding how I can draw a route from an origin to a destination node? I&#x27;m struggling to see how routing algorith...'''
date = "2014-02-19T18:03:00Z"
lastmod = "2014-02-20T16:32:00Z"
weight = 30843
keywords = [ "ways", "nodes", "dijkstra", "osm", "routing" ]
aliases = [ "/questions/30843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to route origin to destination using only OSM data?](/questions/30843/how-to-route-origin-to-destination-using-only-osm-data)

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
<span id="post-30843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, Using a ready made open source API is not an option. All I have to work with is filtered OSM data consisting of only nodes of roads and ways.</p>
<p>Can somebody please give me some insight regarding how I can draw a route from an origin to a destination node?</p>
<p>I'm struggling to see how routing algorithms such as Dijkstra or A* fit in with nodes &amp; ways.</p>
<p>Any help would be appreciated.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-dijkstra" rel="tag" title="see questions tagged &#39;dijkstra&#39;">dijkstra</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '14, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/56d5ec9b3e908fa8e2b33e604f334284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyanite&#39;s gravatar image" />
<p><span>Kyanite</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyanite has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '14, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-30843" class="comments-container">
<span id="30859"></span>
<div id="comment-30859" class="comment">
<div id="post-30859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sounds like a student homework...</p>
</div>
<div id="comment-30859-info" class="comment-info">
<span class="comment-age">(20 Feb '14, 16:32)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-30843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30843-form-container" class="comment-form-container">
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

<span id="30844"></span>

<div id="answer-container-30844" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30844-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-30844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are already lots of <a href="https://wiki.openstreetmap.org/wiki/Routing#Libraries.2FDevelopment-Tools">libraries</a> as well as <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">online offline</a> and <a href="https://wiki.openstreetmap.org/wiki/Routing/offline_routers">offline routers</a> and <a href="https://wiki.openstreetmap.org/wiki/Routing#See_also">general information about routing with OSM</a>.</p>
<p>If you want to implement your own routing solution, you need a proper routing graph. Use the search words "network" or "graph" on this help site to find previous questions that deal with extracting routing graphs from OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '14, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '14, 22:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-30844" class="comments-container">
&#10;</div>
<div id="comment-tools-30844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30844-form-container" class="comment-form-container">
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

