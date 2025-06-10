+++
type = "question"
title = "Segmentation fault on a command &quot;sudo -u taras renderd -f -c /usr/local/etc/renderd.conf&quot;"
description = '''I am new to Apache technologies and renderd. I am following stages written in a manual: switch2osm | Manually building a tile server (16.04.2 LTS). But on a stage of &quot;Running renderd for the first time&quot; I got problems. When I execute next command sudo -u taras renderd -f -c /usr/local/etc/renderd.co...'''
date = "2017-07-13T10:23:00Z"
lastmod = "2017-07-13T14:53:00Z"
weight = 57052
keywords = [ "apache", "renderd", "ubuntu", "switch2osm", "tileserver" ]
aliases = [ "/questions/57052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Segmentation fault on a command "sudo -u taras renderd -f -c /usr/local/etc/renderd.conf"](/questions/57052/segmentation-fault-on-a-command-sudo-u-taras-renderd-f-c-usrlocaletcrenderdconf)

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
<span id="post-57052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to Apache technologies and renderd. I am following stages written in a manual: <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">switch2osm | Manually building a tile server (16.04.2 LTS)</a>.</p>
<p>But on a stage of <code>"Running renderd for the first time"</code> I got problems.</p>
<p>When I execute next command <code>sudo -u taras renderd -f -c /usr/local/etc/renderd.conf</code> I received next reply in my Terminal:</p>
<pre><code>renderd[24791]: Rendering daemon started
renderd[24791]: Initiating reqyest_queue
renderd[24791]: Parsing section renderd
renderd[24791]: Parsing render section 0
renderd[24791]: Parsing section mapnik
renderd[24791]: Parsing section ajt
renderd[24791]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[24791]: config renderd: num_threads=2
renderd[24791]: config renderd: num_slaves=0
renderd[24791]: config renderd: tile_dir=/var/lib/mod_tile
renderd[24791]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[24791]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[24791]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[24791]: config mapnik:  font_dir_recurse=1
renderd[24791]: config renderd(0): Active
renderd[24791]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[24791]: config renderd(0): num_threads=2
renderd[24791]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[24791]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[24791]: config map 0:   name(ajt) file(/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[24791]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[24791]: Created server socket 5
renderd[24791]: Renderd is using mapnik version 2.2.0
renderd[24791]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-punjabi/Lohit-Punjabi.ttf
... (some very similar code with no errors)
renderd[24791]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-Bold.ttf
renderd[24791]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa.ttf
renderd[24791]: DEBUG: Loading font: /usr/share/fonts/truetype/olga/GFSOlga.otf
Running in foreground mode...
renderd[24791]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[24791]: Loading parameterization function for 
renderd[24791]: Loading parameterization function for 
**Segmentation fault**</code></pre>
<p>What does it mean Segmentation fault and what should I do?</p>
<p>Also, when I open my browser <a href="http://130.89.234.165/mod_tile/0/0/0.png">http://myIP/mod_tile/0/0/0.png</a> I got the next reply on the black background: <code>The image “</code><a href="http://myIP/mod_tile/0/0/0.png”"><code>http://myIP/mod_tile/0/0/0.png”</code></a><code> cannot be displayed, because it contains errors.</code></p>
<p>After execution of the next code: <code>sudo -u taras gdb -batch -ex run -ex bt --args renderd -f -c /usr/local/etc/renderd.conf</code> I received a long reply from a system, where 12 issues are indicated:</p>
<pre><code>[Thread debugging using libthread_db enabled]
Using host libthread_db library &quot;/lib/x86_64-linux-gnu/libthread_db.so.1&quot;.
renderd[15977]: Rendering daemon started
renderd[15977]: Initiating reqyest_queue
renderd[15977]: Parsing section renderd
renderd[15977]: Parsing render section 0
renderd[15977]: Parsing section mapnik
renderd[15977]: Parsing section ajt
renderd[15977]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[15977]: config renderd: num_threads=4
renderd[15977]: config renderd: num_slaves=0
renderd[15977]: config renderd: tile_dir=/var/lib/mod_tile
renderd[15977]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[15977]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[15977]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[15977]: config mapnik:  font_dir_recurse=1
renderd[15977]: config renderd(0): Active
renderd[15977]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[15977]: config renderd(0): num_threads=4
renderd[15977]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[15977]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[15977]: config map 0:   name(ajt) file(/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[15977]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[15977]: Created server socket 5
renderd[15977]: Renderd is using mapnik version 2.2.0
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-punjabi/Lohit-Punjabi.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/didot-classic/GFSDidotClassic.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond12-Italic.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond-InitialsF2.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond-Initials.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond08-Regular.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond08-SC.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond-InitialsF1.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond08-Italic.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/GilliusADF-Regular.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/AccanthisADFStdNo3-Italic.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/GilliusADFNo2-Bold.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/AccanthisADFStdNo2-Bold.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/AccanthisADFStdNo3-BoldItalic.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/AccanthisADFStd-Regular.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/GilliusADFNo2Cd-Italic.otf
renderd[15977]: DEBUG: Loading font: /usr/share/fonts/truetype/adf/UniversalisADFStd-BoldOblique.otf
(...everything abount fonts..I skip this long part)
Running in foreground mode...
[New Thread 0x7fffdd164700 (LWP 15981)]
renderd[15977]: Starting stats thread
[New Thread 0x7fffdc963700 (LWP 15982)]
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[15977]: Loading parameterization function for 
[New Thread 0x7fffd7fff700 (LWP 15983)]
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[15977]: Loading parameterization function for 
[New Thread 0x7fffd77fe700 (LWP 15984)]
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[15977]: Loading parameterization function for 
[New Thread 0x7fffd6ffd700 (LWP 15985)]
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[15977]: Loading parameterization function for
&#10;Thread 3 &quot;renderd&quot; received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7fffdc963700 (LWP 15982)]
0x00007ffff7910700 in std::pair&lt;boost::unordered::iterator_detail::iterator&lt;boost::unordered::detail::ptr_node&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; &gt;, bool&gt; boost::unordered::detail::table_impl&lt;boost::unordered::detail::map&lt;std::allocator&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt;, boost::hash&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; &gt;, std::equal_to&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; &gt; &gt; &gt;::emplace_impl&lt;boost::unordered::detail::emplace_args1&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; &gt;(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, boost::unordered::detail::emplace_args1&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; const&amp;) () from /usr/local/lib/libmapnik.so.2.2
#0  0x00007ffff7910700 in std::pair&lt;boost::unordered::iterator_detail::iterator&lt;boost::unordered::detail::ptr_node&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; &gt;, bool&gt; boost::unordered::detail::table_impl&lt;boost::unordered::detail::map&lt;std::allocator&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt;, boost::hash&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; &gt;, std::equal_to&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; &gt; &gt; &gt;::emplace_impl&lt;boost::unordered::detail::emplace_args1&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; &gt;(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, boost::unordered::detail::emplace_args1&lt;std::pair&lt;std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const, boost::shared_ptr&lt;boost::interprocess::mapped_region&gt; &gt; &gt; const&amp;) () from /usr/local/lib/libmapnik.so.2.2
&#10;#1  0x00007ffff790dd57 in mapnik::mapped_memory_cache::find(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool) () from /usr/local/lib/libmapnik.so.2.2
#2  0x00007fffe983858b in shape_io::shape_io(std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool) () from /usr/lib/mapnik/3.0/input/shape.input
#3  0x00007fffe982bfce in shape_datasource::shape_datasource(mapnik::parameters const&amp;) () from /usr/lib/mapnik/3.0/input/shape.input
#4  0x00007fffe982d581 in create () from /usr/lib/mapnik/3.0/input/shape.input
#5  0x00007ffff78327ce in mapnik::datasource_cache::create(mapnik::parameters const&amp;) () from /usr/local/lib/libmapnik.so.2.2
#6  0x00007ffff789caaf in mapnik::map_parser::parse_layer(mapnik::Map&amp;, mapnik::xml_node const&amp;) () from /usr/local/lib/libmapnik.so.2.2
#7  0x00007ffff78a1864 in mapnik::map_parser::parse_map_include(mapnik::Map&amp;, mapnik::xml_node const&amp;) () from /usr/local/lib/libmapnik.so.2.2
#8  0x00007ffff78a35f6 in mapnik::map_parser::parse_map(mapnik::Map&amp;, mapnik::xml_node const&amp;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;) () from /usr/local/lib/libmapnik.so.2.2
#9  0x00007ffff78a44a1 in mapnik::load_map(mapnik::Map&amp;, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, bool, std::__cxx11::basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt;) () from /usr/local/lib/libmapnik.so.2.2
#10 0x000000000040a334 in render_thread (arg=&lt;optimised out&gt;) at src/gen_tile.cpp:361
#11 0x00007ffff665e6ba in start_thread (arg=0x7fffdc963700) at pthread_create.c:333
#12 0x00007ffff63943dd in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '17, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/3961e27939d00a1f4a6fe22992fc3809?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taras&#39;s gravatar image" />
<p><span>taras</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taras has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '19, 10:11</strong> </span></p>
</div>
</div>
<div id="comments-container-57052" class="comments-container">
<span id="57053"></span>
<div id="comment-57053" class="comment">
<div id="post-57053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Per <a href="https://github.com/openstreetmap/mod_tile/issues/165#issuecomment-315023234">https://github.com/openstreetmap/mod_tile/issues/165#issuecomment-315023234</a> (which I suspect overlapped with you asking here) - what OS and version are you using and are there any other variations from the switch2osm guide?</p>
</div>
<div id="comment-57053-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57054"></span>
<div id="comment-57054" class="comment">
<div id="post-57054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for reply. Could you be so kind and specify what do you mean by "OS and version", please? I want to be as specific as possible for other people and write explicit question.</p>
</div>
<div id="comment-57054-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:49)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57055"></span>
<div id="comment-57055" class="comment">
<div id="post-57055-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I followed the switch2osm guide one in one. I succeeded with everything that was before in that guide.</p>
</div>
<div id="comment-57055-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:52)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57056"></span>
<div id="comment-57056" class="comment">
<div id="post-57056-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am using Ubuntu 16.04 LTS, does it make any sense?</p>
</div>
<div id="comment-57056-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:53)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57057"></span>
<div id="comment-57057" class="comment">
<div id="post-57057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(your second comment answers it, but just to clarify) I was wondering whether you were running a different version of Ubuntu, or a different version of Linux.</p>
</div>
<div id="comment-57057-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57058"></span>
<div id="comment-57058" class="comment not_top_scorer">
<div id="post-57058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Someone will need to try and reproduce the problem, I think.</p>
</div>
<div id="comment-57058-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 10:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57059"></span>
<div id="comment-57059" class="comment not_top_scorer">
<div id="post-57059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does it mean that I need to go through steps from a guide for a lower version of OS, e.g. <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> ?</p>
</div>
<div id="comment-57059-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 11:27)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57060"></span>
<div id="comment-57060" class="comment not_top_scorer">
<div id="post-57060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We don't know. Segmentation faults can be caused by various issues. You could try to run the following command and show us your output: <code>sudo -u taras gdb -batch -ex run -ex bt --args renderd -f -c /usr/local/etc/renderd.conf</code>. It requires the program <code>gdb</code> to be installed.</p>
</div>
<div id="comment-57060-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 11:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57063"></span>
<div id="comment-57063" class="comment not_top_scorer">
<div id="post-57063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much! I added results of debugging to the end of my initial question. As I can see there are 12 issues were found in my system.</p>
</div>
<div id="comment-57063-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 12:32)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57064"></span>
<div id="comment-57064" class="comment not_top_scorer">
<div id="post-57064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you ran "make" after "Install mod_tile and renderd" what output did you get? I suspect that some dependancies might have changed (within Ubuntu - the version of mod_tile referenced has not changed).</p>
</div>
<div id="comment-57064-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 13:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57052" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-57052-form-container" class="comment-form-container">
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

<span id="57065"></span>

<div id="answer-container-57065" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57065-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fixed my first issue with</p>
<p><code>plugins_dir=/usr/lib/mapnik/3.0/input</code> switch into <code>plugins_dir=/usr/local/lib/mapnik/input</code></p>
<p>but now new issues appeared...((</p>
<p><code>Running in foreground mode... renderd[22429]: Starting stats thread debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile renderd[22429]: Loading parameterization function for renderd[22429]: Loading parameterization function for debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile renderd[22429]: Loading parameterization function for debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile renderd[22429]: Loading parameterization function for Mapnik LOG&gt; 2017-07-13 14:12:38: Unable to process some data while parsing '/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml': * attribute 'minimum-scale-denominator' with value '750000' at line 268</code></p>
<p>Is it okay if it unable to process some data ??</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '17, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/3961e27939d00a1f4a6fe22992fc3809?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taras&#39;s gravatar image" />
<p><span>taras</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taras has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '17, 13:19</strong> </span></p>
</div>
</div>
<div id="comments-container-57065" class="comments-container">
<span id="57067"></span>
<div id="comment-57067" class="comment">
<div id="post-57067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did wonder why you had libmapnik 2 in there :)</p>
<p>Bit confused about the error at line 268 in the xml stylesheet though - are you perhaps using a different stylesheet?</p>
<p>I've tried updating a server to the latest version of everything and it "just works" (with OSM's "standard" style and Azerbaijan data).</p>
</div>
<div id="comment-57067-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 13:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57068"></span>
<div id="comment-57068" class="comment">
<div id="post-57068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using stylesheet provided by <code>git clone </code><span><code>git://github.com/gravitystorm/openstreetmap-carto.git</code></span> and converted into xml format with a command <code>carto project.mml &gt; mapnik.xml</code></p>
</div>
<div id="comment-57068-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 13:48)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57069"></span>
<div id="comment-57069" class="comment">
<div id="post-57069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, could you tell me, please if these issues are crucial? e.g. Mapnik LOG&gt; 2017-07-13 14:12:39: Unable to process some data while parsing '/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml': * attribute 'minimum-scale-denominator' with value '750000' at line 268 Thank you</p>
</div>
<div id="comment-57069-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 13:56)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57070"></span>
<div id="comment-57070" class="comment">
<div id="post-57070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well it works for me - I wonder if something's still trying to use old libraries? The "build from source" of some things will probably look around at what libraries are available.</p>
<p>Does it actually work? Do any map layers appear?</p>
</div>
<div id="comment-57070-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57071"></span>
<div id="comment-57071" class="comment">
<div id="post-57071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, yes a general map of entire world appears, nevertheless the map of Luxembourg did not appeared yet...((</p>
<p>means some problems still exist... which I need to solve</p>
<p>Thank you so much</p>
</div>
<div id="comment-57071-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:14)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57072"></span>
<div id="comment-57072" class="comment not_top_scorer">
<div id="post-57072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think a lot of issues still exist, because I am quite anxious about this messages in the Terminal:</p>
<p><code>Running in foreground mode... ... renderd[32745]: Loading parameterization function for renderd[32745]: An error occurred while loading the map layer 'ajt': Postgis Plugin: Bad connection Connection string: ' dbname=lux connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 525 of '/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml' ... renderd[32745]: An error occurred while loading the map layer 'ajt': Postgis Plugin: Bad connection Connection string: ' dbname=lux connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 525 of '/home/taras/Documents/projects/luxembourg/src/openstreetmap-carto/mapnik.xml'</code></p>
<p>BUT the 525 string looks okay as for me <code>srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=</code><a href="https://help.openstreetmap.org/users/2957/nullpointer"><code>@null</code></a><code> +wktext +no_defs +over"&gt;</code></p>
</div>
<div id="comment-57072-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:20)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57073"></span>
<div id="comment-57073" class="comment not_top_scorer">
<div id="post-57073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The switch2osm instructions suggest a database name of "gis" (which used to be the default in many OSM programs). Perhaps you've imported data in there but renderd is trying to access one called "lux"?</p>
</div>
<div id="comment-57073-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="57074"></span>
<div id="comment-57074" class="comment not_top_scorer">
<div id="post-57074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could be...</p>
<p>But when I check my system I do have only this:</p>
<p><code>Name | Owner | Encoding | Collate | Ctype | Access privileges -----------+----------+----------+-------------+-------------+----------------------- lux | taras | UTF8 | en_US.UTF-8 | en_US.UTF-8 | postgres | postgres | UTF8 | en_US.UTF-8 | en_US.UTF-8 | template0 | postgres | UTF8 | en_US.UTF-8 | en_US.UTF-8 | =c/postgres + | | | | | postgres=CTc/postgres template1 | postgres | UTF8 | en_US.UTF-8 | en_US.UTF-8 | =c/postgres + | | | | | postgres=CTc/postgres (4 rows)</code></p>
</div>
<div id="comment-57074-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:45)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
<span id="57075"></span>
<div id="comment-57075" class="comment not_top_scorer">
<div id="post-57075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I need to set PostgreSQL login method to "trust" in pg_hba.conf file. I just do not know how to perform that... I know the command <code>sudo nano /etc/postgresql/9.5/main/pg_hba.conf</code>, but what exactly I need to change I have no idea literally...</p>
</div>
<div id="comment-57075-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 14:53)</span> <span class="comment-user userinfo">taras</span>
</div>
</div>
</div>
<div id="comment-tools-57065" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-57065-form-container" class="comment-form-container">
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

