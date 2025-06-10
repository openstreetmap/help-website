+++
type = "question"
title = "Accurate, incomplete survey of bus routes"
description = '''The Israeli OSM community has discussed importing bus routes information from Ministry data. The data contains the sequence of stops for each route but not the sequence of highways the bus would take. However, type=route relation specifies that the ways that make up the route are mandatory members o...'''
date = "2018-03-24T21:09:00Z"
lastmod = "2018-03-30T18:21:00Z"
weight = 62812
keywords = [ "bus", "accurate", "route", "incomplete" ]
aliases = [ "/questions/62812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Accurate, incomplete survey of bus routes](/questions/62812/accurate-incomplete-survey-of-bus-routes)

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
<span id="post-62812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62812-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Israeli OSM community has discussed importing bus routes information from Ministry data. The data contains the sequence of stops for each route but not the sequence of highways the bus would take. However, <a href="https://wiki.openstreetmap.org/wiki/Relation:route#Members"><code>type=route</code> relation</a> specifies that the ways that make up the route are mandatory members of the relation, and it is not feasible to manually survey the highways information. (It can probably be inferred with reasonable accuracy from the sequence of stops, of course.)</p>
<p>What would be the best way to handle this situation? Would it make sense to import the stops data without highways data? Should we try to infer the highways data (run a routing app on each pair of successive stops, etc)? Or just leave the data unimported?</p>
<p>Personally, I would have thought that adding the <code>type=route</code> relations without member ways would be fine (it would be <a href="https://help.openstreetmap.org/questions/44227/car-park-entranceexits/44236">accurate, incomplete information</a>; requiring complete, accurate information would be making the perfect the enemy of the good), but a counter-argument was presented that the schema should be adhered to.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-accurate" rel="tag" title="see questions tagged &#39;accurate&#39;">accurate</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-incomplete" rel="tag" title="see questions tagged &#39;incomplete&#39;">incomplete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '18, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '18, 21:10</strong> </span></p>
</div>
</div>
<div id="comments-container-62812" class="comments-container">
&#10;</div>
<div id="comment-tools-62812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62812-form-container" class="comment-form-container">
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

<span id="62816"></span>

<div id="answer-container-62816" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62816-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just importing the stop in relations is probably easy, but I guess contacting the bus operator for free daily passes to organize a mapping party would allow your community to complete a lot of routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '18, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-62816" class="comments-container">
<span id="62863"></span>
<div id="comment-62863" class="comment">
<div id="post-62863-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for the idea. Perhaps the bus operator would consent to share the maps they already have under an OSM-compatible license, too. That would be far easier to work with, especially for intercity routes.</p>
</div>
<div id="comment-62863-info" class="comment-info">
<span class="comment-age">(30 Mar '18, 18:21)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-62816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62816-form-container" class="comment-form-container">
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

