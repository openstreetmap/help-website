+++
type = "question"
title = "How to integrate openstreetmap with UWP to find the shortest path"
description = '''hi I want to develop an UWP app (a Windows phone app) which shows a map on a user interface. When user select 2 points it should shows the shortest path on the map. I am going to implement the dijkstra&#x27;s algorithm to find the shortest path.I can implement this algorithm if I have map data. I just do...'''
date = "2018-01-05T08:26:00Z"
lastmod = "2018-01-08T02:41:00Z"
weight = 61488
keywords = [ "development", "usage", "app", "uwp", "routing" ]
aliases = [ "/questions/61488" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to integrate openstreetmap with UWP to find the shortest path](/questions/61488/how-to-integrate-openstreetmap-with-uwp-to-find-the-shortest-path)

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
<span id="post-61488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi I want to develop an UWP app (a Windows phone app) which shows a map on a user interface. When user select 2 points it should shows the shortest path on the map. I am going to implement the dijkstra's algorithm to find the shortest path.I can implement this algorithm if I have map data. I just don't understand how to start. How to integrate openstreet map with my UWP app and how to get map data.</p>
<p>Please help me, Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-app" rel="tag" title="see questions tagged &#39;app&#39;">app</span> <span class="post-tag tag-link-uwp" rel="tag" title="see questions tagged &#39;uwp&#39;">uwp</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '18, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/2f44e9d00f417d4cdd1d58c594804d92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swiftDroid&#39;s gravatar image" />
<p><span>swiftDroid</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swiftDroid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '18, 22:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span></p>
</div>
</div>
<div id="comments-container-61488" class="comments-container">
&#10;</div>
<div id="comment-tools-61488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61488-form-container" class="comment-form-container">
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

<span id="61493"></span>

<div id="answer-container-61493" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61493-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="swiftDroid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Basically there are 3 solutions:</p>
<ul>
<li>you use the API of a 3rd party provider to specify 2 points and let them calculate the route. This will probably cost you money to use their API, but you do no have to create a routing algorithm, nor do you have to download OSM data.</li>
<li>You download OSM-data to a local server, transform that data in such a way that you can develop a routing algorithm. Then you create an API on top of that server which you call from your UWP app (a Windows phone app)</li>
<li>You do the same as in step 2, but move the data to the phone (so-called off line maps) instead of keeping it on the server. This is the approach Maps.me, OsmAnd, MagicEarth etc. use</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '18, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61493" class="comments-container">
<span id="61528"></span>
<div id="comment-61528" class="comment">
<div id="post-61528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for the great clarification :)</p>
</div>
<div id="comment-61528-info" class="comment-info">
<span class="comment-age">(08 Jan '18, 02:41)</span> <span class="comment-user userinfo">swiftDroid</span>
</div>
</div>
</div>
<div id="comment-tools-61493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61493-form-container" class="comment-form-container">
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

