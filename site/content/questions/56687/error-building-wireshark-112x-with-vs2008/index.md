+++
type = "question"
title = "error building Wireshark 1.12x with VS2008"
description = '''Setting environment for using Microsoft Visual Studio 2008 x86 tools.  c:&#92;Program Files (x86)&#92;Microsoft Visual Studio 9.0&#92;VC&amp;gt;cd c:&#92;Aravind&#92;Project&#92;SVN&#92;CalyposoGeneralTools&#92;trunk&#92;Wireshark_Plugin&#92;WSI_Simple  Verify tools: c:&#92;Aravind&#92;Project&#92;SVN&#92;CalyposoGeneralTools&#92;trunk&#92;Wireshark_Plugin&#92;WSI_Simpl...'''
date = "2016-10-26T05:35:00Z"
lastmod = "2016-10-29T05:30:00Z"
weight = 56687
keywords = [ "build_error", "wireshark-1.12", "vs2008" ]
aliases = [ "/questions/56687" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [error building Wireshark 1.12x with VS2008](/questions/56687/error-building-wireshark-112x-with-vs2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56687-score" class="post-score" title="current number of votes">0</div><span id="post-56687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Setting environment for using Microsoft Visual Studio 2008 x86 tools.

c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC&gt;cd c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple</code></pre><p>Verify tools:</p><pre><code>c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/nmake
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget</code></pre><p>Setup:</p><pre><code>c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/nmake
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget
        cd &quot;C:\Wireshark-win32-libs-1.12&quot;
        rm -r -f adns-1.0-win32-05ws
        rm -r -f c-ares-1.5.3ws
        rm -r -f c-ares-1.6.0ws
        rm -r -f c-ares-1.7.0-win??ws
        rm -r -f c-ares-1.7.1-win??ws
        rm -r -f c-ares-1.9.1-1-win??ws
        rm -r -f gettext-0.14.5
        rm -r -f gettext-runtime-0.17
        rm -r -f gettext-runtime-0.17-1
        rm -r -f gettext-0.17-1            # win64
        rm -r -f glib
        rm -r -f gnutls-2.8.1-1
        rm -r -f gnutls-2.8.5-*-win??ws
        rm -r -f gnutls-2.10.3-*-win??ws
        rm -r -f gnutls-2.12.18-*-win??ws
        rm -r -f gnutls-3.1.22-*-win??ws
        rm -r -f gnutls-3.2.15-*-win??ws
        rm -r -f gtk2
        rm -r -f gtk+
        rm -r -f gtk-wimp
        rm -r -f kfw-2.5
        rm -r -f kfw-3-2-2-final
        rm -r -f kfw-3.2.2-ws1
        rm -r -f kfw-3-2-2-i386-ws-vc6
        rm -r -f libiconv-1.9.1.bin.woe32
        rm -r -f lua5.1
        rm -r -f lua5.1.4
        rm -r -f lua5.2.?
        rm -r -f libsmi-0.4.5
        rm -r -f libsmi-0.4.8
        rm -r -f libsmi-svn-40773-win??ws
        rm -r -f nasm-2.00
        rm -r -f nasm-2.02
        rm -r -f nasm-2.09.08
        rm -r -f pcre-6.4
        rm -r -f pcre-7.0
        rm -r -f portaudio_v19
        rm -r -f portaudio_v19_2
        rm -r -f upx301w
        rm -r -f upx303w
        rm -r -f user-guide
        rm -r -f zlib123
        rm -r -f zlib125
        rm -r -f zlib-1.2.5
        rm -r -f zlib123-dll
        rm -r -f AirPcap_Devpack_1_0_0_594
        rm -r -f AirPcap_Devpack_4_0_0_1480
        rm -r -f AirPcap_Devpack_4_1_0_1622
        rm -r -f GeoIP-1.4.5ws
        rm -r -f GeoIP-1.4.6-win??ws
        rm -r -f GeoIP-1.4.8-win??ws
        rm -r -f GeoIP-1.4.8-*-win??ws
        rm -r -f GeoIP-1.5.1-*-win??ws
        rm -r -f WinSparkle-0.3-44-g2c8d9d3-win??ws
        rm -r -f WpdPack
        cd &quot;c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple&quot;

****** WinPcap_4_1_3.exe ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WinPcap_4_1_3.exe into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;WinPcap_4_1_3.exe&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/WinPcap_4_1_3.exe&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;

****** gtk+-bundle_2.24.23-1.1_win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.24.23-1.1_win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into gtk2
File &#39;gtk+-bundle_2.24.23-1.1_win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/gtk+-bundle_2.24.23-1.1_win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/gtk2&#39;
Verifying that the DLLs and EXEs in gtk2 are executable.
Changing file permissions (add executable bit) to:
./bin/glib-genmarshal.exe
Changing file permissions (add executable bit) to:
./bin/gobject-query.exe
Changing file permissions (add executable bit) to:
./bin/gspawn-win32-helper-console.exe
Changing file permissions (add executable bit) to:
./bin/gspawn-win32-helper.exe
Changing file permissions (add executable bit) to:
./bin/libatk-1.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libcairo-2.dll
Changing file permissions (add executable bit) to:
./bin/libffi-6.dll
Changing file permissions (add executable bit) to:
./bin/libfontconfig-1.dll
Changing file permissions (add executable bit) to:
./bin/libfreetype-6.dll
Changing file permissions (add executable bit) to:
./bin/libgailutil-18.dll
Changing file permissions (add executable bit) to:
./bin/libgcc_s_sjlj-1.dll
Changing file permissions (add executable bit) to:
./bin/libgdk-win32-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgdk_pixbuf-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgio-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libglib-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgmodule-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgobject-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgthread-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libgtk-win32-2.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libharfbuzz-0.dll
Changing file permissions (add executable bit) to:
./bin/libintl-8.dll
Changing file permissions (add executable bit) to:
./bin/libjasper-1.dll
Changing file permissions (add executable bit) to:
./bin/libjpeg-8.dll
Changing file permissions (add executable bit) to:
./bin/liblzma-5.dll
Changing file permissions (add executable bit) to:
./bin/libpango-1.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libpangocairo-1.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libpangoft2-1.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libpangowin32-1.0-0.dll
Changing file permissions (add executable bit) to:
./bin/libpixman-1-0.dll
Changing file permissions (add executable bit) to:
./bin/libpng15-15.dll
Changing file permissions (add executable bit) to:
./bin/libtiff-5.dll
Changing file permissions (add executable bit) to:
./bin/libxml2-2.dll
Changing file permissions (add executable bit) to:
./bin/zlib1.dll
Changing file permissions (add executable bit) to:
./lib/gtk-2.0/2.10.0/engines/libpixmap.dll
Changing file permissions (add executable bit) to:
./lib/gtk-2.0/2.10.0/engines/libwimp.dll
Changing file permissions (add executable bit) to:
./lib/gtk-2.0/modules/libgail.dll

****** kfw-3-2-2-i386-ws-vc6.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading kfw-3-2-2-i386-ws-vc6.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;kfw-3-2-2-i386-ws-vc6.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/kfw-3-2-2-i386-ws-vc6.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.

****** WpdPack_4_1_2.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WpdPack_4_1_2.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;WpdPack_4_1_2.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/WpdPack_4_1_2.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.

****** AirPcap_Devpack_4_1_0_1622.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading AirPcap_Devpack_4_1_0_1622.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into AirPcap_Devpack_4_1_0_1622
File &#39;AirPcap_Devpack_4_1_0_1622.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/AirPcap_Devpack_4_1_0_1622.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/AirPcap_Devpack_4_1_0_1622&#39;
Verifying that the DLLs and EXEs in AirPcap_Devpack_4_1_0_1622 are executable.
Changing file permissions (add executable bit) to:
./Airpcap_Devpack/bin/x64/airpcap.dll
Changing file permissions (add executable bit) to:
./Airpcap_Devpack/bin/x86/airpcap.dll
Changing file permissions (add executable bit) to:
./Airpcap_Devpack/bin/x86/AirpcapConf.exe

****** c-ares-1.9.1-1-win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading c-ares-1.9.1-1-win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;c-ares-1.9.1-1-win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/c-ares-1.9.1-1-win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.
Changing file permissions (add executable bit) to:
./c-ares-1.9.1-1-win32ws/bin/libcares-2.dll

****** zlib-1.2.5.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading zlib-1.2.5.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into zlib125
File &#39;zlib-1.2.5.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/zlib-1.2.5.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/zlib125&#39;
Verifying that the DLLs and EXEs in zlib125 are executable.

****** lua-5.2.3_Win32_dll10_lib.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading lua-5.2.3_Win32_dll10_lib.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into lua5.2.3
File &#39;lua-5.2.3_Win32_dll10_lib.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/lua-5.2.3_Win32_dll10_lib.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/lua5.2.3&#39;
Verifying that the DLLs and EXEs in lua5.2.3 are executable.
Changing file permissions (add executable bit) to:
./lua52.dll

****** gnutls-3.2.15-2.7-win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gnutls-3.2.15-2.7-win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;gnutls-3.2.15-2.7-win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/gnutls-3.2.15-2.7-win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/dumpsexp.exe
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/gpg-error.exe
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/hmac256.exe
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libffi-6.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libgcc_s_sjlj-1.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libgcrypt-20.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libgmp-10.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libgnutls-28.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libgpg-error-0.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libhogweed-2-4.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libintl-8.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libnettle-4-6.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libp11-kit-0.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/libtasn1-6.dll
Changing file permissions (add executable bit) to:
./gnutls-3.2.15-2.7-win32ws/bin/mpicalc.exe

****** portaudio_v19_2.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading portaudio_v19_2.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;portaudio_v19_2.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/portaudio_v19_2.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.

****** libsmi-svn-40773-win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading libsmi-svn-40773-win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;libsmi-svn-40773-win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/libsmi-svn-40773-win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.

****** GeoIP-1.5.1-2-win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading GeoIP-1.5.1-2-win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into GeoIP-1.5.1-2-win32ws
File &#39;GeoIP-1.5.1-2-win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/GeoIP-1.5.1-2-win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/GeoIP-1.5.1-2-win32ws&#39;
Verifying that the DLLs and EXEs in GeoIP-1.5.1-2-win32ws are executable.
Changing file permissions (add executable bit) to:
./bin/geoiplookup.exe
Changing file permissions (add executable bit) to:
./bin/geoiplookup6.exe
Changing file permissions (add executable bit) to:
./bin/geoipupdate.exe
Changing file permissions (add executable bit) to:
./bin/libGeoIP-1.dll

****** WinSparkle-0.3-44-g2c8d9d3-win32ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WinSparkle-0.3-44-g2c8d9d3-win32ws.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;WinSparkle-0.3-44-g2c8d9d3-win32ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/WinSparkle-0.3-44-g2c8d9d3-win32ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.
Changing file permissions (add executable bit) to:
./WinSparkle-0.3-44-g2c8d9d3-win32ws/WinSparkle.dll

****** user-guide-g7ea0d6c.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading user-guide-g7ea0d6c.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into user-guide
File &#39;user-guide-g7ea0d6c.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/user-guide-g7ea0d6c.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/user-guide&#39;
Verifying that the DLLs and EXEs in user-guide are executable.

****** upx303w.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading upx303w.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;upx303w.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/upx303w.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.
Changing file permissions (add executable bit) to:
./upx303w/upx.exe

****** nasm-2.09.08-win32.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading nasm-2.09.08-win32.zip into &#39;/cygdrive/c/Wireshark-win32-libs-1.12&#39;, installing into .
File &#39;nasm-2.09.08-win32.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win32-libs-1.12/nasm-2.09.08-win32.zip&#39; into &#39;/cygdrive/c/Wireshark-win32-libs-1.12/.&#39;
Verifying that the DLLs and EXEs in . are executable.

Wireshark is ready to build.</code></pre><p>Building:</p><pre><code>c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple&gt;nmake -f Makefile.nmake all

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd tools
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake
Setting environment for using Microsoft Visual Studio 2008 x86 tools.

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        cd ..
        cd image
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        cd codecs
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

&#39;codecs.lib&#39; is up-to-date
        cd ..
        xcopy C:\Wireshark-win32-libs-1.12\zlib125 zlib.tmp /D /I /E /Y
C:\Wireshark-win32-libs-1.12\zlib125\adler32.c
C:\Wireshark-win32-libs-1.12\zlib125\ChangeLog
C:\Wireshark-win32-libs-1.12\zlib125\CMakeLists.txt
C:\Wireshark-win32-libs-1.12\zlib125\compress.c
C:\Wireshark-win32-libs-1.12\zlib125\configure
C:\Wireshark-win32-libs-1.12\zlib125\crc32.c
C:\Wireshark-win32-libs-1.12\zlib125\crc32.h
C:\Wireshark-win32-libs-1.12\zlib125\deflate.c
C:\Wireshark-win32-libs-1.12\zlib125\deflate.h
C:\Wireshark-win32-libs-1.12\zlib125\example.c
C:\Wireshark-win32-libs-1.12\zlib125\FAQ
C:\Wireshark-win32-libs-1.12\zlib125\gzclose.c
C:\Wireshark-win32-libs-1.12\zlib125\gzguts.h
C:\Wireshark-win32-libs-1.12\zlib125\gzlib.c
C:\Wireshark-win32-libs-1.12\zlib125\gzread.c
C:\Wireshark-win32-libs-1.12\zlib125\gzwrite.c
C:\Wireshark-win32-libs-1.12\zlib125\INDEX
C:\Wireshark-win32-libs-1.12\zlib125\infback.c
C:\Wireshark-win32-libs-1.12\zlib125\inffast.c
C:\Wireshark-win32-libs-1.12\zlib125\inffast.h
C:\Wireshark-win32-libs-1.12\zlib125\inffixed.h
C:\Wireshark-win32-libs-1.12\zlib125\inflate.c
C:\Wireshark-win32-libs-1.12\zlib125\inflate.h
C:\Wireshark-win32-libs-1.12\zlib125\inftrees.c
C:\Wireshark-win32-libs-1.12\zlib125\inftrees.h
C:\Wireshark-win32-libs-1.12\zlib125\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\Makefile.in
C:\Wireshark-win32-libs-1.12\zlib125\make_vms.com
C:\Wireshark-win32-libs-1.12\zlib125\minigzip.c
C:\Wireshark-win32-libs-1.12\zlib125\README
C:\Wireshark-win32-libs-1.12\zlib125\treebuild.xml
C:\Wireshark-win32-libs-1.12\zlib125\trees.c
C:\Wireshark-win32-libs-1.12\zlib125\trees.h
C:\Wireshark-win32-libs-1.12\zlib125\uncompr.c
C:\Wireshark-win32-libs-1.12\zlib125\zconf.h
C:\Wireshark-win32-libs-1.12\zlib125\zconf.h.cmakein
C:\Wireshark-win32-libs-1.12\zlib125\zconf.h.in
C:\Wireshark-win32-libs-1.12\zlib125\zlib.3
C:\Wireshark-win32-libs-1.12\zlib125\zlib.3.pdf
C:\Wireshark-win32-libs-1.12\zlib125\zlib.h
C:\Wireshark-win32-libs-1.12\zlib125\zlib.map
C:\Wireshark-win32-libs-1.12\zlib125\zlib.pc.in
C:\Wireshark-win32-libs-1.12\zlib125\zlib2ansi
C:\Wireshark-win32-libs-1.12\zlib125\zutil.c
C:\Wireshark-win32-libs-1.12\zlib125\zutil.h
C:\Wireshark-win32-libs-1.12\zlib125\amiga\Makefile.pup
C:\Wireshark-win32-libs-1.12\zlib125\amiga\Makefile.sas
C:\Wireshark-win32-libs-1.12\zlib125\contrib\README.contrib
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\buffer_demo.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\mtest.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\read.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\test.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib-streams.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib-streams.ads
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib-thin.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib-thin.ads
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib.adb
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib.ads
C:\Wireshark-win32-libs-1.12\zlib125\contrib\ada\zlib.gpr
C:\Wireshark-win32-libs-1.12\zlib125\contrib\amd64\amd64-match.S
C:\Wireshark-win32-libs-1.12\zlib125\contrib\asm686\match.S
C:\Wireshark-win32-libs-1.12\zlib125\contrib\asm686\README.686
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\blast.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\blast.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\README
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\test.pk
C:\Wireshark-win32-libs-1.12\zlib125\contrib\blast\test.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\delphi\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\delphi\ZLib.pas
C:\Wireshark-win32-libs-1.12\zlib125\contrib\delphi\ZLibConst.pas
C:\Wireshark-win32-libs-1.12\zlib125\contrib\delphi\zlibd32.mak
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib.build
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib.chm
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib.sln
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\LICENSE_1_0.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\AssemblyInfo.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\ChecksumImpl.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\CircularBuffer.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\CodecBase.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\Deflater.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\DotZLib.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\DotZLib.csproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\GZipStream.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\Inflater.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\dotzlib\DotZLib\UnitTests.cs
C:\Wireshark-win32-libs-1.12\zlib125\contrib\gcc_gvmat64\gvmat64.S
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\infback9.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\infback9.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\inffix9.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\inflate9.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\inftree9.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\inftree9.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\infback9\README
C:\Wireshark-win32-libs-1.12\zlib125\contrib\inflate86\inffas86.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\inflate86\inffast.S
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream\test.cpp
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream\zfstream.cpp
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream\zfstream.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream2\zstream.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream2\zstream_test.cpp
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream3\README
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream3\test.cc
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream3\TODO
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream3\zfstream.cc
C:\Wireshark-win32-libs-1.12\zlib125\contrib\iostream3\zfstream.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx64\bld_ml64.bat
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx64\gvmat64.asm
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx64\inffas8664.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx64\inffasx64.asm
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx64\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx86\bld_ml32.bat
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx86\inffas32.asm
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx86\match686.asm
C:\Wireshark-win32-libs-1.12\zlib125\contrib\masmx86\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\crypt.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\ioapi.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\ioapi.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\iowin32.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\iowin32.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\make_vms.com
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\miniunz.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\minizip.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\MiniZip64_Changes.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\MiniZip64_info.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\mztools.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\mztools.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\unzip.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\unzip.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\zip.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\minizip\zip.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\pascal\example.pas
C:\Wireshark-win32-libs-1.12\zlib125\contrib\pascal\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\pascal\zlibd32.mak
C:\Wireshark-win32-libs-1.12\zlib125\contrib\pascal\zlibpas.pas
C:\Wireshark-win32-libs-1.12\zlib125\contrib\puff\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\contrib\puff\puff.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\puff\puff.h
C:\Wireshark-win32-libs-1.12\zlib125\contrib\puff\README
C:\Wireshark-win32-libs-1.12\zlib125\contrib\puff\zeros.raw
C:\Wireshark-win32-libs-1.12\zlib125\contrib\testzlib\testzlib.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\testzlib\testzlib.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\untgz\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\contrib\untgz\Makefile.msc
C:\Wireshark-win32-libs-1.12\zlib125\contrib\untgz\untgz.c
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\miniunz.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\miniunz.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\miniunz.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\minizip.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\minizip.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\minizip.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlib.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlib.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlib.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlibdll.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlibdll.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\testzlibdll.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlib.rc
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibstat.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibstat.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibstat.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibvc.def
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibvc.sln
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibvc.vcxproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibvc.vcxproj.filters
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc10\zlibvc.vcxproj.user
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\miniunz.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\minizip.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\testzlib.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\testzlibdll.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\zlib.rc
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\zlibstat.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\zlibvc.def
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\zlibvc.sln
C:\Wireshark-win32-libs-1.12\zlib125\contrib\vstudio\vc9\zlibvc.vcproj
C:\Wireshark-win32-libs-1.12\zlib125\doc\algorithm.txt
C:\Wireshark-win32-libs-1.12\zlib125\doc\rfc1950.txt
C:\Wireshark-win32-libs-1.12\zlib125\doc\rfc1951.txt
C:\Wireshark-win32-libs-1.12\zlib125\doc\rfc1952.txt
C:\Wireshark-win32-libs-1.12\zlib125\doc\txtvsbin.txt
C:\Wireshark-win32-libs-1.12\zlib125\examples\enough.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\fitblk.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\gun.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\gzappend.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\gzjoin.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\gzlog.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\gzlog.h
C:\Wireshark-win32-libs-1.12\zlib125\examples\README.examples
C:\Wireshark-win32-libs-1.12\zlib125\examples\zlib_how.html
C:\Wireshark-win32-libs-1.12\zlib125\examples\zpipe.c
C:\Wireshark-win32-libs-1.12\zlib125\examples\zran.c
C:\Wireshark-win32-libs-1.12\zlib125\msdos\Makefile.bor
C:\Wireshark-win32-libs-1.12\zlib125\msdos\Makefile.dj2
C:\Wireshark-win32-libs-1.12\zlib125\msdos\Makefile.emx
C:\Wireshark-win32-libs-1.12\zlib125\msdos\Makefile.msc
C:\Wireshark-win32-libs-1.12\zlib125\msdos\Makefile.tc
C:\Wireshark-win32-libs-1.12\zlib125\nintendods\Makefile
C:\Wireshark-win32-libs-1.12\zlib125\nintendods\README
C:\Wireshark-win32-libs-1.12\zlib125\old\descrip.mms
C:\Wireshark-win32-libs-1.12\zlib125\old\Makefile.riscos
C:\Wireshark-win32-libs-1.12\zlib125\old\README
C:\Wireshark-win32-libs-1.12\zlib125\old\visual-basic.txt
C:\Wireshark-win32-libs-1.12\zlib125\old\as400\bndsrc
C:\Wireshark-win32-libs-1.12\zlib125\old\as400\compile.clp
C:\Wireshark-win32-libs-1.12\zlib125\old\as400\readme.txt
C:\Wireshark-win32-libs-1.12\zlib125\old\as400\zlib.inc
C:\Wireshark-win32-libs-1.12\zlib125\old\os2\Makefile.os2
C:\Wireshark-win32-libs-1.12\zlib125\old\os2\zlib.def
C:\Wireshark-win32-libs-1.12\zlib125\old\visualc6\example.dsp
C:\Wireshark-win32-libs-1.12\zlib125\old\visualc6\minigzip.dsp
C:\Wireshark-win32-libs-1.12\zlib125\old\visualc6\README.txt
C:\Wireshark-win32-libs-1.12\zlib125\old\visualc6\zlib.dsp
C:\Wireshark-win32-libs-1.12\zlib125\old\visualc6\zlib.dsw
C:\Wireshark-win32-libs-1.12\zlib125\qnx\package.qpg
C:\Wireshark-win32-libs-1.12\zlib125\watcom\watcom_f.mak
C:\Wireshark-win32-libs-1.12\zlib125\watcom\watcom_l.mak
C:\Wireshark-win32-libs-1.12\zlib125\win32\DLL_FAQ.txt
C:\Wireshark-win32-libs-1.12\zlib125\win32\Makefile.bor
C:\Wireshark-win32-libs-1.12\zlib125\win32\Makefile.emx
C:\Wireshark-win32-libs-1.12\zlib125\win32\Makefile.gcc
C:\Wireshark-win32-libs-1.12\zlib125\win32\Makefile.msc
C:\Wireshark-win32-libs-1.12\zlib125\win32\README-WIN32.txt
C:\Wireshark-win32-libs-1.12\zlib125\win32\VisualC.txt
C:\Wireshark-win32-libs-1.12\zlib125\win32\zlib.def
C:\Wireshark-win32-libs-1.12\zlib125\win32\zlib1.rc
229 File(s) copied
        cd zlib.tmp
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /                   -f win32/Makefile.msc zlib1.dll LOC=&quot;-DASMV -DASMINF&quot; OBJA=&quot;inffas32.obj match686.obj&quot;

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF adler32.c
adler32.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF compress.c
compress.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF crc32.c
crc32.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF deflate.c
deflate.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF gzclose.c
gzclose.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF gzlib.c
gzlib.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF gzread.c
gzread.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF gzwrite.c
gzwrite.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF infback.c
infback.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF inflate.c
inflate.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF inftrees.c
inftrees.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF trees.c
trees.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF uncompr.c
uncompr.c
        cl -c -D_CRT_SECURE_NO_DEPRECATE -D_CRT_NONSTDC_NO_DEPRECATE -nologo -MD -W3 -O2 -Oy- -Zi -Fd&quot;zlib&quot; -DASMV -DASMINF zutil.c
zutil.c
        ml -c -coff -Zi -DASMV -DASMINF contrib/masmx86\inffas32.asm
Microsoft (R) Macro Assembler Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

 Assembling: contrib/masmx86\inffas32.asm
        ml -c -coff -Zi -DASMV -DASMINF contrib/masmx86\match686.asm
Microsoft (R) Macro Assembler Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

 Assembling: contrib/masmx86\match686.asm
        rc /dWIN32 /r /fozlib1.res win32/zlib1.rc
Microsoft (R) Windows (R) Resource Compiler Version 6.0.5724.0
Copyright (C) Microsoft Corporation.  All rights reserved.

        link -nologo -debug -incremental:no -opt:ref -def:win32/zlib.def -dll -implib:zdll.lib  -out:zlib1.dll -base:0x5A4C0000 adler32.obj compress.obj crc32.obj deflate.obj gzclose.obj gzlib.obj gzread.obj  gzwrite.obj infback.obj inflate.obj inftrees.obj trees.obj uncompr.obj zutil.obj inffas32.obj match686.obj zlib1.res
   Creating library zdll.lib and object zdll.exp
        if exist zlib1.dll.manifest  mt -nologo -manifest zlib1.dll.manifest -outputresource:zlib1.dll;2
        if not exist C:\Wireshark-win32-libs-1.12\zlib125 mkdir C:\Wireshark-win32-libs-1.12\zlib125
        if not exist C:\Wireshark-win32-libs-1.12\zlib125\lib mkdir C:\Wireshark-win32-libs-1.12\zlib125\lib
        if not exist C:\Wireshark-win32-libs-1.12\zlib125\include mkdir C:\Wireshark-win32-libs-1.12\zlib125\include
        mt.exe -nologo -manifest &quot;zlib1.dll.manifest&quot; -outputresource:zlib1.dll;2
        copy zlib1.dll C:\Wireshark-win32-libs-1.12\zlib125
        1 file(s) copied.
        copy zdll.lib C:\Wireshark-win32-libs-1.12\zlib125\lib
        1 file(s) copied.
        copy zconf.h C:\Wireshark-win32-libs-1.12\zlib125\include
        1 file(s) copied.
        copy zlib.h C:\Wireshark-win32-libs-1.12\zlib125\include
        1 file(s) copied.
        cd ..
        rm -r -f zlib.tmp
        cd wsutil
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl  /DWINPCAP_VERSION=4_1_3 /Zi /W3 /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1500  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /GS /w34295  /I. /I.. /IC:\Wireshark-win32-libs-1.12\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs-1.12\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES /IC:\Wireshark-win32-libs-1.12\gnutls-3.2.15-2.7-win32ws\include /DNOCRYPT /DIMPORT_LIGNUTLSDLL  /IC:\Wir
eshark-win32-libs-1.12\WPdpack\include -DWS_BUILD_DLL -Fd.\ -c eax.c
Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 15.00.21022.08 for 80x86
Copyright (C) Microsoft Corporation.  All rights reserved.

eax.c
C:\Wireshark-win32-libs-1.12\gnutls-3.2.15-2.7-win32ws\include\gpg-error.h(714) : fatal error C1083: Cannot open include file: &#39;stdint.h&#39;: No such file or directory
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.

c:\Aravind\Project\SVN\CalyposoGeneralTools\trunk\Wireshark_Plugin\WSI_Simple&gt;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-wireshark-1.12" rel="tag" title="see questions tagged &#39;wireshark-1.12&#39;">wireshark-1.12</span> <span class="post-tag tag-link-vs2008" rel="tag" title="see questions tagged &#39;vs2008&#39;">vs2008</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '16, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '16, 02:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56687" class="comments-container"></div><div id="comment-tools-56687" class="comment-tools"></div><div class="clear"></div><div id="comment-56687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56812"></span>

<div id="answer-container-56812" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56812-score" class="post-score" title="current number of votes">0</div><span id="post-56812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DhanuShalz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>VS2008 doesn't come with stdint.h so, i provided a copy of stdint.h from the VS2010 Dir.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Oct '16, 05:33</strong> </span></p></div></div><div id="comments-container-56812" class="comments-container"></div><div id="comment-tools-56812" class="comment-tools"></div><div class="clear"></div><div id="comment-56812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56688"></span>

<div id="answer-container-56688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56688-score" class="post-score" title="current number of votes">0</div><span id="post-56688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version are you trying to build, as current versions use CMake not nmake?</p><p>Have you followed the steps in the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> exactly as written?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '16, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56688" class="comments-container"><span id="56698"></span><div id="comment-56698" class="comment"><div id="post-56698-score" class="comment-score"></div><div class="comment-text"><p>Wireshark-win32-1.12.6 is the version im trying to build.!</p><p>i have the fallowed the steps.</p></div><div id="comment-56698-info" class="comment-info"><span class="comment-age">(26 Oct '16, 07:16)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="56699"></span><div id="comment-56699" class="comment"><div id="post-56699-score" class="comment-score"></div><div class="comment-text"><p>That version isn't supported anymore, but I'll have a go.</p><p>You'll need to post the full output of your build as there isn't enough context to determine the issue. Redirect the build output to a file, e.g.</p><pre><code>nmake ... 2&gt;&amp;1 &gt; build.txt</code></pre><p>and then edit your question with the full build output.</p></div><div id="comment-56699-info" class="comment-info"><span class="comment-age">(26 Oct '16, 07:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56700"></span><div id="comment-56700" class="comment"><div id="post-56700-score" class="comment-score"></div><div class="comment-text"><p>updated the log.</p></div><div id="comment-56700-info" class="comment-info"><span class="comment-age">(26 Oct '16, 08:07)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="56704"></span><div id="comment-56704" class="comment"><div id="post-56704-score" class="comment-score"></div><div class="comment-text"><blockquote>C:\Wireshark-win32-libs-1.12\gnutls-3.2.15-2.7-win32ws\include\gpg-error.h(714) : fatal error C1083: Cannot open include file: 'stdint.h': No such file or directory</blockquote><p>The build can't locate stdint.h, the release versions of 1.12 were built using VS 2010, not sure if that's the issue.</p><p>Can you find stdint.h anywhere in the VS 2008 VC\include directory? If not, then try with VS2010.</p></div><div id="comment-56704-info" class="comment-info"><span class="comment-age">(26 Oct '16, 08:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56705"></span><div id="comment-56705" class="comment"><div id="post-56705-score" class="comment-score"></div><div class="comment-text"><p>This SO <a href="http://stackoverflow.com/questions/126279/c99-stdint-h-header-and-ms-visual-studio">question</a> implies that VS2008 doesn't come with stdint.h, so you'll either need to use VS2010, or provide your own copy of stdint.h as noted in the question.</p><p>Even doing the latter might not be enough to resolve any further build issues, so moving to 2010 might be a better choice.</p><p>Even better than that would be to move to a supported version and update your plugin to run with modern versions of Wireshark, built using a modern VS toolchain.</p></div><div id="comment-56705-info" class="comment-info"><span class="comment-age">(26 Oct '16, 09:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56771"></span><div id="comment-56771" class="comment not_top_scorer"><div id="post-56771-score" class="comment-score"></div><div class="comment-text"><p>Thank you grahamb it worked out...!</p></div><div id="comment-56771-info" class="comment-info"><span class="comment-age">(28 Oct '16, 00:47)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="56776"></span><div id="comment-56776" class="comment not_top_scorer"><div id="post-56776-score" class="comment-score"></div><div class="comment-text"><p><span>@Dhanu</span> Schalz</p><p>Can you tell the rest of the world how "it worked out" so anyone else stuck with the same issue can see the answer?</p></div><div id="comment-56776-info" class="comment-info"><span class="comment-age">(28 Oct '16, 02:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56688" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

