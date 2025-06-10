+++
type = "question"
title = "Openstreetmap server high availability"
description = '''Hi everyone ! I&#x27;d like to build an OpenStreetMap server for my company ... We want to handle a large area of data (the whole Europe). My question is quite simple, i&#x27;d like to know if there is a simple (or not ) way to pre compile tiles for this area in order to fill the /var/lib/mod_tile folder. Onc...'''
date = "2014-04-29T15:52:00Z"
lastmod = "2014-04-29T18:06:00Z"
weight = 32744
keywords = [ "high-speed", "precompiled", "tileserver" ]
aliases = [ "/questions/32744" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Openstreetmap server high availability](/questions/32744/openstreetmap-server-high-availability)

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
<span id="post-32744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32744-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone !</p>
<p>I'd like to build an OpenStreetMap server for my company ...</p>
<p>We want to handle a large area of data (the whole Europe). My question is quite simple, i'd like to know if there is a simple (or not ) way to pre compile tiles for this area in order to fill the /var/lib/mod_tile folder. Once this is done, if i understand well how all this works, that would be much faster to access the tiles for our customers.</p>
<p>Thank you very much for reading and helping. Regards, Guillaume.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-high-speed" rel="tag" title="see questions tagged &#39;high-speed&#39;">high-speed</span> <span class="post-tag tag-link-precompiled" rel="tag" title="see questions tagged &#39;precompiled&#39;">precompiled</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '14, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/8fb68885ff997c74135f182880395f56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guillaume&#39;s gravatar image" />
<p><span>guillaume</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guillaume has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32744" class="comments-container">
&#10;</div>
<div id="comment-tools-32744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32744-form-container" class="comment-form-container">
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

<span id="32751"></span>

<div id="answer-container-32751" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32751-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="guillaume has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pre-rendering tiles is something essentially every provider does, including OSM proper.</p>
<p>It is simply a trade off between disk space used (even just Europe down to zoom level or so, will be rather large) and compute time. Since the low zoom tiles tend to be very explensive to produce it is customary to pre-render tiles down to around zoom 14 regardless of what you do.</p>
<p>Tile disk requirements for a full planet can be found here <a href="http://wiki.openstreetmap.org/wiki/Tile_disk_usage">http://wiki.openstreetmap.org/wiki/Tile_disk_usage</a></p>
<p>If you are using renderd you should already have render_list available that will batch render tiles, see the end of the page of <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '14, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '14, 18:08</strong> </span></p>
</div>
</div>
<div id="comments-container-32751" class="comments-container">
&#10;</div>
<div id="comment-tools-32751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32751-form-container" class="comment-form-container">
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

