+++
type = "question"
title = "Getting build fatal errors U1077: return code &#x27;0x1&#x27; and &#x27;0x2&#x27;"
description = '''I am trying to build Wireshark development code 1.12 (as is) using microsoft VSD Express 10 and am getting 2 fatal errors as below. I found in another FAQ regarding setting the cygwin path prior to nmake to resolve the return code of &#x27;0x1&#x27; doesn&#x27;t seem to help in my case. Please suggest. thanks Muri...'''
date = "2014-09-02T09:55:00Z"
lastmod = "2014-09-03T08:41:00Z"
weight = 35933
keywords = [ "build_error", "fatal" ]
aliases = [ "/questions/35933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting build fatal errors U1077: return code '0x1' and '0x2'](/questions/35933/getting-build-fatal-errors-u1077-return-code-0x1-and-0x2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35933-score" class="post-score" title="current number of votes">0</div><span id="post-35933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build Wireshark development code 1.12 (as is) using microsoft VSD Express 10 and am getting 2 fatal errors as below. I found in another FAQ regarding setting the cygwin path prior to nmake to resolve the return code of '0x1' doesn't seem to help in my case. Please suggest. thanks Muriel</p><p>sbc.c link /lib /out:codecs.lib codecs.obj G711udecode.obj G711adecode.obj G722decode.obj G726decode.obj sbc.obj /usr/bin/link: extra operand <code>codecs.obj' Try</code>/usr/bin/link --help' for more information. NMAKE : fatal error U1077: 'c:\cygwin\bin\link.EXE' : return code '0x1' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\nmake.exe"' : return code '0x2' Stop.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-fatal" rel="tag" title="see questions tagged &#39;fatal&#39;">fatal</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p><span>christenmu</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div></div><div id="comments-container-35933" class="comments-container"></div><div id="comment-tools-35933" class="comment-tools"></div><div class="clear"></div><div id="comment-35933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35939"></span>

<div id="answer-container-35939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35939-score" class="post-score" title="current number of votes">0</div><span id="post-35939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your log output, it seems that your system has a link.exe program in Cygwin installation that is being used instead of the one coming from MSVC2010.</p><p>Are you trying to compile from Cygwin shell or from MSVC command prompt (as configured by the vcvarsall.bat script)? You should use the latter and your PATH environment variable should have MSVC2010 bin folder included before Cygwin bin folder.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35939" class="comments-container"><span id="35941"></span><div id="comment-35941" class="comment"><div id="post-35941-score" class="comment-score"></div><div class="comment-text"><p>I did my build from windows cmd.exe. But I noticed that when I downloaded the cygwin there's a link.exe in C:\cygwin64\bin. I renamed that link.exe so it won't pick up. But I am now getting these errors. cd zlib.tmp "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe" / -f win32/Makefile.msc zlib1.dll AS=ml64 LOC="-DASMV -DASMINF" OBJA="inffasx64.obj gvmat64.obj inffas8664.obj"</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.30319.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>    ml64 -c -coff -Zi -DASMV -DASMINF contrib/masmx64\inffasx64.asm</code></pre><p>'ml64' is not recognized as an internal or external command, operable program or batch file. NMAKE : fatal error U1077: 'ml64' : return code '0x1' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\nmake.exe"' : return code '0x2' Stop.</p></div><div id="comment-35941-info" class="comment-info"><span class="comment-age">(02 Sep '14, 15:46)</span> <span class="comment-user userinfo">christenmu</span></div></div><span id="35945"></span><div id="comment-35945" class="comment"><div id="post-35945-score" class="comment-score"></div><div class="comment-text"><p>As far as I know, MSVC2010 Express Edition does not come with an x64 compiler out of the box. You need to install the 7.1 SDK (see <a href="http://stackoverflow.com/questions/1865069/how-to-compile-a-64-bit-application-using-visual-c-2010-express">http://stackoverflow.com/questions/1865069/how-to-compile-a-64-bit-application-using-visual-c-2010-express</a> ) and ensure that it's part of your PATH environement variable.</p></div><div id="comment-35945-info" class="comment-info"><span class="comment-age">(02 Sep '14, 22:18)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="35955"></span><div id="comment-35955" class="comment"><div id="post-35955-score" class="comment-score"></div><div class="comment-text"><p>oh ok. thanks, I will install the 7.1 SDK. Earlier I had issue installing this version. Will try again.</p></div><div id="comment-35955-info" class="comment-info"><span class="comment-age">(03 Sep '14, 04:57)</span> <span class="comment-user userinfo">christenmu</span></div></div><span id="35960"></span><div id="comment-35960" class="comment"><div id="post-35960-score" class="comment-score"></div><div class="comment-text"><p>Sorry to keep coming up with new questions. Since I wanted to do the 32 bit build first, I went back to build for win32 and am getting these link errors. I am currently having 7.1 SDK install failures so I thought of doing the 32 first and try for 64 bit later. The errors below are for win32 build.</p><pre><code>    link -nologo -debug -incremental:no -opt:ref -def:win32/zlib.def -dll -i</code></pre><p>mplib:zdll.lib -out:zlib1.dll -base:0x5A4C0000 adler32.obj compress.obj crc32.o bj deflate.obj gzclose.obj gzlib.obj gzread.obj gzwrite.obj infback.obj inflate .obj inftrees.obj trees.obj uncompr.obj zutil.obj inffas32.obj match686.obj zlib 1.res Creating library zdll.lib and object zdll.exp LINK : fatal error LNK1123: failure during conversion to COFF: file invalid or c orrupt NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\link.EXE"' : return code '0x463' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\nmake.exe"' : return code '0x2' Stop.</p></div><div id="comment-35960-info" class="comment-info"><span class="comment-age">(03 Sep '14, 07:31)</span> <span class="comment-user userinfo">christenmu</span></div></div><span id="35963"></span><div id="comment-35963" class="comment"><div id="post-35963-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I just realized that I was using the MSVC2010 for 64 version instead of 32 when I was building. Build successfully now. Thank you again for your help.</p></div><div id="comment-35963-info" class="comment-info"><span class="comment-age">(03 Sep '14, 08:41)</span> <span class="comment-user userinfo">christenmu</span></div></div></div><div id="comment-tools-35939" class="comment-tools"></div><div class="clear"></div><div id="comment-35939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

