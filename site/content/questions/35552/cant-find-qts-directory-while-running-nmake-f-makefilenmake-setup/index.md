+++
type = "question"
title = "Can&#x27;t find Qt&#x27;s directory while running nmake -f Makefile.nmake setup"
description = '''I&#x27;m trying to set up the wireshark build on a Windows 7, 32 bit OS. I&#x27;ve installed all the mandatory tools for the build, including the latest version of Qt(5.3.1) for VS 2010, OpenGl combination. When I run the commande nmake -f Makefile.nmake setup, I get an error that the Qt directory was not fou...'''
date = "2014-08-19T00:43:00Z"
lastmod = "2014-08-27T00:20:00Z"
weight = 35552
keywords = [ "qt", "build" ]
aliases = [ "/questions/35552" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't find Qt's directory while running nmake -f Makefile.nmake setup](/questions/35552/cant-find-qts-directory-while-running-nmake-f-makefilenmake-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to set up the wireshark build on a Windows 7, 32 bit OS. I've installed all the mandatory tools for the build, including the latest version of Qt(5.3.1) for VS 2010, OpenGl combination.</p><p>When I run the commande <em>nmake -f Makefile.nmake setup</em>, I get an error that the Qt directory was not found</p><pre><code>C:\Development\wireshark&gt;nmake -f Makefile.nmake setup

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

ERROR: The contents of &#39;C:\Wireshark-win32-libs-1.12\current_tag.txt&#39; is (unknow
n).
It should be 2014-06-19.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/Bin/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/Bin/link

        nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/Bin/nma
ke
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        peflags: /usr/bin/peflags
        perl: /cygdrive/c/Perl/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget

Can&#39;t find:  C:\Qt\Qt5.3.1\5.3\msvc2010_opengl\bin

ERROR: These application(s) are either not installed or simply can&#39;t be found in
 the current PATH: /cygdrive/c/Python27:/cygdrive/c/Windows/Microsoft.NET/Framew
ork/v4.0.30319:/cygdrive/c/Windows/Microsoft.NET/Framework/v3.5:/cygdrive/c/Prog
ram Files/Microsoft Visual Studio 10.0/Common7/IDE:/cygdrive/c/Program Files/Mic
rosoft Visual Studio 10.0/Common7/Tools:/cygdrive/c/Program Files/Microsoft Visu
al Studio 10.0/VC/Bin:/cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/
Bin/VCPackages:/cygdrive/c/Program Files/Microsoft SDKs/Windows/v7.1/Bin/NETFX 4
.0 Tools:/cygdrive/c/Program Files/Microsoft SDKs/Windows/v7.1/Bin:/cygdrive/c/P
erl/site/bin:/cygdrive/c/Perl/bin:/cygdrive/c/DevEnv/RBTools:/cygdrive/c/Windows
/system32:/cygdrive/c/Windows:/cygdrive/c/Windows/System32/Wbem:/cygdrive/c/Wind
ows/System32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files/Microsoft/Web Plat
form Installer:/cygdrive/c/Program Files/Microsoft ASP.NET/ASP.NET Web Pages/v1.
0:/cygdrive/c/Program Files/Windows Kits/8.0/Windows Performance Toolkit:/cygdri
ve/c/Program Files/Microsoft SQL Server/110/Tools/Binn:/cygdrive/c/Program Files
/Windows Phone TShell:/cygdrive/c/Program Files/IBM/RationalSDLC/ClearCase/bin:/
cygdrive/c/Program Files/IBM/RationalSDLC/common:/cygdrive/c/Program Files/Perfo
rce:/cygdrive/c/Program Files/Subversion/bin:/cygdrive/c/Program Files/doxygen/b
in:/cygdrive/c/Program Files/QuickTime/QTSystem:/cygdrive/d/Tools/ADB:/cygdrive/
c/Python27:/cygdrive/c/Program Files/Git/cmd:/cygdrive/c/Program Files/Microsoft
 Windows Performance Toolkit:/cygdrive/c/Users/shishir.j/AppData/Local/Bandizip/
7z:/usr/bin:/cygdrive/c/Wireshark-win32-libs-1.12/gtk2/bin:/cygdrive/c/bin:/cygd
rive/c/Wireshark-win32-libs-1.12/zlib125.

For additional help, please visit:
    http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html

