+++
type = "question"
title = "ERROR: The contents of C:&#92;wireshark-win32-libs&#92;current_tag.txt is (unknown). It should be 2011-06-27."
description = '''I am developing amf plugin for wireshark in windows. when i run the following command:  nmake -f Makefile.nmake verify_tools The output is as follows: C:&#92;wireshark&amp;gt; nmake -f Makefile.nmake verify_tools  Microsoft (R) Program Maintenance Utility Version 10.00.40219.01 Copyright (C) Microsoft Corpo...'''
date = "2012-11-22T21:26:00Z"
lastmod = "2012-11-23T02:02:00Z"
weight = 16230
keywords = [ "error" ]
aliases = [ "/questions/16230" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ERROR: The contents of C:\\wireshark-win32-libs\\current\_tag.txt is (unknown). It should be 2011-06-27.](/questions/16230/error-the-contents-of-cwireshark-win32-libscurrent_tagtxt-is-unknown-it-should-be-2011-06-27)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16230-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing amf plugin for wireshark in windows.</p><p>when i run the following command: nmake -f Makefile.nmake verify_tools</p><p>The output is as follows:</p><pre><code>C:\wireshark&gt; nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of C:\wireshark-win32-libs\current_tag.txt is (unknown).
It should be 2011-06-27.

Checking for required applications:
        cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/BIN/nmake
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget

Can&#39;t find:  mt

ERROR: These application(s) are either not installed or simply can&#39;t be found in
 the current PATH: /cygdrive/c/Python27:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VSTSDB/Deploy:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/Common7/IDE:/cygdrive/c/Program Files (x86)/Microsoft Visual Stu    dio 10.0/VC/BIN:/cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/Common7/Tools:/cygdrive/c/Windows/Microsoft.NET/Framework64/v4.0.30319:/cygdrive/c/Windows/Microsoft.NET/Framework64/v3.5:/cygdrive/c/Program Files (x86)/MicrosoftVisual Studio 10.0/VC/VCPackages:/cygdrive/c/PlatformSDK/bin/NETFX 4.0 Tools:/cygdrive/c/PlatformSDK/bin:/usr/bin:/cygdrive/c/Windows/system32:/cygdrive/c/Windows:/cygdrive/c/WindowsWbem:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files (x86)/Hewlett-HP ProtectTools Security Manager/Bin:/cygdrive/c/Program Files/Intel/DMIX:/cygdrive/c/Program Files (x86)/Intel/Services/IPT:/cygdrive/c/Program Files/Microsoft/Web Platform Installer:/cygdrive/c/Program Files (x86)/Microsoft SQL Server/100/Tools/Binn:/cygdrive/c/Program Files/Microsoft SQL Server/100/Tools/Binn:/cygdrive/c/Program Files/Microsoft SQL Server/100/DTS/Binn:/cygdrive/c/Program Files (x86)/Microsoft ASP.NET/ASP.NET Web Pages/v1.0:/cygdrive/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files/Microsoft Windows Performance Toolkit:/cygdrive/c/Program Files/TortoiseSVN/bin:/usr/bin:/cygdrive/c/wireshark-win32-libs/gtk2/bin:/cygdrive/c/bin:/cygdrive/c/wireshark-win32-libs/zlib125.

For additional help, please visit:
    http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html

NMAKE : fatal error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;</code></pre><hr /><p>how should i fix it</p></div><div id="question-tags" class="tags-container tags">error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '12, 21:26</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p>Akhil<br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '12, 01:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16230" class="comments-container"><span id="16231"></span><div id="comment-16231" class="comment"><div id="post-16231-score" class="comment-score"></div><div class="comment-text"><p>If you have followed the developers guide and installed cygwin and all the tools I supose it's a problem with your path.</p></div><div id="comment-16231-info" class="comment-info"><span class="comment-age">(22 Nov '12, 22:05)</span> Anders ♦</div></div><span id="16232"></span><div id="comment-16232" class="comment"><div id="post-16232-score" class="comment-score"></div><div class="comment-text"><p>I have followed developers guide strictly and have installed the tools in the same order.</p></div><div id="comment-16232-info" class="comment-info"><span class="comment-age">(22 Nov '12, 22:22)</span> Akhil</div></div><span id="16233"></span><div id="comment-16233" class="comment"><div id="post-16233-score" class="comment-score"></div><div class="comment-text"><p>Do this in a cmd window, not the bash shell.</p></div><div id="comment-16233-info" class="comment-info"><span class="comment-age">(22 Nov '12, 22:52)</span> Jaap ♦</div></div><span id="16236"></span><div id="comment-16236" class="comment"><div id="post-16236-score" class="comment-score"></div><div class="comment-text"><p>I am doing it in a cmd window</p></div><div id="comment-16236-info" class="comment-info"><span class="comment-age">(23 Nov '12, 00:52)</span> Akhil</div></div></div><div id="comment-tools-16230" class="comment-tools"></div><div class="clear"></div><div id="comment-16230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16239"></span>

<div id="answer-container-16239" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16239-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your configuration (in config.nmake) doesn't seem to be set correctly. You appear to have VS 2010 installed (from the path) but verify_tools is looking for mt.exe, the manifest tool.</p><p>According to my reading of config.nmake, mt.exe is only required for VS 2005 and 2008. This is set by checking the config.nmake entry for the compiler to use.</p><p>The compiler to use is set by by the MSVC_VARIANT variable, e.g. <code>MSVC_VARIANT=MSVS2010</code>.</p><p>If you have strictly followed the developers guide you should have set this entry as part of step 2.2.5.2.c</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-16239" class="comments-container"><span id="33180"></span><div id="comment-33180" class="comment"><div id="post-33180-score" class="comment-score"></div><div class="comment-text"><p>I followed the guide and it give an error:</p><p>Can't find: cl E:\Python27\python.exe</p><p>NMAKE : fatal error U1077: 'c:\cygwin\bin\bash.EXE' : return code '0x1' Stop. How do I solve it?</p></div><div id="comment-33180-info" class="comment-info"><span class="comment-age">(29 May '14, 11:54)</span> aman</div></div><span id="33193"></span><div id="comment-33193" class="comment"><div id="post-33193-score" class="comment-score"></div><div class="comment-text"><p>This seems to be a different question, please start a new question with an appropriate title and the full output from <code>nmake -f Makefile.nmake verify_tools</code></p></div><div id="comment-33193-info" class="comment-info"><span class="comment-age">(30 May '14, 02:53)</span> grahamb ♦</div></div></div><div id="comment-tools-16239" class="comment-tools"></div><div class="clear"></div><div id="comment-16239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

