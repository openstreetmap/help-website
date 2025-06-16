+++
type = "question"
title = "How to generate list of tiles from bbox"
description = '''Hi I have a dumb question maybe because I don&#x27;t really understand how the generation of tiles depending on the minLon,MinLat, MaxLon,MaxLat numbers? How to calculate  /folderNumber(Zoom)   /FolderNumber   tileNumber  ???'''
date = "2013-09-06T14:28:00Z"
lastmod = "2013-09-06T17:12:00Z"
weight = 26158
keywords = [ "tiles", "osm" ]
aliases = [ "/questions/26158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to generate list of tiles from bbox](/questions/26158/how-to-generate-list-of-tiles-from-bbox)

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
<span id="post-26158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26158-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have a dumb question maybe because I don't really understand how the generation of tiles depending on the minLon,MinLat, MaxLon,MaxLat numbers?</p>
<p>How to calculate</p>
<p>/folderNumber(Zoom) /FolderNumber tileNumber</p>
<p>???</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '13, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26158" class="comments-container">
<span id="26160"></span>
<div id="comment-26160" class="comment">
<div id="post-26160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you talking about in the context of something like "generate_tiles.py" or in some other context?</p>
</div>
<div id="comment-26160-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 15:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="26163"></span>
<div id="comment-26163" class="comment">
<div id="post-26163-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am talking overall.</p>
</div>
<div id="comment-26163-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 16:41)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="26164"></span>
<div id="comment-26164" class="comment">
<div id="post-26164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Er what? Perhaps it would help if you could explain what exactly it is that you are trying to do.</p>
</div>
<div id="comment-26164-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 17:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="26165"></span>
<div id="comment-26165" class="comment">
<div id="post-26165-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am trying in rhomobile(ruby mobile app framework) write a mechanism of tile caching for a given bbox</p>
</div>
<div id="comment-26165-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 17:12)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-26158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26158-form-container" class="comment-form-container">
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

<span id="26159"></span>

<div id="answer-container-26159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26159-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Starting in the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Tiles">Tiles</a> ... there is a link to <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">Slippy_map_tilenames</a></p>
<p>Tell us if you cannot a solution though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '13, 15:12</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-26159" class="comments-container">
<span id="26161"></span>
<div id="comment-26161" class="comment">
<div id="post-26161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi <span>@Stephan75</span>, I have saw those earlier, but the problem is I don't understand how much to cicle for each zoom to get next tile? -74.25909,40.477399,-73.700172,40.917577. Lets say 40.477399-40.917577 . For each zoom level loop how much should be the step value ? (0.001 ? 0.002? ) . I would be very greatfull if somebody will provide an example on perl or php ...</p>
</div>
<div id="comment-26161-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 15:58)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-26159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26159-form-container" class="comment-form-container">
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

