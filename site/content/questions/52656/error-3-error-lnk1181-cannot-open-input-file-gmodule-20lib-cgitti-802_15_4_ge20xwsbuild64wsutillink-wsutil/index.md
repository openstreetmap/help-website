+++
type = "question"
title = "Error	3	error LNK1181: cannot open input file &#x27;gmodule-2.0.lib&#x27;	C:&#92;git&#92;ti-802_15_4_ge&#92;2.0.x&#92;wsbuild64&#92;wsutil&#92;LINK	wsutil"
description = '''I am trying to build Wireshark 2.0.2, and I can&#x27;t get past this linker error: Error 3 error LNK1181: cannot open input file &#x27;gmodule-2.0.lib&#x27; Although, I do have it under C:&#92;git&#92;ti-802_15_4_ge&#92;2.0.x&#92;Wireshark-win64-libs-2.0&#92;gtk2&#92;lib. I can&#x27;t seem to find any solutions on this issue, except that it m...'''
date = "2016-05-16T17:38:00Z"
lastmod = "2016-05-17T10:27:00Z"
weight = 52656
keywords = [ "lnk1181" ]
aliases = [ "/questions/52656" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error 3 error LNK1181: cannot open input file 'gmodule-2.0.lib' C:\\git\\ti-802\_15\_4\_ge\\2.0.x\\wsbuild64\\wsutil\\LINK wsutil](/questions/52656/error-3-error-lnk1181-cannot-open-input-file-gmodule-20lib-cgitti-802_15_4_ge20xwsbuild64wsutillink-wsutil)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build Wireshark 2.0.2, and I can't get past this linker error:</p><p>Error 3 error LNK1181: cannot open input file 'gmodule-2.0.lib'</p><p>Although, I do have it under C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib. I can't seem to find any solutions on this issue, except that it might be stemming from my path having a space in it, but that is not the case here. Does anyone know what to do?</p><p>Here is the full context of my cmake step:</p><pre><code>-- The C compiler identification is MSVC 18.0.40629.0
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
-- Generating build using CMake 3.5.1
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe  
-- Building for win64 using Visual Studio 12 2013 Win64
Working in C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0

Tag 2015-12-11 not found. Refreshing.

Unable to find 7-zip, retrieving from anonsvn into C:\git\ti-802_15_4_ge\2.0.x\

Wireshark-win64-libs-2.0\bin\7za.exe

Downloading https://anonsvn.wireshark.org/wireshark-win32-libs/trunk/bin/7za.ex

e into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/WinPcap_4_1_3.exe into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-lib

s-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/USBPcapSetup-1.1.0.0-g794bf26-1.exe into C:\git\ti-802_15_4_ge\2.0.x\W

ireshark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/AirPcap_Devpack_4_1_0_1622.zip into C:\git\ti-802_15_4_ge\2.0.x\Wiresh

ark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/c-ares-1.9.1-1-win64ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-

win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/GeoIP-1.6.6-win64ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win

64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/gnutls-3.2.15-2.9-win64ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wiresha

rk-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/gtk+-bundle_2.24.23-3.39_win64ws.zip into C:\git\ti-802_15_4_ge\2.0.x\

Wireshark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/kfw-3-2-2-x64-ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-

libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/libsmi-svn-40773-win64ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshar

k-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/lua-5.2.3_Win64_dll12_lib.zip into C:\git\ti-802_15_4_ge\2.0.x\Wiresha

rk-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/nasm-2.09.08-win32.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win6

4-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/portaudio_v19_2.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-l

ibs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/upx303w.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/user-guide-gdf2fcdf.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win

64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/WinSparkle-0.3-44-g2c8d9d3-win64ws.zip into C:\git\ti-802_15_4_ge\2.0.

x\Wireshark-win64-libs-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/WpdPack_4_1_2.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-lib

s-2.0

Downloading https://anonsvn.wireshark.org/wireshark-win64-libs/tags/2015-12-11/

packages/zlib-1.2.8-ws.zip into C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-lib

s-2.0

