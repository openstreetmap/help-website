+++
type = "question"
title = "64-bit Wireshark build fails in Windows"
description = '''I copied a 32-bit build code(after running distclean) and changed &quot;WIRESHARK_TARGET_PLATFORM=win64&quot; in the config.nmake file.  Then I setup the build environment using the command: &quot;CALL &quot;C:&#92;Program Files&#92;Microsoft SDKs&#92;Windows&#92;v7.1&#92;Bin&#92;SetEnv.cmd&quot; /x64&quot; Then, after running the commands:  nmake -f M...'''
date = "2012-12-16T22:13:00Z"
lastmod = "2012-12-16T22:49:00Z"
weight = 16952
keywords = [ "windows7", "build", "64-bit" ]
aliases = [ "/questions/16952" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [64-bit Wireshark build fails in Windows](/questions/16952/64-bit-wireshark-build-fails-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I copied a 32-bit build code(after running distclean) and changed "WIRESHARK_TARGET_PLATFORM=win64" in the config.nmake file.</p><p>Then I setup the build environment using the command: <code>"CALL "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" /x64"</code></p><p>Then, after running the commands:</p><blockquote><p>nmake -f Makefile.nmake distclean</p><p>nmake -f Makefile.nmake setup</p><p>nmake -f Makefile.nmake distclean</p></blockquote><p>in that order, when I build the code I get the following error:</p><pre><code>    Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

Verifying library package files ...

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

Wireshark is ready to build.
        sed -e s/@[email protected]/1.9.0-sid1/  -e &quot;s/@HA[email protected]/#define HAVE_C
_ARES 1/&quot;  -e &quot;s/@HA[email protected]//&quot;  -e &quot;s/@HA[email protected]//&quot;  -e &quot;s/@HA[email protected]//&quot;
  -e &quot;s/@HA[email protected]/#define HAVE_LIBZ 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_LIB
PCAP 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_PCAP_FINDALLDEVS 1/&quot;  -e &quot;s
/@HA[email protected]/#define HAVE_PCAP_DATALINK_NAME_TO_VAL 1/&quot;  -e
 &quot;s/@HA[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO_NAME 1/&quot;
 -e &quot;s/@HA[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO
_DESCRIPTION 1/&quot;  -e &quot;s/@HA[email protected]//&quot;  -e &quot;s/@HA[email protected]/#define HA
VE_REMOTE 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_PCAP_REMOTE 1/&quot;  -e &quot;s/@HAV
[email protected]/#define HAVE_PCAP_OPEN 1/&quot;  -e &quot;s/@HA[email protected]/#define HAV
E_PCAP_OPEN_DEAD 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_PCAP_LIST_DA
TALINKS 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_PCAP_FREE_DATALINKS 1
/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_PCAP_SET_DATALINK 1/&quot;  -e &quot;s/@HA
[email protected]/#define HAVE_PCAP_SETSAMPLING 1/&quot;  -e &quot;s/@HA[email protected]/#
define HAVE_BPF_IMAGE 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_LIBWIRESHAR
KDLL 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_LIBGNUTLS 1/&quot;  -e &quot;s/@HAVE_LIBGCRY
[email protected]/#define HAVE_LIBGCRYPT 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_LUA 1/&quot;  -e &quot;s/@HA
[email protected]/#define HAVE_LUA 1/&quot;  -e &quot;s/@HA[email protected]//&quot;  -e &quot;s/@HA[email protected]/#defi
ne HAVE_AIRPCAP 1/&quot;  -e &quot;s/@HA[email protected]//&quot;  -e &quot;s/@HA[email protected]/#define
 HAVE_LIBPORTAUDIO 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@HA[email protected]/#define HAV
E_LIBSMI 1/&quot;  -e &quot;s/@HA[email protected]/#define HAVE_GEOIP 1/&quot;  -e &quot;s/@HA[email protected]/#
define HAVE_GEOIP_V6 1/&quot;  -e &quot;s/@[email protected]/#define INET6 1/&quot;  -e &quot;s/@HAVE_NTDDNDIS_
[email protected]/#define HAVE_NTDDNDIS_H 1/&quot;  -e &quot;s/@[email protected]/#define PCAP_NG_DEFAULT
1/&quot;  -e &quot;s/@[email protected]//&quot;  &lt; config.h.win32 &gt; config.h
        cd tools
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.
exe&quot; /                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\
Bin\amd64\nmake.exe&quot; /                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl -WX -D_U_=&quot;&quot; /Zi /W3 /MD /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=160
0  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE /MP /GS lemon.c
Microsoft (R) C/C++ Optimizing Compiler Version 16.00.40219.01 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

lemon.c
Microsoft (R) Incremental Linker Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:lemon.exe
/debug
lemon.obj
        cd ..
        cd ..
        cd image
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.
exe&quot; /                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        sed -e s/@[email protected]/1/  -e s/@[email protected]/9/  -e s/@VERSION_MICR
[email protected]/0/  -e s/@[email protected]/amd64/  &lt; wireshark.exe.manifest.in &gt; wires
hark.exe.manifest
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; wire
shark.rc.in &gt; wireshark.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; libw
ireshark.rc.in &gt; libwireshark.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; tsha
rk.rc.in &gt; tshark.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; raws
hark.rc.in &gt; rawshark.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; capi
nfos.rc.in &gt; capinfos.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; edit
cap.rc.in &gt; editcap.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; text
2pcap.rc.in &gt; text2pcap.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; merg
ecap.rc.in &gt; mergecap.rc
        sed -e s/@[email protected]/1.9.0/  -e s/@[email protected]/1,9,0/  &lt; wiretap.rc.in &gt; w
iretap.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; dump
cap.rc.in &gt; dumpcap.rc
        sed -e s/@[email protected]/1.9.0-sid1/  -e s/@[email protected]/1,9,0,0/  &lt; libw
sutil.rc.in &gt; libwsutil.rc
        cd ..
        cd codecs
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.
exe&quot; /                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl -WX -DHAVE_CONFIG_H -D_U_=&quot;&quot; /DPCAP_VERSION=4_1_2 /Zi /W3 /MD /DWIN32
_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTD
C_NO_DEPRECATE /MP /GS /w34295  /IC:\wireshark-win64-libs\gtk2\include\glib-2.0
 /IC:\wireshark-win64-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -D
G_DISABLE_SINGLE_INCLUDES -Fd.\ -c G711u\G711udecode.c /FoG711udecode.obj
Microsoft (R) C/C++ Optimizing Compiler Version 16.00.40219.01 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

G711udecode.c
        cl -WX -DHAVE_CONFIG_H -D_U_=&quot;&quot; /DPCAP_VERSION=4_1_2 /Zi /W3 /MD /DWIN32
_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTD
C_NO_DEPRECATE /MP /GS /w34295  /IC:\wireshark-win64-libs\gtk2\include\glib-2.0
 /IC:\wireshark-win64-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -D
G_DISABLE_SINGLE_INCLUDES -Fd.\ -c G711a\G711adecode.c /FoG711adecode.obj
Microsoft (R) C/C++ Optimizing Compiler Version 16.00.40219.01 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

G711adecode.c
        link /lib /out:codecs.lib G711udecode.obj  G711adecode.obj
Microsoft (R) Library Manager Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        xcopy C:\wireshark-win64-libs\zlib125 zlib.tmp /D /I /E /Y
0 File(s) copied
        cd zlib.tmp
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.
exe&quot; /                   -f win32/Makefile.msc zlib1.dll AS=ml64 LOC=&quot;-DASMV -DA
SMINF&quot; OBJA=&quot;inffasx64.obj gvmat64.obj inffas8664.obj&quot;

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        link -nologo -debug -incremental:no -opt:ref -def:win32/zlib.def -dll -i
mplib:zdll.lib  -out:zlib1.dll -base:0x5A4C0000 adler32.obj compress.obj crc32.o
bj deflate.obj gzclose.obj gzlib.obj gzread.obj  gzwrite.obj infback.obj inflate
.obj inftrees.obj trees.obj uncompr.obj zutil.obj inffasx64.obj gvmat64.obj inff
as8664.obj zlib1.res
inffasx64.obj : fatal error LNK1112: module machine type &#39;x64&#39; conflicts with ta
rget machine type &#39;X86&#39;
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0
\VC\Bin\amd64\link.EXE&quot;&#39; : return code &#39;0x458&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0
\VC\Bin\amd64\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>Can someone please tell me what I'm doing wrong?</p></div><div id="question-tags" class="tags-container tags">windows7 build 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '12, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-16952" class="comments-container"><span id="16957"></span><div id="comment-16957" class="comment"><div id="post-16957-score" class="comment-score"></div><div class="comment-text"><p>It worked! Thanks a lot! Can you convert your comment into an answer so that I can accept it?</p></div><div id="comment-16957-info" class="comment-info"><span class="comment-age">(17 Dec '12, 01:13)</span> SidR</div></div></div><div id="comment-tools-16952" class="comment-tools"></div><div class="clear"></div><div id="comment-16952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16954"></span>

<div id="answer-container-16954" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16954-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have the dir C:\wireshark\zlib.tmp, try deleting that before building.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16954" class="comments-container"><span id="36898"></span><div id="comment-36898" class="comment"><div id="post-36898-score" class="comment-score"></div><div class="comment-text"><p>I've been struggling with this link error for days until I found this solution. Just delete the zlib.tmp and rebuild. thank you!</p></div><div id="comment-36898-info" class="comment-info"><span class="comment-age">(07 Oct '14, 13:43)</span> christenmu</div></div></div><div id="comment-tools-16954" class="comment-tools"></div><div class="clear"></div><div id="comment-16954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

