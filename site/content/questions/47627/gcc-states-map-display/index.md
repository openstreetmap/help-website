+++
type = "question"
title = "gcc states map display"
description = '''Hi, I have set up local OSM server using OSM2pgsql. I have extracted India map data and it is looking okay. But, when I extracted gcc states pbf file from Geofabrik website and extracted it, map is not showing that data. Gcc states data is not visible on map.'''
date = "2016-01-22T10:20:00Z"
lastmod = "2016-01-27T06:41:00Z"
weight = 47627
keywords = [ "gcc" ]
aliases = [ "/questions/47627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [gcc states map display](/questions/47627/gcc-states-map-display)

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
<span id="post-47627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47627-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-47627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have set up local OSM server using OSM2pgsql. I have extracted India map data and it is looking okay. But, when I extracted gcc states pbf file from Geofabrik website and extracted it, map is not showing that data. Gcc states data is not visible on map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gcc" rel="tag" title="see questions tagged &#39;gcc&#39;">gcc</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '16, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47627" class="comments-container">
<span id="47628"></span>
<div id="comment-47628" class="comment">
<div id="post-47628-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please explain what you did to add the GCC states data to your already existing map. What programs did you run and with what arguments?</p>
</div>
<div id="comment-47628-info" class="comment-info">
<span class="comment-age">(22 Jan '16, 10:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="47629"></span>
<div id="comment-47629" class="comment">
<div id="post-47629-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>sudo -u www-data osm2pgsql -C 2048 --slim --number-processes 4 gcc-states-latest.osm.pbf --cache-strategy sparse</p>
</div>
<div id="comment-47629-info" class="comment-info">
<span class="comment-age">(22 Jan '16, 10:52)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47630"></span>
<div id="comment-47630" class="comment">
<div id="post-47630-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This has deleted your India data from the database, and loaded the gcc-states data instead of it. Is that what you wanted? Are you running a tile server with renderd? Are you seeing "pink tiles" on your map, or just empty tiles with oceans and nothing else?</p>
</div>
<div id="comment-47630-info" class="comment-info">
<span class="comment-age">(22 Jan '16, 16:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="47631"></span>
<div id="comment-47631" class="comment">
<div id="post-47631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Additionally, I suspect that "Gcc states data is not visible on map" means that previously generated tiles are being cached somewhere, perhaps even in the browser.</p>
<p>In summary, a bit more information about which commands are being run in what order (and what was visible at each stage) would be needed to provide much more help. Maybe an option would be to ask in the #osm IRC channel - that we people could ask questions a bit more interactively?</p>
</div>
<div id="comment-47631-info" class="comment-info">
<span class="comment-age">(22 Jan '16, 16:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47661"></span>
<div id="comment-47661" class="comment">
<div id="post-47661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I executed following commands in given sequence.</p>
<ol>
<li>Map server was setup and India and Gcc states data was imported. Both the maps were visible. 2.Then for importing latest India map data, following command was executed. After this command, latest India map was visible but Gcc states map was not visible.</li>
</ol>
<p>sudo -u www-data osm2pgsql -C 2048 --slim --number-processes 4 India-latest.osm.pbf --cache-strategy sparse</p>
<ol>
<li>For Gcc states, following command was executed. But it did not change anything. India map is still visible and Gcc states are still not visible.</li>
</ol>
<p>sudo -u www-data osm2pgsql -C 2048 --slim --number-processes 4 gcc-states-latest.osm.pbf --cache-strategy sparse</p>
<p>Also, Gcc map is available in higher zoom levels. It is not visible for lower zoom levels.</p>
</div>
<div id="comment-47661-info" class="comment-info">
<span class="comment-age">(27 Jan '16, 06:41)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-47627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

