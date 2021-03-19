+++
type = "question"
title = "issue of wireshark compiling with Cmake under WIN7 64BIT"
description = '''I tried to compile wireshark source code by Cmake,some error happened,do i lack some component?could you like to give me some suggestions with the error script show behind the environment setting  the environment setting is as below call &quot;C:&#92;Program Files (x86)&#92;Microsoft Visual Studio 12.0&#92;VC&#92;vcvars...'''
date = "2016-06-11T23:26:00Z"
lastmod = "2016-06-15T13:51:00Z"
weight = 53359
keywords = [ "compile", "cmake" ]
aliases = [ "/questions/53359" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [issue of wireshark compiling with Cmake under WIN7 64BIT](/questions/53359/issue-of-wireshark-compiling-with-cmake-under-win7-64bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53359-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to compile wireshark source code by Cmake,some error happened,do i lack some component?could you like to give me some suggestions with the error script show behind the environment setting</p><p><strong>the environment setting is as below</strong></p><pre><code>call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; x86_amd64
set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\SecVersion\wireshark
set CYGWIN=nodosfilewarning
set WIRESHARK_CYGWIN_INSTALL_PATH=E:\Software\Cygwin
set WIRESHARK_TARGET_PLATFORM=win64
set QT5_BASE_DIR=E:\Software\QT\5.6\msvc2013_64
e:
cd  E:\Wireshark_Plugin\SecVersion\build</code></pre><p><strong>error script is as below:</strong></p><pre><code>cmake -DENABLE_CHM_GUIDES=on  -DENABLE_CAP=OFF  -DENABLE_GTK3=OFF -DENABLE_APPLICATION_BUNDLE=OFF -G &quot;Visual Studio 12 Win64&quot; ..\wireshark
pause

   140&gt;Done Building Project &quot;E:\Wireshark_Plugin\SecVersion\build\copy_qt_dlls
       .vcxproj&quot; (default targets).
    12&gt;Done Building Project &quot;E:\Wireshark_Plugin\SecVersion\build\copy_qt_dlls
       .vcxproj.metaproj&quot; (default targets).
     2&gt;Project &quot;E:\Wireshark_Plugin\SecVersion\build\ALL_BUILD.vcxproj.metaproj
       &quot; (2) is building &quot;E:\Wireshark_Plugin\SecVersion\build\ALL_BUILD.vcxpro
       j&quot; (141) on node 2 (default targets).
   141&gt;PrepareForBuild:
         Creating directory &quot;x64\RelWithDebInfo\ALL_BUILD\&quot;.
         Creating directory &quot;x64\RelWithDebInfo\ALL_BUILD\ALL_BUILD.tlog\&quot;.
       InitializeBuildStatus:
         Creating &quot;x64\RelWithDebInfo\ALL_BUILD\ALL_BUILD.tlog\unsuccessfulbuil
         d&quot; because &quot;AlwaysCreate&quot; was specified.
       CustomBuild:
         Building Custom Rule E:/Wireshark_Plugin/SecVersion/wireshark/CMakeLis
         ts.txt
         CMake does not need to re-run because E:\Wireshark_Plugin\SecVersion\b
         uild\CMakeFiles\generate.stamp is up-to-date.
       FinalizeBuildStatus:
         Deleting file &quot;x64\RelWithDebInfo\ALL_BUILD\ALL_BUILD.tlog\unsuccessfu
         lbuild&quot;.
         Touching &quot;x64\RelWithDebInfo\ALL_BUILD\ALL_BUILD.tlog\ALL_BUILD.lastbu
         ildstate&quot;.
   141&gt;Done Building Project &quot;E:\Wireshark_Plugin\SecVersion\build\ALL_BUILD.vc
       xproj&quot; (default targets).
     2&gt;Done Building Project &quot;E:\Wireshark_Plugin\SecVersion\build\ALL_BUILD.vc
       xproj.metaproj&quot; (default targets).
     1&gt;Done Building Project &quot;E:\Wireshark_Plugin\SecVersion\build\Wireshark.sl
       n&quot; (default targets) -- FAILED.

Build FAILED.

       &quot;E:\Wireshark_Plugin\SecVersion\build\Wireshark.sln&quot; (default target) (1
       ) -&gt;
       &quot;E:\Wireshark_Plugin\SecVersion\build\docbook\release_notes_html.vcxproj
       .metaproj&quot; (default target) (45) -&gt;
       &quot;E:\Wireshark_Plugin\SecVersion\build\docbook\release_notes_html.vcxproj
       &quot; (default target) (93) -&gt;
       (CustomBuild target) -&gt;
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCo
       mmon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 9009. [E:
       \Wireshark_Plugin\SecVersion\build\docbook\release_notes_html.vcxproj]

    0 Warning(s)
    1 Error(s)</code></pre></div><div id="question-tags" class="tags-container tags">compile cmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '16, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/1445b0c2e6369c9b39c7802df15a2299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Water&#39;s gravatar image" /><p>Water<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Water has no accepted answers">0%</span></p></div></div><div id="comments-container-53359" class="comments-container"><span id="53393"></span><div id="comment-53393" class="comment"><div id="post-53393-score" class="comment-score"></div><div class="comment-text"><p>I guess some configuration issue or software component missing.As other *.sln prject have compiled successfully.Does any of you,master,meet the same problem as I did.</p></div><div id="comment-53393-info" class="comment-info"><span class="comment-age">(13 Jun '16, 01:17)</span> Water</div></div></div><div id="comment-tools-53359" class="comment-tools"></div><div class="clear"></div><div id="comment-53359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53478"></span>

<div id="answer-container-53478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53478-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your CMake line is a bit odd, that's not what's in the Developer's Guide, until you have a regular build working please don't deviate from the Developer's Guide.</p><p>Apart from that I'll guess that the failure to build the release_notes_html target is likely to be missing Cygwin components.</p><p>Please post the output of your CMake generation step by redirecting it to a file, i.e. <code>cmake ... 2&gt;&amp;1 &gt; path\to\file.txt</code> and then posting the file contents here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53478" class="comments-container"><span id="54931"></span><div id="comment-54931" class="comment"><div id="post-54931-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb :</p><p>I appreciate your great support. Your comments are always helpful to me.</p><p>Following your suggestion, I output the CMake building procedure into logfiles. As the files are too large to post here. So I uploaded it on Cloud.http://pan.baidu.com/s/1dFbo7Bj</p><p>you can download it and have a check when you are available. Actually the wireshark executable file has been created and it can work,but in the building process,there is a lot of warnings and errors,I think there should be something wrong. Hope you can give me a few feedback.</p><p>Many Many thanks .Looking forward for your feedback.</p></div><div id="comment-54931-info" class="comment-info"><span class="comment-age">(17 Aug '16, 19:26)</span> Water</div></div><span id="54932"></span><div id="comment-54932" class="comment"><div id="post-54932-score" class="comment-score"></div><div class="comment-text"><pre><code>-- The C compiler identification is MSVC 18.0.40629.0
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
Working in E:\Wireshark_Plugin\SecVersion\wireshark\wireshark-win64-libs

Tag 2016-05-10 found. Skipping.

-- No custom file found in E:/Wireshark_Plugin/SecVersion/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.0-git, MaV: 2, MiV: 1, PL: 0, EV: -git.
-- Found PythonInterp: C:/Python27/python.exe (found version &quot;2.7.8&quot;) 
-- Found python module asn2wrs: E:\Wireshark_Plugin\SecVersion\wireshark\tools\asn2wrs.py
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
-- Packagelist: AIRPCAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include  
-- AIRPCAP FOUND
-- AIRPCAP includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Found CARES: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib  
-- CARES FOUND
-- CARES includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/c-ares-1.11.0-win64ws/include
-- CARES libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib
-- Found GCRYPT: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.6.2&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib  
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GLIB2 FOUND
-- GLIB2 includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/glib-2.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- Found GMODULE2: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib  
-- GMODULE2 FOUND
-- GMODULE2 includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;) 
-- GNUTLS FOUND
-- GNUTLS includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- Found GTHREAD2: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GTHREAD2 FOUND
-- GTHREAD2 includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Found GTK2_GTK: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib  
-- GTK2 FOUND
-- GTK2 includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/gtk-2.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/freetype2;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/glib-2.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0/include;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/atk-1.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/gdk-pixbuf-2.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/cairo;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/include/pango-1.0;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gtk-2.0/include
-- GTK2 libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/glib-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gobject-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/atk-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gdk_pixbuf-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/cairo.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/pango-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/pangocairo-1.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gdk-win32-2.0.lib;E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Found Git: C:/Program Files/Git/cmd/git.exe (found version &quot;2.8.3.windows.1&quot;) 
-- Git FOUND
-- Git includes: 
-- Git libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib  
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Found LEX: E:/Software/Cygwin/bin/flex.exe  
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: E:/Software/Cygwin/bin/flex.exe
-- Found LIBSSH: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libssh-0.7.2-win64ws/lib/ssh.lib (found suitable version &quot;0.7.2&quot;, minimum required is &quot;0.6&quot;) 
-- LIBSSH FOUND
-- LIBSSH includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libssh-0.7.2-win64ws/include
-- LIBSSH libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libssh-0.7.2-win64ws/lib/ssh.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Found LUA: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/lua5.2.3/lua52.lib (found version &quot;502&quot;) 
-- LUA FOUND
-- LUA includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/lua5.2.3/include
-- LUA libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- Found PCAP: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WpdPack/Include  
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
-- PCAP includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WpdPack/Include
-- PCAP libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- Found POD: E:/Software/Cygwin/bin/pod2man  
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- Found PORTAUDIO: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/portaudio_v19_2/include  
-- PORTAUDIO FOUND
-- PORTAUDIO includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/portaudio_v19_2/include;E:/Wireshark_Plugin/SecVersion/wireshark/wireshark-win64-libs/portaudio_v19_2/src/common;E:/Wireshark_Plugin/SecVersion/wireshark/wireshark-win64-libs/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- Found Perl: E:/Software/Cygwin/bin/perl.exe (found version &quot;5.22.1&quot;) 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: E:/Software/Cygwin/bin/perl.exe
-- Found PythonInterp: C:/Python27/python.exe (found suitable version &quot;2.7.8&quot;, minimum required is &quot;2&quot;) 
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core FOUND
-- Qt5Core includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5LinguistTools includes: 
-- Qt5LinguistTools libs: 
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtMultimedia;E:/Software/QT/5.6/msvc2013_64/include/QtNetwork;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013;E:/Software/QT/5.6/msvc2013_64/include/QtGui
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtPrintSupport;E:/Software/QT/5.6/msvc2013_64/include/QtWidgets;E:/Software/QT/5.6/msvc2013_64/include/QtGui;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtSvg;E:/Software/QT/5.6/msvc2013_64/include/QtWidgets;E:/Software/QT/5.6/msvc2013_64/include/QtGui;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtWidgets;E:/Software/QT/5.6/msvc2013_64/include/QtGui;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5WinExtras FOUND
-- Qt5WinExtras includes: E:/Software/QT/5.6/msvc2013_64/include/;E:/Software/QT/5.6/msvc2013_64/include/QtWinExtras;E:/Software/QT/5.6/msvc2013_64/include/QtGui;E:/Software/QT/5.6/msvc2013_64/include/QtCore;E:/Software/QT/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5WinExtras libs: Qt5::WinExtras
-- Qt5WinExtras definitions: -DQT_WINEXTRAS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Could NOT find SBC (missing:  SBC_INCLUDE_DIR SBC_LIBRARY) 
-- SBC NOT FOUND
-- Found SED: E:/Software/Cygwin/bin/sed.exe  
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: E:/Software/Cygwin/bin/sed.exe
-- Found SH: E:/Software/Cygwin/bin/bash.exe  
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: E:/Software/Cygwin/bin/bash.exe
-- Found SMI: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib  
-- SMI FOUND
-- SMI includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libsmi-svn-40773-win64ws/include
-- SMI libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- Found WINSPARKLE: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib  
-- WINSPARKLE FOUND
-- WINSPARKLE includes: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws
-- WINSPARKLE libs: E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib
-- Found YACC: E:/Software/Cygwin/bin/bison.exe  
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: E:/Software/Cygwin/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- Looking for inflatePrime
-- Looking for inflatePrime - not found
-- Found ZLIB: zlib  
-- ZLIB FOUND
-- ZLIB includes: E:/Wireshark_Plugin/SecVersion/wireshark/wireshark-win64-libs/zlib-1.2.8-ws;E:/Wireshark_Plugin/SecVersion/newBuild/zlib
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
-- Looking for ifaddrs.h
-- Looking for ifaddrs.h - not found
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
-- Looking for getopt_long
-- Looking for getopt_long - not found
-- Looking for getprotobynumber
-- Looking for getprotobynumber - not found
-- Looking for getifaddrs
-- Looking for getifaddrs - not found
-- Looking for inet_aton
-- Looking for inet_aton - not found
-- Looking for inet_ntop
-- Looking for inet_ntop - not found
-- Looking for inet_pton
-- Looking for inet_pton - not found
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
-- Performing Test HAVE_SOCKADDR_SA_LEN
-- Performing Test HAVE_SOCKADDR_SA_LEN - Failed
-- Performing Test HAVE_STAT_ST_FLAGS
-- Performing Test HAVE_STAT_ST_FLAGS - Failed
-- Performing Test HAVE_STRUCT_TM_TM_ZONE
-- Performing Test HAVE_STRUCT_TM_TM_ZONE - Failed</code></pre></div><div id="comment-54932-info" class="comment-info"><span class="comment-age">(17 Aug '16, 19:29)</span> Water</div></div><span id="54933"></span><div id="comment-54933" class="comment"><div id="post-54933-score" class="comment-score"></div><div class="comment-text"><p>And i also post a few of the generate build files log here.</p></div><div id="comment-54933-info" class="comment-info"><span class="comment-age">(17 Aug '16, 19:30)</span> Water</div></div><span id="54934"></span><div id="comment-54934" class="comment"><div id="post-54934-score" class="comment-score"></div><div class="comment-text"><p><code> 生成启动时间为 2016/8/17 23:43:24。</code></p><p><code></code></p><p><code>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1c542.vcxproj”(默认目标)。</code></p><code></code><p>PrepareForBuild:</p><p>正在创建目录“cmTC_1c542.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_1c542.dir\Debug\cmTC_1c542.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_1c542.dir\Debug\cmTC_1c542.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D WS_LD_FLAG_VALID0 /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_1c542.dir\Debug\" /Fd"cmTC_1c542.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\src.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D WS_LD_FLAG_VALID0 /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_1c542.dir\Debug\" /Fd"cmTC_1c542.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\src.c</p><p>src.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_1c542.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib "\WX -Wl,--as-needed" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_1c542.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_1c542.lib" /MACHINE:X64 /machine:x64 cmTC_1c542.dir\Debug\src.obj</p><p>LINK : fatal error LNK1104: cannot open file '\WX -Wl,--as-needed.obj' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1c542.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1c542.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1c542.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>LINK : fatal error LNK1104: cannot open file '\WX -Wl,--as-needed.obj' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1c542.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.27</p><p>Source file was: int main() { return 0;} Performing C SOURCE FILE Test WS_LD_FLAG_VALID1 failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_b93a4.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:24。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b93a4.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_b93a4.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_b93a4.dir\Debug\cmTC_b93a4.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_b93a4.dir\Debug\cmTC_b93a4.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D WS_LD_FLAG_VALID1 /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_b93a4.dir\Debug\" /Fd"cmTC_b93a4.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\src.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D WS_LD_FLAG_VALID1 /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_b93a4.dir\Debug\" /Fd"cmTC_b93a4.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\src.c</p><p>src.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_b93a4.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib "\WX -pie" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_b93a4.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_b93a4.lib" /MACHINE:X64 /machine:x64 cmTC_b93a4.dir\Debug\src.obj</p><p>LINK : fatal error LNK1104: cannot open file '\WX -pie.obj' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b93a4.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b93a4.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b93a4.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>LINK : fatal error LNK1104: cannot open file '\WX -pie.obj' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b93a4.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.26</p><p>Source file was: int main() { return 0;} Determining size of off64_t failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_5a2ee.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:26。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_5a2ee.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_5a2ee.dir\Debug\cmTC_5a2ee.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_5a2ee.dir\Debug\cmTC_5a2ee.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D _LARGEFILE64_SOURCE=1 /D HAVE_SYS_TYPES_H /D HAVE_STDINT_H /D HAVE_STDDEF_H /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5a2ee.dir\Debug\" /Fd"cmTC_5a2ee.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D _LARGEFILE64_SOURCE=1 /D HAVE_SYS_TYPES_H /D HAVE_STDINT_H /D HAVE_STDDEF_H /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5a2ee.dir\Debug\" /Fd"cmTC_5a2ee.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c</p><p>OFF64_T.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(19): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(20): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(21): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(22): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(23): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(19): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(20): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(21): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(22): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CheckTypeSize\OFF64_T.c(23): error C2065: 'off64_t' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5a2ee.vcxproj]</p><pre><code>0 个警告
5 个错误</code></pre><p>已用时间 00:00:00.22</p><p>E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CheckTypeSize/OFF64_T.c:</p><h1 id="include-sys-types.h">include &lt;sys types.h=""&gt;</h1><h1 id="include-stdint.h">include &lt;stdint.h&gt;</h1><h1 id="include-stddef.h">include &lt;stddef.h&gt;</h1><h1 id="undef-key">undef KEY</h1><h1 id="if-definedi386">if defined(<strong>i386)</strong></h1><strong></strong><h1 id="define-key-i386">define KEY '<em>','</em>','i','3','8','6'</h1></strong><h1 id="elif-definedx86_64"><strong>elif defined(</strong>x86_64)</h1><h1 id="define-key-x86_64">define KEY '<em>','</em>','x','8','6','_','6','4'</h1><h1 id="elif-definedppc">elif defined(<strong>ppc</strong>)</h1><h1 id="define-key-ppc">define KEY '<em>','</em>','p','p','c','<em>','</em>'</h1><h1 id="elif-definedppc64">elif defined(<strong>ppc64</strong>)</h1><h1 id="define-key-ppc64">define KEY '<em>','</em>','p','p','c','6','4','<em>','</em>'</h1><h1 id="endif">endif</h1><h1 id="define-size-sizeofoff64_t">define SIZE (sizeof(off64_t))</h1><p>char info_size[] = {'I', 'N', 'F', 'O', ':', 's','i','z','e','[', ('0' + ((SIZE / 10000)%10)), ('0' + ((SIZE / 1000)%10)), ('0' + ((SIZE / 100)%10)), ('0' + ((SIZE / 10)%10)), ('0' + (SIZE % 10)), ']',</p><h1 id="ifdef-key">ifdef KEY</h1><p>' ','k','e','y','[', KEY, ']',</p><h1 id="endif-1">endif</h1><p>'\0'};</p><h1 id="ifdef-classic_c">ifdef <strong>CLASSIC_C</strong></h1><p>int main(argc, argv) int argc; char <em>argv[];</em></p><em></em><h1 id="else">else</h1></em><p><em>int main(int argc, char</em> argv[])</p><h1 id="endif-2">endif</h1><p>{ int require = 0; require += info_size[argc]; (void)argv; return require; }</p><p>Determining if the function fseeko exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_6c2f3.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:27。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_6c2f3.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_6c2f3.dir\Debug\cmTC_6c2f3.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_6c2f3.dir\Debug\cmTC_6c2f3.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=fseeko /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_6c2f3.dir\Debug\" /Fd"cmTC_6c2f3.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=fseeko /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_6c2f3.dir\Debug\" /Fd"cmTC_6c2f3.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>CheckFunctionExists.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_6c2f3.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_6c2f3.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_6c2f3.lib" /MACHINE:X64 /machine:x64 cmTC_6c2f3.dir\Debug\CheckFunctionExists.obj</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol fseeko referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_6c2f3.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol fseeko referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_6c2f3.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_6c2f3.vcxproj]</p><pre><code>0 个警告
2 个错误</code></pre><p>已用时间 00:00:00.34</p><p>Determining if the include file unistd.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_2ad04.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:27。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_2ad04.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_2ad04.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_2ad04.dir\Debug\cmTC_2ad04.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_2ad04.dir\Debug\cmTC_2ad04.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_2ad04.dir\Debug\" /Fd"cmTC_2ad04.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_2ad04.dir\Debug\" /Fd"cmTC_2ad04.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'unistd.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_2ad04.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_2ad04.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_2ad04.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'unistd.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_2ad04.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.23</p><p>Determining if the heimdal_version exist failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_b5aab.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:29。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b5aab.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_b5aab.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_b5aab.dir\Debug\cmTC_b5aab.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_b5aab.dir\Debug\cmTC_b5aab.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\kfw-3-2-2-x64-ws\include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_b5aab.dir\Debug\" /Fd"cmTC_b5aab.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckSymbolExists.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\kfw-3-2-2-x64-ws\include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_b5aab.dir\Debug\" /Fd"cmTC_b5aab.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckSymbolExists.c</p><p>CheckSymbolExists.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckSymbolExists.c(8): error C2065: 'heimdal_version' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b5aab.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b5aab.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b5aab.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckSymbolExists.c(8): error C2065: 'heimdal_version' : undeclared identifier [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_b5aab.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.43</p><p>File E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/CheckSymbolExists.c: / <em></em> /</p><h1 id="include-krb5.h">include &lt;krb5.h&gt;</h1><p>int main(int argc, char* <em>argv) { (void)argv;</em></p><em></em><h1 id="ifndef-heimdal_version">ifndef heimdal_version</h1></em><p><em>return ((int</em>)(&amp;heimdal_version))[argc];</p><h1 id="else-1">else</h1><p>(void)argc; return 0;</p><h1 id="endif-3">endif</h1><p>}</p><p>Determining if the function pcap_get_selectable_fd exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_1bd49.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:35。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_1bd49.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_1bd49.dir\Debug\cmTC_1bd49.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_1bd49.dir\Debug\cmTC_1bd49.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=pcap_get_selectable_fd /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_1bd49.dir\Debug\" /Fd"cmTC_1bd49.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=pcap_get_selectable_fd /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_1bd49.dir\Debug\" /Fd"cmTC_1bd49.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>CheckFunctionExists.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_1bd49.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib "E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Lib\x64\wpcap.lib" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_1bd49.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_1bd49.lib" /MACHINE:X64 /machine:x64 cmTC_1bd49.dir\Debug\CheckFunctionExists.obj</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol pcap_get_selectable_fd referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_1bd49.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol pcap_get_selectable_fd referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_1bd49.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_1bd49.vcxproj]</p><pre><code>0 个警告
2 个错误</code></pre><p>已用时间 00:00:00.33</p><p>Determining if the function pcap_set_tstamp_precision exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_df000.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:39。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_df000.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_df000.dir\Debug\cmTC_df000.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_df000.dir\Debug\cmTC_df000.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=pcap_set_tstamp_precision /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_df000.dir\Debug\" /Fd"cmTC_df000.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /I"E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Include" /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=pcap_set_tstamp_precision /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_df000.dir\Debug\" /Fd"cmTC_df000.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>CheckFunctionExists.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_df000.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib "E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs\WpdPack\Lib\x64\wpcap.lib" /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_df000.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_df000.lib" /MACHINE:X64 /machine:x64 cmTC_df000.dir\Debug\CheckFunctionExists.obj</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol pcap_set_tstamp_precision referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_df000.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>CheckFunctionExists.obj : error LNK2019: unresolved external symbol pcap_set_tstamp_precision referenced in function main [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj]</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_df000.exe : fatal error LNK1120: 1 unresolved externals [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_df000.vcxproj]</p><pre><code>0 个警告
2 个错误</code></pre><p>已用时间 00:00:00.30</p><p>Determining if the function inflatePrime exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_77ea8.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:40。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_77ea8.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_77ea8.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_77ea8.dir\Debug\cmTC_77ea8.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_77ea8.dir\Debug\cmTC_77ea8.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=inflatePrime /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_77ea8.dir\Debug\" /Fd"cmTC_77ea8.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D CHECK_FUNCTION_EXISTS=inflatePrime /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_77ea8.dir\Debug\" /Fd"cmTC_77ea8.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 "E:\Software\CMake\share\cmake-3.5\Modules\CheckFunctionExists.c"</p><p>CheckFunctionExists.c</p><p>Link:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\link.exe /ERRORREPORT:QUEUE /OUT:"E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\cmTC_77ea8.exe" /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib zlib.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_77ea8.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp/Debug/cmTC_77ea8.lib" /MACHINE:X64 /machine:x64 cmTC_77ea8.dir\Debug\CheckFunctionExists.obj</p><p>LINK : fatal error LNK1104: cannot open file 'zlib.lib' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_77ea8.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_77ea8.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_77ea8.vcxproj”(默认目标) (1) -&gt;</p><p>(Link 目标) -&gt;</p><p>LINK : fatal error LNK1104: cannot open file 'zlib.lib' [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_77ea8.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.29</p><p>Determining if the include file arpa/inet.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_c1239.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:41。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_c1239.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_c1239.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_c1239.dir\Debug\cmTC_c1239.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_c1239.dir\Debug\cmTC_c1239.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_c1239.dir\Debug\" /Fd"cmTC_c1239.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_c1239.dir\Debug\" /Fd"cmTC_c1239.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'arpa/inet.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_c1239.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_c1239.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_c1239.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'arpa/inet.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_c1239.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.25</p><p>Determining if the include file arpa/nameser.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_ddff7.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:41。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_ddff7.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_ddff7.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_ddff7.dir\Debug\cmTC_ddff7.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_ddff7.dir\Debug\cmTC_ddff7.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_ddff7.dir\Debug\" /Fd"cmTC_ddff7.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_ddff7.dir\Debug\" /Fd"cmTC_ddff7.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'arpa/nameser.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_ddff7.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_ddff7.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_ddff7.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'arpa/nameser.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_ddff7.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.22</p><p>Determining if the include file dlfcn.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_727e6.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:41。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_727e6.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_727e6.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_727e6.dir\Debug\cmTC_727e6.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_727e6.dir\Debug\cmTC_727e6.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_727e6.dir\Debug\" /Fd"cmTC_727e6.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_727e6.dir\Debug\" /Fd"cmTC_727e6.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'dlfcn.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_727e6.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_727e6.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_727e6.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'dlfcn.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_727e6.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.24</p><p>Determining if the include file getopt.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_9852c.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:42。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_9852c.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_9852c.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_9852c.dir\Debug\cmTC_9852c.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_9852c.dir\Debug\cmTC_9852c.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_9852c.dir\Debug\" /Fd"cmTC_9852c.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_9852c.dir\Debug\" /Fd"cmTC_9852c.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'getopt.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_9852c.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_9852c.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_9852c.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'getopt.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_9852c.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.23</p><p>Determining if the include file grp.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_5fdbf.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:43。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fdbf.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_5fdbf.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_5fdbf.dir\Debug\cmTC_5fdbf.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_5fdbf.dir\Debug\cmTC_5fdbf.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5fdbf.dir\Debug\" /Fd"cmTC_5fdbf.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5fdbf.dir\Debug\" /Fd"cmTC_5fdbf.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'grp.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fdbf.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fdbf.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fdbf.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'grp.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fdbf.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.24</p><p>Determining if the include file ifaddrs.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_76c31.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:43。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_76c31.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_76c31.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_76c31.dir\Debug\cmTC_76c31.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_76c31.dir\Debug\cmTC_76c31.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_76c31.dir\Debug\" /Fd"cmTC_76c31.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_76c31.dir\Debug\" /Fd"cmTC_76c31.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'ifaddrs.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_76c31.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_76c31.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_76c31.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'ifaddrs.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_76c31.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.29</p><p>Determining if the include file netinet/in.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_51cdf.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:45。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_51cdf.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_51cdf.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_51cdf.dir\Debug\cmTC_51cdf.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_51cdf.dir\Debug\cmTC_51cdf.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_51cdf.dir\Debug\" /Fd"cmTC_51cdf.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_51cdf.dir\Debug\" /Fd"cmTC_51cdf.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'netinet/in.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_51cdf.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_51cdf.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_51cdf.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'netinet/in.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_51cdf.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.24</p><p>Determining if the include file netdb.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_5fe7b.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:45。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fe7b.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_5fe7b.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_5fe7b.dir\Debug\cmTC_5fe7b.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_5fe7b.dir\Debug\cmTC_5fe7b.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5fe7b.dir\Debug\" /Fd"cmTC_5fe7b.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5fe7b.dir\Debug\" /Fd"cmTC_5fe7b.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'netdb.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fe7b.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fe7b.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fe7b.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'netdb.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5fe7b.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.24</p><p>Determining if the include file portaudio.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_7304f.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:46。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_7304f.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_7304f.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_7304f.dir\Debug\cmTC_7304f.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_7304f.dir\Debug\cmTC_7304f.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_7304f.dir\Debug\" /Fd"cmTC_7304f.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_7304f.dir\Debug\" /Fd"cmTC_7304f.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'portaudio.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_7304f.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_7304f.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_7304f.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'portaudio.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_7304f.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.43</p><p>Determining if the include file pwd.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_e78aa.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:46。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_e78aa.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_e78aa.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_e78aa.dir\Debug\cmTC_e78aa.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_e78aa.dir\Debug\cmTC_e78aa.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_e78aa.dir\Debug\" /Fd"cmTC_e78aa.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_e78aa.dir\Debug\" /Fd"cmTC_e78aa.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'pwd.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_e78aa.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_e78aa.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_e78aa.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'pwd.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_e78aa.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.32</p><p>Determining if the include file sys/ioctl.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_cb2be.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:47。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_cb2be.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_cb2be.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_cb2be.dir\Debug\cmTC_cb2be.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_cb2be.dir\Debug\cmTC_cb2be.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_cb2be.dir\Debug\" /Fd"cmTC_cb2be.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_cb2be.dir\Debug\" /Fd"cmTC_cb2be.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/ioctl.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_cb2be.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_cb2be.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_cb2be.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/ioctl.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_cb2be.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.22</p><p>Determining if the include file sys/param.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_70088.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:47。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_70088.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_70088.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_70088.dir\Debug\cmTC_70088.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_70088.dir\Debug\cmTC_70088.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_70088.dir\Debug\" /Fd"cmTC_70088.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_70088.dir\Debug\" /Fd"cmTC_70088.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/param.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_70088.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_70088.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_70088.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/param.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_70088.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.23</p><p>Determining if the include file sys/socket.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_5940b.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:47。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5940b.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_5940b.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_5940b.dir\Debug\cmTC_5940b.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_5940b.dir\Debug\cmTC_5940b.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5940b.dir\Debug\" /Fd"cmTC_5940b.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_5940b.dir\Debug\" /Fd"cmTC_5940b.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/socket.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5940b.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5940b.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5940b.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/socket.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_5940b.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre><p>已用时间 00:00:00.22</p><p>Determining if the include file sys/sockio.h exists failed with the following output: Change Dir: E:/Wireshark_Plugin/SecVersion/newBuild/CMakeFiles/CMakeTmp</p><p>Run Build Command:"C:/Program Files (x86)/MSBuild/12.0/bin/MSBuild.exe" "cmTC_d6c14.vcxproj" "/p:Configuration=Debug" "/p:VisualStudioVersion=12.0" Microsoft(R) 生成引擎版本 12.0.40629.0</p><p>[Microsoft .NET Framework 版本 4.0.30319.18408]</p><p>版权所有 (C) Microsoft Corporation。保留所有权利。</p><p>生成启动时间为 2016/8/17 23:43:48。</p><p>节点 1 上的项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_d6c14.vcxproj”(默认目标)。</p><p>PrepareForBuild:</p><p>正在创建目录“cmTC_d6c14.dir\Debug\”。</p><p>正在创建目录“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\Debug\”。</p><p>正在创建目录“cmTC_d6c14.dir\Debug\cmTC_d6c14.tlog\”。</p><p>InitializeBuildStatus:</p><p>正在创建“cmTC_d6c14.dir\Debug\cmTC_d6c14.tlog\unsuccessfulbuild”，因为已指定“AlwaysCreate”。</p><p>ClCompile:</p><p>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\x86_amd64\CL.exe /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_d6c14.dir\Debug\" /Fd"cmTC_d6c14.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>Microsoft (R) C/C++ Optimizing Compiler Version 18.00.40629 for x64</p><p>Copyright (C) Microsoft Corporation. All rights reserved.</p><p>cl /c /Zi /W3 /WX- /MP /Od /Ob0 /D WIN32 /D _WINDOWS /D _DEBUG /D "CMAKE_INTDIR=\"Debug\"" /D _MBCS /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo"cmTC_d6c14.dir\Debug\" /Fd"cmTC_d6c14.dir\Debug\vc120.pdb" /Gd /TC /errorReport:queue /Zo /w34295 /w34189 E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c</p><p>CheckIncludeFile.c</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/sockio.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_d6c14.vcxproj]</p><p>已完成生成项目“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_d6c14.vcxproj”(默认目标)的操作 - 失败。</p><p>生成失败。</p><p>“E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_d6c14.vcxproj”(默认目标) (1) -&gt;</p><p>(ClCompile 目标) -&gt;</p><p>E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1): fatal error C1083: Cannot open include file: 'sys/sockio.h': No such file or directory [E:\Wireshark_Plugin\SecVersion\newBuild\CMakeFiles\CMakeTmp\cmTC_d6c14.vcxproj]</p><pre><code>0 个警告
1 个错误</code></pre></code><p><code></code></p></div><div id="comment-54934-info" class="comment-info"><span class="comment-age">(17 Aug '16, 19:33)</span> Water</div></div><span id="54935"></span><div id="comment-54935" class="comment"><div id="post-54935-score" class="comment-score"></div><div class="comment-text"><p>in the CmakeError.log below ,警告 means warning ,错误 means error, 失败 means failure. sorry for trouble you so much</p></div><div id="comment-54935-info" class="comment-info"><span class="comment-age">(17 Aug '16, 19:34)</span> Water</div></div><span id="54945"></span><div id="comment-54945" class="comment not_top_scorer"><div id="post-54945-score" class="comment-score"></div><div class="comment-text"><p>The CMakeError.log isn't all that useful. The output of CMake is missing the vital bit which should appear at the end, something like:</p><pre><code>-- The following OPTIONAL packages have been found:

 * AIRPCAP
 * CARES
 * GCRYPT (required version &gt;= 1.4.2)
 * GEOIP
 * GMODULE2
 * GNUTLS (required version &gt;= 2.12.0)
 * GTK2
 * Git
 * KERBEROS
 * LIBSSH (required version &gt;= 0.6) , libssh is library for ssh connections and it is needed to build sshdump/ciscodump , &lt;www: https://www.libssh.org/get-it/&gt;
 * LUA
 * PCAP
 * POD
 * PORTAUDIO
 * Perl
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.6.1)
 * Qt5Gui (required version &gt;= 5.6.1)
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

-- Using C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\redist\1033\vcredist_x86.exe for the installer
-- Configuring done
-- Generating done
-- Build files have been written to: E:/Wireshark/build</code></pre><p>Rerun the CMake command again, redirecting to a file and post that.</p></div><div id="comment-54945-info" class="comment-info"><span class="comment-age">(18 Aug '16, 05:50)</span> grahamb ♦</div></div></div><div id="comment-tools-53478" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-53478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

