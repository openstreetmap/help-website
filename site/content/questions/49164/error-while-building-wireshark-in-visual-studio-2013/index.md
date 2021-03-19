+++
type = "question"
title = "Error while building Wireshark in Visual Studio 2013"
description = '''I am trying to build Wireshark in my 64 bit Windows7 machine. I downloaded the source code(2.0.1) from downloads and configured and generated using CMake as per this documentation. All these were OK. Then I built the generated Wireshark.sln file in Visual Studio 2013. First it gave me an error becau...'''
date = "2016-01-13T04:34:00Z"
lastmod = "2016-01-14T04:22:00Z"
weight = 49164
keywords = [ "build_error", "flex", "windows7", "vs2013" ]
aliases = [ "/questions/49164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while building Wireshark in Visual Studio 2013](/questions/49164/error-while-building-wireshark-in-visual-studio-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49164-score" class="post-score" title="current number of votes">0</div><span id="post-49164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build Wireshark in my 64 bit Windows7 machine. I downloaded the source code(2.0.1) from <a href="https://www.wireshark.org/download.html">downloads</a> and configured and generated using CMake as per <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">this documentation</a>. All these were OK. Then I built the generated <code>Wireshark.sln</code> file in Visual Studio 2013. First it gave me an error because of which I had to install <code>flex 2.5.37</code>. Now while building, the previous error was solved and it tells :</p><pre><code>1&gt;------ Build started: Project: wiretap, Configuration: RelWithDebInfo Win32 ------
1&gt;  ascend_scanner.c
1&gt;E:/WShark/Build/wiretap/ascend_scanner_lex.h(111): warning C4005: &#39;yyconst&#39; : macro redefinition
1&gt;          E:/WShark/Build/wiretap/ascend_scanner.c(128) : see previous definition of &#39;yyconst&#39;
1&gt;E:/WShark/Build/wiretap/ascend_scanner_lex.h(195): warning C4028: formal parameter 1 different from declaration
1&gt;E:/WShark/Build/wiretap/ascend_scanner_lex.h(196): warning C4028: formal parameter 1 different from declaration
1&gt;E:/WShark/Build/wiretap/ascend_scanner.c(1793): error C2065: &#39;YY_DO_BEFORE_ACTION&#39; : undeclared identifier
1&gt;E:/WShark/Build/wiretap/ascend_scanner.c(2271): error C2065: &#39;YY_NEW_FILE&#39; : undeclared identifier
1&gt;E:/WShark/Build/wiretap/ascend_scanner.c(2590): error C2065: &#39;YY_NEW_FILE&#39; : undeclared identifier
1&gt;E:/WShark/Build/wiretap/ascend_scanner.c(2967): warning C4028: formal parameter 1 different from declaration
2&gt;------ Build started: Project: epan, Configuration: RelWithDebInfo Win32 ------
2&gt;LINK : fatal error LNK1181: cannot open input file &#39;..\run\RelWithDebInfo\wiretap-2.0.1.lib&#39;
3&gt;------ Build started: Project: wireshark, Configuration: RelWithDebInfo Win32 ------
3&gt;LINK : fatal error LNK1181: cannot open input file &#39;run\RelWithDebInfo\wireshark.lib&#39;
========== Build: 0 succeeded, 3 failed, 10 up-to-date, 0 skipped ==========</code></pre><p>Please help me to solve this :(..</p><p>EDIT: output of Cmake</p><pre><code>-- Generating build using CMake 3.4.1
-- Building for win32 using Visual Studio 12 2013
Working in E:\WShark\Wireshark-win32-libs-2.0

Tag 2015-12-11 found. Skipping.

-- No custom file found in E:/WShark/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- RelWithDebInfo: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.0.1, MaV: 2, MiV: 0, PL: 1, EV: .
-- Checking for c-compiler flag: /MP
-- Checking for c-compiler flag: /Zo
-- Checking for c-compiler flag: /w34295 /w34189
-- Checking for c++-compiler flag: /MP
-- Checking for c++-compiler flag: /Zo
-- Checking for c++-compiler flag: /w34295 /w34189
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;HtmlViewer;KERBEROS;LEX;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- AIRPCAP FOUND
-- AIRPCAP includes: E:/WShark/Wireshark-win32-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: E:/WShark/Wireshark-win32-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- CARES FOUND
-- CARES includes: E:/WShark/Wireshark-win32-libs-2.0/c-ares-1.9.1-1-win32ws/include
-- CARES libs: E:/WShark/Wireshark-win32-libs-2.0/c-ares-1.9.1-1-win32ws/lib/libcares-2.lib
-- GCRYPT FOUND
-- GCRYPT includes: E:/WShark/Wireshark-win32-libs-2.0/gnutls-3.2.15-2.7-win32ws/include
-- GCRYPT libs: E:/WShark/Wireshark-win32-libs-2.0/gnutls-3.2.15-2.7-win32ws/bin/libgcrypt-20.lib;E:/WShark/Wireshark-win32-libs-2.0/gnutls-3.2.15-2.7-win32ws/bin/libgpg-error-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- GEOIP FOUND
-- GEOIP includes: E:/WShark/Wireshark-win32-libs-2.0/GeoIP-1.6.6-win32ws/include
-- GEOIP libs: E:/WShark/Wireshark-win32-libs-2.0/GeoIP-1.6.6-win32ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- GLIB2 FOUND
-- GLIB2 includes: E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/glib-2.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/glib-2.0/include
-- GLIB2 libs: E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/glib-2.0
-- GMODULE2 libs: E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- GNUTLS FOUND
-- GNUTLS includes: E:/WShark/Wireshark-win32-libs-2.0/gnutls-3.2.15-2.7-win32ws/include
-- GNUTLS libs: E:/WShark/Wireshark-win32-libs-2.0/gnutls-3.2.15-2.7-win32ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gthread-2.0.lib
-- GTK2 FOUND
-- GTK2 includes: E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/gtk-2.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/freetype2;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/glib-2.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/glib-2.0/include;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/atk-1.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/gdk-pixbuf-2.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/cairo;E:/WShark/Wireshark-win32-libs-2.0/gtk2/include/pango-1.0;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gtk-2.0/include
-- GTK2 libs: E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/glib-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gobject-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/atk-1.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gio-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gthread-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gmodule-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gdk_pixbuf-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/cairo.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/pango-1.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/pangocairo-1.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/pangoft2-1.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gdk-win32-2.0.lib;E:/WShark/Wireshark-win32-libs-2.0/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- HTML_VIEWER NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- KERBEROS FOUND
-- KERBEROS includes: E:/WShark/Wireshark-win32-libs-2.0/kfw-3-2-2-i386-ws-vc6/include
-- KERBEROS libs: E:/WShark/Wireshark-win32-libs-2.0/kfw-3-2-2-i386-ws-vc6/lib/krb5_32.lib
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: C:/GnuWin32/bin/flex.exe
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- LUA FOUND
-- LUA includes: E:/WShark/Wireshark-win32-libs-2.0/lua5.2.3/include
-- LUA libs: E:/WShark/Wireshark-win32-libs-2.0/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- PCAP FOUND
-- PCAP includes: E:/WShark/Wireshark-win32-libs-2.0/WpdPack/Include
-- PCAP libs: E:/WShark/Wireshark-win32-libs-2.0/WpdPack/Lib/wpcap.lib
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- PORTAUDIO FOUND
-- PORTAUDIO includes: E:/WShark/Wireshark-win32-libs-2.0/portaudio_v19_2/include;E:/WShark/wireshark-win32-libs-2.0/portaudio_v19_2/src/common;E:/WShark/wireshark-win32-libs-2.0/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: C:/Perl/bin/perl.exe
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core FOUND
-- Qt5Core includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5LinguistTools includes: 
-- Qt5LinguistTools libs: 
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtMultimedia;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtNetwork;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtGui
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtPrintSupport;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtWidgets;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtGui;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtSvg;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtWidgets;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtGui;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtWidgets;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtGui;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5WinExtras FOUND
-- Qt5WinExtras includes: D:/QT/Qt5.4.0/5.4/msvc2013/include/;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtWinExtras;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtGui;D:/QT/Qt5.4.0/5.4/msvc2013/include/QtCore;D:/QT/Qt5.4.0/5.4/msvc2013//mkspecs/win32-msvc2013
-- Qt5WinExtras libs: Qt5::WinExtras
-- Qt5WinExtras definitions: -DQT_WINEXTRAS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Could NOT find SBC (missing:  SBC_INCLUDE_DIR SBC_LIBRARY) 
-- SBC NOT FOUND
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: C:/cygwin/bin/sed.exe
-- Could NOT find SETCAP (missing:  SETCAP_EXECUTABLE) 
-- SETCAP NOT FOUND
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: C:/cygwin/bin/bash.exe
-- SMI FOUND
-- SMI includes: E:/WShark/Wireshark-win32-libs-2.0/libsmi-svn-40773-win32ws/include
-- SMI libs: E:/WShark/Wireshark-win32-libs-2.0/libsmi-svn-40773-win32ws/lib/libsmi-2.lib
-- WINSPARKLE FOUND
-- WINSPARKLE includes: E:/WShark/Wireshark-win32-libs-2.0/WinSparkle-0.3-44-g2c8d9d3-win32ws
-- WINSPARKLE libs: E:/WShark/Wireshark-win32-libs-2.0/WinSparkle-0.3-44-g2c8d9d3-win32ws/WinSparkle.lib
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: C:/GnuWin32/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- ZLIB FOUND
-- ZLIB includes: E:/WShark/Wireshark-win32-libs-2.0/zlib-1.2.8-ws;E:/WShark/Build/zlib
-- ZLIB libs: zlib
-- C-Flags:  /MP /w34295 /w34189  /DWIN32 /D_WINDOWS /W3
-- CXX-Flags:  /MP /w34295 /w34189  /DWIN32 /D_WINDOWS /W3 /GR /EHsc 
-- Using Cygwin a2x
-- No custom file found in E:/WShark/wireshark/epan
-- No custom file found in E:/WShark/wireshark/ui/gtk
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
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.4.0)
 * Qt5Gui (required version &gt;= 5.4.0)
 * Qt5Multimedia
 * Qt5PrintSupport
 * Qt5Svg
 * Qt5Widgets
 * Qt5WinExtras
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
 * M
 * PkgConfig
 * SBC , SBC Codec for Bluetooth A2DP stream playing , &lt;www: http://git.kernel.org/cgit/bluetooth/sbc.git&gt;
 * SETCAP
 * YAPP
 * HTMLHelp

-- Configuring done
-- Generating done
-- Build files have been written to: E:/WShark/Build</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-flex" rel="tag" title="see questions tagged &#39;flex&#39;">flex</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-vs2013" rel="tag" title="see questions tagged &#39;vs2013&#39;">vs2013</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '16, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/a0fdf2d4c4f8a8cc417b620b2618bb3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anazz&#39;s gravatar image" /><p><span>Anazz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anazz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '16, 20:52</strong> </span></p></div></div><div id="comments-container-49164" class="comments-container"><span id="49167"></span><div id="comment-49167" class="comment"><div id="post-49167-score" class="comment-score"></div><div class="comment-text"><p>Please post the output of your CMake generation step, e.g. redirect the output to a file ( <code>cmake ... &gt; cmake.txt</code>) and post the file's contents here as a comment under your question.</p><p>Flex is normally installed as the Cygwin package flex.</p></div><div id="comment-49167-info" class="comment-info"><span class="comment-age">(13 Jan '16, 05:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49194"></span><div id="comment-49194" class="comment"><div id="post-49194-score" class="comment-score"></div><div class="comment-text"><p>Under cygwin package, flex version was 2.5.4. So I had to install 2.5.37 separately</p></div><div id="comment-49194-info" class="comment-info"><span class="comment-age">(13 Jan '16, 19:45)</span> <span class="comment-user userinfo">Anazz</span></div></div><span id="49195"></span><div id="comment-49195" class="comment"><div id="post-49195-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>: Added the output of CMake generation step</p></div><div id="comment-49195-info" class="comment-info"><span class="comment-age">(13 Jan '16, 20:53)</span> <span class="comment-user userinfo">Anazz</span></div></div><span id="49203"></span><div id="comment-49203" class="comment"><div id="post-49203-score" class="comment-score"></div><div class="comment-text"><p>The CMake output looks OK, although I haven't personally used the Gnuwin32 fle and bison packages. My cygwin flex is 2.5.39, why was there an issue with 2.5.4?</p><p>I note from your question:</p><blockquote>I downloaded the source code(2.0.1) from downloads</blockquote><p>so does that mean you used a source tarball rather than git? If so then you may have hit on a "bad" version, can you try to download the sources using git clone as described in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#_install_and_prepare_sources">Developers Guide</a>?</p></div><div id="comment-49203-info" class="comment-info"><span class="comment-age">(14 Jan '16, 00:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49206"></span><div id="comment-49206" class="comment"><div id="post-49206-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>: Yes, I downloaded manually.But it was specified as a stable release. In flex 2.5.4, the option <code>--header-file</code> to specify output header file is not supported which gave me <code>undefined flag</code> error.</p></div><div id="comment-49206-info" class="comment-info"><span class="comment-age">(14 Jan '16, 02:03)</span> <span class="comment-user userinfo">Anazz</span></div></div><span id="49207"></span><div id="comment-49207" class="comment not_top_scorer"><div id="post-49207-score" class="comment-score"></div><div class="comment-text"><p>Also, In the generated <code>.h</code> file, <code>#undef YY_NEW_FILE</code> and <code>#undef YY_DO_BEFORE_ACTION</code> is set. Commenting these two lines gives me a successful build. It is something related to flex it seems. Already reported here [<a href="http://sourceforge.net/p/flex/mailman/message/21495862/">http://sourceforge.net/p/flex/mailman/message/21495862/</a>]</p></div><div id="comment-49207-info" class="comment-info"><span class="comment-age">(14 Jan '16, 02:04)</span> <span class="comment-user userinfo">Anazz</span></div></div><span id="49213"></span><div id="comment-49213" class="comment not_top_scorer"><div id="post-49213-score" class="comment-score"></div><div class="comment-text"><p>Running lex involves some funky stuff, it's not run directly, but via the bash script tools\runlex.sh.</p><p>No-one else has reported this issue so either:</p><ol><li>There is an issue with using the GnuWin32 flex, but no-one else is using it so the issue is unknown (till now).</li><li>There is something different in your environment.</li></ol></div><div id="comment-49213-info" class="comment-info"><span class="comment-age">(14 Jan '16, 04:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-49164" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-49164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