-- Including C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit/CMakeListsCustom.txt
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- RelWithDebInfo: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.0.2, MaV: 2, MiV: 0, PL: 2, EV: .
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
-- Renaming
--     C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/zlib-1.2.8-ws/zconf.h
-- to &#39;zconf.h.included&#39; because this file is included with zlib
-- but CMake generates it automatically in the build directory.
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;HtmlViewer;KERBEROS;LEX;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include  
-- AIRPCAP FOUND
-- AIRPCAP includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Found PkgConfig: C:/cygwin64/bin/pkg-config.exe (found version &quot;0.29&quot;) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Found CARES: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/c-ares-1.9.1-1-win64ws/lib/libcares-2.lib  
-- CARES FOUND
-- CARES includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/c-ares-1.9.1-1-win64ws/include
-- CARES libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/c-ares-1.9.1-1-win64ws/lib/libcares-2.lib
-- Found GCRYPT: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.6.2&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib  
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib  
-- GLIB2 FOUND
-- GLIB2 includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0/include
-- GLIB2 libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GMODULE2 libs: gmodule-2.0;glib-2.0;intl
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;) 
-- GNUTLS FOUND
-- GNUTLS includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GTHREAD2 libs: gthread-2.0;glib-2.0;intl
-- Found GTK2_GTK: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gtk-win32-2.0.lib  
-- GTK2 FOUND
-- GTK2 includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/gtk-2.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/freetype2;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/glib-2.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0/include;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/atk-1.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/gdk-pixbuf-2.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/cairo;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/include/pango-1.0;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gtk-2.0/include
-- GTK2 libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/glib-2.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gobject-2.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/atk-1.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gmodule-2.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gdk_pixbuf-2.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/cairo.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/pango-1.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/pangocairo-1.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gdk-win32-2.0.lib;C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Found HtmlViewer: C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  
-- HTML_VIEWER NOT FOUND
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/kfw-3-2-2-x64-ws/lib/krb5_64.lib  
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Found LEX: C:/cygwin64/bin/flex.exe  
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: C:/cygwin64/bin/flex.exe
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Found LUA: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/lua5.2.3/lua52.lib (found version &quot;502&quot;) 
-- LUA FOUND
-- LUA includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/lua5.2.3/include
-- LUA libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- Found PCAP: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WpdPack/Include  
-- Looking for pcap_open_dead
-- Looking for pcap_open_dead - found
-- Looking for pcap_freecode
-- Looking for pcap_freecode - found
-- Looking for pcap_breakloop
-- Looking for pcap_breakloop - found
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
-- PCAP includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WpdPack/Include
-- PCAP libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WpdPack/Lib/x64/wpcap.lib
-- Found POD: C:/cygwin64/bin/pod2man  
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- Found PORTAUDIO: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/portaudio_v19_2/include  
-- PORTAUDIO FOUND
-- PORTAUDIO includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/portaudio_v19_2/include;C:/git/ti-802_15_4_ge/2.0.x/wireshark-win64-libs-2.0/portaudio_v19_2/src/common;C:/git/ti-802_15_4_ge/2.0.x/wireshark-win64-libs-2.0/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- Found Perl: C:/cygwin64/bin/perl.exe (found version &quot;5.22.2&quot;) 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: C:/cygwin64/bin/perl.exe
-- Found PythonInterp: C:/Program Files/GNURadio-3.7/gr-python27/python.exe (found suitable version &quot;2.7.10&quot;, minimum required is &quot;2&quot;) 
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
-- Found SED: C:/cygwin64/bin/sed.exe  
-- SED FOUND
-- SED includes: 
-- SED libs: 
-- SED executable: C:/cygwin64/bin/sed.exe
-- Could NOT find SETCAP (missing:  SETCAP_EXECUTABLE) 
-- SETCAP NOT FOUND
-- Found SH: C:/cygwin64/bin/bash.exe  
-- SH FOUND
-- SH includes: 
-- SH libs: 
-- SH executable: C:/cygwin64/bin/bash.exe
-- Found SMI: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/libsmi-svn-40773-win64ws/lib/libsmi-2.lib  
-- SMI FOUND
-- SMI includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/libsmi-svn-40773-win64ws/include
-- SMI libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- Found WINSPARKLE: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib  
-- WINSPARKLE FOUND
-- WINSPARKLE includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WinSparkle-0.3-44-g2c8d9d3-win64ws
-- WINSPARKLE libs: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib
-- Found YACC: C:/cygwin64/bin/bison.exe  
-- YACC FOUND
-- YACC includes: 
-- YACC libs: 
-- YACC executable: C:/cygwin64/bin/bison.exe
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE) 
-- YAPP NOT FOUND
-- Looking for inflatePrime
-- Looking for inflatePrime - not found
-- Found ZLIB: zlib  
-- ZLIB FOUND
-- ZLIB includes: C:/git/ti-802_15_4_ge/2.0.x/Wireshark-win64-libs-2.0/zlib-1.2.8-ws;C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/zlib
-- ZLIB libs: zlib
-- C-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3
-- CXX-Flags:  /MP /Zo /w34295 /w34189  /DWIN32 /D_WINDOWS /W3 /GR /EHsc
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
-- Looking for tzname - found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Found python module asn2wrs: C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\tools\asn2wrs.py
-- Found LYNX: C:/cygwin64/bin/lynx.exe  
-- Found XSLTPROC: C:/cygwin64/bin/xsltproc.exe  
-- Found XMLLINT: C:/cygwin64/bin/xmllint.exe  
-- Using Cygwin a2x
-- Found ASCIIDOC: C:/cygwin64/bin/bash.exe;/cygdrive/c/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit/tools/runa2x.sh  
-- No custom file found in C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit/epan
-- Found python module make-dissector-reg: C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\tools\make-dissector-reg.py
-- Looking for emmintrin.h
-- Looking for emmintrin.h - found
-- Looking for nmmintrin.h
-- Looking for nmmintrin.h - found
-- No custom file found in C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit/ui/gtk
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
 * HtmlViewer
 * KERBEROS
 * LUA
 * PCAP
 * POD
 * PkgConfig
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
 * M
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
-- Generating done
-- Build files have been written to: C:/git/ti-802_15_4_ge/2.0.x/wsbuild64</code></pre><p>Here is the full context from my build step (updated):</p><pre><code>Microsoft (R) Build Engine version 12.0.40629.0
[Microsoft .NET Framework, version 4.0.30319.42000]
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 5/17/2016 9:50:03 AM.
Project &quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj&quot; on node 1 (rebuild target(s)).
Project &quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj&quot; (1) is building &quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\ZERO_CHECK.vcxproj&quot; (2:2) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
CustomBuild:
  Checking Build System
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/zlib/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/HI2Operations/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/acp133/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/acse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ansi_map/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ansi_tcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/atn-cm/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/atn-cpdlc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/atn-ulcs/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/c1222/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/camel/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/cdt/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/charging_ase/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/cmip/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/cmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/cms/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/credssp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/crmf/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/dap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/disp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/dop/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/dsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ess/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ftam/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/goose/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/gprscdr/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/gsm_map/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h225/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h235/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h245/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h248/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h282/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h283/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h323/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h450/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h450-ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h460/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/h501/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/hnbap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/idmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ilp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/inap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/isdn-sup/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/kerberos/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/lcsap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ldap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/logotypecertextn/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/lpp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/lppa/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/lppe/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/lte-rrc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/m3ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/mms/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/mpeg-audio/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/mpeg-pes/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/nbap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ns_cert_exts/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/novell_pkis/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ocsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/p1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/p22/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/p7/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/p772/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkcs1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkcs12/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkinit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkix1explicit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkix1implicit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkixac/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkixproxy/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkixqualified/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pkixtsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/pres/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/q932/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/q932-ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/qsig/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ranap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/rnsap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/rrc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/rrlp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/rtse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/rua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/s1ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/sabp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/sbc-ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/smrse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/snmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/spnego/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/sv/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/t124/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/t125/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/t38/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/tcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/tetra/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/ulp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/wlancertextn/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/x2ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/x509af/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/x509ce/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/x509if/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/asn1/x509sat/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/capchild/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/caputils/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/codecs/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/docbook/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/epan/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/epan/wslua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/epan/dissectors/dcerpc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/tools/lemon/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/ui/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/wiretap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/wsutil/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/ui/gtk/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/docsis/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/ethercat/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/gryphon/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/irda/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/m2m/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/mate/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/opcua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/profinet/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/stats_tree/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/unistim/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/wimax/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/wimaxasncp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/wimaxmacphy/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/plugins/ti802154ge/CMakeFiles/generate.stamp is up-to-date.
FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate&quot;.
Done Building Project &quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\ZERO_CHECK.vcxproj&quot; (default targets).
InitializeBuildStatus:
  Touching &quot;wsutil.dir\RelWithDebInfo\wsutil.tlog\unsuccessfulbuild&quot;.
