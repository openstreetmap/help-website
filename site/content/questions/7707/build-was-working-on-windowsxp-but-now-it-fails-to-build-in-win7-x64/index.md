+++
type = "question"
title = "Build was working on WindowsXP, but now it fails to build in Win7 x64"
description = '''I have a source tree of Wireshark 1.4.9 that builds grreat in WindowsXP. I am moving to a Windows 7 x64 box now and need it to build there. So I did all the normal stuff (install VS 2008ee, install the right cygwin packages) but I get an error from nmake (see below). There are lots of google hits on...'''
date = "2011-11-29T13:38:00Z"
lastmod = "2011-11-30T08:04:00Z"
weight = 7707
keywords = [ "1.4.9", "windows7", "build", "x64" ]
aliases = [ "/questions/7707" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Build was working on WindowsXP, but now it fails to build in Win7 x64](/questions/7707/build-was-working-on-windowsxp-but-now-it-fails-to-build-in-win7-x64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7707-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a source tree of Wireshark 1.4.9 that builds grreat in WindowsXP. I am moving to a Windows 7 x64 box now and need it to build there. So I did all the normal stuff (install VS 2008ee, install the right cygwin packages) but I get an error from nmake (see below). There are lots of google hits on the U1045 error code, but they all lead no where. I have tried the usual tricks of running from an elevated command prompt and checking the environment to no avail.</p><pre><code>&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:

cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/cl
        link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/link
        nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 9.0/VC/BIN/nmake
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
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

&gt;nmake -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

cd tools
        &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
                  -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

cd lemon
        ..\native-nmake &quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /                   -f Makefile.nmake
NMAKE : fatal error U1045: spawn failed : No error
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
</code></pre></div><div id="question-tags" class="tags-container tags">1.4.9 windows7 build x64</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '11, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/0f5a76f518f2574b7933529218f9c6eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobwhite&#39;s gravatar image" /><p>bobwhite<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobwhite has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '11, 13:51</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-7707" class="comments-container"></div><div id="comment-tools-7707" class="comment-tools"></div><div class="clear"></div><div id="comment-7707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7716"></span>

<div id="answer-container-7716" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7716-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I FIXED IT!!!!!!!!!!!!!!!!!!!!!!</p><p>I did a "check out" of the native-nmake.cmd file (we use clearcase for CM) so then it was "writable". Now the build completes fine!</p><p>Can anyone explain such a thing to me? Why would native-name.cmd need to be writable to be spawned by nmake?????</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '11, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/0f5a76f518f2574b7933529218f9c6eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobwhite&#39;s gravatar image" /><p>bobwhite<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobwhite has one accepted answer">100%</span></p></div></div><div id="comments-container-7716" class="comments-container"><span id="7719"></span><div id="comment-7719" class="comment"><div id="post-7719-score" class="comment-score"></div><div class="comment-text"><p>Are you sure native-nmake.cmd was executable before? In SVN it has the property <code>svn:executable</code> set. Its writability shouldn't make a difference.</p></div><div id="comment-7719-info" class="comment-info"><span class="comment-age">(30 Nov '11, 11:37)</span> Gerald Combs ♦♦</div></div><span id="7727"></span><div id="comment-7727" class="comment"><div id="post-7727-score" class="comment-score"></div><div class="comment-text"><p>Indeed, you make a good point. I dug around and found I can set an "execute" bit in the MVFS view. Upon doing this, the build also works without having to checkout anything. But it appears to be a setting to only <em>my</em> view. So others would have to set it as well? At this point it becomes a clearcase usage question so I will take it elsewhere. Thank you all for your help!</p></div><div id="comment-7727-info" class="comment-info"><span class="comment-age">(01 Dec '11, 08:04)</span> bobwhite</div></div></div><div id="comment-tools-7716" class="comment-tools"></div><div class="clear"></div><div id="comment-7716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7714"></span>

<div id="answer-container-7714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7714-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have done essentially the same thing myself, i.e., moved from Windows XP x86 to Windows 7 x86_64, except for the 1.6 and trunk branches instead of the 1.4 branch. If at all possible, I'd recommend the latest version.</p><p>I started with the <a href="http://wiki.wireshark.org/Development/Win64">Win64 Development</a> wiki page, which you might also want to take a look at. However, I took some notes of my experience and here are the steps I took (as far as I recall and actually wrote down ... although I can't guarantee these notes are 100% complete):</p><ol><li>Install <a href="http://www.microsoft.com/visualstudio/en-us/products/2010-editions/visual-cpp-express">Microsoft Visual Studio 2010 Express Edition</a>.</li><li>Check for and install any updates.</li><li>Download <a href="http://www.microsoft.com/download/en/details.aspx?id=14632">vcredist_x64.exe</a> and save it to <code>C:\wireshark-win64-libs\</code>.</li><li>Download and install <a href="http://msdn.microsoft.com/en-us/windows/bb980924">Microsoft SDK</a>.</li><li>Download and install <a href="http://www.cygwin.com/">cygwin</a>.</li><li>Download and install <a href="http://python.org/">Python</a> (2.7.2).</li><li>Download and extract the <a href="http://www.wireshark.org/download.html">Wireshark sources</a>.</li><li>If you plan to create a Wireshark installer, download and install <a href="http://nsis.sourceforge.net/Download">NSIS</a> (2.4.6).</li><li><p>Edit Wireshark's <code>config.nmake</code> file, setting:</p><ul><li><code>MSVC_VARIANT=MSVC2010</code> (Yes, I know intuitively it should be set to MSVC2010EE, but I found that setting it to MSVC2010EE didn't work. I don't know why.)</li><li><code>MAKENSIS="$(PROGRAM_FILES) (x86)\NSIS\makensis.exe"</code></li><li><code>WIRESHARK_TARGET_PLATFORM=win64</code> (Alternatively, you can set this as an environment variable.)</li></ul></li><li><p>From the Windows SDK 7.1 command prompt:</p><ul><li><code>nmake -f Makefile.nmake setup</code></li><li><code>nmake -f Makefile.nmake distclean</code></li><li><code>nmake -f Makefile.nmake all</code></li><li><code>nmake -f Makefile.nmake packaging</code></li><li>etc.</li></ul></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '11, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '11, 19:47</p></div></div><div id="comments-container-7714" class="comments-container"><span id="7715"></span><div id="comment-7715" class="comment"><div id="post-7715-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for the reply. It appears you are building the <em>64bit</em> version on Win7. I desire to build a <em>32bit</em> version so it will still run on both flavors of windows (for my fellow workers who still only hae XP machines, ha!).</p><p>A co-worker was able to build my 32-bit code base on his win7 x64 machine, so I must have some problem with my cygwin installation. My cygwin throws a error upon launching that his does not ("/usr/bin/mintty: could not load icon from /Cygwin-Terminal.ico"). I have tried everything to fix it but it must be some Windows update I have that he does not. Are the two problems related? Maybe not, but it's all I have to go on right now.</p><p>Anyone else have cygwin installed on Win7 x64? Does your desktop icon work without modification?</p><p>Thanks!</p></div><div id="comment-7715-info" class="comment-info"><span class="comment-age">(30 Nov '11, 07:08)</span> bobwhite</div></div></div><div id="comment-tools-7714" class="comment-tools"></div><div class="clear"></div><div id="comment-7714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

