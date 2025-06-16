+++
type = "question"
title = "OSM Tile Server Provisioning"
description = '''We are looking to roll our own OSM server, and are currently trying to lay down some basic server requirements in terms of disk space and bandwidth usage. According to the OSM wiki, the full tile-set without pre-rendering is on the order of ~1.7TB. Looking at network stats for a number of the tile s...'''
date = "2013-01-28T16:15:00Z"
lastmod = "2013-01-28T17:22:00Z"
weight = 19401
keywords = [ "bandwidth", "osm" ]
aliases = [ "/questions/19401" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM Tile Server Provisioning](/questions/19401/osm-tile-server-provisioning)

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
<span id="post-19401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19401-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are looking to roll our own OSM server, and are currently trying to lay down some basic server requirements in terms of disk space and bandwidth usage.</p>
<p>According to the OSM wiki, the full tile-set without pre-rendering is on the order of <a href="https://wiki.openstreetmap.org/wiki/Tile_Disk_Usage">~1.7TB</a>.</p>
<p>Looking at network <a href="https://wiki.openstreetmap.org/wiki/Stats">stats</a> for a number of the tile servers, <a href="http://munin.openstreetmap.org/openstreetmap/www.openstreetmap/index.html">specifically the www.openstreetmap.org server</a>, I am getting the following breakdown from the weekly charts:</p>
<pre><code>Apache Accesses/sec = ~105k
Apache Data/sec = ~625kb</code></pre>
<p>So on average, each data access generates ~6.25 b/s. Per day, that works out to 540k bytes/user - seems low though as each map tile is ~30k and just the default map with the settings they use is going to be ~15 tiles... and then they are going to be zooming, panning, etc.</p>
<p>Am I reading these numbers correctly? Can anyone who has rolled their own OSM server confirm these are a good estimate?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '13, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/fc25d878d34c4d6c0c7b28c756b2cec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Mennega&#39;s gravatar image" />
<p><span>Paul Mennega</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Mennega has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '13, 16:58</strong> </span></p>
</div>
</div>
<div id="comments-container-19401" class="comments-container">
<span id="19402"></span>
<div id="comment-19402" class="comment">
<div id="post-19402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It isn't clear which ressource you are trying to estimate. Disk space ? Total bandwidth ? Bandwidth per user ? Number of connections ?</p>
</div>
<div id="comment-19402-info" class="comment-info">
<span class="comment-age">(28 Jan '13, 16:30)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="19403"></span>
<div id="comment-19403" class="comment">
<div id="post-19403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bandwidth/user - we have estimates for the number of users we will have, but trying to figure out how much a typical OSM end-user consumes, thus my calcs above on bytes per user per day.</p>
</div>
<div id="comment-19403-info" class="comment-info">
<span class="comment-age">(28 Jan '13, 16:34)</span> <span class="comment-user userinfo">Paul Mennega</span>
</div>
</div>
<span id="19406"></span>
<div id="comment-19406" class="comment">
<div id="post-19406-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@apmon</span> Thanks! Understood on the sheer volume, thus why i am trying to break it down to bandwidth per user. This clarification helps though!</p>
</div>
<div id="comment-19406-info" class="comment-info">
<span class="comment-age">(28 Jan '13, 17:22)</span> <span class="comment-user userinfo">Paul Mennega</span>
</div>
</div>
</div>
<div id="comment-tools-19401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19401-form-container" class="comment-form-container">
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

<span id="19405"></span>

<div id="answer-container-19405" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19405-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Paul Mennega has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are looking at the wrong stats if you want a tile server. Those stats are just for the website without the tiles.</p>
<p>The OSM tileserver is behind a set of 5 reverse proxy servers as a cdn. The stats for the aggregate are at <a href="http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/index.html">http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/index.html</a> The stats for the actual backend tile server are at <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html</a> But there is a good chance you won't see anything like the traffic on osm.org. A usefull resource is also <a href="https://wiki.openstreetmap.org/wiki/Tile_Disk_Usage">https://wiki.openstreetmap.org/wiki/Tile_Disk_Usage</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '13, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19405" class="comments-container">
&#10;</div>
<div id="comment-tools-19405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19405-form-container" class="comment-form-container">
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

