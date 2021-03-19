+++
type = "question"
title = "How to fix &quot;qt not available&quot; issue when compiling Wireshark on CentOS from source"
description = '''Hello, I tried to install Wireshark to my CentOS machine (offline, no internet connection). I extracted the tar file, then run ./configure and got the following error: checking for Qt5Core - version &amp;gt;= 5.0.0... no checking for QtCore - version &amp;gt;= 4.7.0... no configure: error: Qt is not availab...'''
date = "2016-08-03T08:35:00Z"
lastmod = "2016-08-11T06:36:00Z"
weight = 54560
keywords = [ "compile", "centos", "wireshark" ]
aliases = [ "/questions/54560" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to fix "qt not available" issue when compiling Wireshark on CentOS from source](/questions/54560/how-to-fix-qt-not-available-issue-when-compiling-wireshark-on-centos-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54560-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I tried to install Wireshark to my CentOS machine (offline, no internet connection). I extracted the tar file, then run ./configure and got the following error:</p><p>checking for Qt5Core - version &gt;= 5.0.0... no checking for QtCore - version &gt;= 4.7.0... no</p><p>configure: error: Qt is not available</p><p>I then downloaded Qt 5.7.0 and installed on my machine and run configure again but still get the same error message.</p><p>Can you please help me resolve the issue?</p></div><div id="question-tags" class="tags-container tags">compile centos wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '16, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/7f3ba631907d7294c6b3cb4a6493acc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j52652&#39;s gravatar image" /><p>j52652<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j52652 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Aug '16, 09:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54560" class="comments-container"><span id="54561"></span><div id="comment-54561" class="comment"><div id="post-54561-score" class="comment-score"></div><div class="comment-text"><p>What version of Centos and what version of source are you using (or git tag\branch)?</p></div><div id="comment-54561-info" class="comment-info"><span class="comment-age">(03 Aug '16, 09:49)</span> grahamb ♦</div></div><span id="54562"></span><div id="comment-54562" class="comment"><div id="post-54562-score" class="comment-score"></div><div class="comment-text"><p>I am running CentOS 6.3 and the Wireshark version I tried to install was 2.0.5</p></div><div id="comment-54562-info" class="comment-info"><span class="comment-age">(03 Aug '16, 09:58)</span> j52652</div></div><span id="54563"></span><div id="comment-54563" class="comment"><div id="post-54563-score" class="comment-score"></div><div class="comment-text"><p>"downloaded Qt 5.7.0 and installed on my machine" but were these the development packages?</p></div><div id="comment-54563-info" class="comment-info"><span class="comment-age">(03 Aug '16, 12:11)</span> Jaap ♦</div></div></div><div id="comment-tools-54560" class="comment-tools"></div><div class="clear"></div><div id="comment-54560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54739"></span>

<div id="answer-container-54739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Jaap's comment is most likely the problem: you need the development packages too. According to the shell script <code>tools/install_rpms_for_devel.sh</code> these are the packages you'll need to compile with Qt:</p><pre><code>qt-devel gcc-c++ qt5-qtbase-devel qt5-qtmultimedia-devel</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '16, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54739" class="comments-container"></div><div id="comment-tools-54739" class="comment-tools"></div><div class="clear"></div><div id="comment-54739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

