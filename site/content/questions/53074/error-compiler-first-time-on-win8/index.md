+++
type = "question"
title = "Error Compiler first time on Win8"
description = '''As my title i tried to build on MSVS 2013 on win8 the latest version of wireshark taken from git repository. i followed wireshark guide until cmake but when i try to build on visual studio a 32-bit build version i found 3 errors. I tried to compile because i&#x27;d like to create a new dissector plugin i...'''
date = "2016-05-31T06:45:00Z"
lastmod = "2016-05-31T07:18:00Z"
weight = 53074
keywords = [ "c2220", "errorc2220", "visual-studio", "compiler" ]
aliases = [ "/questions/53074" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error Compiler first time on Win8](/questions/53074/error-compiler-first-time-on-win8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53074-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As my title i tried to build on MSVS 2013 on win8 the latest version of wireshark taken from git repository. i followed wireshark guide until cmake but when i try to build on visual studio a 32-bit build version i found 3 errors. I tried to compile because i'd like to create a new dissector plugin in railway environment. i had lots of difficult and errors trying to build a 64 bit versione so i'd like to make a 32 bit version. List of 3 errors:</p><pre><code>Error   5   error C2220: warning treated as error - no &#39;object&#39; file generated (C:\Development\Wireshark\wireshark\ui\qt\proto_tree.cpp)    C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\include\xutility 2798    1   qtui

Error   8   error LNK1181: cannot open input file &#39;run\Debug\qtui.lib&#39;  C:\Development\wsbuild32\LINK   wireshark

Error   9   error MSB3073: The command &quot;setlocal
set PATH=%PATH%;C:/Qt/Qt5.6.0_32/5.6/msvc2013/bin
if %errorlevel% neq 0 goto :cmEnd
C:\Qt\Qt5.6.0_32\5.6\msvc2013\bin\windeployqt.exe --debug  --no-compiler-runtime --verbose 10 C:/Development/wsbuild32/run/Debug/Wireshark.exe
if %errorlevel% neq 0 goto :cmEnd
:cmEnd
endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
:cmErrorLevel
exit /b %1
:cmDone
if %errorlevel% neq 0 goto :VCEnd
:VCEnd&quot; exited with code 1. C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets  132 5   copy_qt_dlls</code></pre><p>Can someone help me? Thanks in advance</p></div><div id="question-tags" class="tags-container tags">c2220 errorc2220 visual-studio compiler</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p>kenhero<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '16, 07:12</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53074" class="comments-container"></div><div id="comment-tools-53074" class="comment-tools"></div><div class="clear"></div><div id="comment-53074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53075"></span>

<div id="answer-container-53075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53075-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The listing of your errors is a bit odd, it's easier to diagnose issues if they are copied 'as-is'. Redirect the msbuild output to a file (<code>msbuild ... 2&amp;&gt;1 &gt; path\to\file.txt</code>) and then cut and paste from the file. It also helps to turn off the parallel build to keep things in order by removing the <code>/m</code> flag to msbuild.</p><p>I can't work out what the first error is, the actual error is missing. The second &amp; third errors are probably a result of the first, in that the build isn't producing a qtui.lib.</p><p>Have you modified the code at all? If so, revert all changes and just build the standard code first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '16, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53075" class="comments-container"><span id="53076"></span><div id="comment-53076" class="comment"><div id="post-53076-score" class="comment-score"></div><div class="comment-text"><p>Hi,these are MSVS errors.</p><p><a href="http://postimg.org/image/768utcg3f/">http://postimg.org/image/768utcg3f/</a></p></div><div id="comment-53076-info" class="comment-info"><span class="comment-age">(31 May '16, 07:32)</span> kenhero</div></div><span id="53077"></span><div id="comment-53077" class="comment"><div id="post-53077-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-53077-info" class="comment-info"><span class="comment-age">(31 May '16, 07:41)</span> Jaap ♦</div></div><span id="53078"></span><div id="comment-53078" class="comment"><div id="post-53078-score" class="comment-score"></div><div class="comment-text"><p>So you're not following the Dev. Guide. Can you try building from the command line using msbuild as <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChWin32Build">detailed</a> in the Dev. Guide and reporting those errors back to us?</p></div><div id="comment-53078-info" class="comment-info"><span class="comment-age">(31 May '16, 08:11)</span> grahamb ♦</div></div><span id="53083"></span><div id="comment-53083" class="comment"><div id="post-53083-score" class="comment-score"></div><div class="comment-text"><p><a href="http://s33.postimg.org/f1uzhg6bj/msbuilderror.png">http://s33.postimg.org/f1uzhg6bj/msbuilderror.png</a></p><p>if u need i can translate in english</p></div><div id="comment-53083-info" class="comment-info"><span class="comment-age">(31 May '16, 11:31)</span> kenhero</div></div><span id="53085"></span><div id="comment-53085" class="comment not_top_scorer"><div id="post-53085-score" class="comment-score"></div><div class="comment-text"><p>You still seem to be not following the Dev. Guide. Please re-read Section <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">2.2.10</a> on setting up the command prompt. You need to <code>cd</code> to the build directory, <code>C:\development\wsbuild32</code> before running msbuild. If you follow the Dev. Guide exactly as written it will work.</p><p>There also seems to be an issue with the build configuration, the error is indicating that RelWithDebInfo|Win64 isn't a valid configuration, yet you don't seem to be passing that config option. Did you originally try to build a Win64 version in that build directory? If so, delete the build directory and start again from step 2.2.10.</p></div><div id="comment-53085-info" class="comment-info"><span class="comment-age">(31 May '16, 15:04)</span> grahamb ♦</div></div><span id="53093"></span><div id="comment-53093" class="comment not_top_scorer"><div id="post-53093-score" class="comment-score"></div><div class="comment-text"><p>ok,the error was a wrong VS Command prompt. i try to build a 64bit . After found the right command prompt i created a separated folder "wsbuild64" and build on it. Actually i only have this error about Qt5Widgets.lib</p><p><a href="http://s33.postimg.org/qz0yveokv/Build_Error.png">http://s33.postimg.org/qz0yveokv/Build_Error.png</a></p></div><div id="comment-53093-info" class="comment-info"><span class="comment-age">(01 Jun '16, 03:26)</span> kenhero</div></div><span id="53094"></span><div id="comment-53094" class="comment not_top_scorer"><div id="post-53094-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>You have tried to build an x64 version of Wireshark using an x86 version of Qt. See the Developer's Guide <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupQt">instructions</a> for installing Qt.</p></div><div id="comment-53094-info" class="comment-info"><span class="comment-age">(01 Jun '16, 03:33)</span> grahamb ♦</div></div><span id="53095"></span><div id="comment-53095" class="comment not_top_scorer"><div id="post-53095-score" class="comment-score"></div><div class="comment-text"><p>no,i had a 32 and 64bit QT version. Also: <a href="http://s33.postimg.org/h20nkio33/QTissue.png">http://s33.postimg.org/h20nkio33/QTissue.png</a></p></div><div id="comment-53095-info" class="comment-info"><span class="comment-age">(01 Jun '16, 03:48)</span> kenhero</div></div><span id="53098"></span><div id="comment-53098" class="comment not_top_scorer"><div id="post-53098-score" class="comment-score"></div><div class="comment-text"><p>Again, your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-53098-info" class="comment-info"><span class="comment-age">(01 Jun '16, 04:47)</span> Jaap ♦</div></div><span id="53100"></span><div id="comment-53100" class="comment not_top_scorer"><div id="post-53100-score" class="comment-score"></div><div class="comment-text"><p>As you seem unable to post the full build info, only fragmentary screenshots it's a bit difficult to help.</p><p>Please re-run the CMake generation step, redirecting the output to a text file and then post the contents of that text file as a <strong>comment</strong>, or by editing your original question and adding it:</p><pre><code>cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; path\to\wireshark\sources 2&gt;&amp;1 &gt; log.txt</code></pre><p>If you need to temporarily post a comment as an answer, e.g. for length or to use the editor buttons, please then convert the answer to a comment under the appropriate question.</p></div><div id="comment-53100-info" class="comment-info"><span class="comment-age">(01 Jun '16, 04:58)</span> grahamb ♦</div></div><span id="53101"></span><div id="comment-53101" class="comment not_top_scorer"><div id="post-53101-score" class="comment-score"></div><div class="comment-text"><pre><code>-- The C compiler identification is MSVC 18.0.31101.0
-- The CXX compiler identification is MSVC 18.0.31101.0
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
Working in C:\Development\wireshark-win64-libs

Tag 2016-05-10 found. Skipping.

-- No custom file found in C:/Development/Wireshark/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.0-YourExtraVersionInfo, MaV: 2, MiV: 1, PL: 0, EV: -YourExtraVersionInfo.
-- Found PythonInterp: C:/Python27/python.exe (found version &quot;2.7.11&quot;) 
-- Found python module asn2wrs: C:\Development\Wireshark\wireshark\tools\asn2wrs.py
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
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Found AIRPCAP: C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include  
-- AIRPCAP FOUND
-- AIRPCAP includes: C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Found CARES: C:/Development/wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib  
-- CARES FOUND
-- CARES includes: C:/Development/wireshark-win64-libs/c-ares-1.11.0-win64ws/include
-- CARES libs: C:/Development/wireshark-win64-libs/c-ares-1.11.0-win64ws/lib/libcares-2.lib
-- Found GCRYPT: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.6.2&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib  
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GLIB2 FOUND
-- GLIB2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0;C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0/include
-- GLIB2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- Found GMODULE2: C:/Development/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib  
-- GMODULE2 FOUND
-- GMODULE2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0
-- GMODULE2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;) 
-- GNUTLS FOUND
-- GNUTLS includes: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- Found GTHREAD2: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib  
-- GTHREAD2 FOUND
-- GTHREAD2 includes: C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib
-- Found GTK2_GTK: C:/Development/wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib  
-- GTK2 FOUND
-- GTK2 includes: C:/Development/wireshark-win64-libs/gtk2/include/gtk-2.0;C:/Development/wireshark-win64-libs/gtk2/include;C:/Development/wireshark-win64-libs/gtk2/include/freetype2;C:/Development/wireshark-win64-libs/gtk2/include/glib-2.0;C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0/include;C:/Development/wireshark-win64-libs/gtk2/include/atk-1.0;C:/Development/wireshark-win64-libs/gtk2/include/gdk-pixbuf-2.0;C:/Development/wireshark-win64-libs/gtk2/include/cairo;C:/Development/wireshark-win64-libs/gtk2/include/pango-1.0;C:/Development/wireshark-win64-libs/gtk2/lib/gtk-2.0/include
-- GTK2 libs: C:/Development/wireshark-win64-libs/gtk2/lib/glib-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gobject-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/atk-1.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gmodule-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gdk_pixbuf-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/cairo.lib;C:/Development/wireshark-win64-libs/gtk2/lib/pango-1.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/pangocairo-1.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gdk-win32-2.0.lib;C:/Development/wireshark-win64-libs/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Found Git: C:/Program Files/Git/cmd/git.exe (found version &quot;2.8.3.windows.1&quot;) 
-- Git FOUND
-- Git includes: 
-- Git libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib  
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/lib/krb5_64.lib
-- Found LEX: C:/cygwin64/bin/flex.exe  
-- LEX FOUND
-- LEX includes: 
-- LEX libs: 
-- LEX executable: C:/cygwin64/bin/flex.exe
-- Found LIBSSH: C:/Development/wireshark-win64-libs/libssh-0.7.2-win64ws/lib/ssh.lib (found suitable version &quot;0.7.2&quot;, minimum required is &quot;0.6&quot;) 
-- LIBSSH FOUND
-- LIBSSH includes: C:/Development/wireshark-win64-libs/libssh-0.7.2-win64ws/include
-- LIBSSH libs: C:/Development/wireshark-win64-libs/libssh-0.7.2-win64ws/lib/ssh.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;lua5.2;lua-5.2;lua52;lua5.1;lua-5.1;lua51;lua5.0;lua-5.0;lua50&#39;
-- Checking for one of the modules &#39;lua&lt;=5.2.99&#39;
-- Found LUA: C:/Development/wireshark-win64-libs/lua5.2.3/lua52.lib (found version &quot;502&quot;) 
-- LUA FOUND
-- LUA includes: C:/Development/wireshark-win64-libs/lua5.2.3/include
-- LUA libs: C:/Development/wireshark-win64-libs/lua5.2.3/lua52.lib
-- Could NOT find M (missing:  M_LIBRARY) 
-- M NOT FOUND
-- Found PCAP: C:/Development/wireshark-win64-libs/WpdPack/Include  
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
-- PCAP includes: C:/Development/wireshark-win64-libs/WpdPack/Include
-- PCAP libs: C:/Development/wireshark-win64-libs/WpdPack/Lib/x64/wpcap.lib
-- Found POD: C:/cygwin64/bin/pod2man  
-- POD FOUND
-- POD includes: 
-- POD libs: 
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;portaudio-2.0&#39;
-- Found PORTAUDIO: C:/Development/wireshark-win64-libs/portaudio_v19_2/include  
-- PORTAUDIO FOUND
-- PORTAUDIO includes: C:/Development/wireshark-win64-libs/portaudio_v19_2/include;C:/Development/wireshark-win64-libs/portaudio_v19_2/src/common;C:/Development/wireshark-win64-libs/portaudio_v19_2/src/os/win
-- PORTAUDIO libs: 
-- Found Perl: C:/cygwin64/bin/perl.exe (found version &quot;5.22.2&quot;) 
-- PERL FOUND
-- Perl includes: 
-- Perl libs: 
-- Perl executable: C:/cygwin64/bin/perl.exe
-- Found PythonInterp: C:/Python27/python.exe (found suitable version &quot;2.7.11&quot;, minimum required is &quot;2&quot;) 
-- PYTHONINTERP FOUND
-- PythonInterp includes: 
-- PythonInterp libs: 
-- Qt5Core FOUND
-- Qt5Core includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Core libs: Qt5::Core
-- Qt5Core definitions: -DQT_CORE_LIB
-- Qt5LinguistTools FOUND
-- Qt5LinguistTools includes: 
-- Qt5LinguistTools libs: 
-- Qt5Multimedia FOUND
-- Qt5Multimedia includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtMultimedia;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtNetwork;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtGui
-- Qt5Multimedia libs: Qt5::Multimedia
-- Qt5Multimedia definitions: -DQT_MULTIMEDIA_LIB;-DQT_NETWORK_LIB;-DQT_CORE_LIB;-DQT_GUI_LIB
-- Qt5PrintSupport FOUND
-- Qt5PrintSupport includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtPrintSupport;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtWidgets;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtGui;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5PrintSupport libs: Qt5::PrintSupport
-- Qt5PrintSupport definitions: -DQT_PRINTSUPPORT_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Svg FOUND
-- Qt5Svg includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtSvg;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtWidgets;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtGui;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Svg libs: Qt5::Svg
-- Qt5Svg definitions: -DQT_SVG_LIB;-DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5Widgets FOUND
-- Qt5Widgets includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtWidgets;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtGui;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5Widgets libs: Qt5::Widgets
-- Qt5Widgets definitions: -DQT_WIDGETS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
-- Qt5WinExtras FOUND
-- Qt5WinExtras includes: C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtWinExtras;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtGui;C:/Qt/Qt5.6.0/5.6/msvc2013_64/include/QtCore;C:/Qt/Qt5.6.0/5.6/msvc2013_64/.//mkspecs/win32-msvc2013
-- Qt5WinExtras libs: Qt5::WinExtras
-- Qt5WinExtras definitions: -DQT_WINEXTRAS_LIB;-DQT_GUI_LIB;-DQT_CORE_LIB
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
-- Found SMI: C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib  
-- SMI FOUND
-- SMI includes: C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/include
-- SMI libs: C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/lib/libsmi-2.lib
-- Found WINSPARKLE: C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib  
-- WINSPARKLE FOUND
-- WINSPARKLE includes: C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws
-- WINSPARKLE libs: C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.lib
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
-- ZLIB includes: C:/Development/wireshark-win64-libs/zlib-1.2.8-ws;C:/Development/Wireshark/wireshark/zlib
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
-- Performing Test HAVE_STRUCT_TM_TM_ZONE - Failed
-- Looking for tzname
-- Looking for tzname - found
-- Check if the system is big endian
-- Searching 16 bit integer
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Using unsigned short
-- Check if the system is big endian - little endian
-- Found LYNX: C:/cygwin64/bin/lynx.exe  
-- Found XSLTPROC: C:/cygwin64/bin/xsltproc.exe  
-- Using Cygwin a2x
-- Found ASCIIDOC: C:/cygwin64/bin/bash.exe;/cygdrive/c/Development/Wireshark/wireshark/tools/runa2x.sh  
-- No custom file found in C:/Development/Wireshark/wireshark/epan/crypt
-- No custom file found in C:/Development/Wireshark/wireshark/epan/dissectors
-- No custom file found in C:/Development/Wireshark/wireshark/epan/dissectors/asn1
-- Found python module make-dissector-reg: C:\Development\Wireshark\wireshark\tools\make-dissector-reg.py
-- Looking for emmintrin.h
-- Looking for emmintrin.h - found
-- Looking for nmmintrin.h
-- Looking for nmmintrin.h - found
-- No custom file found in C:/Development/Wireshark/wireshark/ui/gtk
-- Looking for ssh_userauth_agent
-- Looking for ssh_userauth_agent - not found
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
 * KERBEROS
 * LIBSSH (required version &gt;= 0.6) , libssh is library for ssh connections and it is needed to build sshdump/ciscodump , &lt;www: https://www.libssh.org/get-it/&gt;
 * LUA
 * PCAP
 * POD
 * PORTAUDIO
 * Perl
 * Qt5Core
 * Qt5LinguistTools
 * Qt5Network (required version &gt;= 5.6.0)
 * Qt5Gui (required version &gt;= 5.6.0)
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

