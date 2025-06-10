+++
type = "question"
title = "clipping polygons and relations that exceed the borders of the exported map"
description = '''Hi,  I want to use the open world map data in an app that I develop. The app generates chunks around the player. Each chunk draws the information provided in a .osm file that has the same name as the chunk. The problem is that the polygons and relations sometimes go over the map border and are drawn...'''
date = "2017-05-28T14:16:00Z"
lastmod = "2017-06-07T18:03:00Z"
weight = 56339
keywords = [ "development", "borders", "export", "bounds", "split" ]
aliases = [ "/questions/56339" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [clipping polygons and relations that exceed the borders of the exported map](/questions/56339/clipping-polygons-and-relations-that-exceed-the-borders-of-the-exported-map)

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
<span id="post-56339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56339-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to use the open world map data in an app that I develop. The app generates chunks around the player. Each chunk draws the information provided in a .osm file that has the same name as the chunk. The problem is that the polygons and relations sometimes go over the map border and are drawn multiple times because of that. This costs performance. Is there any program or online-service that clips the polygons and relations that go over the border of the exported map? If not, I'll need to write a script that does this. I tried to split a big .osm file into several small ones with osmosis but didn't got the intended result with it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-bounds" rel="tag" title="see questions tagged &#39;bounds&#39;">bounds</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '17, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a3785e3269a7d2d075eb016f6534709d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Time2Design&#39;s gravatar image" />
<p><span>Time2Design</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Time2Design has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '17, 14:17</strong> </span></p>
</div>
</div>
<div id="comments-container-56339" class="comments-container">
&#10;</div>
<div id="comment-tools-56339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56339-form-container" class="comment-form-container">
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

<span id="56499"></span>

<div id="answer-container-56499" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56499-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I developed a text based application to solve my issue. It can cut any polygon and line from osm street map so the polygon or line is only existent and visible inside the bounds and not outside of them. The application adds points to the edges and corners of the exported map if nessessary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '17, 18:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a3785e3269a7d2d075eb016f6534709d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Time2Design&#39;s gravatar image" />
<p><span>Time2Design</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Time2Design has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56499" class="comments-container">
&#10;</div>
<div id="comment-tools-56499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56499-form-container" class="comment-form-container">
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

