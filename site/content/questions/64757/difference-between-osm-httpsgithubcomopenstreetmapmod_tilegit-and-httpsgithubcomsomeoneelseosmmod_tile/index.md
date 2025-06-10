+++
type = "question"
title = "Difference between osm https://github.com/openstreetmap/mod_tile.git and https://github.com/SomeoneElseOSM/mod_tile"
description = '''I am trying to build a tile server. For implementation, I am going through the steps given in switch2osm and osm-carto-tutorial. I found in switch2osm, they are suggesting to use https://github.com/SomeoneElseOSM/mod_tile whereas osm-carto-tutorial  https://github.com/openstreetmap/mod_tile.git is u...'''
date = "2018-07-17T07:56:00Z"
lastmod = "2018-07-17T14:09:00Z"
weight = 64757
keywords = [ "openstreetmap-carto", "openstreetmap", "switch2osm", "mod_tile" ]
aliases = [ "/questions/64757" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between osm https://github.com/openstreetmap/mod_tile.git and https://github.com/SomeoneElseOSM/mod_tile](/questions/64757/difference-between-osm-httpsgithubcomopenstreetmapmod_tilegit-and-httpsgithubcomsomeoneelseosmmod_tile)

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
<span id="post-64757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64757-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build a tile server. For implementation, I am going through the steps given in <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm</a> and <a href="https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/">osm-carto-tutorial</a>. I found in switch2osm, they are suggesting to use <a href="https://github.com/SomeoneElseOSM/mod_tile">https://github.com/SomeoneElseOSM/mod_tile</a> whereas osm-carto-tutorial <a href="https://github.com/openstreetmap/mod_tile.git">https://github.com/openstreetmap/mod_tile.git</a> is used.</p>
<p>So my question is what are problems I may face if I use openstreetmap mod_tile instead of SomeoneElse's mod_tiles?Or which mod_tile project is recommended?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '18, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64757" class="comments-container">
&#10;</div>
<div id="comment-tools-64757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64757-form-container" class="comment-form-container">
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

<span id="64763"></span>

<div id="answer-container-64763" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64763-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anuranpal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I made the change a couple of switch2osm releases ago. It made no sense to have everyone following the switch2osm "manual" instructions (which are designed to be as simple as possible to follow) all making the same changes to config files. There are 3 active branches of <a href="https://github.com/SomeoneElseOSM/mod_tile">https://github.com/SomeoneElseOSM/mod_tile</a> - <a href="https://github.com/SomeoneElseOSM/mod_tile/tree/master">master</a>, which tracks the parent repository, <a href="https://github.com/SomeoneElseOSM/mod_tile/tree/switch2osm">switch2osm</a>, which incorporates some minor changes to config files to match the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm instructions</a>, and <a href="https://github.com/SomeoneElseOSM/mod_tile/tree/zoom">zoom</a> which incorporates some further changes to support zoom levels up to 24. See <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/39423">this diary entry</a> for details. The paths used in the metatile cache are different in the "zoom" and other branches, so it wouldn't be possible to make that a "switch2osm standard" without everyone deleting their tile caches.</p>
<p>As to whether you'd want to follow <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm</a> or <a href="https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/">Ircama's instructions</a>, it's up to you. The switch2osm guides deliberately use packages distributed as part of the OS if possible; Ircama's guide suggests using later versions from elsewhere in some cases. For example, if you want to use Mapnik 3.0.19 on Ubuntu 16.04 Ircama's guide explains how but switch2osm doesn't, in the interests of keeping it simple for people who have not set up a tile server before. If you're installing on Ubuntu 18.04 I think you'll actually end up in pretty much the same place whichever set of instructions you follow. One possible diffeence is that the tile expiry scripts in the switch2osm version work out of the box; the parent ones may not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '18, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '18, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-64763" class="comments-container">
&#10;</div>
<div id="comment-tools-64763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64763-form-container" class="comment-form-container">
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

