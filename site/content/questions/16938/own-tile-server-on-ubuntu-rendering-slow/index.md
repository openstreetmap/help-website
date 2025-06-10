+++
type = "question"
title = "Own tile server on Ubuntu rendering slow"
description = '''Hi all I have set up my own local OSM server according to http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages on my Kubuntu 12.04 system. It works great, how ever I am a bit disappointed about the rendering speed. Even when I use it on the same PC, the tiles are rendered and loa...'''
date = "2012-10-16T18:30:00Z"
lastmod = "2012-10-18T16:37:00Z"
weight = 16938
keywords = [ "slow", "workload", "renderd", "bottleneck" ]
aliases = [ "/questions/16938" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Own tile server on Ubuntu rendering slow](/questions/16938/own-tile-server-on-ubuntu-rendering-slow)

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
<span id="post-16938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16938-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I have set up my own local OSM server according to <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages</a> on my Kubuntu 12.04 system. It works great, how ever I am a bit disappointed about the rendering speed. Even when I use it on the same PC, the tiles are rendered and loaded in the browser quite slow.</p>
<p>I would like to figure out where the boddle neck is. None of the CPU cores (4 cores, Intel Core i5 2500K) is at 100%. Also the RAM (4 GB) is not at its limit. I use a SSD as hard drive for the system and tile store.</p>
<p>Once the tiles are rendered and served from the cache, it is as fast as I would expect it to be normally.</p>
<p>How can I see the work load of the apache2, renderd or postgresql service? I could not find any usful log file in /var/log/.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-workload" rel="tag" title="see questions tagged &#39;workload&#39;">workload</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-bottleneck" rel="tag" title="see questions tagged &#39;bottleneck&#39;">bottleneck</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '12, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/adad2c3132557e364d57c8fc746dd89d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CaCO3&#39;s gravatar image" />
<p><span>CaCO3</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CaCO3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16938" class="comments-container">
&#10;</div>
<div id="comment-tools-16938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16938-form-container" class="comment-form-container">
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

<span id="16943"></span>

<div id="answer-container-16943" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16943-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most likely the bottleneck is the database. There's a PostgreSQL config option called <code>log_min_statement</code> that you can use to log all database statements taking longer than a given amount of time, then investigate. You'll either find that each tile makes a lot of slow queries (which would point to general database slowness), or you might find that one specific query is always the culprit (in that case, creating a specific index might help).</p>
<p>Yo <em>do</em> have the database on the SSD, right?</p>
<p>It is absolutely normal for tiles on the lower zoom levels, up to z13 or z14, to take longer than the user is prepared to wait; that's why these are usually rendered in advance (a.k.a. "seeding" of the tile cache).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '12, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16943" class="comments-container">
<span id="16953"></span>
<div id="comment-16953" class="comment">
<div id="post-16953-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for your quick reply.</p>
<p>My database is on the SSD (my whole system is on it). My main usage will be on zoom level 18, so prerendering is not an option. I will have a look on the postgreSQL config. Since I am not planing to update the database frequently, I dropped the --slim parameter on the osm2postgreSQL import. Also I increased the memory. How ever I understand this is only the memory limit during the import. My command was: osm2pgsql -C 2500 Switzerland.osm.pbf</p>
<p>Over all, I would expect that my server is rendering and serving faster than the public osm server, since my server has enough resources for one country and I am the only user on it.</p>
</div>
<div id="comment-16953-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 08:26)</span> <span class="comment-user userinfo">CaCO3</span>
</div>
</div>
<span id="16955"></span>
<div id="comment-16955" class="comment">
<div id="post-16955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd check the postgresql performance too.</p>
<p>But before that, one all-round tool you can use is <code>atop</code> (not <code>top</code>), which tells you about disk utilisation, displays more correct memory usage, and fully tracks processes instead of showing periodic snapshots.</p>
</div>
<div id="comment-16955-info" class="comment-info">
<span class="comment-age">(17 Oct '12, 10:17)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="16998"></span>
<div id="comment-16998" class="comment">
<div id="post-16998-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Probably not the issue here, but make sure that you have set the planet-import-complete file. Otherwise mod_tile will try and re-render everything every 3 days, which is unnecessary if you don't update your database.</p>
<p>Otherwise, can you say how slow slow is? Seconds? 10s of seconds or minutes? At which zoom level? Rendering Z18 tiles of a Switzerland only db should probably take &lt; 3 seconds in most cases.</p>
</div>
<div id="comment-16998-info" class="comment-info">
<span class="comment-age">(18 Oct '12, 16:37)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-16943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16943-form-container" class="comment-form-container">
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

