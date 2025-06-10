+++
type = "question"
title = "Calculate tile from latitude and longitude"
description = '''I&#x27;m trying to determine how the &quot;TILE&quot; field in the current_nodes table is calculated based off of the latitude and longitude. I&#x27;ve seen the slippy map tile names and understand the concept of xtile vs. ytile. But I am failing to see the correlation between xtile, ytile, and the TILE value as seen i...'''
date = "2014-12-11T07:19:00Z"
lastmod = "2014-12-11T09:02:00Z"
weight = 39206
keywords = [ "tile", "current_nodes", "slippymap" ]
aliases = [ "/questions/39206" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Calculate tile from latitude and longitude](/questions/39206/calculate-tile-from-latitude-and-longitude)

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
<span id="post-39206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to determine how the "TILE" field in the current_nodes table is calculated based off of the latitude and longitude.</p>
<p>I've seen the <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map tile names</a> and understand the concept of xtile vs. ytile. But I am failing to see the correlation between xtile, ytile, and the TILE value as seen in the current_nodes table. I've seen a write up on Bing about how <a href="http://msdn.microsoft.com/en-us/library/bb259689.aspx">Bing makes the conversion</a>, and it seems similar, but not exact to what OSM is doing. Any ideas?</p>
<p>As an example, using the following latitude and longitude, you should get the following:<br />
Lat: 52.5164839<br />
Lng: 13.3817427<br />
Tile: 3502687520</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-current_nodes" rel="tag" title="see questions tagged &#39;current_nodes&#39;">current_nodes</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '14, 07:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3740fddd7e310cfd4bf54388a30c3e4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhilll&#39;s gravatar image" />
<p><span>jhilll</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhilll has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '14, 07:22</strong> </span></p>
</div>
</div>
<div id="comments-container-39206" class="comments-container">
&#10;</div>
<div id="comment-tools-39206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39206-form-container" class="comment-form-container">
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

<span id="39209"></span>

<div id="answer-container-39209" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39209-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jhilll has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "tile" column in the current_nodes table has nothing to do with map tiles. See <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/lib/quad_tile/quad_tile.h">https://github.com/openstreetmap/openstreetmap-website/blob/master/lib/quad_tile/quad_tile.h</a> for how to compute the value.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '14, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-39209" class="comments-container">
&#10;</div>
<div id="comment-tools-39209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39209-form-container" class="comment-form-container">
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