CustomBuild:
  Building Custom Rule C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit/wsutil/CMakeLists.txt
  CMake does not need to re-run because C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\CMakeFiles\generate.stamp is up-to-date.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\CL.exe /c /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\zlib&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\zlib-1.2.8-ws&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\epan&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\tools\lemon&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wiretap&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\AirPcap_Devpack_4_1_0_1622\Airpcap_Devpack\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\c-ares-1.9.1-1-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\GeoIP-1.6.6-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\glib-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\glib-2.0\include&quot; /I&quot;\usr\include\glib-2.0&quot; /I&quot;\usr\lib\glib-2.0\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\gtk-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\freetype2&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\atk-1.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\gdk-pixbuf-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\cairo&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\pango-1.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\gtk-2.0\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\kfw-3-2-2-x64-ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\lua5.2.3\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\WpdPack\Include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\portaudio_v19_2\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-win64-libs-2.0\portaudio_v19_2\src\common&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-win64-libs-2.0\portaudio_v19_2\src\os\win&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\libsmi-svn-40773-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\WinSparkle-0.3-44-g2c8d9d3-win64ws&quot; /Zi /nologo /W3 /WX- /MP /O2 /Ob1 /D WIN32 /D _WINDOWS /D NDEBUG /D WS_BUILD_DLL /D WIN32_LEAN_AND_MEAN /D MSC_VER_REQUIRED=1800 /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D NOMINMAX /D PSAPI_VERSION=1 /D BUILD_WINDOWS /D _ALLOW_KEYWORD_MACROS /D WINPCAP_VERSION=4_1_3 /D &quot;TOP_SRCDIR=\&quot;C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit\&quot;&quot; /D &quot;CMAKE_INTDIR=\&quot;RelWithDebInfo\&quot;&quot; /D wsutil_EXPORTS /D _WINDLL /D _MBCS /Gm- /MD /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo&quot;wsutil.dir\RelWithDebInfo\\&quot; /Fd&quot;wsutil.dir\RelWithDebInfo\vc120.pdb&quot; /Gd /TC /errorReport:queue  /Zo /w34295 /w34189 &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\adler32.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\aes.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\airpdcap_wep.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\base64.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\bitswap.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\buffer.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\cfutils.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\clopts_common.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\cmdarg_err.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\copyright_info.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crash_info.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc10.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc16.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc16-plain.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc32.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc6.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc7.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc8.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\crc11.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\des.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\eax.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\filesystem.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\frequency-utils.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\g711.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\jsmn.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\md4.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\md5.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\mpeg-audio.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\nstime.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\os_version_info.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\plugins.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\privileges.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\sha1.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\sober128.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\strnatcmp.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\str_util.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\rc4.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\report_err.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\tempfile.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\time_util.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\type_util.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\u3.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\unicode-utils.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\ws_mempbrk.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\ws_version_info.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\file_util.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\inet_ntop.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\inet_pton.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\ws_mempbrk_sse42.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\wsgetopt.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\inet_aton.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\popcount.c&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wsutil\strptime.c&quot;
  adler32.c
  aes.c
  airpdcap_wep.c
  base64.c
  bitswap.c
  buffer.c
  cfutils.c
  clopts_common.c
  cmdarg_err.c
  copyright_info.c
  crash_info.c
  crc10.c
  crc16.c
  crc16-plain.c
  crc32.c
  crc6.c
  crc7.c
  crc8.c
  crc11.c
  des.c
  eax.c
  filesystem.c
  frequency-utils.c
  g711.c
  jsmn.c
  md4.c
  md5.c
  mpeg-audio.c
  nstime.c
  os_version_info.c
  plugins.c
  privileges.c
  sha1.c
  sober128.c
  strnatcmp.c
  str_util.c
  rc4.c
  report_err.c
  tempfile.c
  time_util.c
  type_util.c
  u3.c
  unicode-utils.c
  ws_mempbrk.c
  ws_version_info.c
  file_util.c
  inet_ntop.c
  inet_pton.c
  ws_mempbrk_sse42.c
  wsgetopt.c
  inet_aton.c
  popcount.c
  strptime.c
