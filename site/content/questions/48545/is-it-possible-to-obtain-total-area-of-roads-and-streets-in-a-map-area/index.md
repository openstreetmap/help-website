+++
type = "question"
title = "Is it possible to obtain total area of roads and streets in a map area?"
description = '''I would like to obtain the total area of road and streets in a map area (forgive the repetition, but I thought maybe map region is not that specific). My intention is to calculate the density of pedestrians and vehicles in the areas they can use.'''
date = "2016-03-07T15:58:00Z"
lastmod = "2016-03-11T06:30:00Z"
weight = 48545
keywords = [ "measurement", "newbie", "area" ]
aliases = [ "/questions/48545" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to obtain total area of roads and streets in a map area?](/questions/48545/is-it-possible-to-obtain-total-area-of-roads-and-streets-in-a-map-area)

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
<span id="post-48545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48545-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to obtain the total area of road and streets in a map area (forgive the repetition, but I thought maybe map region is not that specific). My intention is to calculate the density of pedestrians and vehicles in the areas they can use.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-measurement" rel="tag" title="see questions tagged &#39;measurement&#39;">measurement</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '16, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9487434b45dfe8b85603edb437cfd459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fa__&#39;s gravatar image" />
<p><span>Fa__</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fa__ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48545" class="comments-container">
&#10;</div>
<div id="comment-tools-48545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48545-form-container" class="comment-form-container">
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

<span id="48546"></span>

<div id="answer-container-48546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48546-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In most cases no, because the width of most roads isn't stored in OSM.</p>
<p>There have been attempts to store highway areas (most successfully via an "area:highway" tag), and some roads have a "width" tag, so you could maybe do something with them.</p>
<p>Maybe you could estimate "if it's a secondary road it'll be X meters wide" externally to OSM and use that in your calculations?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '16, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48546" class="comments-container">
<span id="48547"></span>
<div id="comment-48547" class="comment">
<div id="post-48547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How should I use that estimation? Is it possible to obtain the total length of every kind of road separately and calculate the area using a estimated width for every one of them?</p>
</div>
<div id="comment-48547-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 16:35)</span> <span class="comment-user userinfo">Fa__</span>
</div>
</div>
<span id="48625"></span>
<div id="comment-48625" class="comment">
<div id="post-48625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An option is to download a dataset of roads and load them into a GIS software like QGIS. The length calculation is straightforward. You could even create polygons by buffering the lines. And it is possible to use a data attribute for buffering.</p>
</div>
<div id="comment-48625-info" class="comment-info">
<span class="comment-age">(11 Mar '16, 06:30)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-48546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48546-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48548"></span>

<div id="answer-container-48548" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48548-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In order to get the complete way length of all ways in an OSM file, do a search on this FAQ site for "<strong>length</strong>".</p>
<p>Maybe with the result you can calculate or estimate the covered area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '16, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-48548" class="comments-container">
&#10;</div>
<div id="comment-tools-48548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48548-form-container" class="comment-form-container">
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

