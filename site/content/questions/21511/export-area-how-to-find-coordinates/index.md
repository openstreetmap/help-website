+++
type = "question"
title = "Export Area - How to find coordinates"
description = '''Hi, I need to export an area from OSM. As I needed the exported part of the map to be a certain area e.g. 2000m x 2000m, I got coordinates for precisely that size area from Bing Maps (lat, long of each of the four points of the square). What I don&#x27;t understand is what coordinates I need to put into ...'''
date = "2013-04-13T22:39:00Z"
lastmod = "2013-04-14T22:20:00Z"
weight = 21511
keywords = [ "export" ]
aliases = [ "/questions/21511" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export Area - How to find coordinates](/questions/21511/export-area-how-to-find-coordinates)

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
<span id="post-21511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21511-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to export an area from OSM. As I needed the exported part of the map to be a certain area e.g. 2000m x 2000m, I got coordinates for precisely that size area from Bing Maps (lat, long of each of the four points of the square).</p>
<p>What I don't understand is what coordinates I need to put into the "Area to Export" fields as only two lat/long values are required.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '13, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/05120e6e3dbb311df5314657b6e03548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerrymaid&#39;s gravatar image" />
<p><span>kerrymaid</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerrymaid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21511" class="comments-container">
&#10;</div>
<div id="comment-tools-21511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21511-form-container" class="comment-form-container">
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

<span id="21530"></span>

<div id="answer-container-21530" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21530-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're right a bounding box has four edges with lat/lon each, resulting in four, not two lat/lon pairs. What you're missing is: The box is not rotated. That means two sides of the box are in parallel with the equator. Therefore two connected points always share either the latitude or the longitude. That's why only two lat/lon pairs suffice to describe a bounding box.</p>
<p>In other words you need so specify the max latitude, min latitude, max longitude and min longitude to describe a bounding box that you want to query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '13, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/680bc1d9127776b4acb2e6af485a6869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="konstantin&#39;s gravatar image" />
<p><span>konstantin</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="konstantin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21530" class="comments-container">
&#10;</div>
<div id="comment-tools-21530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21530-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21513"></span>

<div id="answer-container-21513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are four parameters in the "Area to Export" page on the OSM map. If you have the four box co-ordinates for an area then take the first number in your first box coordinate pair and put it in the first "Area to Export" field. Put the second member of the first box pair in the second field. Fill in the third and fourth "Area to Export" fields with the values from the last co-ordinate pair for your box.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '13, 23:44</strong></p>
<img src="https://secure.gravatar.com/avatar/4afbcc50f5d94cce5f85c1da49f3de6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Feilipu&#39;s gravatar image" />
<p><span>Feilipu</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Feilipu has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '13, 23:45</strong> </span></p>
</div>
</div>
<div id="comments-container-21513" class="comments-container">
&#10;</div>
<div id="comment-tools-21513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21513-form-container" class="comment-form-container">
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

