+++
type = "question"
title = "Area measured by JOSM measurement plugin"
description = '''I am using the measurement plugin for JOSM. When using the option select everything, every road appears as selected and by using the measurement option I can obtain path length and selected area. Does this selected area displayed refers to the area of the whole osm map or just to the roads (and othe...'''
date = "2016-04-11T16:58:00Z"
lastmod = "2016-04-12T11:03:00Z"
weight = 49183
keywords = [ "josm", "area", "newbie", "measurement" ]
aliases = [ "/questions/49183" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Area measured by JOSM measurement plugin](/questions/49183/area-measured-by-josm-measurement-plugin)

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
<span id="post-49183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the measurement plugin for JOSM. When using the option select everything, every road appears as selected and by using the measurement option I can obtain path length and selected area. Does this selected area displayed refers to the area of the whole osm map or just to the roads (and other ways), which are the elements that are shown as selected?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-measurement" rel="tag" title="see questions tagged &#39;measurement&#39;">measurement</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '16, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9487434b45dfe8b85603edb437cfd459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fa__&#39;s gravatar image" />
<p><span>Fa__</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fa__ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49183" class="comments-container">
&#10;</div>
<div id="comment-tools-49183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49183-form-container" class="comment-form-container">
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

<span id="49185"></span>

<div id="answer-container-49185" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49185-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Fa__ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Neither.</p>
<p>The area displayed by the "measurement" plugin is the sum of the areas of every closed way in your selection. That means that if two areas overlap (say, a pond inside a park), the overlapping area gets counted twice. It also means that areas formed by multiple ways (such as a city boundary defined by several roads) aren't counted at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '16, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-49185" class="comments-container">
<span id="49186"></span>
<div id="comment-49186" class="comment">
<div id="post-49186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't want to hijack this thread but I use the measurement tool quite a bit but cannot seem to find a way to switch the area units from hectares to acres. Can you help?</p>
</div>
<div id="comment-49186-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 00:26)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="49189"></span>
<div id="comment-49189" class="comment">
<div id="post-49189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a> There is a ruler symbol on the bottom of the map. By clicking on it you change the units. A message explaining the change will appear. There are several units that can be chosen, click on the ruler until the one you are looking for appears.</p>
</div>
<div id="comment-49189-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 08:39)</span> <span class="comment-user userinfo">Fa__</span>
</div>
</div>
<span id="49190"></span>
<div id="comment-49190" class="comment">
<div id="post-49190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11913/carnildo">@Carnildo</a> Thank you for your answer. Is there a way to avoid counting twice overlapping areas?</p>
</div>
<div id="comment-49190-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 08:46)</span> <span class="comment-user userinfo">Fa__</span>
</div>
</div>
<span id="49195"></span>
<div id="comment-49195" class="comment">
<div id="post-49195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/115/fake-stevec">@Fa</a>, Thank you. That control is fairly well hidden LOL.</p>
</div>
<div id="comment-49195-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 11:03)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-49185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49185-form-container" class="comment-form-container">
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