-- Configuring done
-- Generating done
-- Build files have been written to: C:/Development/Wireshark/wireshark</code></pre></div><div id="comment-53101-info" class="comment-info"><span class="comment-age">(01 Jun '16, 05:27)</span> kenhero</div></div><span id="53102"></span><div id="comment-53102" class="comment not_top_scorer"><div id="post-53102-score" class="comment-score"></div><div class="comment-text"><p>i think the error is in mkspecs/win32-msvc2013</p></div><div id="comment-53102-info" class="comment-info"><span class="comment-age">(01 Jun '16, 05:46)</span> kenhero</div></div><span id="53103"></span><div id="comment-53103" class="comment not_top_scorer"><div id="post-53103-score" class="comment-score"></div><div class="comment-text"><p>The CMake generation all looks good, what do you get when you build, again redirect output to a text file:</p><pre><code>msbuild /p:Configuration=RelWithDebInfo Wireshark.sln 2&gt;&amp;1 &gt; build.txt</code></pre></div><div id="comment-53103-info" class="comment-info"><span class="comment-age">(01 Jun '16, 06:05)</span> grahamb ♦</div></div><span id="53105"></span><div id="comment-53105" class="comment not_top_scorer"><div id="post-53105-score" class="comment-score"></div><div class="comment-text"><pre><code>Microsoft (R) Build Engine versione 12.0.31101.0
[Microsoft .NET Framework versione 4.0.30319.42000]
Copyright (C) Microsoft Corporation. Tutti i diritti riservati.

Compilazione dei progetti nella soluzione uno alla volta. Per abilitare la compilazione parallela, aggiungere l&#39;opzione &quot;/m&quot;.
Compilazione avviata 01/06/2016 15:33:12.
Progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; sul nodo 1 (destinazioni predefinite).
ValidateSolutionConfiguration:
  Compilazione della configurazione di soluzione &quot;RelWithDebInfo|X64&quot; in corso.
ValidateProjects:
  Il progetto &quot;INSTALL&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;PACKAGE&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_capchild-base&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_capchild-todo&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_caputils-base&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_caputils-todo&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_codecs&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_crypt&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_dfilter&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_dissectors&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_docsis&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_epan&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_ethercat&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_ftypes&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_gryphon&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_gtk-base&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_gtk-todo&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_irda&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_m2m&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_main&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_mate&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_opcua&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_profinet&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_randpkt_core-base&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_randpkt_core-todo&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_stats_tree&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_ui-base&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_ui-todo&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_unistim&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wimax&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wimaxasncp&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wimaxmacphy&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wiretap&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wmem&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wslua&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;checkAPI_wsutil&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;dumpabi-libwireshark&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;dumpabi-libwiretap&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;dumpabi-libwsutil&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;gen-authors&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;hardening-check&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;news&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;pdb_zip_package&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;plugins&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;release_notes&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;test-programs&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;update-sminmpec&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
  Il progetto &quot;x11-dissector&quot; non Š selezionato per la compilazione nella configurazione di soluzione &quot;RelWithDebInfo|x64&quot;.
Compilazione di &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\ZERO_CHECK.vcxproj&quot; (3) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ZERO_CHECK.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj.metaproj&quot; (4) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj.metaproj&quot; (5) dal progetto &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj.metaproj&quot; (4) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (6) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj.metaproj&quot; (5) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (7) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (6) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (8) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (7) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\generate_developer-guide.xml.vcxproj&quot; (9) dal progetto &quot;C:\Development\wsbuild64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (8) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\generate_developer-guide.xml\generate.71341513.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\generate_developer-guide.xml\generate.71341513.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\generate_developer-guide.xml\generate.71341513.tlog\generate_developer-guide.xml.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\generate_developer-guide.xml.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj&quot; (10) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (7) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.8854FB96.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.8854FB96.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.8854FB96.tlog\developer_guide_docbook.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj&quot; (11) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (6) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\developer_guide_chm\develope.72BF719D.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\developer_guide_chm\develope.72BF719D.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\developer_guide_chm\develope.72BF719D.tlog\developer_guide_chm.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj&quot; (12) dal progetto &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj.metaproj&quot; (5) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\developer_guides.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\developer_guides.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj.metaproj&quot; (13) dal progetto &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj.metaproj&quot; (4) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj.metaproj&quot; (13) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (15) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\generate_user-guide.xml.vcxproj&quot; (16) dal progetto &quot;C:\Development\wsbuild64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (15) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\generate_user-guide.xml\generate.B0E9B8C9.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\generate_user-guide.xml\generate.B0E9B8C9.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\generate_user-guide.xml\generate.B0E9B8C9.tlog\generate_user-guide.xml.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\generate_user-guide.xml.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guide_docbook.vcxproj.metaproj&quot; (17) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guide_docbook.vcxproj&quot; (18) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guide_docbook.vcxproj.metaproj&quot; (17) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\user_guide_docbook\user_gui.A992DE34.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\user_guide_docbook\user_gui.A992DE34.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\user_guide_docbook\user_gui.A992DE34.tlog\user_guide_docbook.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guide_docbook.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guide_docbook.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj&quot; (19) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\user_guide_chm\user_guide_chm.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\user_guide_chm\user_guide_chm.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\user_guide_chm\user_guide_chm.tlog\user_guide_chm.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj&quot; (20) dal progetto &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj.metaproj&quot; (13) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\user_guides\user_guides.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\user_guides\user_guides.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\user_guides\user_guides.tlog\user_guides.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\user_guides.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj&quot; (21) dal progetto &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj.metaproj&quot; (4) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\all_guides\all_guides.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\all_guides\all_guides.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\all_guides\all_guides.tlog\all_guides.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\all_guides.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\androiddump.vcxproj.metaproj&quot; (22) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj.metaproj&quot; (23) dal progetto &quot;C:\Development\wsbuild64\androiddump.vcxproj.metaproj&quot; (22) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\version.vcxproj.metaproj&quot; (24) dal progetto &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj.metaproj&quot; (23) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\version.vcxproj&quot; (25) dal progetto &quot;C:\Development\wsbuild64\version.vcxproj.metaproj&quot; (24) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\version\version.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  version.h unchanged.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\version\version.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\version\version.tlog\version.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\version.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\version.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (26) dal progetto &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj.metaproj&quot; (23) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\zlib\zlib.vcxproj.metaproj&quot; (27) dal progetto &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (26) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\zlib\zlib.vcxproj&quot; (28) dal progetto &quot;C:\Development\wsbuild64\zlib\zlib.vcxproj.metaproj&quot; (27) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;zlib.dir\RelWithDebInfo\zlib.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  zlib.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\zlib1.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;zlib.dir\RelWithDebInfo\zlib.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;zlib.dir\RelWithDebInfo\zlib.tlog\zlib.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\zlib\zlib.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\zlib\zlib.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj&quot; (29) dal progetto &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (26) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wsutil.dir\RelWithDebInfo\wsutil.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wsutil.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\libwsutil.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wsutil.dir\RelWithDebInfo\wsutil.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wsutil.dir\RelWithDebInfo\wsutil.tlog\wsutil.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj&quot; (30) dal progetto &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj.metaproj&quot; (23) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wiretap.dir\RelWithDebInfo\wiretap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wiretap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\wiretap-2.1.0-YourExtraVersionInfo.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wiretap.dir\RelWithDebInfo\wiretap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wiretap.dir\RelWithDebInfo\wiretap.tlog\wiretap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\wiretap\wiretap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\androiddump.vcxproj&quot; (31) dal progetto &quot;C:\Development\wsbuild64\androiddump.vcxproj.metaproj&quot; (22) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;androiddump.dir\RelWithDebInfo\androiddump.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  androiddump.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\extcap\androiddump.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;androiddump.dir\RelWithDebInfo\androiddump.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;androiddump.dir\RelWithDebInfo\androiddump.tlog\androiddump.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\androiddump.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\androiddump.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\capchild\capchild.vcxproj.metaproj&quot; (32) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\capchild\capchild.vcxproj&quot; (33) dal progetto &quot;C:\Development\wsbuild64\capchild\capchild.vcxproj.metaproj&quot; (32) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;capchild.dir\RelWithDebInfo\capchild.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  capchild.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\capchild.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;capchild.dir\RelWithDebInfo\capchild.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;capchild.dir\RelWithDebInfo\capchild.tlog\capchild.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\capchild\capchild.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\capchild\capchild.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\capinfos.vcxproj.metaproj&quot; (34) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\capinfos.vcxproj&quot; (35) dal progetto &quot;C:\Development\wsbuild64\capinfos.vcxproj.metaproj&quot; (34) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;capinfos.dir\RelWithDebInfo\capinfos.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  capinfos.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\capinfos.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;capinfos.dir\RelWithDebInfo\capinfos.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;capinfos.dir\RelWithDebInfo\capinfos.tlog\capinfos.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\capinfos.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\capinfos.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\captype.vcxproj.metaproj&quot; (36) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\captype.vcxproj&quot; (37) dal progetto &quot;C:\Development\wsbuild64\captype.vcxproj.metaproj&quot; (36) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;captype.dir\RelWithDebInfo\captype.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  captype.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\captype.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;captype.dir\RelWithDebInfo\captype.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;captype.dir\RelWithDebInfo\captype.tlog\captype.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\captype.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\captype.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\caputils\caputils.vcxproj.metaproj&quot; (38) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\caputils\caputils.vcxproj&quot; (39) dal progetto &quot;C:\Development\wsbuild64\caputils\caputils.vcxproj.metaproj&quot; (38) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;caputils.dir\RelWithDebInfo\caputils.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  caputils.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\caputils.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;caputils.dir\RelWithDebInfo\caputils.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;caputils.dir\RelWithDebInfo\caputils.tlog\caputils.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\caputils\caputils.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\caputils\caputils.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ciscodump.vcxproj.metaproj&quot; (40) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\writecap\writecap.vcxproj.metaproj&quot; (41) dal progetto &quot;C:\Development\wsbuild64\ciscodump.vcxproj.metaproj&quot; (40) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\writecap\writecap.vcxproj&quot; (42) dal progetto &quot;C:\Development\wsbuild64\writecap\writecap.vcxproj.metaproj&quot; (41) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;writecap.dir\RelWithDebInfo\writecap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  writecap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\writecap.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;writecap.dir\RelWithDebInfo\writecap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;writecap.dir\RelWithDebInfo\writecap.tlog\writecap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\writecap\writecap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\writecap\writecap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ciscodump.vcxproj&quot; (43) dal progetto &quot;C:\Development\wsbuild64\ciscodump.vcxproj.metaproj&quot; (40) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;ciscodump.dir\RelWithDebInfo\ciscodump.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  ciscodump.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\extcap\ciscodump.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;ciscodump.dir\RelWithDebInfo\ciscodump.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;ciscodump.dir\RelWithDebInfo\ciscodump.tlog\ciscodump.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ciscodump.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ciscodump.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\copy_data_files.vcxproj.metaproj&quot; (44) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\doc\docs.vcxproj.metaproj&quot; (45) dal progetto &quot;C:\Development\wsbuild64\copy_data_files.vcxproj.metaproj&quot; (44) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\doc\docs.vcxproj&quot; (46) dal progetto &quot;C:\Development\wsbuild64\doc\docs.vcxproj.metaproj&quot; (45) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\docs\docs.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\docs\docs.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\docs\docs.tlog\docs.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\doc\docs.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\doc\docs.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\wslua\wsluaauxiliary.vcxproj.metaproj&quot; (47) dal progetto &quot;C:\Development\wsbuild64\copy_data_files.vcxproj.metaproj&quot; (44) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\wslua\wsluaauxiliary.vcxproj&quot; (48) dal progetto &quot;C:\Development\wsbuild64\epan\wslua\wsluaauxiliary.vcxproj.metaproj&quot; (47) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\wsluaauxiliary\wsluaauxiliary.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\wsluaauxiliary\wsluaauxiliary.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\wsluaauxiliary\wsluaauxiliary.tlog\wsluaauxiliary.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wslua\wsluaauxiliary.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wslua\wsluaauxiliary.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\copy_data_files.vcxproj&quot; (49) dal progetto &quot;C:\Development\wsbuild64\copy_data_files.vcxproj.metaproj&quot; (44) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\copy_data_files\copy_data_files.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\copy_data_files\copy_data_files.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\copy_data_files\copy_data_files.tlog\copy_data_files.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_data_files.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_data_files.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (50) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) dal progetto &quot;C:\Development\wsbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (50) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) dal progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\copy_cli_dlls.vcxproj.metaproj&quot; (53) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\copy_cli_dlls.vcxproj&quot; (54) dal progetto &quot;C:\Development\wsbuild64\copy_cli_dlls.vcxproj.metaproj&quot; (53) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\copy_cli_dlls\copy_cli_dlls.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
PreBuildEvent:
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;libglib-2.0-0.dll&quot; xcopy libglib-2.0-0.dll C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;libgio-2.0-0.dll&quot; xcopy libgio-2.0-0.dll C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;libgmodule-2.0-0.dll&quot; xcopy libgmodule-2.0-0.dll C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;libgobject-2.0-0.dll&quot; xcopy libgobject-2.0-0.dll C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;libintl-8.dll&quot; xcopy libintl-8.dll C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if exist &quot;&quot; xcopy  C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if not exist &quot;C:\Development\wsbuild64\run\RelWithDebInfo\gspawn-win64-helper-console.exe&quot; xcopy gspawn-win64-helper-console.exe C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  cd C:\Development\wireshark-win64-libs\gtk2\bin
  if %errorlevel% neq 0 goto :cmEnd
  C:
  if %errorlevel% neq 0 goto :cmEnd
  if not exist &quot;C:\Development\wsbuild64\run\RelWithDebInfo\gspawn-win64-helper.exe&quot; xcopy gspawn-win64-helper.exe C:\Development\wsbuild64\run\RelWithDebInfo /D /Y
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/bin/x64/airpcap.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/c-ares-1.11.0-win64ws/bin/libcares-2.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/GeoIP-1.6.6-win64ws/bin/libGeoIP-1.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/libssh-0.7.2-win64ws/bin/libssh.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcc_s_seh-1.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgmp-10.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgcc_s_seh-1.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libffi-6.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libhogweed-2-4.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libnettle-4-6.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libp11-kit-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gnutls-3.2.15-2.9-win64ws/bin/libtasn1-6.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/bin/comerr64.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/bin/krb5_64.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/kfw-3-2-2-x64-ws/bin/k5sprt64.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/lua5.2.3/lua52.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/bin/libsmi-2.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/mibs/iana C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/mibs/ietf C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/mibs/irtf C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/mibs/site C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/mibs/tubs C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/pibs C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/libsmi-svn-40773-win64ws/share/yang C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E remove_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs/iana
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E remove_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs/ietf
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E remove_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs/site
  if %errorlevel% neq 0 goto :cmEnd
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E remove_directory C:/Development/wsbuild64/run/RelWithDebInfo/snmp/mibs/tubs
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/WinSparkle-0.3-44-g2c8d9d3-win64ws/WinSparkle.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  :VCEnd
  0 File copiati
  0 File copiati
  0 File copiati
  0 File copiati
  0 File copiati
