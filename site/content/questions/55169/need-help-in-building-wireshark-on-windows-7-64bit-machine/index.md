+++
type = "question"
title = "Need help in building wireshark on windows 7, 64bit machine"
description = '''Hi, I&#x27;m awfully stuck for two days trying to build legacy code(1.8.7) on windows 7, 64bit machine. I followed the process as below:  https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html But it fails during CMake. My understanding from the below log is that required libraries(gmodule-2....'''
date = "2016-08-29T09:05:00Z"
lastmod = "2016-08-29T10:25:00Z"
weight = 55169
keywords = [ "1.8", "windows7", "cmake" ]
aliases = [ "/questions/55169" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Need help in building wireshark on windows 7, 64bit machine](/questions/55169/need-help-in-building-wireshark-on-windows-7-64bit-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55169-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm awfully stuck for two days trying to build legacy code(1.8.7) on windows 7, 64bit machine.</p><p>I followed the process as below: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</a></p><p>But it fails during CMake.</p><p>My understanding from the below log is that required libraries(gmodule-2.0, gthread-2.0) are not found. These libraries are supposed to be in folder 'wireshark-win64-libs' But this folder is not present in my source code.</p><p>I'm totally clueless. Request for some pointers so that I can progress ahead</p><pre><code>C:\Development\wsbuild64&gt;cmake -DENABLE_CHM_GUIDES=on -G &quot;Visual Studio 12 Win64&quot; ..\wireshark
-- The C compiler identification is MSVC 18.0.31101.0
-- The CXX compiler identification is MSVC 18.0.31101.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/bin/x86_amd64/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/bin/x86_amd64/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/bin/x86_amd64/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/bin/x86_amd64/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- V: 1.8.7, MaV: 1, MiV: 8, PL: 7, EV: .
-- Performing Test WS_C_FLAG_VALID0
-- Performing Test WS_C_FLAG_VALID0 - Failed
-- Performing Test WS_C_FLAG_VALID1
-- Performing Test WS_C_FLAG_VALID1 - Success
-- Performing Test WS_C_FLAG_VALID2
-- Performing Test WS_C_FLAG_VALID2 - Failed
-- Performing Test WS_C_FLAG_VALID3
-- Performing Test WS_C_FLAG_VALID3 - Failed
-- Performing Test WS_C_FLAG_VALID4
-- Performing Test WS_C_FLAG_VALID4 - Failed
-- Performing Test WS_C_FLAG_VALID5
-- Performing Test WS_C_FLAG_VALID5 - Failed
-- Performing Test WS_C_FLAG_VALID6
-- Performing Test WS_C_FLAG_VALID6 - Failed
-- Performing Test WS_C_FLAG_VALID7
-- Performing Test WS_C_FLAG_VALID7 - Failed
-- Performing Test WS_C_FLAG_VALID8
-- Performing Test WS_C_FLAG_VALID8 - Failed
-- Performing Test WS_C_FLAG_VALID9
-- Performing Test WS_C_FLAG_VALID9 - Failed
-- Performing Test WS_C_FLAG_VALID10
-- Performing Test WS_C_FLAG_VALID10 - Failed
-- Performing Test WS_C_FLAG_VALID11
-- Performing Test WS_C_FLAG_VALID11 - Failed
-- Performing Test WS_C_FLAG_VALID12
-- Performing Test WS_C_FLAG_VALID12 - Failed
statuscheck linker flag - test linker flags: -Wl,--as-needed
-- Performing Test WS_LD_FLAG_VALID0
-- Performing Test WS_LD_FLAG_VALID0 - Failed
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
GLIB2_FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- Could NOT find GMODULE2
GMODULE2_FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE)
-- Checking for one of the modules &#39;gthread-2.0&#39;
-- Could NOT find GTHREAD2
GTHREAD2_FOUND
-- Could NOT find M (missing:  M_LIBRARY)
M_FOUND
-- Found LEX: C:/cygwin64/bin/flex.exe
LEX_FOUND
-- LEX includes:
-- LEX libs:
-- Found YACC: C:/cygwin64/bin/bison.exe
YACC_FOUND
-- YACC includes:
-- YACC libs:
-- Found Perl: C:/cygwin64/bin/perl.exe (found version &quot;5.22.2&quot;)
Perl_FOUND
-- Perl includes:
-- Perl libs:
-- Found SH: C:/Program Files/Git/bin/sh.exe
SH_FOUND
-- SH includes:
-- SH libs:
-- Found PythonInterp: C:/ProgramData/chocolatey/bin/python.exe (found version &quot;3.5.1&quot;)
PythonInterp_FOUND
-- PythonInterp includes:
-- PythonInterp libs:
-- Could NOT find HtmlViewer (missing:  HTML_VIEWER_EXECUTABLE)
HtmlViewer_FOUND
FATAL Pcap include dirs cannot be found
FATALPcap library cannot be found
-- Looking for pcap_version
-- Looking for pcap_version - not found
-- Looking for pcap_open_dead
-- Looking for pcap_open_dead - not found
-- Looking for pcap_freecode
-- Looking for pcap_freecode - not found
-- Looking for pcap_breakloop
-- Looking for pcap_breakloop - not found
-- Looking for pcap_create
-- Looking for pcap_create - not found
-- Looking for pcap_datalink_name_to_val
-- Looking for pcap_datalink_name_to_val - not found
-- Looking for pcap_datalink_val_to_description
-- Looking for pcap_datalink_val_to_description - not found
-- Looking for pcap_datalink_val_to_name
-- Looking for pcap_datalink_val_to_name - not found
-- Looking for pcap_findalldevs
-- Looking for pcap_findalldevs - not found
-- Looking for pcap_free_datalinks
-- Looking for pcap_free_datalinks - not found
-- Looking for pcap_get_selectable_fd
-- Looking for pcap_get_selectable_fd - not found
-- Looking for pcap_lib_version
-- Looking for pcap_lib_version - not found
-- Looking for pcap_list_datalinks
-- Looking for pcap_list_datalinks - not found
-- Looking for pcap_set_datalink
-- Looking for pcap_set_datalink - not found
-- Looking for pcap_open
-- Looking for pcap_open - not found
-- Looking for pcap_findalldevs_ex
-- Looking for pcap_findalldevs_ex - not found
-- Looking for pcap_createsrcstr
-- Looking for pcap_createsrcstr - not found
-- Could NOT find PCAP (missing:  PCAP_INCLUDE_DIRS PCAP_LIBRARIES)
PCAP_FOUND
GTK2_FOUND
-- Could NOT find SMI (missing:  SMI_LIBRARY SMI_INCLUDE_DIR)
SMI_FOUND
-- Could NOT find GCRYPT (missing:  GCRYPT_LIBRARY GCRYPT_INCLUDE_DIR)
GCRYPT_FOUND
-- Could NOT find GNUTLS (missing:  GNUTLS_LIBRARY GNUTLS_INCLUDE_DIR)
GNUTLS_FOUND
-- Could NOT find KERBEROS (missing:  KERBEROS_LIBRARY KERBEROS_INCLUDE_DIR)
KERBEROS_FOUND
-- Could NOT find PORTAUDIO (missing:  PORTAUDIO_LIBRARY PORTAUDIO_INCLUDE_DIR)
PORTAUDIO_FOUND
-- Could NOT find CARES (missing:  CARES_LIBRARY CARES_INCLUDE_DIR)
CARES_FOUND
-- Looking for inflatePrime
-- Looking for inflatePrime - not found
-- Could NOT find ZLIB (missing:  ZLIB_LIBRARY ZLIB_INCLUDE_DIR)
ZLIB_FOUND
-- Could NOT find LUA (missing:  LUA_LIBRARY LUA_INCLUDE_DIR)
LUA_FOUND
-- Could NOT find GEOIP (missing:  GEOIP_LIBRARY GEOIP_INCLUDE_DIR)
GEOIP_FOUND
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR)
CAP_FOUND
-- Could NOT find YAPP (missing:  YAPP_EXECUTABLE)
YAPP_FOUND
-- Found POD: C:/cygwin64/bin/pod2man
POD_FOUND
-- POD includes:
-- POD libs:
-- Looking for arpa/inet.h
-- Looking for arpa/inet.h - not found
-- Looking for arpa/nameser.h
-- Looking for arpa/nameser.h - not found
-- Looking for direct.h
-- Looking for direct.h - found
-- Looking for dirent.h
-- Looking for dirent.h - not found
-- Looking for dlfcn.h
-- Looking for dlfcn.h - not found
-- Looking for fcntl.h
-- Looking for fcntl.h - found
-- Looking for grp.h
-- Looking for grp.h - not found
-- Looking for g_ascii_strtoull.h
-- Looking for g_ascii_strtoull.h - not found
-- Looking for inet/aton.h
-- Looking for inet/aton.h - not found
-- Looking for inttypes.h
-- Looking for inttypes.h - found
-- Looking for lauxlib.h
-- Looking for lauxlib.h - not found
-- Looking for memory.h
-- Looking for memory.h - found
-- Looking for netinet/in.h
-- Looking for netinet/in.h - not found
-- Looking for netdb.h
-- Looking for netdb.h - not found
-- Looking for Ntddndis.h
-- Looking for Ntddndis.h - not found
-- Looking for portaudio.h
-- Looking for portaudio.h - not found
-- Looking for pwd.h
-- Looking for pwd.h - not found
-- Looking for stdarg.h
-- Looking for stdarg.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stdlib.h
-- Looking for stdlib.h - found
-- Looking for strings.h
-- Looking for strings.h - not found
-- Looking for string.h
-- Looking for string.h - found
-- Looking for sys/ioctl.h
-- Looking for sys/ioctl.h - not found
-- Looking for sys/param.h
-- Looking for sys/param.h - not found
-- Looking for sys/socket.h</code></pre><p>Finally below error:</p><pre><code>CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
GMODULE2_LIBRARIES (ADVANCED)
    linked by target &quot;wiretap&quot; in directory C:/Development/wireshark/wiretap
