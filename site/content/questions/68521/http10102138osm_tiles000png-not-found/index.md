+++
type = "question"
title = "http://10.10.21.38/osm_tiles/0/0/0.png not found"
description = '''tail -f /var/log/apache2/error.log Thu Mar 28 07:35:03.001960 2019] [mpm_prefork:notice] [pid 12824] AH00163: Apache/2.4.18 (Ubuntu) configured -- resuming normal operations [Thu Mar 28 07:35:03.001998 2019] [core:notice] [pid 12824] AH00094: Command line: &#x27;/usr/sbin/apache2&#x27; [Thu Mar 28 10:55:33.88...'''
date = "2019-03-28T05:34:00Z"
lastmod = "2019-03-28T05:34:00Z"
weight = 68521
keywords = [ "apache", "openstreetmap", "osm2pgsql", "mapnik", "mod_tile" ]
aliases = [ "/questions/68521" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [http://10.10.21.38/osm_tiles/0/0/0.png not found](/questions/68521/http10102138osm_tiles000png-not-found)

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
<span id="post-68521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>tail -f /var/log/apache2/error.log</p>
<pre><code>Thu Mar 28 07:35:03.001960 2019] [mpm_prefork:notice] [pid 12824] AH00163: Apache/2.4.18 (Ubuntu) configured -- resuming normal operations
[Thu Mar 28 07:35:03.001998 2019] [core:notice] [pid 12824] AH00094: Command line: &#39;/usr/sbin/apache2&#39;
[Thu Mar 28 10:55:33.880692 2019] [mpm_prefork:notice] [pid 12824] AH00171: Graceful restart requested, doing restart
[Thu Mar 28 10:55:33.956871 2019] [so:warn] [pid 12824] AH01574: module tile_module is already loaded, skipping
[Thu Mar 28 10:55:33.959605 2019] [tile:notice] [pid 12824] Loading tile config default at /osm_tiles/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png
[Thu Mar 28 10:55:33.959645 2019] [tile:notice] [pid 12824] Loading tile config default at /osm_tiles/  for zooms 0 - 20 from tile directory /var/lib/mod_tile/ with extension .png and mime type image/png
AH00558: apache2: Could not reliably determine the server&#39;s fully qualified domain name, using 127.0.1.1. Set the &#39;ServerName&#39; directive globally to suppress this message
[Thu Mar 28 10:55:34.000252 2019] [mpm_prefork:notice] [pid 12824] AH00163: Apache/2.4.18 (Ubuntu) configured -- resuming normal operations
[Thu Mar 28 10:55:34.000286 2019] [core:notice] [pid 12824] AH00094: Command line: &#39;/usr/sbin/apache2&#39;</code></pre>
<p>/etc/apache2/sites-enabled/osm_tiles.conf*</p>
<pre><code>&lt;VirtualHost *:80&gt;
&#10;        ServerName 10.10.21.38
        ServerAdmin webmaster@10.10.21.38
&#10;                  CustomLog /var/log/apache2/default_access.log common
                  ErrorLog /var/log/apache2/default_error.log
&#10;                  LoadModule tile_module /usr/lib/apache2/modules/mod_tile.so
&#10;                  AddTileConfig /osm_tiles/ default
                  LoadTileConfigFile /usr/local/etc/renderd.conf
                  ModTileTileDir /var/lib/mod_tile
                  ModTileRenderdSocketName /var/run/renderd/renderd.sock
                  ModTileRequestTimeout 0
                  ModTileMissingRequestTimeout 30
&#10;
                  DocumentRoot &quot;/var/www/osm_tiles/&quot;
&#10;                  &lt;Directory &quot;/var/www/osm_tiles/&quot;&gt;
                          AllowOverride None
                          Options None
                          Order allow,deny
                          Allow from all
                  &lt;/Directory&gt;
&#10;                  Alias /osm_tiles &quot;/var/www/osm_tiles&quot;
&#10;                  &lt;Directory &quot;/var/www/osm_tiles/&quot;&gt;
                          AllowOverride None
                          Options None
                          Order allow,deny
                    &lt;/Directory&gt;
&#10;                  LogLevel debug
&lt;/VirtualHost&gt;</code></pre>
<p>/usr/local/etc/renderd.conf</p>
<pre><code>[renderd]
socketname=/var/run/renderd/renderd.sock
num_threads=4
tile_dir=/var/lib/mod_tile/
stats_file=/var/run/renderd/renderd.stats
&#10;;[renderd01]
;iphostname=::1
;ipport=7654
;num_threads=4
;tile_dir=rados://tiles/etc/ceph/ceph.conf
;stats_file=/var/run/renderd/renderd.stats
&#10;;[renderd02]
;iphostname=::1
;ipport=7654
;num_threads=8
;tile_dir=memcached://
;stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input/
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[default]
URI=/osm_tiles/
TILEDIR=/var/lib/mod_tile/
XML=/home/osm/openstreetmap-carto-2.41.0/style.xml
HOST=10.10.21.38
TILESIZE=256
&#10;;HTCPHOST=proxy.openstreetmap.org
;** config options used by mod_tile, but not renderd **
;MINZOOM=0
;MAXZOOM=18
;TYPE=png image/png
;DESCRIPTION=This is a description of the tile layer used in the tile json request
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/wiki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://opendatacommons.org/licenses/odbl/\&quot;&gt;ODbL&lt;/a&gt;
;SERVER_ALIAS=http://localhost/
;CORS=http://www.openstreetmap.org
;ASPECTX=1
;ASPECTY=1
;SCALE=1.0
&#10;;[style2]
;URI=/osm_tiles2/
;TILEDIR=rados://tiles/etc/ceph/ceph.conf
;TILESIZE=512
;XML=/home/jburgess/osm/svn.openstreetmap.org/applications/rendering/mapnik/osm-local2.xml
;HOST=10.10.21.38
;HTCPHOST=proxy.openstreetmap.org
;** config options used by mod_tile, but not renderd **
;MINZOOM=0
;MAXZOOM=22
;TYPE=png image/png
;DESCRIPTION=This is a description of the tile layer used in the tile json request
;ATTRIBUTION=&amp;copy;&lt;a href=\&quot;http://www.openstreetmap.org/\&quot;&gt;OpenStreetMap&lt;/a&gt; and &lt;a href=\&quot;http://wiki.openstreetmap.org/wiki/Contributors\&quot;&gt;contributors&lt;/a&gt;, &lt;a href=\&quot;http://opendatacommons.org/licenses/odbl/\&quot;&gt;ODbL&lt;/a&gt;
;SERVER_ALIAS=http://localhost/
;CORS=*</code></pre>
<p>anyone can you please me on this?</p>
<p>Thanks in advanced.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '19, 05:34</strong></p>
<img src="https://secure.gravatar.com/avatar/fe2dd96c7d6ccf79f5bfc448d6771ecd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vinod%20sisodiya&#39;s gravatar image" />
<p><span>vinod sisodiya</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vinod sisodiya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '19, 07:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68521" class="comments-container">
&#10;</div>
<div id="comment-tools-68521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68521-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