CustomBuild:
  Tutti gli output sono aggiornati.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\copy_cli_dlls\copy_cli_dlls.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\copy_cli_dlls\copy_cli_dlls.tlog\copy_cli_dlls.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_cli_dlls.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_cli_dlls.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\crypt\crypt.vcxproj.metaproj&quot; (55) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\crypt\crypt.vcxproj&quot; (56) dal progetto &quot;C:\Development\wsbuild64\epan\crypt\crypt.vcxproj.metaproj&quot; (55) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;crypt.dir\RelWithDebInfo\crypt.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  crypt.vcxproj -&gt; C:\Development\wsbuild64\epan\crypt\crypt.dir\RelWithDebInfo\crypt.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;crypt.dir\RelWithDebInfo\crypt.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;crypt.dir\RelWithDebInfo\crypt.tlog\crypt.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\crypt\crypt.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\crypt\crypt.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (57) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\tools\lemon\lemon.vcxproj.metaproj&quot; (58) dal progetto &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (57) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\tools\lemon\lemon.vcxproj&quot; (59) dal progetto &quot;C:\Development\wsbuild64\tools\lemon\lemon.vcxproj.metaproj&quot; (58) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;lemon.dir\RelWithDebInfo\lemon.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  lemon.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\lemon.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;lemon.dir\RelWithDebInfo\lemon.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;lemon.dir\RelWithDebInfo\lemon.tlog\lemon.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\tools\lemon\lemon.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\tools\lemon\lemon.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj&quot; (60) dal progetto &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (57) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;dfilter.dir\RelWithDebInfo\dfilter.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  dfilter.vcxproj -&gt; C:\Development\wsbuild64\epan\dfilter\dfilter.dir\RelWithDebInfo\dfilter.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;dfilter.dir\RelWithDebInfo\dfilter.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;dfilter.dir\RelWithDebInfo\dfilter.tlog\dfilter.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\dissectors\dissectors.vcxproj.metaproj&quot; (61) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\dissectors\dissectors.vcxproj&quot; (62) dal progetto &quot;C:\Development\wsbuild64\epan\dissectors\dissectors.vcxproj.metaproj&quot; (61) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;dissectors.dir\RelWithDebInfo\dissectors.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  dissectors.vcxproj -&gt; C:\Development\wsbuild64\epan\dissectors\dissectors.dir\RelWithDebInfo\dissectors.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;dissectors.dir\RelWithDebInfo\dissectors.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;dissectors.dir\RelWithDebInfo\dissectors.tlog\dissectors.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dissectors\dissectors.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dissectors\dissectors.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\ftypes\ftypes.vcxproj.metaproj&quot; (63) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\ftypes\ftypes.vcxproj&quot; (64) dal progetto &quot;C:\Development\wsbuild64\epan\ftypes\ftypes.vcxproj.metaproj&quot; (63) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;ftypes.dir\RelWithDebInfo\ftypes.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  ftypes.vcxproj -&gt; C:\Development\wsbuild64\epan\ftypes\ftypes.dir\RelWithDebInfo\ftypes.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;ftypes.dir\RelWithDebInfo\ftypes.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;ftypes.dir\RelWithDebInfo\ftypes.tlog\ftypes.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\ftypes\ftypes.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\ftypes\ftypes.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\nghttp2\nghttp2.vcxproj.metaproj&quot; (65) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\nghttp2\nghttp2.vcxproj&quot; (66) dal progetto &quot;C:\Development\wsbuild64\epan\nghttp2\nghttp2.vcxproj.metaproj&quot; (65) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;nghttp2.dir\RelWithDebInfo\nghttp2.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  nghttp2.vcxproj -&gt; C:\Development\wsbuild64\epan\nghttp2\nghttp2.dir\RelWithDebInfo\nghttp2.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;nghttp2.dir\RelWithDebInfo\nghttp2.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;nghttp2.dir\RelWithDebInfo\nghttp2.tlog\nghttp2.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\nghttp2\nghttp2.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\nghttp2\nghttp2.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\wmem\wmem.vcxproj.metaproj&quot; (67) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\wmem\wmem.vcxproj&quot; (68) dal progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem.vcxproj.metaproj&quot; (67) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wmem.dir\RelWithDebInfo\wmem.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  wmem.vcxproj -&gt; C:\Development\wsbuild64\epan\wmem\wmem.dir\RelWithDebInfo\wmem.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;wmem.dir\RelWithDebInfo\wmem.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wmem.dir\RelWithDebInfo\wmem.tlog\wmem.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\wslua\wslua.vcxproj.metaproj&quot; (69) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\wslua\wslua.vcxproj&quot; (70) dal progetto &quot;C:\Development\wsbuild64\epan\wslua\wslua.vcxproj.metaproj&quot; (69) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wslua.dir\RelWithDebInfo\wslua.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  wslua.vcxproj -&gt; C:\Development\wsbuild64\epan\wslua\wslua.dir\RelWithDebInfo\wslua.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;wslua.dir\RelWithDebInfo\wslua.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wslua.dir\RelWithDebInfo\wslua.tlog\wslua.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wslua\wslua.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wslua\wslua.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\epan.vcxproj&quot; (71) dal progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (52) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;epan.dir\RelWithDebInfo\epan.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  epan.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\libwireshark.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;epan.dir\RelWithDebInfo\epan.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;epan.dir\RelWithDebInfo\epan.tlog\epan.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\epan.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ui\qt\qtui.vcxproj.metaproj&quot; (72) dal progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\ui\qt\qtui.vcxproj&quot; (73) dal progetto &quot;C:\Development\wsbuild64\ui\qt\qtui.vcxproj.metaproj&quot; (72) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;qtui.dir\RelWithDebInfo\qtui.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  qtui.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\qtui.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;qtui.dir\RelWithDebInfo\qtui.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;qtui.dir\RelWithDebInfo\qtui.tlog\qtui.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\qt\qtui.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\qt\qtui.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ui\ui.vcxproj.metaproj&quot; (74) dal progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\ui\ui.vcxproj&quot; (75) dal progetto &quot;C:\Development\wsbuild64\ui\ui.vcxproj.metaproj&quot; (74) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;ui.dir\RelWithDebInfo\ui.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  ui.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\ui.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;ui.dir\RelWithDebInfo\ui.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;ui.dir\RelWithDebInfo\ui.tlog\ui.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\ui.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\ui.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\codecs\wscodecs.vcxproj.metaproj&quot; (76) dal progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\codecs\wscodecs.vcxproj&quot; (77) dal progetto &quot;C:\Development\wsbuild64\codecs\wscodecs.vcxproj.metaproj&quot; (76) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wscodecs.dir\RelWithDebInfo\wscodecs.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wscodecs.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\libwscodecs.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wscodecs.dir\RelWithDebInfo\wscodecs.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wscodecs.dir\RelWithDebInfo\wscodecs.tlog\wscodecs.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\codecs\wscodecs.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\codecs\wscodecs.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wireshark.vcxproj&quot; (78) dal progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (51) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Aggiornamento timestamp di &quot;wireshark.dir\RelWithDebInfo\wireshark.tlog\unsuccessfulbuild&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\link.exe /ERRORREPORT:QUEUE /OUT:&quot;C:\Development\wsbuild64\run\RelWithDebInfo\Wireshark.exe&quot; /INCREMENTAL:NO /NOLOGO /LIBPATH:C:/Development/wsbuild64/ui /LIBPATH:C:/Development/wsbuild64/ui/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/ui/gtk /LIBPATH:C:/Development/wsbuild64/ui/gtk/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/ui/qt /LIBPATH:C:/Development/wsbuild64/ui/qt/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/capchild /LIBPATH:C:/Development/wsbuild64/capchild/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/caputils /LIBPATH:C:/Development/wsbuild64/caputils/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/codecs /LIBPATH:C:/Development/wsbuild64/codecs/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/epan /LIBPATH:C:/Development/wsbuild64/epan/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/randpkt_core /LIBPATH:C:/Development/wsbuild64/randpkt_core/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/wiretap /LIBPATH:C:/Development/wsbuild64/wiretap/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/writecap /LIBPATH:C:/Development/wsbuild64/writecap/RelWithDebInfo /LIBPATH:C:/Development/wsbuild64/wsutil /LIBPATH:C:/Development/wsbuild64/wsutil/RelWithDebInfo kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib run\RelWithDebInfo\qtui.lib run\RelWithDebInfo\ui.lib run\RelWithDebInfo\capchild.lib run\RelWithDebInfo\caputils.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5PrintSupport.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Multimedia.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Svg.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5WinExtras.lib &quot;C:\Development\wireshark-win64-libs\gtk2\lib\glib-2.0.lib&quot; run\RelWithDebInfo\wscodecs.lib run\RelWithDebInfo\wireshark.lib &quot;C:\Development\wireshark-win64-libs\AirPcap_Devpack_4_1_0_1622\Airpcap_Devpack\lib\airpcap.lib&quot; &quot;C:\Development\wireshark-win64-libs\WpdPack\Lib\x64\wpcap.lib&quot; &quot;C:\Development\wireshark-win64-libs\c-ares-1.11.0-win64ws\lib\libcares-2.lib&quot; &quot;C:\Development\wireshark-win64-libs\kfw-3-2-2-x64-ws\lib\krb5_64.lib&quot; &quot;C:\Development\wireshark-win64-libs\lua5.2.3\lua52.lib&quot; &quot;C:\Development\wireshark-win64-libs\GeoIP-1.6.6-win64ws\lib\libGeoIP-1.lib&quot; &quot;C:\Development\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgcrypt-20.lib&quot; &quot;C:\Development\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgpg-error6-0.lib&quot; &quot;C:\Development\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgnutls-28.lib&quot; &quot;C:\Development\wireshark-win64-libs\libsmi-svn-40773-win64ws\lib\libsmi-2.lib&quot; &quot;C:\Development\wireshark-win64-libs\WinSparkle-0.3-44-g2c8d9d3-win64ws\WinSparkle.lib&quot; C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Network.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Widgets.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Gui.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\Qt5Core.lib C:\Qt\Qt5.6.0_32\5.6\msvc2013\lib\qtmain.lib &quot;run\RelWithDebInfo\wiretap-2.1.0-YourExtraVersionInfo.lib&quot; run\RelWithDebInfo\wsutil.lib &quot;C:\Development\wireshark-win64-libs\gtk2\lib\glib-2.0.lib&quot; run\RelWithDebInfo\zlib.lib &quot;C:\Development\wireshark-win64-libs\gtk2\lib\gmodule-2.0.lib&quot; wsock32.lib ws2_32.lib psapi.lib &quot;C:\Development\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgcrypt-20.lib&quot; &quot;C:\Development\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\bin\libgpg-error6-0.lib&quot; /MANIFEST:NO /DEBUG /PDB:&quot;C:/Development/wsbuild64/run/RelWithDebInfo/Wireshark.pdb&quot; /SUBSYSTEM:WINDOWS /LARGEADDRESSAWARE /TLBID:1 /RELEASE /DYNAMICBASE /NXCOMPAT /IMPLIB:&quot;C:/Development/wsbuild64/run/RelWithDebInfo/Wireshark.lib&quot; /MACHINE:X64  /machine:x64 setargv.obj wireshark.dir\RelWithDebInfo\wireshark.res
  wireshark.dir\RelWithDebInfo\file_dlg_win32.res
  &quot;wireshark.dir\RelWithDebInfo\wireshark-qt.obj&quot;
  wireshark.dir\RelWithDebInfo\capture_info.obj
  wireshark.dir\RelWithDebInfo\capture_opts.obj
  wireshark.dir\RelWithDebInfo\file.obj
  wireshark.dir\RelWithDebInfo\fileset.obj
  wireshark.dir\RelWithDebInfo\filter_files.obj
  wireshark.dir\RelWithDebInfo\summary.obj
  wireshark.dir\RelWithDebInfo\cfile.obj
  wireshark.dir\RelWithDebInfo\frame_tvbuff.obj
  wireshark.dir\RelWithDebInfo\sync_pipe_write.obj
  wireshark.dir\RelWithDebInfo\ws_version_info.obj
  wireshark.dir\RelWithDebInfo\extcap.obj
  wireshark.dir\RelWithDebInfo\extcap_parser.obj
  wireshark.dir\RelWithDebInfo\console_win32.obj
  wireshark.dir\RelWithDebInfo\file_dlg_win32.obj
  wireshark.dir\RelWithDebInfo\print_win32.obj
