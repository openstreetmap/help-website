+++
type = "question"
title = "How to get Node OSM id from position (lat, lon)"
description = '''I am trying to get the nearest Node&#x27;s OSM id from some position (given latitude and longitude) by doing a request to nominatim reverse endpoint, but I always get the nearest Way. The only reference I get to the nearest Node is its position (again latitude and longitude), but not its OSM id. Is there...'''
date = "2019-05-21T11:06:00Z"
lastmod = "2019-05-21T14:16:00Z"
weight = 69257
keywords = [ "node", "position", "nominatim" ]
aliases = [ "/questions/69257" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get Node OSM id from position (lat, lon)](/questions/69257/how-to-get-node-osm-id-from-position-lat-lon)

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
<span id="post-69257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69257-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get the nearest Node's OSM id from some position (given latitude and longitude) by doing a request to nominatim reverse endpoint, but I always get the nearest Way. The only reference I get to the nearest Node is its position (again latitude and longitude), but not its OSM id.</p>
<p>Is there a way to get the OSM id of the nearest Node to some position?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-position" rel="tag" title="see questions tagged &#39;position&#39;">position</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '19, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b3ddda90091326f86430659eb6b1db80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Axel%20Afonso&#39;s gravatar image" />
<p><span>Axel Afonso</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Axel Afonso has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69257" class="comments-container">
&#10;</div>
<div id="comment-tools-69257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69257-form-container" class="comment-form-container">
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

<span id="69260"></span>

<div id="answer-container-69260" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69260-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim's database only contains named nodes, or those relevant for addresses. So a bus stop can be relevant, but a park bench or empty building won't.</p>
<p>I think the openstreetmap.org website uses <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Around">https://wiki.openstreetmap.org/wiki/Overpass_API#Around</a> for the 'what's here?' feature. I mean the pointer with question mark button on the right-hand side of the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '19, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-69260" class="comments-container">
&#10;</div>
<div id="comment-tools-69260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69260-form-container" class="comment-form-container">
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