ResourceCompile:
  C:\Program Files (x86)\Windows Kits\8.1\bin\x64\rc.exe /D WIN32 /D _WINDOWS /D NDEBUG /D WS_BUILD_DLL /D WIN32_LEAN_AND_MEAN /D MSC_VER_REQUIRED=1800 /D _CRT_SECURE_NO_DEPRECATE /D _CRT_NONSTDC_NO_DEPRECATE /D NOMINMAX /D PSAPI_VERSION=1 /D BUILD_WINDOWS /D _ALLOW_KEYWORD_MACROS /D WINPCAP_VERSION=4_1_3 /D &quot;TOP_SRCDIR=\\\&quot;C:/git/ti-802_15_4_ge/2.0.x/wireshark-2.0.2-64bit\\\&quot;&quot; /D &quot;CMAKE_INTDIR=\\\&quot;RelWithDebInfo\\\&quot;&quot; /D wsutil_EXPORTS /l&quot;0x0409&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\zlib&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\zlib-1.2.8-ws&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\epan&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\tools\lemon&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-2.0.2-64bit\wiretap&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\AirPcap_Devpack_4_1_0_1622\Airpcap_Devpack\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\c-ares-1.9.1-1-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\GeoIP-1.6.6-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\glib-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\glib-2.0\include&quot; /I&quot;\usr\include\glib-2.0&quot; /I&quot;\usr\lib\glib-2.0\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\gtk-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\freetype2&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\atk-1.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\gdk-pixbuf-2.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\cairo&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\include\pango-1.0&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\gtk-2.0\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\kfw-3-2-2-x64-ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\lua5.2.3\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\WpdPack\Include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\portaudio_v19_2\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-win64-libs-2.0\portaudio_v19_2\src\common&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\wireshark-win64-libs-2.0\portaudio_v19_2\src\os\win&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\libsmi-svn-40773-win64ws\include&quot; /I&quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\WinSparkle-0.3-44-g2c8d9d3-win64ws&quot; /nologo /fo&quot;wsutil.dir\RelWithDebInfo\libwsutil.res&quot; C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\image\libwsutil.rc 
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\link.exe /ERRORREPORT:QUEUE /OUT:&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\run\RelWithDebInfo\libwsutil.dll&quot; /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib &quot;gmodule-2.0.lib&quot; &quot;glib-2.0.lib&quot; intl.lib &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\glib-2.0.lib&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\bin\libgcrypt-20.lib&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\bin\libgpg-error6-0.lib&quot; wsock32.lib ws2_32.lib /MANIFEST:NO /DEBUG /PDB:&quot;C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/run/RelWithDebInfo/libwsutil.pdb&quot; /SUBSYSTEM:CONSOLE /LARGEADDRESSAWARE /TLBID:1 /RELEASE /DYNAMICBASE /NXCOMPAT /IMPLIB:&quot;C:/git/ti-802_15_4_ge/2.0.x/wsbuild64/run/RelWithDebInfo/wsutil.lib&quot; /MACHINE:X64  /machine:x64 setargv.obj /DLL wsutil.dir\RelWithDebInfo\libwsutil.res
  wsutil.dir\RelWithDebInfo\adler32.obj
  wsutil.dir\RelWithDebInfo\aes.obj
  wsutil.dir\RelWithDebInfo\airpdcap_wep.obj
  wsutil.dir\RelWithDebInfo\base64.obj
  wsutil.dir\RelWithDebInfo\bitswap.obj
  wsutil.dir\RelWithDebInfo\buffer.obj
  wsutil.dir\RelWithDebInfo\cfutils.obj
  wsutil.dir\RelWithDebInfo\clopts_common.obj
  wsutil.dir\RelWithDebInfo\cmdarg_err.obj
  wsutil.dir\RelWithDebInfo\copyright_info.obj
  wsutil.dir\RelWithDebInfo\crash_info.obj
  wsutil.dir\RelWithDebInfo\crc10.obj
  wsutil.dir\RelWithDebInfo\crc16.obj
  &quot;wsutil.dir\RelWithDebInfo\crc16-plain.obj&quot;
  wsutil.dir\RelWithDebInfo\crc32.obj
  wsutil.dir\RelWithDebInfo\crc6.obj
  wsutil.dir\RelWithDebInfo\crc7.obj
  wsutil.dir\RelWithDebInfo\crc8.obj
  wsutil.dir\RelWithDebInfo\crc11.obj
  wsutil.dir\RelWithDebInfo\des.obj
  wsutil.dir\RelWithDebInfo\eax.obj
  wsutil.dir\RelWithDebInfo\filesystem.obj
  &quot;wsutil.dir\RelWithDebInfo\frequency-utils.obj&quot;
  wsutil.dir\RelWithDebInfo\g711.obj
  wsutil.dir\RelWithDebInfo\jsmn.obj
  wsutil.dir\RelWithDebInfo\md4.obj
  wsutil.dir\RelWithDebInfo\md5.obj
  &quot;wsutil.dir\RelWithDebInfo\mpeg-audio.obj&quot;
  wsutil.dir\RelWithDebInfo\nstime.obj
  wsutil.dir\RelWithDebInfo\os_version_info.obj
  wsutil.dir\RelWithDebInfo\plugins.obj
  wsutil.dir\RelWithDebInfo\privileges.obj
  wsutil.dir\RelWithDebInfo\sha1.obj
  wsutil.dir\RelWithDebInfo\sober128.obj
  wsutil.dir\RelWithDebInfo\strnatcmp.obj
  wsutil.dir\RelWithDebInfo\str_util.obj
  wsutil.dir\RelWithDebInfo\rc4.obj
  wsutil.dir\RelWithDebInfo\report_err.obj
  wsutil.dir\RelWithDebInfo\tempfile.obj
  wsutil.dir\RelWithDebInfo\time_util.obj
  wsutil.dir\RelWithDebInfo\type_util.obj
  wsutil.dir\RelWithDebInfo\u3.obj
  &quot;wsutil.dir\RelWithDebInfo\unicode-utils.obj&quot;
  wsutil.dir\RelWithDebInfo\ws_mempbrk.obj
  wsutil.dir\RelWithDebInfo\ws_version_info.obj
  wsutil.dir\RelWithDebInfo\file_util.obj
  wsutil.dir\RelWithDebInfo\inet_ntop.obj
  wsutil.dir\RelWithDebInfo\inet_pton.obj
  wsutil.dir\RelWithDebInfo\ws_mempbrk_sse42.obj
  wsutil.dir\RelWithDebInfo\wsgetopt.obj
  wsutil.dir\RelWithDebInfo\inet_aton.obj
  wsutil.dir\RelWithDebInfo\popcount.obj
  wsutil.dir\RelWithDebInfo\strptime.obj
