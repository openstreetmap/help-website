+++
type = "question"
title = "Slow tile rendering and stuck render_list"
description = '''Hi all, my first post here.  I installed a tile server following this https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ and managed to get it work ... sort of. I installed leaflet on top of that, and something indeed happens - eventually. When I go to a new location on the map or a...'''
date = "2018-02-05T14:35:00Z"
lastmod = "2018-11-29T11:13:00Z"
weight = 61962
keywords = [ "tileserver" ]
aliases = [ "/questions/61962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow tile rendering and stuck render_list](/questions/61962/slow-tile-rendering-and-stuck-render_list)

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
<span id="post-61962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61962-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, my first post here.</p>
<p>I installed a tile server following this <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> and managed to get it work ... sort of. I installed leaflet on top of that, and something indeed happens - eventually. When I go to a new location on the map or a new zoom level, I get an empty screen and after 30 seconds (timeout set in apache conf) 404 errors (GET /hot/3/1/3.png HTTP/1.1" 404 503 "http://10.0.0.126/map.html") and so on. (map of the whole world imported).</p>
<p>When I do a refresh later or move elsewhere and come back, the tiles are there. I am not too familiar with any of this but my diagnosis is that rendering of tiles just takes "too long". This is unlikely to be a hardware issue as I commandeered an unused server from a server room rack for this. I have 40 cores, 192GB of memory and 6TB of solid state storage. This is a fresh 16.04 server install with nothing else running on it and everything up to date.</p>
<p>Ok. Rendering of tiles may be slow, and I thought to speed it up by doing a lot of it beforehand as I do not particularly lack resources here. I tried</p>
<pre><code>./render_list -m default -a -z 0 -Z 10 -n 10</code></pre>
<p>but it just hangs. It does not appear to be doing anything. It does not consume any resources whatsoever and it does not cause anything visible in CPU, renderd or postgresql processes. In contrast, when I navigate with my browser to an unvisited area on the map, I can see 6-8 postgresql processes taking 100% of CPU for a while and renderd peaking occasionally as well.</p>
<p>Apparently something is not right, but what exactly and how could I debug this?</p>
<p>EDIT:</p>
<p>This is my renderd.conf:</p>
<pre><code>[renderd]
num_threads=16
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[ajt]
URI=/hot/
TILEDIR=/var/lib/mod_tile
XML=/home/osm/src/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256
MAXZOOM=20</code></pre>
<p>From syslog I can see successful rendering but the lower the zoom level, the more time it takes. The higher zoom level speeds are completely acceptable, it is just zoom levels 3-5 that seem to take forever:</p>
<pre><code>Feb  5 14:54:01 foo renderd[2544]: DEBUG: DONE TILE ajt 8 144-151 96-103 in 17.569 seconds
Feb  5 14:56:30 foo renderd[2544]: DEBUG: DONE TILE ajt 4 8-15 8-15 in 154.711 seconds
Feb  5 14:57:38 foo renderd[2544]: DEBUG: DONE TILE ajt 6 32-39 32-39 in 55.559 seconds
Feb  5 14:57:40 foo renderd[2544]: DEBUG: DONE TILE ajt 5 16-23 16-23 in 64.475 seconds
Feb  5 14:58:04 foo renderd[2544]: DEBUG: DONE TILE ajt 7 64-71 72-79 in 1.414 seconds
Feb  5 14:58:08 foo renderd[2544]: DEBUG: DONE TILE ajt 8 136-143 144-151 in 2.584 seconds
Feb  5 14:58:09 foo renderd[2544]: DEBUG: DONE TILE ajt 10 568-575 592-599 in 1.164 seconds</code></pre>
<p>When I run render_list, I do get a connection reported like this (the only interesting line, no other RenderBulk requests appear):</p>
<pre><code>renderd[2544]: DEBUG: Got command RenderBulk fd(8) xml(default), z(1), x(0), y(0), mime(image/png), options()</code></pre>
<p>but then nothing else happens. No other log entries, and no CPU or disk activity whatsoever (I have waited for about an hour for something to happen).</p>
<p>Restarting renderd does not produce any interesting log messages (debug messages about fonts mainly). The only "odd" part is this (no function name - not sure if it is ok or not).</p>
<pre><code>Feb  5 15:54:54 foo renderd[22643]: Starting stats thread
Feb  5 15:54:54 foo renderd[22643]: Loading parameterization function for
Feb  5 15:54:54 foo renderd[22643]: message repeated 15 times: [ Loading parameterization function for]
Feb  5 15:54:55 foo renderd[22643]: Updating max_connection parameter for mapnik layers to reflect thread count
Feb  5 15:54:57 foo renderd[22643]: message repeated 15 times: [ Updating max_connection parameter for mapnik layers to reflect thread count]
Feb  5 15:54:57 foo renderd[22643]: Using web mercator projection settings
Feb  5 15:54:59 foo renderd[22643]: message repeated 15 times: [ Using web mercator projection settings]</code></pre>
<p><strong>EDIT2</strong></p>
<p>If I run render_list as</p>
<pre><code>./render_list -m default -a -z 1 -Z 4 -n 10</code></pre>
<p>I <em>sometimes</em> seem to be getting log messages:</p>
<pre><code>Feb  5 16:00:20 foo renderd[22643]: DEBUG: Got command RenderBulk fd(12) xml(default), z(4), x(8), y(8), mime(image/png), options()
Feb  5 16:00:20 foo renderd[22643]: No map for: default</code></pre>
<p>But it does not seem to matter from functional perspective if these appear or not.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '18, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/b02dba4479ba90129bd366dac7858959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hv42&#39;s gravatar image" />
<p><span>hv42</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hv42 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '18, 21:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61962" class="comments-container">
<span id="61963"></span>
<div id="comment-61963" class="comment">
<div id="post-61963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and it seems to be only the "wide" zooms causing the problem making the above render_list really useful. If I zoom into an obscure location on the planet, those tiles are server quickly. So I guess my question is how can I find out why render_list does not do anything.</p>
</div>
<div id="comment-61963-info" class="comment-info">
<span class="comment-age">(05 Feb '18, 14:59)</span> <span class="comment-user userinfo">hv42</span>
</div>
</div>
<span id="61964"></span>
<div id="comment-61964" class="comment">
<div id="post-61964-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What messages do you see in /var/log/syslog ? When a request is made to render a tile such as <a href="http://yourserver.example.com/maps/default/0/0/0.png">http://yourserver.example.com/maps/default/0/0/0.png</a> you should see things including lines such as:</p>
<pre><code>Feb  5 14:54:49 yourserver renderd[20130]: DEBUG: START TILE default 0 0-0 0-0, age 45.75 days
Feb  5 14:57:09 yourserver renderd[20130]: DEBUG: DONE TILE default 0 0-0 0-0 in 140.203 seconds</code></pre>
<p>"render_list" just sends a series of requests for tiles, so you should see a series of requests.</p>
<p>What's in your "renderd.conf" file? What happens in syslog in response to "sudo /etc/init.d/render restart"?</p>
</div>
<div id="comment-61964-info" class="comment-info">
<span class="comment-age">(05 Feb '18, 15:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61965"></span>
<div id="comment-61965" class="comment">
<div id="post-61965-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your reply. I have updated the question instead of posting answers here for the sake of readability.</p>
</div>
<div id="comment-61965-info" class="comment-info">
<span class="comment-age">(05 Feb '18, 15:57)</span> <span class="comment-user userinfo">hv42</span>
</div>
</div>
<span id="62780"></span>
<div id="comment-62780" class="comment">
<div id="post-62780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The same problem: render_list does not do anything! No tiles generating.</p>
</div>
<div id="comment-62780-info" class="comment-info">
<span class="comment-age">(22 Mar '18, 14:50)</span> <span class="comment-user userinfo">Michael Holopov</span>
</div>
</div>
<span id="62782"></span>
<div id="comment-62782" class="comment">
<div id="post-62782-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"the lower the zoom level, the more time it takes" - this is expected behavior. That's why low zoom levels on <a href="http://openstreetmap.org/">http://openstreetmap.org/</a> only get updated from time to time.</p>
</div>
<div id="comment-62782-info" class="comment-info">
<span class="comment-age">(22 Mar '18, 15:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62783"></span>
<div id="comment-62783" class="comment not_top_scorer">
<div id="post-62783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14903/michael-holopov">@Michael Holopov</a> - it shouldn't "not do anything"; you should see activity in syslog (see the snippets added to the question). You might have to wait <em>minutes</em> or even longer to see tiles at low zoom level, but that's normal.</p>
</div>
<div id="comment-62783-info" class="comment-info">
<span class="comment-age">(22 Mar '18, 15:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63418"></span>
<div id="comment-63418" class="comment not_top_scorer">
<div id="post-63418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>typically a posgres issue : you have enough memory but did you configured postges to use it ?</p>
</div>
<div id="comment-63418-info" class="comment-info">
<span class="comment-age">(11 May '18, 03:48)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
</div>
<div id="comment-tools-61962" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-61962-form-container" class="comment-form-container">
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

<span id="66985"></span>

<div id="answer-container-66985" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66985-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>map is ajt -m ajt that works</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '18, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/5fc09cc7b1faf82827919ab62dedcb32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andreaswoods&#39;s gravatar image" />
<p><span>andreaswoods</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andreaswoods has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66985" class="comments-container">
<span id="66986"></span>
<div id="comment-66986" class="comment">
<div id="post-66986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The original question was asking about slow tile rendering rather than not working at all - I wonder if the "default" in the original quoted render_list command was a typo, or if "default" actually works if there's only one style defined?</p>
</div>
<div id="comment-66986-info" class="comment-info">
<span class="comment-age">(29 Nov '18, 11:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66985-form-container" class="comment-form-container">
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

