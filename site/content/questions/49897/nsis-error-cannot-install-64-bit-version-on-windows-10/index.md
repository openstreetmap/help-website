+++
type = "question"
title = "NSIS Error - cannot install 64 bit version on Windows 10"
description = '''Hi all, I&#x27;m trying to installed Wireshark-win64-2.0.1 on a Windows 10 64-bit machine, but when I try running the installer it says: &quot;NSIS Error X Installer integrity check has failed. Common casuses include incomplete download and damaged media. Contact the installer&#x27;s author to obtain a new copy. M...'''
date = "2016-02-05T08:11:00Z"
lastmod = "2016-02-05T08:48:00Z"
weight = 49897
keywords = [ "installer", "64bit", "windows10", "nsis" ]
aliases = [ "/questions/49897" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NSIS Error - cannot install 64 bit version on Windows 10](/questions/49897/nsis-error-cannot-install-64-bit-version-on-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49897-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying to installed Wireshark-win64-2.0.1 on a Windows 10 64-bit machine, but when I try running the installer it says: "NSIS Error</p><p>X Installer integrity check has failed. Common casuses include incomplete download and damaged media. Contact the installer's author to obtain a new copy.</p><p>More information at: <a href="http://nsis.sf.net/NSIS_Error">http://nsis.sf.net/NSIS_Error"</a></p><p>Then nothing gets installed. Help please.</p></div><div id="question-tags" class="tags-container tags">installer 64bit windows10 nsis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '16, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/eb5ea16d44f317d281d50094df56768d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lundaling&#39;s gravatar image" /><p>Lundaling<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lundaling has no accepted answers">0%</span></p></div></div><div id="comments-container-49897" class="comments-container"></div><div id="comment-tools-49897" class="comment-tools"></div><div class="clear"></div><div id="comment-49897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49898"></span>

<div id="answer-container-49898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49898-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure the file is intact? As noted in the <a href="https://www.wireshark.org/lists/wireshark-announce/201512/msg00000.html">release announcement</a> it should have the following size and hashes:</p><pre><code>Wireshark-win64-2.0.1.exe: 47333544 bytes
SHA256(Wireshark-win64-2.0.1.exe)=5c5c9668d0254d183ef94eaaab2ca35e1376ae1bac3f10b21ccf5e14eaafb045
RIPEMD160(Wireshark-win64-2.0.1.exe)=06fc6a95a6a93d4287e4cb4fcbe1f584c8a393d8
SHA1(Wireshark-win64-2.0.1.exe)=27e290b4647adeb51a714d7a831ef88702b518da
MD5(Wireshark-win64-2.0.1.exe)=8a05505aae3807d554a394c8f86ca4ac</code></pre><p>You can use <a href="http://superuser.com/questions/245775/is-there-a-built-in-checksum-utility-on-windows-7">certutil (which ships with Windows) or a number of other utilities</a> to check the hashes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-49898" class="comments-container"></div><div id="comment-tools-49898" class="comment-tools"></div><div class="clear"></div><div id="comment-49898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

