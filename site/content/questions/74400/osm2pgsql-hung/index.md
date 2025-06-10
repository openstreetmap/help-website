+++
type = "question"
title = "osm2pgsql hung"
description = '''osm2pgsql seems to freeze midway. I had done an osmosis upgrade few days back. Please suggest how to troubleshoot this. Earlier also it had hung up for 6 days so I had killed it.  Below process is running right now: osm2pgsql -a --slim -e10-15 -d gis --flat-nodes /var/data/flat_nodes.bin --cache 200...'''
date = "2020-04-27T10:20:00Z"
lastmod = "2020-04-28T05:19:00Z"
weight = 74400
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/74400" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql hung](/questions/74400/osm2pgsql-hung)

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
<span id="post-74400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74400-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>osm2pgsql seems to freeze midway. I had done an osmosis upgrade few days back. Please suggest how to troubleshoot this. Earlier also it had hung up for 6 days so I had killed it.</p>
<p>Below process is running right now: osm2pgsql -a --slim -e10-15 -d gis --flat-nodes /var/data/flat_nodes.bin --cache 2000 --number-processes 8 -G --hstore --tag-transform-script /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.lua --style /home/postgresql/osm/openstreetmap-carto/openstreetmap-carto.style --multi-geometry -o /var/lib/mod_tile/dirty_tiles.10057 /var/lib/mod_tile/changes.osc.gz</p>
<h1 id="usrlocalbinosm2pgsql---version">/usr/local/bin/osm2pgsql --version</h1>
<p>osm2pgsql version 0.96.0 (64 bit id space)</p>
<p>Compiled using the following library versions: Libosmium 2.14.2 Lua 5.2.4</p>
<pre><code>root@xxxxx:/var/log/tiles# tail osm2pgsql.log
Large polygon (33929 x 41624 metres, OSM ID -162378) - only expiring perimeter
Large polygon (33929 x 41624 metres, OSM ID -162378) - only expiring perimeter
Large polygon (88519 x 83715 metres, OSM ID -163123) - only expiring perimeter
Large polygon (82590 x 80987 metres, OSM ID -163123) - only expiring perimeter
Large polygon (79281 x 53239 metres, OSM ID -163123) - only expiring perimeter
Large polygon (78634 x 80987 metres, OSM ID -163123) - only expiring perimeter
Large polygon (91576 x 83715 metres, OSM ID -163123) - only expiring perimeter
Large polygon (79281 x 53239 metres, OSM ID -163123) - only expiring perimeter
Large polygon (95617 x 139209 metres, OSM ID -163124) - only expiring perimeter
Large polygon (96661 x 112500 metres, OSM ID -163124) - only expiring perimeter</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '20, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '20, 10:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-74400" class="comments-container">
<span id="74401"></span>
<div id="comment-74401" class="comment">
<div id="post-74401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When it "seems to freeze" what is happening on your system in terms of CPU use, memory use, etc.?</p>
</div>
<div id="comment-74401-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 10:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74402"></span>
<div id="comment-74402" class="comment">
<div id="post-74402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The process is running as seen in the output of top. This server has 32 cpu cores. But osm2pgsql.log is not having any updates. It runs like this for many days without any updates in the log file.</p>
<p>PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND 15406 rendera+ 20 0 58.183g 0.013t 0.012t R 100.0 20.6 82:25.79 osm2pgsql</p>
<p>memory usage:</p>
<h1 id="free--m">free -m</h1>
<pre><code>          total        used        free      shared  buff/cache   available</code></pre>
<p>Mem: 64384 2505 980 16706 60898 44522 Swap: 15255 0 15255</p>
</div>
<div id="comment-74402-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 10:43)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="74406"></span>
<div id="comment-74406" class="comment">
<div id="post-74406-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What is your osmosis command like? Did you simplified the changes and is this a combined change for what timeframe? Which osmosis version are you using?</p>
<p>This may be of help: <a href="https://blog.geofabrik.de/?p=544">https://blog.geofabrik.de/?p=544</a> (read the case about problems since or around April 17th.).</p>
</div>
<div id="comment-74406-info" class="comment-info">
<span class="comment-age">(27 Apr '20, 11:34)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="74432"></span>
<div id="comment-74432" class="comment">
<div id="post-74432-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The solution provided by Spiekerooger worked for me. I increased the maxInterval to 432000 seconds which is 5 days and the update worked fine.</p>
</div>
<div id="comment-74432-info" class="comment-info">
<span class="comment-age">(28 Apr '20, 05:19)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
</div>
<div id="comment-tools-74400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74400-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

