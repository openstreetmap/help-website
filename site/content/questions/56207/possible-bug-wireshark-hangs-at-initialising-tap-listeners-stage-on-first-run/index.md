+++
type = "question"
title = "Possible Bug? Wireshark hangs at Initialising Tap Listeners stage on first run"
description = '''Hi, Windows 10 64 bit, build 14936 Wireshark Version 2.2.1 (v2.2.1-0-ga6fbd27 from master-2.2) When Wireshark is first loaded after a reboot, the application will hang at the Initializing Tap Listeners screen. you then need to force close the app. Second time round, all seems to load as expected, bu...'''
date = "2016-10-06T15:42:00Z"
lastmod = "2016-10-06T23:18:00Z"
weight = 56207
keywords = [ "initialising", "listeners", "tap", "bug" ]
aliases = [ "/questions/56207" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Possible Bug? Wireshark hangs at Initialising Tap Listeners stage on first run](/questions/56207/possible-bug-wireshark-hangs-at-initialising-tap-listeners-stage-on-first-run)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56207-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Windows 10 64 bit, build 14936 Wireshark Version 2.2.1 (v2.2.1-0-ga6fbd27 from master-2.2)</p><p>When Wireshark is first loaded after a reboot, the application will hang at the Initializing Tap Listeners screen. you then need to force close the app. Second time round, all seems to load as expected, but when running an update, it complains that either Wireshark or an associated application is still open.</p><p>Windows event log:</p><pre><code>The program Wireshark.exe version 2.2.1.0 stopped interacting with Windows and was closed. To see if more information about the problem is available, check the problem history in the Security and Maintenance control panel.
 Process ID: 3c3c
 Start Time: 01d22019bfab4a38
 Termination Time: 4
 Application Path: C:\Program Files\Wireshark\Wireshark.exe
 Report Id: 37e0316b-3593-4cd2-befd-ff83d4a0254b
 Faulting package full name: 
 Faulting package-relative application ID:</code></pre><p>Ideas?</p><p>Chris</p></div><div id="question-tags" class="tags-container tags">initialising listeners tap bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '16, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/bbeb91ebbe399c56bae792a4b546ee0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swinster&#39;s gravatar image" /><p>swinster<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swinster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '16, 07:45</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-56207" class="comments-container"></div><div id="comment-tools-56207" class="comment-tools"></div><div class="clear"></div><div id="comment-56207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56211"></span>

<div id="answer-container-56211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56211-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have an extcap tools installed (like USBPcap for example)? If yes, you are probably facing <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12845">bug 12845</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '16, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-56211" class="comments-container"><span id="56244"></span><div id="comment-56244" class="comment"><div id="post-56244-score" class="comment-score"></div><div class="comment-text"><p>Hey Pascal,</p><p>That looks to the the issue. I skimmed the bug, removed C:\Program Files\Wireshark\extcap\USBPcapCMD.exe, and all is good. This is not super important for me so its Ok for the moment to leave as is.</p><p>Hope you guys will be able to create a fix at some point.</p><p>Regards,</p><p>Chris</p></div><div id="comment-56244-info" class="comment-info"><span class="comment-age">(08 Oct '16, 19:00)</span> swinster</div></div><span id="59562"></span><div id="comment-59562" class="comment"><div id="post-59562-score" class="comment-score">1</div><div class="comment-text"><p>Can confirm; it is the bug Pascal Quantin pointed out. Still a problem as of 2017-02-20. I first renamed .\extcap\USBPcapCMD.exe to USBPcapCMD.exe.bak. That allowed it me to relaunch Wireshark successfully. However, upon an OS restart, it failed again. I then uninstalled USBPcap 1.1.0.0-g794bf26-5 and Wireshark is working again.</p></div><div id="comment-59562-info" class="comment-info"><span class="comment-age">(20 Feb '17, 09:36)</span> peterfnet</div></div><span id="59564"></span><div id="comment-59564" class="comment"><div id="post-59564-score" class="comment-score"></div><div class="comment-text"><p>The bug is still open. Which Wireshark version were you using?</p></div><div id="comment-59564-info" class="comment-info"><span class="comment-age">(20 Feb '17, 10:06)</span> grahamb ♦</div></div><span id="60062"></span><div id="comment-60062" class="comment"><div id="post-60062-score" class="comment-score"></div><div class="comment-text"><p>Installed wireshark 2.2.5 and faced the same symptom.</p><p>Wireshark hangs at Initialising Tap Listeners stage on first run. I have uninstalled USBPcapCMD and wireshark starts again.</p><p>Brgds,</p><p>Bas.</p></div><div id="comment-60062-info" class="comment-info"><span class="comment-age">(14 Mar '17, 07:03)</span> bascaves</div></div></div><div id="comment-tools-56211" class="comment-tools"></div><div class="clear"></div><div id="comment-56211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

