+++
type = "question"
title = "Mapbox tile: how?"
description = '''Hi, I created a tile map with mapbox.com, and I would like to use that as tile of a umap&#x27;map. The your supported openlayers format for replace the tile, is: http://{s}.domain.com/{z}/{x}/{y}.png I talk with mapbox.com team. After 2 month of speaking, mapbox team suggest me this format url: https://a...'''
date = "2018-07-14T19:23:00Z"
lastmod = "2018-07-14T23:16:00Z"
weight = 64726
keywords = [ "tile", "mapbox" ]
aliases = [ "/questions/64726" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapbox tile: how?](/questions/64726/mapbox-tile-how)

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
<span id="post-64726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64726-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I created a tile map with mapbox.com, and I would like to use that as tile of a umap'map.</p>
<p>The your supported openlayers format for replace the tile, is:</p>
<p>http://{s}.domain.com/{z}/{x}/{y}.png</p>
<p>I talk with mapbox.com team. After 2 month of speaking, mapbox team suggest me this format url:</p>
<p><a href="https://api.mapbox.com//styles/v1/papafrancesco/cj8w4kjz08l3x2slhj8c9zmvp/tiles/512/%7Bz%7D/%7Bx%7D/%7By%7D%7B@2x%7D?access_token=pk.eyJ1IjoicGFwYWZyYW5jZXNjbyIsImEiOiJjaXFmZDRubzkwMDduaHhuaHVxemk5amZ5In0.cpMeGC7s9Pw8KqKXalh0Wg">https://api.mapbox.com//styles/v1/papafrancesco/cj8w4kjz08l3x2slhj8c9zmvp/tiles/512/{z}/{x}/{y}{@2x}?access_token=pk.eyJ1IjoicGFwYWZyYW5jZXNjbyIsImEiOiJjaXFmZDRubzkwMDduaHhuaHVxemk5amZ5In0.cpMeGC7s9Pw8KqKXalh0Wg</a></p>
<p>BUT IT DON'T WORK</p>
<p>Mapbox team says me that the openlayers format is correct, and if don't work, the problem is by umap, not mapbox team.</p>
<p>Can you help me?</p>
<p>Francesco</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '18, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/c102f7eb92270d115d6dea8c4e0e8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franccicccio&#39;s gravatar image" />
<p><span>franccicccio</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franccicccio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64726" class="comments-container">
&#10;</div>
<div id="comment-tools-64726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64726-form-container" class="comment-form-container">
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

<span id="64729"></span>

<div id="answer-container-64729" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64729-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if umap supports the @2x in brackets.. Maybe try explicitly including or excluding it. Also try changing from 512 tiles to 256 tiles to see if that helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '18, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharvey has 4 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-64729" class="comments-container">
&#10;</div>
<div id="comment-tools-64729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64729-form-container" class="comment-form-container">
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

