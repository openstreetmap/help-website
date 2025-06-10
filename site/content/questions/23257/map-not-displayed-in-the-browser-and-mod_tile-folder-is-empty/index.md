+++
type = "question"
title = "Map not displayed in the browser and mod_tile folder is empty"
description = '''Hi All, I tried to set MapServer (http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/), the only change was that I replaced planet map with india map (with the same name as planet_osm.pbf). I did all the steps as explained, once rendered and restarted the apache server...on ac...'''
date = "2013-06-12T12:02:00Z"
lastmod = "2014-05-18T10:46:00Z"
weight = 23257
keywords = [ "rendering", "mapserver", "mapnik", "geoserver" ]
aliases = [ "/questions/23257" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Map not displayed in the browser and mod_tile folder is empty](/questions/23257/map-not-displayed-in-the-browser-and-mod_tile-folder-is-empty)

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
<span id="post-23257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23257-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I tried to set MapServer (<a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/),">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/),</a> the only change was that I replaced planet map with india map (with the same name as planet_osm.pbf).</p>
<p>I did all the steps as explained, once rendered and restarted the apache server...on accessing <a href="http://localhost/osm_tiles/0/0/0.png">http://localhost/osm_tiles/0/0/0.png</a> is giving me NOT FOUND ERROR.</p>
<p>When I run "renderd -f -c /usr/local/etc/renderd.conf" I am getting the following console output</p>
<pre><code>sanal@sanal-virtual-machine:~/src/mapnik-style/inc$ renderd -f -c /usr/local/etc/renderd.conf
    renderd[25743]: Rendering daemon started
    renderd[25743]: Initiating reqyest_queue
    renderd[25743]: Parsing section renderd
    renderd[25743]: Parsing render section 0
    renderd[25743]: Parsing section renderd01
    renderd[25743]: Parsing render section 1
    renderd[25743]: Parsing section renderd02
    renderd[25743]: Parsing render section 2
    renderd[25743]: Parsing section mapnik
    renderd[25743]: Parsing section default
    renderd[25743]: Parsing section style2
    renderd[25743]: config renderd: unix socketname=/var/run/renderd/renderd.sock
    renderd[25743]: config renderd: num_threads=4
    renderd[25743]: config renderd: num_slaves=8
    renderd[25743]: config renderd: tile_dir=/var/lib/mod_tile
    renderd[25743]: config renderd: stats_file=/var/run/renderd/renderd.stats
    renderd[25743]: config mapnik:  plugins_dir=/usr/local/lib/mapnik/input
    renderd[25743]: config mapnik:  font_dir=/usr/share/fonts/truetype/ttf-dejavu
    renderd[25743]: config mapnik:  font_dir_recurse=1
    renderd[25743]: config renderd(0): Active
    renderd[25743]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
    renderd[25743]: config renderd(0): num_threads=4
    renderd[25743]: config renderd(0): tile_dir=/var/lib/mod_tile
    renderd[25743]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
    renderd[25743]: config renderd(1): unix socketname=/var/run/renderd/renderd.sock
    renderd[25743]: config renderd(1): num_threads=4
    renderd[25743]: config renderd(1): tile_dir=/var/lib/mod_tile
    renderd[25743]: config renderd(1): stats_file=(null)
    renderd[25743]: config renderd(2): unix socketname=/var/run/renderd/renderd.sock
    renderd[25743]: config renderd(2): num_threads=4
    renderd[25743]: config renderd(2): tile_dir=/var/lib/mod_tile
    renderd[25743]: config renderd(2): stats_file=(null)
    renderd[25743]: config map 0:   name(default) file(/home/sanal/src/mapnik-style/osm.xml) uri(/osm_tiles/) htcp() host(localhost)
    renderd[25743]: config map 1:   name(style2) file() uri() htcp() host()
    renderd[25743]: Initialising unix server socket on /var/run/renderd/renderd.sock
    renderd[25743]: Created server socket 5
    renderd[25743]: Renderd is using mapnik version 3.0.0
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
    renderd[25743]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
    Running in foreground mode...
    renderd[25743]: Starting stats thread
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 6
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 7
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 8
    debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
    debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
    debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 9
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 10
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 11
    renderd[25743]: DEBUG: Got incoming connection, fd 14, number 1
    renderd[25743]: DEBUG: Got incoming connection, fd 15, number 2
    renderd[25743]: DEBUG: Got incoming connection, fd 16, number 3
    renderd[25743]: DEBUG: Got incoming connection, fd 17, number 4
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: DEBUG: Got incoming connection, fd 18, number 5
    renderd[25743]: DEBUG: Got incoming connection, fd 20, number 6
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 19
    renderd[25743]: DEBUG: Got incoming connection, fd 21, number 7
    renderd[25743]: Initialising unix client socket on /var/run/renderd/renderd.sock
    renderd[25743]: socket /var/run/renderd/renderd.sock initialised to fd 22
    renderd[25743]: DEBUG: Got incoming connection, fd 23, number 8
    renderd[25743]: Using web mercator projection settings
    renderd[25743]: Using web mercator projection settings
    renderd[25743]: Using web mercator projection settings
    renderd[25743]: Using web mercator projection settings
