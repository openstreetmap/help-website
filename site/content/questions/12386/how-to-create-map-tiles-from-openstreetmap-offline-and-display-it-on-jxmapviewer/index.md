+++
type = "question"
title = "How to create map tiles from OpenStreetMap offline and display it on JxMapViewer?"
description = '''I need to display world map( A single Map with a view of whole world) by JxMapviewer with OpenStreetMap. The map need to be available locally . How can I download worldmap from OpenStreetmap and display it on JxMapViewer? Thanks.'''
date = "2012-04-27T10:54:00Z"
lastmod = "2012-05-02T07:09:00Z"
weight = 12386
keywords = [ "map", "offline", "osm", "for", "jxmapviewer" ]
aliases = [ "/questions/12386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create map tiles from OpenStreetMap offline and display it on JxMapViewer?](/questions/12386/how-to-create-map-tiles-from-openstreetmap-offline-and-display-it-on-jxmapviewer)

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
<span id="post-12386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12386-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to display world map( A single Map with a view of whole world) by JxMapviewer with OpenStreetMap. The map need to be available locally . How can I download worldmap from OpenStreetmap and display it on JxMapViewer? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span> <span class="post-tag tag-link-jxmapviewer" rel="tag" title="see questions tagged &#39;jxmapviewer&#39;">jxmapviewer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '12, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/5d5ba4c5e2429e318407e81498842447?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DSreddy&#39;s gravatar image" />
<p><span>DSreddy</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DSreddy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12386" class="comments-container">
&#10;</div>
<div id="comment-tools-12386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12386-form-container" class="comment-form-container">
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

<span id="12387"></span>

<div id="answer-container-12387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12387-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally we don't allow bulk downloads from OpenStreetMap (see <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a>). However if you really only want a world overview map (without zooming in) then that would amount to just a handful of tiles and you could probably download them without causing trouble.</p>
<p>If, on the other hand, you want to be able to zoom in, then you will need many more tiles and you will have to produce them yourself. You will have to install a tile generator like TileMill, or plain Mapnik with the generate_tiles.py script, or even Maperitive (works for smaller areas, not whole world). You will also need some space for a database (about 300 GB) to import OSM data into, and depending on what zoom level you want to go up to, you will need a lot of time for rendering the tiles. (All programs mentioned in this paragraph have pages on our wiki.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '12, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12387" class="comments-container">
<span id="12498"></span>
<div id="comment-12498" class="comment">
<div id="post-12498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik for your reply.</p>
</div>
<div id="comment-12498-info" class="comment-info">
<span class="comment-age">(02 May '12, 07:09)</span> <span class="comment-user userinfo">DSreddy</span>
</div>
</div>
</div>
<div id="comment-tools-12387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12387-form-container" class="comment-form-container">
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

