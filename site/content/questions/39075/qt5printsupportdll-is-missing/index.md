+++
type = "question"
title = "Qt5PrintSupport.dll is missing"
description = '''I&#x27;m building Wireshark for Windows from source, and have run into a problem. I previously was trying to run the .exe file from the build directory, which did not work. It told me I was missing a file. Now I&#x27;ve gone to the wireshark-gtk2 directory, where I&#x27;m supposed to, and that problem cleared up. ...'''
date = "2015-01-12T05:38:00Z"
lastmod = "2015-01-12T06:20:00Z"
weight = 39075
keywords = [ "windows", "qtprintsupport", "qt", "wireshark" ]
aliases = [ "/questions/39075" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Qt5PrintSupport.dll is missing](/questions/39075/qt5printsupportdll-is-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39075-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm building Wireshark for Windows from source, and have run into a problem. I previously was trying to run the .exe file from the build directory, which did not work. It told me I was missing a file. Now I've gone to the wireshark-gtk2 directory, where I'm supposed to, and that problem cleared up. However, now it is telling me "The program can't start because Qt5PrintSupport.dll is missing from your computer. Try reinstalling the program to fix this problem."</p><p>I've checked and the file truly doesn't seem to be there. Why is this? What step did I miss to not have this file (or is it located somewhere else that my PATH can't see?) What do I do?</p></div><div id="question-tags" class="tags-container tags">windows qtprintsupport qt wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '15, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p>mehubb985<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39075" class="comments-container"><span id="44174"></span><div id="comment-44174" class="comment"><div id="post-44174-score" class="comment-score"></div><div class="comment-text"><p>I just saw the same problem. My solution was to build and run the NSIS packager (which includes the actions of windeployqt?). After that the DLLs were all found when I ran my own build of wireshark.exe</p></div><div id="comment-44174-info" class="comment-info"><span class="comment-age">(15 Jul '15, 07:13)</span> MartinM</div></div></div><div id="comment-tools-39075" class="comment-tools"></div><div class="clear"></div><div id="comment-39075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39076"></span>

<div id="answer-container-39076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When building on Windows, to run the built versions you must run from the special directories that contain all the 3rd party DLL's. For the new QT based version, use wireshark-qt-release\Wireshark.exe and for the older GTK based version use wireshark-gtk2\Wireshark-gtk.exe. Note the different program names.</p><p>As to your issue, I can't think of any reason why the gtk version would require a QT5 DLL. Are you sure you're running Wirehark-gtk.exe?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '15, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39076" class="comments-container"><span id="39077"></span><div id="comment-39077" class="comment"><div id="post-39077-score" class="comment-score"></div><div class="comment-text"><p>When I got this error, I was running the wireshark-qt-release\Wireshark.exe from the wirehsark-gtk2 directory. Running the Wireshark-gtk.exe from that directory seems to work. Running the wireshark-qt-release\Wireshark.exe file from the wireshark-qt-release directory had a similar error but with a different dll file. Not sure why that one didn't work.</p></div><div id="comment-39077-info" class="comment-info"><span class="comment-age">(12 Jan '15, 06:44)</span> mehubb985</div></div><span id="39078"></span><div id="comment-39078" class="comment"><div id="post-39078-score" class="comment-score"></div><div class="comment-text"><p>What version of Visual Studio and QT are you using?</p></div><div id="comment-39078-info" class="comment-info"><span class="comment-age">(12 Jan '15, 06:58)</span> grahamb ♦</div></div><span id="39079"></span><div id="comment-39079" class="comment"><div id="post-39079-score" class="comment-score"></div><div class="comment-text"><p>2010 for Visual Studio, 5.3 for QT</p></div><div id="comment-39079-info" class="comment-info"><span class="comment-age">(12 Jan '15, 07:00)</span> mehubb985</div></div><span id="39080"></span><div id="comment-39080" class="comment"><div id="post-39080-score" class="comment-score"></div><div class="comment-text"><p>For QT 5.3 the build should be using the QT windeployqt tool to copy all the required QT components into wireshark-qt-release, so I can't think what's gone wrong there.</p><p>What is the exact error when running wireshark-qt-release\Wireshark.exe?</p></div><div id="comment-39080-info" class="comment-info"><span class="comment-age">(12 Jan '15, 07:27)</span> grahamb ♦</div></div></div><div id="comment-tools-39076" class="comment-tools"></div><div class="clear"></div><div id="comment-39076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

