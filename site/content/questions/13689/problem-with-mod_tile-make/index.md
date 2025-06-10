+++
type = "question"
title = "Problem with mod_tile make"
description = '''Hi, I&#x27;ve setup the ruby_port of openstreetmaps and imported some data via osm2pgsql.. although the english.osm.bz fails but other countries work fine. My big problem is that make fails when I try to install mod_tile: ./autogen ./configure [root@s16307932 mod_tile]# make install Making install in ini...'''
date = "2012-06-21T14:26:00Z"
lastmod = "2012-07-01T21:35:00Z"
weight = 13689
keywords = [ "mapnik", "mod_tile" ]
aliases = [ "/questions/13689" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with mod_tile make](/questions/13689/problem-with-mod_tile-make)

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
<span id="post-13689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13689-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've setup the ruby_port of openstreetmaps and imported some data via osm2pgsql.. although the english.osm.bz fails but other countries work fine.</p>
<p>My big problem is that make fails when I try to install mod_tile:</p>
<pre><code>./autogen
./configure
[root@s16307932 mod_tile]# make install
Making install in iniparser3.0b
make[1]: Entering directory `/root/mod_tile/iniparser3.0b&#39;
make[2]: Entering directory `/root/mod_tile/iniparser3.0b&#39;
test -z &quot;/usr/local/lib&quot; || /bin/mkdir -p &quot;/usr/local/lib&quot;
 /bin/sh ../libtool   --mode=install /usr/bin/install -c   libiniparser.la &#39;/usr/local/lib&#39;
libtool: install: /usr/bin/install -c .libs/libiniparser.so.3.0.0 /usr/local/lib/libiniparser.so.3.0.0
libtool: install: (cd /usr/local/lib &amp;&amp; { ln -s -f libiniparser.so.3.0.0 libiniparser.so.3 || { rm -f libiniparser.so.3 &amp;&amp; ln -s libiniparser.so.3.0.0 libiniparser.so.3; }; })
libtool: install: (cd /usr/local/lib &amp;&amp; { ln -s -f libiniparser.so.3.0.0 libiniparser.so || { rm -f libiniparser.so &amp;&amp; ln -s libiniparser.so.3.0.0 libiniparser.so; }; })
libtool: install: /usr/bin/install -c .libs/libiniparser.lai /usr/local/lib/libiniparser.la
libtool: install: /usr/bin/install -c .libs/libiniparser.a /usr/local/lib/libiniparser.a
libtool: install: chmod 644 /usr/local/lib/libiniparser.a
libtool: install: ranlib /usr/local/lib/libiniparser.a
libtool: finish: PATH=&quot;/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/sbin&quot; ldconfig -n /usr/local/lib
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib
&#10;If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR&#39;
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH&#39; environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH&#39; environment variable
     during linking
   - use the `-Wl,-rpath -Wl,LIBDIR&#39; linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf&#39;
&#10;See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
make[2]: Nothing to be done for `install-data-am&#39;.
make[2]: Leaving directory `/root/mod_tile/iniparser3.0b&#39;
make[1]: Leaving directory `/root/mod_tile/iniparser3.0b&#39;
make[1]: Entering directory `/root/mod_tile&#39;
g++ -DHAVE_CONFIG_H -I.  -I/usr/include/freetype2 -pthread -I/usr/local/include -D_REENTRANT -D_REENTRANT -I/usr/include    -g -O2 -MT gen_tile.o -MD -MP -MF .deps/gen_tile.Tpo -c -o gen_tile.o gen_tile.cpp
In file included from gen_tile.cpp:5:
/usr/local/include/mapnik/filter_factory.hpp:1:2: warning: #warning &quot;filter_factory.hpp&quot; is now called &quot;expression.hpp&quot;
gen_tile.cpp: In function âprotoCmd render(mapnik::Map&amp;, char*, mapnik::projection&amp;, int, int, int, unsigned int, metaTile&amp;)â:
gen_tile.cpp:445: error: variable âmapnik::image_32 bufâ has initializer but incomplete type
gen_tile.cpp:453: error: âimage_viewâ was not declared in this scope
gen_tile.cpp:453: error: expected primary-expression before â&gt;â token
gen_tile.cpp:453: error: âvwâ was not declared in this scope
make[1]: *** [gen_tile.o] Error 1
make[1]: Leaving directory `/root/mod_tile&#39;
make: *** [install-recursive] Error 1</code></pre>
<p>I gather expression.hpp is included correctly and the error stems from gen_tile.cpp.</p>
<p>I have installed and tested mapnik and can generate tiles when I call ./generate_tiles.py</p>
<p>Here's the output when I configure mapnik:</p>
<pre><code>[root@s16307932 mapnik]# python scons/scons.py configure
scons: Reading SConscript files ...
&#10;Welcome to Mapnik...
&#10;Configuring build environment...
SCons CONFIG found: &#39;config.py&#39;, variables will be inherited...
Configuring on Linux in *release mode*...
Checking for freetype-config... yes
Checking for xml2-config... yes
Sorting lib and inc compiler paths...(cached) yes
Checking for C library m... yes
Checking for C library ltdl... yes
Checking for C library png... yes
Checking for C library tiff... yes
Checking for C library z... yes
Checking for C library proj... yes
Checking for C++ library icuuc... yes
Checking for C library jpeg... yes
Checking for ICU version &gt;= 4.2... found: icu 4.2
(cached) Searching for boost libs and headers... (cached)
  *libs found: /usr/local/lib
  *headers found: /usr/local/include
  *no lib naming extension found
