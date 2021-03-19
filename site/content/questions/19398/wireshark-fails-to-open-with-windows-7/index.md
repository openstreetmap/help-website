+++
type = "question"
title = "Wireshark fails to open with windows 7"
description = '''With Wireshark 1.8.5 and 1.8.6 sometimes wireshark will not open. The icon on the taskbar will become become highlighted for a few seconds then dissapear. If I look at the running processes wireshark is listed but I can not interact with it. If I kill the process tree and try to reopen Wireshark the...'''
date = "2013-03-12T11:41:00Z"
lastmod = "2013-03-12T11:47:00Z"
weight = 19398
keywords = [ "fail", "start", "windows7", "open", "restart" ]
aliases = [ "/questions/19398" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fails to open with windows 7](/questions/19398/wireshark-fails-to-open-with-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19398-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With Wireshark 1.8.5 and 1.8.6 sometimes wireshark will not open. The icon on the taskbar will become become highlighted for a few seconds then dissapear. If I look at the running processes wireshark is listed but I can not interact with it. If I kill the process tree and try to reopen Wireshark the same thing will happen. I must restart in order to open a usable Wireshark.</p><p>Windows Pro 64 bit Wireshark 64 bit or 32 bit</p></div><div id="question-tags" class="tags-container tags">fail start windows7 open restart</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/0f45b0b7c1b00749c4fb6fc9126f61fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20Conley&#39;s gravatar image" /><p>Joseph Conley<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph Conley has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Mar '13, 10:26</p></div></div><div id="comments-container-19398" class="comments-container"></div><div id="comment-tools-19398" class="comment-tools"></div><div class="clear"></div><div id="comment-19398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19399"></span>

<div id="answer-container-19399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19399-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In cases like this I usually delete my profile settings to have Wireshark start with default settings. Usually that helps.</p><p>To clear the settings, go to C:\Users\USERNAME\AppData\Roaming\Wireshark\ and remove all files, including sub directories. You can copy the files to a backup location in case you want to preserve some of the profiles after testing which one was problematic. With an empty settings folder Wireshark should start.</p><p>Hint: the "AppData" part of the path is a hidden directory, so you may not be able to see it but it's there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '13, 11:48</p></div></div><div id="comments-container-19399" class="comments-container"><span id="19403"></span><div id="comment-19403" class="comment"><div id="post-19403-score" class="comment-score"></div><div class="comment-text"><p>Sadly this did not help me :(</p></div><div id="comment-19403-info" class="comment-info"><span class="comment-age">(12 Mar '13, 13:01)</span> Joseph Conley</div></div><span id="19404"></span><div id="comment-19404" class="comment"><div id="post-19404-score" class="comment-score"></div><div class="comment-text"><p>Unless you really need the x64 version try the 32 bit version. The 64 bit versions of the 3rd party libraries used by Wireshark don't get as much usage in the wild as the 32 bit ones do.</p></div><div id="comment-19404-info" class="comment-info"><span class="comment-age">(12 Mar '13, 13:10)</span> grahamb ♦</div></div><span id="19620"></span><div id="comment-19620" class="comment"><div id="post-19620-score" class="comment-score"></div><div class="comment-text"><p>Using 32-bit doesnt make a difference. Still gets in the unusable state.</p></div><div id="comment-19620-info" class="comment-info"><span class="comment-age">(18 Mar '13, 10:25)</span> Joseph Conley</div></div></div><div id="comment-tools-19399" class="comment-tools"></div><div class="clear"></div><div id="comment-19399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

