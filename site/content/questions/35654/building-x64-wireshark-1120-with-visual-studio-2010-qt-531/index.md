+++
type = "question"
title = "Building x64 Wireshark 1.12.0 with Visual Studio 2010, QT 5.3.1"
description = '''I&#x27;m trying to build a 64-bit version of Wireshark 1.12.0 with Visual Studio 2012. I&#x27;ve installed  qt-opensource-windows-x86-msvc2010_opengl-5.3.1.exe and I think that&#x27;s where the problem lies. I get the error below. I didn&#x27;t see a 64-bit version of QT 5.3.1 for VS2010. Please tell me I don&#x27;t have to...'''
date = "2014-08-21T11:45:00Z"
lastmod = "2014-08-21T14:30:00Z"
weight = 35654
keywords = [ "5.3.1", "1.12.0", "qt", "vs2010", "x64" ]
aliases = [ "/questions/35654" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Building x64 Wireshark 1.12.0 with Visual Studio 2010, QT 5.3.1](/questions/35654/building-x64-wireshark-1120-with-visual-studio-2010-qt-531)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35654-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to build a 64-bit version of Wireshark 1.12.0 with Visual Studio 2012. I've installed qt-opensource-windows-x86-msvc2010_opengl-5.3.1.exe and I think that's where the problem lies. I get the error below. I didn't see a 64-bit version of QT 5.3.1 for VS2010. Please tell me I don't have to build QT.</p><p>Qt5Widgets.lib(Qt5Widgets.dll) : fatal error LNK1112: module machine type 'X86' conflicts with target machine type 'x64' NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\x86_amd64\link.EXE"' : return code '0x458' Stop. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\nmake.EXE"' : return code '0x2' Stop.</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags">5.3.1 1.12.0 qt vs2010 x64</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '14, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-35654" class="comments-container"><span id="35657"></span><div id="comment-35657" class="comment"><div id="post-35657-score" class="comment-score"></div><div class="comment-text"><p>The official GUI for Wireshark 1.12 stays GTK as the Qt port is an ongoing work done in master branch (aka Wireshark 1.99). It lacks a lot of features yet so it's probably better to stick to GK. But if you really want to build qtshark, as you said there is no official x64 Digia package for MSVC2010. You can still find an old 5.1.1 x64 package compiled for MSVC2010 here: <a href="http://anonsvn.wireshark.org/viewvc/tags/2014-07-27/packages/Qt-5.1.1-MSVC2010-win64-ws.zip?view=co&amp;revision=407&amp;root=Wireshark-win64-libs">http://anonsvn.wireshark.org/viewvc/tags/2014-07-27/packages/Qt-5.1.1-MSVC2010-win64-ws.zip?view=co&amp;revision=407&amp;root=Wireshark-win64-libs</a></p></div><div id="comment-35657-info" class="comment-info"><span class="comment-age">(21 Aug '14, 12:20)</span> Pascal Quantin</div></div></div><div id="comment-tools-35654" class="comment-tools"></div><div class="clear"></div><div id="comment-35654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35661"></span>

<div id="answer-container-35661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35661-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per the comment from @Pascal Quantin, as we move forward with the QT port, the "normal" toolchain on Windows will be Visual Studio 2013. Digia have already dropped VS2012 builds and are likely to do the same with VS2010 builds, even for x86, so you should try to move onto VS2013.</p><p>The automated buildbots for Windows are now compiling with VS2013.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '14, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Aug '14, 14:30</p></div></div><div id="comments-container-35661" class="comments-container"><span id="35777"></span><div id="comment-35777" class="comment"><div id="post-35777-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I wasn't quite clear on that. What does that mean for the 1.12 series? Will it use GTK by default and the next stable series (1.14 ?) use QT.</p><p>Brian</p></div><div id="comment-35777-info" class="comment-info"><span class="comment-age">(26 Aug '14, 13:39)</span> brwiese</div></div><span id="35778"></span><div id="comment-35778" class="comment"><div id="post-35778-score" class="comment-score"></div><div class="comment-text"><p>Yes, for 1.12 GTK is the default and some binary installs will also include the QT version, i.e. the wireshark binary will be GTK, and the qtshark binary wil be QT.</p><p>Post 1.12, 1.99 and 2.0 will use QT as the default, so the wireshark binary will be QT and (probably) gtkshark will be GTK.</p></div><div id="comment-35778-info" class="comment-info"><span class="comment-age">(26 Aug '14, 14:19)</span> grahamb ♦</div></div></div><div id="comment-tools-35661" class="comment-tools"></div><div class="clear"></div><div id="comment-35661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

