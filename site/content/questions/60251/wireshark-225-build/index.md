+++
type = "question"
title = "wireshark 2.2.5 build"
description = '''i was following the build procedure for 2.2.5 as shown in the Developers Guide Sect 2.2. is the installation of QT is mandatory?  or the copying of lib files should be fine? As i&#x27;m facing the below build issue: D:&#92;Development&#92;msbuild64&amp;gt;cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..&#92;w...'''
date = "2017-03-22T03:25:00Z"
lastmod = "2017-03-22T04:40:00Z"
weight = 60251
keywords = [ "build_error", "wireshark-2.2.5" ]
aliases = [ "/questions/60251" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark 2.2.5 build](/questions/60251/wireshark-225-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60251-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i was following the build procedure for 2.2.5 as shown in the Developers Guide Sect 2.2.</p><p>is the installation of QT is mandatory? or the copying of lib files should be fine?</p><p>As i'm facing the below build issue:</p><pre><code>D:\Development\msbuild64&gt;cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\wireshark
-- Generating build using CMake 3.7.2
-- Building for win64 using Visual Studio 12 2013 Win64
Working in D:\Development\WireShark\wireshark-win64-libs
Tag 2017-02-15 found. Skipping.
-- No custom file found in D:/Development/WireShark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- V: 2.3.0, MaV: 2, MiV: 3, PL: 0, EV: .
-- Found PythonInterp: C:/Python27/python.exe (found version &quot;2.7.11&quot;)
-- Found python module asn2wrs: D:\Development\WireShark\tools\asn2wrs.py
-- Checking for c-compiler flag: /MP
-- Performing Test C__MP_VALID
-- Performing Test C__MP_VALID - Success
-- Checking for c-compiler flag: /Zo
-- Performing Test C__Zo_VALID
-- Performing Test C__Zo_VALID - Failed
-- Checking for c-compiler flag: /w34295 /w34189 /wd4200
-- Performing Test C__w34295_w34189_wd4200_VALID
-- Performing Test C__w34295_w34189_wd4200_VALID - Success
-- Checking for c++-compiler flag: /MP
-- Performing Test CXX__MP_VALID
-- Performing Test CXX__MP_VALID - Success
-- Checking for c++-compiler flag: /Zo
-- Performing Test CXX__Zo_VALID
-- Performing Test CXX__Zo_VALID - Failed
-- Checking for c++-compiler flag: /w34295 /w34189 /wd4200
-- Performing Test CXX__w34295_w34189_wd4200_VALID
-- Performing Test CXX__w34295_w34189_wd4200_VALID - Success
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
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;LZ4;M;NGHTTP2;PCAP;POD;Perl;PythonInterp;Qt5Core;Qt5Ling
uistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;SNAPPY;SPANDSP;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: D:/Development/WireShark/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP FOUND
-- AIRPCAP includes: D:/Development/WireShark/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: D:/Development/WireShark/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Found PkgConfig: C:/cygwin64/bin/pkg-config.exe (found version &quot;0.29.1&quot;)
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR)
-- CAP NOT FOUND
-- Found CARES: D:/Development/WireShark/wireshark-win64-libs/c-ares-1.12.0-win64ws/lib/libcares-2.lib
-- CARES FOUND
-- CARES includes: D:/Development/WireShark/wireshark-win64-libs/c-ares-1.12.0-win64ws/include
-- CARES libs: D:/Development/WireShark/wireshark-win64-libs/c-ares-1.12.0-win64ws/lib/libcares-2.lib
-- Found GCRYPT: D:/Development/WireShark/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.7.6&quot;, minimum required is &quot;1.4.2&quot;)