Qt5Widgets.lib(Qt5Widgets.dll) : fatal error LNK1112: module machine type &#39;X86&#39; conflicts with target machine type &#39;x64&#39; [C:\Development\wsbuild64\wireshark.vcxproj]
Compilazione progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj&quot; (destinazioni predefinite) NON COMPLETATA.
Compilazione progetto &quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (destinazioni predefinite) NON COMPLETATA.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (destinazioni predefinite) NON COMPLETATA.
Compilazione di &quot;C:\Development\wsbuild64\dftest.vcxproj.metaproj&quot; (79) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\dftest.vcxproj&quot; (80) dal progetto &quot;C:\Development\wsbuild64\dftest.vcxproj.metaproj&quot; (79) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;dftest.dir\RelWithDebInfo\dftest.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  dftest.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\dftest.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;dftest.dir\RelWithDebInfo\dftest.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;dftest.dir\RelWithDebInfo\dftest.tlog\dftest.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\dftest.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\dftest.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\docsis\docsis.vcxproj.metaproj&quot; (81) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\docsis\docsis.vcxproj&quot; (82) dal progetto &quot;C:\Development\wsbuild64\plugins\docsis\docsis.vcxproj.metaproj&quot; (81) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;docsis.dir\RelWithDebInfo\docsis.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  docsis.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\docsis.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;docsis.dir\RelWithDebInfo\docsis.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;docsis.dir\RelWithDebInfo\docsis.tlog\docsis.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\docsis\docsis.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\docsis\docsis.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\dumpcap.vcxproj.metaproj&quot; (83) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\dumpcap.vcxproj&quot; (84) dal progetto &quot;C:\Development\wsbuild64\dumpcap.vcxproj.metaproj&quot; (83) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;dumpcap.dir\RelWithDebInfo\dumpcap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  dumpcap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\dumpcap.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;dumpcap.dir\RelWithDebInfo\dumpcap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;dumpcap.dir\RelWithDebInfo\dumpcap.tlog\dumpcap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\dumpcap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\dumpcap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\editcap.vcxproj.metaproj&quot; (85) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\editcap.vcxproj&quot; (86) dal progetto &quot;C:\Development\wsbuild64\editcap.vcxproj.metaproj&quot; (85) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;editcap.dir\RelWithDebInfo\editcap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  editcap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\editcap.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;editcap.dir\RelWithDebInfo\editcap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;editcap.dir\RelWithDebInfo\editcap.tlog\editcap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\editcap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\editcap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\ethercat\ethercat.vcxproj.metaproj&quot; (87) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\ethercat\ethercat.vcxproj&quot; (88) dal progetto &quot;C:\Development\wsbuild64\plugins\ethercat\ethercat.vcxproj.metaproj&quot; (87) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;ethercat.dir\RelWithDebInfo\ethercat.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  ethercat.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\ethercat.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;ethercat.dir\RelWithDebInfo\ethercat.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;ethercat.dir\RelWithDebInfo\ethercat.tlog\ethercat.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\ethercat\ethercat.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\ethercat\ethercat.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\gryphon\gryphon.vcxproj.metaproj&quot; (89) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\gryphon\gryphon.vcxproj&quot; (90) dal progetto &quot;C:\Development\wsbuild64\plugins\gryphon\gryphon.vcxproj.metaproj&quot; (89) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;gryphon.dir\RelWithDebInfo\gryphon.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  gryphon.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\gryphon.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;gryphon.dir\RelWithDebInfo\gryphon.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;gryphon.dir\RelWithDebInfo\gryphon.tlog\gryphon.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\gryphon\gryphon.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\gryphon\gryphon.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj.metaproj&quot; (91) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\ui\gtk\portaudio.vcxproj.metaproj&quot; (92) dal progetto &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj.metaproj&quot; (91) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\ui\gtk\portaudio.vcxproj&quot; (93) dal progetto &quot;C:\Development\wsbuild64\ui\gtk\portaudio.vcxproj.metaproj&quot; (92) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;portaudio.dir\RelWithDebInfo\portaudio.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  portaudio.vcxproj -&gt; C:\Development\wsbuild64\ui\gtk\portaudio.dir\RelWithDebInfo\portaudio.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;portaudio.dir\RelWithDebInfo\portaudio.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;portaudio.dir\RelWithDebInfo\portaudio.tlog\portaudio.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\gtk\portaudio.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\gtk\portaudio.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj&quot; (94) dal progetto &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj.metaproj&quot; (91) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;gtkui.dir\RelWithDebInfo\gtkui.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  gtkui.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\gtkui.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;gtkui.dir\RelWithDebInfo\gtkui.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;gtkui.dir\RelWithDebInfo\gtkui.tlog\gtkui.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ui\gtk\gtkui.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\dissectors\dcerpc\idl2wrs.vcxproj.metaproj&quot; (95) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\dissectors\dcerpc\idl2wrs.vcxproj&quot; (96) dal progetto &quot;C:\Development\wsbuild64\epan\dissectors\dcerpc\idl2wrs.vcxproj.metaproj&quot; (95) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;idl2wrs.dir\RelWithDebInfo\idl2wrs.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  idl2wrs.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\idl2wrs.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;idl2wrs.dir\RelWithDebInfo\idl2wrs.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;idl2wrs.dir\RelWithDebInfo\idl2wrs.tlog\idl2wrs.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dissectors\dcerpc\idl2wrs.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\dissectors\dcerpc\idl2wrs.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\irda\irda.vcxproj.metaproj&quot; (97) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\irda\irda.vcxproj&quot; (98) dal progetto &quot;C:\Development\wsbuild64\plugins\irda\irda.vcxproj.metaproj&quot; (97) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;irda.dir\RelWithDebInfo\irda.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  irda.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\irda.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;irda.dir\RelWithDebInfo\irda.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;irda.dir\RelWithDebInfo\irda.tlog\irda.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\irda\irda.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\irda\irda.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\m2m\m2m.vcxproj.metaproj&quot; (99) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\m2m\m2m.vcxproj&quot; (100) dal progetto &quot;C:\Development\wsbuild64\plugins\m2m\m2m.vcxproj.metaproj&quot; (99) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;m2m.dir\RelWithDebInfo\m2m.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  m2m.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\m2m.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;m2m.dir\RelWithDebInfo\m2m.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;m2m.dir\RelWithDebInfo\m2m.tlog\m2m.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\m2m\m2m.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\m2m\m2m.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\mate\mate.vcxproj.metaproj&quot; (101) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\mate\mate.vcxproj&quot; (102) dal progetto &quot;C:\Development\wsbuild64\plugins\mate\mate.vcxproj.metaproj&quot; (101) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;mate.dir\RelWithDebInfo\mate.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  mate.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\mate.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;mate.dir\RelWithDebInfo\mate.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;mate.dir\RelWithDebInfo\mate.tlog\mate.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\mate\mate.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\mate\mate.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\mergecap.vcxproj.metaproj&quot; (103) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\mergecap.vcxproj&quot; (104) dal progetto &quot;C:\Development\wsbuild64\mergecap.vcxproj.metaproj&quot; (103) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;mergecap.dir\RelWithDebInfo\mergecap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  mergecap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\mergecap.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;mergecap.dir\RelWithDebInfo\mergecap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;mergecap.dir\RelWithDebInfo\mergecap.tlog\mergecap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\mergecap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\mergecap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\opcua\opcua.vcxproj.metaproj&quot; (105) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\opcua\opcua.vcxproj&quot; (106) dal progetto &quot;C:\Development\wsbuild64\plugins\opcua\opcua.vcxproj.metaproj&quot; (105) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;opcua.dir\RelWithDebInfo\opcua.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  opcua.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\opcua.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;opcua.dir\RelWithDebInfo\opcua.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;opcua.dir\RelWithDebInfo\opcua.tlog\opcua.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\opcua\opcua.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\opcua\opcua.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\profinet\profinet.vcxproj.metaproj&quot; (107) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\profinet\profinet.vcxproj&quot; (108) dal progetto &quot;C:\Development\wsbuild64\plugins\profinet\profinet.vcxproj.metaproj&quot; (107) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;profinet.dir\RelWithDebInfo\profinet.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  profinet.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\profinet.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;profinet.dir\RelWithDebInfo\profinet.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;profinet.dir\RelWithDebInfo\profinet.tlog\profinet.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\profinet\profinet.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\profinet\profinet.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\randpkt.vcxproj.metaproj&quot; (109) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\randpkt_core\randpkt_core.vcxproj.metaproj&quot; (110) dal progetto &quot;C:\Development\wsbuild64\randpkt.vcxproj.metaproj&quot; (109) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\randpkt_core\randpkt_core.vcxproj&quot; (111) dal progetto &quot;C:\Development\wsbuild64\randpkt_core\randpkt_core.vcxproj.metaproj&quot; (110) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;randpkt_core.dir\RelWithDebInfo\randpkt_core.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  randpkt_core.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\randpkt_core.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;randpkt_core.dir\RelWithDebInfo\randpkt_core.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;randpkt_core.dir\RelWithDebInfo\randpkt_core.tlog\randpkt_core.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\randpkt_core\randpkt_core.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\randpkt_core\randpkt_core.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\randpkt.vcxproj&quot; (112) dal progetto &quot;C:\Development\wsbuild64\randpkt.vcxproj.metaproj&quot; (109) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;randpkt.dir\RelWithDebInfo\randpkt.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  randpkt.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\randpkt.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;randpkt.dir\RelWithDebInfo\randpkt.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;randpkt.dir\RelWithDebInfo\randpkt.tlog\randpkt.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\randpkt.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\randpkt.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\randpktdump.vcxproj.metaproj&quot; (113) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\randpktdump.vcxproj&quot; (114) dal progetto &quot;C:\Development\wsbuild64\randpktdump.vcxproj.metaproj&quot; (113) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;randpktdump.dir\RelWithDebInfo\randpktdump.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  randpktdump.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\extcap\randpktdump.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;randpktdump.dir\RelWithDebInfo\randpktdump.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;randpktdump.dir\RelWithDebInfo\randpktdump.tlog\randpktdump.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\randpktdump.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\randpktdump.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\rawshark.vcxproj.metaproj&quot; (115) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\rawshark.vcxproj&quot; (116) dal progetto &quot;C:\Development\wsbuild64\rawshark.vcxproj.metaproj&quot; (115) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;rawshark.dir\RelWithDebInfo\rawshark.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  rawshark.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\rawshark.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;rawshark.dir\RelWithDebInfo\rawshark.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;rawshark.dir\RelWithDebInfo\rawshark.tlog\rawshark.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\rawshark.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\rawshark.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\reordercap.vcxproj.metaproj&quot; (117) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\reordercap.vcxproj&quot; (118) dal progetto &quot;C:\Development\wsbuild64\reordercap.vcxproj.metaproj&quot; (117) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;reordercap.dir\RelWithDebInfo\reordercap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  reordercap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\reordercap.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;reordercap.dir\RelWithDebInfo\reordercap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;reordercap.dir\RelWithDebInfo\reordercap.tlog\reordercap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\reordercap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\reordercap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\sshdump.vcxproj.metaproj&quot; (119) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\sshdump.vcxproj&quot; (120) dal progetto &quot;C:\Development\wsbuild64\sshdump.vcxproj.metaproj&quot; (119) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;sshdump.dir\RelWithDebInfo\sshdump.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  sshdump.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\extcap\sshdump.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;sshdump.dir\RelWithDebInfo\sshdump.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;sshdump.dir\RelWithDebInfo\sshdump.tlog\sshdump.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\sshdump.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\sshdump.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\stats_tree\stats_tree.vcxproj.metaproj&quot; (121) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\stats_tree\stats_tree.vcxproj&quot; (122) dal progetto &quot;C:\Development\wsbuild64\plugins\stats_tree\stats_tree.vcxproj.metaproj&quot; (121) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;stats_tree.dir\RelWithDebInfo\stats_tree.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  stats_tree.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\stats_tree.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;stats_tree.dir\RelWithDebInfo\stats_tree.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;stats_tree.dir\RelWithDebInfo\stats_tree.tlog\stats_tree.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\stats_tree\stats_tree.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\stats_tree\stats_tree.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\text2pcap.vcxproj.metaproj&quot; (123) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\text2pcap.vcxproj&quot; (124) dal progetto &quot;C:\Development\wsbuild64\text2pcap.vcxproj.metaproj&quot; (123) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;text2pcap.dir\RelWithDebInfo\text2pcap.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  text2pcap.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\text2pcap.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;text2pcap.dir\RelWithDebInfo\text2pcap.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;text2pcap.dir\RelWithDebInfo\text2pcap.tlog\text2pcap.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\text2pcap.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\text2pcap.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\tfshark.vcxproj.metaproj&quot; (125) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\tfshark.vcxproj&quot; (126) dal progetto &quot;C:\Development\wsbuild64\tfshark.vcxproj.metaproj&quot; (125) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;tfshark.dir\RelWithDebInfo\tfshark.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  tfshark.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\tfshark.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;tfshark.dir\RelWithDebInfo\tfshark.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;tfshark.dir\RelWithDebInfo\tfshark.tlog\tfshark.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\tfshark.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\tfshark.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\tshark.vcxproj.metaproj&quot; (127) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\tshark.vcxproj&quot; (128) dal progetto &quot;C:\Development\wsbuild64\tshark.vcxproj.metaproj&quot; (127) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;tshark.dir\RelWithDebInfo\tshark.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  tshark.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\tshark.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;tshark.dir\RelWithDebInfo\tshark.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;tshark.dir\RelWithDebInfo\tshark.tlog\tshark.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\tshark.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\tshark.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\unistim\unistim.vcxproj.metaproj&quot; (129) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\unistim\unistim.vcxproj&quot; (130) dal progetto &quot;C:\Development\wsbuild64\plugins\unistim\unistim.vcxproj.metaproj&quot; (129) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;unistim.dir\RelWithDebInfo\unistim.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  unistim.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\unistim.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;unistim.dir\RelWithDebInfo\unistim.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;unistim.dir\RelWithDebInfo\unistim.tlog\unistim.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\unistim\unistim.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\unistim\unistim.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimax\wimax.vcxproj.metaproj&quot; (131) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimax\wimax.vcxproj&quot; (132) dal progetto &quot;C:\Development\wsbuild64\plugins\wimax\wimax.vcxproj.metaproj&quot; (131) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wimax.dir\RelWithDebInfo\wimax.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wimax.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\wimax.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wimax.dir\RelWithDebInfo\wimax.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wimax.dir\RelWithDebInfo\wimax.tlog\wimax.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimax\wimax.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimax\wimax.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimaxasncp\wimaxasncp.vcxproj.metaproj&quot; (133) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimaxasncp\wimaxasncp.vcxproj&quot; (134) dal progetto &quot;C:\Development\wsbuild64\plugins\wimaxasncp\wimaxasncp.vcxproj.metaproj&quot; (133) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wimaxasncp.dir\RelWithDebInfo\wimaxasncp.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wimaxasncp.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\wimaxasncp.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wimaxasncp.dir\RelWithDebInfo\wimaxasncp.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wimaxasncp.dir\RelWithDebInfo\wimaxasncp.tlog\wimaxasncp.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimaxasncp\wimaxasncp.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimaxasncp\wimaxasncp.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimaxmacphy\wimaxmacphy.vcxproj.metaproj&quot; (135) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\plugins\wimaxmacphy\wimaxmacphy.vcxproj&quot; (136) dal progetto &quot;C:\Development\wsbuild64\plugins\wimaxmacphy\wimaxmacphy.vcxproj.metaproj&quot; (135) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wimaxmacphy.dir\RelWithDebInfo\wimaxmacphy.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wimaxmacphy.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\plugins\wimaxmacphy.dll
FinalizeBuildStatus:
  Eliminazione del file &quot;wimaxmacphy.dir\RelWithDebInfo\wimaxmacphy.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wimaxmacphy.dir\RelWithDebInfo\wimaxmacphy.tlog\wimaxmacphy.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimaxmacphy\wimaxmacphy.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\plugins\wimaxmacphy\wimaxmacphy.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj.metaproj&quot; (137) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\copy_gtk_dlls.vcxproj.metaproj&quot; (138) dal progetto &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj.metaproj&quot; (137) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\copy_gtk_dlls.vcxproj&quot; (139) dal progetto &quot;C:\Development\wsbuild64\copy_gtk_dlls.vcxproj.metaproj&quot; (138) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\copy_gtk_dlls\copy_gtk_dlls.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
