+++
type = "question"
title = "script for automation of &#x27;node to way&#x27;"
description = '''Hi. I have thousands of gpx tracks and make it routable path with it on JOSM. and then I will make my own mapsforge map I use &quot;J&quot; command to connect intersection part of every tracks manually. But It needs much time and I worry about missing some of the part. I found scripting plugin for JOSM. but I...'''
date = "2020-02-11T04:59:00Z"
lastmod = "2020-02-12T00:17:00Z"
weight = 72995
keywords = [ "routing" ]
aliases = [ "/questions/72995" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [script for automation of 'node to way'](/questions/72995/script-for-automation-of-node-to-way)

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
<span id="post-72995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I have thousands of gpx tracks and make it routable path with it on JOSM. and then I will make my own mapsforge map I use "J" command to connect intersection part of every tracks manually. But It needs much time and I worry about missing some of the part. I found scripting plugin for JOSM. but I don't know how to make script for automatic "J" command</p>
<p>I guess the procedure like this. 1. Define preset value of distance of 'node to way' (ex. 10m) 2. On the script, search whole bound of gpx tracks and compare with the value to preset. 3. Join node to way 4. loop</p>
<p><img src="https://i.ibb.co/ZGMSCyW/4444.png" alt="alt text" /></p>
<p>Need some advise . Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '20, 04:59</strong></p>
<img src="https://secure.gravatar.com/avatar/675d3b2a6f665359e96bbbc06a689efe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orango6666&#39;s gravatar image" />
<p><span>orango6666</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orango6666 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-72995" class="comments-container">
&#10;</div>
<div id="comment-tools-72995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72995-form-container" class="comment-form-container">
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

<span id="73006"></span>

<div id="answer-container-73006" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73006-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The plugin utilsplugin2 comes with a command "Add Nodes at intersections" (shift-I), see <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2#Add_nodes_at_intersections_.28Shift.2BI.29.">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/utilsplugin2#Add_nodes_at_intersections_.28Shift.2BI.29.</a></p>
<p>Select all ways, press shift-I. done</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '20, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-73006" class="comments-container">
&#10;</div>
<div id="comment-tools-73006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73006-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73033"></span>

<div id="answer-container-73033" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for answer, escada. It works nice! I have one more question. Is there some way to join node with adjacent way automatically?</p>
<p><img src="https://i.ibb.co/dfmDpzh/55.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '20, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/675d3b2a6f665359e96bbbc06a689efe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orango6666&#39;s gravatar image" />
<p><span>orango6666</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orango6666 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '20, 00:21</strong> </span></p>
</div>
</div>
<div id="comments-container-73033" class="comments-container">
&#10;</div>
<div id="comment-tools-73033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73033-form-container" class="comment-form-container">
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

