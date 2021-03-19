+++
type = "question"
title = "Error building wireshark"
description = '''Hi, I&#x27;m trying to build wireshark for first time on a Windows environment. I follow the developer&#x27;s guide and everything looks OK until step 2.2.12. A this time I have an error i do not understand. I put the description below. Can you help me understand it and solve it ? Thank you -- Configuring don...'''
date = "2017-07-31T09:54:00Z"
lastmod = "2017-08-02T10:39:00Z"
weight = 63262
keywords = [ "windows", "build", "wireshark" ]
aliases = [ "/questions/63262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error building wireshark](/questions/63262/error-building-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63262-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to build wireshark for first time on a Windows environment.</p><p>I follow the developer's guide and everything looks OK until step 2.2.12.</p><p>A this time I have an error i do not understand. I put the description below.</p><p>Can you help me understand it and solve it ? Thank you</p><pre><code>-- Configuring done
-- Generating done
-- Build files have been written to: C:/Nicolas/Dev/wsbuild64

c:\Nicolas\Dev\wsbuild64&gt;msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln
Microsoft (R) Build Engine, version 12.0.31101.0
[Microsoft .NET Framework, Version 4.0.30319.42000]
Copyright (C) Microsoft Corporation. Tous droits réservés.

La génération a démarré 31/07/2017 18:28:36.
     1&gt;Projet &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; sur le noud 1 (cibles par défaut).
     1&gt;c:\Nicolas\Dev\wsbuild64\Wireshark.sln.metaproj : error MSB4126: La configuration de solution spécifiée &quot;RelWithDebInfo|win64&quot; n&#39;est pas valide. Spécifiez une configuration de solution valide à l&#39;aide des propriétés Configuration et Platform (exemple : MSBuild.exe Solution.sln /p:Configuration=Debug /p:Platform=&quot;Any CPU&quot;) ou laissez ces propriétés vides si vous voulez utiliser la configuration de solution par défaut. [c:\Nicolas\Dev\wsbuild64\Wireshark.sln]
     1&gt;Génération du projet &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; terminée (cibles par défaut) -- ÉCHEC.

ÉCHEC de la build.

   &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; (cible par défaut) (1) -&gt;
   (ValidateSolutionConfiguration cible) -&gt;
     c:\Nicolas\Dev\wsbuild64\Wireshark.sln.metaproj : error MSB4126: La configuration de solution spécifiée &quot;RelWithDebInfo|win64&quot; n&#39;est pas valide. Spécifiez une configuration de solution valide à l&#39;aide des propriétés Configuration et Platform (exemple : MSBuild.exe Solution.sln /p:Configuration=Debug /p:Platform=&quot;Any CPU&quot;) ou laissez ces propriétés vides si vous voulez utiliser la configuration de solution par défaut. [c:\Nicolas\Dev\wsbuild64\Wireshark.sln]

0 Avertissement(s)
1 Erreur(s)

Temps écoulé 00:00:00.82</code></pre></div><div id="question-tags" class="tags-container tags">windows build wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '17, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/4d7366f0ba4d9f9e9c6a11f40ae1ab66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas2333&#39;s gravatar image" /><p>Nicolas2333<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas2333 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '17, 23:59</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-63262" class="comments-container"><span id="63266"></span><div id="comment-63266" class="comment"><div id="post-63266-score" class="comment-score"></div><div class="comment-text"><p>Can you show the complete CMake and msbuild output by redirecting them to files and posting them, i.e.</p><pre><code>cmake ... &gt;2&amp;1 &gt; cmake.txt</code></pre><p>and</p><pre><code>msbuild ... 2&gt;&amp;1 &gt; build.txt</code></pre><p>Can you also show your CMake and msbuild commands</p></div><div id="comment-63266-info" class="comment-info"><span class="comment-age">(31 Jul '17, 12:09)</span> grahamb ♦</div></div><span id="63304"></span><div id="comment-63304" class="comment"><div id="post-63304-score" class="comment-score"></div><div class="comment-text"><p>Hi, Here are the two command lines I used :</p><pre><code>cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\wireshark &gt;cmake.txt
msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln &gt;build.txt</code></pre><p>I still have the same error. I look the Wireshark.sln.metaproj but i do not know the build process enought to find the problem.</p><p>Can you help me ?</p><p>Here are the cmmake.txt file :</p><pre><code>-- Generating build using CMake 3.8.2
-- Building for win64 using Visual Studio 12 2013 Win64
Working in C:\Nicolas\Dev\wireshark-win64-libs
Tag 2017-07-19 found. Skipping.
-- No custom file found in C:/Nicolas/Dev/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- V: 2.5.0-YourExtraVersionInfo, MaV: 2, MiV: 5, PL: 0, EV: -YourExtraVersionInfo.
-- Found PythonInterp: C:/Python27/python.exe (found version &quot;2.7.11&quot;) 
-- Checking for c-compiler flag: /MP
-- Checking for c-compiler flag: /Zo
-- Checking for c-compiler flag: /w34295 /w34189 /wd4200
-- Checking for c++-compiler flag: /MP
-- Checking for c++-compiler flag: /Zo
-- Checking for c++-compiler flag: /w34295 /w34189 /wd4200
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;LZ4;LibXml2;M;NGHTTP2;PCAP;POD;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SETCAP;SH;SMI;SNAPPY;SPANDSP;WINSPARKLE;YACC;YAPP;ZLIB
-- AIRPCAP FOUND
-- AIRPCAP includes: C:/Nicolas/Dev/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: C:/Nicolas/Dev/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- CARES FOUND
-- CARES includes: C:/Nicolas/Dev/wireshark-win64-libs/c-ares-1.13.0-win64ws/include
-- CARES libs: C:/Nicolas/Dev/wireshark-win64-libs/c-ares-1.13.0-win64ws/lib/libcares-2.lib
-- GCRYPT FOUND
-- GCRYPT includes: C:/Nicolas/Dev/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/include
-- GCRYPT libs: C:/Nicolas/Dev/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/bin/libgcrypt-20.lib;C:/Nicolas/Dev/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- GEOIP FOUND
-- GEOIP includes: C:/Nicolas/Dev/wireshark-win64-libs/GeoIP-1.6.10-win64ws/include
-- GEOIP libs: C:/Nicolas/Dev/wireshark-win64-libs/GeoIP-1.6.10-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.22.0&#39;
-- GLIB2 FOUND
-- GLIB2 includes: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/include/glib-2.0;C:/Nicolas/Dev/wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- GNUTLS FOUND
-- GNUTLS includes: C:/Nicolas/Dev/wireshark-win64-libs/gnutls-3.4.11-1.35-win64ws/include
-- GNUTLS libs: C:/Nicolas/Dev/wireshark-win64-libs/gnutls-3.4.11-1.35-win64ws/bin/libgnutls-30.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: C:/Nicolas/Dev/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Git FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- KERBEROS FOUND
-- KERBEROS includes: C:/Nicolas/Dev/wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: C:/Nicolas/Dev/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- LEX FOUND
-- LEX executable: C:/cygwin64/bin/flex.exe
-- LIBSSH FOUND
-- LIBSSH includes: C:/Nicolas/Dev/wireshark-win64-libs/libssh-0.7.3-win64ws/include
-- LIBSSH libs: C:/Nicolas/Dev/wireshark-win64-libs/libssh-0.7.3-win64ws/lib/ssh.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- LUA FOUND
-- LUA includes: C:/Nicolas/Dev/wireshark-win64-libs/lua5.2.4/include
-- LUA libs: C:/Nicolas/Dev/wireshark-win64-libs/lua5.2.4/lua52.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lz4;liblz4&#39;
-- LZ4 FOUND
-- LZ4 includes: C:/Nicolas/Dev/wireshark-win64-libs/lz4-1.7.5-win64ws/include
-- LZ4 libs: C:/Nicolas/Dev/wireshark-win64-libs/lz4-1.7.5-win64ws/lib/lz4.lib
-- LIBXML2 FOUND
-- LibXml2 includes: C:/Nicolas/Dev/wireshark-win64-libs/libxml2-2.9.4-win64ws/include/libxml2
-- LibXml2 libs: C:/Nicolas/Dev/wireshark-win64-libs/libxml2-2.9.4-win64ws/lib/libxml2-2.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libnghttp2&#39;
-- NGHTTP2 FOUND
-- NGHTTP2 includes: C:/Nicolas/Dev/wireshark-win64-libs/nghttp2-1.14.0-win64ws/include
-- NGHTTP2 libs: C:/Nicolas/Dev/wireshark-win64-libs/nghttp2-1.14.0-win64ws/lib/nghttp2.lib
-- PCAP FOUND
-- PCAP includes: C:/Nicolas/Dev/wireshark-win64-libs/WpdPack/Include
-- PCAP libs: C:/Nicolas/Dev/wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- POD FOUND
-- PERL FOUND
-- Perl executable: C:/cygwin64/bin/perl.exe
-- Found PythonInterp: C:/Python27/python.exe (found suitable version &quot;2.7.11&quot;, minimum required is &quot;2&quot;) 
-- PYTHONINTERP FOUND
-- Qt5Core FOUND
-- Qt5Core includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtMultimedia;C:/Qt/5.6/msvc2013_64/include/QtNetwork;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013;C:/Qt/5.6/msvc2013_64/include/QtGui
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtPrintSupport;C:/Qt/5.6/msvc2013_64/include/QtWidgets;C:/Qt/5.6/msvc2013_64/include/QtGui;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtSvg;C:/Qt/5.6/msvc2013_64/include/QtWidgets;C:/Qt/5.6/msvc2013_64/include/QtGui;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtWidgets;C:/Qt/5.6/msvc2013_64/include/QtGui;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5WinExtras FOUND
-- Qt5WinExtras includes: C:/Qt/5.6/msvc2013_64/include/;C:/Qt/5.6/msvc2013_64/include/QtWinExtras;C:/Qt/5.6/msvc2013_64/include/QtGui;C:/Qt/5.6/msvc2013_64/include/QtCore;C:/Qt/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5WinExtras libs: Qt5::WinExtras
-- Qt5WinExtras definitions: -DQT_WINEXTRAS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- SBC FOUND
-- SBC includes: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/include
-- SBC libs: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/lib/sbc.lib
-- Could NOT find SETCAP (missing:  SETCAP_EXECUTABLE) 
-- SETCAP NOT FOUND
-- SH FOUND
-- SH executable: C:/cygwin64/bin/bash.exe
-- SMI FOUND
-- SMI includes: C:/Nicolas/Dev/wireshark-win64-libs/libsmi-svn-40773-win64ws/include
-- SMI libs: C:/Nicolas/Dev/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libsnappy&#39;
-- SNAPPY FOUND
-- SNAPPY includes: C:/Nicolas/Dev/wireshark-win64-libs/snappy-1.1.3-win64ws/include
-- SNAPPY libs: C:/Nicolas/Dev/wireshark-win64-libs/snappy-1.1.3-win64ws/lib/snappy.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;spandsp&#39;
-- SPANDSP FOUND
-- SPANDSP includes: C:/Nicolas/Dev/wireshark-win64-libs/spandsp-0.0.6-win64ws/include
-- SPANDSP libs: C:/Nicolas/Dev/wireshark-win64-libs/spandsp-0.0.6-win64ws/lib/spandsp.lib
-- WINSPARKLE FOUND
-- WINSPARKLE includes: C:/Nicolas/Dev/wireshark-win64-libs/WinSparkle-0.5.4/include
-- WINSPARKLE libs: C:/Nicolas/Dev/wireshark-win64-libs/WinSparkle-0.5.4/x64/Release/WinSparkle.lib
-- YACC FOUND
-- YACC executable: C:/cygwin64/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- Zlib might not be built yet; assume it contains inflatePrime
-- ZLIB FOUND
-- ZLIB includes: C:/Nicolas/Dev/wireshark-win64-libs/zlib-1.2.11-ws;C:/Nicolas/Dev/wsbuild64/zlib
-- ZLIB libs: zlib
-- C-Flags:  /MP /Zo /w34295 /w34189 /wd4200 /DWIN32 /D_WINDOWS /W3 
-- CXX-Flags:  /MP /Zo /w34295 /w34189 /wd4200 /DWIN32 /D_WINDOWS /W3 /GR /EHsc  
-- Warnings as errors: /WX
-- Could NOT find LYNX (missing:  LYNX_EXECUTABLE) 
-- Using Cygwin a2x
-- No custom file found in C:/Nicolas/Dev/wireshark/epan/crypt
-- No custom file found in C:/Nicolas/Dev/wireshark/epan/dissectors
-- No custom file found in C:/Nicolas/Dev/wireshark/epan/dissectors/asn1
-- No custom file found in C:/Nicolas/Dev/wireshark/ui/qt
-- docdir: 
-- The following OPTIONAL packages have been found:

 * AIRPCAP
 * CARES (required version &gt;= 1.5.0)
 * GEOIP
 * GMODULE2
 * GNUTLS (required version &gt;= 2.12.0)
 * Git
 * KERBEROS
 * LIBSSH (required version &gt;= 0.6), Library for implementing SSH clients, &lt;https://www.libssh.org/&gt;
   extcap remote SSH interfaces (sshdump, ciscodump)
 * LUA
 * LZ4, LZ4 is lossless compression algorithm used in some protocol (CQL...), &lt;http://www.lz4.org&gt;
   LZ4 decompression in CQL and Kafka dissectors
 * LibXml2
 * NGHTTP2, HTTP/2 C library and tools, &lt;https://nghttp2.org&gt;
   Header decompression in HTTP2
 * PCAP
 * POD
 * Perl
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.6.2)
 * Qt5Gui (required version &gt;= 5.6.2)
 * Qt5Multimedia
 * Qt5PrintSupport
 * Qt5Svg
 * Qt5Widgets
 * Qt5WinExtras
 * SBC, Bluetooth low-complexity, subband codec (SBC) decoder, &lt;https://git.kernel.org/pub/scm/bluetooth/sbc.git&gt;
   Support for playing SBC codec in RTP player
 * SH
 * SMI
 * SNAPPY, A fast compressor/decompressor from Google, &lt;http://google.github.io/snappy/&gt;
   Snappy decompression in CQL and Kafka dissectors
 * SPANDSP, a library of many DSP functions for telephony, &lt;http://www.soft-switch.org/&gt;
   Support for G.722 and G.726 codecs in RTP player
 * WINSPARKLE
 * ZLIB
 * XSLTPROC
 * ASCIIDOC
 * PythonInterp

