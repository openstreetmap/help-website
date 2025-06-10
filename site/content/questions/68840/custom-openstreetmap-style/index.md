+++
type = "question"
title = "Custom OpenStreetMap style"
description = '''I want to use a custom style over an OpenStreetMap map, to change some colors, avoid showing some texts and stuff like that. I only need an image of the final map (I need it for a poster). I have seen there are several solutions, like Mapzen and Mapbox, but they seem focused in displaying the map in...'''
date = "2019-04-18T18:16:00Z"
lastmod = "2019-04-19T16:25:00Z"
weight = 68840
keywords = [ "style", "maperitive", "mapbox" ]
aliases = [ "/questions/68840" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Custom OpenStreetMap style](/questions/68840/custom-openstreetmap-style)

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
<span id="post-68840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68840-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use a custom style over an OpenStreetMap map, to change some colors, avoid showing some texts and stuff like that.</p>
<p>I only need an image of the final map (I need it for a poster). I have seen there are several solutions, like Mapzen and Mapbox, but they seem focused in displaying the map in a website and pricing by the number of visits per month, so I don't think I can use them to just take a picture of the map.</p>
<p>I have tried Maperitive, but it just doesn't work with big maps.</p>
<p>What do you recommend me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '19, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/831da0918fc7a102b221e99413c625d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hashmaper&#39;s gravatar image" />
<p><span>hashmaper</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hashmaper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68840" class="comments-container">
&#10;</div>
<div id="comment-tools-68840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68840-form-container" class="comment-form-container">
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

<span id="68849"></span>

<div id="answer-container-68849" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68849-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hashmaper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simplest solution is exporting a large image via the web site and then modifying in a graphics program. (You can export SVG too.) More flexible solution is loading data into your own PostgreSQL database and rendering openstreetmap-carto, mapnik, nik4.py but that requires Linux and quite a bit of software installation. If the map you want to make is just "a little too big for Maperitive" then pre-filtering the OSM data with osmfilter or osmosis - throwing out all the houses and residential roads and other stuff that won't show anyway - could potentially bring your data size down to something that Maperitive can handle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '19, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68849" class="comments-container">
&#10;</div>
<div id="comment-tools-68849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68849-form-container" class="comment-form-container">
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