Checking for Boost version &gt;= 1.47... yes
Found boost lib version... 1_47
Checking for C++ library boost_system... yes
Checking for C++ library boost_filesystem... yes
Checking for C++ library boost_regex... yes
Checking for C++ library boost_program_options... yes
Checking for C++ library boost_thread... yes
Checking if boost_regex was built with ICU unicode support... (cached) yes
Checking for requested plugins dependencies...
Checking for gdal-config --libs... error: no result
no
Checking if gdal is ogr enabled... no
Checking for C library curl... yes
Checking for pg_config... yes
Checking for C library sqlite3... yes
Checking if SQLite supports RTREE... (cached) yes
Checking for pkg-config... yes
Checking for cairo... no
Checking for C++ header file boost/python/detail/config.hpp... yes
Checking for pkg-config... yes
Checking for pycairo... no
&#10;All Required dependencies found!
&#10;Overwriting and re-saving file &#39;config.py&#39;...
Will hold custom path variables from commandline and python config file(s)...
&#10;Note: will build without these OPTIONAL dependencies:
   - gdal-config (gdal-config program | try setting GDAL_CONFIG SCons option)
   - ogr (OGR-enabled GDAL C++ Library | configured using gdal-config program | try setting GDAL_CONFIG SCons option | more info: http://trac.mapnik.org/wiki/OGR)
   - cairo (Cairo C library | configured using pkg-config | try setting PKG_CONFIG_PATH SCons option)
   - pycairo (Python bindings to Cairo library | configured using pkg-config | try setting PKG_CONFIG_PATH SCons option)
&#10;Checking for C header file Python.h... yes
Bindings Python version... 2.6
Python 2.6 prefix... /usr
Python bindings will install in... /usr/lib64/python2.6/site-packages
&#10;Configure completed: run `make` to build or `make install`</code></pre>
<p>I'm afraid I'm really not sure where to go from here. I'd really appreciate any pointers as I have a project going live soon and we want to run openstreetmaps on our own server rather than hammering the communities resources.</p>
<p>Thanks,</p>
<p>Paul Hudson</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '12, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a167058a65e986e9e76247775cbc38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Hudson&#39;s gravatar image" />
<p><span>Paul Hudson</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Hudson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13689" class="comments-container">
<span id="13693"></span>
<div id="comment-13693" class="comment">
<div id="post-13693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What OS and version are you using for the above?</p>
</div>
<div id="comment-13693-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 16:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="13694"></span>
<div id="comment-13694" class="comment">
<div id="post-13694-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hey, sorry should have said. I'm on CentOS 6.</p>
</div>
<div id="comment-13694-info" class="comment-info">
<span class="comment-age">(21 Jun '12, 16:30)</span> <span class="comment-user userinfo">Paul Hudson</span>
</div>
</div>
<span id="13730"></span>
<div id="comment-13730" class="comment">
<div id="post-13730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>...and it's Mapnik v2.0.1 - and mod_tile as available here: <a href="http://svn.openstreetmap.org/applications/utils/mod_tile">http://svn.openstreetmap.org/applications/utils/mod_tile</a></p>
<p>Are they the most recent versions and compatible? Let me know if you need any other info. Thanks!!!</p>
</div>
<div id="comment-13730-info" class="comment-info">
<span class="comment-age">(22 Jun '12, 17:42)</span> <span class="comment-user userinfo">Paul Hudson</span>
</div>
</div>
</div>
<div id="comment-tools-13689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13689-form-container" class="comment-form-container">
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

<span id="13731"></span>

<div id="answer-container-13731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13731-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After discussion with Paul on #osm-dev we determined that this is likely to be a version conflict and that currently mod_tile will probably not compile against mapnik 2.01.</p>
<p>As a result the current answer would be to compile against mapnik 2.0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '12, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '12, 19:49</strong> </span></p>
</div>
</div>
<div id="comments-container-13731" class="comments-container">
<span id="13738"></span>
<div id="comment-13738" class="comment">
<div id="post-13738-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks to SimonPoole and the other chaps at #osm-dev. Compiling against mapnik 2.0 went smoothly.</p>
</div>
<div id="comment-13738-info" class="comment-info">
<span class="comment-age">(23 Jun '12, 09:13)</span> <span class="comment-user userinfo">Paul Hudson</span>
</div>
</div>
</div>
<div id="comment-tools-13731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13902"></span>

<div id="answer-container-13902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use mod_tile fork to compile against mapnik 2.1 <a href="https://github.com/ramunasd/mod_tile">https://github.com/ramunasd/mod_tile</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '12, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e1e1ebfcf8cb003397221dd42ffb94f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ieskok&#39;s gravatar image" />
<p><span>ieskok</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ieskok has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '12, 11:29</strong> </span></p>
</div>
</div>
<div id="comments-container-13902" class="comments-container">
<span id="13931"></span>
<div id="comment-13931" class="comment">
<div id="post-13931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>mv render_config.h-dist render_config.h</code></p>
</div>
<div id="comment-13931-info" class="comment-info">
<span class="comment-age">(01 Jul '12, 21:27)</span> <span class="comment-user userinfo">Dave Jarvis</span>
</div>
</div>
<span id="13932"></span>
<div id="comment-13932" class="comment">
<div id="post-13932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>sudo cp .libs/mod_tile.so /usr/lib/apache2/modules/.</code></p>
</div>
<div id="comment-13932-info" class="comment-info">
<span class="comment-age">(01 Jul '12, 21:35)</span> <span class="comment-user userinfo">Dave Jarvis</span>
</div>
</div>
</div>
<div id="comment-tools-13902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13902-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13930"></span>

<div id="answer-container-13930" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>mkdir -p $HOME/src
cd $HOME/src
git clone https://github.com/ramunasd/mod_tile
cd mod_tile
mv render_config.h-dist render_config.h
./autogen.sh
./configure
make
sudo make install
sudo cp .libs/mod_tile.so /usr/lib/apache2/modules/.
sudo bash -c &quot;echo &#39;LoadModule tile_module /usr/lib/apache2/modules/mod_tile.so&#39; &gt; /etc/apache2/mods-available/tile.load&quot;
sudo a2enmod tile
sudo /etc/init.d/apache2 restart</code></pre>
<p>Seems to work against Mapnik 2.0.1.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '12, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/55e2feeeed03eba1db3bbc39a8d301f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave%20Jarvis&#39;s gravatar image" />
<p><span>Dave Jarvis</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave Jarvis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '12, 21:35</strong> </span></p>
</div>
</div>
<div id="comments-container-13930" class="comments-container">
&#10;</div>
<div id="comment-tools-13930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13930-form-container" class="comment-form-container">
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