-- The following REQUIRED packages have been found:

 * PowerShell
 * GCRYPT (required version &gt;= 1.4.2)
 * GLIB2
 * GTHREAD2
 * LEX
 * YACC

-- The following OPTIONAL packages have not been found:

 * CAP
 * Gettext
 * M
 * SETCAP
 * PkgConfig
 * YAPP, Yet Another Perl Parser compiler, &lt;http://search.cpan.org/dist/Parse-Yapp/&gt;
   tpg plugin
 * LYNX
 * HTMLHelp

-- Configuring done
-- Generating done
-- Build files have been written to: C:/Nicolas/Dev/wsbuild64</code></pre><p>And the build.txt file : Microsoft (R) Build Engine, version 12.0.31101.0 [Microsoft .NET Framework, Version 4.0.30319.42000] Copyright (C) Microsoft Corporation. Tous droits róervó.</p><pre><code>La gîòation a díarr 01/08/2017 18:02:13.
     1&gt;Projet &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; sur le noud 1 (cibles par dæaut).
     1&gt;c:\Nicolas\Dev\wsbuild64\Wireshark.sln.metaproj : error MSB4126: La configuration de solution spãifiå &quot;RelWithDebInfo|win64&quot; n&#39;est pas valide. Spãifiez une configuration de solution valide Šl&#39;aide des propriôó Configuration et Platform (exemple��SBuild.exe Solution.sln /p:Configuration=Debug /p:Platform=&quot;Any CPU&quot;) ou laissez ces propriôó vides si vous voulez utiliser la configuration de solution par dæaut. [c:\Nicolas\Dev\wsbuild64\Wireshark.sln]
     1&gt;Gîòation du projet &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; terminå (cibles par dæaut) -- уHEC.

