+++
type = "question"
title = "Rendering failed with command 4, pausing."
description = '''Hi all, I am trying to run the render_list command to render my maps. However I am getting a &quot;rendering failed with command 4, pausing.&quot; when it gets to zoom 7. The same &quot;error&quot; will happen for about 20-30 times before it gets to &quot;Rendering All tiles for zoom 7...&quot; and then back to the error. Any he...'''
date = "2017-12-19T18:43:00Z"
lastmod = "2020-10-09T23:11:00Z"
weight = 61278
keywords = [ "zoomlevel", "rendering", "tiles", "zoom" ]
aliases = [ "/questions/61278" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering failed with command 4, pausing.](/questions/61278/rendering-failed-with-command-4-pausing)

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
<span id="post-61278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to run the render_list command to render my maps. However I am getting a "rendering failed with command 4, pausing." when it gets to zoom 7. The same "error" will happen for about 20-30 times before it gets to "Rendering All tiles for zoom 7..." and then back to the error. Any help would be greatly appreciate and please let me know if I need to provide more logs or any more details.</p>
<p>Edit: based off the syslog it looks like its going to pull some maps from 7/88/48 (for example) but cant find it?</p>
<pre><code>jth-admin@xxxxxxx:/home/osm$ sudo ./render_world.sh
[sudo] password for jth-admin:
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Rendering client
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 7
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)
rendering failed with command 4, pausing.
rendering failed with command 4, pausing.
rendering failed with command 4, pausing.</code></pre>
<p>Here is the contents of render_world.sh (just used for logging):</p>
<pre><code>jth-admin@xxxxxxx:/home/osm$ cat render_world.sh
#!/bin/sh
echo Starting render for World level 0-7 &gt;&gt; render.log
date &gt;&gt; render.log
time render_list -a -s /var/run/renderd/renderd.sock -z 0 -Z 7 --force
echo Finished render for World level 0-7 &gt;&gt; render.log
date &gt;&gt; render.log
&#10;echo &quot;Done&quot;</code></pre>
<p>here is a small snippet of /var/log/syslog</p>
<pre><code>Dec 19 13:00:01 xxxxxxx render_list: DEBUG: Sending render cmd(6 default 7/88/40) with protocol version 2 to fd 4
Dec 19 13:00:01 xxxxxxx renderd[3795]: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:01 xxxxxxx renderd[3795]: DEBUG: Got command RenderBulk fd(8) xml(default), z(7), x(88), y(40), mime(image/png), options()
Dec 19 13:00:01 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load
Dec 19 13:00:01 xxxxxxx renderd[3795]: DEBUG: Sending render cmd(4 default 7/88/40) with protocol version 2 to fd 8
Dec 19 13:00:01 xxxxxxx render_list: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:11 xxxxxxx render_list: DEBUG: Sending render cmd(6 default 7/88/48) with protocol version 2 to fd 4
Dec 19 13:00:11 xxxxxxx renderd[3795]: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:11 xxxxxxx renderd[3795]: DEBUG: Got command RenderBulk fd(8) xml(default), z(7), x(88), y(48), mime(image/png), options()
Dec 19 13:00:11 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load
Dec 19 13:00:11 xxxxxxx renderd[3795]: DEBUG: Sending render cmd(4 default 7/88/48) with protocol version 2 to fd 8
Dec 19 13:00:11 xxxxxxx render_list: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:18 xxxxxxx renderd[3795]: DEBUG: Failed to read cmd on fd 8
Dec 19 13:00:18 xxxxxxx renderd[3795]: DEBUG: Connection 0, fd 8 closed, now 0 left
Dec 19 13:00:48 xxxxxxx renderd[3795]: DEBUG: Got incoming connection, fd 8, number 1
Dec 19 13:00:48 xxxxxxx render_list: DEBUG: Sending render cmd(6 default 0/0/0) with protocol version 2 to fd 4
Dec 19 13:00:48 xxxxxxx renderd[3795]: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:48 xxxxxxx renderd[3795]: DEBUG: Got command RenderBulk fd(8) xml(default), z(0), x(0), y(0), mime(image/png), options()
Dec 19 13:00:48 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load
Dec 19 13:00:48 xxxxxxx renderd[3795]: DEBUG: Sending render cmd(4 default 0/0/0) with protocol version 2 to fd 8
Dec 19 13:00:48 xxxxxxx render_list: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:58 xxxxxxx render_list: DEBUG: Sending render cmd(6 default 1/0/0) with protocol version 2 to fd 4
Dec 19 13:00:58 xxxxxxx renderd[3795]: DEBUG: Got incoming request with protocol version 2
Dec 19 13:00:58 xxxxxxx renderd[3795]: DEBUG: Got command RenderBulk fd(8) xml(default), z(1), x(0), y(0), mime(image/png), options()
Dec 19 13:00:58 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load
Dec 19 13:00:58 xxxxxxx renderd[3795]: DEBUG: Sending render cmd(4 default 1/0/0) with protocol version 2 to fd 8
Dec 19 13:00:58 xxxxxxx render_list: DEBUG: Got incoming request with protocol version 2
Dec 19 13:01:08 xxxxxxx render_list: DEBUG: Sending render cmd(6 default 2/0/0) with protocol version 2 to fd 4
Dec 19 13:01:08 xxxxxxx renderd[3795]: DEBUG: Got incoming request with protocol version 2
Dec 19 13:01:08 xxxxxxx renderd[3795]: DEBUG: Got command RenderBulk fd(8) xml(default), z(2), x(0), y(0), mime(image/png), options()
Dec 19 13:01:08 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load
Dec 19 13:01:08 xxxxxxx renderd[3795]: DEBUG: Sending render cmd(4 default 2/0/0) with protocol version 2 to fd 8
Dec 19 13:01:08 xxxxxxx render_list: DEBUG: Got incoming request with protocol version 2
Dec 19 13:05:01 xxxxxxx CRON[20446]: (munin) CMD (if [ -x /usr/bin/munin-cron ]; then /usr/bin/munin-cron; fi)</code></pre>
<p>Here is the contents of the renderd.conf file:</p>
<pre><code>jth-admin@xxxxxxx:/home/osm$ cat /usr/local/etc/renderd.conf
[renderd]
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/var/lib/mod_tile
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/truetype/ttf-dejavu
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_file
XML=/usr/local/share/maps/style/OSMBright/OSMBright.xml
HOST=localhost
TILESIZE=256</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Dec '17, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/7e15a6fef91f6e39d22fcd6873a5d835?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhollingsworth&#39;s gravatar image" />
<p><span>jhollingsworth</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhollingsworth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '17, 18:52</strong> </span></p>
</div>
</div>
<div id="comments-container-61278" class="comments-container">
&#10;</div>
<div id="comment-tools-61278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61278-form-container" class="comment-form-container">
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

<span id="61279"></span>

<div id="answer-container-61279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61279-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's your problem:</p>
<pre><code>Dec 19 13:00:48 xxxxxxx renderd[3795]: Received request for map layer &#39;default&#39; which failed to load</code></pre>
<p>There's something that the map style is trying to do which failed to load. Try restarting renderd and look at syslog, and there will be more information there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '17, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-61279" class="comments-container">
&#10;</div>
<div id="comment-tools-61279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61279-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67139"></span>

<div id="answer-container-67139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>in my case the problem was get-shapefiles.py faild to download some of the files so map layer 'default' dident find the shapes and failed , so i downloaded and added them manually.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '18, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8524afbaa2cb261296c620ea044952de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="do-d&#39;s gravatar image" />
<p><span>do-d</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="do-d has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67139" class="comments-container">
<span id="77033"></span>
<div id="comment-77033" class="comment">
<div id="post-77033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16029/do-d">@do-d</a>, can you explain how you did that?</p>
</div>
<div id="comment-77033-info" class="comment-info">
<span class="comment-age">(09 Oct '20, 23:11)</span> <span class="comment-user userinfo">Bill</span>
</div>
</div>
</div>
<div id="comment-tools-67139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67139-form-container" class="comment-form-container">
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

