+++
type = "question"
title = "way_id, node_id are those permanent ? Connect to the same place, coordinate always ?"
description = '''My question is what happens with way_id, node_id as time goes? Are they always permanently bound to the real world entities they were first time assigned (some geographical object like a highway or river for ways and simple coordinate for nodes) or they could change their real world counterparts ove...'''
date = "2019-12-02T21:56:00Z"
lastmod = "2019-12-03T06:31:00Z"
weight = 71952
keywords = [ "id", "database" ]
aliases = [ "/questions/71952" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [way_id, node_id are those permanent ? Connect to the same place, coordinate always ?](/questions/71952/way_id-node_id-are-those-permanent-connect-to-the-same-place-coordinate-always)

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
<span id="post-71952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My question is what happens with way_id, node_id as time goes? Are they always permanently bound to the real world entities they were first time assigned (some geographical object like a highway or river for ways and simple coordinate for nodes) or they could change their real world counterparts over time ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '19, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a8f90b657d65e9a61669af64f2cd969f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stan%20Sokolov&#39;s gravatar image" />
<p><span>Stan Sokolov</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stan Sokolov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71952" class="comments-container">
&#10;</div>
<div id="comment-tools-71952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71952-form-container" class="comment-form-container">
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

<span id="71953"></span>

<div id="answer-container-71953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71953-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The IDs are not permanent. They can change for various reasons, e.g.:</p>
<ul>
<li>something is deleted and re-created (the old ID will become unused)</li>
<li>something is split into several parts (the old ID will either become unused or refer to only one of the parts)</li>
<li>several things are merged into one (it is possible that one of the old IDs then refers to the whole thing and the others become unused)</li>
</ul>
<p>Do not rely on IDs remaining constant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '19, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71953" class="comments-container">
<span id="71954"></span>
<div id="comment-71954" class="comment">
<div id="post-71954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We are working on a routing framework that uses permanent route keys that contain entire path. In certain scenarios it was desired to repeat route exactly the same way without any modifications. We were using a way:node id sequence to encode route, however it seems to be not a legit option as those IDs are not permanent. Hmm very sad. Seems that our problem has no solution as coordinates of nodes could also be moved with map modifications. So there is no way to force a route go exactly the same path as was found suitable a certain time before.</p>
</div>
<div id="comment-71954-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 23:11)</span> <span class="comment-user userinfo">Stan Sokolov</span>
</div>
</div>
<span id="71955"></span>
<div id="comment-71955" class="comment">
<div id="post-71955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe it would work to store the coordinates directly? That way you know they aren't going to change.</p>
</div>
<div id="comment-71955-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 00:37)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="71957"></span>
<div id="comment-71957" class="comment">
<div id="post-71957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We have some additional metadata attached to OSM ways that we would like to append to the route each time someone uses it. If we store coordinates we will need to figure out which OSM way this coordinate lays on that is an expensive step for us. Ideally we would like to have a quick way to match route with OSM ways and get the metadata from the place we store it (Redis at this moment). Also as of now we only store OSM way:node id at places where route switches from one OSM way to another, skipping all the nodes in between. But if we store the coordinates we would need to store the entire path what will make us to transmit more data. Many downsides of this approach.</p>
<p>Take example of a person who walks the same way from one place to another 2.5 miles every day and back just for some purpose (let say a servicemen). He also has a few alternative routes in case if they provide more service targets. We have the information stored in Redis that is updated every minute about service targets assigned to OSM ways/nodes and we would like quickly figure out which alternative route has more places for service. When we store ways:nodes we could easily match route against list of targets.</p>
</div>
<div id="comment-71957-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 01:12)</span> <span class="comment-user userinfo">Stan Sokolov</span>
</div>
</div>
<span id="71959"></span>
<div id="comment-71959" class="comment">
<div id="post-71959-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>But as soon as someone splits a road (e.g. different sidewalks, max speed, a bus route that uses only part of the OSM-way), you will have to adapt your route and add the extra OSM way otherwise, you have a gap in your route</p>
</div>
<div id="comment-71959-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 04:08)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="71960"></span>
<div id="comment-71960" class="comment">
<div id="post-71960-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>But if we store the coordinates we would need to store the entire path what will make us to transmit more data</p>
</blockquote>
<p>Look into Google polyline format.</p>
</div>
<div id="comment-71960-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 06:31)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71953-form-container" class="comment-form-container">
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

