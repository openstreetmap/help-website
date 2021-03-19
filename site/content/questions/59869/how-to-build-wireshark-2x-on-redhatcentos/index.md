+++
type = "question"
title = "How to build wireshark 2.x on Redhat/Centos"
description = '''Hi, I am trying to build wireshark 2.2.5 on centos 6.8. I am getting the following errors, any help would be greatly appreciated. When I execute &quot;make&quot; I get: [ 2%] Built target wsutil Unable to open /home/c.wiggum/wireshark/wireshark/.svn/entries version.h unchanged. [ 2%] Built target version [ 50...'''
date = "2017-03-06T13:03:00Z"
lastmod = "2017-03-07T11:06:00Z"
weight = 59869
keywords = [ "development", "build", "linux" ]
aliases = [ "/questions/59869" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to build wireshark 2.x on Redhat/Centos](/questions/59869/how-to-build-wireshark-2x-on-redhatcentos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59869-score" class="post-score" title="current number of votes">0</div><span id="post-59869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to build wireshark 2.2.5 on centos 6.8.</p><p>I am getting the following errors, any help would be greatly appreciated.</p><p>When I execute "make" I get:</p><pre><code>[  2%] Built target wsutil
Unable to open /home/c.wiggum/wireshark/wireshark/.svn/entries
version.h unchanged.
[  2%] Built target version
[ 50%] Built target dissectors
[ 50%] Built target lemon
[ 51%] Built target dfilter
[ 51%] Built target crypt
[ 51%] Built target dissectors-corba
[ 52%] Built target ftypes
[ 52%] Built target nghttp2
[ 53%] Built target wmem
[ 53%] Generating ascend.c
/usr/bin/yacc: e - line 4 of &quot;/home/c.wiggum/wireshark/wireshark/wiretap/ascend.y&quot;, syntax error
%pure-parser
^
make[2]: *** [wiretap/ascend.c] Error 1
make[2]: *** Deleting file `wiretap/ascend.c&#39;
make[1]: *** [wiretap/CMakeFiles/wiretap.dir/all] Error 2
make: *** [all] Error 2</code></pre><p>I installed byacc from the yum repository.</p><p>When I execute "make wireshark" I get:</p><pre><code>[  1%] Built target translations
[ 24%] Built target qtui
[ 24%] Building C object caputils/CMakeFiles/caputils.dir/capture-pcap-util.c.o
/home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.c:614:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration
 pcap_datalink_name_to_val(const char *name)
 ^
In file included from /usr/local/include/pcap.h:43:0,
                 from /home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.h:32,
                 from /home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.c:76:
/usr/local/include/pcap/pcap.h:405:14: note: previous declaration of ‘pcap_datalink_name_to_val’ was here
 PCAP_API int pcap_datalink_name_to_val(const char *);
              ^
/home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.c:629:1: error: static declaration of ‘pcap_datalink_val_to_name’ follows non-static declaration
 pcap_datalink_val_to_name(int dlt)
 ^
In file included from /usr/local/include/pcap.h:43:0,
                 from /home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.h:32,
                 from /home/c.wiggum/wireshark/wireshark/caputils/capture-pcap-util.c:76:
/usr/local/include/pcap/pcap.h:406:22: note: previous declaration of ‘pcap_datalink_val_to_name’ was here
 PCAP_API const char *pcap_datalink_val_to_name(int);
                      ^
make[3]: *** [caputils/CMakeFiles/caputils.dir/capture-pcap-util.c.o] Error 1
make[2]: *** [caputils/CMakeFiles/caputils.dir/all] Error 2
make[1]: *** [CMakeFiles/wireshark.dir/rule] Error 2
make: *** [wireshark] Error 2</code></pre><p>I download libpcap from tcpdump.org and compiled and installed libpcap.</p><p>Below is the output from cmake:</p><pre><code>-- Generating build using CMake 3.7.0-rc2
-- No custom file found in /home/c.wiggum/wireshark/wireshark
-- Configuration types: 
-- CMAKE_C_FLAGS_RELWITHDEBINFO: -O2 -g -DNDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: -O2 -g -DNDEBUG
-- V: 2.2.5, MaV: 2, MiV: 2, PL: 5, EV: .
-- Found PythonInterp: /usr/bin/python (found version &quot;2.6.6&quot;) 
-- Checking for c-compiler flag: -Wall
-- Checking for c-compiler flag: -Wextra
-- Checking for c-compiler flag: -Wendif-labels
-- Checking for c-compiler flag: -Wpointer-arith
-- Checking for c-compiler flag: -Wformat-security
-- Checking for c-compiler flag: -fwrapv
-- Checking for c-compiler flag: -fno-strict-overflow
-- Checking for c-compiler flag: -Wvla
-- Checking for c-compiler flag: -Waddress
-- Checking for c-compiler flag: -Wattributes
-- Checking for c-compiler flag: -Wdiv-by-zero
-- Checking for c-compiler flag: -Wignored-qualifiers
-- Checking for c-compiler flag: -Wpragmas
-- Checking for c-compiler flag: -Wno-overlength-strings
-- Checking for c-compiler flag: -Wno-long-long
-- Checking for c-compiler flag: -Wheader-guard
-- Checking for c-compiler flag: -fexcess-precision=fast
-- Checking for c-compiler flag: -Wc++-compat
-- Checking for c-compiler flag: -Wdeclaration-after-statement
-- Checking for c-compiler flag: -Wshadow
-- Checking for c-compiler flag: -Wno-pointer-sign
-- Checking for c-compiler flag: -Wold-style-definition
-- Checking for c-compiler flag: -Wstrict-prototypes
-- Checking for c-compiler flag: -Wlogical-op
-- Checking for c-compiler flag: -Wjump-misses-init
-- Checking for c-compiler flag: -Wunused-const-variable
-- Checking for c-compiler flag: -Wshorten-64-to-32
-- Checking for c-compiler flag: -Wc99-extensions
-- Checking for c++-compiler flag: -Wall
-- Checking for c++-compiler flag: -Wextra
-- Checking for c++-compiler flag: -Wendif-labels
-- Checking for c++-compiler flag: -Wpointer-arith
-- Checking for c++-compiler flag: -Wformat-security
-- Checking for c++-compiler flag: -fwrapv
-- Checking for c++-compiler flag: -fno-strict-overflow
-- Checking for c++-compiler flag: -Wvla
-- Checking for c++-compiler flag: -Waddress
-- Checking for c++-compiler flag: -Wattributes
-- Checking for c++-compiler flag: -Wdiv-by-zero
-- Checking for c++-compiler flag: -Wignored-qualifiers
-- Checking for c++-compiler flag: -Wpragmas
-- Checking for c++-compiler flag: -Wno-overlength-strings
-- Checking for c++-compiler flag: -Wno-long-long
-- Checking for c++-compiler flag: -Wheader-guard
-- Checking for c++-compiler flag: -fexcess-precision=fast
-- Packagelist: CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK3;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;NL;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;SBC;SED;SETCAP;SH;SMI;YACC;YAPP;ZLIB
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Could NOT find CARES (missing:  CARES_LIBRARY CARES_INCLUDE_DIR) 
-- CARES NOT FOUND
-- Could NOT find GCRYPT (missing:  GCRYPT_LIBRARY GCRYPT_INCLUDE_DIR) (Required is at least version &quot;1.4.2&quot;)
-- GCRYPT NOT FOUND
-- Checking for one of the modules &#39;geoip&#39;
-- Could NOT find GEOIP (missing:  GEOIP_LIBRARY GEOIP_INCLUDE_DIR) 
-- GEOIP NOT FOUND
-- GLIB2 FOUND
-- GLIB2 includes: /usr/include/glib-2.0;/usr/lib64/glib-2.0/include
-- GLIB2 libs: /usr/lib64/libglib-2.0.so
-- GMODULE2 FOUND
-- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib64/glib-2.0/include
-- GMODULE2 libs: gmodule-2.0;rt;glib-2.0
-- Checking for one of the modules &#39;gnutls&#39;
-- Could NOT find GNUTLS: Found unsuitable version &quot;&quot;, but required is at least &quot;2.12.0&quot; (found GNUTLS_LIBRARY-NOTFOUND)
-- GNUTLS NOT FOUND
-- GTHREAD2 FOUND
-- GTHREAD2 includes: /usr/include/glib-2.0;/usr/lib64/glib-2.0/include
-- GTHREAD2 libs: gthread-2.0;rt;glib-2.0
-- Could NOT find GTK3 (missing:  GTK3_LIBRARY GTK3_INCLUDE_DIR) 
-- GTK3 NOT FOUND
-- GETTEXT FOUND
-- Gettext includes: 
-- Gettext libs: 
-- Git FOUND
-- Git includes: 
-- Git libs: 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Could NOT find KERBEROS (missing:  KERBEROS_LIBRARY KERBEROS_INCLUDE_DIR) 
-- KERBEROS NOT FOUND
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: /usr/bin/flex
-- Could NOT find LIBSSH (missing:  LIBSSH_LIBRARIES LIBSSH_INCLUDE_DIRS LIBSSH_VERSION) (Required is at least version &quot;0.6&quot;)
-- LIBSSH NOT FOUND
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Could NOT find LUA (missing:  LUA_LIBRARY LUA_INCLUDE_DIR LUA_VERSION_NUM) 
-- LUA NOT FOUND
-- M FOUND
-- M includes: /usr/include
-- M libs: /usr/lib64/libm.so
-- Checking for modules &#39;libnl-3.0;libnl-genl-3.0;libnl-route-3.0&#39;
--   No package &#39;libnl-3.0&#39; found
--   No package &#39;libnl-genl-3.0&#39; found
--   No package &#39;libnl-route-3.0&#39; found
-- Checking for one of the modules &#39;libnl-2.0&#39;
-- Checking for one of the modules &#39;libnl-1&#39;
-- Could NOT find NL (missing:  NL_LIBRARY NL_INCLUDE_DIR) 
-- NL NOT FOUND
-- PCAP FOUND
-- PCAP includes: /usr/include
-- PCAP libs: /usr/lib64/libpcap.so
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- Could NOT find PORTAUDIO (missing:  PORTAUDIO_LIBRARY PORTAUDIO_INCLUDE_DIR) 
-- PORTAUDIO NOT FOUND
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: /usr/bin/perl
-- Found PythonInterp: /usr/bin/python (found suitable version &quot;2.6.6&quot;, minimum required is &quot;2&quot;) 
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core FOUND
-- Qt5Core includes: /home/c.wiggum/qtInstall/include/;/home/c.wiggum/qtInstall/include/QtCore;/home/c.wiggum/qtInstall/.//mkspecs/linux-g++
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5LinguistTools includes: 
-- Qt5LinguistTools libs: 
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: /home/c.wiggum/qtInstall/include/;/home/c.wiggum/qtInstall/include/QtMultimedia;/home/c.wiggum/qtInstall/include/QtNetwork;/home/c.wiggum/qtInstall/include/QtCore;/home/c.wiggum/qtInstall/.//mkspecs/linux-g++;/home/c.wiggum/qtInstall/include/QtGui;/usr/include
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: /home/c.wiggum/qtInstall/include/;/home/c.wiggum/qtInstall/include/QtPrintSupport;/home/c.wiggum/qtInstall/include/QtWidgets;/home/c.wiggum/qtInstall/include/QtGui;/home/c.wiggum/qtInstall/include/QtCore;/home/c.wiggum/qtInstall/.//mkspecs/linux-g++;/usr/include
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: /home/c.wiggum/qtInstall/include/;/home/c.wiggum/qtInstall/include/QtSvg;/home/c.wiggum/qtInstall/include/QtWidgets;/home/c.wiggum/qtInstall/include/QtGui;/home/c.wiggum/qtInstall/include/QtCore;/home/c.wiggum/qtInstall/.//mkspecs/linux-g++;/usr/include
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: /home/c.wiggum/qtInstall/include/;/home/c.wiggum/qtInstall/include/QtWidgets;/home/c.wiggum/qtInstall/include/QtGui;/home/c.wiggum/qtInstall/include/QtCore;/home/c.wiggum/qtInstall/.//mkspecs/linux-g++;/usr/include
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Could NOT find SBC (missing:  SBC_INCLUDE_DIR SBC_LIBRARY) 
-- SBC NOT FOUND
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: /bin/sed
-- SETCAP FOUND
-- SETCAP includes: 
-- SETCAP libs: 
-- SETCAP executable: /usr/sbin/setcap
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: /bin/bash
-- Could NOT find SMI (missing:  SMI_LIBRARY SMI_INCLUDE_DIR) 
-- SMI NOT FOUND
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: /usr/bin/yacc
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- ZLIB FOUND
-- ZLIB includes: /usr/include
-- ZLIB libs: /usr/lib64/libz.so
-- Checking for C++ 11 support (Required by Qt 5.7 and later)
-- C-Flags:  -Wall -Wextra -Wendif-labels -Wpointer-arith -Wformat-security -fwrapv -fno-strict-overflow -Wvla -Waddress -Wattributes -Wdiv-by-zero -Wignored-qualifiers -Wpragmas -Wno-overlength-strings -Wno-long-long -fexcess-precision=fast -Wc++-compat -Wdeclaration-after-statement -Wshadow -Wno-pointer-sign -Wold-style-definition -Wstrict-prototypes -Wlogical-op -Wjump-misses-init  -fvisibility=hidden
-- CXX-Flags:  -Wall -Wextra -Wendif-labels -Wpointer-arith -Wformat-security -fwrapv -fno-strict-overflow -Wvla -Waddress -Wattributes -Wdiv-by-zero -Wignored-qualifiers -Wpragmas -Wno-overlength-strings -Wno-long-long -fexcess-precision=fast  -std=c++11 
-- Warnings as errors: FALSE
-- Could NOT find LYNX (missing:  LYNX_EXECUTABLE) 
-- Could NOT find ASCIIDOC (missing:  RUNA2X) 
-- No custom file found in /home/c.wiggum/wireshark/wireshark/epan/crypt
-- No custom file found in /home/c.wiggum/wireshark/wireshark/epan/dissectors
-- No custom file found in /home/c.wiggum/wireshark/wireshark/epan/dissectors/asn1
-- Checking for c-compiler flag: -msse4.2
-- docdir: 
-- 
-- The following OPTIONAL packages have been found:

 * GMODULE2
 * Gettext
 * Git
 * PCAP
 * POD
 * PkgConfig
 * Perl
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.7.0)
 * Qt5Gui (required version &gt;= 5.7.0)
 * Qt5Multimedia
 * Qt5PrintSupport
 * Qt5Svg
 * Qt5Widgets
 * SED
 * SETCAP
 * SH
 * ZLIB
 * XSLTPROC
 * PythonInterp

-- The following REQUIRED packages have been found:

 * GLIB2
 * GTHREAD2
 * LEX
 * M
 * YACC

-- The following OPTIONAL packages have not been found:

 * CAP
 * CARES
 * GCRYPT (required version &gt;= 1.4.2)
 * GEOIP
 * GNUTLS (required version &gt;= 2.12.0)
 * GTK3
 * KERBEROS
 * LIBSSH (required version &gt;= 0.6) , libssh is library for ssh connections and it is needed to build sshdump/ciscodump , &lt;www: https://www.libssh.org/get-it/&gt;
 * LUA
 * NL
 * PORTAUDIO
 * SBC , SBC Codec for Bluetooth A2DP stream playing , &lt;www: http://git.kernel.org/cgit/bluetooth/sbc.git&gt;
 * SMI
 * YAPP
 * LYNX
 * ASCIIDOC

-- Configuring done
-- Generating done</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '17, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p><span>Rob B</span><br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-59869" class="comments-container"></div><div id="comment-tools-59869" class="comment-tools"></div><div class="clear"></div><div id="comment-59869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59870"></span>

<div id="answer-container-59870" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59870-score" class="post-score" title="current number of votes">0</div><span id="post-59870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob B has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you've got 2 separate issues here. <strong>Please split the 2nd issue into another question otherwise this is going to get really confusing.</strong></p><p>For the first problem, it appears that the <a href="https://stackoverflow.com/questions/33537935/syntax-error-when-using-byacc">yacc in RHEL/CentOS 6 is too old</a>.</p><p>I'm really surprised no one has complained before since there are a number of CentOS 6 users around.</p><p>One solution (and probably why there haven't been more complaints): I believe that the source tarballs contain the generated parsers. So if you build from them instead of building from git it should work. You may also have to use automake, etc., rather than cmake.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '17, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-59870" class="comments-container"><span id="59873"></span><div id="comment-59873" class="comment"><div id="post-59873-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm really surprised no one has complained before since there are a number of CentOS 6 users around.</p></blockquote><p>There are (at least) two enhanced YACC clones out there - Bison and Berkeley YACC. Current versions of both of them should support <code>%pure-parser</code>. It may be that the Bison in CentOS 6 supports it but the Berkeley YACC doesn't; if so, then, if you have Bison installed, it builds, but if you don't, the configure script and CMake pick (Berkeley) YACC, it doesn't.</p><p>Try installing Bison.</p></div><div id="comment-59873-info" class="comment-info"><span class="comment-age">(06 Mar '17, 17:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59877"></span><div id="comment-59877" class="comment"><div id="post-59877-score" class="comment-score"></div><div class="comment-text"><p>If I use automake how do I provide the path to qt5? I will give Bison a try. Thanks</p></div><div id="comment-59877-info" class="comment-info"><span class="comment-age">(06 Mar '17, 20:17)</span> <span class="comment-user userinfo">Rob B</span></div></div><span id="59878"></span><div id="comment-59878" class="comment"><div id="post-59878-score" class="comment-score"></div><div class="comment-text"><p>This shouldn't be a CMake vs. autotools issue - if you have Bison installed, CMake should find Bison, just as the autotools configure script would find it, so there should be no need to worry about autotools.</p><p>If you <em>want</em> to use autotools, then, unless you've installed Qt5 yourself rather than installing a CentOS package, the configure script should Just Work. If you have installed Qt5 yourself (for example, if CentOS 6 doesn't have a Qt5 package), it'll have to have installed the appropriate <code>pkg-config</code> information for it, otherwise the configure script won't be able to find it - if it has installed it, the configure script should be able to find it without having to tell them where to look.</p></div><div id="comment-59878-info" class="comment-info"><span class="comment-age">(06 Mar '17, 21:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59898"></span><div id="comment-59898" class="comment"><div id="post-59898-score" class="comment-score"></div><div class="comment-text"><p>Thanks everyone for the help. Used the source tar ball for 2.2.5 and it compiled nicely. I was even able to add my custom plugin into the build process.</p></div><div id="comment-59898-info" class="comment-info"><span class="comment-age">(07 Mar '17, 11:06)</span> <span class="comment-user userinfo">Rob B</span></div></div></div><div id="comment-tools-59870" class="comment-tools"></div><div class="clear"></div><div id="comment-59870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

