+++
type = "question"
title = "Wireshark uninstaller can&#x27;t remove various .exes"
description = '''I just ran into a problem on Windows 7, Wireshark 1.12.3 (although I have the same problems with versions 1.10.8 and 1.11.3). I cannot uninstall Wireshark, when I navigate to folder: C:&#92;Program Files&#92;Wireshark&#92;uninstall.exe, because &quot;rawshark.exe could not be removed. Is it in use?&quot; But rawshark.exe...'''
date = "2015-01-11T03:54:00Z"
lastmod = "2015-01-11T08:38:00Z"
weight = 39037
keywords = [ "windows", "uninstall" ]
aliases = [ "/questions/39037" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark uninstaller can't remove various .exes](/questions/39037/wireshark-uninstaller-cant-remove-various-exes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39037-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just ran into a problem on Windows 7, Wireshark 1.12.3 (although I have the same problems with versions 1.10.8 and 1.11.3).</p><p>I cannot uninstall Wireshark, when I navigate to folder: C:\Program Files\Wireshark\uninstall.exe, because "rawshark.exe could not be removed. Is it in use?" But rawshark.exe is not in use. I have checked this with Windows Task Manager and Process Explorer. So I deleted rawshark.exe. Next I cannot uninstall Wireshark, because "capinfos.exe could not be removed. Is it in use?" After deleting capinfos.exe, reordercap.exe cannot be removed... and so on...</p><p>However I can uninstall Wireshark by using the Windows Control Panel: Control Panel\All Control Panel Items\Programs and Features</p></div><div id="question-tags" class="tags-container tags">windows uninstall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '15, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '15, 16:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-39037" class="comments-container"></div><div id="comment-tools-39037" class="comment-tools"></div><div class="clear"></div><div id="comment-39037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39047"></span>

<div id="answer-container-39047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39047-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to manually run the uninstaller, ensure to launch it as Administrator. Otherwise you will have the same symptoms as what you describe.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '15, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39047" class="comments-container"><span id="39057"></span><div id="comment-39057" class="comment"><div id="post-39057-score" class="comment-score"></div><div class="comment-text"><p>Thanks Pascal. The message "*.exe could not be removed. Is it in use?" has put me on the wrong track.</p></div><div id="comment-39057-info" class="comment-info"><span class="comment-age">(11 Jan '15, 10:55)</span> joke</div></div></div><div id="comment-tools-39047" class="comment-tools"></div><div class="clear"></div><div id="comment-39047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

