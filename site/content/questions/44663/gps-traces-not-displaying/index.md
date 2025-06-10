+++
type = "question"
title = "GPS traces not displaying"
description = '''I have been taking some GPS traces on iPhone using the Trails app and then uploaded them to OSM. They import successfully but I can&#x27;t get them to overlay on the map, neither on the editor on the website or in the Go Map!! App on iOS. I&#x27;ve tried setting them to all of the different privacy settings a...'''
date = "2015-08-08T11:22:00Z"
lastmod = "2015-08-08T12:24:00Z"
weight = 44663
keywords = [ "problem", "traces", "gps" ]
aliases = [ "/questions/44663" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [GPS traces not displaying](/questions/44663/gps-traces-not-displaying)

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
<span id="post-44663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been taking some GPS traces on iPhone using the Trails app and then uploaded them to OSM. They import successfully but I can't get them to overlay on the map, neither on the editor on the website or in the Go Map!! App on iOS. I've tried setting them to all of the different privacy settings and still they don't appear. Other people's traces appear and if I click on my individual traces, they will overlay correctly on the map. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '15, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/49a84f998d4b438addf44df17fb06f29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edwardsaid&#39;s gravatar image" />
<p><span>edwardsaid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edwardsaid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44663" class="comments-container">
&#10;</div>
<div id="comment-tools-44663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44663-form-container" class="comment-form-container">
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

<span id="44666"></span>

<div id="answer-container-44666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44666-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing that you're <a href="http://www.openstreetmap.org/user/edwardsaid/traces">this user</a>. Looking at <a href="http://www.openstreetmap.org/user/edwardsaid/traces/2012908">this trace</a>, it appears OK in the "Potlatch 2" editor (and I presume that it will in JOSM too). The "iD" editor (which you were using <a href="http://www.openstreetmap.org/changeset/28954808">here</a>) uses a "background overlay" of GPS map tiles. The relevant one for your trace is <a href="http://gps-b.tile.openstreetmap.org/lines/17/77510/56494.png">here</a>, but as you can see it doesn't include your trace. I believe that the software that updates iD's GPS background layer is <a href="https://github.com/ericfischer/gpx-updater">here</a>. Issues have been logged for update problems there in the past - <a href="https://github.com/ericfischer/gpx-updater/issues/1">this one</a> might be relevant if you've changed the permissions, and there's also <a href="https://github.com/ericfischer/gpx-updater/issues/2">this one</a>.</p>
<p>There's another option, though - you can <a href="http://help.openstreetmap.org/questions/24410/is-there-a-way-to-see-my-gps-track-overlayed-in-the-map-editor/24411">drag and drop</a> local GPS files into the iD editor. That should allow you see them there.</p>
<p>I'm not sure what "Go Map!!!" uses for GPS background, though (maybe someone can edit this answer and add details?).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '15, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '15, 12:24</strong> </span></p>
</div>
</div>
<div id="comments-container-44666" class="comments-container">
&#10;</div>
<div id="comment-tools-44666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44666-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44664"></span>

<div id="answer-container-44664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44664-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi edwardsaid, read this, <a href="https://help.openstreetmap.org/questions/24410/is-there-a-way-to-see-my-gps-track-overlayed-in-the-map-editor,">https://help.openstreetmap.org/questions/24410/is-there-a-way-to-see-my-gps-track-overlayed-in-the-map-editor,</a> the editor seems to be the bottle neck. Use JOSM and the file triggers the program and realizes the display of your trace.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '15, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '15, 11:51</strong> </span></p>
</div>
</div>
<div id="comments-container-44664" class="comments-container">
&#10;</div>
<div id="comment-tools-44664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44664-form-container" class="comment-form-container">
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

