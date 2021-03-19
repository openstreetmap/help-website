+++
type = "question"
title = "VS2015, error C2220, Define ws_inet_pton not found !"
description = '''Hello, I have a probleme for Visual Studio 2015 when generate all file for Wireshark.  This is error:  3&amp;gt;C:&#92;Program Files (x86)&#92;Windows Kits&#92;8.1&#92;Include&#92;um&#92;ws2tcpip.h(563): error C2220: avertissement considéré comme une erreur - aucun fichier &#x27;object&#x27; généré 3&amp;gt;C:&#92;Program Files (x86)&#92;Windows Ki...'''
date = "2016-02-08T09:51:00Z"
lastmod = "2016-02-09T02:43:00Z"
weight = 49976
keywords = [ "vs2015", "c2220", "error" ]
aliases = [ "/questions/49976" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VS2015, error C2220, Define ws\_inet\_pton not found !](/questions/49976/vs2015-error-c2220-define-ws_inet_pton-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49976-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a probleme for Visual Studio 2015 when generate all file for Wireshark. This is error:</p><pre><code>3&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(563): error C2220: avertissement considéré comme une erreur - aucun fichier &#39;object&#39; généré
3&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(563): warning C4273: &#39;ws_inet_pton&#39; : liaison DLL incohérente
3&gt;  D:\Projets\wireshark\wsutil/inet_v6defs.h(41): note: voir la définition précédente de &#39;ws_inet_pton&#39;
3&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(579): warning C4030: première liste de paramètres formels plus longue que la seconde
3&gt;C:\Program Files (x86)\Windows Kits\8.1\Include\um\ws2tcpip.h(579): warning C4028: paramètre formel 2 différent de la déclaration</code></pre><p>Have you a solution for me ?</p><p>I have tested with Pragma warning on this, but my probleme it's already here !</p><p>Thank you for you help !</p></div><div id="question-tags" class="tags-container tags">vs2015 c2220 error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '16, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/0336e0743d6c4eeff40db1a46b245a09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tybbow%20Iskow&#39;s gravatar image" /><p>Tybbow Iskow<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tybbow Iskow has no accepted answers">0%</span></p></div></div><div id="comments-container-49976" class="comments-container"><span id="49978"></span><div id="comment-49978" class="comment"><div id="post-49978-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark are you trying to build?</p></div><div id="comment-49978-info" class="comment-info"><span class="comment-age">(08 Feb '16, 10:58)</span> Anders ♦</div></div><span id="49980"></span><div id="comment-49980" class="comment"><div id="post-49980-score" class="comment-score"></div><div class="comment-text"><p>The version of wireshark is 2.1.0. The last version. I use git clone for download source code.</p></div><div id="comment-49980-info" class="comment-info"><span class="comment-age">(08 Feb '16, 11:09)</span> Tybbow Iskow</div></div><span id="49983"></span><div id="comment-49983" class="comment"><div id="post-49983-score" class="comment-score"></div><div class="comment-text"><p>Can you edit your question, adding the output of the CMake generation step?</p><p>You can redirect the output to a file with <code>cmake -G ... 2&gt;&amp;1 &gt; cmake.txt</code></p></div><div id="comment-49983-info" class="comment-info"><span class="comment-age">(08 Feb '16, 11:34)</span> grahamb ♦</div></div><span id="49987"></span><div id="comment-49987" class="comment"><div id="post-49987-score" class="comment-score"></div><div class="comment-text"><p>I have a feeling I came across this problem when compiling with vs2015 the first time.</p></div><div id="comment-49987-info" class="comment-info"><span class="comment-age">(08 Feb '16, 14:53)</span> Anders ♦</div></div></div><div id="comment-tools-49976" class="comment-tools"></div><div class="clear"></div><div id="comment-49976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49993"></span>

<div id="answer-container-49993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49993-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Only very minor preparatory work for VS 2015 has been done, it's not really supported at the moment. When Qt release 5.6 with a version for use with VS2015 then support for VS2015 will be looked at again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49993" class="comments-container"><span id="50007"></span><div id="comment-50007" class="comment"><div id="post-50007-score" class="comment-score"></div><div class="comment-text"><p>I just built master with nmake with VS 2015 and that works. The problem may be related to this change made for nmake. <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=9cb09a242f752c775a6d11d12dcb84ef6d9264d2">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=9cb09a242f752c775a6d11d12dcb84ef6d9264d2</a></p></div><div id="comment-50007-info" class="comment-info"><span class="comment-age">(09 Feb '16, 04:28)</span> Anders ♦</div></div><span id="50009"></span><div id="comment-50009" class="comment"><div id="post-50009-score" class="comment-score"></div><div class="comment-text"><p>I was referring to CMake, but regardless of the build system, Qt is the hold-up.</p></div><div id="comment-50009-info" class="comment-info"><span class="comment-age">(09 Feb '16, 05:57)</span> grahamb ♦</div></div><span id="50062"></span><div id="comment-50062" class="comment"><div id="post-50062-score" class="comment-score"></div><div class="comment-text"><p>Hello, Thanks Grahamb..</p><p>So, after read log, i found that:</p><pre><code>-- Looking for inet_ntop
-- Looking for inet_ntop - not found</code></pre><p>and that :</p><pre><code> * Qt5Network (required version &gt;= 5.5.1)
 * Qt5Gui (required version &gt;= 5.5.1)</code></pre><p>:'(</p><pre><code>I give my Cmake log :

-- The C compiler identification is MSVC 19.0.23506.0
-- The CXX compiler identification is MSVC 19.0.23506.0
-- Check for working C compiler using: Visual Studio 14 2015 Win64
-- Check for working C compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64
-- Check for working CXX compiler using: Visual Studio 14 2015 Win64 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.3.2
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe  
-- Building for win64 using Visual Studio 14 2015 Win64
Working in D:\Projets\wireshark-win64-libs

Tag 2015-12-11 found. Skipping.

-- No custom file found in D:/Projets/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.02.0.1, MaV: 2, MiV: 1, PL: 0, EV: 2.0.1.
-- Checking for c-compiler flag: /MP
-- Performing Test C__MP_VALID
-- Performing Test C__MP_VALID - Success
-- Checking for c-compiler flag: /Zo
-- Performing Test C__Zo_VALID
-- Performing Test C__Zo_VALID - Success
-- Checking for c-compiler flag: /w34295 /w34189
-- Performing Test C__w34295_w34189_VALID
-- Performing Test C__w34295_w34189_VALID - Success
-- Checking for c++-compiler flag: /MP
-- Performing Test CPP__MP_VALID
-- Performing Test CPP__MP_VALID - Success
-- Checking for c++-compiler flag: /Zo
-- Performing Test CPP__Zo_VALID
-- Performing Test CPP__Zo_VALID - Success
-- Checking for c++-compiler flag: /w34295 /w34189
-- Performing Test CPP__w34295_w34189_VALID
-- Performing Test CPP__w34295_w34189_VALID - Success
-- Performing Test WS_LD_FLAG_VALID0
-- Performing Test WS_LD_FLAG_VALID0 - Failed
-- Performing Test WS_LD_FLAG_VALID1
-- Performing Test WS_LD_FLAG_VALID1 - Failed
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of off64_t
-- Check size of off64_t - failed
-- Looking for fseeko
-- Looking for fseeko - not found
-- Looking for unistd.h
-- Looking for unistd.h - not found
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;HtmlViewer;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: D:/Projets/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include  
-- AIRPCAP FOUND
-- AIRPCAP includes: D:/Projets/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: D:/Projets/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Found CARES: D:/Projets/wireshark-win64-libs/c-ares-1.9.1-1-win64ws/lib/libcares-2.lib  
-- CARES FOUND
-- CARES includes: D:/Projets/wireshark-win64-libs/c-ares-1.9.1-1-win64ws/include
-- CARES libs: D:/Projets/wireshark-win64-libs/c-ares-1.9.1-1-win64ws/lib/libcares-2.lib
-- Found GCRYPT: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.6.2&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: D:/Projets/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib  
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: D:/Projets/wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: D:/Projets/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GLIB2 FOUND
-- GLIB2 includes: D:/Projets/wireshark-win64-libs/gtk2/include/glib-2.0;D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;gmodule-2.0&#39;
-- Found GMODULE2: D:/Projets/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib  
-- GMODULE2 FOUND
-- GMODULE2 includes: D:/Projets/wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: D:/Projets/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;) 
-- GNUTLS FOUND
-- GNUTLS includes: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: D:/Projets/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;gthread-2.0&#39;
-- Found GTHREAD2: D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GTHREAD2 FOUND
-- GTHREAD2 includes: D:/Projets/wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Found GTK2_GTK: D:/Projets/wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib  
-- GTK2 FOUND
-- GTK2 includes: D:/Projets/wireshark-win64-libs/gtk2/include/gtk-2.0;D:/Projets/wireshark-win64-libs/gtk2/include;D:/Projets/wireshark-win64-libs/gtk2/include/freetype2;D:/Projets/wireshark-win64-libs/gtk2/include/glib-2.0;D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0/include;D:/Projets/wireshark-win64-libs/gtk2/include/atk-1.0;D:/Projets/wireshark-win64-libs/gtk2/include/gdk-pixbuf-2.0;D:/Projets/wireshark-win64-libs/gtk2/include/cairo;D:/Projets/wireshark-win64-libs/gtk2/include/pango-1.0;D:/Projets/wireshark-win64-libs/gtk2/lib/gtk-2.0/include
-- GTK2 libs: D:/Projets/wireshark-win64-libs/gtk2/lib/glib-2.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/gobject-2.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/atk-1.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/gdk_pixbuf-2.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/cairo.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/pango-1.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/pangocairo-1.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/gdk-win32-2.0.lib;D:/Projets/wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Found Git: C:/Program Files/Git/cmd/git.exe (found version &quot;2.7.0.windows.1&quot;) 
-- Git FOUND
-- Git includes: 
-- Git libs: 
-- Found HtmlViewer: C:/Program Files/Internet Explorer/iexplore.exe  
-- HTML_VIEWER NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: D:/Projets/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib  
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: D:/Projets/wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: D:/Projets/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Found LEX: C:/Tools/Cygwin/bin/flex.exe  
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: C:/Tools/Cygwin/bin/flex.exe
-- Could NOT find LIBSSH (missing:  LIBSSH_LIBRARIES LIBSSH_INCLUDE_DIRS LIBSSH_VERSION) (Required is at least version &quot;0.6&quot;)
-- LIBSSH NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Found LUA: D:/Projets/wireshark-win64-libs/lua5.2.3/lua52.lib (found version &quot;502&quot;) 
-- LUA FOUND
-- LUA includes: D:/Projets/wireshark-win64-libs/lua5.2.3/include
-- LUA libs: D:/Projets/wireshark-win64-libs/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- Found PCAP: D:/Projets/wireshark-win64-libs/WpdPack/Include  
-- Looking for pcap_open_dead
-- Looking for pcap_open_dead - found
-- Looking for pcap_freecode
-- Looking for pcap_freecode - found
-- Looking for pcap_breakloop
-- Looking for pcap_breakloop - found
-- Looking for pcap_create
-- Looking for pcap_create - found
-- Looking for pcap_datalink_name_to_val
-- Looking for pcap_datalink_name_to_val - found
-- Looking for pcap_datalink_val_to_description
-- Looking for pcap_datalink_val_to_description - found
-- Looking for pcap_datalink_val_to_name
-- Looking for pcap_datalink_val_to_name - found
-- Looking for pcap_findalldevs
-- Looking for pcap_findalldevs - found
-- Looking for pcap_free_datalinks
-- Looking for pcap_free_datalinks - found
-- Looking for pcap_get_selectable_fd
-- Looking for pcap_get_selectable_fd - not found
-- Looking for pcap_lib_version
-- Looking for pcap_lib_version - found
-- Looking for pcap_list_datalinks
-- Looking for pcap_list_datalinks - found
-- Looking for pcap_set_datalink
-- Looking for pcap_set_datalink - found
-- Looking for bpf_image
-- Looking for bpf_image - found
-- Looking for pcap_setsampling
-- Looking for pcap_setsampling - found
-- Looking for pcap_set_tstamp_precision
-- Looking for pcap_set_tstamp_precision - not found
-- Looking for pcap_open
-- Looking for pcap_open - found
-- PCAP FOUND
-- PCAP includes: D:/Projets/wireshark-win64-libs/WpdPack/Include
-- PCAP libs: D:/Projets/wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- Found POD: C:/Tools/Cygwin/bin/pod2man  
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- checking for one of the modules &#39;portaudio-2.0&#39;
-- Found PORTAUDIO: D:/Projets/wireshark-win64-libs/portaudio_v19_2/include  
-- PORTAUDIO FOUND
-- PORTAUDIO includes: D:/Projets/wireshark-win64-libs/portaudio_v19_2/include;D:/Projets/wireshark-win64-libs/portaudio_v19_2/src/common;D:/Projets/wireshark-win64-libs/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- Found Perl: C:/Tools/Cygwin/bin/perl.exe (found version &quot;5.22.1&quot;) 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: C:/Tools/Cygwin/bin/perl.exe
-- Found PythonInterp: C:/Tools/Python/python.exe (found suitable version &quot;2.7.11&quot;, minimum required is &quot;2&quot;) 
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core FOUND
-- Qt5Core includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5LinguistTools includes: 
-- Qt5LinguistTools libs: 
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtMultimedia;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtNetwork;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtGui
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtPrintSupport;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtWidgets;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtGui;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtSvg;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtWidgets;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtGui;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtWidgets;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtGui;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5WinExtras FOUND
-- Qt5WinExtras includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtWinExtras;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtGui;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5WinExtras libs: Qt5::WinExtras
-- Qt5WinExtras definitions: -DQT_WINEXTRAS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Could NOT find SBC (missing:  SBC_INCLUDE_DIR SBC_LIBRARY) 
-- SBC NOT FOUND
-- Found SED: C:/Tools/Cygwin/bin/sed.exe  
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: C:/Tools/Cygwin/bin/sed.exe
-- Could NOT find SETCAP (missing:  SETCAP_EXECUTABLE) 
-- SETCAP NOT FOUND
-- Found SH: C:/Tools/Cygwin/bin/bash.exe  
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: C:/Tools/Cygwin/bin/bash.exe
-- Found SMI: D:/Projets/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib  
-- SMI FOUND
-- SMI includes: D:/Projets/wireshark-win64-libs/libsmi-svn-40773-win64ws/include
-- SMI libs: D:/Projets/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- Found WINSPARKLE: D:/Projets/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib  
-- WINSPARKLE FOUND
-- WINSPARKLE includes: D:/Projets/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws
-- WINSPARKLE libs: D:/Projets/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib
-- Found YACC: C:/Tools/Cygwin/bin/bison.exe  
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: C:/Tools/Cygwin/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- Looking for inflatePrime
-- Looking for inflatePrime - not found
-- Found ZLIB: zlib  
-- ZLIB FOUND
-- ZLIB includes: D:/Projets/wireshark-win64-libs/zlib-1.2.8-ws;D:/Projets/wsbuild/zlib
-- ZLIB libs: zlib
-- C-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3
-- CXX-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3 /GR /EHsc 
-- Warnings as errors: /WX
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - not found
-- Looking for arpa/nameser.h
-- Looking for arpa/nameser.h - not found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - not found
-- Looking for fcntl.h
-- Looking for fcntl.h - found
-- Looking for getopt.h
-- Looking for getopt.h - not found
-- Looking for grp.h
-- Looking for grp.h - not found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - not found
-- Looking for netdb.h
-- Looking for netdb.h - not found
-- Looking for portaudio.h
-- Looking for portaudio.h - not found
-- Looking for pwd.h
-- Looking for pwd.h - not found
-- Looking for sys/ioctl.h
-- Looking for sys/ioctl.h - not found
-- Looking for sys/param.h
-- Looking for sys/param.h - not found
-- Looking for sys/socket.h
-- Looking for sys/socket.h - not found
-- Looking for sys/sockio.h
-- Looking for sys/sockio.h - not found
-- Looking for sys/stat.h
-- Looking for sys/stat.h - found
-- Looking for sys/time.h
-- Looking for sys/time.h - not found
-- Looking for sys/utsname.h
-- Looking for sys/utsname.h - not found
-- Looking for sys/wait.h
-- Looking for sys/wait.h - not found
-- Looking for unistd.h
-- Looking for unistd.h - not found
-- Looking for windows.h
-- Looking for windows.h - found
-- Looking for winsock2.h
-- Looking for winsock2.h - found
-- Looking for chown
-- Looking for chown - not found
-- Looking for dladdr
-- Looking for dladdr - not found
-- Looking for floorl
-- Looking for floorl - found
-- Looking for lrint
-- Looking for lrint - found
-- Looking for getaddrinfo
-- Looking for getaddrinfo - not found
-- Looking for gethostbyname
-- Looking for gethostbyname - not found
-- Looking for gethostbyname2
-- Looking for gethostbyname2 - not found
-- Looking for getopt_long
-- Looking for getopt_long - not found
-- Looking for getprotobynumber
-- Looking for getprotobynumber - not found
-- Looking for inet_aton
-- Looking for inet_aton - not found
-- Looking for inet_ntop
-- Looking for inet_ntop - not found
-- Looking for issetugid
-- Looking for issetugid - not found
-- Looking for mkdtemp
-- Looking for mkdtemp - not found
-- Looking for mkstemp
-- Looking for mkstemp - not found
-- Looking for popcount
-- Looking for popcount - not found
-- Looking for setresgid
-- Looking for setresgid - not found
-- Looking for setresuid
-- Looking for setresuid - not found
-- Looking for strptime
-- Looking for strptime - not found
-- Looking for sysconf
-- Looking for sysconf - not found
-- Performing Test HAVE_SA_LEN
-- Performing Test HAVE_SA_LEN - Failed
-- Performing Test HAVE_ST_FLAGS
-- Performing Test HAVE_ST_FLAGS - Failed
-- Performing Test HAVE_TM_ZONE
-- Performing Test HAVE_TM_ZONE - Failed
-- Looking for tzname
-- Looking for tzname - not found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- No custom file found in D:/Projets/wireshark/asn1
-- Found python module asn2wrs: D:\Projets\wireshark\tools\asn2wrs.py
-- Found LYNX: C:/Tools/Cygwin/bin/lynx.exe  
-- Found XSLTPROC: C:/Tools/Cygwin/bin/xsltproc.exe  
-- Found XMLLINT: C:/Tools/Cygwin/bin/xmllint.exe  
-- Using Cygwin a2x
-- Found ASCIIDOC: C:/Tools/Cygwin/bin/bash.exe;/cygdrive/d/Projets/wireshark/tools/runa2x.sh  
-- No custom file found in D:/Projets/wireshark/epan
-- Found python module make-dissector-reg: D:\Projets\wireshark\tools\make-dissector-reg.py
-- Looking for emmintrin.h
-- Looking for emmintrin.h - found
-- Looking for nmmintrin.h
-- Looking for nmmintrin.h - found
-- No custom file found in D:/Projets/wireshark/ui/gtk
-- docdir: 
-- Checking for 64-bit off_t
-- Checking for 64-bit off_t - present with _fseeki64
-- Checking for fseeko/ftello
-- 
-- The following OPTIONAL packages have been found:

 * AIRPCAP
 * CARES
 * GCRYPT (required version &gt;= 1.4.2)
 * GEOIP
 * GMODULE2
 * GNUTLS (required version &gt;= 2.12.0)
 * GTK2
 * Git
 * HtmlViewer
 * KERBEROS
 * LUA
 * PCAP
 * POD
 * PORTAUDIO
 * Perl
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.5.1)
 * Qt5Gui (required version &gt;= 5.5.1)
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
 * LIBSSH (required version &gt;= 0.6) , libssh is library for ssh connections and it is needed to build sshdump , 
 * M
 * PkgConfig
 * SBC , SBC Codec for Bluetooth A2DP stream playing , 
 * SETCAP
 * YAPP
 * HTMLHelp

