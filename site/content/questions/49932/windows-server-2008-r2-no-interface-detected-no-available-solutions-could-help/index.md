+++
type = "question"
title = "Windows Server 2008 R2 -- No Interface detected -- No available solutions could help"
description = '''Hi All, Problem is: No Interfaces... System: Windows Server 2008 R2 Installed: Wireshark Version 2.0.1, WinPcap Version 4.1.3 I already tried to start the NPF service as admin, but no effect. NPF service can not start Error 1275 Also to start Wireshark as Admin, has no effect. Usually I tried all co...'''
date = "2016-02-06T07:51:00Z"
lastmod = "2016-02-09T08:48:00Z"
weight = 49932
keywords = [ "windows", "server2008", "wireshark", "winpcap", "server" ]
aliases = [ "/questions/49932" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Windows Server 2008 R2 -- No Interface detected -- No available solutions could help](/questions/49932/windows-server-2008-r2-no-interface-detected-no-available-solutions-could-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49932-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, Problem is: No Interfaces... System: Windows Server 2008 R2 Installed: Wireshark Version 2.0.1, WinPcap Version 4.1.3 I already tried to start the NPF service as admin, but no effect. NPF service can not start Error 1275 Also to start Wireshark as Admin, has no effect. Usually I tried all comments which I found online but I got no solution. Please, I hope here is somebody who can help me.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">windows server2008 wireshark winpcap server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '16, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/27770080946906e81f352cf35de5b7ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vecdatra&#39;s gravatar image" /><p>vecdatra<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vecdatra has no accepted answers">0%</span></p></div></div><div id="comments-container-49932" class="comments-container"></div><div id="comment-tools-49932" class="comment-tools"></div><div class="clear"></div><div id="comment-49932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="49943"></span>

<div id="answer-container-49943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49943-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without NPF you won't see interfaces, running Wireshark has no influence on that. Tend to the OS installation/registry, were the 1275 error seems to come from.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '16, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Feb '16, 08:31</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49943" class="comments-container"></div><div id="comment-tools-49943" class="comment-tools"></div><div class="clear"></div><div id="comment-49943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49948"></span>

<div id="answer-container-49948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49948-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently error 1275 is "ERROR_DRIVER_BLOCKED". Not sure why you are getting this error.</p><p>Try un-installing WinPcap, reboot, ensure there is no file %WINDIR%\System32\Drivers\npf.sys left over, and then install WinPcap again on its own from the WinPcap <a href="https://www.winpcap.org/install/">download page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49948" class="comments-container"><span id="49953"></span><div id="comment-49953" class="comment"><div id="post-49953-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb, They is no change. I unistalled the WinPcad and did an reboot. After reboot, I installed the WinP again and checked the npf service but it doesn´t work. Also no effect to try the service start as admin. Same error message. I´m realy not sure what I can do to run wireshark on the server.</p><p>If somebody has any other idea, please let me know. thanks</p></div><div id="comment-49953-info" class="comment-info"><span class="comment-age">(07 Feb '16, 13:40)</span> vecdatra</div></div><span id="50113"></span><div id="comment-50113" class="comment"><div id="post-50113-score" class="comment-score"></div><div class="comment-text"><p>Are there any errors in the Event Log relating to the driver. Try starting the service again as admin and check the Event Log for entries.</p></div><div id="comment-50113-info" class="comment-info"><span class="comment-age">(11 Feb '16, 14:15)</span> grahamb ♦</div></div></div><div id="comment-tools-49948" class="comment-tools"></div><div class="clear"></div><div id="comment-49948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50020"></span>

<div id="answer-container-50020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50020-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try Npcap: <a href="https://github.com/nmap/npcap">https://github.com/nmap/npcap</a>, it is based on WinPcap and works on Vista and later OS.</p><p>The latest version is Npcap 0.05 r10:</p><p><a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-50020" class="comments-container"><span id="50111"></span><div id="comment-50111" class="comment"><div id="post-50111-score" class="comment-score"></div><div class="comment-text"><p>Hi Luo, I uninstalled the WIinPcap and installed the programm Npcap. After installation, I did an reboot and I started wireshark but the same message as before. No interface. ;o(</p><p>Which service should I check for Npcap?</p><p>Thanks</p></div><div id="comment-50111-info" class="comment-info"><span class="comment-age">(11 Feb '16, 10:50)</span> vecdatra</div></div><span id="50119"></span><div id="comment-50119" class="comment"><div id="post-50119-score" class="comment-score"></div><div class="comment-text"><p>Hi vecdatra, I have a few questions.</p><p>Does Npcap install successfully on your machine? If yes, launch a command prompt with Administrator privilege and run "net start npf" to see what happens.</p><p>BTW, you can launch ncpa.cpl to see whether you have disabled all your adapters? If an adapter is disbaled in ncpa.cpl, it will not show up in the list.</p></div><div id="comment-50119-info" class="comment-info"><span class="comment-age">(11 Feb '16, 21:16)</span> Yang Luo</div></div><span id="50169"></span><div id="comment-50169" class="comment"><div id="post-50169-score" class="comment-score"></div><div class="comment-text"><p>Hi, cmd as admin and then "net start npf" shows the same error message as before. Error code 1275, driver could not be loaded. Installation itself (of Npcap) was succesful without any error. ncpa.cpl shows only one adapter and this adapter is enabled. If this would be disabled, the connection to my server is not possible anymore.</p></div><div id="comment-50169-info" class="comment-info"><span class="comment-age">(13 Feb '16, 03:54)</span> vecdatra</div></div><span id="50177"></span><div id="comment-50177" class="comment"><div id="post-50177-score" class="comment-score"></div><div class="comment-text"><p>Can you show me the C:\Program Files\Npcap\npf.sys file's Properties -&gt; Details -&gt; File description? It should be the right version:</p><p>For 32-bit Windows should be "npf.sys (NT6 x86) Kernel Filter Driver"</p><p>For 64-bit Windows should be "npf.sys (NT6 AMD64) Kernel Filter Driver"</p><p>For your case (Windows Server 2008 R2), it should be "AMD64" instead of "x86"</p><p>Also run these two commands to see what happens:</p><p>NPFInstall.exe -iw</p><p>NPFInstall.exe -i</p></div><div id="comment-50177-info" class="comment-info"><span class="comment-age">(13 Feb '16, 08:06)</span> Yang Luo</div></div></div><div id="comment-tools-50020" class="comment-tools"></div><div class="clear"></div><div id="comment-50020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

