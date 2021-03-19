+++
type = "question"
title = "How can I resolve this link error LNK1112 when building on 64-bit Windows?"
description = '''I followed the steps mentioned in the wiki article for win64 compilation, but I am getting the below error: ERROR fatal error LNK1112: module machine type &#x27;x64&#x27; conflicts with target machine type &#x27;X86&#x27;  Below is the compilation log: D:&#92;wireshark-1.6.7&amp;gt;nmake -f Makefile.nmake all  Microsoft (R) Pr...'''
date = "2012-04-26T09:09:00Z"
lastmod = "2015-01-29T01:04:00Z"
weight = 10463
keywords = [ "win64", "build" ]
aliases = [ "/questions/10463" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I resolve this link error LNK1112 when building on 64-bit Windows?](/questions/10463/how-can-i-resolve-this-link-error-lnk1112-when-building-on-64-bit-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10463-score" class="post-score" title="current number of votes">0</div><span id="post-10463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I followed the steps mentioned in the <a href="http://wiki.wireshark.org/Development/Win64">wiki</a> article for win64 compilation, but I am getting the below error:</p><pre><code>ERROR
fatal error LNK1112: module machine type &#39;x64&#39; conflicts with target machine type &#39;X86&#39;</code></pre><p>Below is the compilation log:</p><pre><code>D:\wireshark-1.6.7&gt;nmake -f Makefile.nmake all

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd tools
        &quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
                  -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\B
IN\nmake.exe&quot; /                   -f Makefile.nmake
Setting environment for using Microsoft Visual Studio 2008 x86 tools.

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        cd ..
        cd image
        &quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
                  -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd ..
        cd codecs
        &quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
                  -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

&#39;codecs.lib&#39; is up-to-date
        cd ..
        xcopy D:\wireshark-win64-libs-1.6\zlib125 zlib.tmp /D /I /E /Y
0 File(s) copied
        cd zlib.tmp
        &quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot; /
                  -f win32/Makefile.msc zlib1.dll AS=ml64 LOC=&quot;-DASMV -DASMINF&quot;
OBJA=&quot;inffasx64.obj gvmat64.obj inffas8664.obj&quot;

Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        link -nologo -debug -incremental:no -opt:ref -def:win32/zlib.def -dll -i
mplib:zdll.lib  -out:zlib1.dll -base:0x5A4C0000 adler32.obj compress.obj crc32.o
bj deflate.obj gzclose.obj gzlib.obj gzread.obj  gzwrite.obj infback.obj inflate
.obj inftrees.obj trees.obj uncompr.obj zutil.obj inffasx64.obj gvmat64.obj inff
as8664.obj zlib1.res
inffasx64.obj : fatal error LNK1112: module machine type &#39;x64&#39; conflicts with ta
rget machine type &#39;X86&#39;
NMAKE : fatal error U1077: &#39;&quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\x86_amd64\link.EXE&quot;&#39; : return code &#39;0x458&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.

D:\wireshark-1.6.7&gt;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win64" rel="tag" title="see questions tagged &#39;win64&#39;">win64</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '12, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/fc438dd41ea60662c8ddf0cef116e137?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pradeep&#39;s gravatar image" /><p><span>Pradeep</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pradeep has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '12, 09:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-10463" class="comments-container"></div><div id="comment-tools-10463" class="comment-tools"></div><div class="clear"></div><div id="comment-10463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39451"></span>

<div id="answer-container-39451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39451-score" class="post-score" title="current number of votes">1</div><span id="post-39451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the issue is more likely to be confusion over the build type and artefacts left from a previous build attempt. If you switch from x86 to x64 or vice-versa with an in-tree (i.e. nmake) build then you must run <code>nmake -f Makefile.nmake distclean</code> and then to make sure <code>del /s *.obj</code> and <code>del /s *.lib</code> to clean up.</p><p>Then you must also start a new command prompt and set the required VC tool chain (i.e. appropriate vcvars.bat for x86 or x64) and ensure any changes to config.nmake are also modified correctly for the required build type.</p><p>For the OP's question, they are using the x86 toolchain</p><blockquote><p>Setting environment for using Microsoft Visual Studio 2008 x86 tools.</p></blockquote><p>but using 64 bit libraries;</p><blockquote><p>xcopy D:\wireshark-win64-libs-1.6\zlib125</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '15, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '15, 02:37</strong> </span></p></div></div><div id="comments-container-39451" class="comments-container"><span id="39471"></span><div id="comment-39471" class="comment"><div id="post-39471-score" class="comment-score"></div><div class="comment-text"><p>if target machine is x86 why is it using wireshark-win64-libs... Is it because he didnot use nmake -f Makefile.nmake setup command before making all but only changed the target machine type to win32???</p></div><div id="comment-39471-info" class="comment-info"><span class="comment-age">(29 Jan '15, 01:04)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-39451" class="comment-tools"></div><div class="clear"></div><div id="comment-39451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39448"></span>

<div id="answer-container-39448" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39448-score" class="post-score" title="current number of votes">0</div><span id="post-39448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I know its late but for someone else who encounters the same problem this might help!!</p><p>So..This is because you are using x64 native command prompt and trying to build 32 bit version of wireshark.Make sure you use the correct command prompt!!<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '15, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p><span>koundi</span><br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39448" class="comments-container"></div><div id="comment-tools-39448" class="comment-tools"></div><div class="clear"></div><div id="comment-39448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

