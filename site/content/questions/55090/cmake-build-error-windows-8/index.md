+++
type = "question"
title = "cmake build error windows 8"
description = '''Hi, i have followed the steps in https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html. first thing i must mention is that the git clone does not work: git clone https://code.wireshark.org/review/wireshark. so i have downloaded the source code from the site: https://1.eu.dl.wireshark.or...'''
date = "2016-08-24T01:41:00Z"
lastmod = "2016-08-24T02:57:00Z"
weight = 55090
keywords = [ "cmake", "build", "windows8" ]
aliases = [ "/questions/55090" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [cmake build error windows 8](/questions/55090/cmake-build-error-windows-8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55090-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i have followed the steps in <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.</a> first thing i must mention is that the git clone does not work: git clone <a href="https://code.wireshark.org/review/wireshark.">https://code.wireshark.org/review/wireshark.</a></p><p>so i have downloaded the source code from the site: <a href="https://1.eu.dl.wireshark.org/src/wireshark-2.0.5.tar.bz2">https://1.eu.dl.wireshark.org/src/wireshark-2.0.5.tar.bz2</a></p><p>now when i use cmake i get the following: this is the output of the VS2013 x64 Native Tool Command Prompt:</p><pre><code>C:\wireshark-2.0.5\wsbuild64&gt;cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\
-- Generating build using CMake 3.6.1
-- Building for win64 using Visual Studio 12 2013 Win64
Working in C:\wireshark-2.0.5\Wireshark-win64-libs-2.0
Tag 2016-06-03 found. Skipping.
-- No custom file found in C:/wireshark-2.0.5
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- RelWithDebInfo: /MD /Zi /O2 /Ob1 /DNDEBUG
-- V: 2.0.5, MaV: 2, MiV: 0, PL: 5, EV: .
-- Checking for c-compiler flag: /MP
-- Checking for c-compiler flag: /Zo
-- Checking for c-compiler flag: /w34295 /w34189
-- Checking for c++-compiler flag: /MP
-- Checking for c++-compiler flag: /Zo
-- Checking for c++-compiler flag: /w34295 /w34189
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;HtmlViewer;KERBEROS;LEX;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- AIRPCAP FOUND
-- AIRPCAP includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR)
-- CAP NOT FOUND
-- CARES FOUND
-- CARES includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/c-ares-1.11.0-win64ws/include
-- CARES libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/c-ares-1.11.0-win64ws/lib/libcares-2.lib
-- GCRYPT FOUND
-- GCRYPT includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;geoip&#39;
-- GEOIP FOUND
-- GEOIP includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- GLIB2 FOUND
-- GLIB2 includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0/include
-- GLIB2 libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0
-- GMODULE2 libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gnutls&#39;
-- GNUTLS FOUND
-- GNUTLS includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib
-- GTK2 FOUND
-- GTK2 includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/gtk-2.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/freetype2;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0/include;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/atk-1.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/gdk-pixbuf-2.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/cairo;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/include/pango-1.0;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gtk-2.0/include
-- GTK2 libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gobject-2.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/atk-1.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gmodule-2.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gdk_pixbuf-2.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/cairo.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/pango-1.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/pangocairo-1.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gdk-win32-2.0.lib;C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE)
-- GETTEXT NOT FOUND
-- Could NOT find Git (missing:  GIT_EXECUTABLE)
-- Git NOT FOUND
-- HTML_VIEWER NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- KERBEROS FOUND
-- KERBEROS includes: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: C:/wireshark-2.0.5/Wireshark-win64-libs-2.0/kfw-3-2-2-x64-ws/lib/krb5_64.lib

CMake Error at C:/Program Files/CMake/share/cmake-3.6/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find LEX (missing: LEX_EXECUTABLE)
  Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.6/Modules/FindPackageHandleStandardArgs.c
  make:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/modules/FindLEX.cmake:23 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
    CMakeLists.txt:810 (find_package)

-- Configuring incomplete, errors occurred!
See also &quot;C:/wireshark-2.0.5/wsbuild64/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;C:/wireshark-2.0.5/wsbuild64/CMakeFiles/CMakeError.log&quot;.</code></pre><p>if any other information is needed please let me know.</p><p>Thanks in advance, Ran</p></div><div id="question-tags" class="tags-container tags">cmake build windows8</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/2a790061b6d1f5ec0fb06a4ab6a5e52f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ran&#39;s gravatar image" /><p>Ran<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ran has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '16, 03:06</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55090" class="comments-container"></div><div id="comment-tools-55090" class="comment-tools"></div><div class="clear"></div><div id="comment-55090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55091"></span>

<div id="answer-container-55091" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55091-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Firstly the git clone URL works for many other people, what is the error you get?</p><p>CMake is complaining that it can't find the LEX executable which is normally the Cygwin version found as &lt;cygwindir&gt;/bin/flex.exe. Have you installed the Cygwin Devel/flex package, or the chocolatey Win flex-bison package?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '16, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55091" class="comments-container"><span id="55093"></span><div id="comment-55093" class="comment"><div id="post-55093-score" class="comment-score"></div><div class="comment-text"><p>you were right i over looked the package installation of cygwin, after i installed them it compiled.</p><p>thanks.</p></div><div id="comment-55093-info" class="comment-info"><span class="comment-age">(24 Aug '16, 05:13)</span> Ran</div></div><span id="63065"></span><div id="comment-63065" class="comment"><div id="post-63065-score" class="comment-score"></div><div class="comment-text"><p>For others which have the same issue, I had to add C:\ProgramData\chocolatey\bin; to the system PATH environment variable.</p></div><div id="comment-63065-info" class="comment-info"><span class="comment-age">(24 Jul '17, 19:03)</span> keoma</div></div><span id="63077"></span><div id="comment-63077" class="comment"><div id="post-63077-score" class="comment-score"></div><div class="comment-text"><p>As the OP didn't have either the Cygwin flex or winflex (via chocolatey) then this advice would not have helped.</p><p>Chocolatey normally adds itself to your user PATH, so if you had to add it manually, either:</p><ol><li>The chocolatey install was broken which should be reported to chocolatey.</li><li>Chocolatey was installed using a different user account to that currently being used, in which case your fix would be appropriate.</li><li>Someone unhelpfully removed it from your user PATH.</li></ol></div><div id="comment-63077-info" class="comment-info"><span class="comment-age">(25 Jul '17, 02:25)</span> grahamb ♦</div></div><span id="63099"></span><div id="comment-63099" class="comment"><div id="post-63099-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a>, I agree, I wrote this comment as a note for other users having similar issues.</p><p>I was in the third situation you've listed (removed chocolatey from the PATH) because I had other errors and I was trying to "clean" my PATH.</p></div><div id="comment-63099-info" class="comment-info"><span class="comment-age">(25 Jul '17, 10:32)</span> keoma</div></div></div><div id="comment-tools-55091" class="comment-tools"></div><div class="clear"></div><div id="comment-55091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

