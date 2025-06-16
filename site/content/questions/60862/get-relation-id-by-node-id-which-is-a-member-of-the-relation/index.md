+++
type = "question"
title = "Get relation id by node id (which is a member of the relation)"
description = '''Hi everyone, how can i get the relation id by the node id? Or in other words - how can i get from here: https://www.openstreetmap.org/api/0.6/node/240076989 to here:  https://www.openstreetmap.org/api/0.6/relation/191645 (which both is the city of dresden) Thank you for every contribution.'''
date = "2017-11-29T12:53:00Z"
lastmod = "2017-11-30T09:33:00Z"
weight = 60862
keywords = [ "nodes", "api", "osm", "id", "relations" ]
aliases = [ "/questions/60862" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get relation id by node id (which is a member of the relation)](/questions/60862/get-relation-id-by-node-id-which-is-a-member-of-the-relation)

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
<span id="post-60862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60862-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>how can i get the relation id by the node id?</p>
<p>Or in other words - how can i get from here: <a href="https://www.openstreetmap.org/api/0.6/node/240076989">https://www.openstreetmap.org/api/0.6/node/240076989</a> to here: <a href="https://www.openstreetmap.org/api/0.6/relation/191645">https://www.openstreetmap.org/api/0.6/relation/191645</a> (which both is the city of dresden)</p>
<p>Thank you for every contribution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '17, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/dd9c8a6b96e9e37ba8ea15c2ef74847a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="T4Titan&#39;s gravatar image" />
<p><span>T4Titan</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="T4Titan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60862" class="comments-container">
&#10;</div>
<div id="comment-tools-60862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60862-form-container" class="comment-form-container">
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

<span id="60863"></span>

<div id="answer-container-60863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60863-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just append <code>/relations</code> to your first link: <a href="https://www.openstreetmap.org/api/0.6/node/240076989/relations">https://www.openstreetmap.org/api/0.6/node/240076989/relations</a></p>
<p>This will return all relations the node is part of. This feature is described <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Relations_for_element:_GET_.2Fapi.2F0.6.2F.5Bnode.7Cway.7Crelation.5D.2F.23id.2Frelations">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '17, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60863" class="comments-container">
<span id="60869"></span>
<div id="comment-60869" class="comment">
<div id="post-60869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Greetings to dresden :)</p>
</div>
<div id="comment-60869-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 13:44)</span> <span class="comment-user userinfo">T4Titan</span>
</div>
</div>
</div>
<div id="comment-tools-60863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60863-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60867"></span>

<div id="answer-container-60867" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your fast answer. I have not expected such an easy way :D Which osm tool do i have to use to query big amounts of data?</p>
<p>Maybe the overpass api is able to handle such volumes. <a href="https://overpass-api.de/api/interpreter?data=%5Bout:json%5D;out;">https://overpass-api.de/api/interpreter?data=[out:json];out;</a> But i have no idea how to do this query from above whit this api.</p>
<p>Is there anyone who is able to formulate the correct query?</p>
<p>...a query that uses the node id of a city/village to get its direct parent relations id (which is the city also)</p>
<p><a href="https://overpass.kumi.systems/api/interpreter?data=%5Bout:json%5D;node(">https://overpass.kumi.systems/api/interpreter?data=[out:json];node(</a> <strong>IdOfNode</strong> );&lt;; <strong>filteringToGetTheParentRelationWhichDesribesAlsoTheCityOrVillage</strong> out;</p>
<p>I need this id to be able to use nominatim to get the borders of all cities in my database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '17, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/dd9c8a6b96e9e37ba8ea15c2ef74847a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="T4Titan&#39;s gravatar image" />
<p><span>T4Titan</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="T4Titan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '17, 09:32</strong> </span></p>
</div>
</div>
<div id="comments-container-60867" class="comments-container">
<span id="60870"></span>
<div id="comment-60870" class="comment">
<div id="post-60870-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which query? The main API is just an editing API and should not be used to perform large queries. Overpass API instead can handle rather large queries.</p>
</div>
<div id="comment-60870-info" class="comment-info">
<span class="comment-age">(29 Nov '17, 13:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60883"></span>
<div id="comment-60883" class="comment">
<div id="post-60883-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>...a query that uses the node id of a city/village to get its direct parent relations id (which is the city also)</p>
<p><a href="https://overpass.kumi.systems/api/interpreter?data=%5Bout:json%5D;node(">https://overpass.kumi.systems/api/interpreter?data=[out:json];node(</a> <strong>IdOfNode</strong> );&lt;; <strong>filteringToGetTheParentRelationIdOfTheRelationWhichDesribesAlsoTheCityOrVillage</strong> out;</p>
</div>
<div id="comment-60883-info" class="comment-info">
<span class="comment-age">(30 Nov '17, 09:33)</span> <span class="comment-user userinfo">T4Titan</span>
</div>
</div>
</div>
<div id="comment-tools-60867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60867-form-container" class="comment-form-container">
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