&#10;    &gt; Blockquote
    &gt; 
    &gt; Blockquote</code></pre>
<p>and when I restarted apache server it gave me this</p>
<pre><code>    sanal@sanal-virtual-machine:/var/lib$ sudo /etc/init.d/apache2 restart
 * Restarting web server apache2                                                                                         [Wed Jun 12 16:21:35 2013] [warn] module tile_module is already loaded, skipping
[Wed Jun 12 16:21:35 2013] [warn] Could not determine host name of server to configure tile-json request. Using localhost instead
[Wed Jun 12 16:21:35 2013] [notice] Loading tile config default at /osm_tiles/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
[Wed Jun 12 16:21:35 2013] [warn] Could not determine host name of server to configure tile-json request. Using localhost instead
[Wed Jun 12 16:21:35 2013] [notice] Loading tile config style2 at  for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
 ... waiting .[Wed Jun 12 16:21:37 2013] [warn] module tile_module is already loaded, skipping
[Wed Jun 12 16:21:37 2013] [warn] Could not determine host name of server to configure tile-json request. Using localhost instead
[Wed Jun 12 16:21:37 2013] [notice] Loading tile config default at /osm_tiles/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
[Wed Jun 12 16:21:37 2013] [warn] Could not determine host name of server to configure tile-json request. Using localhost instead
[Wed Jun 12 16:21:37 2013] [notice] Loading tile config style2 at  for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png</code></pre>
<p>and my renderd.conf file contents is below</p>
<p>[renderd] socketname=/var/run/renderd/renderd.sock num_threads=4 tile_dir=/var/lib/mod_tile stats_file=/var/run/renderd/renderd.stats</p>
<pre><code>[renderd01]
;iphostname=::1
;ipport=7654
;num_threads=4
;tile_dir=rados://tiles/etc/ceph/ceph.conf
;stats_file=/var/run/renderd/renderd.stats
&#10;[renderd02]
;iphostname=::1
;ipport=7654
;num_threads=8
;tile_dir=memcached://
;stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/local/lib/mapnik/input
font_dir=/usr/share/fonts/truetype/ttf-dejavu
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile
XML=/home/sanal/src/mapnik-style/osm.xml
HOST=localhost
TILESIZE=256
;HTCPHOST=proxy.openstreetmap.org
;MINZOOM=0
;MAXZOOM=18
;TYPE=png image/png
;DESCRIPTION=This is a description of the tile layer used in the tile json request
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/wiki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://opendatacommons.org/licenses/odbl/\&quot;&gt;ODbL&lt;/a&gt;
;SERVER_ALIAS=http://localhost/
;CORS=http://www.openstreetmap.org
&#10;[style2]
;URI=/osm_tiles2/
;TILEDIR=rados://tiles/etc/ceph/ceph.conf
;TILESIZE=512
;XML=/home/jburgess/osm/svn.openstreetmap.org/applications/rendering/mapnik/osm-local2.xml
;HOST=tile.openstreetmap.org
;HTCPHOST=proxy.openstreetmap.org
;MINZOOM=0
;MAXZOOM=22
;TYPE=png image/png
;DESCRIPTION=This is a description of the tile layer used in the tile json request
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/wiki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://opendatacommons.org/licenses/odbl/\&quot;&gt;ODbL&lt;/a&gt;
;SERVER_ALIAS=http://localhost/
;CORS=*</code></pre>
<p>Please help me in fixing this...thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-geoserver" rel="tag" title="see questions tagged &#39;geoserver&#39;">geoserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '13, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/48c18f08bf31cc32ee48a884ae4f62da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanal&#39;s gravatar image" />
<p><span>Sanal</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23257" class="comments-container">
<span id="23259"></span>
<div id="comment-23259" class="comment">
<div id="post-23259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "ls -al /var/lib/mod_tile/" return?</p>
</div>
<div id="comment-23259-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23261"></span>
<div id="comment-23261" class="comment">
<div id="post-23261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have changed the permissions of mod_tile drwxrwxrwx 2 sanal root 4096 Jun 12 10:54 mod_tile</p>
</div>
<div id="comment-23261-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 12:14)</span> <span class="comment-user userinfo">Sanal</span>
</div>
</div>
<span id="23262"></span>
<div id="comment-23262" class="comment">
<div id="post-23262-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That should allow you to write to it, sure! For info what you should see in the renderd debug output in response to browsing to <a href="http://yourserveraddress/osm_tiles/0/0/0.png">http://yourserveraddress/osm_tiles/0/0/0.png</a> is something like:</p>
<pre><code>renderd[16245]: Using web mercator projection settings
renderd[16245]: Using web mercator projection settings
renderd[16245]: Using web mercator projection settings
renderd[16245]: Using web mercator projection settings
renderd[16245]: DEBUG: Got incoming connection, fd 12, number 1
renderd[16245]: DEBUG: Got command Render fd(12) xml(default), z(0), x(0), y(0)
renderd[16245]: DEBUG: START TILE default 0 0-0 0-0, age 19.84 days
renderd[16245]: DEBUG: Connection 0, fd 12 closed, now 0 left
renderd[16245]: DEBUG: DONE TILE default 0 0-0 0-0 in 5.732 seconds
debug: Creating and writing a metatile to /var/lib/mod_tile/default/0/0/0/0/0/0.meta</code></pre>
</div>
<div id="comment-23262-info" class="comment-info">
<span class="comment-age">(12 Jun '13, 12:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23295"></span>
<div id="comment-23295" class="comment">
<div id="post-23295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span></p>
<p>This is the output to</p>
<pre><code>sanal@sanal-virtual-machine:~$ ls -al /var/lib/mod_tile/
total 8
drwxrwxrwx  2 sanal root 4096 Jun 12 10:54 .
drwxr-xr-x 65 root  root 4096 Jun 12 13:19</code></pre>
</div>
<div id="comment-23295-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 04:25)</span> <span class="comment-user userinfo">Sanal</span>
</div>
</div>
<span id="23297"></span>
<div id="comment-23297" class="comment">
<div id="post-23297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>on render the output is</p>
<pre><code>renderd[13603]: Using web mercator projection settings
renderd[13603]: Using web mercator projection settings
renderd[13603]: Using web mercator projection settings
renderd[13603]: DEBUG: Got incoming connection, fd 25, number 9
renderd[13603]: DEBUG: Got command RenderPrio fd(25) xml(default), z(0), x(0), y(0)
renderd[13603]: Dispatching request to slave thread on fd 6
renderd[13603]: DEBUG: Got command Render fd(14) xml(default), z(0), x(0), y(0)
renderd[13603]: DEBUG: Connection 8, fd 25 closed, now 8 left</code></pre>
</div>
<div id="comment-23297-info" class="comment-info">
<span class="comment-age">(13 Jun '13, 04:26)</span> <span class="comment-user userinfo">Sanal</span>
</div>
</div>
<span id="23552"></span>
<div id="comment-23552" class="comment not_top_scorer">
<div id="post-23552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, the next step is probably to try and add some more debug to the rendering code to try and see what's not working.<br />
</p>
<p>Even if you're not a C programmer this needn't be too scary since you should be able to copy some of the existing debug messages, and the "make" instructions are contained on the switch2osm page.</p>
</div>
<div id="comment-23552-info" class="comment-info">
<span class="comment-age">(20 Jun '13, 13:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24819"></span>
<div id="comment-24819" class="comment not_top_scorer">
<div id="post-24819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I m also facing the same problem someone please answer this question</p>
</div>
<div id="comment-24819-info" class="comment-info">
<span class="comment-age">(02 Aug '13, 06:52)</span> <span class="comment-user userinfo">san</span>
</div>
</div>
<span id="30682"></span>
<div id="comment-30682" class="comment not_top_scorer">
<div id="post-30682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i am also having same problem, i did every thing as given in <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> help me to get out of this issue</p>
</div>
<div id="comment-30682-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 12:30)</span> <span class="comment-user userinfo">Arun kmp</span>
</div>
</div>
</div>
<div id="comment-tools-23257" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-23257-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="26104"></span>

<div id="answer-container-26104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26104-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I followed tutorial on osm2switch and installed the server on ubuntu 11.10. but I am also getting the similar problem No output is shown on <a href="http://localhost/osm_tiles/0/0/0.png.">http://localhost/osm_tiles/0/0/0.png.</a> But fortunately maps are available on localhost/osm/slippymap.html page.</p>
<p>Can any body resolve this problem</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '13, 05:15</strong></p>
<img src="https://secure.gravatar.com/avatar/46fe2c2acfb7bcb45ce82c411406d2e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SUKHJIT%20SINGH%20SEHRA&#39;s gravatar image" />
<p><span>SUKHJIT SING...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SUKHJIT SINGH SEHRA has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-26104" class="comments-container">
&#10;</div>
<div id="comment-tools-26104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26104-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27686"></span>

<div id="answer-container-27686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27686-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was having this problem too, but I think I've found the solution.<br />
</p>
<p>The problem is that the tiles are being generated as <a href="http://localhost/osm_tiles/0/0/0.png.">http://localhost/osm_tiles/0/0/0.png.</a> Of course localhost is translated to the machine you're browsing from, so what that should be is <a href="http://tile.mytileserver.org/osm_tiles/0/0/0.png">http://tile.mytileserver.org/osm_tiles/0/0/0.png</a> or <a href="http://10.10.10.10/osm_tiles/0/0/0.png.">http://10.10.10.10/osm_tiles/0/0/0.png.</a></p>
<p>So first thing to do is to set your hostname. I used tile.mytileserver.org eg nano /etc/hostname -&gt; tile.mytileserver.org hostname -F /etc/hostname nano /etc/hosts -&gt; tile.mytileserver.org</p>
<p>Then change the value for &lt;paraeter name="host"&gt;&lt;/parameter&gt; in /etc/mapnik-osm-data/inc/datasource-settings.xml.inc</p>
<p>If you're using slippymap.html, open that at /var/www/osm/slippymap.html and change localhost to tile.mytileserver.org</p>
<p>Previously I tried changing the HOST parameter in /etc/renderd.conf and the Server parameter in /etc/apache2/sites-enabled/tileserver-site so if the above doesn't work, you might want to look at those too.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '13, 04:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ea8055d4c79c7fc1838076887670b188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plutocrat&#39;s gravatar image" />
<p><span>Plutocrat</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plutocrat has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '13, 04:26</strong> </span></p>
</div>
</div>
<div id="comments-container-27686" class="comments-container">
&#10;</div>
<div id="comment-tools-27686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27686-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33257"></span>

<div id="answer-container-33257" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33257-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No one have an answer for this question... so many threads, no answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '14, 06:55</strong></p>
<img src="https://secure.gravatar.com/avatar/98a3cef6fd42a9093690c87d2eed2777?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexlana&#39;s gravatar image" />
<p><span>alexlana</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexlana has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33257" class="comments-container">
<span id="33259"></span>
<div id="comment-33259" class="comment">
<div id="post-33259-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are a large number of possible reasons why it might not work: software versions in different distributions, permissions in various places, missing fonts (depending on machine setup), possible apache issues such as the one that <span>@Plutocrat</span> above mentioned, and more.</p>
<p>It's probably easiest to create a wiki page behind your user page describing what you've done, what you've tried and what still doesn't work, and then asking on IRC (#osm should have people with some experience of tile server setup; if it doesn't then try #osm=dev).</p>
</div>
<div id="comment-33259-info" class="comment-info">
<span class="comment-age">(17 May '14, 10:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33284"></span>
<div id="comment-33284" class="comment">
<div id="post-33284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it can be anything. The problem is that I am not a programer, and this issue took me all my week and weekend, my nights... it's a beautiful project, but it's useless for designers, business people, someone looking for fun... and it's only because nobody think about the layer that reach non-programers. All what I need is some healthy image to download and use on Virtualbox... like that: <a href="http://tek.io/1ge1kuq">http://tek.io/1ge1kuq</a></p>
<p>Sorry if it is not the right place for post that, but after dozens of installations, searches on google, Virtualbox snapshots, log reads... I quit...</p>
</div>
<div id="comment-33284-info" class="comment-info">
<span class="comment-age">(18 May '14, 08:23)</span> <span class="comment-user userinfo">alexlana</span>
</div>
</div>
<span id="33287"></span>
<div id="comment-33287" class="comment">
<div id="post-33287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@alexlana</span> - the reason why I suggested IRC is that it allows faster communication with people trying to help. Asking here is not wrong, (better as a new question than as an "answer" to a previous one though) but it wouldn't be as fast a conversation.</p>
<p>However, we don't actually know what <em>your</em> problem is yet (beyond "it doesn't work"). That's why I suggested putting some details together explaining it.</p>
</div>
<div id="comment-33287-info" class="comment-info">
<span class="comment-age">(18 May '14, 10:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33257-form-container" class="comment-form-container">
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

