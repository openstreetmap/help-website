+++
type = "question"
title = "How to cross compile Wireshark x64 on an x86 Windows machine"
description = '''I am using rev 37663 of Wireshark (1.7.0) and VS 2008 on Windows XP x86 and I would like to compile a 64-bit version of Wireshark. I have followed all the instructions detailed in   http://wiki.wireshark.org/Development/Win64 Here&#x27;s what I&#x27;ve done:  prepared cmd.exe by running:&quot;C:&#92;Program Files&#92;Micr...'''
date = "2012-02-13T18:47:00Z"
lastmod = "2012-02-14T01:07:00Z"
weight = 8986
keywords = [ "development", "cross-compile", "windows", "win64" ]
aliases = [ "/questions/8986" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to cross compile Wireshark x64 on an x86 Windows machine](/questions/8986/how-to-cross-compile-wireshark-x64-on-an-x86-windows-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8986-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using rev 37663 of Wireshark (1.7.0) and VS 2008 on Windows XP x86 and I would like to compile a 64-bit version of Wireshark. I have followed all the instructions detailed in <a href="http://wiki.wireshark.org/Development/Win64">http://wiki.wireshark.org/Development/Win64</a></p><p>Here's what I've done:</p><ul><li><p>prepared cmd.exe by running:</p><blockquote>"C:\Program Files\Microsoft Visual Studio 9.0\VC\vcvarsall.bat" x86_amd64</blockquote></li><li><p>I've also tried running this command as well, with the same result:<br />
</p><blockquote><p>"C:\Program Files\Microsoft Visual Studio 9.0\VC\bin\x86_amd64\vcvarsx86_amd64.bat"</p></blockquote></li><li><p>I've downloaded vcredist_x64.exe and put it into:<br />
</p><blockquote><p>C:\wireshark-win64-libs</p></blockquote></li><li><p>I've modified a line in config.nmake to this:<br />
</p><blockquote><p>WIRESHARK_TARGET_PLATFORM=win64</p></blockquote></li></ul><p>I've run the following commands:</p><pre><code>nmake -f Makefile.nmake verify_tools
nmake -f Makefile.nmake setup
nmake -f Makefile.nmake distclean
nmake -f Makefile.nmake all</code></pre><p>which all succeed until the last command. Here is the output of the last command:</p><pre><code>Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

Verifying library package files ...

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

Wireshark is ready to build.
        sed -e s/@[email protected]/1.7.0&quot;-HONE-TEST-x64-1&quot;/  -e &quot;s/@[email protected]/#define
 HAVE_C_ARES 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@HAVE_KF
[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBZ 1/&quot;  -e &quot;s/@H
[email protected]/#define HAVE_LIBPCAP 1/&quot;  -e &quot;s/@[email protected]/#define HAV
E_PCAP_FINDALLDEVS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP
_DATALINK_NAME_TO_VAL 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_P
CAP_DATALINK_VAL_TO_NAME 1/&quot;  -e &quot;s/@[email protected]/#def
ine HAVE_PCAP_DATALINK_VAL_TO_DESCRIPTION 1/&quot;  -e &quot;s/@[email protected]//&quot;  -
e &quot;s/@[email protected]/#define HAVE_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAV
E_PCAP_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_OPEN 1/&quot;  -e &quot;s/@HAV
[email protected]/#define HAVE_PCAP_OPEN_DEAD 1/&quot;  -e &quot;s/@HAVE_PCAP_LIST_DATALIN
[email protected]/#define HAVE_PCAP_LIST_DATALINKS 1/&quot;  -e &quot;s/@[email protected]/#defi
ne HAVE_PCAP_FREE_DATALINKS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCA
P_SET_DATALINK 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_SETSAMPLING
1/&quot;  -e &quot;s/@[email protected]/#define HAVE_BPF_IMAGE 1/&quot;  -e &quot;s/@HAVE_LIBWIRESHARK
[email protected]/#define HAVE_LIBWIRESHARKDLL 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGN
UTLS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGCRYPT 1/&quot;  -e &quot;s/@[email protected]/#d
efine HAVE_LUA 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LUA_5_1 1/&quot;  -e &quot;s/@HAVE_P
[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@HAVE_LIBPOR
[email protected]/#define HAVE_LIBPORTAUDIO 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@HAVE_S
[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_GEOIP 1/&quot;  -e &quot;s/@[email protected]/#define INET6 1
/&quot;  -e &quot;s/@[email protected]/#define HAVE_NTDDNDIS_H 1/&quot;  -e &quot;s/@MAIN_MENU_USE_UI
[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_HONE
1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s
/@[email protected]//&quot;  &lt; config.h.win32 &gt; config.h
        cd tools
        &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
            -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\nma
ke.exe&quot; /                   -f Makefile.nmake
Setting environment for using Microsoft Visual Studio 2008 x86 tools.

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl -WX -D_U_=&quot;&quot; /Zi /W3 /MD /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=150
0  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE /MP /GS lemon.c
Microsoft (R) C/C++ Optimizing Compiler Version 15.00.21022.08 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

lemon.c
Microsoft (R) Incremental Linker Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:lemon.exe
/debug
lemon.obj
MSVCRT.lib(chkstk.obj) : fatal error LNK1112: module machine type &#39;X86&#39; conflict
s with target machine type &#39;x64&#39;
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN
\x86_amd64\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;..\native-nmake.CMD&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN
\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>What am I missing? -Russ</p></div><div id="question-tags" class="tags-container tags">development cross-compile windows win64</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '12, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/043a3cdec1b6228c8cbd690de705fd84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruslanad&#39;s gravatar image" /><p>ruslanad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruslanad has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '12, 19:56</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-8986" class="comments-container"></div><div id="comment-tools-8986" class="comment-tools"></div><div class="clear"></div><div id="comment-8986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8989"></span>

<div id="answer-container-8989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8989-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Somehow you have an x86 object (chkstk.obj) module that obviously won't link with amd64 code.</p><p>There are some lines in the output that intrigues me:</p><pre><code>        cd lemon
        ..\native-nmake &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; -f Makefile.nmake
Setting environment for using Microsoft Visual Studio 2008 x86 tools.</code></pre><p>Why is the environment being set for x86? chkstk.obj is a Visual Studio/SDK object file and is provided in both x86 and amd64 versions. I suspect that the library search path is being set to x86 by the last line I've shown above.</p><p>I can't see what would be causing this looking at Makefile.nmake in the lemon directory. Have you made any source modifications at all?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-8989" class="comments-container"><span id="9004"></span><div id="comment-9004" class="comment"><div id="post-9004-score" class="comment-score"></div><div class="comment-text"><p>The environment is being set back to x86 in native-nmake.cmd by calling vcvarsall.bat without any arguments. This is in fact the correct behavior, because when I changed that line in native-nmake.cmd to set the environment for cross-compiling, the build process failed later on. It turns out that the lemon executable gets executed later in the build process. This means that it does indeed need to be compiled in the x86 environment. The problem is that NMAKE thinks that it should be compiling 64-bit code and fails because we are (correctly) trying to generate 32-bit code in this one instance.</p></div><div id="comment-9004-info" class="comment-info"><span class="comment-age">(14 Feb '12, 12:19)</span> ruslanad</div></div></div><div id="comment-tools-8989" class="comment-tools"></div><div class="clear"></div><div id="comment-8989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

