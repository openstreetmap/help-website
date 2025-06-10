+++
type = "question"
title = "[closed] What&#x27;s the best practice regarding the age of data between saves?"
description = '''Suppose I want to map an area, and I have lots of data (from aerial imagery, and other authorized sources), and that it will take (for example) 1 full work day to do it. Using JOSM, I download the area from the OSM database, and almost nothing comes up (as expected, as it is an remote area), and I s...'''
date = "2012-10-19T00:07:00Z"
lastmod = "2012-10-19T15:26:00Z"
weight = 17008
keywords = [ "josm", "time", "upload", "refresh", "changeset" ]
aliases = [ "/questions/17008" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] What's the best practice regarding the age of data between saves?](/questions/17008/whats-the-best-practice-regarding-the-age-of-data-between-saves)

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
<span id="post-17008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17008-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Suppose I want to map an area, and I have lots of data (from aerial imagery, and other authorized sources), and that it will take (for example) 1 full work day to do it.</p>
<p>Using JOSM, I download the area from the OSM database, and almost nothing comes up (as expected, as it is an remote area), and I start editing it.</p>
<p>What should be the interval between saves and/or updates? It is not very likely, but if other users come and edit the same area, adding data, the changes will overlap.</p>
<p>Should I upload everything at the end (after one day of editing) or should I upload it in parts (let's say, every hour)? Or should I upload everything at the end of the day, but updating/refresing the downloaded data a few times along the day to see if there are changes made by other users?</p>
<p>When I used Potlatch 2 instead of JOSM, this never was an issue (for me). However, there were cases of changes appearing "from nowhere" when the map was dragged because some other user edited the same area.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-refresh" rel="tag" title="see questions tagged &#39;refresh&#39;">refresh</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '12, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>09 Oct '13, 19:46</strong> </span></p>
</div>
</div>
<div id="comments-container-17008" class="comments-container">
&#10;</div>
<div id="comment-tools-17008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17008-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by MCPicoli 09 Oct '13, 19:46

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17017"></span>

<div id="answer-container-17017" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17017-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect the answer is a mixture of both uploading at intervals (which lets other mappers see that work is being done in the area) and downloading again at intervals (as uploading won't download new or changed objects in an area). The frequency will depend on how likely you think someone else will be working in the same area. You might just get away with downloading the area again just before uploading to check nothing else has been added in the meantime.</p>
<p>If you are worried about other users amending things that you are also working on then JOSM does have a conflict resolution dialog, but don't always just take your version as it might lose important changes from the other user. It is easy to use, but often difficult to use correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '12, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17017" class="comments-container">
&#10;</div>
<div id="comment-tools-17017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17017-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17027"></span>

<div id="answer-container-17027" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17027-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you edit for more than an hour without saving (uploading) you are risking losing your edits - all computer software complex enough to be useful is complex enough to have bugs. Saving often has no real downside. Saving often has the advantage of being able to describe the upload with a specific changeset comment to describe what you did. I would mentally divide the area into sections or areas or types of edit and save at the end of each one. If you have edited more than about 500 objects I'd think about saving too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '12, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17027" class="comments-container">
<span id="17029"></span>
<div id="comment-17029" class="comment">
<div id="post-17029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I generally agree with your recommendations, but saving and uploading are not the same thing with JOSM. I save (on disk) every few minutes, but upload (to the server) only when one self-contained task is complete.</p>
</div>
<div id="comment-17029-info" class="comment-info">
<span class="comment-age">(19 Oct '12, 15:26)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-17027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17027-form-container" class="comment-form-container">
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

