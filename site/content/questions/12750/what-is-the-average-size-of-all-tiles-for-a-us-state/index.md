+++
type = "question"
title = "What is the average size of all tiles for a US state?"
description = '''On average, if all tiles for an average US state were rendered at 15 zoom levels with default styles using Mapnik, how much would be the total used disk space by all PNG files? 200MB/500MB/1GB/5GB/1TB? I know for the whole world it is 20TB.'''
date = "2012-05-15T19:26:00Z"
lastmod = "2012-06-13T01:32:00Z"
weight = 12750
keywords = [ "tiles", "mapnik", "render", "size" ]
aliases = [ "/questions/12750" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the average size of all tiles for a US state?](/questions/12750/what-is-the-average-size-of-all-tiles-for-a-us-state)

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
<span id="post-12750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On average, if all tiles for an average US state were rendered at 15 zoom levels with default styles using Mapnik, how much would be the total used disk space by all PNG files? 200MB/500MB/1GB/5GB/1TB? I know for the whole world it is 20TB.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '12, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/752a4621191717194f17ba466d4b2451?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiveCarMap&#39;s gravatar image" />
<p><span>LiveCarMap</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiveCarMap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12750" class="comments-container">
&#10;</div>
<div id="comment-tools-12750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12750-form-container" class="comment-form-container">
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

<span id="13447"></span>

<div id="answer-container-13447" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13447-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LiveCarMap has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get an estimate of the number of tiles you need to cover a state, go to map.geofabrik.de and activate the "tile coordinates" overlay (from the layer switcher in the top right corner of the map). Zoom in on the state you're interested in. You'll get something like this:</p>
<p><img src="/upfiles/tiles.png" alt="tiles colorado" /></p>
<p>So, Colorado for example has about one and half tiles on zoom level 6. The number of tiles quadruples for each zoom level, so you are looking at...</p>
<ul>
<li>1.5 tiles on z6</li>
<li>6 tiles on z7</li>
<li>24 tiles on z8</li>
<li>96 on z9</li>
<li>400 on z10</li>
<li>1600 on z11</li>
<li>6400 on z12</li>
<li>25k on z13</li>
<li>100k on z14</li>
<li>400k on z15</li>
</ul>
<p>making a total of roughly 500k tiles. Now the average size of tiles is a tricky thing, it varies between zoom levels. But if your scenario includes tiles on higher zoom levels then the average size is surprisingly small - something like 2 kB. Tiles can easily reach 50kB and more but on high zooms, most of Colorado will likely be almost empty and the empty ones dominate the few large inner-city tiles. (And, tile count wise, the higher zoom levels dominate the lower ones.)</p>
<p>So the answer to your question is that for a state the size of Colorado and up to z15, you're probably looking at 2 kB * 500k tiles = 1 GB of tile storage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '12, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-13447" class="comments-container">
<span id="13484"></span>
<div id="comment-13484" class="comment">
<div id="post-13484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this answers my question.</p>
</div>
<div id="comment-13484-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 01:32)</span> <span class="comment-user userinfo">LiveCarMap</span>
</div>
</div>
</div>
<div id="comment-tools-13447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13447-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13323"></span>

<div id="answer-container-13323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could also find the size of a single tile and then multiply that number for the area of the state that you are trying to cover. You just have to download the vector data and determine how far across a single tile is. Then find the x and y axis for the state and then finally multiply. It will be a rough estimate but still give you a baseline.</p>
<p>Cheers, Nicholas</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '12, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5c34b9dddd033da37483a8634fab6a82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingalls&#39;s gravatar image" />
<p><span>ingalls</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13323" class="comments-container">
&#10;</div>
<div id="comment-tools-13323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13323-form-container" class="comment-form-container">
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

