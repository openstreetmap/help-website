+++
type = "question"
title = "Create a Wireshark Windows Installer"
description = '''I am looking this page: https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin I read the following chapter 2.2.16. Optional: Create a Wireshark Installer to create a Wireshark installer.  However, I get an error that saying: File: &quot;....&#92;wireshark-qt-release*qm&quot; -&amp;gt; no fi...'''
date = "2014-11-25T23:02:00Z"
lastmod = "2014-11-26T05:26:00Z"
weight = 38153
keywords = [ "installer", "wireshark" ]
aliases = [ "/questions/38153" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Create a Wireshark Windows Installer](/questions/38153/create-a-wireshark-windows-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking this page: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin</a></p><p>I read the following chapter 2.2.16. Optional: Create a Wireshark Installer to create a Wireshark installer.</p><p>However, I get an error that saying:</p><p>File: "....\wireshark-qt-release*qm" -&gt; no files found</p><p>Then it is giving and Nmake: fatal error U1077:</p><p>I can build wireshark and also work with it, however I cannot make an installer.</p><p>What am I missing? How can I put there that qm files that the script wants?</p></div><div id="question-tags" class="tags-container tags">installer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '14, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p>BirolCapa<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '14, 01:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38153" class="comments-container"></div><div id="comment-tools-38153" class="comment-tools"></div><div class="clear"></div><div id="comment-38153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38155"></span>

<div id="answer-container-38155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38155-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are building without Qt support comment out these lines in packaging/nsis/Makefile.nmake</p><blockquote><p>!IF EXIST("....\wireshark-qt-release\wireshark.exe")</p><p>/DQT_DIR="....\wireshark-qt-release" \</p><p>!ENDIF</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '14, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '14, 01:18</p></div></div><div id="comments-container-38155" class="comments-container"><span id="38157"></span><div id="comment-38157" class="comment"><div id="post-38157-score" class="comment-score"></div><div class="comment-text"><p>Anders thanks for answer but, I am building with QT. I solve this issue as following. I copy files below and rerun all process:</p><p>wireshark_de.qm</p><p>wireshark_en.qm</p><p>wireshark_fr.qm</p><p>wireshark_it.qm</p><p>wireshark_ja_JP.qm</p><p>wireshark_pl.qm</p><p>wireshark_zh_CN.qm</p><p>It works. I managed to get an installer file of Wireshark. However, I do copy these files by hand. So, my problem is why do I need to copy them by hand. Why do not script does that process?</p></div><div id="comment-38157-info" class="comment-info"><span class="comment-age">(26 Nov '14, 01:38)</span> BirolCapa</div></div></div><div id="comment-tools-38155" class="comment-tools"></div><div class="clear"></div><div id="comment-38155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38165"></span>

<div id="answer-container-38165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38165-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it does work for you. The wireshark_*.qm files are the binary language files produced when compiling the qt version and are linked into the Wireshark.exe binary so NSIS doesn't know (or need to) know about them.</p><p>What NSIS is looking for though, is the qt standard .qm files, e.g. qt_*.qm, that are copied into the wireshark-qt-release directory by the qt tool <code>windeployqt</code> which is run as part of the build process. There have been problems with the this tool in versions of QT &lt; 5.3.</p><p>What version of QT are you building with?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '14, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38165" class="comments-container"><span id="38166"></span><div id="comment-38166" class="comment"><div id="post-38166-score" class="comment-score"></div><div class="comment-text"><p>I am using Qt-5.1.1-MSVC2010-win64-ws version.</p><p>I can debug both QT and GTK variants of Wireshark Visual Studio 2010. When I debug Wireshark with Visual Studio I see that above files are here: ..\build\ui\qt</p><p>Today I decided to make a setup file.Then I build Wireshark as told in <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html#idp442305884">https://www.wireshark.org/docs/wsdg_html_chunked/ChDissectAdd.html#idp442305884</a> While I was trying to create a setup file I encountered with this problem. But I remember that these files are already in ..\build\ui\qt. I copied it. And successfully the setup script worked well and now setup also works well.</p><p>But I want to learn the proper way not the workaround.</p></div><div id="comment-38166-info" class="comment-info"><span class="comment-age">(26 Nov '14, 05:33)</span> BirolCapa</div></div><span id="38170"></span><div id="comment-38170" class="comment"><div id="post-38170-score" class="comment-score">1</div><div class="comment-text"><p>For QT-5.1.1, windeployqt doesn't exist, so there has to be an explicit copy of the files. This should be done in the Wireshark.pro qmake file. Unfortunately it isn't, and unlikely to be so as there is no further Wireshark QT dev planned with VS2010 and QT &lt; 5.3.</p><p>Is there any reason you can't move to VS2013 (the Community Edition is free) and also move up to at least QT 5.3?</p></div><div id="comment-38170-info" class="comment-info"><span class="comment-age">(26 Nov '14, 06:35)</span> grahamb ♦</div></div><span id="38223"></span><div id="comment-38223" class="comment"><div id="post-38223-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer Graham. No actually, I am a newbie, therefore I do all steps that written at following link: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupCygwin</a> Thats actually why I use Vs2010 and QT &lt; 5.3. But now I get a little bit experience, so I think I can move to VS2013. But I am afraid that if I become a newbie again when I move to VS2013 :)</p></div><div id="comment-38223-info" class="comment-info"><span class="comment-age">(27 Nov '14, 22:25)</span> BirolCapa</div></div><span id="38229"></span><div id="comment-38229" class="comment"><div id="post-38229-score" class="comment-score"></div><div class="comment-text"><p>I have changes planned for the Dev Guide to move up to VS2013, but haven't quite finished them yet. See my answer to <a href="https://ask.wireshark.org/questions/38124/error-building-wireshark-windows">this</a> question for how I do it.</p></div><div id="comment-38229-info" class="comment-info"><span class="comment-age">(28 Nov '14, 01:54)</span> grahamb ♦</div></div></div><div id="comment-tools-38165" class="comment-tools"></div><div class="clear"></div><div id="comment-38165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