-- GCRYPT FOUND
-- GCRYPT includes: D:/Development/WireShark/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/include
-- GCRYPT libs: D:/Development/WireShark/wireshark-win64-libs/libgcrypt-1.7.6-win64ws/bin/libgcrypt-20.lib;D:/Development/WireShark/wireshark-win64-libs/libgcrypt-1.7.6-w
in64ws/bin/libgpg-error6-0.lib
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: D:/Development/WireShark/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: D:/Development/WireShark/wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: D:/Development/WireShark/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Checking for one of the modules &#39;glib-2.0&gt;=2.22.0&#39;
-- Found GLIB2: D:/Development/WireShark/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- GLIB2 FOUND
-- GLIB2 includes: D:/Development/WireShark/wireshark-win64-libs/gtk2/include/glib-2.0;D:/Development/WireShark/wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: D:/Development/WireShark/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GMODULE2 libs: gmodule-2.0;glib-2.0;intl
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: D:/Development/WireShark/wireshark-win64-libs/gnutls-3.4.11-1.35-win64ws/bin/libgnutls-30.lib (found suitable version &quot;3.4.11&quot;, minimum required is &quot;2.12
.0&quot;)
-- GNUTLS FOUND
-- GNUTLS includes: D:/Development/WireShark/wireshark-win64-libs/gnutls-3.4.11-1.35-win64ws/include
-- GNUTLS libs: D:/Development/WireShark/wireshark-win64-libs/gnutls-3.4.11-1.35-win64ws/bin/libgnutls-30.lib
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GTHREAD2 libs: gthread-2.0;glib-2.0;intl
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE)
-- GETTEXT NOT FOUND
-- Found Git: C:/cygwin64/bin/git.exe (found version &quot;2.8.3&quot;)
-- Git FOUND
-- Git includes:
-- Git libs:
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: D:/Development/WireShark/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: D:/Development/WireShark/wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: D:/Development/WireShark/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Found LEX: C:/cygwin64/bin/flex.exe
-- LEX FOUND
-- LEX includes:
-- LEX libs:
-- LEX executable: C:/cygwin64/bin/flex.exe
-- Found LIBSSH: D:/Development/WireShark/wireshark-win64-libs/libssh-0.7.3-win64ws/lib/ssh.lib (found suitable version &quot;0.7.3&quot;, minimum required is &quot;0.6&quot;)
-- LIBSSH FOUND
-- LIBSSH includes: D:/Development/WireShark/wireshark-win64-libs/libssh-0.7.3-win64ws/include
-- LIBSSH libs: D:/Development/WireShark/wireshark-win64-libs/libssh-0.7.3-win64ws/lib/ssh.lib
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Found LUA: D:/Development/WireShark/wireshark-win64-libs/lua5.2.4/lua52.lib (found version &quot;502&quot;)
-- LUA FOUND
-- LUA includes: D:/Development/WireShark/wireshark-win64-libs/lua5.2.4/include
-- LUA libs: D:/Development/WireShark/wireshark-win64-libs/lua5.2.4/lua52.lib
-- Checking for one of the modules &#39;lz4;liblz4&#39;
-- Found LZ4: D:/Development/WireShark/wireshark-win64-libs/lz4-r131-win64ws/include
-- LZ4 FOUND
-- LZ4 includes: D:/Development/WireShark/wireshark-win64-libs/lz4-r131-win64ws/include
-- LZ4 libs: D:/Development/WireShark/wireshark-win64-libs/lz4-r131-win64ws/lib/lz4.lib
-- Could NOT find M (missing:  M_LIBRARY)
-- M NOT FOUND
-- Checking for one of the modules &#39;libnghttp2&#39;
-- Found Nghttp2: D:/Development/WireShark/wireshark-win64-libs/nghttp2-1.14.0-win64ws/include
-- NGHTTP2 FOUND
-- NGHTTP2 includes: D:/Development/WireShark/wireshark-win64-libs/nghttp2-1.14.0-win64ws/include
-- NGHTTP2 libs: D:/Development/WireShark/wireshark-win64-libs/nghttp2-1.14.0-win64ws/lib/nghttp2.lib
-- Found PCAP: D:/Development/WireShark/wireshark-win64-libs/WpdPack/Include
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
-- PCAP includes: D:/Development/WireShark/wireshark-win64-libs/WpdPack/Include
-- PCAP libs: D:/Development/WireShark/wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- Found POD: C:/cygwin64/bin/pod2man
-- POD FOUND
-- POD includes:
-- POD libs:
-- Found Perl: C:/Perl64/bin/perl.exe (found version &quot;5.20.1&quot;)
-- PERL FOUND
-- Perl includes:
-- Perl libs:
-- Perl executable: C:/Perl64/bin/perl.exe
-- Found PythonInterp: C:/Python27/python.exe (found suitable version &quot;2.7.11&quot;, minimum required is &quot;2&quot;)
-- PYTHONINTERP FOUND
-- PythonInterp includes:
-- PythonInterp libs:
CMake Error at C:/cygwin64/lib/cmake/Qt5Core/Qt5CoreConfig.cmake:27 (message):
  The imported target &quot;Qt5::Core&quot; references the file

     &quot;C:/cygwin64/include/qt5/&quot;

  but this file does not exist.  Possible reasons include:

  * The file was deleted, renamed, or moved to another location.

  * An install or uninstall procedure did not complete successfully.

  * The installation package was faulty and contained

     &quot;C:/cygwin64/lib/cmake/Qt5Core/Qt5CoreConfig.cmake&quot;

  but not all the files it references.

