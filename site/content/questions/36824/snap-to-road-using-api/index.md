+++
type = "question"
title = "Snap to road using API"
description = '''Hello, would it be possible with OSM API, to magnet point, based on gps coordinates, to the closest road? So simply, how to determine closest car position on the road, based on gps coordinates which shows off-road position.'''
date = "2014-09-14T23:10:00Z"
lastmod = "2014-09-22T18:55:00Z"
weight = 36824
keywords = [ "api", "road", "gps" ]
aliases = [ "/questions/36824" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Snap to road using API](/questions/36824/snap-to-road-using-api)

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
<span id="post-36824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36824-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, would it be possible with OSM API, to magnet point, based on gps coordinates, to the closest road? So simply, how to determine closest car position on the road, based on gps coordinates which shows off-road position.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '14, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/3cebc21c0476e9fc5167e7287c109246?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janzamoy&#39;s gravatar image" />
<p><span>janzamoy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janzamoy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '14, 12:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-36824" class="comments-container">
<span id="36825"></span>
<div id="comment-36825" class="comment">
<div id="post-36825-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The OSM API is used for uploading data to OSM, not for displaying it.</p>
</div>
<div id="comment-36825-info" class="comment-info">
<span class="comment-age">(14 Sep '14, 23:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36829"></span>
<div id="comment-36829" class="comment">
<div id="post-36829-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Furthermore the API doesn't provide a snap-to-road feature. But of course you can implement it yourself with the help of OSM data.</p>
</div>
<div id="comment-36829-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 08:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="36841"></span>
<div id="comment-36841" class="comment">
<div id="post-36841-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In other words, you can use OSM data from various sources (like the planet or from planet extracts), keep only the roads data (and possibly simply them), then develop your own algorythm to find the nearest road based on lat/lon coordinates (with a certain velocity to avoid wrong streets determination at e.g. junctions)</p>
</div>
<div id="comment-36841-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 13:19)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-36824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36824-form-container" class="comment-form-container">
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

<span id="36979"></span>

<div id="answer-container-36979" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36979-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some routing applications on smartphones that can display your GPS position on an OSM based map, and you can enable "snap-to-road" feature.</p>
<p>See for example <a href="http://wiki.openstreetmap.org/wiki/Osmand">Osmand</a> for android devices ... it is open source and has an own mailing list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '14, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-36979" class="comments-container">
&#10;</div>
<div id="comment-tools-36979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36979-form-container" class="comment-form-container">
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

