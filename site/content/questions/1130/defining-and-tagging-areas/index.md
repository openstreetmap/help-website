+++
type = "question"
title = "Defining and tagging areas"
description = '''The rural area where I live has a lot of Greens and Commons. How can I define these on the map? Similarly, can I map areas of woodland and field boundaries?'''
date = "2010-10-11T16:16:00Z"
lastmod = "2010-10-11T22:21:00Z"
weight = 1130
keywords = [ "green", "boundary", "woodland", "common", "field" ]
aliases = [ "/questions/1130" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Defining and tagging areas](/questions/1130/defining-and-tagging-areas)

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
<span id="post-1130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The rural area where I live has a lot of Greens and Commons. How can I define these on the map? Similarly, can I map areas of woodland and field boundaries?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-green" rel="tag" title="see questions tagged &#39;green&#39;">green</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-woodland" rel="tag" title="see questions tagged &#39;woodland&#39;">woodland</span> <span class="post-tag tag-link-common" rel="tag" title="see questions tagged &#39;common&#39;">common</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '10, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7804d12c173db8b6c9869b814cf8f5db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yapmaul&#39;s gravatar image" />
<p><span>yapmaul</span><br />
<span class="score" title="121 reputation points">121</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yapmaul has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Oct '10, 16:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1130" class="comments-container">
&#10;</div>
<div id="comment-tools-1130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1130-form-container" class="comment-form-container">
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

<span id="1137"></span>

<div id="answer-container-1137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1137-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is both a technical and a ontological dimension to this question.</p>
<p>Technically, the way to define an area, which is not a separate feature type in the OpenStreetMap data model, is to create a way (line) that has a common first and last point: a closed way. See <a href="https://wiki.openstreetmap.org/wiki/Elements#Area_.28closed_way_.29">here</a> for the relevant information on the OpenStreetMap Wiki.</p>
<p>Depending on how you tag your closed way, it will be rendered as an area on the map. The <a href="https://wiki.openstreetmap.org/wiki/Map_Features">Map Features</a> page on the OpenStreetMap wiki will give you an indication as to which tags can be applied to closed ways in order to have them redered as visible areas. For example, tagging a closed way as <a href="https://wiki.openstreetmap.org/wiki/Map_Features#Landuse"><code>landuse=village_green</code></a> will make that feature show up as a green area on the rendered map. Key-value combinations that apply to closed ways will be indicated by the area icon on this page: <img src="https://wiki.openstreetmap.org/w/images/8/83/Mf_area.png" alt="alt text" /></p>
<p>Note that there are several similar key-value combinations for green areas in built-up areas: <code>leisure=park</code>, <code>landuse=village_green</code>, <code>landuse=grass</code>, <code>landuse=recreation_ground</code>, to name a few. Ask on your local mailing list or here to learn more about the sometimes intricate differences.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '10, 22:21</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-1137" class="comments-container">
&#10;</div>
<div id="comment-tools-1137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1137-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1131"></span>

<div id="answer-container-1131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1131-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Areas are ways that starts and ends in the same node. Just add a way around the area and add the appropriate tags. If the area is made up of several ways or have holes in it you might be interested in the <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon</a> relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '10, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1131" class="comments-container">
&#10;</div>
<div id="comment-tools-1131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1131-form-container" class="comment-form-container">
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

