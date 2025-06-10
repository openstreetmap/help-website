+++
type = "question"
title = "mod_tile/renderd register_datasource segfault mapnik2.1"
description = '''Hi  mod_tile (renderd) is working with mapnik 2.0, but failing with a higher mapnik release like mapnik2.1 I get an segementation fault when we try to register the datatsource kismet.input. Do you know why? $ /usr/local/bin/renderd -f -c /etc/renderd.conf renderd[17548]: Rendering daemon started ren...'''
date = "2014-04-23T09:24:00Z"
lastmod = "2014-04-23T13:49:00Z"
weight = 32550
keywords = [ "segfault" ]
aliases = [ "/questions/32550" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mod_tile/renderd register_datasource segfault mapnik2.1](/questions/32550/mod_tilerenderd-register_datasource-segfault-mapnik21)

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
<span id="post-32550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32550-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>mod_tile (renderd) is working with mapnik 2.0, but failing with a higher mapnik release like mapnik2.1 I get an segementation fault when we try to register the datatsource kismet.input. Do you know why?</p>
<pre><code>$ /usr/local/bin/renderd -f  -c /etc/renderd.conf
renderd[17548]: Rendering daemon started
renderd[17548]: Initiating reqyest_queue
renderd[17548]: Parsing section renderd
renderd[17548]: Parsing render section 0
renderd[17548]: Parsing section mapnik
renderd[17548]: Parsing section default
renderd[17548]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[17548]: config renderd: num_threads=4
renderd[17548]: config renderd: num_slaves=0
renderd[17548]: config renderd: tile_dir=/var/lib/mod_tile
renderd[17548]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[17548]: config mapnik:  plugins_dir=/usr/lib/mapnik/input
renderd[17548]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[17548]: config mapnik:  font_dir_recurse=1
renderd[17548]: config renderd(0): Active
renderd[17548]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[17548]: config renderd(0): num_threads=4
renderd[17548]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[17548]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[17548]: config map 0:   name(default) file(/home/myuser/src/mapnik-style/mapnik.xml) uri(/osm_tiles/) htcp() host(localhost)
renderd[17548]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[17548]: Created server socket 4
renderd[17548]: Renderd is using mapnik version 2.1.1
renderd[17548]: register datasource /usr/lib/mapnik/input
renderd[17548]: instance found
Segmentation fault (core dumped)
&#10;Program received signal SIGSEGV, Segmentation fault.
0x00007ffff6c81a58 in std::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;::basic_string(char const*, std::allocator&lt;char&gt; const&amp;) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6                                                                         │debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
(gdb) bt
#0  0x00007ffff6c81a58 in std::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;::basic_string(char const*, std::allocator&lt;char&gt; const&amp;) () from /usr/lib/x86_64-linux-gnu/libstdc++.so.6
#1  0x00007fffebd9dbb9 in kismet_datasource::name() () from /usr/lib/mapnik/input/kismet.input
#2  0x00007fffebd9dbd9 in datasource_name () from /usr/lib/mapnik/input/kismet.input
#3  0x00007ffff791effb in mapnik::datasource_cache::register_datasource(std::string const&amp;) () from /usr/local/lib/libmapnik.so.2.1
#4  0x00007ffff791f3f0 in mapnik::datasource_cache::register_datasources(std::string const&amp;) () from /usr/local/lib/libmapnik.so.2.1
#5  0x0000000000407dfb in render_init (plugins_dir=0x620cc0 &quot;/usr/lib/mapnik/input&quot;, font_dir=0x620d00 &quot;/usr/share/fonts/truetype&quot;,font_dir_recurse=1) at src/gen_tile.cpp:318 
#6  0x0000000000405d1c in main (argc=&lt;optimized out&gt;, argv=&lt;optimized out&gt;) at src/daemon.c:906
(gdb)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segfault" rel="tag" title="see questions tagged &#39;segfault&#39;">segfault</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '14, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/3f5cc321ad7349ecfe706b4ccdc6a1e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wqeqew&#39;s gravatar image" />
<p><span>wqeqew</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wqeqew has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32550" class="comments-container">
&#10;</div>
<div id="comment-tools-32550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32550-form-container" class="comment-form-container">
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

<span id="32565"></span>

<div id="answer-container-32565" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32565-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>found the problem.</p>
<p>I had the wrong input path in /etc/rendered.conf</p>
<pre><code>...
[mapnik]
#plugins_dir=/usr/lib/mapnik/input       # for mapnik_2.0
plugins_dir=/usr/local/lib/mapnik/input  # &gt;=  mapnik_2.1 (has not kismet.input)
...</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '14, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/3f5cc321ad7349ecfe706b4ccdc6a1e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wqeqew&#39;s gravatar image" />
<p><span>wqeqew</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wqeqew has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32565" class="comments-container">
&#10;</div>
<div id="comment-tools-32565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32565-form-container" class="comment-form-container">
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

