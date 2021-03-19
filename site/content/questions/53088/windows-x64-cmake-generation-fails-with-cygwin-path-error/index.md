+++
type = "question"
title = "Windows x64 CMake generation fails with Cygwin path error"
description = '''Hi friends: I tried to compile wireshark at WIN7 with CMAKE under 64bit option,however the result is failed I can not figure out the reason,could you help me to have a check.I appreciate any suggestions  from you.Thanks a lot,i like this platform.below is the environment setting and command. call &quot;C...'''
date = "2016-05-31T19:50:00Z"
lastmod = "2016-06-01T01:55:00Z"
weight = 53088
keywords = [ "windows", "cmake", "x64", "cygwin" ]
aliases = [ "/questions/53088" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows x64 CMake generation fails with Cygwin path error](/questions/53088/windows-x64-cmake-generation-fails-with-cygwin-path-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53088-score" class="post-score" title="current number of votes">0</div><span id="post-53088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi friends: I tried to compile wireshark at WIN7 with CMAKE under 64bit option,however the result is failed I can not figure out the reason,could you help me to have a check.I appreciate any suggestions from you.Thanks a lot,i like this platform.below is the environment setting and command.</p><pre><code>call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; x86_amd64
set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\SecVersion\wireshark-master
set WIRESHARK_CYGWIN_INSTALL_PATH==E:\Software\Cygwin\bin
set WIRESHARK_TARGET_PLATFORM=win64
set QT5_BASE_DIR=E:\Software\QT\5.6\msvc2013_64
set  VISUALSTUDIOVERSION=12.0
set MSVC_VARIANT=MSVC2013EE
e:
cd  E:\Wireshark_Plugin\SecVersion\wsbuild
cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\wireshark-master
pause

E:\Wireshark_Plugin\SecVersion\wsbuild&gt;call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; x86_amd64

-- The C compiler identification is MSVC 18.0.40629.0
-- The CXX compiler identification is MSVC 18.0.40629.0
-- Check for working C compiler using: Visual Studio 12 2013 Win64
-- Check for working C compiler using: Visual Studio 12 2013 Win64 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler using: Visual Studio 12 2013 Win64
-- Check for working CXX compiler using: Visual Studio 12 2013 Win64 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.5.2
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe
-- Building for win64 using Visual Studio 12 2013 Win64
Working in E:\Wireshark_Plugin\SecVersion\wireshark-master\wireshark-win64-libs
Tag 2016-05-10 found. Skipping.
-- No custom file found in E:/Wireshark_Plugin/SecVersion/wireshark-master
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.0-git, MaV: 2, MiV: 1, PL: 0, EV: -git.
-- Found PythonInterp: C:/Python27/python.exe (found version &quot;2.7.8&quot;)
-- Found python module asn2wrs: E:\Wireshark_Plugin\SecVersion\wireshark-master\tools\asn2wrs.py
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
-- Performing Test CXX__MP_VALID
-- Performing Test CXX__MP_VALID - Success
-- Checking for c++-compiler flag: /Zo
-- Performing Test CXX__Zo_VALID
-- Performing Test CXX__Zo_VALID - Success
-- Checking for c++-compiler flag: /w34295 /w34189
-- Performing Test CXX__w34295_w34189_VALID
-- Performing Test CXX__w34295_w34189_VALID - Success
statuscheck linker flag - test linker flags: -Wl,--as-needed
-- Performing Test WS_LD_FLAG_VALID0
-- Performing Test WS_LD_FLAG_VALID0 - Failed
statuscheck linker flag - test linker flags: -pie
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
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP FOUND
-- AIRPCAP includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR)
-- CAP NOT FOUND
-- Found CARES: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib
-- CARES FOUND
-- CARES includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/c-ares-1.11.0-win64ws/include
-- CARES libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib
-- Found GCRYPT: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.
6.2&quot;, minimum required is &quot;1.4.2&quot;)
-- GCRYPT FOUND
-- GCRYPT includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-er
ror6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-
libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- GLIB2 FOUND
-- GLIB2 includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/glib-2.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- Found GMODULE2: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- GMODULE2 FOUND
-- GMODULE2 includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;)
-- GNUTLS FOUND
-- GNUTLS includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- Found GTHREAD2: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- GTHREAD2 FOUND
-- GTHREAD2 includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Found GTK2_GTK: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- GTK2 FOUND
-- GTK2 includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/gtk-2.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/freetype2;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/glib-2.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0/include;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/atk-1.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/gdk-pixbuf-2.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/cairo;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/include/pango-1.0;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gtk-2.0/include
-- GTK2 libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gobject-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/atk-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gdk_pixbuf-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/cairo.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/pango-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/pangocairo-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gdk-win32-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_
EXECUTABLE)
-- GETTEXT NOT FOUND
-- Could NOT find Git (missing:  GIT_EXECUTABLE)
-- Git NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: E:/Wireshark_Plugin/SecVersion/wireshark-master/Wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
CMake Error at cmake/modules/FindCygwin.cmake:59 (message):
  Cygwin installation path was not detected.  You can set it with WIRESHARK_CYGWIN_INSTALL_PATH environment variable.
Call Stack (most recent call first):
  cmake/modules/FindLEX.cmake:5 (INCLUDE)
  CMakeLists.txt:835 (find_package)

-- Configuring incomplete, errors occurred!
See also &quot;E:/Wireshark_Plugin/SecVersion/wsbuild/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;E:/Wireshark_Plugin/SecVersion/wsbuild/CMakeFiles/CMakeError.log&quot;.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span> <span class="post-tag tag-link-x64" rel="tag" title="see questions tagged &#39;x64&#39;">x64</span> <span class="post-tag tag-link-cygwin" rel="tag" title="see questions tagged &#39;cygwin&#39;">cygwin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/1445b0c2e6369c9b39c7802df15a2299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Water&#39;s gravatar image" /><p><span>Water</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Water has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 01:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53088" class="comments-container"></div><div id="comment-tools-53088" class="comment-tools"></div><div class="clear"></div><div id="comment-53088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53090"></span>

<div id="answer-container-53090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53090-score" class="post-score" title="current number of votes">0</div><span id="post-53090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Note I converted your "answer" to your nmake <a href="https://ask.wireshark.org/questions/52492/issue-of-compiling-wireshark-source-code-with-vs2013-under-64bit-option">question</a> to this new CMake question as that's how this site works.</p><p>I think the cause is right there in the error message:</p><pre><code>Cygwin installation path was not detected.  You can set it with WIRESHARK_CYGWIN_INSTALL_PATH environment variable.</code></pre><p>Your set of the environment variable has two <code>==</code>, so it actually sets the env var to <code>=E:\Software\Cygwin\bin</code>. Try this setting:</p><pre><code>set WIRESHARK_CYGWIN_INSTALL_PATH=E:\Software\Cygwin\bin</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 01:58</strong> </span></p></div></div><div id="comments-container-53090" class="comments-container"></div><div id="comment-tools-53090" class="comment-tools"></div><div class="clear"></div><div id="comment-53090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

