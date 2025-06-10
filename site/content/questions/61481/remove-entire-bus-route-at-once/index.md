+++
type = "question"
title = "Remove entire bus route at once"
description = '''Hi everyone, There are several bus routes withdrawn in my town. But these are still shown on OpenStreetMap. Is there a way to remove an entire bus route, without first deleting all members one by one? Thank you in advance! Sincerly, Rico'''
date = "2018-01-04T13:41:00Z"
lastmod = "2018-01-04T15:03:00Z"
weight = 61481
keywords = [ "bus", "transit", "busroute", "delete" ]
aliases = [ "/questions/61481" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remove entire bus route at once](/questions/61481/remove-entire-bus-route-at-once)

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
<span id="post-61481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61481-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>There are several bus routes withdrawn in my town.<br />
But these are still shown on OpenStreetMap.</p>
<p>Is there a way to remove an entire bus route, without first deleting all members one by one?<br />
Thank you in advance!</p>
<p>Sincerly,<br />
Rico</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-transit" rel="tag" title="see questions tagged &#39;transit&#39;">transit</span> <span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '18, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/6d17dd5e18e21846e6134137fca00bf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PlantedRabbit&#39;s gravatar image" />
<p><span>PlantedRabbit</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PlantedRabbit has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-61481" class="comments-container">
&#10;</div>
<div id="comment-tools-61481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61481-form-container" class="comment-form-container">
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

<span id="61482"></span>

<div id="answer-container-61482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61482-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming you want to delete all the <a href="https://wiki.openstreetmap.org/wiki/Relation:route">route relations</a> that belong to a single <a href="https://wiki.openstreetmap.org/wiki/Tag:type%3Droute_master">route master relation</a> ? Deleting the <em>highway=*</em> ways that are members of the route relation is not a good idea.</p>
<p>With JOSM, you can do the former by selecting any highway that is part of the route, then right-click on the route master relation in the <em>tag/membership</em> panel and choose <em>select members</em>, and finally press <em>delete</em>. You can then delete the route master relation itself. Not sure how to do this with other editors.</p>
<p>That said, I would probably not bulk-delete things like this: route relations can be a bit complex and I'd prefer to check relations individually before deleting each one. Route master relations don't usually have too many members.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '18, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span> </br></p>
</div>
</div>
<div id="comments-container-61482" class="comments-container">
&#10;</div>
<div id="comment-tools-61482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61482-form-container" class="comment-form-container">
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

