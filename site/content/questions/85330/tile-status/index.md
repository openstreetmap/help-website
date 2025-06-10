+++
type = "question"
title = "tile status"
description = '''Hi, according to the wiki https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_%22Standard%22_tile_server, we can have information about the rendering of osm standard tiles. In this section, there is an example with 3 links, the first to see a specific tile, the second to see the status of t...'''
date = "2022-08-12T14:06:00Z"
lastmod = "2022-08-12T15:25:00Z"
weight = 85330
keywords = [ "rendering", "tiles", "standard" ]
aliases = [ "/questions/85330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tile status](/questions/85330/tile-status)

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
<span id="post-85330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>according to the wiki <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_%22Standard%22_tile_server,">https://wiki.openstreetmap.org/wiki/Slippy_Map#OpenStreetMap_%22Standard%22_tile_server,</a> we can have information about the rendering of osm standard tiles.</p>
<p>In this section, there is an example with 3 links, the first to see a specific tile, the second to see the status of this tile and the 3rd to send to osm server an instruction to force it to recalculate this tile.</p>
<p>The first link works, no more the second and third links (message "You requested an invalid tile").</p>
<p>I tried some other tiles, same message. I also tried with "b." at the beginning of the url (b.tile.open...) and with "c.", same result.</p>
<p>A few months ago, all was working.</p>
<p>What's going on ?</p>
<p>Best regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-standard" rel="tag" title="see questions tagged &#39;standard&#39;">standard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '22, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/33b586336c1978cc33b67e8b3cff9cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred73000&#39;s gravatar image" />
<p><span>Fred73000</span><br />
<span class="score" title="54 reputation points">54</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred73000 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85330" class="comments-container">
&#10;</div>
<div id="comment-tools-85330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85330-form-container" class="comment-form-container">
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

<span id="85331"></span>

<div id="answer-container-85331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85331-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM now employs a CDN between the end user and the tile server, to improve tile serving speed and reduce load on the servers. The "status" and "dirty" URLs don't make sense any more because they would not affect (or reflect) the status of a tile in the CDN cache. Hence these URLs are not supported any more. I have updated the wiki page to that effect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '22, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-85331" class="comments-container">
<span id="85332"></span>
<div id="comment-85332" class="comment">
<div id="post-85332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, thanks : so, there is no more way to know the date/hour of a tile ? And to know if a tile is in a queue to be recalculated ? To give an example, I made a changeset yesterday, the result is visible at zoom 18 <a href="https://www.openstreetmap.org/relation/11143425#map=18/55.86532/36.68801">https://www.openstreetmap.org/relation/11143425#map=18/55.86532/36.68801</a> but not at zoom 17 <a href="https://www.openstreetmap.org/relation/11143425#map=17/55.86532/36.68801">https://www.openstreetmap.org/relation/11143425#map=17/55.86532/36.68801</a> and I was wondering why ?</p>
</div>
<div id="comment-85332-info" class="comment-info">
<span class="comment-age">(12 Aug '22, 15:25)</span> <span class="comment-user userinfo">Fred73000</span>
</div>
</div>
</div>
<div id="comment-tools-85331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85331-form-container" class="comment-form-container">
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

