+++
type = "question"
title = "Slow rendering with base OSM-Bright style"
description = '''Hi, I&#x27;ve installed my own tileserver and imported the whole France to test (the goal being to serve the entire planet). But the rendering is VERY VERY slow, like even for zoom 12 tiles it takes sometimes over than one minute to render (and I&#x27;m the only one on the server, so one minute to render a fe...'''
date = "2018-08-07T10:49:00Z"
lastmod = "2018-10-02T13:40:00Z"
weight = 65179
keywords = [ "slow", "postgresql", "switch2osm", "tileserver" ]
aliases = [ "/questions/65179" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Slow rendering with base OSM-Bright style](/questions/65179/slow-rendering-with-base-osm-bright-style)

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
<span id="post-65179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65179-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've installed my own tileserver and imported the whole France to test (the goal being to serve the entire planet). But the rendering is VERY VERY slow, like even for zoom 12 tiles it takes sometimes over than one minute to render (and I'm the only one on the server, so one minute to render a few zoom 12 tiles, it is really slow). I really don't know why it takes so long, I've followed the instructions on switch2osm, the only difference being that I choosed to use the OSM-Bright theme, customized for my needs. But to be sure it wasn't my custom style which impacted the perfs, I've also tried with the original OSM-Bright and it is the same rendering time.</p>
<p>Here is my configuration:</p>
<ul>
<li>Intel Xeon E3-1245v2 (4c / 8t - 3,4GHz)</li>
<li>32GB DDR3 1333MHz</li>
<li>SSD</li>
<li>apache/mod_tile/postgresql running in docker container</li>
</ul>
<p>I've imported the data with this osm2pgsql command:</p>
<pre><code>osm2pgsql -d gis --create --slim -G --hstore --hstore-match-only -C 4000 --number-processes 8 -S custom.style --flat-nodes /path/to/flat_nodes.bin data.osm.pbf</code></pre>
<p>But I've also tried without my custom style and without flat-nodes, it doesn't make any relevant difference. While monitoring the server process and ram usage, I've noticed that it was postgresql and not renderd which was taking a long time, and using all process cores at there maximum (which make sense because from what I understood, the postgresql queries are the slowest part of the process).</p>
<p>Following the <a href="http://www.paulnorman.ca/blog/2016/08/sampling-slow-postgres-queries/">small tutorial</a> of Paul Norman, I've logged theses queries, returning over and over (the log file is almost only composed of queries like theses ones):</p>
<pre><code>SELECT ST_XMin(ext),ST_YMin(ext),ST_XMax(ext),ST_YMax(ext) FROM (SELECT ST_Extent(way) as ext from planet_osm_polygon) as tmp
SELECT ST_XMin(ext),ST_YMin(ext),ST_XMax(ext),ST_YMax(ext) FROM (SELECT ST_Extent(way) as ext from planet_osm_line) as tmp</code></pre>
<p>With an average time of 1/2secs by queries, so it's probably what slows down the process.</p>
<p>For the record, I haven't enable update yet, so the only queries running are the ones I use for testing rendering. Also, I've tried multiple postgresql confs (following again Paul Newman and Frederik Ramm recommandations), but haven't noticed any big improvment (the time being actually around 1 minute for a zoom 12, I expect it to be closer to a second at this level, am I wrong?).</p>
<p>For higher zoom levels, it become faster (but still a bit slow I think):</p>
<ul>
<li>z16 : 1.5s</li>
<li>z15 : 2.7s</li>
<li>z14 : 6.2s</li>
</ul>
<p>Does anybody have any idea of why even with the basic OSM-Bright style and this specs I'm facing this very slow rendering time? It doesn't make any sense to me...</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '18, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '18, 11:08</strong> </span></p>
</div>
</div>
<div id="comments-container-65179" class="comments-container">
<span id="65183"></span>
<div id="comment-65183" class="comment">
<div id="post-65183-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just a couple of thoughts:</p>
<p>1) I'd pre-render tiles to zoom 12 so that the time to do those isn't an issue that users notice.</p>
<p>2) Are you using Docker for a particular reason? Surely any unnecessary redirection will slow things down?</p>
</div>
<div id="comment-65183-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 11:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65185"></span>
<div id="comment-65185" class="comment">
<div id="post-65185-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer.</p>
<p>1) Yes I intend to, but still it seems to me that this rendering tile is really high, even on higher zooms (I've edited my question), the rendering tile can be problematic, ~6 seconds for a zoom 14 tile seems too much...</p>
<p>2) The original reason was to be able to deploy easily (in dev or prod) and to facilitate an eventual use of multiples servers. I'm just starting with Docker, so I don't know all the inconveniants but from what I understand, unlike a virtual machine, the process are actually runned on the host machine, so it may slow down things a bit but not that much I think...</p>
</div>
<div id="comment-65185-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 11:24)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-65179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65179-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="65184"></span>

