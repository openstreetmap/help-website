+++
type = "question"
title = "how can i get best symbolistic for gis display related to zoom level?"
description = '''Hello, can someone tell me what is the relation between zoom level and the data displayed. That is, for a certain zoom level the user can see certain vector or raster data, and when zooming in, another set of data is displayed. how are the symbols chosen: color, width, or raster scale, resolution, a...'''
date = "2011-11-14T08:24:00Z"
lastmod = "2011-11-15T08:22:00Z"
weight = 8967
keywords = [ "zoomlevel", "datadisplay" ]
aliases = [ "/questions/8967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can i get best symbolistic for gis display related to zoom level?](/questions/8967/how-can-i-get-best-symbolistic-for-gis-display-related-to-zoom-level)

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
<span id="post-8967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, can someone tell me what is the relation between zoom level and the data displayed. That is, for a certain zoom level the user can see certain vector or raster data, and when zooming in, another set of data is displayed. how are the symbols chosen: color, width, or raster scale, resolution, and color (when map) for a zoom level and how is that done, through programming? i would like to set up a gis for a city and i need to know these things so my display always looks good, no matter the zoom level, you know what i mean. can i do this in arcgis for example? do i have to use multiple data frames?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-datadisplay" rel="tag" title="see questions tagged &#39;datadisplay&#39;">datadisplay</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '11, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/aacdad94758a6d0edce5cfdab9962740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scemy&#39;s gravatar image" />
<p><span>scemy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scemy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '11, 06:48</strong> </span></p>
</div>
</div>
<div id="comments-container-8967" class="comments-container">
&#10;</div>
<div id="comment-tools-8967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8967-form-container" class="comment-form-container">
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

<span id="9003"></span>

<div id="answer-container-9003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9003-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The minimum and maximum zoom level at which a certain kind of object will be drawn depends on the renderer and its rules/stylesheet (the wiki has a <a href="https://wiki.openstreetmap.org/wiki/Mapnik#Stylesheet">section about mapnik's stylesheet</a>). You can use this as a starting point for rendering your own maps. Everything else doesn't seem to have much to do with OpenStreetMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '11, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9003" class="comments-container">
&#10;</div>
<div id="comment-tools-9003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9003-form-container" class="comment-form-container">
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

