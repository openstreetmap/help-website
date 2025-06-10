+++
type = "question"
title = "Configuring mod_tile and renderd for memcache"
description = '''I have my mod_tile.config set up like this # This is the Apache server configuration file for providing OSM tile support # through mod_tile  LoadModule tile_module modules/mod_tile.so  &amp;lt;VirtualHost *:80&amp;gt;  ServerName tile.openstreetmap.org  ServerAlias a.tile.openstreetmap.org b.tile.openstreet...'''
date = "2018-06-20T23:03:00Z"
lastmod = "2018-06-21T18:32:00Z"
weight = 64291
keywords = [ "renderd", "memcache", "configuration", "mod_tile" ]
aliases = [ "/questions/64291" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Configuring mod_tile and renderd for memcache](/questions/64291/configuring-mod_tile-and-renderd-for-memcache)

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
<span id="post-64291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have my mod_tile.config set up like this</p>
<pre><code># This is the Apache server configuration file for providing OSM tile support
# through mod_tile
&#10;LoadModule tile_module modules/mod_tile.so
&#10;&lt;VirtualHost *:80&gt;
    ServerName tile.openstreetmap.org
    ServerAlias a.tile.openstreetmap.org b.tile.openstreetmap.org c.tile.openstreetmap.org d.tile.openstreetmap.org
    DocumentRoot /var/www/html
&#10;# Specify the default base storage path for where tiles live. A number of different storage backends
# are available, that can be used for storing tiles.  Currently these are a file based storage, a memcached
# based storage and a RADOS based storage.
# The file based storage uses a simple file path as its storage path ( /path/to/tiledir )
# The RADOS based storage takes a location to the rados config file and a pool name ( rados://poolname/path/to/ceph.conf )
# The memcached based storage currently has no configuration options and always connects to memcached on localhost ( memcached:// )
#
# The storage path can be overwritten on a style by style basis from the style TileConfigFile
    ModTileTileDir memcached://
...</code></pre>
<p>and my renderd.config set up like this</p>
<pre><code>[renderd]
num_threads=4
tile_dir=memcached://localhost:11211
stats_file=/var/run/renderd/renderd.stats
&#10;[mapnik]
plugins_dir=/usr/lib/mapnik/3.0/input
font_dir=/usr/share/fonts/truetype
font_dir_recurse=1
&#10;[ajt]
URI=/hot/
TILEDIR=memcached://localhost:11211
XML=/home/renderaccount/src/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256
MAXZOOM=20</code></pre>
<p>yet I am receiving this error:</p>
<pre><code>renderd[10095]: Loading parameterization function for debug: init_storage_backend: initialising memcached storage backend at: memcached://
ERROR: init_storage_memcached: Support for memcached has not been compiled into this program</code></pre>
<p>How do I compile support for memcached into mod_tile and renderd?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-memcache" rel="tag" title="see questions tagged &#39;memcache&#39;">memcache</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '18, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/4a389be371e807913bffdbe1b2a9d671?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willAirtory&#39;s gravatar image" />
<p><span>willAirtory</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willAirtory has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jun '18, 23:56</strong> </span></p>
</div>
</div>
<div id="comments-container-64291" class="comments-container">
&#10;</div>
<div id="comment-tools-64291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64291-form-container" class="comment-form-container">
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

<span id="64310"></span>

<div id="answer-container-64310" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64310-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Fixed by adding libmemcached and then restarting apache and my rendering system.</p>
<pre><code>sudo apt-get update
sudo apt-get install -y libmemcached-tools libmemcached-dev libmemcached11
sudo service apache2 restart
sudo service renderd restart</code></pre>
<p>The rest of the way I configured my system works well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '18, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/4a389be371e807913bffdbe1b2a9d671?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willAirtory&#39;s gravatar image" />
<p><span>willAirtory</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willAirtory has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '18, 18:33</strong> </span></p>
</div>
</div>
<div id="comments-container-64310" class="comments-container">
&#10;</div>
<div id="comment-tools-64310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64310-form-container" class="comment-form-container">
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

