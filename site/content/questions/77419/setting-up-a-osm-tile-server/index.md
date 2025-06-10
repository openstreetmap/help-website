+++
type = "question"
title = "Setting up a OSM Tile Server?"
description = '''Hi, I need to set up an OSM Tile Server for my organization for the entire planet data. Can anyone guide me on the ideal hardware configuration required and also the time that would take up for a full planet load? Also are there any specific PostgreSQL DB configuration tweaks that need to be done in...'''
date = "2020-11-06T11:54:00Z"
lastmod = "2020-11-06T12:43:00Z"
weight = 77419
keywords = [ "tileserversetup" ]
aliases = [ "/questions/77419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Setting up a OSM Tile Server?](/questions/77419/setting-up-a-osm-tile-server)

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
<span id="post-77419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to set up an OSM Tile Server for my organization for the entire planet data. Can anyone guide me on the ideal hardware configuration required and also the time that would take up for a full planet load? Also are there any specific PostgreSQL DB configuration tweaks that need to be done in order to improve the tile server performance?</p>
<p>Thanks in advance for your help.</p>
<p>Thanks, Christopher</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserversetup" rel="tag" title="see questions tagged &#39;tileserversetup&#39;">tileserversetup</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '20, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0479ea402bfffeb70236946603798443?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jchrisprabu&#39;s gravatar image" />
<p><span>jchrisprabu</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jchrisprabu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77419" class="comments-container">
&#10;</div>
<div id="comment-tools-77419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77419-form-container" class="comment-form-container">
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

<span id="77420"></span>

<div id="answer-container-77420" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77420-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Get a machine with about 1.5 TB of fast NVMe storage and then about ~300 GB extra storage for operating system and tile cache, which may or may not be on the NVMe as well. Depending on your budget and what provider you're using, you could choose a setup with 2x1TB NVMe arranged in an LVM stripe or RAID0 and put the database one that, and then choose standard disks for OS and tile cache. Get 64 GB of RAM and at least 4 CPU cores. With a setup like that, initial import should take between 12 and 24 hours.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '20, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77420" class="comments-container">
<span id="77421"></span>
<div id="comment-77421" class="comment">
<div id="post-77421-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik. Is there any specific postgressql configuration that needs to be tweaked to make it import within this time range? Also the osm2pgsql tool needs to be run as flatnodes or slim mode? Any specific cache configuration that needs to be specified while running this tool.</p>
</div>
<div id="comment-77421-info" class="comment-info">
<span class="comment-age">(06 Nov '20, 12:43)</span> <span class="comment-user userinfo">jchrisprabu</span>
</div>
</div>
</div>
<div id="comment-tools-77420" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77420-form-container" class="comment-form-container">
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

