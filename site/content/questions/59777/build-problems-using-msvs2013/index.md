+++
type = "question"
title = "Build Problems using MSVS2013"
description = '''I am experiencing unexpected errors on compiling and building wireshark-2.2.4.tar.bz2 following the instructions in 2.2. Win32_64 Step-by-Step Guide.htm, using Microsoft Visual Studio 2013 under Windows 7 64 bit OS. All the environment variables appear to be fine, the various components (Qt, Python,...'''
date = "2017-03-01T12:00:00Z"
lastmod = "2017-03-02T00:14:00Z"
weight = 59777
keywords = [ "msvs2013" ]
aliases = [ "/questions/59777" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Build Problems using MSVS2013](/questions/59777/build-problems-using-msvs2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59777-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am experiencing unexpected errors on compiling and building wireshark-2.2.4.tar.bz2 following the instructions in 2.2. Win32_64 Step-by-Step Guide.htm, using Microsoft Visual Studio 2013 under Windows 7 64 bit OS. All the environment variables appear to be fine, the various components (Qt, Python, Cygwin etc) are correctly found during the build and I am closely following the guide, with only the following exceptions:</p><p>PER GUIDE<br />
</p><p>Base directory for build = C:\Development<br />
</p><p>Subdirectory of base containing source files = C:\Development\wireshark<br />
</p><p>PER MY IMPLEMENTATION</p><p>Base directory for build = <code>F:\Wireshark_Build</code></p><p>Subdirectory of base containing source files = <code>F:\Wireshark_Build\wireshark_development</code></p><p>I'm not using Git.</p><p>** The original question as posted had lots of expected errors from the CMake test compilation steps for features and compiler\linker flags not present on windows. superfluous CMakeError log removed **</p><p>The exact CMake generation command which I used is:</p><pre><code>cmake -DENABLE_CHM_GUIDES=on -G&quot;Visual Studio 12 Win64&quot; ..\Wireshark_development&gt;&gt; cmakegen.txt 2&gt;&amp;1</code></pre><p>The contents of the cmakegen.txt file is pasted below:</p><pre><code>-- The C compiler identification is MSVC 18.0.30723.0
-- The CXX compiler identification is MSVC 18.0.30723.0
-- Check for working C compiler: F:/Visual Studio 2013/VC/bin/x86_amd64/cl.exe
-- Check for working C compiler: F:/Visual Studio 2013/VC/bin/x86_amd64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: F:/Visual Studio 2013/VC/bin/x86_amd64/cl.exe
-- Check for working CXX compiler: F:/Visual Studio 2013/VC/bin/x86_amd64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Generating build using CMake 3.7.2
-- Found POWERSHELL: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe  
-- Building for win64 using Visual Studio 12 2013 Win64
Working in F:\Wireshark_Build\Wireshark-win64-libs-2.2

Tag 2016-12-12-2.2 found. Skipping.

-- No custom file found in F:/Wireshark_Build/wireshark_development
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /DNDEBUG
-- V: 2.2.4-OriginalVersion, MaV: 2, MiV: 2, PL: 4, EV: -OriginalVersion.
-- Found PythonInterp: F:/Python/python.exe (found version &quot;3.5.3&quot;) 
-- Found python module asn2wrs: F:\Wireshark_Build\wireshark_development\tools\asn2wrs.py
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
-- Found AIRPCAP: F:/Wireshark_Build/Wireshark-win64-libs-2.2/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include  
-- AIRPCAP FOUND
-- AIRPCAP includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/include
-- AIRPCAP libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/AirPcap_Devpack_4_1_0_1622/Airpcap_Devpack/lib/airpcap.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Found CARES: F:/Wireshark_Build/Wireshark-win64-libs-2.2/c-ares-1.12.0-win64ws/lib/libcares-2.lib  
-- CARES FOUND
-- CARES includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/c-ares-1.12.0-win64ws/include
-- CARES libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/c-ares-1.12.0-win64ws/lib/libcares-2.lib
-- Found GCRYPT: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib (found suitable version &quot;1.6.2&quot;, minimum required is &quot;1.4.2&quot;) 
-- GCRYPT FOUND
-- GCRYPT includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/include
-- GCRYPT libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/bin/libgcrypt-20.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/bin/libgpg-error6-0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- Found GEOIP: F:/Wireshark_Build/Wireshark-win64-libs-2.2/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib  
-- Looking for GeoIP_country_name_by_ipnum_v6
-- Looking for GeoIP_country_name_by_ipnum_v6 - found
-- GEOIP FOUND
-- GEOIP includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/GeoIP-1.6.6-win64ws/include
-- GEOIP libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/GeoIP-1.6.6-win64ws/lib/libGeoIP-1.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Found GLIB2: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0.lib  
-- GLIB2 FOUND
-- GLIB2 includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/glib-2.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0/include
-- GLIB2 libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- Found GMODULE2: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gmodule-2.0.lib  
-- GMODULE2 FOUND
-- GMODULE2 includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/glib-2.0
-- GMODULE2 libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gmodule-2.0.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gnutls&#39;
-- Found GNUTLS: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib (found suitable version &quot;3.2.15&quot;, minimum required is &quot;2.12.0&quot;) 
-- GNUTLS FOUND
-- GNUTLS includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/include
-- GNUTLS libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gnutls-3.2.15-2.9-win64ws/bin/libgnutls-28.lib
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- Found GTHREAD2: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0.lib  
-- GTHREAD2 FOUND
-- GTHREAD2 includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/glib-2.0/glib
-- GTHREAD2 libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0.lib
-- Found GTK2_GTK: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gtk-win32-2.0.lib  
-- GTK2 FOUND
-- GTK2 includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/gtk-2.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/freetype2;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/glib-2.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0/include;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/atk-1.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/gdk-pixbuf-2.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/cairo;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/include/pango-1.0;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gtk-2.0/include
-- GTK2 libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/glib-2.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gobject-2.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/atk-1.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gmodule-2.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gdk_pixbuf-2.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/cairo.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/pango-1.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/pangocairo-1.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gdk-win32-2.0.lib;F:/Wireshark_Build/Wireshark-win64-libs-2.2/gtk2/lib/gtk-win32-2.0.lib
-- Could NOT find Gettext (missing:  GETTEXT_MSGMERGE_EXECUTABLE GETTEXT_MSGFMT_EXECUTABLE) 
-- GETTEXT NOT FOUND
-- Could NOT find Git (missing:  GIT_EXECUTABLE) 
-- Git NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;krb5;mit-krb5;heimdal-krb5&#39;
-- Found KERBEROS: F:/Wireshark_Build/Wireshark-win64-libs-2.2/kfw-3-2-2-x64-ws/lib/krb5_64.lib  
-- Looking for heimdal_version
-- Looking for heimdal_version - not found
-- KERBEROS FOUND
-- KERBEROS includes: F:/Wireshark_Build/Wireshark-win64-libs-2.2/kfw-3-2-2-x64-ws/include
-- KERBEROS libs: F:/Wireshark_Build/Wireshark-win64-libs-2.2/kfw-3-2-2-x64-ws/lib/krb5_64.lib
CMake Error at F:/CMake/share/cmake-3.7/Modules/FindPackageHandleStandardArgs.cmake:138 (message):
  Could NOT find LEX (missing: LEX_EXECUTABLE)
Call Stack (most recent call first):
  F:/CMake/share/cmake-3.7/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  cmake/modules/FindLEX.cmake:23 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  CMakeLists.txt:828 (find_package)

-- Configuring incomplete, errors occurred!
See also &quot;F:/Wireshark_Build/wsbuild64/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;F:/Wireshark_Build/wsbuild64/CMakeFiles/CMakeError.log&quot;.</code></pre></div><div id="question-tags" class="tags-container tags">msvs2013</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '17, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/469e7fba59f37c655afa16ea559bee97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Utnapishtim&#39;s gravatar image" /><p>Utnapishtim<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Utnapishtim has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '17, 10:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></br></p></div></div><div id="comments-container-59777" class="comments-container"></div><div id="comment-tools-59777" class="comment-tools"></div><div class="clear"></div><div id="comment-59777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59797"></span>

<div id="answer-container-59797" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59797-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>** This was the original answer to the question about the expected CMake test compilation errors **</p><p>I was once told the CMake "way" was to not clutter the CMakeLists.txt files with lots of conditionals based on the build OS, just to let CMake sort it out. This leads to (IMHO) useless tests for compiler and linker flags and also searches for libraries that will never be found on some build targets.</p><p>Regardless of that gripe, the failures the OP posts are expected as these are the test of linker flags and unavailable libraries and functions that fail on Windows.</p><p>What's missing from the wall of text is the output of the CMake generation step. Please delete the <code>CMakeCache.txt</code> file from the build directory and run the CMake generation command being used, redirecting output to a text file and then post the contents of the text file, e.g.</p><pre><code>cmake ... 2&amp;&gt;1 &gt; cmakegen.txt</code></pre><p>Please also post the exact CMake generation command being used.</p><p>** This is the amended answer after the OP posted the required CMake generation step output **</p><p>The configure step shows the issue:</p><blockquote>CMake Error at F:/CMake/share/cmake-3.7/Modules/FindPackageHandleStandardArgs.cmake:138 (message): Could NOT find LEX (missing: LEX_EXECUTABLE)</blockquote><p>You appear to have missed the installation of flex\bison as noted in the Developers Guide section <a href="https://www.wireshark.org/docs/wsdg_html/#ChSetupCygwin">Install Cygwin</a>. Currently the recommended install is winflexbison via chocolatey.</p><p>I have just noted however, that chocolatey now has two separate packages for winflexbison; winflexbison and winflexbison3. I'm successfully using the newer winflexbison3 but the Dev Guide still uses the older one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '17, 00:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '17, 11:01</p></div></div><div id="comments-container-59797" class="comments-container"><span id="59801"></span><div id="comment-59801" class="comment"><div id="post-59801-score" class="comment-score"></div><div class="comment-text"><p>Glad to hear it's fixed. I see no need to pass the full path for the solution. It's in the directory you should be starting the build from so msbuild will find it there.</p><p>This question (and comments) has become a gigantic wall of text that's mostly irrelevant and unhelpful to others, so with your permission I'd like to reorganise it to just show the CMake generation log in the question and change my answer to point out the flex\bison issue and then your comment to that answer stating that it worked.</p></div><div id="comment-59801-info" class="comment-info"><span class="comment-age">(02 Mar '17, 04:40)</span> grahamb ♦</div></div><span id="59848"></span><div id="comment-59848" class="comment"><div id="post-59848-score" class="comment-score"></div><div class="comment-text"><p>For what it's worth:</p><pre><code>statuscheck linker flag - test linker flags: -Wl,--as-needed
-- Performing Test WS_LD_FLAG_VALID0
-- Performing Test WS_LD_FLAG_VALID0 - Failed
statuscheck linker flag - test linker flags: -pie
-- Performing Test WS_LD_FLAG_VALID1
-- Performing Test WS_LD_FLAG_VALID1 - Failed</code></pre><p>seems to indicate that CMake found that <code>-Wl,--as-needed</code> and <code>-pie</code> were found <em>not</em> to have worked, so it should <em>not</em> have included them as linker flags.</p></div><div id="comment-59848-info" class="comment-info"><span class="comment-age">(04 Mar '17, 10:58)</span> Guy Harris ♦♦</div></div><span id="59849"></span><div id="comment-59849" class="comment"><div id="post-59849-score" class="comment-score"></div><div class="comment-text"><p>Gah, I've managed to delete the comment from @Utnapishtim showing that the build completed when trying to clean up the massive wall of text.</p></div><div id="comment-59849-info" class="comment-info"><span class="comment-age">(04 Mar '17, 11:04)</span> grahamb ♦</div></div><span id="59884"></span><div id="comment-59884" class="comment"><div id="post-59884-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/WSBuild_Screendump_1OI2atN.gif" alt="alt text" /></p><p><em>Gah, I've managed to delete the comment from @Utnapishtim showing that the build completed when trying to clean up the massive wall of text.</em></p><p>After some rummaging around, I have managed to find &amp; have reloaded the Build Completed Screendump, which @grahamb threw out with the bathwater.</p></div><div id="comment-59884-info" class="comment-info"><span class="comment-age">(07 Mar '17, 02:56)</span> Utnapishtim</div></div><span id="59885"></span><div id="comment-59885" class="comment"><div id="post-59885-score" class="comment-score"></div><div class="comment-text"><p>We now seem to have a reasonably clear question and answer that will hopefully help others.</p><p>@Utnapishtim, if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-59885-info" class="comment-info"><span class="comment-age">(07 Mar '17, 03:17)</span> grahamb ♦</div></div></div><div id="comment-tools-59797" class="comment-tools"></div><div class="clear"></div><div id="comment-59797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59791"></span>

<div id="answer-container-59791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm surprised this works <em>at all</em> on Windows, but apparently it does, because our Windows buildbot works.</p><p>We appear to make <code>-Wl,--as-needed</code> as a linker flag on <em>all</em> platforms, even though <code>--as-needed</code> is a flag specific to the GNU linker. <em>Perhaps</em> some versions of CMake are clever enough to know that and to use it only with the GNU linker - CMake builds work on my machine, but it's running macOS and uses Apple's linker.</p><p>Please file a bug on this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>; I'll look at it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-59791" class="comments-container"><span id="59792"></span><div id="comment-59792" class="comment"><div id="post-59792-score" class="comment-score"></div><div class="comment-text"><p>OK, the CMake files try to check each of the flags to see whether it works with the linker. On macOS, it detects that <code>-Wl,--as-needed</code> doesn't work and removes it from the flags, and it may do so on our Windows buildbot, but perhaps that check isn't working on your machine.</p></div><div id="comment-59792-info" class="comment-info"><span class="comment-age">(01 Mar '17, 16:20)</span> Guy Harris ♦♦</div></div><span id="59793"></span><div id="comment-59793" class="comment"><div id="post-59793-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy. Its late here in the UK, and I shall fight it out with CMake tomorrow. Would you be so kind as to tell me which file to edit in order to remove the -Wl flag ?</p></div><div id="comment-59793-info" class="comment-info"><span class="comment-age">(01 Mar '17, 16:31)</span> Utnapishtim</div></div><span id="59796"></span><div id="comment-59796" class="comment"><div id="post-59796-score" class="comment-score"></div><div class="comment-text"><p>If you just want to hack it so that it builds, remove</p><pre><code>set(WIRESHARK_LD_FLAGS
    -Wl,--as-needed
    # -flto
    # -fwhopr
    # -fwhole-program
)
# CMAKE_POSITION_INDEPENDENT_CODE is only supported starting with CMake
# 2.8.9. Do not add -pie automatically for older versions.
#
# XXX - are there other compilers that don&#39;t support -pie?  It&#39;s
# not as if the only platforms we support are Windows and Linux....
#
if(NOT CMAKE_VERSION VERSION_LESS &quot;2.8.9&quot;)
    set(WIRESHARK_LD_FLAGS ${WIRESHARK_LD_FLAGS}
        -pie
    )
endif()</code></pre><p>from <code>CMakeLists.txt</code>.</p></div><div id="comment-59796-info" class="comment-info"><span class="comment-age">(01 Mar '17, 18:25)</span> Guy Harris ♦♦</div></div><span id="59847"></span><div id="comment-59847" class="comment"><div id="post-59847-score" class="comment-score"></div><div class="comment-text"><p>This answer and the subsequent comments now don't make much sense after I've reorganised the question to remove the massive and mostly irrelevant wall of text about expected CMake errors when testing compiler\linker flags and checking for libraries and functions.</p><p>This was done to actually make the question and the subsequent answer useful for others.</p></div><div id="comment-59847-info" class="comment-info"><span class="comment-age">(04 Mar '17, 10:55)</span> grahamb ♦</div></div></div><div id="comment-tools-59791" class="comment-tools"></div><div class="clear"></div><div id="comment-59791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

