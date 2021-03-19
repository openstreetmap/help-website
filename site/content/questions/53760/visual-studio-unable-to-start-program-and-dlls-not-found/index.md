+++
type = "question"
title = "Visual Studio Unable to start program and DLLs not found"
description = '''Hi, trying the first time to start Wireshark with Visual Studio 2013 to be able to debug a dissector, I ran into the following issue by just pressing &quot;Play&quot; and running the debugger: Unable to start program &quot;filepath&quot; Access is denied. For a pro the reason might be clear, however I struggled a bit. ...'''
date = "2016-07-01T01:15:00Z"
lastmod = "2016-07-01T02:50:00Z"
weight = 53760
keywords = [ "debug", "visual-studio" ]
aliases = [ "/questions/53760" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Visual Studio Unable to start program and DLLs not found](/questions/53760/visual-studio-unable-to-start-program-and-dlls-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53760-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, trying the first time to start Wireshark with Visual Studio 2013 to be able to debug a dissector, I ran into the following issue by just pressing "Play" and running the debugger: Unable to start program "filepath" Access is denied.</p><p>For a pro the reason might be clear, however I struggled a bit. What you need to do is to set the startup project to a project in the Executable folder of the solution. I hope this statement is correct. Maybe this could be added in the documentation under 4.6.7.1. Would have saved me some time and since I don't have admin rights the phrase "Access is denied" led me on the wrong path.</p><p>Now I can start the debugger an run Wireshark, however now I get several errors from xyz.exe that either libwiretab.dll or libwsutil.dll is missing. When I click "ok" Wireshark starts fine and for playing with a pcap file it does not seem to have consequences. Still I would like to now what I am doing wrong and how I would be able to have "clean" start.</p><p>Best regards, Mike</p></div><div id="question-tags" class="tags-container tags">debug visual-studio</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '16, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/c288ec16e3d47bc1e1602e5b4e283949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebo&#39;s gravatar image" /><p>mikethebo<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '16, 03:25</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53760" class="comments-container"></div><div id="comment-tools-53760" class="comment-tools"></div><div class="clear"></div><div id="comment-53760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53764"></span>

<div id="answer-container-53764" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue of not setting the start-up project for debugging is a somewhat basic Visual Studio usage issue when there are multiple executables in a project. I'll look into adding a note into the docs though.</p><p>What is "xyz.exe"? Setting Wireshark.exe as the startup project works for me, although for reasons currently unknown, the VS IDE considers a build from the command line as "incomplete" and would like to build some items. This can either be ignored or allow the IDE to build as you see fit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53764" class="comments-container"><span id="53771"></span><div id="comment-53771" class="comment"><div id="post-53771-score" class="comment-score"></div><div class="comment-text"><p>Ok sorry, I have been a little lazy. xyz.exe is only a placeholder for several exes, that give me an error message during start. After starting Wireshark in Visual Studio in debug mode, by changing the start-up project it works, but I get new error messages of the same kind:</p><pre><code>xyz.exe - System Error  
The Programm cant&#39; start because libwiretab.dll is missing from your computer. Try reinstalling the programm to fix this problem.</code></pre><p>xyz.exe is a placeholder for:<br />
androiddumb.exe<br />
ciscodump.exe<br />
randpktdump.exe<br />
sshdump.exe</p><p>There is an error message each for missing libwiretab.dll and libwsutil.dll. I didn't want to post the same error messages 8 times ;-). So I thought I'd go for a variable.</p><p>br Mike</p></div><div id="comment-53771-info" class="comment-info"><span class="comment-age">(01 Jul '16, 08:39)</span> mikethebo</div></div><span id="53772"></span><div id="comment-53772" class="comment"><div id="post-53772-score" class="comment-score"></div><div class="comment-text"><p>OK, I've just retested and also see that. These are the extcap executables, so I think there's a DLL load issue in VS such that these executables can't load with the required DLL's. Just running Wireshark.exe from the run\RelWithDebInfo directory works fine. If you don't need the extcap items, the issue can be ignored. I'll have a look to see if anything can be done here.</p></div><div id="comment-53772-info" class="comment-info"><span class="comment-age">(01 Jul '16, 08:49)</span> grahamb ♦</div></div><span id="53774"></span><div id="comment-53774" class="comment"><div id="post-53774-score" class="comment-score">1</div><div class="comment-text"><p>I've found that if I add the location of the Wireshark executables directory to the path before starting Visual Studio, then starting wireshark in the debugger doesn't generate those errors, e.g.</p><pre><code>set PATH=%PATH%;path\to\run\RelWithDebInfo
wireshark.sln</code></pre><p>I did try modifying the wireshark project properties in VS, Debugging -&gt; Working Directory to the same location, but that didn't seem to change anything.</p></div><div id="comment-53774-info" class="comment-info"><span class="comment-age">(01 Jul '16, 09:10)</span> grahamb ♦</div></div><span id="53804"></span><div id="comment-53804" class="comment"><div id="post-53804-score" class="comment-score"></div><div class="comment-text"><p>Works for me. Thank you!</p></div><div id="comment-53804-info" class="comment-info"><span class="comment-age">(04 Jul '16, 07:14)</span> mikethebo</div></div></div><div id="comment-tools-53764" class="comment-tools"></div><div class="clear"></div><div id="comment-53764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

