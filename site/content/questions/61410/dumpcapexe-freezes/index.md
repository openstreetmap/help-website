+++
type = "question"
title = "dumpcap.exe freezes"
description = '''Hello, I&#x27;m attempting to run Wireshark 2.2.6 64 on a Windows 10, 64 bit device and it will run once then freeze on loading a pcap file. Forcing the process to stop, leaves dumpcap.exe running and it cannot be halted via task manager or taskkil. The only way to clear the process is to restart. Based ...'''
date = "2017-05-15T09:10:00Z"
lastmod = "2017-05-15T10:12:00Z"
weight = 61410
keywords = [ "crash", "dumpcap" ]
aliases = [ "/questions/61410" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap.exe freezes](/questions/61410/dumpcapexe-freezes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61410-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm attempting to run Wireshark 2.2.6 64 on a Windows 10, 64 bit device and it will run once then freeze on loading a pcap file. Forcing the process to stop, leaves dumpcap.exe running and it cannot be halted via task manager or taskkil. The only way to clear the process is to restart.</p><p>Based on some similar questions(<a href="https://ask.wireshark.org/questions/48178/wireshark-fails-to-start-on-windows-10">https://ask.wireshark.org/questions/48178/wireshark-fails-to-start-on-windows-10</a> and <a href="https://ask.wireshark.org/questions/55394/wireshark-220-freezes-during-first-start-after-each-reboot)">https://ask.wireshark.org/questions/55394/wireshark-220-freezes-during-first-start-after-each-reboot)</a> I've tried reinstalling Wireshark without winpcap and this problem remains.</p><p>Also, I have never installed the usb capture utility. I have also tried earlier version of Wireshark, going back to 2.0.3 64.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">crash dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '17, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/e588a90c779c8c69e246cab1fd48ba69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bionic_cow&#39;s gravatar image" /><p>bionic_cow<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bionic_cow has no accepted answers">0%</span></p></div></div><div id="comments-container-61410" class="comments-container"></div><div id="comment-tools-61410" class="comment-tools"></div><div class="clear"></div><div id="comment-61410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61412"></span>

<div id="answer-container-61412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61412-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have any AV or VPN software installed? These have been known to cause WinPcap freezes.</p><p>Can you post the contents of Wireshark Help -&gt; About if you can display it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '17, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 May '17, 10:13</p></div></div><div id="comments-container-61412" class="comments-container"><span id="61414"></span><div id="comment-61414" class="comment"><div id="post-61414-score" class="comment-score"></div><div class="comment-text"><p>I can't get that as the program freezes.</p><p>Device is running AV and VPN which does not interfere with Wireshark on other devices.</p></div><div id="comment-61414-info" class="comment-info"><span class="comment-age">(15 May '17, 10:34)</span> bionic_cow</div></div></div><div id="comment-tools-61412" class="comment-tools"></div><div class="clear"></div><div id="comment-61412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

