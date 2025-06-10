+++
type = "question"
title = "Slow generation of tiles for whole Europe"
description = '''Hi! I am using generate_tiles.py script to generate tiles but it is taking awfully long time for whole Europe. It was generating tiles really fast for just one town, but whole Europe seems to be taking forever. Basicaly I followed this tutorial:  http://openstreetmapserverwindows.blogspot.ie/2015/11...'''
date = "2017-02-08T23:05:00Z"
lastmod = "2017-02-09T13:58:00Z"
weight = 54560
keywords = [ "windows", "generate_tiles", "slow", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/54560" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Slow generation of tiles for whole Europe](/questions/54560/slow-generation-of-tiles-for-whole-europe)

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
<span id="post-54560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54560-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I am using generate_tiles.py script to generate tiles but it is taking awfully long time for whole Europe. It was generating tiles really fast for just one town, but whole Europe seems to be taking forever. Basicaly I followed this tutorial: <a href="http://openstreetmapserverwindows.blogspot.ie/2015/11/osmopenstreetmap-tile-server.html">http://openstreetmapserverwindows.blogspot.ie/2015/11/osmopenstreetmap-tile-server.html</a> to set up everything on Windows Server 2012 64-bit and we made it. Importing whole Europe from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> took 15 days (wow!) probably because we have HDD instead of SSD disk on our server. Our processor is Xenon 3.5 GHz and 32 GB RAM. I started generate_tiles.py 10 minutes ago for zoom level (3-16) 10 minutes ago and I got <em>only</em> 135 tiles so far ;-( (it is processing zoom level 6 now...). This is terribly slooow. How can we speed up this process so that we get all tiles for zoom level (3-16) in at least 1 month? :-) This is serious question.</p>
<p>Looking in Windows "Resource Monitor" I see 4 postgres.exe processes reading data with average speed between ~ 500 and ~ 2500 B/s - isn't this terribly slow ? Maybe we should tweak Postgres to speed it up ?</p>
<p>I can provide further technical details and settings I used in files if needed. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '17, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '17, 23:10</strong> </span></p>
</div>
</div>
<div id="comments-container-54560" class="comments-container">
&#10;</div>
<div id="comment-tools-54560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54560-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="54561"></span>

<div id="answer-container-54561" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54561-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The style your using should provide recommendations for partial indexes. Beyond that, general PostgreSQL tuning is applicable, mainly work_mem. <a href="https://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf">https://www.geofabrik.de/media/2012-09-08-osm2pgsql-performance.pdf</a> has some recommendations, but mainly as they apply to importing, and for an older PostgreSQL version.</p>
<p>Most styles are slowest per tile at low zooms, particularly zoom 6-9.</p>
<p>If you are using <a href="https://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py">https://svn.openstreetmap.org/applications/rendering/mapnik/generate_tiles.py</a> you need to adjust the default NUM_THREADS to reflect your CPU. Unfortunately, generate_tiles.py generates tiles one by one instead of rendering a larger area and cutting the image to size like mod_tile. This probably makes it 4 to 16 times slower than mod_tile.</p>
<p>Pre-rendering to zoom 16 isn't practical with most styles. The OSMF rendering servers pre-render to zoom 12, and this takes about a day. Each zoom has 4x the number of tiles, so you're looking at about 300x as many tiles as zoom 12.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '17, 00:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54561" class="comments-container">
&#10;</div>
<div id="comment-tools-54561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54561-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54568"></span>

<div id="answer-container-54568" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, nevermind. I noticed there is generate_tiles_multiprocess.py script , I changed NUM_THREADS to 8 and used and it generated half million tiles over the night already :-) It is processing zoom level 12 now, so I think it should be done over next few days.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '17, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54568" class="comments-container">
&#10;</div>
<div id="comment-tools-54568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54568-form-container" class="comment-form-container">
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

