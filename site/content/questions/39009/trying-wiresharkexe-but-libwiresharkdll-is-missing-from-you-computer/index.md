+++
type = "question"
title = "Trying Wireshark.exe, but &quot;libwireshark.dll is missing from you computer&quot;"
description = '''I have been following the steps for building x32 Wireshark for Windows from source, and things had been going relatively well. I got to the &quot;nmake -f Makefile.nmake all&quot; step. However, it quit with an error after being unable to find a path (I no longer have this error). I went and made sure all my ...'''
date = "2015-01-09T11:52:00Z"
lastmod = "2015-01-10T04:44:00Z"
weight = 39009
keywords = [ "windows", "build", "missing" ]
aliases = [ "/questions/39009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying Wireshark.exe, but "libwireshark.dll is missing from you computer"](/questions/39009/trying-wiresharkexe-but-libwiresharkdll-is-missing-from-you-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been following the steps for building x32 Wireshark for Windows from source, and things had been going relatively well. I got to the "nmake -f Makefile.nmake all" step. However, it quit with an error after being unable to find a path (I no longer have this error). I went and made sure all my environment variables were correctly set, and that I had verified my tools (there was a long gap between when I last did these things and when I built.) Then, I tried to build again, and it seemed to complete successfully. There were no error messages. However, when I tried to run the Wireshark.exe file, it gave me an error message.</p><p>"The program can't start because libwireshark.dll is missing from your computer. Try reinstalling the program to fix this problem."</p><p>Which program is that, exactly? How do I fix this? I've tried building again, and I didn't have any errors in the build process.</p></div><div id="question-tags" class="tags-container tags">windows build missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '15, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p>mehubb985<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39009" class="comments-container"></div><div id="comment-tools-39009" class="comment-tools"></div><div class="clear"></div><div id="comment-39009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39020"></span>

<div id="answer-container-39020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39020-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You haven't followed the instructions completely. After building you do have Wireshark.exe at the top-level of the source tree, but it can't be run from there as it won't find all the required DLL's, e.g. libwireshark.dll.</p><p>See the Dev Guide Sect 3.6.2 <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html#ChSrcRunFirstTimeWin32">Run Generated Wireshark, Win32</a>, you should cd into wireshark-gtk2 (or wireshark-qt-release for the new QT version), and run it from there, where all the DLL's have been copied to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39020" class="comments-container"></div><div id="comment-tools-39020" class="comment-tools"></div><div class="clear"></div><div id="comment-39020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