PreBuildEvent:
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libgtk-win32-2.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libgdk-win32-2.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libgdk_pixbuf-2.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libatk-1.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpango-1.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpangowin32-1.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libcairo-2.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpangocairo-1.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libffi-6.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libfontconfig-1.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpangoft2-1.0-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libfreetype-6.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libharfbuzz-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libjasper-1.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libjpeg-8.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/liblzma-5.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpixman-1-0.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libpng16-16.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libtiff-5.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/bin/libxml2-2.dll C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo/etc
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/gtk2/etc C:/Development/wsbuild64/run/RelWithDebInfo/etc
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E make_directory C:/Development/wsbuild64/run/RelWithDebInfo/lib/gtk-2.0/2.10.0/engines
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/lib/gtk-2.0/2.10.0/engines/libpixmap.dll C:/Development/wsbuild64/run/RelWithDebInfo/lib/gtk-2.0/2.10.0/engines
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/lib/gtk-2.0/2.10.0/engines/libwimp.dll C:/Development/wsbuild64/run/RelWithDebInfo/lib/gtk-2.0/2.10.0/engines
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/wireshark-win64-libs/gtk2/share/themes/MS-Windows/gtk-2.0/gtkrc C:/Development/wsbuild64/run/RelWithDebInfo/etc/gtk-2.0
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_directory C:/Development/wireshark-win64-libs/gtk2/lib/gtk-2.0 C:/Development/wsbuild64/run/RelWithDebInfo/lib/gtk-2.0
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  :VCEnd
CustomBuild:
  Tutti gli output sono aggiornati.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\copy_gtk_dlls\copy_gtk_dlls.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\copy_gtk_dlls\copy_gtk_dlls.tlog\copy_gtk_dlls.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_gtk_dlls.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\copy_gtk_dlls.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj&quot; (140) dal progetto &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj.metaproj&quot; (137) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wireshark-gtk.dir\RelWithDebInfo\wireshark-gtk.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
ResourceCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wireshark-gtk.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\wireshark-gtk.exe
PostBuildEvent:
  setlocal
  &quot;C:\Program Files (x86)\CMake\bin\cmake.exe&quot; -E copy_if_different C:/Development/Wireshark/wireshark/ipmap.html C:/Development/wsbuild64/run/RelWithDebInfo
  if %errorlevel% neq 0 goto :cmEnd
  :cmEnd
  endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone
  :cmErrorLevel
  exit /b %1
  :cmDone
  if %errorlevel% neq 0 goto :VCEnd
  :VCEnd
FinalizeBuildStatus:
  Eliminazione del file &quot;wireshark-gtk.dir\RelWithDebInfo\wireshark-gtk.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wireshark-gtk.dir\RelWithDebInfo\wireshark-gtk.tlog\wireshark-gtk.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\wireshark-gtk.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\zlib\zlibstatic.vcxproj.metaproj&quot; (141) dal progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (2) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\zlib\zlibstatic.vcxproj&quot; (142) dal progetto &quot;C:\Development\wsbuild64\zlib\zlibstatic.vcxproj.metaproj&quot; (141) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;zlibstatic.dir\RelWithDebInfo\zlibstatic.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Lib:
  Tutti gli output sono aggiornati.
  zlibstatic.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\zlibstatic.lib
