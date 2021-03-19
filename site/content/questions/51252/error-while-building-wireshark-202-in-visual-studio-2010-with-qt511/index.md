+++
type = "question"
title = "Error while building Wireshark-2.0.2 in Visual Studio 2010 with Qt5.1.1"
description = '''Hi, I am facing issue with wireshark version 2.0.2 after giving command nmake -f Makefile.nmake all Error:  cd ui/qt C:&#92;Qt&#92;Qt-5.1.1-MSVC2010-win64-ws&#92;bin&#92;qmake CONFIG+=release Wireshark.pro  Project ERROR : Unknown module in QT: multimedia NMAKE : fatal error U1077: &#x27;C:&#92;Qt&#92;Qt-5.1.1-MSVC2010-win64-ws...'''
date = "2016-03-29T04:05:00Z"
lastmod = "2016-03-29T04:30:00Z"
weight = 51252
keywords = [ "wireshark-2.0.1", "gtk", "msvc2010", "qt5" ]
aliases = [ "/questions/51252" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while building Wireshark-2.0.2 in Visual Studio 2010 with Qt5.1.1](/questions/51252/error-while-building-wireshark-202-in-visual-studio-2010-with-qt511)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51252-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am facing issue with wireshark version 2.0.2 after giving command nmake -f Makefile.nmake all</p><p><strong>Error</strong>:</p><pre><code>cd ui/qt
C:\Qt\Qt-5.1.1-MSVC2010-win64-ws\bin\qmake CONFIG+=release Wireshark.pro 
Project ERROR : Unknown module in QT: multimedia
NMAKE : fatal error U1077: &#39;C:\Qt\Qt-5.1.1-MSVC2010-win64-ws\bin\qmake.exe&#39; : return code &#39;0x3&#39;
Stop.

verify_tools and setup stage is not showing any error and warning.</code></pre><p>One more thing, with Wireshark version 1.12.3 I am able to build successfully.</p></div><div id="question-tags" class="tags-container tags">wireshark-2.0.1 gtk msvc2010 qt5</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '16, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/778ba2d594528c81b5b85780fe1d88d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chandan%20Mishra&#39;s gravatar image" /><p>Chandan Mishra<br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chandan Mishra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '16, 04:18</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51252" class="comments-container"></div><div id="comment-tools-51252" class="comment-tools"></div><div class="clear"></div><div id="comment-51252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51254"></span>

<div id="answer-container-51254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51254-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>While nmake\qmake is deprecated for Wireshark 2.x, it still mostly works for the present, but I'm not sure anyone has tried to build 2.x with VS 2010. The production releases are built with VS2013 and there were some folks building with VS2012.</p><p>I'm also uncertain about using Qt 5.1.1, the production releases are built with 5.3.2, and in addition to that I don't think that Qt provides an x64 bit build for use with VS2010.</p><p>If you need an x64 build of Wireshark, I think you'll have to move to VS2012, as Qt provides an x64 version of 5.1.1 for that version.</p><p>If you don't need an x64 build of Wireshark, then report back what happens when using VS2010 and an x86 version of Qt 5.1.1 for VS2010.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '16, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51254" class="comments-container"><span id="51281"></span><div id="comment-51281" class="comment"><div id="post-51281-score" class="comment-score"></div><div class="comment-text"><p>Thanks for details I used VS2010 and x86 version of qt 5.1.1 for x86 wireshark. With that wireshark.exe is not created after command "nmake -f Makefile.nmake all"</p><p>only Wireshrak-gtk.exe is created inside wireshrak-gtk2 folder. But build is successful.</p></div><div id="comment-51281-info" class="comment-info"><span class="comment-age">(30 Mar '16, 02:13)</span> Chandan Mishra</div></div><span id="51283"></span><div id="comment-51283" class="comment"><div id="post-51283-score" class="comment-score"></div><div class="comment-text"><p>Sounds like you don't have the correct path set for nmake (in config.nmake) to locate the Qt install, thus it doesn't build the Qt version of Wireshark.</p></div><div id="comment-51283-info" class="comment-info"><span class="comment-age">(30 Mar '16, 02:35)</span> grahamb ♦</div></div><span id="51287"></span><div id="comment-51287" class="comment"><div id="post-51287-score" class="comment-score"></div><div class="comment-text"><p>It have correct path, while building wireshark log show:</p><p>cd ui/qt C:\Qt\Qt-5.1.1\5.1.1\msvc2010\bin\qmake CONFG+=release Wireshark.pro</p><p>In verify_tools also shows same path.</p></div><div id="comment-51287-info" class="comment-info"><span class="comment-age">(30 Mar '16, 04:49)</span> Chandan Mishra</div></div></div><div id="comment-tools-51254" class="comment-tools"></div><div class="clear"></div><div id="comment-51254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

