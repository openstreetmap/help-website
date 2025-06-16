+++
type = "question"
title = "Difference between a way and a relation route"
description = '''I am interested in extracting all of the bycle routes from witihn certain coordinates. I found that it could be done like thus: http://www.overpass-api.de/api/xapi?way[bicycle=yes][bbox=32.744,35.267,33.04,35.729] meaning I extracted all of the ways with the tag &quot;bicycle&quot;, within a range of coordina...'''
date = "2013-08-29T13:44:00Z"
lastmod = "2013-08-30T07:09:00Z"
weight = 25927
keywords = [ "routes", "bicycle", "osm", "relations" ]
aliases = [ "/questions/25927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between a way and a relation route](/questions/25927/difference-between-a-way-and-a-relation-route)

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
<span id="post-25927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested in extracting all of the bycle routes from witihn certain coordinates. I found that it could be done like thus:</p>
<p><a href="http://www.overpass-api.de/api/xapi?way%5Bbicycle=yes%5D%5Bbbox=32.744,35.267,33.04,35.729%5D">http://www.overpass-api.de/api/xapi?way[bicycle=yes][bbox=32.744,35.267,33.04,35.729]</a></p>
<p>meaning I extracted all of the ways with the tag "bicycle", within a range of coordinates.</p>
<p>However, I've read in the OSM wiki that bike routes are represented as relations of the type "route". Upon checking the XML database of OSM, I found ways, tagged as "bicycle", that don't even exist in any relations.</p>
<p>What is the right way to find bike-routes? using ways or using relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routes" rel="tag" title="see questions tagged &#39;routes&#39;">routes</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '13, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/6c46c949a16eb63b46f46a16b1a61f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yehudit&#39;s gravatar image" />
<p><span>yehudit</span><br />
<span class="score" title="61 reputation points">61</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yehudit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25927" class="comments-container">
&#10;</div>
<div id="comment-tools-25927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25927-form-container" class="comment-form-container">
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

<span id="25930"></span>

<div id="answer-container-25930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25930-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A way tagged as bicycle=yes means a bicycle is legally allowed to travel along it. This is used for various types of roads and paths. Note most types of roads allow bicycles by default, it is not necessary to explicitly tag them with bicycle=yes. See the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a>.</p>
<p>Also, just because a road is tagged as bicycle=yes, it may not be a nice road for cycling. eg it may be very busy, without any cycle lanes. Cycle lanes can be tagged with <a href="https://wiki.openstreetmap.org/wiki/Key:cycleway">cycleway=lane</a> Or a path tagged as bicycle=yes might be very rough, only suitable for mountain bikes. This can be tagged with surface, smoothness, or mtb:scale.</p>
<p>Whereas cycle routes are mapped using relations, tagged as type=route and route=bicycle. A cycle route may include a variety of different roads and paths, and is usually signposted in some way, it may go to a specific destination. The route may have a name or number, and is often part of a wider network.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '13, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-25930" class="comments-container">
<span id="25945"></span>
<div id="comment-25945" class="comment">
<div id="post-25945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This reply should be enhanced with ways tagged "bicycle=designated" or "highway=cycleway" which are not necessarily part of a route relation</p>
</div>
<div id="comment-25945-info" class="comment-info">
<span class="comment-age">(29 Aug '13, 16:42)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="25955"></span>
<div id="comment-25955" class="comment">
<div id="post-25955-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You could get all those relations with</p>
<p><a href="http://www.overpass-api.de/api/interpreter?data=(rel%5Broute=bicycle%5D(35.267,32.744,35.729,33.04);%3E;);out;">http://www.overpass-api.de/api/interpreter?data=(rel[route=bicycle](35.267,32.744,35.729,33.04);&gt;;);out;</a></p>
<p>but there are no bicycle relations in your area.</p>
</div>
<div id="comment-25955-info" class="comment-info">
<span class="comment-age">(30 Aug '13, 07:09)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-25930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25930-form-container" class="comment-form-container">
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

