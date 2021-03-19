+++
type = "question"
title = "Compilation with MacPorts - Plugins fail to load"
description = '''I&#x27;m attempting to compile Wireshark from the GitHub repo on macOS Sierra using MacPorts. I know there&#x27;s a macosx-setup.sh script for installing all the dependencies, but I&#x27;d rather not go this route since I have my dependencies fulfilled by MacPorts and I don&#x27;t want duplicates strewn around my syste...'''
date = "2017-04-28T10:20:00Z"
lastmod = "2017-05-04T09:05:00Z"
weight = 61106
keywords = [ "macosx", "build", "macports" ]
aliases = [ "/questions/61106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compilation with MacPorts - Plugins fail to load](/questions/61106/compilation-with-macports-plugins-fail-to-load)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to compile Wireshark from the GitHub repo on macOS Sierra using MacPorts. I know there's a <code>macosx-setup.sh</code> script for installing all the dependencies, but I'd rather not go this route since I have my dependencies fulfilled by MacPorts and I don't want duplicates strewn around my system. I can build and run Wireshark but none of the plugins load. They each fail with an error like the following:</p><pre><code>Couldn&#39;t load module /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/ethercat.so: dlopen(/Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/ethercat.so, 2): initializer function 0x10fd09b92 not in mapped image for /opt/local/lib/libgpg-error.0.dylib</code></pre><p>The initializer function address is different with each build of Wireshark that I make. The steps I use for building are:</p><pre><code>mkdir build
cd build
cmake ..
make
make app_bundle</code></pre><p>CMake doesn't report any required dependencies missing, and GPG itself is discovered as follows:</p><pre><code>-- Found GCRYPT: /opt/local/lib/libgcrypt.dylib (found suitable version &quot;1.7.6&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: /opt/local/include
-- GCRYPT libs: /opt/local/lib/libgcrypt.dylib;/opt/local/lib/libgpg-error.dylib</code></pre><p>I notice that <code>libgpg-error.0.dylib</code> in the build output differs from the one MacPorts provides.</p><pre><code>diff /opt/local/lib/libgpg-error.0.dylib /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/Frameworks/libgpg-error.0.dylib
Binary files /opt/local/lib/libgpg-error.0.dylib and /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/Frameworks/libgpg-error.0.dylib differ</code></pre><p>It appears that some paths in the Application-local dylib are being remapped in the build process (from <code>otool -l</code>):</p><pre><code>Load command 10
          cmd LC_LOAD_DYLIB
      cmdsize 72
         name @executable_path/../Frameworks/libintl.8.dylib (offset 24)</code></pre><p>It seems to me, that the Application-local dylib (not the MacPorts one) should be loading. I don't have any of these environment variables set:</p><pre><code>$DYLD_FRAMEWORK_PATH
$DYLD_FALLBACK_FRAMEWORK_PATH
$DYLD_VERSIONED_FRAMEWORK_PATH
$DYLD_LIBRARY_PATH
$DYLD_FALLBACK_LIBRARY_PATH
$DYLD_VERSIONED_LIBRARY_PATH
$DYLD_ROOT_PATH
$DYLD_INSERT_LIBRARIES</code></pre><p>I would expect Wireshark's <code>dlopen</code> call to first look in the application package before searching the system. Has anyone else built on a MacPorts system and run into this?</p><p><strong>EDIT:</strong></p><p>I did some tracking of the module load process by turning on some DYLD environment variables. I just looked at the <code>docsis.so</code> plugin.</p><p>The applicable parts of the debug trace are as follows:</p><pre><code>dyld: Main executable mapped /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/Wireshark
        __PAGEZERO at 0x00000000-&gt;0x100000000
            __TEXT at 0x10636E000-&gt;0x1069B6000
            __DATA at 0x1069B6000-&gt;0x106A1E000
        __LINKEDIT at 0x106A1E000-&gt;0x106B7B9F8
dyld: loaded: /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/Wireshark</code></pre><p>dyld: re-using existing development shared cache mapping 0x7FFF8A27D000-&gt;0x7FFFA5009FFF read execute init=5, max=5 0x7FFFA900A000-&gt;0x7FFFADBE4FFF read write init=3, max=3 0x7FFFB1BE5000-&gt;0x7FFFB915CFFF read init=1, max=1 0x7FFF9EEE0000-&gt;0x7FFF9F3C0000 (code signature)</p><p>This is where we're loading all the shared libraries on startup. Notice that <code>libgpg-error.0.dylib</code> is first loaded from the application package.</p><pre><code>dyld: Mapping /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/../Frameworks/libgpg-error.0.dylib
            __TEXT at 0x10A4BA000-&gt;0x10A4C7FFF with permissions r.x
            __DATA at 0x10A4C8000-&gt;0x10A4C8FFF with permissions rw.
        __LINKEDIT at 0x10A4C9000-&gt;0x10A4CD1E7 with permissions r..
            __DATA prefetching 0x10A4C8000 -&gt; 0x10A4C8FFF
dyld: loaded: /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/../Frameworks/libgpg-error.0.dylib</code></pre><p>Here's the binding of the initialization function:</p><pre><code>dyld: bind: libgpg-error.0.dylib:0x10A4C84B8 = libgpg-error.0.dylib:_gpg_err_init, *0x10A4C84B8 = 0x10A4C3B92</code></pre><p>Then, it's called.</p><pre><code>dyld: calling initializer function 0x10a4c3b92 in /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/../Frameworks/libgpg-error.0.dylib</code></pre><p>This looks like a lazy bind of the initialization function again, but it starts with two underscores.</p><pre><code>dyld: lazy bind: libgpg-error.0.dylib:0x10A4C8078 = libgpg-error.0.dylib:__gpg_err_init, *0x10A4C8078 = 0x10A4BC345</code></pre><p>Now the docsis plugin is loaded.</p><pre><code>dlopen(/Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so, 0x00000002)
dyld: Mapping /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so
            __TEXT at 0x114D47000-&gt;0x114D6DFFF with permissions r.x
            __DATA at 0x114D6E000-&gt;0x114D84FFF with permissions rw.
        __LINKEDIT at 0x114D85000-&gt;0x114DABBDB with permissions r..
dyld: loaded: /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so</code></pre><p>Then <code>libgpg-error.0.dylib</code> is loaded again! But this time it's from MacPorts and it's going into a different part of memory.</p><pre><code>dyld: Mapping /opt/local/lib/libgpg-error.0.dylib
            __TEXT at 0x114F68000-&gt;0x114F75FFF with permissions r.x
            __DATA at 0x114F76000-&gt;0x114F76FFF with permissions rw.
        __LINKEDIT at 0x114F77000-&gt;0x114F7BA37 with permissions r..
dyld: loaded: /opt/local/lib/libgpg-error.0.dylib</code></pre><p>The initialization function is bound again. It's bound to the same address as before, but this time from the memory location holding the MacPorts version of the library.</p><pre><code>dyld: bind: libgpg-error.0.dylib:0x114F764B8 = libgpg-error.0.dylib:_gpg_err_init, *0x114F764B8 = 0x10A4C3B92</code></pre><p>Then the lazy bind of the init function with two underscores again.</p><pre><code>dyld: forced lazy bind: libgpg-error.0.dylib:0x114F76078 = libgpg-error.0.dylib:__gpg_err_init, *0x114F76078 = 0x10A4BC345</code></pre><p>The glib initializer is called, and then docsis is considered unused? Huh.</p><pre><code>dyld: calling initializer function 0x114dd66ae in /opt/local/lib/libglib-2.0.0.dylib
dlclose(), found unused image 0x7fa2d2c1f610 docsis.so
dlclose(), deleting 0x7fa2d2c1f610 docsis.so
dyld: unloaded: /Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so</code></pre><p>Then one (the MacPorts one, I think) of the gpg lib's images is considered unused.</p><pre><code>dlclose(), found unused image 0x60000015c1a0 libgpg-error.0.dylib</code></pre><p>It's unloaded.</p><pre><code>dlclose(), deleting 0x60000015c1a0 libgpg-error.0.dylib
dyld: unloaded: /opt/local/lib/libgpg-error.0.dylib</code></pre><p>Now DYLD spits out the error about not finding the initialization function for gpg.</p><pre><code>  dlopen() failed, error: &#39;dlopen(/Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so, 2): initializer function 0x10a4c3b92 not in mapped image for /opt/local/lib/libgpg-error.0.dylib
&#39;
dyld: lazy bind: libgmodule-2.0.0.dylib:0x10B78E0C8 = libdyld.dylib:_dlerror, *0x10B78E0C8 = 0x7FFFA4D89907
dlerror()</code></pre><hr /><p>It makes sense that I'm having this problem given the output of <code>otool</code> on Wireshark versus the docsis plugin:</p><pre><code>hostname:~ username$ otool -L ~/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/Wireshark 
/Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/MacOS/Wireshark:
    @executable_path/../Frameworks/libgpg-error.0.dylib (compatibility version 22.0.0, current version 22.0.0)

hostname:~ username$ otool -L ~/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so 
/Users/username/src/github/wireshark/build/run/Wireshark.app/Contents/PlugIns/wireshark/docsis.so:
    /opt/local/lib/libgpg-error.0.dylib (compatibility version 22.0.0, current version 22.0.0)</code></pre><p>However, I'm not sure why the docsis plugin looks in one location for libgpg while the Wireshark binary looks elsewhere.</p></div><div id="question-tags" class="tags-container tags">macosx build macports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '17, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/2e9c62b124fec3ee23c99d84d58ca5bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="watkipet&#39;s gravatar image" /><p>watkipet<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="watkipet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '17, 16:47</p></div></div><div id="comments-container-61106" class="comments-container"></div><div id="comment-tools-61106" class="comment-tools"></div><div class="clear"></div><div id="comment-61106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61234"></span>

<div id="answer-container-61234" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61234-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that the relative path translation normally performed by <code>packaging/macosx/osx-app.sh</code> is not occurring. <code>osx-app.sh:424</code> looks at the Mach headers (using <code>otool -hv</code>) to determine whether the file in question is an executable, dynamic library, or bundle. It then passes the <code>otool</code> output through <code>sed</code> and <code>awk</code> to pull out a specific token. It appears that in the past (or on some other machine / macOS version / installation configuration?) <code>otool</code> spit out 4 lines of output and thus the <code>sed</code> command looked at line 4. However, on my machine, <code>otool</code> spits out only three lines. Thus:</p><ol><li>rpath translation fails silently when running <code>make app_bundle</code></li><li>The plugins use the MacPorts versions of libraries instead of the Wireshark.app versions</li><li>The main Wireshark app successfully uses the Wireshark.app versions of the libraries (not sure why it's different here)</li><li>Two different versions of the same libraries are loaded at runtime</li><li>DYLD now cannot call the proper library initialization function when attempting to load the plugins--thus the cryptic error</li></ol><p>If I can figure out how to contribute a change to the source, I'll try to do that. However, I'm concerned that the 4 versus 3 line output of <code>otool</code> is something specific to my machine / configuration and I'd just be breaking things for others. Anyone else run into this?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '17, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/2e9c62b124fec3ee23c99d84d58ca5bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="watkipet&#39;s gravatar image" /><p>watkipet<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="watkipet has no accepted answers">0%</span></p></div></div><div id="comments-container-61234" class="comments-container"></div><div id="comment-tools-61234" class="comment-tools"></div><div class="clear"></div><div id="comment-61234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