LINK : fatal error LNK1181: cannot open input file &#39;gmodule-2.0.lib&#39; [C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj]
Done Building Project &quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj&quot; (rebuild target(s)) -- FAILED.

Build FAILED.

&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj&quot; (rebuild target) (1) -&gt;
(Link target) -&gt; 
  LINK : fatal error LNK1181: cannot open input file &#39;gmodule-2.0.lib&#39; [C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\wsutil\wsutil.vcxproj]

    0 Warning(s)
    1 Error(s)

Time Elapsed 00:00:08.19</code></pre></div><div id="question-tags" class="tags-container tags">lnk1181</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p>j-demars<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '16, 10:52</p></div></div><div id="comments-container-52656" class="comments-container"><span id="52662"></span><div id="comment-52662" class="comment"><div id="post-52662-score" class="comment-score"></div><div class="comment-text"><p>You'll need to provide the full context of the output to get assistance.</p></div><div id="comment-52662-info" class="comment-info"><span class="comment-age">(17 May '16, 02:58)</span> grahamb ♦</div></div><span id="52676"></span><div id="comment-52676" class="comment"><div id="post-52676-score" class="comment-score"></div><div class="comment-text"><p>I added the full context of the error above. Thanks @grahamb</p></div><div id="comment-52676-info" class="comment-info"><span class="comment-age">(17 May '16, 08:19)</span> j-demars</div></div><span id="52677"></span><div id="comment-52677" class="comment"><div id="post-52677-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately that output only appears to be the tail end with the failure summary, not the actual error. Also the output seem to have been copied from a shell window so all the lines are hard-wrapped making it more difficult to follow.</p><p>Can you use the following command to redirect output to a file? The command also builds only the wsutil project and stops multi-core use so the output is in some form of sane order.</p><pre><code>msbuild /p:Configuration=RelWithDebInfo /t:rebuild wsutil\wsutil.vcxproj 2&gt;&amp;1 &gt;path\to\logfile.txt</code></pre></div><div id="comment-52677-info" class="comment-info"><span class="comment-age">(17 May '16, 09:31)</span> grahamb ♦</div></div><span id="52678"></span><div id="comment-52678" class="comment"><div id="post-52678-score" class="comment-score"></div><div class="comment-text"><p>Here is the output of that command, sorry about that! Should have made sure it was all there. I formatted it with the "code" button, hopefully it's easier to read!</p></div><div id="comment-52678-info" class="comment-info"><span class="comment-age">(17 May '16, 09:56)</span> j-demars</div></div></div><div id="comment-tools-52656" class="comment-tools"></div><div class="clear"></div><div id="comment-52656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52681"></span>

