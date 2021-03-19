+++
type = "question"
title = "issue of compiling wireshark source code with vs2013 under 64bit option"
description = '''The environment is setted as below: @echo off call &quot;C:&#92;Program Files (x86)&#92;Microsoft Visual Studio12.0&#92;Common7&#92;Tools&#92;VsDevCmd.bat&quot; call &quot;C:&#92;Program Files (x86)&#92;Microsoft Visual Studio 12.0&#92;VC&#92;vcvarsall.bat&quot; amd64 e: cd E:&#92;Wireshark_Plugin&#92;Source&#92;wireshark-master set YES_I_KNOW_ABOUT_THE_DEPRECATION=...'''
date = "2016-05-13T00:30:00Z"
lastmod = "2016-06-05T18:13:00Z"
weight = 52492
keywords = [ "compile", "windows", "64bit", "wireshark" ]
aliases = [ "/questions/52492" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [issue of compiling wireshark source code with vs2013 under 64bit option](/questions/52492/issue-of-compiling-wireshark-source-code-with-vs2013-under-64bit-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52492-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The environment is setted as below:</p><pre><code>@echo off call &quot;C:\Program Files (x86)\Microsoft Visual Studio12.0\Common7\Tools\VsDevCmd.bat&quot;
call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; amd64
e:
cd E:\Wireshark_Plugin\Source\wireshark-master
set YES_I_KNOW_ABOUT_THE_DEPRECATION=1
set VISUALSTUDIOVERSION=12.0
set MSVC_VARIANT=MSVC2013EE
set CYGWIN_PATH=E:\Software\Cygwin\bin
set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\Source\wireshark-master
set WIRESHARK_TARGET_PLATFORM=win64
set QT5_BASE_DIR=E:\Software\QT\5.6\msvc2013_64
::nmake -f Makefile.nmake verify_tools
::nmake -f Makefile.nmake setup
::nmake -f Makefile.nmake distclean
nmake -f Makefile.nmake all
pause</code></pre><p>The compile result showed as below which is failed</p><pre><code>Microsoft (R) Program Maintenance Utility Version 12.00.21005.1 Copyright (C) Microsoft Corporation. All rights reserved.

    cd ..
    xcopy E:\Wireshark_Plugin\Source\wireshark-master\Wireshark-win64-libs\zlib-1.2.8-ws zlib.tmp /D /I /E /Y

    cd zlib.tmp
    &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.exe&quot; /
               -f win32/Makefile.msc zlib1.dll AS=ml64 LOC=&quot;-I. -DASMV -DASMINF&quot; OBJA=&quot;inffasx64.obj gvmat64.obj inffas8664.obj&quot;

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1 Copyright (C) Microsoft Corporation. All rights reserved.

    ml64 -c -coff -Zi -I. -DASMV -DASMINF ./contrib/masmx64\inffasx64.asm
&#39;ml64&#39; is not internal or external command

NMAKE : fatal error U1077: &#39;ml64&#39; : return code &#39;0x1&#39; Stop. NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0 \VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39; Stop.</code></pre><p>Does anybody has the same problem as me.I was confused about for almost one week,hope someone may help me. Thanks all.</p><p>By the way ,it has compiled successfully under 32bit option. then environment setting is as below:</p><pre><code>call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\vcvars32.bat&quot;
e:
cd E:\Wireshark_Plugin\Source\wireshark-master
set YES_I_KNOW_ABOUT_THE_DEPRECATION=1
set VISUALSTUDIOVERSION=12.0
set MSVC_VARIANT=MSVC2013EE
set CYGWIN_PATH=E:\Software\Cygwin\bin
set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\Source\wireshark-master
set WIRESHARK_TARGET_PLATFORM=win32
set QT5_BASE_DIR=E:\Software\QT\5.6\msvc2013_64
call &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\vcvarsall.bat&quot; x86
::nmake -f Makefile.nmake verify_tools
::nmake -f Makefile.nmake setup
::nmake -f Makefile.nmake distclean
nmake -f Makefile.nmake all
pause</code></pre></div><div id="question-tags" class="tags-container tags">compile windows 64bit wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/1445b0c2e6369c9b39c7802df15a2299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Water&#39;s gravatar image" /><p>Water<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Water has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '16, 02:16</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52492" class="comments-container"></div><div id="comment-tools-52492" class="comment-tools"></div><div class="clear"></div><div id="comment-52492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52495"></span>

<div id="answer-container-52495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52495-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First off, you should really move to CMake builds ASAP, nmake will be going away soon.</p><p>Next, you have some odd env vars set there, some aren't even required.</p><p><code>call "C:\Program Files (x86)\Microsoft Visual Studio12.0\Common7\Tools\VsDevCmd.bat"</code>, no point in doing this, the call to vcvarsall.bat does the job.</p><p><code>set VISUALSTUDIOVERSION=12.0</code>, this should be set by the call to <code>..\vcvarsall.bat amd64</code>.</p><p><code>set MSVC_VARIANT=MSVC2013EE</code>, this should be manually set in config.nmake.</p><p><code>set CYGWIN_PATH=E:\Software\Cygwin\bin</code>, this should be manually set in config.nmake.</p><p><code>set WIRESHARK_BASE_DIR=E:\Wireshark_Plugin\Source\wireshark-master</code>, this should normally be set to something outside of your source tree, but I don't think it's the cause of your issue.</p><p>The build failure is an inability to run the Visual Studio x64 macro assembler. From your build command prompt, typing "ml64" should get output like:</p><pre><code>C:\Users\graham&gt;ml64
Microsoft (R) Macro Assembler (x64) Version 12.00.31101.0
Copyright (C) Microsoft Corporation.  All rights reserved.

usage: ML64 [ options ] filelist [ /link linkoptions]
Run &quot;ML64 /help&quot; or &quot;ML64 /?&quot; for more info</code></pre><p>If that doesn't happen, then there's something up with your build environment or VS install, ml64.exe should be in <code>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\ml64.exe</code> and the directory <code>C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64</code> should be on your path (added by vcvarsall.bat).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52495" class="comments-container"><span id="53033"></span><div id="comment-53033" class="comment"><div id="post-53033-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb, I modified " amd64" to "x86_amd64" in the bat file,and the problem disappeared. I think it is a command prompt environment problem. But another Link problem happened, below is the error description,please kindly help me have a check,what mistake I have made.<br />
</p><p>Any suggestion and feedback from you are appreciated.Thank you again.</p><pre><code>&#39;libwritecap.lib&#39; is up-to-date
    cd ..
    cd extcap
    &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.exe&quot; /
               /f Makefile.nmake all

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

Linking ciscodump.exe
    link @C:\Users\ADMINI~1\AppData\Local\Temp\nm6B80.tmp
ciscodump.obj : error LNK2019: unresolved external symbol libpcap_write_file_header referenced in function ssh_open_remote_connection
ciscodump.obj : error LNK2019: unresolved external symbol libpcap_write_packet referenced in function ssh_loop_read
ciscodump.exe : fatal error LNK1120: 2 unresolved externals
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0
\VC\BIN\x86_amd64\link.EXE&quot;&#39; : return code &#39;0x460&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0
\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="comment-53033-info" class="comment-info"><span class="comment-age">(29 May '16, 22:32)</span> Water</div></div><span id="53034"></span><div id="comment-53034" class="comment"><div id="post-53034-score" class="comment-score">1</div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information. Also, please pay attention to formatting, which makes replies/comments actually readable.</p></div><div id="comment-53034-info" class="comment-info"><span class="comment-age">(30 May '16, 01:51)</span> Jaap ♦</div></div><span id="53036"></span><div id="comment-53036" class="comment"><div id="post-53036-score" class="comment-score">1</div><div class="comment-text"><p>Try doing a "clean" or "distclean". I note you're still using nmake, this is planned to be removed from the master branch in the near future.</p></div><div id="comment-53036-info" class="comment-info"><span class="comment-age">(30 May '16, 02:23)</span> grahamb ♦</div></div><span id="53089"></span><div id="comment-53089" class="comment"><div id="post-53089-score" class="comment-score"></div><div class="comment-text"><p>I tried to compile with Cmake, Sir.But also some problems happened.Did you have such kind experience,Any suggestions from you are appreciated.Thanks indeed.</p></div><div id="comment-53089-info" class="comment-info"><span class="comment-age">(31 May '16, 19:52)</span> Water</div></div></div><div id="comment-tools-52495" class="comment-tools"></div><div class="clear"></div><div id="comment-52495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53214"></span>

<div id="answer-container-53214" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53214-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks you all for paying attention my question.I have resolved this issue. It seems the Unicode setting problem. Go to Control Panel-&gt;Region and Language-&gt;Language for the non-Unicode programs In "Current language for non-Unicode programs", Change to "English(United States)".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '16, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/1445b0c2e6369c9b39c7802df15a2299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Water&#39;s gravatar image" /><p>Water<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Water has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53214" class="comments-container"></div><div id="comment-tools-53214" class="comment-tools"></div><div class="clear"></div><div id="comment-53214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

