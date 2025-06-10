+++
type = "question"
title = "TileCache with OpenCycleMap and OSM"
description = '''Hello all. I very often download maps for offline usage on a handheld device (that is, an Android phone with the Oruxmaps program). I did set up a TileCache server local to my environment: the idea is to use it so to save bandwidth from the servers I get the maps from, and to get my maps faster once...'''
date = "2012-06-25T12:58:00Z"
lastmod = "2012-06-25T19:40:00Z"
weight = 13761
keywords = [ "tilecache", "opencyclemap" ]
aliases = [ "/questions/13761" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TileCache with OpenCycleMap and OSM](/questions/13761/tilecache-with-opencyclemap-and-osm)

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
<span id="post-13761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all.</p>
<p>I very often download maps for offline usage on a handheld device (that is, an Android phone with the <a href="http://www.oruxmaps.com/index_en.html">Oruxmaps</a> program). I did set up a <a href="http://tilecache.org/">TileCache</a> server local to my environment: the idea is to use it so to save bandwidth from the servers I get the maps from, and to get my maps faster once I downloaded the tiles of an area already (very often the maps I download do overlap to some extent, so to download the very same tiles over and over is not efficient neither for the servers nor myself).</p>
<p>Whilst I could successfully configure TileCache for some WMS services, though, I could not find how to use it with OpenStreetMap and OpenCycleMap in particular. Is there a "quick and dirty" way to get to the point? Thanks so much.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilecache" rel="tag" title="see questions tagged &#39;tilecache&#39;">tilecache</span> <span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '12, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/12183e1acd253b9b337134498b2bfad9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Febs&#39;s gravatar image" />
<p><span>Febs</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Febs has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '12, 15:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13761" class="comments-container">
&#10;</div>
<div id="comment-tools-13761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13761-form-container" class="comment-form-container">
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

<span id="13766"></span>

<div id="answer-container-13766" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13766-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Febs has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is commendable that you set up a cache to save bandwidth, however even then, the bulk downloading from OSM or OpenCycleMap is discouraged (in the case of OSM, <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">http://wiki.openstreetmap.org/wiki/Tile_usage_policy</a>) or strictly forbidden (in the case of OpenCycleMap, <a href="http://thunderforest.com/terms/">http://thunderforest.com/terms/</a>). So if you need local OSM tiles for your applications, you will have to set up your own tile server. Some pointers to that are on <a href="http://switch2osm.org/">http://switch2osm.org/</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '12, 16:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13766" class="comments-container">
<span id="13770"></span>
<div id="comment-13770" class="comment">
<div id="post-13770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please notice that I don't want to bulk download at all; my purpose is just to avoid to download the same tiles of an area I already fetched while preparing the maps of my previous hike. That's all. Thanks for the link though.</p>
</div>
<div id="comment-13770-info" class="comment-info">
<span class="comment-age">(25 Jun '12, 17:54)</span> <span class="comment-user userinfo">Febs</span>
</div>
</div>
<span id="13772"></span>
<div id="comment-13772" class="comment">
<div id="post-13772-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should check with the provider of the maps you are planning to use; "fetching" tiles with anything else than a web browser for anything else than immediate viewing is pretty much the definition of "bulk downloading".</p>
</div>
<div id="comment-13772-info" class="comment-info">
<span class="comment-age">(25 Jun '12, 19:40)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13766" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13766-form-container" class="comment-form-container">
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

