+++
type = "question"
title = "Select ways by following a GPX track"
description = '''I have a GPX track of a bike trip which was entirely on asphalt, so I would like to add surface=asphalt on all the ways I used. From the GPX track, is it possible (for instance in JOSM) to automatically select the nearest ways in OSM? Ideally by taking into account that these must form a valid path ...'''
date = "2020-12-30T09:02:00Z"
lastmod = "2020-12-30T13:12:00Z"
weight = 78118
keywords = [ "ways", "josm", "gpx", "post_process_gpx" ]
aliases = [ "/questions/78118" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Select ways by following a GPX track](/questions/78118/select-ways-by-following-a-gpx-track)

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
<span id="post-78118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a GPX track of a bike trip which was entirely on asphalt, so I would like to add <code>surface=asphalt</code> on all the ways I used.</p>
<p>From the GPX track, is it possible (for instance in JOSM) to automatically select the nearest ways in OSM? Ideally by taking into account that these must form a valid path as a whole (which hopefully helps disambiguate edge cases).</p>
<p>I would then just need to review that the selection is correct and apply the tag to all these ways.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-post_process_gpx" rel="tag" title="see questions tagged &#39;post_process_gpx&#39;">post_process_gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '20, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c447f40cf43cf6c458112f3b46ee3093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pintoch&#39;s gravatar image" />
<p><span>Pintoch</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pintoch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78118" class="comments-container">
&#10;</div>
<div id="comment-tools-78118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78118-form-container" class="comment-form-container">
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

<span id="78124"></span>

<div id="answer-container-78124" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78124-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pintoch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the general term for this is <a href="https://en.wikipedia.org/wiki/Map_matching">map matching</a>. It is supported by some of the routers that use OSM data, but generally isn't present in editors.</p>
<p>While there have been a few tools that use errors during map matching/navigation to flag potential errors in OSM (<a href="https://wiki.openstreetmap.org/wiki/MapDust">MapDust</a>, <a href="https://wiki.openstreetmap.org/wiki/That_Shouldnt_Be_Possible">That Shouldn't be Possible</a>) I'm not aware of any JOSM plugin that will do this.</p>
<p>I think you will have to overlay the GPS trace and select ways manually.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '20, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-78124" class="comments-container">
&#10;</div>
<div id="comment-tools-78124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78124-form-container" class="comment-form-container">
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

