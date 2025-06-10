+++
type = "question"
title = "Tile rendering extremly slow"
description = '''I imported germany and tried to render a tile on 10/535/341. It took like 10 Minutes. Specs:  16gb Ram 8 Cores  I used the openstreetmap carto style and my import command was: osm2pgsql --create --slim --flat-nodes /home/renderer/update_tiles/flat-nodes.raw --hstore -C 13000 --number-processes 8 -d ...'''
date = "2020-03-10T14:02:00Z"
lastmod = "2020-03-11T10:54:00Z"
weight = 73457
keywords = [ "rendering", "renderd", "osm2pgsql", "mapnik", "tileserver" ]
aliases = [ "/questions/73457" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tile rendering extremly slow](/questions/73457/tile-rendering-extremly-slow)

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
<span id="post-73457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73457-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported germany and tried to render a tile on 10/535/341. It took like 10 Minutes.</p>
<p>Specs:</p>
<ul>
<li>16gb Ram</li>
<li>8 Cores</li>
</ul>
<p>I used the openstreetmap carto style and my import command was:</p>
<pre><code>osm2pgsql --create --slim --flat-nodes /home/renderer/update_tiles/flat-nodes.raw --hstore -C 13000 --number-processes 8 -d gis -h 192.168.2.2 -p 5432 -U renderer --tag_transform-script /home/renderer/src/style/openstreetmap-carto.lua -S /home/renderer/src/openstreetmap-carto.style /home/renderer/import_file.osm.pbf</code></pre>
<p>I tried to tune my postgres server through configuration but nothing helped.</p>
<p>Important is that the postgres and tile server are running in docker containers.</p>
<p>I checked the disk writing speed with:</p>
<pre><code>sudo hdparm -t /dev/mapper/</code></pre>
<p>And got <code>Timing buffered disk reads: 3232 MB in 3.00 seconds = 1077.17 MB/sec</code></p>
<p>My <code>renderd.conf</code>:</p>
<pre><code>[renderd]
num_threads=8
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[ajt]
URI=/hot/
TILEDIR=/var/lib/mod_tile
XML=/home/renderer/src/style/mapnik.xml
HOST=localhost
TILESIZE=256
MAXZOOM=20</code></pre>
<p>My render Command:</p>
<pre><code>renderd -f -c /usr/local/etc/renderd.conf</code></pre>
<p>If you need any more information just ask and thanks for reading and maybe helping.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '20, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/dcc21a76b6706730dfab7d3a68272f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arthurle&#39;s gravatar image" />
<p><span>Arthurle</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arthurle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73457" class="comments-container">
&#10;</div>
<div id="comment-tools-73457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73457-form-container" class="comment-form-container">
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

<span id="73459"></span>

<div id="answer-container-73459" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73459-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arthurle has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not unusual for tiles below zoom 12 to be rather slow. Have you created the indexes as recommended in the openstreetmap-carto setup instructions? That may help a little but not much.</p>
<p>Note that if you've got a standard renderd setup, you have not rendered one tile but 64 tiles (the "meta tile" on which your tile resides). And Germany only has about 20 of them - so even if they take 10 minutes to render, you'll be done in 4 hours. Everyone pre-renders tiles on zoom 0-12 or so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '20, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73459" class="comments-container">
<span id="73469"></span>
<div id="comment-73469" class="comment">
<div id="post-73469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"Note that if you've got a standard renderd setup, you have not rendered one tile but 64 tiles (the "meta tile" on which your tile resides)"</p>
<p>What do you mean?</p>
<p>Why are there 64 tiles rendered for every actual tile? is it always like that? How to turn that off?</p>
</div>
<div id="comment-73469-info" class="comment-info">
<span class="comment-age">(11 Mar '20, 07:39)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73470"></span>
<div id="comment-73470" class="comment">
<div id="post-73470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is explained in the context of "Tirex" here but just as valid for renderd setups: <a href="https://wiki.openstreetmap.org/wiki/Tirex/Overview#Metatiles">https://wiki.openstreetmap.org/wiki/Tirex/Overview#Metatiles</a> -- You do not want to switch it off.</p>
</div>
<div id="comment-73470-info" class="comment-info">
<span class="comment-age">(11 Mar '20, 07:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="73474"></span>
<div id="comment-73474" class="comment">
<div id="post-73474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indexing reduced the render time by 25%. After that i tuned my postgis with this turorial <a href="https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning">https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning</a> which saved me another 20%</p>
</div>
<div id="comment-73474-info" class="comment-info">
<span class="comment-age">(11 Mar '20, 10:54)</span> <span class="comment-user userinfo">Arthurle</span>
</div>
</div>
</div>
<div id="comment-tools-73459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73459-form-container" class="comment-form-container">
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

