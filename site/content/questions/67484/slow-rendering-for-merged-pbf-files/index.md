+++
type = "question"
title = "Slow rendering for merged PBF files"
description = '''I have setup a local tile server by following this manual: https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ I need to get tiles for USA, UK and Ireland. I&#x27;ve prepared a merged PBF file as described here: https://gis.stackexchange.com/questions/50745/merging-osm-files-with-osmosis-...'''
date = "2019-01-07T11:45:00Z"
lastmod = "2019-01-07T13:10:00Z"
weight = 67484
keywords = [ "rendering", "slow", "tileserver" ]
aliases = [ "/questions/67484" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Slow rendering for merged PBF files](/questions/67484/slow-rendering-for-merged-pbf-files)

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
<span id="post-67484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67484-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup a local tile server by following this manual: <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
<p>I need to get tiles for USA, UK and Ireland. I've prepared a merged PBF file as described here: <a href="https://gis.stackexchange.com/questions/50745/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql">https://gis.stackexchange.com/questions/50745/merging-osm-files-with-osmosis-and-import-to-postgres-with-osm2pgsql</a></p>
<p>The merged file has been imported successfully. But when I run renderd and tried to open a sample tile in browser, the rendering has been failed (postgres stuck at the SQL query). The behavior was exactly the same as described here: <a href="https://help.openstreetmap.org/questions/24290/local-tile-server-extremely-slow-rendering">https://help.openstreetmap.org/questions/24290/local-tile-server-extremely-slow-rendering</a></p>
<p>Here's the renderd log:</p>
<p>renderd[29977]: DEBUG: Got incoming connection, fd 8, number 1 renderd[29977]: DEBUG: Got incoming request with protocol version 2 renderd[29977]: DEBUG: Got command RenderPrio fd(8) xml(ajt), z(2), x(1), y(0), mime(image/png), options() renderd[29977]: DEBUG: START TILE ajt 2 0-3 0-3, new metatile renderd[29977]: Rendering projected coordinates 2 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 4 x 4 tile renderd[29977]: DEBUG: Connection 0, fd 8 closed, now 0 left renderd[29977]: DEBUG: DONE TILE ajt 2 0-3 0-3 in 393.157 seconds debug: Creating and writing a metatile to /var/lib/mod_tile/ajt/2/0/0/0/0/0.meta</p>
<p>The rendering took 393 seconds!</p>
<p>I checked the postgresql indexes, all indexes were there:</p>
<p>\d planet_osm_polygon ... Indexes: "planet_osm_polygon_osm_id_idx" btree (osm_id) "planet_osm_polygon_way_idx" gist (way) Triggers: planet_osm_polygon_osm2pgsql_valid BEFORE INSERT OR UPDATE ON planet_osm_polygon FOR EACH ROW EXECUTE PROCEDURE planet_osm_polygon_osm2pgsql_valid()</p>
<p>I cleared the database then tried to install the test (Ireland) PBF file. For Ireland, the rendering took less than a second.</p>
<p>What I am doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '19, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/9fb0408ea4f0bb7b09b9e23f8e369248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sevantus&#39;s gravatar image" />
<p><span>sevantus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sevantus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67484" class="comments-container">
&#10;</div>
<div id="comment-tools-67484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67484-form-container" class="comment-form-container">
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

<span id="67485"></span>

<div id="answer-container-67485" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67485-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sevantus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Zoom level two tiles are very large (and Ireland is a lot smaller than a single one), you should in general not expect these to render in a time frame that will work for interactive viewing and no number of exclamation marks is going to change that.</p>
<p>With other words these tiles need to be pre-rendered, see the instructions at the end of <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '19, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67485" class="comments-container">
<span id="67486"></span>
<div id="comment-67486" class="comment">
<div id="post-67486-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That makes sense, thank you for the answer! I rendered some tiles on 13th zoom level and they are rendered within a second.</p>
</div>
<div id="comment-67486-info" class="comment-info">
<span class="comment-age">(07 Jan '19, 13:10)</span> <span class="comment-user userinfo">sevantus</span>
</div>
</div>
</div>
<div id="comment-tools-67485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67485-form-container" class="comment-form-container">
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

