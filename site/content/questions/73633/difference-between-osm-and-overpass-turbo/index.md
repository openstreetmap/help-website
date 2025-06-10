+++
type = "question"
title = "difference between OSM and overpass turbo"
description = '''Hi If I look at e.g. node 514362704, which is the Hanoi railway station in Vietnam (see https://www.openstreetmap.org/way/514362704#map=16/21.0234/105.8404), then I get a lot of details like the name, name:zh, landuse, etc etc etc If I look at the same node using overpass turbo, I get none of those ...'''
date = "2020-03-20T05:02:00Z"
lastmod = "2020-03-31T06:51:00Z"
weight = 73633
keywords = [ "overpass-turbo", "railway", "station", "osm", "openrailwaymap" ]
aliases = [ "/questions/73633" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [difference between OSM and overpass turbo](/questions/73633/difference-between-osm-and-overpass-turbo)

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
<span id="post-73633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73633-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>If I look at e.g. node 514362704, which is the Hanoi railway station in Vietnam (see <a href="https://www.openstreetmap.org/way/514362704#map=16/21.0234/105.8404">https://www.openstreetmap.org/way/514362704#map=16/21.0234/105.8404</a>), then I get a lot of details like the name, name:zh, landuse, etc etc etc</p>
<p>If I look at the same node using overpass turbo, I get none of those details. Please see <a href="http://overpass-turbo.eu/s/RK7">http://overpass-turbo.eu/s/RK7</a></p>
<p>Why is there a difference between OSM and overpass turbo for that node?</p>
<p>If I try with another station, e.g. Da Nang railway station (node 377702460), then I get in overpass turbo the same details as in OSM. What am I missing here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-station" rel="tag" title="see questions tagged &#39;station&#39;">station</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-openrailwaymap" rel="tag" title="see questions tagged &#39;openrailwaymap&#39;">openrailwaymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '20, 05:02</strong></p>
<img src="https://secure.gravatar.com/avatar/870dca17bc1ffd46a5cbe21ac1e1ebec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miteyema&#39;s gravatar image" />
<p><span>miteyema</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miteyema has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73633" class="comments-container">
&#10;</div>
<div id="comment-tools-73633" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73633-form-container" class="comment-form-container">
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

<span id="73636"></span>

<div id="answer-container-73636" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73636-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-73636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="miteyema has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your first link points to a <a href="https://www.openstreetmap.org/way/514362704">way with ID 514362704</a> while your Overpass query asks for a <a href="https://www.openstreetmap.org/node/514362704">node with ID 514362704</a>. These are two completely different objects! <a href="https://wiki.openstreetmap.org/wiki/Elements">Elements</a> in OSM can share the same IDs while still representing different things. IDs are only unique within each element type but not across different element types.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73636" class="comments-container">
<span id="73881"></span>
<div id="comment-73881" class="comment">
<div id="post-73881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for clarifying that for me. My only question left is now: why is a railway station sometimes a node and sometimes a way in OSM?</p>
</div>
<div id="comment-73881-info" class="comment-info">
<span class="comment-age">(31 Mar '20, 06:30)</span> <span class="comment-user userinfo">miteyema</span>
</div>
</div>
<span id="73882"></span>
<div id="comment-73882" class="comment">
<div id="post-73882-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A node is simpler to add for mappers while a way is more accurate since it describes the extent of the railway station building. Both is correct, however. Many objects in OSM can be described by either a node or a way and sometimes also a relation. See <a href="https://wiki.openstreetmap.org/wiki/Elements">elements</a> for more information.</p>
</div>
<div id="comment-73882-info" class="comment-info">
<span class="comment-age">(31 Mar '20, 06:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73636-form-container" class="comment-form-container">
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

