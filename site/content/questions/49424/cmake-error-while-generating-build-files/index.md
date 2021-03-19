+++
type = "question"
title = "CMake error while generating build files"
description = '''Hi everyone, I&#x27;ve just installed NSIS to create a Wireshark installer. So I wanted to generate the build files after the installation but I get the following output -- Generating build using CMake 3.4.1 -- Building for win64 using Visual Studio 12 2013 Win64 Working in C:&#92;Development&#92;wireshark-win64...'''
date = "2016-01-21T00:24:00Z"
lastmod = "2016-01-21T02:46:00Z"
weight = 49424
keywords = [ "nsis", "cmake" ]
aliases = [ "/questions/49424" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [CMake error while generating build files](/questions/49424/cmake-error-while-generating-build-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49424-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I've just installed NSIS to create a Wireshark installer. So I wanted to generate the build files after the installation but I get the following output</p><pre><code>-- Generating build using CMake 3.4.1
-- Building for win64 using Visual Studio 12 2013 Win64
Working in C:\Development\wireshark-win64-libsTag 2015-12-11 found. Skipping.-- No custom file found in C:/Development/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.0-1508-g6e90ca0, MaV: 2, MiV: 1, PL: 0, EV: -1508-g6e90ca0.
-- Checking for c-compiler flag: /MP
-- Checking for c-compiler flag: /Zo
-- Checking for c-compiler flag: /w34295 /w34189
-- Checking for c++-compiler flag: /MP
-- Checking for c++-compiler flag: /Zo
-- Checking for c++-compiler flag: /w34295 /w34189
-- Packagelist:

AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;HtmlViewer;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;

Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- AIRPCAP FOUND
-- AIRPCAP includes: C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- CARES FOUND
-- CARES includes: C:/Development/wireshark-win64-libs/c-ares-1.9.1-1-win64ws/include
-- CARES libs: C:/Development/wireshark-win64-libs/c-ares-1.9.1-1-win64ws/lib/libcares-2.lib
-- GCRYPT FOUND
-- GCRYPT includes: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-

error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- GEOIP FOUND
-- GEOIP includes: C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- GLIB2 FOUND
-- GLIB2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0;C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- GNUTLS FOUND
-- GNUTLS includes: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- GTK2 FOUND
-- GTK2 includes: C:/Development/wireshark-win64-libs/gtk2/include/gtk-2.0;C:/Development/wireshark-win64-libs/gtk2/include;C:/Development/wireshark-win64-

libs/gtk2/include/freetype2;C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0;C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0/include;C:/Development/wireshark-

win64-libs/gtk2/include/atk-1.0;C:/Development/wireshark-win64-libs/gtk2/include/gdk-pixbuf-2.0;C:/Development/wireshark-win64-

libs/gtk2/include/cairo;C:/Development/wireshark-win64-libs/gtk2/include/pango-1.0;C:/Development/wireshark-win64-libs/gtk2/lib/gtk-2.0/include
-- GTK2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gobject-2.0.lib;C:/Development/wireshark-win64-

libs/gtk2/lib/atk-1.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gdk_pixbuf-

2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/cairo.lib;C:/Development/wireshark-win64-libs/gtk2/lib/pango-1.0.lib;C:/Development/wireshark-win64-

libs/gtk2/lib/pangocairo-1.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gdk-win32-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- HTML_VIEWER NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- KERBEROS FOUND
-- KERBEROS includes: C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: C:/cygwin64/bin/flex.exe
-- Could NOT find LIBSSH (missing:  LIBSSH_LIBRARIES LIBSSH_INCLUDE_DIRS LIBSSH_VERSION) (Required is at least version &quot;0.6&quot;)
-- LIBSSH NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- LUA FOUND
-- LUA includes: C:/Development/wireshark-win64-libs/lua5.2.3/include
-- LUA libs: C:/Development/wireshark-win64-libs/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- PCAP FOUND
-- PCAP includes: C:/Development/wireshark-win64-libs/WpdPack/Include
-- PCAP libs: C:/Development/wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- PORTAUDIO FOUND
-- PORTAUDIO includes: C:/Development/wireshark-win64-libs/portaudio_v19_2/include;C:/Development/wireshark-win64-libs/portaudio_v19_2/src/common;C:/Development/wireshark-

win64-libs/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: C:/cygwin64/bin/perl.exe
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core NOT FOUND
-- Qt5LinguistTools NOT FOUND
-- Qt5Multimedia NOT FOUND
-- Qt5PrintSupport NOT FOUND
-- Qt5Svg NOT FOUND
-- Qt5Widgets NOT FOUND
-- Qt5WinExtras NOT FOUND
-- Could NOT find SBC (missing:  SBC_INCLUDE_DIR SBC_LIBRARY) 
-- SBC NOT FOUND
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: C:/cygwin64/bin/sed.exe
-- Could NOT find SETCAP (missing:  SETCAP_EXECUTABLE) 
-- SETCAP NOT FOUND
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: C:/cygwin64/bin/bash.exe
-- SMI FOUND
-- SMI includes: C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/include
-- SMI libs: C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- WINSPARKLE FOUND
-- WINSPARKLE includes: C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws
-- WINSPARKLE libs: C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: C:/cygwin64/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- ZLIB FOUND
-- ZLIB includes: C:/Development/wireshark-win64-libs/zlib-1.2.8-ws;C:/Development/wsbuild64/zlib
-- ZLIB libs: zlib
-- C-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3
-- CXX-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3 /GR /EHsc
-- Warnings as errors: /WX
-- No custom file found in C:/Development/wireshark/asn1
-- Using Cygwin a2x
-- No custom file found in C:/Development/wireshark/epan
-- No custom file found in C:/Development/wireshark/ui/gtk
-- docdir: 
-- 
-- The following OPTIONAL packages have been found:

 * AIRPCAP
 * CARES
 * GCRYPT (required version &gt;= 1.4.2)
 * GEOIP
 * GMODULE2
 * GNUTLS (required version &gt;= 2.12.0)
 * GTK2
 * HtmlViewer
 * KERBEROS
 * LUA
 * PCAP
 * POD
 * PORTAUDIO
 * Perl
 * SH
 * SMI
 * WINSPARKLE
 * ZLIB
 * LYNX
 * SED
 * XSLTPROC
 * XMLLINT
 * ASCIIDOC
 * PythonInterp

-- The following REQUIRED packages have been found:

 * PowerShell
 * GLIB2
 * GTHREAD2
 * LEX
 * YACC

-- The following OPTIONAL packages have not been found:

 * CAP
 * Gettext
 * LIBSSH (required version &gt;= 0.6) , libssh is library for ssh connections and it is needed to build sshdump , &lt;www: https://www.libssh.org/get-it/&gt;
 * M
 * PkgConfig
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Multimedia
 * Qt5PrintSupport
 * Qt5Svg
 * Qt5Widgets
 * Qt5WinExtras
 * SBC , SBC Codec for Bluetooth A2DP stream playing , &lt;www: http://git.kernel.org/cgit/bluetooth/sbc.git&gt;
 * SETCAP
 * YAPP
 * HTMLHelp

-- Configuring done
CMake Error at packaging/nsis/CMakeLists.txt:199 (add_custom_command):
  Error evaluating generator expression:

    $&lt; TARGET_FILE:wireshark&gt;

  No target &quot;wireshark&quot;
Call Stack (most recent call first):
  CMakeLists.txt:2320 (ADD_NSIS_PACKAGE_TARGET)

CMake Error at packaging/nsis/CMakeLists.txt:199 (add_custom_command):
  Error evaluating generator expression:

    $&lt; TARGET_FILE:wireshark&gt;

  No target &quot;wireshark&quot;
Call Stack (most recent call first):
  CMakeLists.txt:2320 (ADD_NSIS_PACKAGE_TARGET)

CMake Error at packaging/nsis/CMakeLists.txt:199 (add_custom_command):
  Error evaluating generator expression:

    $&lt; TARGET_FILE:wireshark&gt;

  No target &quot;wireshark&quot;
Call Stack (most recent call first):
  CMakeLists.txt:2320 (ADD_NSIS_PACKAGE_TARGET)

CMake Error at packaging/nsis/CMakeLists.txt:199 (add_custom_command):
  Error evaluating generator expression:

    $&lt; TARGET_FILE:wireshark&gt;

  No target &quot;wireshark&quot;
Call Stack (most recent call first):
  CMakeLists.txt:2320 (ADD_NSIS_PACKAGE_TARGET)

-- Generating done
-- Build files have been written to: C:/Development/wsbuild64</code></pre><p>I followed the instruction of the developer guide. Could someone tell me what to do?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">nsis cmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '16, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/adff8d731ffe044e74b218776bff2c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lumi&#39;s gravatar image" /><p>Lumi<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lumi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '16, 01:37</p></div></div><div id="comments-container-49424" class="comments-container"><span id="49426"></span><div id="comment-49426" class="comment"><div id="post-49426-score" class="comment-score"></div><div class="comment-text"><p>We'll need to see the complete output from the CMake generation step to help. Please update your question with that info.</p></div><div id="comment-49426-info" class="comment-info"><span class="comment-age">(21 Jan '16, 01:26)</span> grahamb ♦</div></div><span id="49427"></span><div id="comment-49427" class="comment"><div id="post-49427-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: done :)</p></div><div id="comment-49427-info" class="comment-info"><span class="comment-age">(21 Jan '16, 01:38)</span> Lumi</div></div></div><div id="comment-tools-49424" class="comment-tools"></div><div class="clear"></div><div id="comment-49424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49429"></span>

<div id="answer-container-49429" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49429-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have either not installed Qt, or not set the <code>QT5_BASE_DIR</code> env var for it:</p><pre><code>-- Qt5Core NOT FOUND
-- Qt5LinguistTools NOT FOUND
-- Qt5Multimedia NOT FOUND
-- Qt5PrintSupport NOT FOUND
-- Qt5Svg NOT FOUND
-- Qt5Widgets NOT FOUND
-- Qt5WinExtras NOT FOUND</code></pre><p>See the Developers Guide section on <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupQt">installing Qt</a>.</p><p>Arguably, the nsis installer target should be able to cope without Qt, but as that's the main item we're building I'm not sure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '16, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49429" class="comments-container"><span id="49431"></span><div id="comment-49431" class="comment"><div id="post-49431-score" class="comment-score"></div><div class="comment-text"><p>The QT5_BASE_DIR wasn't set properly. Thanks a lot!</p></div><div id="comment-49431-info" class="comment-info"><span class="comment-age">(21 Jan '16, 04:15)</span> Lumi</div></div></div><div id="comment-tools-49429" class="comment-tools"></div><div class="clear"></div><div id="comment-49429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

