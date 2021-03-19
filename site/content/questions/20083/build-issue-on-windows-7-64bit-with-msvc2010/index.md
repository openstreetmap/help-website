+++
type = "question"
title = "Build issue on Windows 7, 64bit with MSVC2010"
description = '''Hi, I have a build issue when building Wireshark on Windows 7, 64bit and MSVC2010. The error log returned is: Build Log Build started: Project: packaging, Configuration: PortableApps|Win32  Command Lines Creating temporary file &quot;C:&#92;Users&#92;RICHAR~1&#92;AppData&#92;Local&#92;Temp&#92;BAT00000357762912.bat&quot; with conten...'''
date = "2013-04-04T09:09:00Z"
lastmod = "2013-04-04T12:24:00Z"
weight = 20083
keywords = [ "windows7", "msvc2010", "build" ]
aliases = [ "/questions/20083" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Build issue on Windows 7, 64bit with MSVC2010](/questions/20083/build-issue-on-windows-7-64bit-with-msvc2010)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20083-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a build issue when building Wireshark on Windows 7, 64bit and MSVC2010. The error log returned is:</p><pre><code>Build Log      Build started: Project: packaging, Configuration: PortableApps|Win32
 Command Lines      Creating temporary file &quot;C:\Users\RICHAR~1\AppData\Local\Temp\BAT00000357762912.bat&quot; with contents
[
@echo off

nmake -f Makefile.nmake packaging_papps

if errorlevel 1 goto VCReportError

goto VCEnd

:VCReportError

echo Project : error PRJ0019: A tool returned an error code from &quot;Performing Makefile project actions&quot;

exit 1

:VCEnd
]
Creating command line &quot;C:\Users\RICHAR~1\AppData\Local\Temp\BAT00000357762912.bat&quot;
Output Window      Performing Makefile project actions
Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.
ERROR: The contents of &#39;C:\Wireshark-win64-libs\current_tag.txt&#39; is (unknown).
It should be 2013-03-09.
? Wireshark Libraries not up-to-date ?
? Do you need to run nmake -f Makefile.nmake setup ?
NMAKE : fatal error U1077: &#39;exit&#39; : return code &#39;0x1&#39;
Stop.
Project : error PRJ0019: A tool returned an error code from &quot;Performing Makefile project actions&quot;
Results      Build log was saved at &quot;file://c:\WireShark\PortableApps\BuildLog.htm&quot;
packaging - 2 error(s), 0 warning(s)</code></pre></div><div id="question-tags" class="tags-container tags">windows7 msvc2010 build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '13, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/d2f6b15e8444050f7f297c5b147fd8b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Drayton&#39;s gravatar image" /><p>Richard Drayton<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Drayton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Apr '13, 11:07</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20083" class="comments-container"></div><div id="comment-tools-20083" class="comment-tools"></div><div class="clear"></div><div id="comment-20083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20087"></span>

<div id="answer-container-20087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20087-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you run <code>nmake -f Makefile.nmake setup</code> before trying to build Wireshark?</p><p>If not, do so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20087" class="comments-container"><span id="20091"></span><div id="comment-20091" class="comment"><div id="post-20091-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response - yes the project was built from within Visual Studio using the wireshark.sln file provided in the SVN download - the environment was built according to the details in the Win32 setup including the CygWin installation, Python download etc.. Running the setup gives:</p><pre><code>c:\WireShark&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of &#39;C:\Wireshark-win64-libs\current_tag.txt&#39; is (unknown).
It should be 2013-03-09.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /cygdrive/c/Perl64/bin/perl
        sed: /usr/bin/sed
        unzip: /cygdrive/c/oraclexe/app/oracle/product/11.2.0/server/bin/unzip
        wget: /usr/bin/wget
        cd &quot;C:\Wireshark-win64-libs&quot;
        rm -r -f adns-1.0-win32-05ws
        rm -r -f c-ares-1.5.3ws
        rm -r -f c-ares-1.6.0ws
        rm -r -f c-ares-1.7.0-win??ws
        rm -r -f c-ares-1.7.1-win??ws
        rm -r -f c-ares-1.9.1-win??ws
        rm -r -f gettext-0.14.5
        rm -r -f gettext-runtime-0.17
        rm -r -f gettext-runtime-0.17-1
        rm -r -f gettext-0.17-1            # win64
        rm -r -f glib
        rm -r -f gnutls-2.8.1-1
        rm -r -f gnutls-2.8.5-*-win??ws
        rm -r -f gnutls-2.10.3-*-win??ws
        rm -r -f gnutls-2.12.18-*-win??ws
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
        rm -r -f WinSparkle-0.3-44-g2c8d9d3-win??ws
        rm -r -f WpdPack
        cd &quot;c:\WireShark&quot;