-- Configuring done
-- Generating done
-- Build files have been written to: D:/Projets/wsbuild</code></pre></div><div id="comment-50062-info" class="comment-info"><span class="comment-age">(10 Feb '16, 09:54)</span> Tybbow Iskow</div></div><span id="50093"></span><div id="comment-50093" class="comment"><div id="post-50093-score" class="comment-score"></div><div class="comment-text"><p>As you can see from the CMake generation output you have used a VS2103 build of Qt:</p><blockquote>-- Qt5Core FOUND -- Qt5Core includes: C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/include/QtCore;C:/Tools/Qt/Qt5.5.1/5.5/msvc2013_64/.//mkspecs/win32-msvc2013</blockquote><p>So even if the compilation issues are fixed up, which may be down to the wrong version of Qt, it won't run because the Qt version uses a different compiler to yours.</p></div><div id="comment-50093-info" class="comment-info"><span class="comment-age">(11 Feb '16, 02:37)</span> grahamb ♦</div></div><span id="50097"></span><div id="comment-50097" class="comment"><div id="post-50097-score" class="comment-score"></div><div class="comment-text"><p>I forgot to mention that my working nmake build was without Qt.</p></div><div id="comment-50097-info" class="comment-info"><span class="comment-age">(11 Feb '16, 06:45)</span> Anders ♦</div></div></div><div id="comment-tools-49993" class="comment-tools"></div><div class="clear"></div><div id="comment-49993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

