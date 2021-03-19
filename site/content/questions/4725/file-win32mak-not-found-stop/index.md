+++
type = "question"
title = "file &#x27;win32.mak&#x27; not found Stop."
description = '''I tried to build wireshark under WinXP + MC VS 2008 by &quot;2.2. Win32: Step-by-Step Guide&quot;, but I&#x27;m having trouble with nmake -f Makefile.nmake verify_tools. I got: E:&#92;work&#92;wireshark&#92;trunk-1.6&amp;gt;nmake -f Makefile.nmake all  Microsoft (R) Program Maintenance Utility Version 9.00.21022.08 Copyright (C) ...'''
date = "2011-06-24T05:05:00Z"
lastmod = "2014-04-16T11:53:00Z"
weight = 4725
keywords = [ "development", "windows", "build" ]
aliases = [ "/questions/4725" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [file 'win32.mak' not found Stop.](/questions/4725/file-win32mak-not-found-stop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4725-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to build wireshark under WinXP + MC VS 2008 by "2.2. Win32: Step-by-Step Guide", but I'm having trouble with <code>nmake -f Makefile.nmake verify_tools</code>. I got:</p><pre><code>E:\work\wireshark\trunk-1.6&gt;nmake -f Makefile.nmake all

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

Makefile.nmake(10) : fatal error U1052: file &#39;win32.mak&#39; not found
Stop.</code></pre><p>I Google'd it and found <a href="http://www.wireshark.org/lists/wireshark-dev/200812/msg00055.html">this</a>, but it didn't help. I tried putting the <code>win32.mak</code> file in <code>C:\Program Files\Microsoft SDKs\Windows\v6.0A\Include</code>, but <code>nmake</code> cannot see it...</p><p>Please help</p></div><div id="question-tags" class="tags-container tags">development windows build</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '11, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/1f74fa27562ae0f98b96fa46254bdd79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boomsic&#39;s gravatar image" /><p>boomsic<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boomsic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '11, 18:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4725" class="comments-container"><span id="4732"></span><div id="comment-4732" class="comment"><div id="post-4732-score" class="comment-score"></div><div class="comment-text"><p>I make next solution</p><p>edit Makefile.nmake</p><p>and define full path to win32.mak</p></div><div id="comment-4732-info" class="comment-info"><span class="comment-age">(24 Jun '11, 09:49)</span> boomsic</div></div><span id="4758"></span><div id="comment-4758" class="comment"><div id="post-4758-score" class="comment-score"></div><div class="comment-text"><p>I run this one:</p><p>C:Program FilesMicrosoft Visual Studio 9.0VCbinvcvars32.bat</p><p>you mean that?</p><p>I agree that where is something wrong in my build environment, but I cant find a mistake.</p></div><div id="comment-4758-info" class="comment-info"><span class="comment-age">(26 Jun '11, 05:50)</span> boomsic</div></div></div><div id="comment-tools-4725" class="comment-tools"></div><div class="clear"></div><div id="comment-4725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="4733"></span>

<div id="answer-container-4733" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4733-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You shouldn't have to edit Makefile.nmake. If nmake can't find win32.mak then that's a strong indication that your build environment isn't set up correctly. Did you run <code>vcvarsall.bat</code> before running <code>nmake</code>?</p><hr /><p><strong>Update 2014-07-24</strong> It looks like Windows SDKs 8.0 and 8.1 don't include win32.mak. I worked around the issue by calling</p><pre><code>set INCLUDE=%INCLUDE%;c:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include</code></pre><p>or</p><pre><code>set INCLUDE=%INCLUDE%;c:\Program Files\Microsoft SDKs\Windows\v7.1A\Include</code></pre><p>as appropriate after running vcvarsall.bat</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '14, 15:50</p></div></div><div id="comments-container-4733" class="comments-container"></div><div id="comment-tools-4733" class="comment-tools"></div><div class="clear"></div><div id="comment-4733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5786"></span>

<div id="answer-container-5786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5786-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should install Windows sdk (http://www.microsoft.com/download/en/details.aspx?displaylang=en&amp;id=3138).</p><p>Then you will found Wind32.mak file in C:\Program Files\Microsoft SDKs\Windows\v7.0\Include.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '11, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/528f8dd6acb92d7bc6189be06e46c5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="one%20step&#39;s gravatar image" /><p>one step<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="one step has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '11, 10:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-5786" class="comments-container"><span id="27585"></span><div id="comment-27585" class="comment"><div id="post-27585-score" class="comment-score"></div><div class="comment-text"><p>Right. Copying it from there to C:\Program Files\Microsoft Visual Studio 12.0\VC\include solved the issue for me.</p></div><div id="comment-27585-info" class="comment-info"><span class="comment-age">(30 Nov '13, 06:21)</span> gtirloni</div></div></div><div id="comment-tools-5786" class="comment-tools"></div><div class="clear"></div><div id="comment-5786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30866"></span>

<div id="answer-container-30866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30866-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably need an include statement, here's the generic script I use (VS 2012 with the 7.1a sdk)</p><pre><code>@echo off
echo Commands are:
echo nmake -f Makefile.nmake verify_tools
echo nmake -f Makefile.nmake setup
echo nmake -f Makefile.nmake all
echo nmake -f Makefile.nmake packaging
echo nmake -f Makefile.nmake packaging_papps
echo nmake -f Makefile.nmake clean

set INCLUDE=%INCLUDE%;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include;
set PATH=%PATH%;c:\cygwin\bin
echo Adding things to the path...
if &quot;%1&quot; == &quot;&quot; goto x86
if /i %1 == x86       goto x86
if /i %1 == x64      goto x64
goto usage

:usage
echo Error in script usage. The correct usage is:
echo     %0 [option]
echo where [option] is: x86 ^| x64 
echo:
echo For example:
echo     %0 x86
goto :eof

:x64
set WIRESHARK_TARGET_PLATFORM=win64
call &quot;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat&quot; x64
title Command Prompt (VC++ 2012 x64)
goto :eof

:x86
set WIRESHARK_TARGET_PLATFORM=win32
call &quot;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat&quot; x86
title Command Prompt (VC++ 2012 -x86)
goto :eof</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '14, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-30866" class="comments-container"><span id="30876"></span><div id="comment-30876" class="comment"><div id="post-30876-score" class="comment-score">1</div><div class="comment-text"><p>While this may work for you, it might cause issues for others, observations\notes:</p><ol><li>Unless you need it in your batch file, there is no need to add Cygwin to the path, config.nmake does that for you.</li><li>The Win 7.1 SDK doesn't get installed with VS2012, it's a separate download.</li><li>The vcvarsall batch files are additive, so if you run the script again (from the same shell), particularly if you change from x86 to x64 (or vice-versa) your environment will grow duplicate entries each time and may not do what you think when changing the "bitedness".</li><li><p>There are some new Wireshark environment variables in the dev versions that you might want to set:</p><p>WIRESHARK_BASE_DIR - sets the base directory for your 3rd party libraries, this directory can contain both x86 and x64 libraries. Only used if WIRESHARK_LIB_DIR isn't defined.</p><p>WIRESHARK_VERSION_EXTRA - the suffix string for your version of Wireshark.</p></li><li><p>For VS2012 and later, the vcvarsall batchfile sets an env var for the VS version (VisualStudioVersion) in use so you don't need to modify config.nmake to manually set that, it picks it up from the env.</p></li><li>For VS2012 and later, the vcvarsall batchfile sets an env var if building for x64 (Platform=X64) in use so you don't need to modify config.nmake to manually set that, it picks it up from the env.</li></ol></div><div id="comment-30876-info" class="comment-info"><span class="comment-age">(17 Mar '14, 03:41)</span> grahamb ♦</div></div><span id="30978"></span><div id="comment-30978" class="comment"><div id="post-30978-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham I will try to make it a bit more generic - that's really helpful!</p></div><div id="comment-30978-info" class="comment-info"><span class="comment-age">(19 Mar '14, 20:27)</span> Scott Harman</div></div></div><div id="comment-tools-30866" class="comment-tools"></div><div class="clear"></div><div id="comment-30866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31903"></span>

<div id="answer-container-31903" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31903-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have already installed VisualStudio and service pack, then try to install SDK it may fail. You may need to unselect both C++ compiler and redistributable package from the install component for the install to work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p>YXI<br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div></div><div id="comments-container-31903" class="comments-container"></div><div id="comment-tools-31903" class="comment-tools"></div><div class="clear"></div><div id="comment-31903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

