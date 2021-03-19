+++
type = "question"
title = "uic.exe about_dialog.ui fatal error (0xc0000135)"
description = '''Hi need help to figure out how to resolve the fatal error with uic.exe for about_dialog.ui when build wireshark on windows target. Please see the logs below :  xcopy &quot;.&#92;profiles&#92;Classic&#92;colorfilters&quot; wireshark-gtk2&#92;profiles&#92;Classic /d .&#92;profiles&#92;Classic&#92;colorfilters 1 File(s) copied  cd ui/qt  C:&#92;Qt...'''
date = "2015-05-29T11:20:00Z"
lastmod = "2015-05-31T01:49:00Z"
weight = 42747
keywords = [ "windows", "win32", "error", "qt", "build" ]
aliases = [ "/questions/42747" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [uic.exe about\_dialog.ui fatal error (0xc0000135)](/questions/42747/uicexe-about_dialogui-fatal-error-0xc0000135)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42747-score" class="post-score" title="current number of votes">0</div><span id="post-42747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>need help to figure out how to resolve the fatal error with uic.exe for about_dialog.ui when build wireshark on windows target. Please see the logs below :</p><pre><code>    xcopy &quot;.\profiles\Classic\colorfilters&quot; wireshark-gtk2\profiles\Classic /d
.\profiles\Classic\colorfilters
1 File(s) copied
    cd ui/qt
    C:\Qt\Qt5.3.2\5.3\msvc2013_opengl\bin\qmake CONFIG+=release QtShark.pro
    nmake

Microsoft (R) Program Maintenance Utility Version 10.00.30319.01
Copyright (C) Microsoft Corporation.  All rights reserved.

    C:\Qt\Qt5.3.2\5.3\msvc2013_opengl\bin\uic.exe about_dialog.ui -o ui_about_dialog.h
NMAKE : fatal error U1077: &#39;C:\Qt\Qt5.3.2\5.3\msvc2013_opengl\bin\uic.exe&#39; : return code &#39;0xc0000135&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.

C:\Development\wireshark-1.12.5&gt;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-win32" rel="tag" title="see questions tagged &#39;win32&#39;">win32</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '15, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/27958ba63986f94e0bae2a8e4a96c290?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PraveenDua&#39;s gravatar image" /><p><span>PraveenDua</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PraveenDua has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 May '15, 14:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42747" class="comments-container"></div><div id="comment-tools-42747" class="comment-tools"></div><div class="clear"></div><div id="comment-42747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42752"></span>

<div id="answer-container-42752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42752-score" class="post-score" title="current number of votes">0</div><span id="post-42752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's a failure in the uic tool from the qt development toolkit.</p><p>Currently all the Wireshark 12.x buildbots are using QT 5.1.1 with MSVC2010. I don't think the MSVC version is the issue here, more likely to be the QT version.</p><p>Do you really need the QT version of Wireshark 1.12.5, it's not very functional, the development version is much better? Can you try a different version of QT? If you can move onwards with Wireshark, you might want to try building the development version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '15, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42752" class="comments-container"><span id="42754"></span><div id="comment-42754" class="comment"><div id="post-42754-score" class="comment-score"></div><div class="comment-text"><p>i dont need to have the Qt version. how do i target to build the development version instead of Qt version ?</p></div><div id="comment-42754-info" class="comment-info"><span class="comment-age">(29 May '15, 16:08)</span> <span class="comment-user userinfo">PraveenDua</span></div></div><span id="42755"></span><div id="comment-42755" class="comment"><div id="post-42755-score" class="comment-score"></div><div class="comment-text"><p>also, in the meantime, i updated to visual studio 2013 and now i get the error :</p><p><code> C:\Development\wireshark-1.12.5\config.h(272) : fatal error C1189: #error :  Your MSVC_VARIANT setting in config.nmake doesn't match the MS compiler version! (.\moc_time_shift_dialog.cpp) moc_wireshark_application.cpp _MSC_VER is:1800 but required is:1600 C:\Development\wireshark-1.12.5\config.h(272) : fatal error C1189: #error :  Your MSVC_VARIANT setting in config.nmake doesn't match the MS compiler version! (.\moc_wireshark_application.cpp) NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\cl.EXE"' : return code '0x2' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.EXE"' : return code '0x2' Stop.</code></p><p>This is using visual studio 2013 :</p><p><code> C:\Development\wireshark-1.12.5&gt;set vi VisualStudioVersion=12.0</code></p></div><div id="comment-42755-info" class="comment-info"><span class="comment-age">(29 May '15, 17:02)</span> <span class="comment-user userinfo">PraveenDua</span></div></div><span id="42756"></span><div id="comment-42756" class="comment"><div id="post-42756-score" class="comment-score"></div><div class="comment-text"><p>The error is because of the setting of MSVC_VARIANT in your copy config.nmake. For VS2013 it should be set to 1800.</p><p>I'm not sure if it works correctly in 1.12.x, but in the dev sources you shouldn't require any changes at all in config.nmake to build with VS2013.</p><p>The development version is in the git "master" branch. I guess you are using a tarball of the sources, it's much easier to use git as you can then keep track of any local modifications as well.</p><p>Note that in the development version, QT is the primary UI, the GTK version is being deprecated.</p></div><div id="comment-42756-info" class="comment-info"><span class="comment-age">(30 May '15, 00:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="42767"></span><div id="comment-42767" class="comment"><div id="post-42767-score" class="comment-score"></div><div class="comment-text"><p>Since i now have both VS2010 and 2013 - it is somehow picking up MSVC10 as the compiler. Not clear why because all p[ath variables are correctly pointing to VS2013</p></div><div id="comment-42767-info" class="comment-info"><span class="comment-age">(30 May '15, 15:58)</span> <span class="comment-user userinfo">PraveenDua</span></div></div><span id="42770"></span><div id="comment-42770" class="comment"><div id="post-42770-score" class="comment-score"></div><div class="comment-text"><p>Have you cleaned the build since switching compilers, e.g. <code>nmake -f makefile.nmake distclean</code>?</p><p>Double check any changes to config.nmake.</p></div><div id="comment-42770-info" class="comment-info"><span class="comment-age">(31 May '15, 01:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42752" class="comment-tools"></div><div class="clear"></div><div id="comment-42752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

