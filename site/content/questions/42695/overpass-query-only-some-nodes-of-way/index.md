+++
type = "question"
title = "overpass query only some nodes of way"
description = '''Is it possible in overpass-turbo to query only some of the nodes of a way? I want to query a wide selection of ways, and then only get some of the nodes as a result. First, make me a list of all the ways (that are highway at least tertiary and surface=paved or similar), then give me the first node o...'''
date = "2015-04-29T15:33:00Z"
lastmod = "2015-06-19T07:19:00Z"
weight = 42695
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/42695" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overpass query only some nodes of way](/questions/42695/overpass-query-only-some-nodes-of-way)

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
<span id="post-42695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42695-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible in overpass-turbo to query only some of the nodes of a way?</p>
<p>I want to query a wide selection of ways, and then only get some of the nodes as a result. First, make me a list of all the ways (that are highway at least tertiary and surface=paved or similar), then give me the first node of any way, and a following node only if it is a least a 100 meters away from the first node. Then follow the way untill you find another node at leat 100m away, and so on untill the end of the way.</p>
<p>The idea is to reduce the waiting and downloading time, so it might be counterproductive to try this?</p>
<p>This question is related to my previous post <a href="https://help.openstreetmap.org/questions/40932/a-umap-with-lots-of-data-through-overpass">https://help.openstreetmap.org/questions/40932/a-umap-with-lots-of-data-through-overpass</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '15, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '15, 13:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span></p>
</div>
</div>
<div id="comments-container-42695" class="comments-container">
&#10;</div>
<div id="comment-tools-42695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42695-form-container" class="comment-form-container">
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

<span id="43632"></span>

<div id="answer-container-43632" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43632-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a comment before, but it seems to be removed. This is kind of a stupid question, it made me realize. In fact, I think what I am describing is kind of what would happen serverside if a future simplification algorithm were in place. If you do this clientside, you'd probably need all the data first anyway, hence increasing total waiting time instead of decreasing it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 07:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-43632" class="comments-container">
&#10;</div>
<div id="comment-tools-43632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43632-form-container" class="comment-form-container">
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

