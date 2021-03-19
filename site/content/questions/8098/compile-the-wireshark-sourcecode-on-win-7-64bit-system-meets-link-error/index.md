+++
type = "question"
title = "compile the wireshark sourcecode on win 7 64bit system meets link error"
description = '''Here is the compile log ,can anybody help me?  cl -DWIN32 -DNULL=0 -D_MT -D_DLL -WX -DHAVE_CONFIG_H /I. /I.. /If:&#92;wireshark-win64-libs-1.2&#92;gtk2&#92;include&#92;glib-2.0 /If:&#92;wireshark-win64-libs-1.2&#92;gtk2&#92;lib&#92;glib-2.0&#92;include /If:&#92;wireshark-win64-libs-1.2&#92;WPdpack&#92;include -D_U_=&quot;&quot; /Zi /W3 /MD /D_CRT_SECURE_NO...'''
date = "2011-12-22T23:08:00Z"
lastmod = "2011-12-23T23:16:00Z"
weight = 8098
keywords = [ "vs2008", "64-bit" ]
aliases = [ "/questions/8098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [compile the wireshark sourcecode on win 7 64bit system meets link error](/questions/8098/compile-the-wireshark-sourcecode-on-win-7-64bit-system-meets-link-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8098-score" class="post-score" title="current number of votes">0</div><span id="post-8098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the compile log ,can anybody help me?</p><pre><code>        cl -DWIN32 -DNULL=0 -D_MT -D_DLL -WX -DHAVE_CONFIG_H /I. /I.. /If:\wireshark-win64-libs-1.2\gtk2\include\glib-2.0  /If:\wireshark-win64-libs-1.2\gtk2\lib\glib-2.0\include /If:\wireshark-win64-libs-1.2\WPdpack\include -D_U_=&quot;&quot; /Zi /W3 /MD /D_CRT_SECURE_NO_DEPRECATE/D_CRT_NONSTDC_NO_DEPRECATE /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1500 -Fd.\ -c file_util.c unicode-utils.c mpeg-audio.c privileges.c str_util.c type_util.c
Microsoft (R) C/C++ Optimizing Compiler Version 15.00.30729.01 for x64
Copyright (C) Microsoft Corporation.  All rights reserved.

file_util.c
unicode-utils.c
mpeg-audio.c
privileges.c
str_util.c
type_util.c
Generating Code...
        link  /INCREMENTAL:NO /NOLOGO -entry:[email protected] -dll kernel32.lib  ws2_32.lib mswsock.lib advapi32.lib  /DEBUG /MACHINE:x64 /MANIFEST:no  /DEF:libwsutil.def /OUT:libwsutil.dll  /IMPLIB:libwsutil.lib  ..\image\libwsutil.res  file_util.obj unicode-utils.obj mpeg-audio.obj        privileges.obj  str_util.obj            type_util.obj f:\wireshark-win64-libs-1.2\gtk2\lib\glib-2.0.lib f:\wireshark-win64-libs-1.2\gtk2\lib\gmodule-2.0.lib  f:\wireshark-win64-libs-1.2\gtk2\lib\gobject-2.0.lib
   Creating library libwsutil.lib and object libwsutil.exp
LINK : error LNK2001: unresolved external symbol [email protected]
libwsutil.dll : fatal error LNK1120: 1 unresolved externals
NMAKE : fatal error U1077: &#39;&quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\x86_amd64\link.EXE&quot;&#39; : return code &#39;0x460&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;D:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vs2008" rel="tag" title="see questions tagged &#39;vs2008&#39;">vs2008</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/6e977eaa963fb93c2a65e3e2e51962ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raphael&#39;s gravatar image" /><p><span>Raphael</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raphael has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Dec '11, 00:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8098" class="comments-container"><span id="8124"></span><div id="comment-8124" class="comment"><div id="post-8124-score" class="comment-score"></div><div class="comment-text"><p>Can you tell me which batch file did u run?</p></div><div id="comment-8124-info" class="comment-info"><span class="comment-age">(23 Dec '11, 23:16)</span> <span class="comment-user userinfo">vish</span></div></div></div><div id="comment-tools-8098" class="comment-tools"></div><div class="clear"></div><div id="comment-8098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8105"></span>

<div id="answer-container-8105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8105-score" class="post-score" title="current number of votes">0</div><span id="post-8105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Make sure <code>PROCESSOR_ARCHITECTURE</code> environment variable is set.</p><p>If not, then your SDK Win32.mak include file will assume x86 / WIN32, hence these (compile and) link problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '11, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Dec '11, 03:26</strong> </span></p></div></div><div id="comments-container-8105" class="comments-container"></div><div id="comment-tools-8105" class="comment-tools"></div><div class="clear"></div><div id="comment-8105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