NMAKE : fatal error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
Stop.</code></pre><p>But, I've hard coded the Qt base directory in the config.nmake file. Should I use an older version of Qt?</p><pre><code>!IF !DEFINED(QT5_BASE_DIR)
# Wireshark custom
QT5_BASE_DIR=C:\Qt\Qt5.3.1\5.3\msvc2010_opengl
# Digia official
#!ELSE IF EXIST(C:\Qt\Qt5.1.1\5.1.1\msvc2010)
#QT5_BASE_DIR=C:\Qt\Qt5.1.1\5.1.1\msvc2010
# Qt 5.2.1 web installer default paths
#!ELSE IF EXIST(C:\Qt\5.2.1\msvc2010)
#QT5_BASE_DIR=C:\Qt\5.2.1\msvc2010
#!ELSE IF EXIST(C:\Qt\5.2.1\msvc2012)
#QT5_BASE_DIR=C:\Qt\5.2.1\msvc2012
#!ELSE IF EXIST(C:\Qt\5.2.1\msvc2012_64)
#QT5_BASE_DIR=C:\Qt\5.2.1\msvc2012_64
# Digia official, installed in $(WIRESHARK_LIB_DIR)
#!ELSE IF EXIST($(WIRESHARK_LIB_DIR)\Qt5.1.1\5.1.1\msvc2010)
#QT5_BASE_DIR=$(WIRESHARK_LIB_DIR)\Qt5.1.1\5.1.1\msvc2010
#!ENDIF
!ENDIF</code></pre></div><div id="question-tags" class="tags-container tags">qt build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/94048b3e53f1991544b01d988e5b4ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shishir127&#39;s gravatar image" /><p>shishir127<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shishir127 has no accepted answers">0%</span></p></div></div><div id="comments-container-35552" class="comments-container"></div><div id="comment-tools-35552" class="comment-tools"></div><div class="clear"></div><div id="comment-35552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35553"></span>

<div id="answer-container-35553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35553-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although the error message is incomplete (it should list the tool it couldn't find), I think the issue is that setup can't find qmake in the QT5_BASE_DIR\bin directory.</p><p>Can you check that you do have qmake in that location? If not there is something up with your qt installation.</p><p>On a side note, rather than changing config.nmake, it can be easier to set environment variables for the config options so that your source tree isn't carrying unnecessary changes. The env vars to set for VS2010 are:</p><p><code>set CYGWIN=nodosfilewarning set WIRESHARK_BASE_DIR=path\to\the directory where you want the 3rd party libs downloaded into set WIRESHARK_TARGET_PLATFORM=win32 set QT5_BASE_DIR=path\to\your\qt installation set VisualStudioVersion=10.0 set WIRESHARK_VERSION_EXTRA=\your\version\suffix</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35553" class="comments-container"><span id="35559"></span><div id="comment-35559" class="comment"><div id="post-35559-score" class="comment-score"></div><div class="comment-text"><p>Qmake is present in the \bin directory. Could there be any other reason for the error? I tried to reinstall the tools, but I'm still getting the same error.</p><p>C:\Qt\Qt5.3.1\5.3\msvc2010_opengl\bin&gt;dir qmake.exe Directory of C:\Qt\Qt5.3.1\5.3\msvc2010_opengl\bin</p><p>08/19/2014 10:01 AM 1,630,720 qmake.exe 1 File(s) 1,630,720 bytes 0 Dir(s) 63,568,146,432 bytes free</p></div><div id="comment-35559-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:16)</span> shishir127</div></div><span id="35561"></span><div id="comment-35561" class="comment"><div id="post-35561-score" class="comment-score"></div><div class="comment-text"><p>cd into QT5_BASE_DIR\bin and execute <code>qmake -query QT_INSTALL_PREFIX</code> and post the output. It should be the same as QT5_BASE_DIR.</p></div><div id="comment-35561-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:26)</span> grahamb ♦</div></div><span id="35564"></span><div id="comment-35564" class="comment"><div id="post-35564-score" class="comment-score"></div><div class="comment-text"><p>Here's the output</p><p>C:\Qt\Qt5.3.1\5.3\msvc2010_opengl\bin&gt;qmake -query QT_INSTALL_PREFIX</p><p>C:/Qt/Qt5.3.1/5.3/msvc2010_opengl</p></div><div id="comment-35564-info" class="comment-info"><span class="comment-age">(19 Aug '14, 03:51)</span> shishir127</div></div><span id="35571"></span><div id="comment-35571" class="comment"><div id="post-35571-score" class="comment-score"></div><div class="comment-text"><p>Looks good, so why isn't the win-setup.sh script locating qmake in your configuration?</p><p>Coming back to the odd error message produced <code>Can't find:  C:\Qt\Qt5.3.1\5.3\msvc2010_opengl\bin</code>. If I set QT5_BASE_DIR to a path that doesn't have <code>\bin\qmake</code>, e.g. <code>C:\Temp</code>, then I get the expected error message <code>Can't find:  C:\Temp\bin\qmake</code>, why does your error message stop short without the qmake part?</p><p>Note: I'm not sure anyone else has used the VC2010 5.3.1 version of QT, the 1.12 release was built using the 5.1.1 version, although I can't see why the version matters at this point as the setup script is just checking qmake can be found. I'm also uncertain about using the opengl version of qt, as that needs extra graphic driver support.</p></div><div id="comment-35571-info" class="comment-info"><span class="comment-age">(19 Aug '14, 04:56)</span> grahamb ♦</div></div></div><div id="comment-tools-35553" class="comment-tools"></div><div class="clear"></div><div id="comment-35553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35785"></span>

<div id="answer-container-35785" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35785-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Reinstalling QT and getting the latest version of the source code solved the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/94048b3e53f1991544b01d988e5b4ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shishir127&#39;s gravatar image" /><p>shishir127<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shishir127 has no accepted answers">0%</span></p></div></div><div id="comments-container-35785" class="comments-container"></div><div id="comment-tools-35785" class="comment-tools"></div><div class="clear"></div><div id="comment-35785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

