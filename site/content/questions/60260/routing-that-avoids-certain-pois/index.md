+++
type = "question"
title = "routing that avoids certain POIs"
description = '''Does anyone know of an OSM-based routing service, where you can choose certain POIs from OSM as &quot;things to avoid&quot;. I recently saw an &quot;art project&quot; with the last pedestrian route you can take through a larger city where you meet no security cameras. Would be cool to be able to do that kind of thing i...'''
date = "2017-10-24T09:07:00Z"
lastmod = "2017-10-24T10:27:00Z"
weight = 60260
keywords = [ "routing", "customization" ]
aliases = [ "/questions/60260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [routing that avoids certain POIs](/questions/60260/routing-that-avoids-certain-pois)

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
<span id="post-60260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does anyone know of an OSM-based routing service, where you can choose certain POIs from OSM as "things to avoid". I recently saw an "art project" with the last pedestrian route you can take through a larger city where you meet no security cameras. Would be cool to be able to do that kind of thing in a router.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '17, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-60260" class="comments-container">
&#10;</div>
<div id="comment-tools-60260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60260-form-container" class="comment-form-container">
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

<span id="60262"></span>

<div id="answer-container-60262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60262-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at the <a href="https://www.openstreetmap.ie/the-dublin-pub-walk-question-answered-again/">crossing Dublin without passing by a pub</a> puzzle for inspiration. The <a href="https://www.graphhopper.com/blog/2015/11/15/publess-routes-graphhopper-edition/">latest solution</a> using graphhopper looks simple enough: use overpass to download a list of no-go POIs, generate new routing weights using that list, and ask for a route using those weights :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '17, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '17, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-60262" class="comments-container">
&#10;</div>
<div id="comment-tools-60262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60262-form-container" class="comment-form-container">
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

