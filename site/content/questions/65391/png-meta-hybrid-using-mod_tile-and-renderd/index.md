+++
type = "question"
title = "PNG / Meta hybrid using mod_tile and renderd"
description = '''I have my style sheet the way I want, and was able to use generate_tiles_multiprocess.py to generate my png tiles for zoom levels 4-12.  My thought was to have the &quot;big picture&quot; be static png files, and then only query the database when someone zooms in past that since I don&#x27;t need high detail of de...'''
date = "2018-08-17T00:03:00Z"
lastmod = "2018-08-17T17:39:00Z"
weight = 65391
keywords = [ "apache2", "renderd", "mod_tile" ]
aliases = [ "/questions/65391" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PNG / Meta hybrid using mod_tile and renderd](/questions/65391/png-meta-hybrid-using-mod_tile-and-renderd)

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
<span id="post-65391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have my style sheet the way I want, and was able to use generate_tiles_multiprocess.py to generate my png tiles for zoom levels 4-12.</p>
<p>My thought was to have the "big picture" be static png files, and then only query the database when someone zooms in past that since I don't need high detail of deserts, oceans and such. I have been having a hard time though where I can get it to work one way or the other, but it isn't working as I expected.</p>
<p>What I thought was an incoming request would come for tile <a href="http://127.0.0.1/tiles/6/5/5.png">http://127.0.0.1/tiles/6/5/5.png</a> If that file existed, Apache would serve it up, if it doesn't it would hand off the request to mod_tile / renderd to render the view, which was then stored as a .meta file.</p>
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
<p>Apache conf:</p>
<pre><code>    ServerAdmin webmaster@localhost
    LoadTileConfigFile /usr/local/etc/renderd.conf
    ModTileRenderdSocketName /var/run/renderd/renderd.sock
    ModTileRequestTimeout 10
    ModTileMissingRequestTimeout 50
    DocumentRoot /home/renderaccount/
    LogLevel info 
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache2" rel="tag" title="see questions tagged &#39;apache2&#39;">apache2</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '18, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/644620e74a312b0ce02a0a1bb1bae155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlanHalls&#39;s gravatar image" />
<p><span>AlanHalls</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlanHalls has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65391" class="comments-container">
<span id="65392"></span>
<div id="comment-65392" class="comment">
<div id="post-65392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what "it isn't working as I expected" means? When you request a tile, do you get a "not found" error, or does it time out, or...? Anything in Apache's error log or in the syslog?</p>
</div>
<div id="comment-65392-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 00:52)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="65393"></span>
<div id="comment-65393" class="comment">
<div id="post-65393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great question. I have renderd running in debug mode so I can see what is happening. When I have it working with the png files, then nothing seems to get passed to renderd. When it works with meta files, it ignores the .png files. I have been using <code>sysdig -c echo_fds proc.name=apache2</code> to watch what is happening to see even stuff that wouldn't get logged, but it isn't providing the insight needed to solve it.</p>
</div>
<div id="comment-65393-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 01:10)</span> <span class="comment-user userinfo">AlanHalls</span>
</div>
</div>
<span id="65395"></span>
<div id="comment-65395" class="comment">
<div id="post-65395-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When looking at the output from renderd, I shouldn't see any output for anywhere on the map at zoom levels 5-12 since those are already rendered as PNG files right? And why do I have files like ./6/0/0/0/2/128.meta and ./6/0/0/0/1/136.meta If you check the webhost <a href="http://64.72.211.216">http://64.72.211.216</a> you can see all the files are there for that zoom level, why would it create a meta?</p>
</div>
<div id="comment-65395-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 04:42)</span> <span class="comment-user userinfo">AlanHalls</span>
</div>
</div>
<span id="65401"></span>
<div id="comment-65401" class="comment">
<div id="post-65401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I see now what has happened. proper answer following.</p>
</div>
<div id="comment-65401-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 09:49)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65391-form-container" class="comment-form-container">
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

<span id="65400"></span>

<div id="answer-container-65400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65400-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have misunderstood how mod_tile and renderd are supposed to work.</p>
<p>The generate_tiles_multiprocess.py script would not normally be used by someone who wants to set up a tile server.</p>
<p>Instead, you would run a command like render_list which would generate meta tiles for the area and zoom levels specified. These meta tiles contain 8x8 PNG files each but the PNGs are never stored on disk directly. Instead, when a certain tile is requested through the web server, mod_tile will open the requisite .meta file, exrtact the PNG from there, and serve it. Only if the meta file is not there will mod_tile send a request to renderd to create it.</p>
<p>The tile directory that you have built with generate_tiles_multiprocess.py <em>could</em> be used to run a tile server completely without renderd and database - simply point DocumentRoot to your tile directory - but of course that server would be fully static, and not support updating or on-the-fly rendering of tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '18, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-65400" class="comments-container">
<span id="65408"></span>
<div id="comment-65408" class="comment">
<div id="post-65408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for teaching me the difference. render_list is doing a great job and seems to be processing much faster than the png files.</p>
</div>
<div id="comment-65408-info" class="comment-info">
<span class="comment-age">(17 Aug '18, 17:39)</span> <span class="comment-user userinfo">AlanHalls</span>
</div>
</div>
</div>
<div id="comment-tools-65400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65400-form-container" class="comment-form-container">
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

