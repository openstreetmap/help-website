+++
type = "question"
title = "Mod_Tile handing off to renderd when tiles exist"
description = '''I have tiles rendered for zoom 0-13, and yet when I bring up the map with renderd running in debug mode I can see it making requests: renderd[18553]: DEBUG: Got incoming connection, fd 8, number 1 renderd[18553]: DEBUG: Got incoming request with protocol version 2 renderd[18553]: DEBUG: Got command ...'''
date = "2018-08-22T16:36:00Z"
lastmod = "2018-08-23T19:13:00Z"
weight = 65502
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/65502" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mod_Tile handing off to renderd when tiles exist](/questions/65502/mod_tile-handing-off-to-renderd-when-tiles-exist)

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
<span id="post-65502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65502-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have tiles rendered for zoom 0-13, and yet when I bring up the map with renderd running in debug mode I can see it making requests:</p>
<pre><code>renderd[18553]: DEBUG: Got incoming connection, fd 8, number 1
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(8) xml(tiles), z(8), x(47), y(100), mime(image/png), options()
renderd[18553]: DEBUG: START TILE tiles 8 40-47 96-103, age 5.93 days
renderd[18553]: Rendering projected coordinates 8 40 96 -&gt; -13775786.985675|3757032.814275 -12523442.714250|5009377.085700 to a 8 x 8 tile
renderd[18553]: DEBUG: Got incoming connection, fd 9, number 2
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(9) xml(tiles), z(8), x(47), y(103), mime(image/png), options()
renderd[18553]: DEBUG: Got incoming connection, fd 10, number 3
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(10) xml(tiles), z(8), x(47), y(101), mime(image/png), options()
renderd[18553]: DEBUG: Got incoming connection, fd 11, number 4
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(11) xml(tiles), z(8), x(47), y(102), mime(image/png), options()
renderd[18553]: DEBUG: Got incoming connection, fd 12, number 5
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(12) xml(tiles), z(8), x(46), y(101), mime(image/png), options()
renderd[18553]: DEBUG: Got incoming connection, fd 14, number 6
renderd[18553]: DEBUG: Got incoming request with protocol version 2
renderd[18553]: DEBUG: Got command RenderLow fd(14) xml(tiles), z(8), x(46), y(102), mime(image/png), options()</code></pre>
<p>If I stop the renderd process, the tiles are pulled from cache instantly, but if it is running it queries the DB even when it doesn't need to. I tried increasing the minimum cache, the render_list was run last week, so if that time listed is in seconds then the cache would last 28 years, if it is in milliseconds it is only 10 days, but it has only been 5 days since render.</p>
<p>Here is my Apache Config:</p>
<pre><code>    LoadTileConfigFile /usr/local/etc/renderd.conf
    ModTileRenderdSocketName /var/run/renderd/renderd.sock
    # Timeout before giving up for a tile to be rendered
    ModTileRequestTimeout 3
    # Timeout before giving up for a tile to be rendered that is otherwise missing
    ModTileMissingRequestTimeout 10
    ModTileCacheDurationMax 60480000000
    ModTileCacheDurationMinimum 908000000
    DocumentRoot /home/renderaccount/</code></pre>
<p>And here is renderd:</p>
<pre><code>[renderd]
num_threads=8
tile_dir=/home/renderaccount
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[tiles]
URI=/tiles/
TILEDIR=/home/renderaccount
XML=/home/renderaccount/openstreetmap-carto/mapnik.xml
HOST=*
TILESIZE=256
MAXZOOM=20</code></pre>
<p>Any suggestions would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '18, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/644620e74a312b0ce02a0a1bb1bae155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlanHalls&#39;s gravatar image" />
<p><span>AlanHalls</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlanHalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65502" class="comments-container">
&#10;</div>
<div id="comment-tools-65502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65502-form-container" class="comment-form-container">
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

<span id="65504"></span>

<div id="answer-container-65504" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65504-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlanHalls has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I'd expect it to do is sending the current tile to the user, and rendering a new one in the background. The tile in your example is "age 5.93 days". If it was less than 4 days old I bet it wouldn't render a new one. It's zoom level 8, so I don't think that "dirty" will come into play.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '18, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-65504" class="comments-container">
<span id="65505"></span>
<div id="comment-65505" class="comment">
<div id="post-65505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The requests are low priority render request (RenderLow) which will be issued by mod_tile if the tile is considered "old but not too old". A tile starts becoming old when its timestamp is older than the timestamp of the <code>planet-import-complete</code> file at the root of the tile directory. If such a file does not exist, the tile starts becoming old when its timestamp is older than three days (<a href="https://github.com/openstreetmap/mod_tile/blob/62c4a5ac7a57720182125b8aad11929dae947e46/src/store_file.c#L40-L41).">https://github.com/openstreetmap/mod_tile/blob/62c4a5ac7a57720182125b8aad11929dae947e46/src/store_file.c#L40-L41).</a> To avoid re-rendering of old tiles altogether, provide a <code>planet-import-complete</code> file that has a very old timestamp. To allow re-rendering but not have the client wait for such tiles, set your <code>ModTileRequestTimeout</code> to 0 instead of 3.</p>
</div>
<div id="comment-65505-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 19:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="65535"></span>
<div id="comment-65535" class="comment">
<div id="post-65535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik, that worked perfect.</p>
</div>
<div id="comment-65535-info" class="comment-info">
<span class="comment-age">(23 Aug '18, 19:13)</span> <span class="comment-user userinfo">AlanHalls</span>
</div>
</div>
</div>
<div id="comment-tools-65504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65504-form-container" class="comment-form-container">
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

