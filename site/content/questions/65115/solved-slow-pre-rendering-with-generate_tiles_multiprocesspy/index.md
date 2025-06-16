+++
type = "question"
title = "SOLVED: Slow pre-rendering with generate_tiles_multiprocess.py"
description = '''Hi Using Mapnik 2.2, and the same recipy for installing PostGis, Mapnik and osm2pgsql as used by Koles500. Earlier I imported europe-latest.osm.pbf to database. The import was done in: 155324s, an import time I&#x27;m quite happy with considering that I only had 12GB of ram on my computer while importing...'''
date = "2018-08-03T19:39:00Z"
lastmod = "2018-08-08T10:24:00Z"
weight = 65115
keywords = [ "generate_tiles", "slow", "performance" ]
aliases = [ "/questions/65115" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SOLVED: Slow pre-rendering with generate_tiles_multiprocess.py](/questions/65115/solved-slow-pre-rendering-with-generate_tiles_multiprocesspy)

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
<span id="post-65115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>Using Mapnik 2.2, and the same recipy for installing PostGis, Mapnik and osm2pgsql as used by Koles500.</p>
<p>Earlier I imported europe-latest.osm.pbf to database. The import was done in: 155324s, an import time I'm quite happy with considering that I only had 12GB of ram on my computer while importing.</p>
<p>Yesterday I startet to pre-generate tiles from a portion of the europe area as set by this bounding box: <a href="http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=3.98,57.69,32.23,71.46">http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=3.98,57.69,32.23,71.46</a></p>
<p>Now generate_tiles_multiprocess.py has only generated 275 tiles in 18 hours and 15 minutes. I have set generate_tiles_multiprocess.py to use 4 threads:</p>
<pre><code>NUM_THREADS = 4</code></pre>
<p>as well as specifying this at the end:</p>
<pre><code>minZoom = 1
maxZoom = 11
bbox = (3.98,57.69,32.23,71.46)
render_tiles(bbox, mapfile, tile_dir, minZoom, maxZoom, &quot;Norway&quot;)</code></pre>
<p>I can see that the four CPU cores has a load usage of approximately 10 - 30%, most of the times it is about 20%. More than 10GB of memory is not in use.</p>
<p>I do not understand why tile pre-rendering is so slow.</p>
<p>But I do remember that I forgot to remove -l from the options when importing data to the database using osm2pgsql: I used this:</p>
<pre><code>osm2pgsql -s -U postgres -C 8000 --number-processes 4 -l -m -d osm -p planet_osm -E 3857 -S &quot;N:\osm2pgsql\default.style&quot;  T:\planet-osm-2018-07-28\europe-latest.osm.pbf</code></pre>
<p>Can that -l option (--latlng) when importing data using osm2pgsql - cause Mapnik to use extra long time to generate the tiles? If that option is the cause - can I fix this without having to import whole pbf file from Europe again? If it's not the cause, what could be the reason for the extremely slow tile generation?</p>
<p>Computer now with a little bit more ram:</p>
<ul>
<li>The whole DB on an SSD</li>
<li>Tiledir on a 10000 RPM disk (SATA 2).</li>
<li>3.2 Ghz CPU with 4 cores.</li>
<li>20 GB RAM (5 x 4 GB)</li>
<li>Windows 7</li>
</ul>
<p>Compared to the specifications on the computer Koles500 uses, I simply do not understand the extreme slowness of pre-rendering time. The few tiles that have been pre-rendered are looking perfect.</p>
<p>If someone has tips on how to improve pre-rendering time (using Mapnik 2.2), please let me know. Waiting more than 100 days for the 41 000 tiles to pre-render is just to long.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '18, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0da1f043b943c87172fb4dc60f017440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MapViking&#39;s gravatar image" />
<p><span>MapViking</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MapViking has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '18, 11:46</strong> </span></p>
</div>
</div>
<div id="comments-container-65115" class="comments-container">
<span id="65127"></span>
<div id="comment-65127" class="comment">
<div id="post-65127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Converted from an answer to a question from <a href="/questions/54560/slow-generation-of-tiles-for-whole-europe">https://help.openstreetmap.org/questions/54560/slow-generation-of-tiles-for-whole-europe</a></p>
</div>
<div id="comment-65127-info" class="comment-info">
<span class="comment-age">(04 Aug '18, 08:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65115-form-container" class="comment-form-container">
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

<span id="65136"></span>

<div id="answer-container-65136" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65136-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Obviously this is difficult to answer without access to the machine, but</p>
<ul>
<li>some low zoom tiles are slow to process (because the tiles will cover a lot of data, particularly in parts of Europe), you don't mention which style you are using, it depends on that naturally too.</li>
<li>using the -l option (essentially that means you have the original OSM WGS84 coordinates in your DB) implies that mapnik needs to reproject all the data to web-mercator for rendering (at least for the OSM standard style), this will definitely have a performance impact, but would have to be quantified by benchmarking the two variants. In any case you could try using PostGIS to reproject all the geometry objects in the DB, but I suspect that re-importing is going to be less work.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '18, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-65136" class="comments-container">
<span id="65150"></span>
<div id="comment-65150" class="comment">
<div id="post-65150-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for answer. I'm using the osm.xml file which comes with mapnik 2.2, only with minor changes to some colors for water and wood. With the current db data, 4 tiles are generated every 22 minutes (approximately). All 4 tiles are generated within a second. Then 22 minutes to next 4 tiles, and so on.</p>
<p>So I imported iceland-latest.osm.pbf into database without the -l option. Used the same stylesheet but with the bbox for iceland (instead of Norway). Then I got 4006 tiles generated in 2 minutes and 40 seconds. Which is good for me.</p>
<p>So pre-rendering obviously works fast with one small country (hopefully because I imported without the -l option).</p>
<p>Currently I'm importing whole europe again - without using the -l option. I'll come back laiter today or tomorrow and tell if the pre-rendering is faster with the new imported db-data.</p>
<p>I have also read about the maximum-extent parameter for the map tag in the xml file. So with the whole europe imported: If I want to pre-render tiles for Iceland only - do I have to set both the extent (in the layer datasource) and the maximum-extent in the map tag, in addition to using bbox in generate_tiles_multiprocess.py?</p>
</div>
<div id="comment-65150-info" class="comment-info">
<span class="comment-age">(06 Aug '18, 10:26)</span> <span class="comment-user userinfo">MapViking</span>
</div>
</div>
</div>
<div id="comment-tools-65136" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65136-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65211"></span>

<div id="answer-container-65211" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65211-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Update. It is now working very good. Imported europe-latest.osm.pbf from geofabrik once more, this time without the -l flag.</p>
<p>Tiles are now pre-rendering pretty fast.</p>
<p>This comment has been changed, since I previously reported that it did not work. By some reason the xml file I used when rendering tiles for iceland did not work. But when I tried the xml file for norway, sweden and finland - it all worked very good.</p>
<p>Thanks for input on removing that -l option for osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '18, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0da1f043b943c87172fb4dc60f017440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MapViking&#39;s gravatar image" />
<p><span>MapViking</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MapViking has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '18, 11:47</strong> </span></p>
</div>
</div>
<div id="comments-container-65211" class="comments-container">
&#10;</div>
<div id="comment-tools-65211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65211-form-container" class="comment-form-container">
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

