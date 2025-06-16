+++
type = "question"
title = "Highlight the route of Bundesautobahn 4 (A4) on a map"
description = '''How can I safely visualize the route of Bundesautobahn 4 (relation 48147) to the default OSM map (ideally directly at osm.org)? Best way would be to highlight the route the same way like the current relations do. If the relation has no sub-relations then it draws itself nicely (like the A1 - though ...'''
date = "2019-05-19T09:46:00Z"
lastmod = "2019-05-22T17:04:00Z"
weight = 69227
keywords = [ "query", "visualize", "wikipedia", "query-to-map", "relations" ]
aliases = [ "/questions/69227" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Highlight the route of Bundesautobahn 4 (A4) on a map](/questions/69227/highlight-the-route-of-bundesautobahn-4-a4-on-a-map)

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
<span id="post-69227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69227-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I safely visualize the route of Bundesautobahn 4 (<a href="https://www.openstreetmap.org/relation/48147">relation 48147</a>) to the default OSM map (ideally directly at osm.org)? Best way would be to highlight the route the same way like the current relations do. If the relation has no sub-relations then it draws itself nicely (<a href="https://www.openstreetmap.org/relation/20904">like the A1</a> - though this relation is missing the north part of A1). But the problem with A4 is that it contains sub-relations with the actual route and these will not highligh anymore (<a href="/questions/7468">explained here</a>).</p>
<p>Yes I have been told relations are not stable over time, but I found this really is a general rule and some relations are very stable (10+ years) but it probably depends on how the local community treats relations, so they really are not 100 % stable.</p>
<p>So I probably want to run a query for A1 with some tags (network=BAB, ref="A 4"?) and highlight the result on a map. My point in using relations is that they are probably much (computationally) cheaper to retrieve from the server then a query, so I try to use them where possible. I see that the <a href="https://wiki.openstreetmap.org/wiki/Query-to-map">Query-to-map</a> at <a href="http://tools.wmflabs.org/query2map">http://tools.wmflabs.org/query2map</a> which may be what I am looking for is not working (503 Service Unavailable).</p>
<p>I actually want to use the map data (A1 route) to share it on Wikipedia. There is the <a href="https://wiki.openstreetmap.org/wiki/WIWOSM">WIWOSM</a> project that would work but the problem is it is not universal (not enabled on all Wikipedias - rather very few) and the articles need to contain coordinates in order for the WIWOSM link to be showed at the top of the page. And the articles about routes (Autobahns, railway lines etc.) usually do not contain any cooordinate so the WIWOSM link is not shown.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-visualize" rel="tag" title="see questions tagged &#39;visualize&#39;">visualize</span> <span class="post-tag tag-link-wikipedia" rel="tag" title="see questions tagged &#39;wikipedia&#39;">wikipedia</span> <span class="post-tag tag-link-query-to-map" rel="tag" title="see questions tagged &#39;query-to-map&#39;">query-to-map</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '19, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '19, 10:04</strong> </span></p>
</div>
</div>
<div id="comments-container-69227" class="comments-container">
<span id="69228"></span>
<div id="comment-69228" class="comment">
<div id="post-69228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For the sake of clarity: Relations are actually much more computationally expensive. Queries are just queries on a system optimized to do queries. Relations interact with everything from the main site to editor and tools to track changes and make those systems much more complex.</p>
<p>It is easy to mis-judge the computational effort of a data structure. This is why guessed complexity (any statement that is not backed by a working and to the whole world scaling implementation!) must not play a role when designing tagging models.</p>
</div>
<div id="comment-69228-info" class="comment-info">
<span class="comment-age">(19 May '19, 11:45)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="69259"></span>
<div id="comment-69259" class="comment">
<div id="post-69259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I really wonder how a retrieval of items by ID (surely with the help of index) can be more expensive then searching the whole DB by tags? I am speaking about data only and do not consider related queries (visualization on website etc.).</p>
</div>
<div id="comment-69259-info" class="comment-info">
<span class="comment-age">(21 May '19, 13:06)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-69227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69227-form-container" class="comment-form-container">
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

<span id="69277"></span>

<div id="answer-container-69277" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69277-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure if this is what you're looking for, but it's visualizing the A4 just as the A1, so I thought to mention it.</p>
<p>The A4 has two parts, the <a href="https://www.openstreetmap.org/relation/5506820#map=7/51.293/11.640">normal A4</a> and then the <a href="https://www.openstreetmap.org/relation/5517495#map=7/51.642/9.531">west-part of the A4</a>. If somehow you can connect these two into a relation then you can show the whole A4 just like the A1 you mentioned. On the other hand, that might overload the browser (points) so you might have to find a workaround for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '19, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69277" class="comments-container">
&#10;</div>
<div id="comment-tools-69277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69277-form-container" class="comment-form-container">
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

