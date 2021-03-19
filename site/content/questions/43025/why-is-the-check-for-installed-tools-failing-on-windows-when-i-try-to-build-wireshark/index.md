+++
type = "question"
title = "Why is the check for installed tools failing on Windows when I try to build Wireshark?"
description = '''Hi I am trying to compile the wireshark source code with the newly placed wpcap.dll and packet.dll which was compiled by me with some changes.while i am going through step by step guide of compiling i am getting following error while verifying the tools.All the tools are installed correctly accordin...'''
date = "2015-06-09T21:37:00Z"
lastmod = "2015-06-09T22:04:00Z"
weight = 43025
keywords = [ "windows", "compilation", "wireshark" ]
aliases = [ "/questions/43025" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the check for installed tools failing on Windows when I try to build Wireshark?](/questions/43025/why-is-the-check-for-installed-tools-failing-on-windows-when-i-try-to-build-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43025-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am trying to compile the wireshark source code with the newly placed wpcap.dll and packet.dll which was compiled by me with some changes.while i am going through step by step guide of compiling i am getting following error while verifying the tools.All the tools are installed correctly according to my knowledge.Can any one help me in solving these errors.</p><pre><code>C:\Development\wireshark-1.99.6&gt;nmake -f makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of &#39;C:\Development\Wireshark-win32-libs\current_tag.txt&#39; is
(unknown).
It should be 2015-04-06.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 12.0/VC/BIN/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 12.0/VC/BIN/link
       nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 12.0/VC/BIN/nmake
       bash: /usr/bin/bash
       env: /usr/bin/env
       grep: /usr/bin/grep
       /usr/bin/find: /usr/bin/find
       peflags: /usr/bin/peflags
       C:\tools\python2\python.exe: /cygdrive/c/tools/python2/python.exe
       C:\Qt\5.4\msvc2013\bin\qmake: /cygdrive/c/Qt/5.4/msvc2013/bin/qmake
       sed: /usr/bin/sed
       wget: /cygdrive/c/ProgramData/chocolatey/bin/wget

Can&#39;t find:  perl unzip

ERROR: These application(s) are either not installed or simply can&#39;t be found in the current PATH: /cygdrive/c/tools/python2:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow:/cygdrive/c/Program Files/Microsoft SDKs/F#/3.1/Framework/v4.0:/cygdrive/c/Program Files/MSBuild/12.0/bin:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/Common7/IDE:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/VC/BIN:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/Common7/Tools:/cygdrive/c/Windows/Microsoft.NET/Framework/v4.0.30319:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/VC/VCPackages:/cygdrive/c/Program Files/HTML Help Workshop:/cygdrive/c/Program Files/Microsoft Visual Studio 12.0/Team Tools/Performance Tools:/cygdrive/c/Program Files/Windows Kits/8.1/bin/x86:/cygdrive/c/Program Files/Microsoft SDKs/Windows/v8.1A/bin/NETFX 4.5.1 Tools:/cygdrive/c/Windows/system32:/cygdrive/c/Windows:/cygdrive/c/Windows/System32/Wbem:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files/Windows Kits/8.1/Windows Performance Toolkit:/cygdrive/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files/Microsoft SDKs/TypeScript/1.0:/cygdrive/c/Program Files/Microsoft SQL Server/120/Tools/Binn:/cygdrive/c/tools/python2:/cygdrive/c/Program Files/Microsoft SQL Server/90/Tools/binn:/cygdrive/c/ProgramData/chocolatey/bin:/cygdrive/c/tools/cygwin:/cygdrive/c/Program Files/HTML Help Workshop:/usr/bin:/cygdrive/c/Development/Wireshark-win32-libs/gtk2/bin:/cygdrive/c/bin:/cygdrive/c/Development/Wireshark-win32-libs/zlib-1.2.8.

For additional help, please visit:
    http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html

NMAKE : fatal error U1077: &#39;C:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.</code></pre><p>Thanks, Karun</p></div><div id="question-tags" class="tags-container tags">windows compilation wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 21:37</strong></p><img src="https://secure.gravatar.com/avatar/50c4b78862c6ca806916c3a71498cdf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karun256&#39;s gravatar image" /><p>karun256<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karun256 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '15, 22:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43025" class="comments-container"></div><div id="comment-tools-43025" class="comment-tools"></div><div class="clear"></div><div id="comment-43025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43026"></span>

<div id="answer-container-43026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43026-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>All the tools are installed correctly according to my knowledge.</p></blockquote><p>So you know that Perl and unzip are installed? If not, install them; they come from Cygwin. See <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin">section 2.2.5 "Install Cygwin"</a> in the Wireshark Developer's Guide; it says that unzip is in Archive/unzip and Perl is in Interpreters/perl in the Cygwin installer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43026" class="comments-container"></div><div id="comment-tools-43026" class="comment-tools"></div><div class="clear"></div><div id="comment-43026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

