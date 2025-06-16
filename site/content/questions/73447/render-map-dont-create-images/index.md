+++
type = "question"
title = "render map dont create images"
description = '''i installed mapnik and other scripts for render the map now i run the sample command &quot;sudo render_list -n 3 -z 0 -Z 1 -a&quot; and  dont create any image in /var/lib/mod_tile folder and i got the output: peiman@map:~$ sudo render_list -n 3 -z 0 -Z 1 -a debug: init_storage_backend: initialising file stora...'''
date = "2020-03-09T15:14:00Z"
lastmod = "2020-03-16T12:37:00Z"
weight = 73447
keywords = [ "rendered", "mapnik" ]
aliases = [ "/questions/73447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [render map dont create images](/questions/73447/render-map-dont-create-images)

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
<span id="post-73447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i installed mapnik and other scripts for render the map</p>
<p>now i run the sample command "sudo render_list -n 3 -z 0 -Z 1 -a" and dont create any image in /var/lib/mod_tile folder</p>
<p>and i got the output:</p>
<pre><code>peiman@map:~$ sudo render_list -n 3 -z 0 -Z 1 -a
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Rendering client
Starting 3 rendering threads
Rendering all tiles from zoom 0 to zoom 1
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Waiting for rendering threads to finish
rendering failed with command 4, pausing.
rendering failed with command 4, pausing.
&#10;*****************************************************
*****************************************************
Total for all tiles rendered
Meta tiles rendered: Rendered 2 tiles in 10.00 seconds (0.20 tiles/s)
Total tiles rendered: Rendered 128 tiles in 10.00 seconds (12.80 tiles/s)
Total tiles handled: Rendered 2 tiles in 10.00 seconds (0.20 tiles/s)
*****************************************************
*****************************************************</code></pre>
<p>how can i debug my process? this is my rendered config file</p>
<pre><code>peiman@map:~$ sudo cat /etc/renderd.conf
[renderd]
stats_file=/var/run/renderd/renderd.stats
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/var/lib/mod_tile
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts
font_dir_recurse=true
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile
&#10;XML=/home/peiman/src/openstreetmap-carto/style.xml
DESCRIPTION=This is the standard osm mapnik style
&#10;
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;https://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;https://wiki.openstreetmap.org/w\
;iki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://creativecommons.org/licenses/by-sa/2.0/\&quot;&gt;CC-BY-SA&lt;/a&gt;
HOST=localhost
TILESIZE=256
&#10;;SERVER_ALIAS=http://a.tile.openstreetmap.org
;SERVER_ALIAS=http://b.tile.openstreetmap.org
;HTCPHOST=proxy.openstreetmap.org</code></pre>
<p>also some scripts and versions</p>
<pre><code>peiman@map:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic
peiman@map:~$ mapnik-config -v
3.0.22
peiman@map:~$ mapnik-config --input-plugins
/usr/lib/mapnik/3.0/input
peiman@map:~$ carto -v
1.2.0</code></pre>
<p>/var/log/syslog</p>
<pre><code>Mar 10 05:38:17 map renderd[1559]: Starting stats thread
Mar 10 05:38:17 map renderd[1559]: Loading parameterization function for
Mar 10 05:38:17 map renderd[1559]: message repeated 3 times: [ Loading parameterization function for]
Mar 10 05:38:17 map renderd[1559]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: FATAL:  role &quot;www-data&quot; does not exist#012Connection string: &#39; dbname=gis connect_timeout=4&#39;#012  encountered during parsing of $
Mar 10 05:38:17 map renderd[1559]: message repeated 3 times: [ An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: FATAL:  role &quot;www-data&quot; does not exist#012Connection string: &#39; dbname=gis connect_timeout=4&#39;#012  en$
Mar 10 05:38:17 map cloud-init[1565]: Cloud-init v. 19.4-33-gbb4131a2-0ubuntu1~18.04.1 running &#39;modules:final&#39; at Tue, 10 Mar 2020 05:38:17 +0000. Up 23.51 seconds.
Mar 10 05:38:17 map cloud-init[1565]: Cloud-init v. 19.4-33-gbb4131a2-0ubuntu1~18.04.1 finished at Tue, 10 Mar 2020 05:38:17 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net][dsmode=net].  Up 23.73 seconds
Mar 10 05:38:18 map systemd[1]: Started Execute cloud user/final scripts.
Mar 10 05:38:18 map systemd[1]: Reached target Cloud-init target.
Mar 10 05:38:18 map systemd[1]: Startup finished in 3.616s (kernel) + 20.190s (userspace) = 23.806s.
Mar 10 05:38:27 map systemd[1]: Created slice User Slice of peiman.
Mar 10 05:38:27 map systemd[1]: Starting User Manager for UID 1000...
Mar 10 05:38:27 map systemd[1]: Started Session 1 of user peiman.
Mar 10 05:38:27 map systemd[1617]: Reached target Timers.
Mar 10 05:38:27 map systemd[1617]: Reached target Paths.
Mar 10 05:38:27 map systemd[1617]: Listening on GnuPG cryptographic agent (ssh-agent emulation).
Mar 10 05:38:27 map systemd[1617]: Listening on GnuPG cryptographic agent and passphrase cache.
Mar 10 05:38:27 map systemd[1617]: Listening on GnuPG cryptographic agent and passphrase cache (restricted).
Mar 10 05:38:27 map systemd[1617]: Listening on GnuPG cryptographic agent and passphrase cache (access for web browsers).
Mar 10 05:38:27 map systemd[1617]: Listening on REST API socket for snapd user session agent.
Mar 10 05:38:27 map systemd[1617]: Listening on GnuPG network certificate management daemon.
Mar 10 05:38:27 map systemd[1617]: Reached target Sockets.
Mar 10 05:38:27 map systemd[1617]: Reached target Basic System.
Mar 10 05:38:27 map systemd[1617]: Reached target Default.
Mar 10 05:38:27 map systemd[1617]: Startup finished in 197ms.
Mar 10 05:38:27 map systemd[1]: Started User Manager for UID 1000.
Mar 10 05:38:19 map systemd-timesyncd[599]: Synchronized to time server 91.189.89.199:123 (ntp.ubuntu.com).
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got incoming connection, fd 7, number 1
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got incoming connection, fd 8, number 2
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got incoming connection, fd 9, number 3
Mar 10 05:39:30 map render_list: DEBUG: Sending render cmd(6 default 0/0/0) with protocol version 2 to fd 4
Mar 10 05:39:30 map render_list: DEBUG: Sending render cmd(6 default 1/0/0) with protocol version 2 to fd 3
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got incoming request with protocol version 2
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got command RenderBulk fd(8) xml(default), z(0), x(0), y(0), mime(image/png), options()
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got incoming request with protocol version 2
Mar 10 05:39:30 map renderd[1559]: Received request for map layer &#39;default&#39; which failed to load
Mar 10 05:39:30 map renderd[1559]: DEBUG: Got command RenderBulk fd(7) xml(default), z(1), x(0), y(0), mime(image/png), options()
Mar 10 05:39:30 map renderd[1559]: DEBUG: Sending render cmd(4 default 0/0/0) with protocol version 2 to fd 8
Mar 10 05:39:30 map renderd[1559]: DEBUG: Failed to read cmd on fd 9
Mar 10 05:39:30 map renderd[1559]: DEBUG: Connection 2, fd 9 closed, now 2 left
Mar 10 05:39:30 map renderd[1559]: Received request for map layer &#39;default&#39; which failed to load
Mar 10 05:39:30 map renderd[1559]: DEBUG: Sending render cmd(4 default 1/0/0) with protocol version 2 to fd 7
Mar 10 05:39:30 map render_list: DEBUG: Got incoming request with protocol version 2
Mar 10 05:39:30 map render_list: DEBUG: Got incoming request with protocol version 2
Mar 10 05:39:40 map renderd[1559]: DEBUG: Failed to read cmd on fd 7
Mar 10 05:39:40 map renderd[1559]: DEBUG: Connection 0, fd 7 closed, now 1 left
Mar 10 05:39:40 map renderd[1559]: DEBUG: Failed to read cmd on fd 8
Mar 10 05:39:40 map renderd[1559]: DEBUG: Connection 0, fd 8 closed, now 0 left</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendered" rel="tag" title="see questions tagged &#39;rendered&#39;">rendered</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '20, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0cc5add59daed413ca657703467678ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peiman2&#39;s gravatar image" />
<p><span>peiman2</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peiman2 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Mar '20, 05:45</strong> </span></p>
</div>
</div>
<div id="comments-container-73447" class="comments-container">
<span id="73451"></span>
<div id="comment-73451" class="comment">
<div id="post-73451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Errors from the renderer will probably be written here:</p>
<pre><code> /var/log/syslog</code></pre>
</div>
<div id="comment-73451-info" class="comment-info">
<span class="comment-age">(09 Mar '20, 23:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73452"></span>
<div id="comment-73452" class="comment">
<div id="post-73452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i added the syslog to my post.thank you</p>
</div>
<div id="comment-73452-info" class="comment-info">
<span class="comment-age">(10 Mar '20, 05:46)</span> <span class="comment-user userinfo">peiman2</span>
</div>
</div>
</div>
<div id="comment-tools-73447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73447-form-container" class="comment-form-container">
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

<span id="73482"></span>

<div id="answer-container-73482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73482-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be the problem:</p>
<pre><code>Mar 10 05:38:17 map renderd[1559]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: FATAL:  role &quot;www-data&quot; does not exist#012Connection string: &#39; dbname=gis connect_timeout=4&#39;</code></pre>
<p>The renderd process runs with user <code>www-data</code>, but that user does not have access to the PostGIS database. So either you have to create a user <code>www-data</code> in the database and grant it access permissions to the data it wants to access, or you have to configure a different, existing database user in the PostgreSQL connection string.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '20, 21:33</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-73482" class="comments-container">
<span id="73483"></span>
<div id="comment-73483" class="comment">
<div id="post-73483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In addition, you seem to be trying to run render_list as root - I'm not sure why.</p>
</div>
<div id="comment-73483-info" class="comment-info">
<span class="comment-age">(11 Mar '20, 21:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73543"></span>
<div id="comment-73543" class="comment">
<div id="post-73543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneElse</a> are talking about <code>sudo</code> or something else? i run command without <code>sudo</code> and also run after <code>su tileserver</code> but nothing changed.</p>
</div>
<div id="comment-73543-info" class="comment-info">
<span class="comment-age">(16 Mar '20, 11:10)</span> <span class="comment-user userinfo">peiman2</span>
</div>
</div>
<span id="73544"></span>
<div id="comment-73544" class="comment">
<div id="post-73544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/409/hfs">@hfs</a> why the renderd process use 'www-data' i added <code>tileserver</code> user for connect to database.also at this point i dont have to use mode_tile.i need to create tile images locally and save them to hard disk.</p>
</div>
<div id="comment-73544-info" class="comment-info">
<span class="comment-age">(16 Mar '20, 11:13)</span> <span class="comment-user userinfo">peiman2</span>
</div>
</div>
<span id="73548"></span>
<div id="comment-73548" class="comment">
<div id="post-73548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, "sudo render_list" will run that command as root. You would almost never want to do that here.</p>
</div>
<div id="comment-73548-info" class="comment-info">
<span class="comment-age">(16 Mar '20, 12:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73482-form-container" class="comment-form-container">
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

