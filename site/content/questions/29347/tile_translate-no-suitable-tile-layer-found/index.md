+++
type = "question"
title = "tile_translate: No suitable tile layer found"
description = '''I running on Fedora 19 with postgis-2.0.3-1, postgresql-9.2.6, mapnik-2.0.2 and osm2pgsql-0.82.0-3. I create a database. Cloned mapnik-stylesheets. Cloned, built and installed mod_tile. I run &#x27;renderd -f&#x27; then in the browser hit slippymap.html but the apache log says things like: [Thu Dec 26 16:20:0...'''
date = "2013-12-26T22:35:00Z"
lastmod = "2013-12-27T00:06:00Z"
weight = 29347
keywords = [ "mod_tile" ]
aliases = [ "/questions/29347" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tile_translate: No suitable tile layer found](/questions/29347/tile_translate-no-suitable-tile-layer-found)

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
<span id="post-29347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I running on Fedora 19 with postgis-2.0.3-1, postgresql-9.2.6, mapnik-2.0.2 and osm2pgsql-0.82.0-3. I create a database. Cloned mapnik-stylesheets. Cloned, built and installed mod_tile. I run 'renderd -f' then in the browser hit slippymap.html but the apache log says things like:</p>
<pre><code>[Thu Dec 26 16:20:05.506318 2013] [core:info] [pid 12644] [client ::1:44050] AH00128: File does not exist: /var/www/html/10/536/359.png, referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506410 2013] [tile:debug] [pid 12637] ./src/mod_tile.c(1278): [client ::1:44047] tile_translate: uri(/10/536/355.png), referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506430 2013] [tile:debug] [pid 12637] ./src/mod_tile.c(1296): [client ::1:44047] tile_translate: testing baseuri(/osm_tiles/) name(default) extension(png), referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506447 2013] [tile:debug] [pid 12637] ./src/mod_tile.c(1386): [client ::1:44047] tile_translate: No suitable tile layer found, referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506489 2013] [authz_core:debug] [pid 12637] mod_authz_core.c(802): [client ::1:44047] AH01626: authorization result of Require all granted: granted, referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506513 2013] [authz_core:debug] [pid 12637] mod_authz_core.c(802): [client ::1:44047] AH01626: authorization result of &lt;RequireAny&gt;: granted, referer: http://localhost/slippymap.html
[Thu Dec 26 16:20:05.506541 2013] [core:info] [pid 12637] [client ::1:44047] AH00128: File does not exist: /var/www/html/10/536/355.png, referer: http://localhost/slippymap.html</code></pre>
<p>There's something I'm not understanding about the configuration because I'm not seeing any output from renderd. It doesn't appear that mod_tile and renderd are talking. Apache and renderd are running as the apache user who owns /var/run/renderd and its contents. Here's my renderd.conf:</p>
<pre><code>[renderd]
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/home/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib64/mapnik/input
font_dir=/usr/share/fonts/dejavu
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/home/mod_tile
XML=/home/apache/mapnik-stylesheets/osm.xml
HOST=127.0.0.1
TILESIZE=256</code></pre>
<p>And I'm using pretty much the stock mod_tile.conf which I dropped into /etc/httpd/conf.d. Can anyone help me understand/debug this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '13, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/49483047a50e772b43d81390908f2901?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="txtoth&#39;s gravatar image" />
<p><span>txtoth</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="txtoth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '13, 00:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-29347" class="comments-container">
&#10;</div>
<div id="comment-tools-29347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29347-form-container" class="comment-form-container">
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

<span id="29348"></span>

<div id="answer-container-29348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29348-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your mod_tile feels responsible for URIs whose first path element is /osm_tiles/ but your slippymap.html does not add this path element and instead of e.g. <a href="http://localhost/osm_tiles/0/0/0.png">http://localhost/osm_tiles/0/0/0.png</a> tries to access <a href="http://localhost/0/0/0.png.">http://localhost/0/0/0.png.</a> Either fix your slippymap.html or the URI line in your renderd.conf.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29348" class="comments-container">
&#10;</div>
<div id="comment-tools-29348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29348-form-container" class="comment-form-container">
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