<div id="answer-container-65184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Lower zoom tiles tend to be slower as there is much more data per tile / meta-tile to retrieve (from the database) and render (this is naturally offset by zoom dependent style changes), think a factor of 4 per zoom level. It is normal to pre-render at least to level 12 for this reason as SomeoneElse has already pointed out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '18, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65184" class="comments-container">
<span id="65186"></span>
<div id="comment-65186" class="comment">
<div id="post-65186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. Yes I know that and as I just sayed to SomeoneElse, we intend to pre-render those tiles. So for you, more than one minute at zoom 12 is normal? I don't know much about rendering so maybe I panic for no reason... I've added some rendering times for higher zooms, it's way faster but still not acceptable for a production server...</p>
</div>
<div id="comment-65186-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 11:28)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-65184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65191"></span>

<div id="answer-container-65191" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65191-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>SELECT ST_XMin</code>... queries should only happen when the renderd worker process starts up, not for every tile. Can you look into that a little more - is there maybe an issue with your setup that causes renderd children to exit after rendering one tile so that you get loads of these queries?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '18, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-65191" class="comments-container">
<span id="65193"></span>
<div id="comment-65193" class="comment">
<div id="post-65193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot Frederik, I didn't know that, but it make sense because when a launch render_list, it seems to process way faster than from an apache request, probably because the process isn't killed with that. It may be linked to my docker installation, I'll investigate on this.</p>
</div>
<div id="comment-65193-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 13:50)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="65196"></span>
<div id="comment-65196" class="comment">
<div id="post-65196-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where should I look to see if the children are killed? Or even when it is fully started? I'm watchning the process list with htop but I can't see any new child process related to renderd, I see some postgres children spawning but that's it.</p>
<p>However I've noticed something strange, after some queries, it become faster (still slow but optimizable slow, like 15 seconds for a zoom 12 tile which is way better than the previous time) and I don't see the SELECT ST_XMin queries anymore... Looks like it's random to me, I've reproduced that twice but it didn't append at the same amount of queries/time...</p>
</div>
<div id="comment-65196-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 14:54)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="65212"></span>
<div id="comment-65212" class="comment">
<div id="post-65212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well the problem is really only for the first tiles, so it may be normal I don't know... You said that these queries should only happen at renderd startup but how long does this startup takes? Because I see in renderd log that it is started like 2/3 seconds after I launched it. It takes a very long time (and log the above psql requests, but only when I request some tiles, it does not launch the requests alone at startup) only for the first tiles rendered, but I can't see any logic here... Sometimes it's the first 20, sometimes more (in time, it can take more than 10 minutes of manual requests). But anyway, after a certain number, these requests stops and it starts to be fast...</p>
<p>Not really a big issue if this is just at the server startup, but still, is this the normal behavior? Thanks.</p>
</div>
<div id="comment-65212-info" class="comment-info">
<span class="comment-age">(08 Aug '18, 10:37)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="65466"></span>
<div id="comment-65466" class="comment">
<div id="post-65466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you find a solution in the end? Did you just need to wait? If so, how much time? And what rendering speed did you get? Thanks</p>
</div>
<div id="comment-65466-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 16:34)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
</div>
<div id="comment-tools-65191" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65191-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66127"></span>

<div id="answer-container-66127" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66127-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've successfully imported the whole planet but now I'm still having the slow rendering issue. I'm just trying to load one tile after the server just started, and I'm seeing the requests Frederik told me before that it was normal at the renderd start:</p>
<pre><code>SELECT ST_XMin(ext),ST_YMin(ext),ST_XMax(ext),ST_YMax(ext) FROM (SELECT ST_Extent(way) as ext from planet_osm_polygon) as tmp</code></pre>
<p>This one * 5 when I'm looking in <code>pg_stat_activity</code>. And it seems to never go further, I've checked 20 minutes after and there was the sames queries (and only these), but with a more recent query_start and a different pid, to it's like the queries ended, and were restarted... But I really don't understand why, or even what they're supposed to do.</p>
<p>In the renderd logs, I see that when the rendering start:</p>
<pre><code>renderd[21]: DEBUG: Got incoming connection, fd 6, number 1
renderd[21]: DEBUG: Got incoming request with protocol version 2
renderd[21]: DEBUG: Got command RenderPrio fd(6) xml(fr), z(10), x(530), y(367), mime(image/png), options()
renderd[21]: DEBUG: START TILE fr 10 528-535 360-367, new metatile
renderd[21]: Rendering projected coordinates 10 528 360 -&gt; 626172.135713|5635549.221413 939258.203569|5948635.289269 to a 8 x 8 tile
renderd[21]: DEBUG: Connection 0, fd 6 closed, now 0 left</code></pre>
<p>But after that, nothing. Nothing in the postgresql logs either.</p>
<p>Does somebody have an idea of what could cause that?</p>
<p>Thanks!</p>
<p><strong>EDIT:</strong> After almost an hour (yeaaah) the tile was done:</p>
<pre><code>renderd[21]: DEBUG: DONE TILE fr 10 528-535 360-367 in 3193.842 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/fr/10/0/0/33/22/8.meta</code></pre>
<p>But then I started another (random) tile at zoom 16, which should be fast... It was a few minutes ago, I'm still waiting... And I'm still seeing the same requests in <code>pg_stat_activity</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '18, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Oct '18, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-66127" class="comments-container">
&#10;</div>
<div id="comment-tools-66127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66127-form-container" class="comment-form-container">
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

