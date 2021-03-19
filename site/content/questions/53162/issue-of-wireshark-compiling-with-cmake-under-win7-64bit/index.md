+++
type = "question"
title = "issue of wireshark compiling with Cmake under WIN7 64BIT"
description = '''I tried to compile wireshark source code with CMAKE,however failed.And I could not figure out the cause.Any suggestions from you are appreciated,thanks a lot. environment setting is as below:----&amp;gt; call &quot;C:&#92;Program Files (x86)&#92;Microsoft Visual Studio 12.0&#92;VC&#92;vcvarsall.bat&quot; x86_amd64 set WIRESHARK_...'''
date = "2016-06-03T00:29:00Z"
lastmod = "2016-10-31T07:03:00Z"
weight = 53162
keywords = [ "compile", "isssue", "cmake" ]
aliases = [ "/questions/53162" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [issue of wireshark compiling with Cmake under WIN7 64BIT](/questions/53162/issue-of-wireshark-compiling-with-cmake-under-win7-64bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53162-score" class="post-score" title="current number of votes">0</div><span id="post-53162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to compile wireshark source code with CMAKE,however failed.And I could not figure out the cause.Any suggestions from you are appreciated,thanks a lot.</p><p><strong><em>environment setting is as below:----&gt;</em></strong></p><pre><code>call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; x86_amd64
set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\SecVersion\wireshark-master
set WIRESHARK_CYGWIN_INSTALL_PATH=E:\Software\Cygwin\bin
set WIRESHARK_TARGET_PLATFORM=win64
set QT5_BASE_DIR=E:\Software\QT\5.6\msvc2013_64
set  VISUALSTUDIOVERSION=12.0
set MSVC_VARIANT=MSVC2013EE
e:
cd  E:\Wireshark_Plugin\SecVersion\wsbuild
cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\wireshark-master
pause</code></pre><p><strong><em>COMPILE result is as below------&gt;</em></strong></p><pre><code>-- Found python module asn2wrs: E:\Wireshark_Plugin\SecVersion\wireshark\tools\asn2wrs.py
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
CMake Error at CMakeLists.txt:766 (add_subdirectory):
  add_subdirectory given source &quot;
  E:/Wireshark_Plugin/SecVersion/wireshark/Wireshark-win64-libs/zlib-1.2.8-ws&quot; which is not an existing directory.
CMake Error at CMakeLists.txt:771 (set_target_properties): set_target_properties Can not find target to add properties to: zlib
CMake Error at CMakeLists.txt:773 (set_target_properties): set_target_properties Can not find target to add properties to: zlibstatic
-- Packagelist: AIRPCAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Could NOT find AIRPCAP (missing:  AIRPCAP_INCLUDE_DIR AIRPCAP_LIBRARY)
-- AIRPCAP NOT FOUND
-- Could NOT find CARES (missing:  CARES_LIBRARY CARES_INCLUDE_DIR)
-- CARES NOT FOUND
-- Could NOT find GCRYPT (missing:  GCRYPT_LIBRARY GCRYPT_INCLUDE_DIR) (Required is at least version &quot;1.4.2&quot;)
-- GCRYPT NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;geoip&#39;
-- Could NOT find GEOIP (missing:  GEOIP_LIBRARY GEOIP_INCLUDE_DIR)
-- GEOIP NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
CMake Error at E:/Software/CMake/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:148 (message):
  Could NOT find GLIB2 (missing: GLIB2_LIBRARY GLIB2_MAIN_INCLUDE_DIR) 
Call Stack (most recent call first):
  E:/Software/CMake/share/cmake-3.5/Modules/FindPackageHandleStandardArgs.cmake:388 (_FPHSA_FAILURE_MESSAGE)
  cmake/modules/FindGLIB2.cmake:90 (find_package_handle_standard_args)
  CMakeLists.txt:835 (find_package)

-- Configuring incomplete, errors occurred!</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-isssue" rel="tag" title="see questions tagged &#39;isssue&#39;">isssue</span> <span class="post-tag tag-link-cmake" rel="tag" title="see questions tagged &#39;cmake&#39;">cmake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/1445b0c2e6369c9b39c7802df15a2299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Water&#39;s gravatar image" /><p><span>Water</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Water has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jun '16, 01:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53162" class="comments-container"></div><div id="comment-tools-53162" class="comment-tools"></div><div class="clear"></div><div id="comment-53162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53166"></span>

<div id="answer-container-53166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53166-score" class="post-score" title="current number of votes">1</div><span id="post-53166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This two lines from the setup shouldn't be required:</p><pre><code>set  VISUALSTUDIOVERSION=12.0
set MSVC_VARIANT=MSVC2013EE</code></pre><p>Cmake is having difficulties with your build environment, there are at least 2 issues shown, one with zlib and one with glib.</p><p>For zlib, can you confirm that <code>E:\Wireshark_Plugin\SecVersion\wireshark\Wireshark-win64-libs</code> contains the file <code>zlib-1.2.8-ws.zip</code> and the directory <code>zlib-1.2.8-ws</code>?</p><p>For glib can you confirm the same directory contain the file <code>gtk+-bundle_2.24.23-3.39_win64ws.zip</code> and the directory <code>gtk2</code>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53166" class="comments-container"><span id="56860"></span><div id="comment-56860" class="comment"><div id="post-56860-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> I have the exact same Problem. I can congfirm that, zlib-1.2.8-ws.zip,zlib-1.2.8-ws and gtk+-bundle_2.24.23-3.39_win64ws.zip and the directory gtk2 are available in the indicated Directory. What could be the solution now?</p></div><div id="comment-56860-info" class="comment-info"><span class="comment-age">(31 Oct '16, 04:57)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="56861"></span><div id="comment-56861" class="comment"><div id="post-56861-score" class="comment-score">1</div><div class="comment-text"><p>The OP has a different directory layout from that recommended in the Developers Guide (and as used by myself), it's possible that may be causing the issues.</p><p>The recommended layout (you can modify the drive and top-level dir, but keep everything the same below that) is:</p><pre><code>C:\Development - Top-level dir
C:\Development\wireshark - source code, preferably from a Git clone.
C:\Development\wsbuild32 - 32 bit build directory
C:\Development\wsbuild64 - 64 bit build directory</code></pre><p>and after running the CMake generation step, the third party libraries will be installed in:</p><pre><code>C:\Development\wireshark-win32-libs
C:\Development\wireshark-win64-libs</code></pre><p>and the environment variable <code>WIRESHARK_BASE_DIR</code> is set to <code>C:\Development</code> or as appropriate for your top-level directory</p></div><div id="comment-56861-info" class="comment-info"><span class="comment-age">(31 Oct '16, 05:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56863"></span><div id="comment-56863" class="comment"><div id="post-56863-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> I have the exact same Directory Setup. I had 100% success with 64bit. but for some weird reason having issues with 32bit. "C:\Development\wireshark-win32-libs" has been generated and all the files that CMake is showing missing is there....I have no clue what to do now! :/</p></div><div id="comment-56863-info" class="comment-info"><span class="comment-age">(31 Oct '16, 06:17)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="56864"></span><div id="comment-56864" class="comment"><div id="post-56864-score" class="comment-score"></div><div class="comment-text"><p>I think you need to start your own question posting the output of the CMake Generation step along with the environment variables you're using so we can help specifically there.</p></div><div id="comment-56864-info" class="comment-info"><span class="comment-age">(31 Oct '16, 06:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56865"></span><div id="comment-56865" class="comment"><div id="post-56865-score" class="comment-score"></div><div class="comment-text"><p>The issue is solved. I have restarted the Computer and started the whole process and it works just fine :D Thanks a lot for your Support and quick answers. <span>@grahamb</span></p></div><div id="comment-56865-info" class="comment-info"><span class="comment-age">(31 Oct '16, 07:03)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-53166" class="comment-tools"></div><div class="clear"></div><div id="comment-53166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

