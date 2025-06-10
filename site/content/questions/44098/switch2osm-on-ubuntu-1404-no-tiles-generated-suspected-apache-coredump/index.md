+++
type = "question"
title = "Switch2osm on Ubuntu 14:04: No tiles generated, suspected Apache coredump"
description = '''Hey guys, I am trying to roll out my pc as an osm server. I followed the tutorial https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ On giving the renderd command, it gives no error. It gives this: sudo -u daman renderd -f -c /usr/local/etc/renderd.conf renderd[26034]: Rende...'''
date = "2015-07-10T07:47:00Z"
lastmod = "2015-07-24T15:02:00Z"
weight = 44098
keywords = [ "renderd", "mod_tile" ]
aliases = [ "/questions/44098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Switch2osm on Ubuntu 14:04: No tiles generated, suspected Apache coredump](/questions/44098/switch2osm-on-ubuntu-1404-no-tiles-generated-suspected-apache-coredump)

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
<span id="post-44098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44098-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys, I am trying to roll out my pc as an osm server. I followed the tutorial <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> On giving the renderd command, it gives no error. It gives this:</p>
<pre><code>sudo -u daman renderd -f -c /usr/local/etc/renderd.conf
renderd[26034]: Rendering daemon started
renderd[26034]: Initiating reqyest_queue
renderd[26034]: Parsing section renderd
renderd[26034]: Parsing render section 0
renderd[26034]: Parsing section renderd01
renderd[26034]: Parsing render section 1
renderd[26034]: Parsing section renderd02
renderd[26034]: Parsing render section 2
renderd[26034]: Parsing section mapnik
renderd[26034]: Parsing section default
renderd[26034]: Parsing section style2
renderd[26034]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[26034]: config renderd: num_threads=4
renderd[26034]: config renderd: num_slaves=8
renderd[26034]: config renderd: tile_dir=/var/lib/mod_tile
renderd[26034]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[26034]: config mapnik:  plugins_dir=/usr/local/lib/mapnik/input
renderd[26034]: config mapnik:  font_dir=/usr/share/fonts/truetype/ttf-dejavu
renderd[26034]: config mapnik:  font_dir_recurse=1
renderd[26034]: config renderd(0): Active
renderd[26034]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[26034]: config renderd(0): num_threads=4
renderd[26034]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[26034]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[26034]: config renderd(1): unix socketname=/var/run/renderd/renderd.sock
renderd[26034]: config renderd(1): num_threads=4
renderd[26034]: config renderd(1): tile_dir=/var/lib/mod_tile
renderd[26034]: config renderd(1): stats_file=(null)
renderd[26034]: config renderd(2): unix socketname=/var/run/renderd/renderd.sock
renderd[26034]: config renderd(2): num_threads=4
renderd[26034]: config renderd(2): tile_dir=/var/lib/mod_tile
renderd[26034]: config renderd(2): stats_file=(null)
renderd[26034]: config map 0:   name(default) file(/usr/local/share/maps/style/OSMBright/OSMBright.xml) uri(/osm_tiles/) htcp() host(localhost)
renderd[26034]: config map 1:   name(style2) file(/usr/local/share/maps/style/OSMBright/OSMBright.xml) uri() htcp() host()
renderd[26034]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[26034]: Created server socket 4
renderd[26034]: Renderd is using mapnik version 2.2.0
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[26034]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
Running in foreground mode...
renderd[26034]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Loading parameterization function for 
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sockrenderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 5
&#10;debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 7
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 6
renderd[26034]: Loading parameterization function for 
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 11
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 12
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 13
renderd[26034]: DEBUG: Got incoming connection, fd 17, number 1
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: DEBUG: Got incoming connection, fd 18, number 2
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 19
renderd[26034]: DEBUG: Got incoming connection, fd 20, number 3
renderd[26034]: DEBUG: Got incoming connection, fd 21, number 4
renderd[26034]: DEBUG: Got incoming connection, fd 22, number 5
renderd[26034]: DEBUG: Got incoming connection, fd 23, number 6
renderd[26034]: DEBUG: Got incoming connection, fd 24, number 7
renderd[26034]: Initialising unix client socket on /var/run/renderd/renderd.sock
renderd[26034]: DEBUG: Got incoming connection, fd 26, number 8
renderd[26034]: socket /var/run/renderd/renderd.sock initialised to fd 25
renderd[26034]: Using web mercator projection settings
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Using web mercator projection settings
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Using web mercator projection settings
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Using web mercator projection settings
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[26034]: Loading parameterization function for 
renderd[26034]: Using web mercator projection settings
renderd[26034]: Using web mercator projection settings
renderd[26034]: Using web mercator projection settings
renderd[26034]: Using web mercator projection settings
renderd[26034]: DEBUG: Got incoming connection, fd 8, number 9
renderd[26034]: DEBUG: Got incoming request with protocol version 2
renderd[26034]: DEBUG: Got command RenderPrio fd(8) xml(default), z(0), x(0), y(0), mime(image/png), options()
renderd[26034]: Dispatching request to slave thread on fd 5
renderd[26034]: DEBUG: Sending render cmd(1 default 0/0/0) with protocol version 3 to fd 5
renderd[26034]: DEBUG: Got incoming request with protocol version 3
renderd[26034]: DEBUG: Got command Render fd(17) xml(default), z(0), x(0), y(0), mime(image/png), options()
renderd[26034]: DEBUG: Failed to read cmd on fd 8
renderd[26034]: DEBUG: Connection 8, fd 8 closed, now 8 left</code></pre>
<p>Even the mod_tile folder is empty. On accessing <a href="http://localhost/osm_tiles/0/0/0.png">http://localhost/osm_tiles/0/0/0.png</a> It gives a 404 not found error Please help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '15, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/7e202335a05627a96a9a2c4fc084f535?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DamBatra&#39;s gravatar image" />
<p><span>DamBatra</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DamBatra has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '15, 14:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-44098" class="comments-container">
<span id="44122"></span>
<div id="comment-44122" class="comment">
<div id="post-44122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked my apache error.log file. It is giving me a coredump message: [core:error] [pid 1688:tid 140121667135360] AH00546: no record of generation 0 of exiting child 22589 [Thu Jul 09 18:29:53.015305 2015] [core:notice] [pid 1688:tid 140121667135360] AH00051: child pid 22590 exit signal Segmentation fault (11), possible coredump in /etc/apache2</p>
</div>
<div id="comment-44122-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 20:11)</span> <span class="comment-user userinfo">DamBatra</span>
</div>
</div>
</div>
<div id="comment-tools-44098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44098-form-container" class="comment-form-container">
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

<span id="44409"></span>

<div id="answer-container-44409" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without knowing the context of what causes Apache to fail, I have no idea.</p>
<p>What would really be needed would be a record of everything that you did. It's all very well saying "I followed XYZ guide" but when other people do this they don't get the same problem, and so there must be something different about your configuration. What would help people diagnose this would be you posted exactly what you did, and what results came back, in a pastebin somewhere and linked to that from here. Currently we simply don't know what you did to get to where you are now.</p>
<p>It's also worth describing what you're running this on - what hardware or VM? How much memory, how much disk?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '15, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-44409" class="comments-container">
&#10;</div>
<div id="comment-tools-44409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44409-form-container" class="comment-form-container">
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

