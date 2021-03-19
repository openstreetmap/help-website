+++
type = "question"
title = "Create a Wireshark Installer Without Including QT Based Version"
description = '''Hello all,  Is it possible to create a Wireshark installer without including QT based version? In other words, when we create the setup file, setup will only install the GTK version. Is that possible?'''
date = "2015-11-23T22:01:00Z"
lastmod = "2015-11-24T02:04:00Z"
weight = 47907
keywords = [ "installer", "qt", "nsis" ]
aliases = [ "/questions/47907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create a Wireshark Installer Without Including QT Based Version](/questions/47907/create-a-wireshark-installer-without-including-qt-based-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>Is it possible to create a Wireshark installer without including QT based version? In other words, when we create the setup file, setup will only install the GTK version. Is that possible?</p></div><div id="question-tags" class="tags-container tags">installer qt nsis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p>BirolCapa<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div></div><div id="comments-container-47907" class="comments-container"><span id="47910"></span><div id="comment-47910" class="comment"><div id="post-47910-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-47910-info" class="comment-info"><span class="comment-age">(24 Nov '15, 01:44)</span> Jaap ♦</div></div><span id="47911"></span><div id="comment-47911" class="comment"><div id="post-47911-score" class="comment-score"></div><div class="comment-text"><p>I am using Wireshark development version. I am directly creating installer from master branch. I am trying to create setups for Windows 7 (32 bit) and for Windows 7 (64 bit).</p><p>When I comment following lines at ..\packaging\nsis\CMakeLists.txt:</p><p>if(BUILD_wireshark AND QT_FOUND) set (QT_DIR "\${STAGING_DIR}") endif()</p><p>I think it only builds old legacy version? Am I missing any other points?</p></div><div id="comment-47911-info" class="comment-info"><span class="comment-age">(24 Nov '15, 01:51)</span> BirolCapa</div></div></div><div id="comment-tools-47907" class="comment-tools"></div><div class="clear"></div><div id="comment-47907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47912"></span>

<div id="answer-container-47912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47912-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may need to hack at the packaging\nsis scripts a bit. Installing without the Qt version isn't supported so you're on your own really.</p><p>You do know that the GTK version is likely to be dropped completely for Windows (and OSX) in the 2.2 release, so by not updating your work for Qt now, you will eventually hit a wall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '15, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47912" class="comments-container"><span id="47913"></span><div id="comment-47913" class="comment"><div id="post-47913-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response Graham, I am aware of this situation.</p><p>For the current master branch, end users are having a little bit trouble with the QT based version, because it crashes time to time.</p><p>(I am creating setup from master branch since latest stable release does not include all changes at Profinet plugin which are written by me. That's why I need GTK based version only for this temporary time.</p></div><div id="comment-47913-info" class="comment-info"><span class="comment-age">(24 Nov '15, 02:09)</span> BirolCapa</div></div><span id="47916"></span><div id="comment-47916" class="comment"><div id="post-47916-score" class="comment-score"></div><div class="comment-text"><p>The current 2.1 automated builds include both GTK and Qt and the Profinet changes, aren't they useful for your users?</p><p>Also, please encourage users who have issues with the Qt version to report them so that hopefully the problems can be fixed.</p></div><div id="comment-47916-info" class="comment-info"><span class="comment-age">(24 Nov '15, 03:18)</span> grahamb ♦</div></div><span id="47922"></span><div id="comment-47922" class="comment"><div id="post-47922-score" class="comment-score"></div><div class="comment-text"><p>What is the difference between following:</p><ol><li>I get the latest master branch, and create a setup from that</li><li>I get the setup of the automated build</li></ol><p>Which one is much more stable?</p><p>Because, as far as I understand, every code firstly goes to automated builds before they are merged to master branch?</p></div><div id="comment-47922-info" class="comment-info"><span class="comment-age">(24 Nov '15, 04:12)</span> BirolCapa</div></div><span id="47923"></span><div id="comment-47923" class="comment"><div id="post-47923-score" class="comment-score"></div><div class="comment-text"><p>They're both the same, automated builds are attempted from the master branch after every commit to master. If the (limited) tests succeed then the installer is uploaded to the web site for download by others.</p></div><div id="comment-47923-info" class="comment-info"><span class="comment-age">(24 Nov '15, 04:22)</span> grahamb ♦</div></div></div><div id="comment-tools-47912" class="comment-tools"></div><div class="clear"></div><div id="comment-47912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

