+++
type = "question"
title = "How do I fix my computer after USBPcap has rendered the USB keyboard and mouse inoperative?"
description = '''How do you login into your Windows 10 Pro 64-Bit, computer if the USB Keyboard and Mouse have been rendered inoperative by this rouge installation. I have been on the phone with both Dell and Microsoft for hours and we cannot seem to find a fix.'''
date = "2017-07-21T22:04:00Z"
lastmod = "2017-07-21T22:46:00Z"
weight = 62996
keywords = [ "mouseandkeyboard", "usbpcap" ]
aliases = [ "/questions/62996" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix my computer after USBPcap has rendered the USB keyboard and mouse inoperative?](/questions/62996/how-do-i-fix-my-computer-after-usbpcap-has-rendered-the-usb-keyboard-and-mouse-inoperative)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62996-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do you login into your Windows 10 Pro 64-Bit, computer if the USB Keyboard and Mouse have been rendered inoperative by this rouge installation. I have been on the phone with both Dell and Microsoft for hours and we cannot seem to find a fix.</p></div><div id="question-tags" class="tags-container tags">mouseandkeyboard usbpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '17, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/8273aa4d34d18db36886a02be3279c59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PLCMAN58&#39;s gravatar image" /><p>PLCMAN58<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PLCMAN58 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 21 Jul '17, 22:09</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-62996" class="comments-container"></div><div id="comment-tools-62996" class="comment-tools"></div><div class="clear"></div><div id="comment-62996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62997"></span>

<div id="answer-container-62997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62997-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11766">bug 11766</a>; it mentions some ways of booting the machine that might keep USBPcap from messing the driver stack up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62997" class="comments-container"></div><div id="comment-tools-62997" class="comment-tools"></div><div class="clear"></div><div id="comment-62997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62998"></span>

<div id="answer-container-62998" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62998-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found a solution that worked after 6+ hours of scouring the Internet and talking to both Dell and Microsoft!!! The solution was posted on the support website for USBPcap. It was buried in the site but after repeated searches I stumbled on the Secure Boot reference.</p><p>On my Dell XPS 8920 with Microsoft Windows Professional 10 64-Bit installed, I disabled the UEFI SECURE BOOT option and then on re-booted the computer. Both my USB keyboard and Mouse were then recognized. I then was able to un-install the USBPcap driver.</p><p>I then rebooted the computer a couple of time just to make sure that everything was working properly. After that I went back into the BIOS and enabled the UEFI Secure Boot option.</p><p>Thanks to everyone that offered assistance!!!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/8273aa4d34d18db36886a02be3279c59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PLCMAN58&#39;s gravatar image" /><p>PLCMAN58<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PLCMAN58 has no accepted answers">0%</span></p></div></div><div id="comments-container-62998" class="comments-container"></div><div id="comment-tools-62998" class="comment-tools"></div><div class="clear"></div><div id="comment-62998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