****** WinPcap_4_1_3.exe ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading WinPcap_4_1_3.exe into &#39;/cygdrive/c/Wireshark-win64-libs&#39;, installing into .
File `WinPcap_4_1_3.exe&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win64-libs/WinPcap_4_1_3.exe&#39; into &#39;/cygdrive/c/Wireshark-win64-libs/.&#39;

****** gtk+-bundle_2.24.14-1.1_win64ws.zip ******
No HTTP proxy specified (http_proxy and HTTP_PROXY are empty).
Downloading gtk+-bundle_2.24.14-1.1_win64ws.zip into &#39;/cygdrive/c/Wireshark-win64-libs&#39;, installing into gtk2
File `gtk+-bundle_2.24.14-1.1_win64ws.zip&#39; already there; not retrieving.

Extracting &#39;/cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip&#39; into &#39;/cygdrive/c/Wireshark-win64-libs/gtk2&#39;
    unzip:  cannot find either /cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip or /cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip.zip.

ERROR: Couldn&#39;t unpack &#39;/cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip&#39;

NMAKE : fatal error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.

c:\WireShark&gt;</code></pre><p>Other than the unzip command (which seems to work fine) the result is as per the documentation until the last step.</p><p>The error occurs irrespective of the command line build or the MSVC build.</p><pre><code>Verify Tools

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of &#39;C:\Wireshark-win64-libs\current_tag.txt&#39; is (unknown).
It should be 2013-03-09.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/amd64/nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /cygdrive/c/Perl64/bin/perl
        sed: /usr/bin/sed
        unzip: /cygdrive/c/oraclexe/app/oracle/product/11.2.0/server/bin/unzip
        wget: /usr/bin/wget

c:\WireShark&gt;</code></pre><p>Regards Richard</p></div><div id="comment-20091-info" class="comment-info"><span class="comment-age">(04 Apr '13, 14:45)</span> Richard Drayton</div></div><span id="20092"></span><div id="comment-20092" class="comment"><div id="post-20092-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Other than the unzip command (which seems to work fine)</p></blockquote><p>Actually, not:</p><pre><code>unzip:  cannot find either /cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip or /cygdrive/c/Wireshark-win64-libs/gtk+-bundle_2.24.14-1.1_win64ws.zip.zip.</code></pre><p>What does the command <code>dir c:\Wireshark-win64-libs</code> print?</p></div><div id="comment-20092-info" class="comment-info"><span class="comment-age">(04 Apr '13, 15:21)</span> Guy Harris ♦♦</div></div><span id="20094"></span><div id="comment-20094" class="comment"><div id="post-20094-score" class="comment-score"></div><div class="comment-text"><p>@Richard Drayton</p><p>As per my answer, do not use the solution file, it is outdated and doesn't work, you must build from the command prompt.</p><p>Your issue with the command prompt is the oracle version of unzip:</p><p><code>unzip: /cygdrive/c/oraclexe/app/oracle/product/11.2.0/server/bin/unzip</code>.</p><p>I don't know what it is, but it doesn't behave like a normal unzip. You'll need to remove it from your path and try again with <code>nmake -f Makefile.nmake setup</code>.</p></div><div id="comment-20094-info" class="comment-info"><span class="comment-age">(04 Apr '13, 16:12)</span> grahamb ♦</div></div></div><div id="comment-tools-20087" class="comment-tools"></div><div class="clear"></div><div id="comment-20087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20089"></span>

<div id="answer-container-20089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20089-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you're trying to build from within Visual Studio with a makefile project. That won't work, you must use a command prompt prepared as per section <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">2.2 Win32 setup</a> of the developer's guide. For a successful build you must follow the guide exactly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-20089" class="comments-container"></div><div id="comment-tools-20089" class="comment-tools"></div><div class="clear"></div><div id="comment-20089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

