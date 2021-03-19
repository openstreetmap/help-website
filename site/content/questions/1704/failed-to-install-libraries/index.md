+++
type = "question"
title = "failed to install libraries"
description = '''I tried to setup the build environment for Windows XP. I have installed Visual Studio 2005 ver.8, cygwin and python 27. Since I had problems with downloading the libraries, I did it manually by SVN. I put them into wireshark lib directory, which was specified in config.nmake file, and run &quot;nmake -f ...'''
date = "2011-01-11T06:44:00Z"
lastmod = "2011-01-13T01:48:00Z"
weight = 1704
keywords = [ "build" ]
aliases = [ "/questions/1704" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [failed to install libraries](/questions/1704/failed-to-install-libraries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1704-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to setup the build environment for Windows XP. I have installed Visual Studio 2005 ver.8, cygwin and python 27. Since I had problems with downloading the libraries, I did it manually by SVN. I put them into wireshark lib directory, which was specified in config.nmake file, and run "nmake -f Makefile.nmake setup". The following errors happen:</p><p>" .... File `gtk+-bundle_2.16.6-20100207_win32.zip' already there; not retrieving.</p><p>Extracting D:\doc\projects\myWIRESH~1.2\libs/gtk+-bundle_2.16.6-20100207_win32. zip into D:\doc\projects\myWIRESH~1.2\libs/gtk2</p><p><strong>Can't open perl script "C:\Program": No such file or directory</strong></p><p>ERROR: Couldn't unpack D:\doc\projects\myWIRESH~1.2\libs/gtk+-bundle_2.16.6-201 00207_win32.zip</p><p>NMAKE : fatal error U1077: 'd:\cygwin\bin\bash.EXE' : return code '0x1'</p><p>Stop."</p><p>Could you help to solve this issue please? What the perl script is mentioned above?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '11, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/6f0e2c60007c8ec9f855fbfdcdbfe5e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstantin&#39;s gravatar image" /><p>Konstantin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstantin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '11, 09:29</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-1704" class="comments-container"></div><div id="comment-tools-1704" class="comment-tools"></div><div class="clear"></div><div id="comment-1704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="1707"></span>

<div id="answer-container-1707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1707-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>it's win-setup.sh that's executing and it seems cygwins unzip you're missing. Try to make the verify_tools target first.</p><p>You can find all the details you need in the Wireshark <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developer's Guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '11, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1707" class="comments-container"></div><div id="comment-tools-1707" class="comment-tools"></div><div class="clear"></div><div id="comment-1707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1712"></span>

<div id="answer-container-1712" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>thank you for advise. I used the Dev Guide and unzip was installed and can read the lib archives. I expect that problem is in some perl script which was mentioned in the log. But the name of this script is truncated and I don't know what script exactly should be updated.</p><p>verify_tools results are ok:</p><pre><code>   d:\doc\projects\my\wireshark-1.4.2&gt;nmake /f Makefile.nmake verify_tools

   Microsoft (R) Program Maintenance Utility Version 8.00.50727.762
   Copyright (C) Microsoft Corporation.  All rights reserved.

   Checking for required applications:

    cl: /cygdrive/d/Program Files/Microsoft Visual Studio 8/VC/BIN/cl
    link: /cygdrive/d/Program Files/Microsoft Visual Studio 8/VC/BIN/link
    nmake: /cygdrive/d/Program Files/Microsoft Visual Studio 8/VC/BIN/nmake
    mt: /cygdrive/d/Program Files/Microsoft Visual Studio 8/VC/BIN/mt
    bash: /usr/bin/bash
    bison: /cygdrive/c/Program Files/Common Files/Symbian/tools/bison
    flex: /cygdrive/c/Program Files/Common Files/Symbian/tools/flex
    env: /usr/bin/env
    grep: /usr/bin/grep
    /usr/bin/find: /usr/bin/find
    perl: /cygdrive/d/Perl/bin/perl
    C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
    sed: /usr/bin/sed
    unzip: /cygdrive/c/Program Files/Common Files/Symbian/tools/unzip
    wget: /usr/bin/wget</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '11, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/6f0e2c60007c8ec9f855fbfdcdbfe5e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstantin&#39;s gravatar image" /><p>Konstantin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstantin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '11, 01:21</p></div></div><div id="comments-container-1712" class="comments-container"><span id="1714"></span><div id="comment-1714" class="comment"><div id="post-1714-score" class="comment-score">1</div><div class="comment-text"><p>Yet verify_tools is distinctly different from the results in the Developer Guide[1]</p><p>[1] http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChToolsWin32Verify</p></div><div id="comment-1714-info" class="comment-info"><span class="comment-age">(12 Jan '11, 04:17)</span> Jaap ♦</div></div></div><div id="comment-tools-1712" class="comment-tools"></div><div class="clear"></div><div id="comment-1712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1726"></span>

<div id="answer-container-1726" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1726-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Oh my god! Symbian! Pardon! I have just checked a presence of a tool but I didn't read the path completely.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '11, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/6f0e2c60007c8ec9f855fbfdcdbfe5e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstantin&#39;s gravatar image" /><p>Konstantin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstantin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '11, 00:00</p></div></div><div id="comments-container-1726" class="comments-container"></div><div id="comment-tools-1726" class="comment-tools"></div><div class="clear"></div><div id="comment-1726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1730"></span>

<div id="answer-container-1730" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1730-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you very much for help. I have setup the environment successfully.</p><p>However I can't still build the wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/6f0e2c60007c8ec9f855fbfdcdbfe5e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstantin&#39;s gravatar image" /><p>Konstantin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstantin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '11, 01:46</p></div></div><div id="comments-container-1730" class="comments-container"></div><div id="comment-tools-1730" class="comment-tools"></div><div class="clear"></div><div id="comment-1730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1731"></span>

<div id="answer-container-1731" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1731-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>SUCCESS :) Thank you.</p><p>There is small bug in GeoIP-1.4.6-win32ws\test\Makefile.vc (for win32).</p><p>It is necessary to add -DSRCDIR="GeoIP_src_path" as following:</p><p>CFLAGS=-DWIN32 -MD -nologo <strong>-DSRCDIR=\"d:\doc\projects\my\wireshark-1.4.2\libs\GeoIP-1.4.6-win32ws\"</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/6f0e2c60007c8ec9f855fbfdcdbfe5e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstantin&#39;s gravatar image" /><p>Konstantin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstantin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '11, 01:54</p></div></div><div id="comments-container-1731" class="comments-container"></div><div id="comment-tools-1731" class="comment-tools"></div><div class="clear"></div><div id="comment-1731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

