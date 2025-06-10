+++
type = "question"
title = "Export PNG square with 1024km2"
description = '''How can i export PNG or SVG perfect square with area of 1024km2? '''
date = "2021-02-28T15:51:00Z"
lastmod = "2021-02-28T17:22:00Z"
weight = 79070
keywords = [ "export" ]
aliases = [ "/questions/79070" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export PNG square with 1024km2](/questions/79070/export-png-square-with-1024km2)

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
<span id="post-79070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can i export PNG or SVG perfect square with area of 1024km2?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '21, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6a3ce94a070a5197467f2c2fd0ea4e36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mddoff&#39;s gravatar image" />
<p><span>mddoff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mddoff has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79070" class="comments-container">
&#10;</div>
<div id="comment-tools-79070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79070-form-container" class="comment-form-container">
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

<span id="79073"></span>

<div id="answer-container-79073" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79073-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an interesting questions. If you are looking for a web service that lets you do that easily, there is none; you will have to run some calculations by yourself. Note that the map projection governs whether what is a square on the ground of the Earth ellipsoid is also a square in the resulting two-dimensional image; you don't say if you need a square PNG (but don't need a square patch of Earth), or if you need a square patch of Earth (but not necessarily a square PNG).</p>
<p>So your question has two parts, first: how to determine the coordinates of the four corners of this area (depending on projection and whether you need a square on Earth or a square result); second: how to export an area with known coordinates from OSM.</p>
<p>The first question is not OpenStreetMap specific and you will likely get better responses on a general GIS forum or Q&amp;A site.</p>
<p>The second question has a number of different answers. If the EPSG:3857 map projection works for you, then you can use OSM's own image exporter (on www.openstreetmap.org, the icon on the right hand side of the map that shows an arrow pointing out of a box). It lets you select the four corners of the export area on the map but if you use your browser's network debugger you can see the request it generates and generate such a request yourself with the exact coordinates you have computed. Another option, especially if you are interested in different projections, might be one of the free third-party WMS servers from <a href="https://wiki.openstreetmap.org/wiki/WMS.">https://wiki.openstreetmap.org/wiki/WMS.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '21, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79073" class="comments-container">
&#10;</div>
<div id="comment-tools-79073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79073-form-container" class="comment-form-container">
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

