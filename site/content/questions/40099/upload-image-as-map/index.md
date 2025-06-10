+++
type = "question"
title = "Upload image as map"
description = '''Good morning, I am developing a new game and I need an online map where I can upload my &quot;Game Map&quot; (it&#x27;s a City) to use instead of the normal world map. Is this possible in some way? Just to make an example, I need something like this, but with MY image as map: http://maps.marlam.in/ Thanks for your...'''
date = "2015-01-07T13:40:00Z"
lastmod = "2015-01-07T13:53:00Z"
weight = 40099
keywords = [ "image", "videogame" ]
aliases = [ "/questions/40099" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Upload image as map](/questions/40099/upload-image-as-map)

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
<span id="post-40099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40099-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-40099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good morning, I am developing a new game and I need an online map where I can upload my "Game Map" (it's a City) to use instead of the normal world map. Is this possible in some way? Just to make an example, I need something like this, but with MY image as map: <a href="http://maps.marlam.in/">http://maps.marlam.in/</a></p>
<p>Thanks for your help, Giulio.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-videogame" rel="tag" title="see questions tagged &#39;videogame&#39;">videogame</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '15, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0f726318c3a4c5dd3132b703f06506d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Giulio17&#39;s gravatar image" />
<p><span>Giulio17</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Giulio17 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40099" class="comments-container">
&#10;</div>
<div id="comment-tools-40099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40099-form-container" class="comment-form-container">
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

<span id="40100"></span>

<div id="answer-container-40100" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40100-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-40100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Giulio17 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. You won't upload your image to anything - you'd simply use the gdal2tiles utility or some similar map tiling program to split your image into a series of "tiles", and then you can host that on any webspace and use OpenLayers or Leaflet to display it. (gdal2tiles will even generate a small .html map page with OpenLayers for you.)</p>
<p>This question is not OpenStreetMap related.</p>
<p>If you do not have a large image of your map already, but wish to use OSM technology to draw one, check out <a href="http://www.opengeofiction.net">opengeofiction.net.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '15, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40100" class="comments-container">
&#10;</div>
<div id="comment-tools-40100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40100-form-container" class="comment-form-container">
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