PCAP_LIBRARY
    linked by target &quot;tshark&quot; in directory C:/Development/wireshark
    linked by target &quot;dftest&quot; in directory C:/Development/wireshark
    linked by target &quot;randpkt&quot; in directory C:/Development/wireshark
    linked by target &quot;epan&quot; in directory C:/Development/wireshark/epan

-- Configuring incomplete, errors occurred!
See also &quot;C:/Development/wsbuild64/CMakeFiles/CMakeOutput.log&quot;.
See also &quot;C:/Development/wsbuild64/CMakeFiles/CMakeError.log&quot;.</code></pre></div><div id="question-tags" class="tags-container tags">1.8 windows7 cmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '16, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/8f33b41ef74fe88317bf5384fc63d4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="satishp&#39;s gravatar image" /><p>satishp<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="satishp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '16, 10:22</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55169" class="comments-container"></div><div id="comment-tools-55169" class="comment-tools"></div><div class="clear"></div><div id="comment-55169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55171"></span>

<div id="answer-container-55171" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55171-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using <del>CMake doesn't work</del> isn't used for Windows in versions &lt; 2.0.</p><p>You have to build using NMake, there's a copy of the older Developers Guide for 1.11 <a href="https://www.wireshark.org/~gerald/wsdg_html_2014_01/">here</a> that may be useful.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '16, 01:28</p></div></div><div id="comments-container-55171" class="comments-container"><span id="55188"></span><div id="comment-55188" class="comment"><div id="post-55188-score" class="comment-score"></div><div class="comment-text"><p>Thanks graham for your quick response. I now switched to nmake but ran into different problems.</p><p>My device is Windows 7, 64 bit using Visual studio 10 express</p><p>I followed steps as in below link <a href="https://www.wireshark.org/~gerald/wsdg_html_2014_01/ChSetupWin32.html">https://www.wireshark.org/~gerald/wsdg_html_2014_01/ChSetupWin32.html</a></p><pre><code>..\..\config.nmake(1035) : fatal error U1050: Can&#39;t find C:\wireshark-win32-libs-1.8\vcredist_x86.exe. Have you downloaded it from Microsoft? See the developer&#39;s guide section &quot;C-Runtime &quot;Redistributa</code></pre><p>As per my understanding it should look in C:\wireshark-win64-libs-1.8. Can you please give me pointers where I might have gone wrong</p><p>Below are the tools and they seem to be fine:</p><pre><code>    cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/amd64/cl
    link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/amd64/link
    nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/amd64/nmake
    bash: /usr/bin/bash
    bison: /usr/bin/bison
    flex: /usr/bin/flex
    env: /usr/bin/env
    grep: /usr/bin/grep
    /usr/bin/find: /usr/bin/find
    peflags: /usr/bin/peflags
    perl: /usr/bin/perl
    sed: /usr/bin/sed
    unzip: /usr/bin/unzip
    wget: /usr/bin/wget</code></pre></div><div id="comment-55188-info" class="comment-info"><span class="comment-age">(29 Aug '16, 23:22)</span> satishp</div></div><span id="55190"></span><div id="comment-55190" class="comment"><div id="post-55190-score" class="comment-score"></div><div class="comment-text"><p>For Express Editions of VS you must manually download the vc redist files and place them in the appropriate locations. See Section <a href="https://www.wireshark.org/~gerald/wsdg_html_2014_01/ChSetupWin32.html#idp412326516">2.2.13</a> of the Dev Guide.</p></div><div id="comment-55190-info" class="comment-info"><span class="comment-age">(30 Aug '16, 01:27)</span> grahamb ♦</div></div><span id="55277"></span><div id="comment-55277" class="comment"><div id="post-55277-score" class="comment-score"></div><div class="comment-text"><p>Thanks graham for your help, I could fix all the issues</p></div><div id="comment-55277-info" class="comment-info"><span class="comment-age">(01 Sep '16, 20:12)</span> satishp</div></div></div><div id="comment-tools-55171" class="comment-tools"></div><div class="clear"></div><div id="comment-55171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