Call Stack (most recent call first):
  C:/cygwin64/lib/cmake/Qt5Core/Qt5CoreConfig.cmake:68 (_qt5_Core_check_file_exists)
  CMakeLists.txt:911 (find_package)

-- Configuring incomplete, errors occurred!
See also &quot;D:/Development/msbuild64/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;D:/Development/msbuild64/CMakeFiles/CMakeError.log&quot;.</code></pre></div><div id="question-tags" class="tags-container tags">build_error wireshark-2.2.5</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '17, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p>DhanuShalz<br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '17, 04:36</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60251" class="comments-container"></div><div id="comment-tools-60251" class="comment-tools"></div><div class="clear"></div><div id="comment-60251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60255"></span>

<div id="answer-container-60255" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60255-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Qt5 is mandatory for Windows 2.2.x or later builds and should be installed as per <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupQt">Sect 2.2.4</a> of the Developers Guide.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '17, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60255" class="comments-container"><span id="60298"></span><div id="comment-60298" class="comment"><div id="post-60298-score" class="comment-score"></div><div class="comment-text"><p>same error appears even after installing the QT5.6</p></div><div id="comment-60298-info" class="comment-info"><span class="comment-age">(23 Mar '17, 23:31)</span> DhanuShalz</div></div><span id="60300"></span><div id="comment-60300" class="comment"><div id="post-60300-score" class="comment-score"></div><div class="comment-text"><p>Did you delete the build dir and rerun the cmake step after adding Qt?</p></div><div id="comment-60300-info" class="comment-info"><span class="comment-age">(24 Mar '17, 02:28)</span> Anders ♦</div></div><span id="60301"></span><div id="comment-60301" class="comment"><div id="post-60301-score" class="comment-score"></div><div class="comment-text"><p>Did you set the required environment variables for QT5_BASE_DIR as in the Developers Guide <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">Section 2.2.10</a>?</p><p>As @Anders noted you might have to either delete CMakeCache.txt or delete the entire build directory to get the installed Qt version picked up by CMake.</p><p>If the CMake output is identical, then it would appear that CMake is picking up some Cygwin related Qt items which can't be used for the build. Please confirm if this is the case, if not please repost the output from the CMake generation step.</p></div><div id="comment-60301-info" class="comment-info"><span class="comment-age">(24 Mar '17, 02:41)</span> grahamb ♦</div></div></div><div id="comment-tools-60255" class="comment-tools"></div><div class="clear"></div><div id="comment-60255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

