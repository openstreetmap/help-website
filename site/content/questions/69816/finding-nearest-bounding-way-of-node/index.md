+++
type = "question"
title = "Finding nearest bounding way of node"
description = '''Hello, I am trying to develop a query that returns the nearest bounding way of a node. For example, I pass in Node 5212949758, and get back Way 30612528. Is this possible with OSM?  Thank you!'''
date = "2019-07-01T06:30:00Z"
lastmod = "2020-03-20T14:30:00Z"
weight = 69816
keywords = [ "bounding", "newbie", "bounding-polygon", "parent", "spatial" ]
aliases = [ "/questions/69816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding nearest bounding way of node](/questions/69816/finding-nearest-bounding-way-of-node)

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
<span id="post-69816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am trying to develop a query that returns the nearest bounding way of a node.</p>
<p>For example, I pass in Node 5212949758, and get back Way 30612528.</p>
<p>Is this possible with OSM?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-parent" rel="tag" title="see questions tagged &#39;parent&#39;">parent</span> <span class="post-tag tag-link-spatial" rel="tag" title="see questions tagged &#39;spatial&#39;">spatial</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '19, 06:30</strong></p>
<img src="https://secure.gravatar.com/avatar/5afd730543c7f961c09a8657ee1b7526?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newto_osm&#39;s gravatar image" />
<p><span>newto_osm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newto_osm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '19, 06:39</strong> </span></p>
</div>
</div>
<div id="comments-container-69816" class="comments-container">
&#10;</div>
<div id="comment-tools-69816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69816-form-container" class="comment-form-container">
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

<span id="73647"></span>

<div id="answer-container-73647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73647-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>let's assume that the nearest building is closer than 40, the first one should be the best one. ( node(4190985791); way(around:40.0); ); out geom;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '20, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/30828ab02c12f127e53e4b03f4aea518?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bendoSK&#39;s gravatar image" />
<p><span>bendoSK</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bendoSK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Mar '20, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-73647" class="comments-container">
&#10;</div>
<div id="comment-tools-73647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73647-form-container" class="comment-form-container">
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