FinalizeBuildStatus:
  Eliminazione del file &quot;zlibstatic.dir\RelWithDebInfo\zlibstatic.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;zlibstatic.dir\RelWithDebInfo\zlibstatic.tlog\zlibstatic.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\zlib\zlibstatic.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\zlib\zlibstatic.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazioni predefinite) NON COMPLETATA.
Compilazione di &quot;C:\Development\wsbuild64\epan\exntest.vcxproj.metaproj&quot; (143) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\exntest.vcxproj&quot; (144) dal progetto &quot;C:\Development\wsbuild64\epan\exntest.vcxproj.metaproj&quot; (143) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;exntest.dir\RelWithDebInfo\exntest.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  exntest.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\exntest.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;exntest.dir\RelWithDebInfo\exntest.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;exntest.dir\RelWithDebInfo\exntest.tlog\exntest.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\exntest.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\exntest.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\oids_test.vcxproj.metaproj&quot; (145) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\oids_test.vcxproj&quot; (146) dal progetto &quot;C:\Development\wsbuild64\epan\oids_test.vcxproj.metaproj&quot; (145) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;oids_test.dir\RelWithDebInfo\oids_test.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  oids_test.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\oids_test.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;oids_test.dir\RelWithDebInfo\oids_test.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;oids_test.dir\RelWithDebInfo\oids_test.tlog\oids_test.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\oids_test.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\oids_test.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\reassemble_test.vcxproj.metaproj&quot; (147) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\reassemble_test.vcxproj&quot; (148) dal progetto &quot;C:\Development\wsbuild64\epan\reassemble_test.vcxproj.metaproj&quot; (147) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;reassemble_test.dir\RelWithDebInfo\reassemble_test.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  reassemble_test.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\reassemble_test.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;reassemble_test.dir\RelWithDebInfo\reassemble_test.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;reassemble_test.dir\RelWithDebInfo\reassemble_test.tlog\reassemble_test.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\reassemble_test.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\reassemble_test.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (149) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\release_notes_html.vcxproj&quot; (150) dal progetto &quot;C:\Development\wsbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (149) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\release_notes_html\release_.10728AED.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\release_notes_html\release_.10728AED.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\release_notes_html\release_.10728AED.tlog\release_notes_html.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\release_notes_html.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\docbook\release_notes_txt.vcxproj.metaproj&quot; (151) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\docbook\release_notes_txt.vcxproj&quot; (152) dal progetto &quot;C:\Development\wsbuild64\docbook\release_notes_txt.vcxproj.metaproj&quot; (151) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\release_notes_txt\release_.141A78B5.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\release_notes_txt\release_.141A78B5.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\release_notes_txt\release_.141A78B5.tlog\release_notes_txt.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\release_notes_txt.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\docbook\release_notes_txt.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\test-sh.vcxproj.metaproj&quot; (153) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\test-sh.vcxproj&quot; (154) dal progetto &quot;C:\Development\wsbuild64\test-sh.vcxproj.metaproj&quot; (153) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;x64\RelWithDebInfo\test-sh\test-sh.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  -- Generated C:/Development/wsbuild64/run/RelWithDebInfo/test.sh
FinalizeBuildStatus:
  Eliminazione del file &quot;x64\RelWithDebInfo\test-sh\test-sh.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;x64\RelWithDebInfo\test-sh\test-sh.tlog\test-sh.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\test-sh.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\test-sh.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\tvbtest.vcxproj.metaproj&quot; (155) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\tvbtest.vcxproj&quot; (156) dal progetto &quot;C:\Development\wsbuild64\epan\tvbtest.vcxproj.metaproj&quot; (155) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;tvbtest.dir\RelWithDebInfo\tvbtest.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  tvbtest.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\tvbtest.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;tvbtest.dir\RelWithDebInfo\tvbtest.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;tvbtest.dir\RelWithDebInfo\tvbtest.tlog\tvbtest.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\tvbtest.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\tvbtest.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione di &quot;C:\Development\wsbuild64\epan\wmem\wmem_test.vcxproj.metaproj&quot; (157) dal progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (1) sul nodo 1 (destinazioni predefinite).
Compilazione di &quot;C:\Development\wsbuild64\epan\wmem\wmem_test.vcxproj&quot; (158) dal progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem_test.vcxproj.metaproj&quot; (157) sul nodo 1 (destinazioni predefinite).
InitializeBuildStatus:
  Creazione di &quot;wmem_test.dir\RelWithDebInfo\wmem_test.tlog\unsuccessfulbuild&quot;. Ô stato specificato &quot;AlwaysCreate&quot;.
CustomBuild:
  Tutti gli output sono aggiornati.
ClCompile:
  Tutti gli output sono aggiornati.
Link:
  Tutti gli output sono aggiornati.
  wmem_test.vcxproj -&gt; C:\Development\wsbuild64\run\RelWithDebInfo\wmem_test.exe
FinalizeBuildStatus:
  Eliminazione del file &quot;wmem_test.dir\RelWithDebInfo\wmem_test.tlog\unsuccessfulbuild&quot; in corso.
  Aggiornamento timestamp di &quot;wmem_test.dir\RelWithDebInfo\wmem_test.tlog\wmem_test.lastbuildstate&quot;.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem_test.vcxproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\epan\wmem\wmem_test.vcxproj.metaproj&quot; (destinazioni predefinite) completata.
Compilazione progetto &quot;C:\Development\wsbuild64\Wireshark.sln&quot; (destinazioni predefinite) NON COMPLETATA.

Compilazione NON RIUSCITA.

