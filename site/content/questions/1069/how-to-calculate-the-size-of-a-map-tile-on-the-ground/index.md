+++
type = "question"
title = "How to calculate the size of a map tile on the ground?"
description = '''I&#x27;m creating a web interface where users click on a map to denote a point of interest. My application then returns all items in a database that lie within a specified distance of that point. I&#x27;m only concerned with UK (I mention this in case there&#x27;s a good approximation available) and primarily work...'''
date = "2010-10-08T14:12:00Z"
lastmod = "2014-02-14T12:10:00Z"
weight = 1069
keywords = [ "tile", "scale", "coordinates" ]
aliases = [ "/questions/1069" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate the size of a map tile on the ground?](/questions/1069/how-to-calculate-the-size-of-a-map-tile-on-the-ground)

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
<span id="post-1069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1069-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm creating a web interface where users click on a map to denote a point of interest. My application then returns all items in a database that lie within a specified distance of that point. I'm only concerned with UK (I mention this in case there's a good approximation available) and primarily working with zoom=9.</p>
<p>AIUI, each tile covers a certain angle of latitude and longitude rather than distances over the ground. Thanks to the information in <span>this wiki article</span>, I can calculate the distance between the top-left corners of adjacent tiles (and hence derive the distance over the ground for any tile), but that seems rather messy.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-scale" rel="tag" title="see questions tagged &#39;scale&#39;">scale</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '10, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/bf42e40b9124f3b9d818f35f11613554?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pajaholic&#39;s gravatar image" />
<p><span>Pajaholic</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pajaholic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1069" class="comments-container">
&#10;</div>
<div id="comment-tools-1069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1069-form-container" class="comment-form-container">
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

<span id="1078"></span>

<div id="answer-container-1078" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1078-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are happy with an approximation then think about this:</p>
<ul>
<li>At zoom level 9, your world has 2^9 by 2^9 tiles (that's 512x512 tiles).</li>
<li>The Earth's circumference is roughly 40,000 kilometres.</li>
</ul>
<p>Thus:</p>
<ul>
<li>For the y axis, you have 20,000 km from North Pole to South Pole, divided by 512, that's roughly 39 km for the height per tile. (The 512x512 tiles don't exactly stretch all the way to the poles, only to the 85° line, but we can ignore that for this approximation.) This tile height is the same everywhere.</li>
<li>For the x axis it is not quite so easy because the number of kilometres used by the 512 tiles is different depending on where you are - 40,000 km at the Equator, 25,000 at the latitude of the Scilly Isles, and 20,000 at the latitude of Unst. So it's fair to use 22,500 as an approximation for the UK; divide that by 512 and you end up at a tile width of roughly 44km.</li>
</ul>
<p>Or very roughly: A zoom level 9 tile in the UK has 40x40km. (Double the width/height when you decrement the zoom level, halve the width/height when you increment.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '10, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Oct '10, 08:59</strong> </span></p>
</div>
</div>
<div id="comments-container-1078" class="comments-container">
&#10;</div>
<div id="comment-tools-1078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1078-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30744"></span>

<div id="answer-container-30744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30744-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can calculate it yourself, based on <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Resolution_and_Scale">this wiki page</a>:</p>
<pre><code>resolution = 156543.034 meters/pixel * cos(latitude) / (2 ^ zoomlevel)</code></pre>
<p>The resolution means how many meters per pixel you get. If you want to know how many pixels per meter, just use the inverse. That is:</p>
<pre><code>pixels = 1/resolution * distance</code></pre>
<hr />
<p>And if you want to calculate the scale (to write it on the map for printing it):</p>
<pre><code>scale = 1 : (dpi * 39.37 in/m * resolution)</code></pre>
<p>The scale means, how many cm in reality is 1 cm on the paper (or on the screen).</p>
<p>So if you have a screen with 96 dpi, you get that one pixel is 1.1943 meters. And you get a scale of 1 : 4 231 which means that 1 cm on your screen is 42.3 m in reality.</p>
<p>If you have a printer which prints 300 dpi … (now do the calculations yourself).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '14, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-30744" class="comments-container">
&#10;</div>
<div id="comment-tools-30744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30744-form-container" class="comment-form-container">
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

