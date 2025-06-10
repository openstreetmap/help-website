+++
type = "question"
title = "house names"
description = '''I live in a village that has named houses everywhere and want to make a map showing their locations, how can i use &quot;points&quot; for the locations as there isn&#x27;t a tag for homes? thanks'''
date = "2019-12-01T12:51:00Z"
lastmod = "2019-12-01T18:20:00Z"
weight = 71919
keywords = [ "house", "names" ]
aliases = [ "/questions/71919" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [house names](/questions/71919/house-names)

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
<span id="post-71919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in a village that has named houses everywhere and want to make a map showing their locations, how can i use "points" for the locations as there isn't a tag for homes?</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '19, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f8937cc51b88deab912ff6d6375a5cd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grays85&#39;s gravatar image" />
<p><span>Grays85</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grays85 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71919" class="comments-container">
&#10;</div>
<div id="comment-tools-71919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71919-form-container" class="comment-form-container">
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

<span id="71923"></span>

<div id="answer-container-71923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71923-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's because the database wants to know what type of feature you are naming. A name on its own has little or no value when not linked to a feature. To name a home you would place a point/node and use minimum tags of building=yes and name=Whatever. It would actually be much better to draw the outline of the building, giving that the minimum tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '19, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-71923" class="comments-container">
<span id="71927"></span>
<div id="comment-71927" class="comment">
<div id="post-71927-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Also note that if the house name is used as part of the official postal address of the building, then it's better to use <code>addr:housename=Whatever</code> rather than <code>name=Whatever</code>.</p>
</div>
<div id="comment-71927-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 16:10)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-71923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71929"></span>

<div id="answer-container-71929" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71929-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-71929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Grays85, as BCNorwich has described, use an good aerial view to draw buildings together with your local knowledge. Draw every building just square as good as it is, with tags as building=yes/house, garage, shed and building:level=, building:material=, roof:shape=, (<a href="https://wiki.openstreetmap.org/wiki/Key:roof:shape/material">https://wiki.openstreetmap.org/wiki/Key:roof:shape/material</a> aso. And remember that every building has to carry a name sign when you ad it into OSM. Have fun and keep mapping</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '19, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-71929" class="comments-container">
&#10;</div>
<div id="comment-tools-71929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71929-form-container" class="comment-form-container">
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