&quot;C:\Development\wsbuild64\Wireshark.sln&quot; (destinazione predefinita) (1) -&gt;
&quot;C:\Development\wsbuild64\ALL_BUILD.vcxproj.metaproj&quot; (destinazione predefinita) (2) -&gt;
&quot;C:\Development\wsbuild64\copy_qt_dlls.vcxproj.metaproj&quot; (destinazione predefinita) (50) -&gt;
&quot;C:\Development\wsbuild64\wireshark.vcxproj.metaproj&quot; (destinazione predefinita) (51) -&gt;
&quot;C:\Development\wsbuild64\wireshark.vcxproj&quot; (destinazione predefinita) (78) -&gt;
(destinazione: Link) -&gt; 
  Qt5Widgets.lib(Qt5Widgets.dll) : fatal error LNK1112: module machine type &#39;X86&#39; conflicts with target machine type &#39;x64&#39; [C:\Development\wsbuild64\wireshark.vcxproj]

    Avvisi: 0
    Errori: 1

Tempo trascorso 00:00:26.92</code></pre></div><div id="comment-53105-info" class="comment-info"><span class="comment-age">(01 Jun '16, 06:36)</span> kenhero</div></div><span id="53109"></span><div id="comment-53109" class="comment not_top_scorer"><div id="post-53109-score" class="comment-score"></div><div class="comment-text"><p>What does the following command display:</p><pre><code>C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\qtdiag.exe</code></pre></div><div id="comment-53109-info" class="comment-info"><span class="comment-age">(01 Jun '16, 06:48)</span> grahamb ♦</div></div><span id="53111"></span><div id="comment-53111" class="comment not_top_scorer"><div id="post-53111-score" class="comment-score"></div><div class="comment-text"><pre><code>qt.network.ssl: QSslSocket: cannot resolve TLSv1_1_client_method
qt.network.ssl: QSslSocket: cannot resolve TLSv1_2_client_method
qt.network.ssl: QSslSocket: cannot resolve TLSv1_1_server_method
qt.network.ssl: QSslSocket: cannot resolve TLSv1_2_server_method
qt.network.ssl: QSslSocket: cannot resolve SSL_select_next_proto
qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_set_next_proto_select_cb
qt.network.ssl: QSslSocket: cannot resolve SSL_get0_next_proto_negotiated
Qt 5.6.0 (x86_64-little_endian-llp64 shared (dynamic) release build; by MSVC 201
3) on &quot;windows&quot;
OS: Windows 8.1 [winnt version 6.3.9600]

Architecture: x86_64; features: SSE2 SSE3 SSSE3 SSE4.1 SSE4.2 AVX AVX2

Environment:
  QT5_BASE_DIR=&quot;C:\Qt\Qt5.6.0\5.6\msvc2013_64&quot;

Features: QT_NO_EXCEPTIONS

Library info:
  PrefixPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64
  DocumentationPath: C:\Qt\Qt5.6.0\Docs\Qt-5.6
  HeadersPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\include
  LibrariesPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\lib
  LibraryExecutablesPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin
  BinariesPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin
  PluginsPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\plugins
  ImportsPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\imports
  Qml2ImportsPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\qml
  ArchDataPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64
  DataPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64
  TranslationsPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\translations
  ExamplesPath: C:\Qt\Qt5.6.0\Examples\Qt-5.6
  TestsPath: C:\Qt\Qt5.6.0\5.6\msvc2013_64\tests
  SettingsPath:

Standard paths [*...* denote writable entry]:
  DesktopLocation: &quot;Desktop&quot; *C:\Users\bvittorino.PROD\Desktop*
  DocumentsLocation: &quot;Documents&quot; *C:\Users\bvittorino.PROD\Documents*
  FontsLocation: &quot;Fonts&quot; *C:\Windows\Fonts*
  ApplicationsLocation: &quot;Applications&quot; *C:\Users\bvittorino.PROD\AppData\Roaming\Microsoft\Windows\Start Menu\Programs*
  MusicLocation: &quot;Music&quot; *C:\Users\bvittorino.PROD\Music*
  MoviesLocation: &quot;Movies&quot; *C:\Users\bvittorino.PROD\Videos*
  PicturesLocation: &quot;Pictures&quot; *C:\Users\bvittorino.PROD\Pictures*
  TempLocation: &quot;Temporary Directory&quot; *C:\Users\bvittorino.PROD\AppData\Local\Temp*
  HomeLocation: &quot;Home&quot; *C:\Users\bvittorino.PROD*
  AppLocalDataLocation: &quot;Application Data&quot; *C:\Users\bvittorino.PROD\AppData\Local\QtProject\qtdiag* C:\ProgramData\QtProject\qtdiag C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data
  CacheLocation: &quot;Cache&quot; *C:\Users\bvittorino.PROD\AppData\Local\QtProject\qtdiag\cache*
  GenericDataLocation: &quot;Shared Data&quot; *C:\Users\bvittorino.PROD\AppData\Local* C:\ProgramData C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data
  RuntimeLocation: &quot;Runtime&quot; *C:\Users\bvittorino.PROD*
  ConfigLocation: &quot;Configuration&quot; *C:\Users\bvittorino.PROD\AppData\Local\QtProject\qtdiag* C:\ProgramData\QtProject\qtdiag C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data
  DownloadLocation: &quot;Download&quot; *C:\Users\bvittorino.PROD\Downloads*
  GenericCacheLocation: &quot;Shared Cache&quot; *C:\Users\bvittorino.PROD\AppData\Local\c
ache*
  GenericConfigLocation: &quot;Shared Configuration&quot; *C:\Users\bvittorino.PROD\AppData\Local* C:\ProgramData C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data
  AppDataLocation: &quot;Application Data&quot; *C:\Users\bvittorino.PROD\AppData\Roaming\QtProject\qtdiag* C:\ProgramData\QtProject\qtdiag C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data
  AppConfigLocation: &quot;Application Configuration&quot; *C:\Users\bvittorino.PROD\AppData\Local\QtProject\qtdiag* C:\ProgramData\QtProject\qtdiag C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin\data

File selectors (increasing order of precedence):
  it_IT windows winnt

Network:
  Using &quot;OpenSSL 1.0.0q 15 Jan 2015&quot;, version: 0x1000011f

Platform capabilities: ThreadedPixmaps OpenGL ThreadedOpenGL WindowMasks MultipleWindows ForeignWindows NonFullScreenWindows NativeWidgets WindowManagement RasterGLSurface AllGLFunctionsQueryable SwitchableWidgetComposition

Style hints:
  mouseDoubleClickInterval: 500
  mousePressAndHoldInterval: 800
  startDragDistance: 10
  startDragTime: 500
  startDragVelocity: 0
  keyboardInputInterval: 400
  keyboardAutoRepeatRate: 32
  cursorFlashTime: 1060
  showIsFullScreen: 0
  showIsMaximized: 0
  passwordMaskDelay: 0
  passwordMaskCharacter: U+25CF
  fontSmoothingGamma: 1.2
  useRtlExtensions: 0
  setFocusOnTouchRelease: 0
  tabFocusBehavior: Qt::TabFocusBehavior(TabFocusAllControls)
  singleClickActivation: 0

Additional style hints (QPlatformIntegration):
  ReplayMousePressOutsidePopup: 1

Theme:
  Available    : windows
  Styles       : WindowsVista,WindowsXP,Windows
  System font  : &quot;MS Shell Dlg 2&quot; 8
  Native file dialog

Fonts:
  General font : &quot;MS Shell Dlg 2&quot; 8
  Fixed font   : &quot;Courier New&quot; 9
  Title font   : &quot;MS Shell Dlg 2&quot; 8
  Smallest font: &quot;MS Shell Dlg 2&quot; 8

Screens: 2, High DPI scaling: inactive
# 0 &quot;\\.\DISPLAY1&quot; Depth: 32 Primary: yes
  Geometry: 1366x768+0+0 Available: 1366x728+0+0
  Virtual geometry: 1920x1848+-438+-1080 Available: 1920x1808+-438+-1080
  2 virtual siblings
  Physical size: 344x193 mm  Refresh: 60 Hz Power state: 0
  Physical DPI: 100.862,101.074 Logical DPI: 96,96 Subpixel_None
  DevicePixelRatio: 1 Pixel density: 1
  Primary orientation: 2 Orientation: 2 Native orientation: 0 OrientationUpdateMask: 0

# 1 &quot;\\.\DISPLAY2&quot; Depth: 32 Primary: no
  Geometry: 1920x1080+-438+-1080 Available: 1920x1040+-438+-1080
  Virtual geometry: 1920x1848+-438+-1080 Available: 1920x1808+-438+-1080
  2 virtual siblings
  Physical size: 477x268 mm  Refresh: 60 Hz Power state: 0
  Physical DPI: 102.239,102.358 Logical DPI: 96,96 Subpixel_None
  DevicePixelRatio: 1 Pixel density: 1
  Primary orientation: 2 Orientation: 2 Native orientation: 0 OrientationUpdateMask: 0

Dynamic GL LibGL Vendor: Intel
Renderer: Intel(R) HD Graphics 520
Version: 4.4.0 - Build 20.19.15.4285
Shading language: 4.40 - Build 20.19.15.4285
Format: Version: 4.4 Profile: 2 Swap behavior: 2 Buffer size (RGBA): 8,8,8,8 Depth buffer: 24 Stencil buffer: 8

GPU:
         Card name: Intel(R) HD Graphics 520
       Driver Name: igdumdim64.dll
    Driver Version: 20.19.15.4285
         Vendor ID: 0x8086
         Device ID: 0x1916
         SubSys ID: 0x504817AA
       Revision ID: 0x0007
C:\Qt\Qt5.6.0\5.6\msvc2013_64\bin&gt;</code></pre><p>ps:in another pc with only 64bit QT framework it works with 0 error and 83 warning</p></div><div id="comment-53111-info" class="comment-info"><span class="comment-age">(01 Jun '16, 07:11)</span> kenhero</div></div><span id="53112"></span><div id="comment-53112" class="comment"><div id="post-53112-score" class="comment-score">1</div><div class="comment-text"><p>That show that it is a 64 bit version of Qt, built using VS2013.</p><p>I'm not sure what to think of now, I'll have to look at your msbuild output a bit more.</p></div><div id="comment-53112-info" class="comment-info"><span class="comment-age">(01 Jun '16, 07:18)</span> grahamb ♦</div></div></div><div id="comment-tools-53075" class="comment-tools"><span class="comments-showing"> showing 5 of 17 </span> <a href="#" class="show-all-comments-link">show 12 more comments</a></div><div class="clear"></div><div id="comment-53075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

