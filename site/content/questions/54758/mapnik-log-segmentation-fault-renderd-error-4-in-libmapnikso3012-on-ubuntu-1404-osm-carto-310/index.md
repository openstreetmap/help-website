+++
type = "question"
title = "Mapnik LOG: Segmentation fault; renderd error 4 in libmapnik.so.3.0.12 on ubuntu 14.04, osm-carto 3.1.0"
description = '''Hi, I am running a tile server with mapnik 2.2 (build from source) with openstreetmap-carto 2.x and everything works fine. On an independent server I am trying to run 3.0.12 (build from source, just changing the version number requested to above) mapnik with osm-carto 3.1.0 but that one is not coope...'''
date = "2017-02-21T08:55:00Z"
lastmod = "2017-02-21T08:55:00Z"
weight = 54758
keywords = [ "openstreetmap", "mapnik", "tileserver" ]
aliases = [ "/questions/54758" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik LOG: Segmentation fault; renderd error 4 in libmapnik.so.3.0.12 on ubuntu 14.04, osm-carto 3.1.0](/questions/54758/mapnik-log-segmentation-fault-renderd-error-4-in-libmapnikso3012-on-ubuntu-1404-osm-carto-310)

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
<span id="post-54758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am running a tile server with mapnik 2.2 (build from source) with openstreetmap-carto 2.x and everything works fine. On an independent server I am trying to run 3.0.12 (build from source, just changing the version number requested to above) mapnik with osm-carto 3.1.0 but that one is not cooperating. Any ideas? Do I potentially have an overlap of libraries, or an inconsistency of version numbers?</p>
<p>when starting renderd, I get the</p>
<pre><code>Mapnik LOG: Segmentation fault</code></pre>
<p>and dmesg gives me</p>
<pre><code>renderd[8213]: segfault at 40 ip 00007fb1e10bb8d3 sp 00007fb1c9d5e1f0 error 4 in libmapnik.so.3.0.12[7fb1e0ce0000+86d000]</code></pre>
<p>I am wondering if that has to do with any of the other mapnik libraries. Do they also have to fit the 3.0.12 mapnik version?</p>
<p>A quick list of what packages are installed that have mapnik in their name, or are suggested as core</p>
<p>Ubuntu 14.04</p>
<pre><code>libmapnik-dev/now 2.2.0+ds1-6build2
libmapnik2.2/now 2.2.0+ds1-6build2
mapnik-reference/now 5.0.6-1
mapnik-utils/now 2.2.0+ds1-6build2 
python-mapnik/now 2.2.0+ds1-6build2
&#10;libboost-dev/now 1.54.0.1ubuntu1
libicu-dev/now 52.1-3ubuntu0.4
libicu52/now 52.1-3ubuntu0.4
zlib1g/now 1:1.2.8.dfsg-1ubuntu1
zlib1g-dev/now 1:1.2.8.dfsg-1ubuntu1
libfreetype6/now 2.5.2-1ubuntu2.5
libfreetype6-dev/now 2.5.2-1ubuntu2.5
libxml2/now 2.9.1+dfsg1-3ubuntu4.8
libxml2-dev/now 2.9.1+dfsg1-3ubuntu4.8
libharfbuzz0b/now 0.9.27-1ubuntu1.1 (checked this and this gets installed at a later point, after mapnik is installed)</code></pre>
<p>also from source</p>
<pre><code>installed harfbuzz 1.4.2 (used for mapnik installation)
mapnik 3.0.12 using python scons/scons.py configure..., install</code></pre>
<p>renderd -f -c /usr/local/etc/renderd.conf</p>
<pre><code>renderd[277]: Rendering daemon started
renderd[277]: Initiating reqyest_queue
iniparser: syntax error in /usr/local/etc/renderd.conf (7):
-&gt; ;[renderd01]
iniparser: syntax error in /usr/local/etc/renderd.conf (14):
-&gt; ;[renderd02]
iniparser: syntax error in /usr/local/etc/renderd.conf (30):
-&gt; ;or should the HOST be db?
iniparser: syntax error in /usr/local/etc/renderd.conf (34):
-&gt; ;** config options used by mod_tile, but not renderd **
iniparser: syntax error in /usr/local/etc/renderd.conf (46):
-&gt; ;[style2]
iniparser: syntax error in /usr/local/etc/renderd.conf (53):
-&gt; ;** config options used by mod_tile, but not renderd **
renderd[277]: Parsing section renderd
renderd[277]: Parsing render section 0
renderd[277]: Parsing section mapnik
renderd[277]: Parsing section default
renderd[277]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[277]: config renderd: num_threads=4
renderd[277]: config renderd: num_slaves=0
renderd[277]: config renderd: tile_dir=/var/lib/mod_tile
renderd[277]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[277]: config mapnik:  **plugins_dir=/usr/lib/mapnik/2.2/input**
renderd[277]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[277]: config mapnik:  font_dir_recurse=1
renderd[277]: config renderd(0): Active
renderd[277]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[277]: config renderd(0): num_threads=4
renderd[277]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[277]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[277]: config map 0:   name(default) file(/home/tileserver/openstreetmap-carto-3.1.0/style.xml) uri(/osm_tiles/) htcp() host(localhost)
renderd[277]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[277]: Created server socket 3
renderd[277]: Renderd is **using mapnik version 3.0.12**
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont.ttf
renderd[277]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_sample.ttf
Running in foreground mode...
renderd[277]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[277]: Loading parameterization function for
renderd[277]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[277]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[277]: Loading parameterization function for
Mapnik LOG&gt; 2017-02-20 11:27:26: warning: unable to find face-name &#39;Noto Sans UI Regular&#39; in FontSet &#39;fontset-0&#39;
.... JUST A TON of warnings (took it out to shorten this) about Noto font, but that should not be the issue....
Mapnik LOG&gt; 2017-02-20 11:27:26: warning: unable to find face-name &#39;Unifont Upper Medium&#39; in FontSet &#39;fontset-2&#39;
Segmentation fault</code></pre>
<p>I was wondering if this could be the problem, but can't find any similar files from 2.2. anywhere else (was thinking if there are duplicates, I might be using some wrong mapnik version)</p>
<pre><code>renderd[277]: config mapnik: plugins_dir=/usr/lib/mapnik/2.2/input
renderd[277]: Renderd is using mapnik version 3.0.12</code></pre>
<p>this is the build report for mapnik and is shows using HarfBuzz 1.4.2. So that should be fine (?)</p>
<pre><code>Configuring build environment...
Configuring on Linux in *release mode*...
Checking for freetype-config... yes
Checking for dlfcn.h support ... yes
Checking if compiler (c++) supports -std=c++11 flag... (cached) yes
Checking for C library z... yes
Checking for C++ library icuuc... yes
Checking for ICU version &gt;= 4.2... found: icu 52.1
(cached) Checking for C++ library harfbuzz... yes
Checking for HarfBuzz version &gt;= 0.9.34... found: HarfBuzz 1.4.2
Checking for HarfBuzz with freetype support
(cached) yes
Searching for boost libs and headers... (cached)
Using default boost lib dir: /usr/lib
Using default boost include dir: /usr/include
Checking for C++ header file boost/version.hpp... yes
Checking for Boost version &gt;= 1.47... yes
Found boost lib version... 1_54
Checking for C++ library boost_system... yes
Checking for C++ library boost_filesystem... yes
Checking for C++ library boost_regex... yes
Checking for C++ library boost_program_options... yes
Checking whether Boost was compiled with C++11 scoped enums ... no
Checking if boost_regex was built with ICU unicode support... (cached) yes
Checking for C library jpeg... yes
Checking for C library proj... yes
Checking for C library png... yes
Checking for C library webp... yes
Checking for C library tiff... yes
Checking for pkg-config... yes
Checking for requested plugins dependencies...
Checking for pg_config... yes
Checking for C library sqlite3... yes
Checking if SQLite supports RTREE... (cached) yes
Checking for gdal-config --libs... yes
Checking for gdal-config --cflags... yes
Checking for name of gdal library... gdal
Checking for C++ library gdal... yes
Checking for pg_config... yes
Checking if gdal is ogr enabled... yes
Checking for gdal-config --libs... yes
Checking for gdal-config --cflags... yes
Checking for name of ogr library... gdal
Checking for C++ library gdal... yes
Checking for cairo... yes
Checking for cairo lib and include paths...  yes
Checking for cairo freetype font support ... yes</code></pre>
<p>The one thing I also changed is the project.mml the connection to my remote psql, but I do not think that that is the issue</p>
<pre><code>  osm2pgsql: &amp;osm2pgsql
    type: &quot;postgis&quot;
    host: &quot;mydatabasehost&quot;
    port: &quot;5432&quot;
    user: &quot;theosmuser&quot;
    password: &quot;theosmuserpassword&quot;
    dbname: &quot;gis&quot;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '17, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e9400940cd6333c87b0403174a213707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wordli&#39;s gravatar image" />
<p><span>wordli</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wordli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '17, 09:06</strong> </span></p>
</div>
</div>
<div id="comments-container-54758" class="comments-container">
&#10;</div>
<div id="comment-tools-54758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54758-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

