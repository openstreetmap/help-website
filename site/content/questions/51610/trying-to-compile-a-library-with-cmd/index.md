+++
type = "question"
title = "[closed] Trying to compile a library with cmd"
description = '''I&#x27;ve been following a guido to compile a library into MATLAB. I&#x27;ve installer visualstudio14 so that i have a C++ compiler, then i used the vsvarsxx.bat to use the vs14 compiler with the cmd. For last, i went to the folder i want to compile and tiped nmake nmake -f Makefile.win clean all. I used a fo...'''
date = "2016-04-12T11:36:00Z"
lastmod = "2016-04-12T11:36:00Z"
weight = 51610
keywords = [ "pronto", "prompt", "cmd", "command", "matlab" ]
aliases = [ "/questions/51610" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Trying to compile a library with cmd](/questions/51610/trying-to-compile-a-library-with-cmd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been following a guido to compile a library into MATLAB. I've installer visualstudio14 so that i have a C++ compiler, then i used the vsvarsxx.bat to use the vs14 compiler with the cmd. For last, i went to the folder i want to compile and tiped nmake nmake -f Makefile.win clean all.</p><p>I used a following commands:</p><p>cd C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin vsvars32.bat cd C:\Users\Rafa\Desktop\estágio\PRoNTo_v2.0\PRoNTo_v2.0\machines\libsvm-3.20 nmake -f Makefile.win clean all</p><p>It runs whithout problem until i reach the final command. It pops up the following error: erase /Q *.obj windows. Could Not Find C:\Users\Rafa\Desktop\estágio\PRoNTo_v2.0\PRoNTo_v2.0\machines\libsvm-3.20*.obj cl.exe /nologo /O2 /EHsc /I. /D _WIN32 /D _CRT_SECURE_NO_DEPRECATE -c svm.cpp 'cl.exe' is not recognized as an internal or external command, operable program or batch file. NMAKE : fatal error U1077: 'cl.exe' : return code '0x1' Stop.</p><p>I have a Makefile.win: 03/25/2016 09:25 PM 732 Makefile 03/25/2016 09:25 PM 1,084 Makefile.win</p><p>I dont understand why that error pops up. Can somebody help me please ?</p></div><div id="question-tags" class="tags-container tags">pronto prompt cmd command matlab</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/3ab3796783dd789495703629396d48c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rafa%20Ramos&#39;s gravatar image" /><p>Rafa Ramos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rafa Ramos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 12 Apr '16, 12:05</p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p></div></div><div id="comments-container-51610" class="comments-container"></div><div id="comment-tools-51610" class="comment-tools"></div><div class="clear"></div><div id="comment-51610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Compilation of libsvm is not related to Wireshark at all. I suggest contacting them instead." by Pascal Quantin 12 Apr '16, 12:05

</div>

</div>

</div>

