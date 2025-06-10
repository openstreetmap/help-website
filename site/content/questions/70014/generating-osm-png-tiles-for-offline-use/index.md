+++
type = "question"
title = "Generating OSM png tiles for offline use"
description = '''I&#x27;m very new and very confused about how to accomplish a seemingly simple task: generate my own OSM .png tiles for offline use. Since I want to be able to have a huge amount of tiles, I don&#x27;t want to load the server by downloading tiles directly from tile.openstreetmap.org. I was using Creating your...'''
date = "2019-07-13T00:23:00Z"
lastmod = "2021-03-15T20:38:00Z"
weight = 70014
keywords = [ "carto", "tiles", "osm", "mapnik", "generate_tiles" ]
aliases = [ "/questions/70014" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Generating OSM png tiles for offline use](/questions/70014/generating-osm-png-tiles-for-offline-use)

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
<span id="post-70014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70014-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm very new and very confused about how to accomplish a seemingly simple task: generate my own OSM .png tiles for offline use. Since I want to be able to have a huge amount of tiles, I don't want to load the server by downloading tiles directly from <code>tile.openstreetmap.org</code>.</p>
<p>I was using <a href="https://wiki.openstreetmap.org/wiki/Creating_your_own_tiles#Creating_tiles_using_Mapnik_and_generate_tiles.py">Creating your own tiles</a>, but learned that this method is outdated with the new styling method: <a href="https://github.com/openstreetmap/mapnik-stylesheets/issues/15">mapnik-stylesheets issue #15</a></p>
<p>Since this is all new to me, I'm quite confused at the sheer number of methods and tools I've seen recommended to download, format, and render OSM tiles. As far as my progress, here are the steps I have taken:</p>
<ol>
<li>Created a Postgres database named <code>gis</code>, enabling the <code>postgis</code> and <code>hstore</code> extensions</li>
<li>Downloaded <code>arizona-latest.osm.pbf</code> from <a href="https://download.geofabrik.de/north-america.html">https://download.geofabrik.de/north-america.html</a></li>
<li>Used <code>osm2pgsql</code> to import <code>arizona-latest.osm.pbf</code> into the Postgres database <code>gis</code>: <code>osm2pgsql -G --hstore --style openstreetmap-carto.style --tag-transform-script openstreetmap-carto.lua -d gis --slim --flat-nodes /home/user/nodes.cache --cache 5000 /home/user/downloads/arizona-latest.osm.pbf</code></li>
<li>Generated shapefiles using <code>scripts/get-shapefiles.py</code> in the <code>openstreetmap-carto</code> directory</li>
<li>Created <code>osm.xml</code> by running <code>carto project.mml &gt; osm.xml</code></li>
<li>Successfully generated an image using <code>generate_image.py</code> from the outdated <code>mapnik-stylesheets</code> with warnings about failing to understand the new <code>carto</code> xml format.</li>
<li>Failed to generate tiles using <code>generate_tiles.py</code> from the outdated <code>mapnik-stylesheets</code> with the same errors from <code>generate_image.py</code>.</li>
</ol>
<p>I'm at a loss at where to go from here with my current understanding of how this all works. If anyone can point me in the right direction, I'd greatly appreciate it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '19, 00:23</strong></p>
<img src="https://secure.gravatar.com/avatar/705ee46fd6a481b68447d9311e9c0647?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karmic%20Creditor&#39;s gravatar image" />
<p><span>Karmic Creditor</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karmic Creditor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70014" class="comments-container">
&#10;</div>
<div id="comment-tools-70014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70014-form-container" class="comment-form-container">
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

<span id="70015"></span>

<div id="answer-container-70015" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70015-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Karmic Creditor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I'd suggest is:</p>
<ul>
<li>Set up a tile server as per <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">the switch2osm guide</a>.</li>
<li>Follow <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Force_Rendering_Tiles">this diary entry</a> to generate tiles.</li>
</ul>
<p>The problem with generate_tiles.py is that it'll complain about unused font definitions in the stylesheet.</p>
<p>Edit: As noted below this will generate metatiles, not .png tiles, which probably isn't the best route here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '19, 00:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '19, 11:09</strong> </span></p>
</div>
</div>
<div id="comments-container-70015" class="comments-container">
<span id="70016"></span>
<div id="comment-70016" class="comment">
<div id="post-70016-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I did have to edit the <code>osm.xml</code> to remove all fonts except <code>Deja Vu Sans</code> because of the complaining. The errors/warnings I get when running the scripts are similar to <code>attribute 'maximum-scale-denominator' with value '100000' at line 0</code>, which, if I understand correctly, is because of the new styles used by OSM. I will try your method and report back.</p>
</div>
<div id="comment-70016-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 00:58)</span> <span class="comment-user userinfo">Karmic Creditor</span>
</div>
</div>
<span id="70020"></span>
<div id="comment-70020" class="comment">
<div id="post-70020-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
<p>The method you suggested works great. One thing I'm curious about is the diary entry you mentioned. When calling <code>render_list</code>, it seems to create <code>.meta</code> files. Does this produce <code>.png</code> files somewhere I'm not looking?</p>
</div>
<div id="comment-70020-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 06:01)</span> <span class="comment-user userinfo">Karmic Creditor</span>
</div>
</div>
<span id="70033"></span>
<div id="comment-70033" class="comment">
<div id="post-70033-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>.meta files are containers that contain 64 PNG files each. To extract .png from .meta, either run mod_tile in your Apache web server and run lots and lots of "wget" or "curl" commands against your own web server, or use <a href="https://github.com/geofabrik/meta2tile">https://github.com/geofabrik/meta2tile</a> to go from meta to png without mod_tile/Apache.</p>
</div>
<div id="comment-70033-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 10:01)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70035"></span>
<div id="comment-70035" class="comment">
<div id="post-70035-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It sounds like you're nearly there - just one comment about "I did have to edit the osm.xml to remove all fonts except Deja Vu Sans because of the complaining":</p>
<p>You might find it easier to edit the stylesheet (the thing you run "carto" on) rather than editing the generated .xml directly. If you can find out what's causing the problem you can probably edit it out in one place in a .mss file rather than many from the generated .xml.</p>
</div>
<div id="comment-70035-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 11:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70041"></span>
<div id="comment-70041" class="comment">
<div id="post-70041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you two for the help. I will use meta2tile when the render_list completes</p>
</div>
<div id="comment-70041-info" class="comment-info">
<span class="comment-age">(13 Jul '19, 12:14)</span> <span class="comment-user userinfo">Karmic Creditor</span>
</div>
</div>
</div>
<div id="comment-tools-70015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70015-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79278"></span>

<div id="answer-container-79278" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79278-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Two years later) You could also use my beefed up version of <a href="https://github.com/StyXman/osm-tile-tools/"><code>generate_tiles.py</code></a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '21, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79278" class="comments-container">
&#10;</div>
<div id="comment-tools-79278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79278-form-container" class="comment-form-container">
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

