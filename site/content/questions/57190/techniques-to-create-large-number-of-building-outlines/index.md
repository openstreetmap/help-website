+++
type = "question"
title = "Techniques to create large number of building outlines"
description = '''Would someone be able to help me out by explaining to me what the standard technique is to create building outlines on a map such as what google maps has in their 2d map view when zoomed in? I am assuming places such as google used aerial imagery &amp;amp; other methods to create these building outlines...'''
date = "2017-07-19T23:47:00Z"
lastmod = "2017-07-20T09:24:00Z"
weight = 57190
keywords = [ "building", "osm", "aerial", "outlines", "lidar" ]
aliases = [ "/questions/57190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Techniques to create large number of building outlines](/questions/57190/techniques-to-create-large-number-of-building-outlines)

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
<span id="post-57190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57190-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Would someone be able to help me out by explaining to me what the standard technique is to create building outlines on a map such as what google maps has in their 2d map view when zoomed in? I am assuming places such as google used aerial imagery &amp; other methods to create these building outlines? I saw some people that used lidar data where available in certain places but I was trying to figure out if there was some method that could be used to create these building outlines using already existing public data such as satellite images and other means. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-aerial" rel="tag" title="see questions tagged &#39;aerial&#39;">aerial</span> <span class="post-tag tag-link-outlines" rel="tag" title="see questions tagged &#39;outlines&#39;">outlines</span> <span class="post-tag tag-link-lidar" rel="tag" title="see questions tagged &#39;lidar&#39;">lidar</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '17, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/283d960f05b6e8d6b6e936e5c361cb5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="comp_user&#39;s gravatar image" />
<p><span>comp_user</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="comp_user has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57190" class="comments-container">
&#10;</div>
<div id="comment-tools-57190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57190-form-container" class="comment-form-container">
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

<span id="57191"></span>

<div id="answer-container-57191" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57191-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-57191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I trace them, usually using the Bing imagery layer in JOSM. There is a building tool plug-in for JOSM that is supposed to make it easier/quicker but I find that it is faster for me to simply click around the perimeter with the drawing tool then use the "q" key to square it up (assuming a building that can be squared up).</p>
<p>There have been some imports of building outlines from governmental or other sources that have appropriate licensing (that is how many/most of the buildings in Los Angeles county were recently entered into OSM). But a lot of it is plain grunt work. I typically do my tracing after I've walked an area collecting street numbers and am entering the house number data.</p>
<p>Now that there are starting to be tools to help enter and render 3D buildings I guess I should start learning that tagging. Always more improvements that can be made even in areas you live in and have, you thought, throughly mapped.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '17, 02:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-57191" class="comments-container">
<span id="57192"></span>
<div id="comment-57192" class="comment">
<div id="post-57192-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5918/stf"></a><a href="https://help.openstreetmap.org/users/5918/stf">@stf</a> the easiest 3D tags to add are <a href="https://wiki.openstreetmap.org/wiki/Key:building:levels">building:levels</a> and roof:levels, just count the number of levels.</p>
</div>
<div id="comment-57192-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 05:39)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="57194"></span>
<div id="comment-57194" class="comment">
<div id="post-57194-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While there are tools to trace building automatically/algorithmicaly from satellite (and maybe lidar) imagery, they are currently more trouble than they're worth unless the imagery is unusually clear (and typically only works for flat-roofed buildings). Tracing water bodies using those tools is a bit more likely to work but still not great.</p>
</div>
<div id="comment-57194-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 09:24)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57191-form-container" class="comment-form-container">
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