уHEC de la build.

       &quot;c:\Nicolas\Dev\wsbuild64\Wireshark.sln&quot; (cible par dæaut) (1) -&gt;
       (ValidateSolutionConfiguration cible) -&gt; 
         c:\Nicolas\Dev\wsbuild64\Wireshark.sln.metaproj : error MSB4126: La configuration de solution spãifiå &quot;RelWithDebInfo|win64&quot; n&#39;est pas valide. Spãifiez une configuration de solution valide Šl&#39;aide des propriôó Configuration et Platform (exemple��SBuild.exe Solution.sln /p:Configuration=Debug /p:Platform=&quot;Any CPU&quot;) ou laissez ces propriôó vides si vous voulez utiliser la configuration de solution par dæaut. [c:\Nicolas\Dev\wsbuild64\Wireshark.sln]

    0 Avertissement(s)
    1 Erreur(s)

Temps ãoul 00:00:00.10</code></pre></div><div id="comment-63304-info" class="comment-info"><span class="comment-age">(01 Aug '17, 09:07)</span> Nicolas2333</div></div><span id="63306"></span><div id="comment-63306" class="comment"><div id="post-63306-score" class="comment-score"></div><div class="comment-text"><p>I think msbuild is complaining that you're using an invalid build configuration, but the command line you have looks correct to me.</p><p>Are you sure you have setup the command prompt correctly? What does the output of "cl" show?</p></div><div id="comment-63306-info" class="comment-info"><span class="comment-age">(01 Aug '17, 10:06)</span> grahamb ♦</div></div><span id="63308"></span><div id="comment-63308" class="comment"><div id="post-63308-score" class="comment-score"></div><div class="comment-text"><p>I would highly recommend that you check the cmake and msbuild stdio output of the <a href="https://buildbot.wireshark.org/wireshark-master/waterfall">buildbot</a> that most closely matches your development system. You can compare environment variables, etc. to see what's different or what you might have missed.</p></div><div id="comment-63308-info" class="comment-info"><span class="comment-age">(01 Aug '17, 11:04)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-63262" class="comment-tools"></div><div class="clear"></div><div id="comment-63262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63347"></span>

<div id="answer-container-63347" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63347-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I follow your advices and finally find the problem.</p><p>In fact, i first have installed cmake 3.9 instead of cmake 3.8.2. When i tried to build with cmake 3.9 i had to declare an environment variable named "PLATFORM" in order the cmake command is performed. It is this environment variable that generates the error in my msbuild command.</p><p>I delete this environment variable and build is successful.</p><p>Thank you very much for your help!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '17, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/4d7366f0ba4d9f9e9c6a11f40ae1ab66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas2333&#39;s gravatar image" /><p>Nicolas2333<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas2333 has no accepted answers">0%</span></p></div></div><div id="comments-container-63347" class="comments-container"><span id="63352"></span><div id="comment-63352" class="comment"><div id="post-63352-score" class="comment-score"></div><div class="comment-text"><p>PLATFORM is an env var set by Visual Studio when building for x64. It's not required for CMake although we do sanity check that PLATFORM (if set it will be "x64") agrees with the WIRESHARK_TARGET_PLATFORM variable and the generator specified to CMake.</p><p>CMake 3.9 is now OK to use with all versions back to 2.0</p></div><div id="comment-63352-info" class="comment-info"><span class="comment-age">(02 Aug '17, 12:48)</span> grahamb ♦</div></div></div><div id="comment-tools-63347" class="comment-tools"></div><div class="clear"></div><div id="comment-63347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