<div id="answer-container-52681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52681-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Much better output, makes me happy :-)</p><p>The link command has some oddities:</p><pre><code>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\link.exe /ERRORREPORT:QUEUE /OUT:&quot;C:\git\ti-802_15_4_ge\2.0.x\wsbuild64\run\RelWithDebInfo\libwsutil.dll&quot; /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib &quot;gmodule-2.0.lib&quot; &quot;glib-2.0.lib&quot; intl.lib &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\glib-2.0.lib&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\bin\libgcrypt-20.lib&quot; &quot;C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gnutls-3.2.15-2.9-win64ws\bin\libgpg-error6-0.lib&quot; wsock32.lib ws2_32.lib</code></pre><p>The odd bits are the plain references to <code>"gmodule-2.0.lib" "glib-2.0.lib" intl.lib</code> followed by what looks like a good reference to <code>"C:\git\ti-802_15_4_ge\2.0.x\Wireshark-win64-libs-2.0\gtk2\lib\glib-2.0.lib"</code>. For reference mine looks like:</p><pre><code>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\link.exe /ERRORREPORT:QUEUE /OUT:&quot;E:\Wireshark\build64\run\RelWithDebInfo\libwsutil.dll&quot; /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib &quot;E:\Wireshark\Wireshark-win64-libs\gtk2\lib\gmodule-2.0.lib&quot; &quot;E:\Wireshark\Wireshark-win64-libs\gtk2\lib\glib-2.0.lib&quot; &quot;E:\Wireshark\Wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgcrypt-20.lib&quot; &quot;E:\Wireshark\Wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgpg-error6-0.lib&quot; ..\run\RelWithDebInfo\zlib.lib wsock32.lib ws2_32.lib</code></pre><p>I think the easiest thing to do to get going is to delete your build directory and re-run the CMake generation steps and then build again. Something's gone very wrong with the CMake generated solution and project files.</p><p>If things are still broken, then we'll also need to see the CMake generation output. Redirect it to a different file in a similar manner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52681" class="comments-container"><span id="52684"></span><div id="comment-52684" class="comment"><div id="post-52684-score" class="comment-score"></div><div class="comment-text"><p>Deleted everything in my wsbuild64 directory and wireshark-win64-libs-2.0 directory and ran cmake again and built again, but still having same error. As you can see, even in the cmake step it still uses the plain references to gmodule and glib after FOUND GMODULE. Do you understand why that could be? I added the cmake output above. Thanks so much for your help!</p></div><div id="comment-52684-info" class="comment-info"><span class="comment-age">(17 May '16, 10:54)</span> j-demars</div></div><span id="52693"></span><div id="comment-52693" class="comment"><div id="post-52693-score" class="comment-score"></div><div class="comment-text"><p>CMake is finding the gmodule libraries in an odd place:</p><pre><code>-- GMODULE2 FOUND
-- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GMODULE2 libs: gmodule-2.0;glib-2.0;intl</code></pre><p>I suspect this might either be Cygwin or Git, what is on your path?</p></div><div id="comment-52693-info" class="comment-info"><span class="comment-age">(17 May '16, 14:54)</span> grahamb ♦</div></div></div><div id="comment-tools-52681" class="comment-tools"></div><div class="clear"></div><div id="comment-52681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

