+++
type = "question"
title = "Wireshark doesn&#x27;t work on Windows 10 build 1511"
description = '''I have recently upgraded Windows 8.1 to Windows 10, and there is problem with Wireshark.  When I run Wireshark as administrator, I can see in task manager that process has started, but that is it. No window, no error message. I tried to reinstall WinPcap, and Wireshark - nothing changes. I installed...'''
date = "2016-06-01T04:40:00Z"
lastmod = "2016-06-01T04:49:00Z"
weight = 53097
keywords = [ "windows10" ]
aliases = [ "/questions/53097" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't work on Windows 10 build 1511](/questions/53097/wireshark-doesnt-work-on-windows-10-build-1511)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53097-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have recently upgraded Windows 8.1 to Windows 10, and there is problem with Wireshark.</p><p>When I run Wireshark as administrator, I can see in task manager that process has started, but that is it. No window, no error message.</p><p>I tried to reinstall WinPcap, and Wireshark - nothing changes.</p><p>I installed Win10Pcap - nothing.</p><p>I installed Ncap - stiil same.</p><p>I am running out of ideas. Anyone have some sugestions?</p></div><div id="question-tags" class="tags-container tags">windows10</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/5a085fcda85f9269dfa4c58c6969eb7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickBo&#39;s gravatar image" /><p>nickBo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickBo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '16, 04:41</p></div></div><div id="comments-container-53097" class="comments-container"></div><div id="comment-tools-53097" class="comment-tools"></div><div class="clear"></div><div id="comment-53097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53099"></span>

<div id="answer-container-53099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53099-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It works for me on two different machines (Win 8.1) that were upgraded to Win 10.</p><p>You can try this:</p><ol><li>Uninstall Wireshark. Uninstall WinPcap. Uninstall USBpcap. Uninstall Win10Pcap. Uninstall NCap (what's that, did you mean npcap?).</li><li>Reboot.</li><li>Check you don't have any pcap detritus, <code>dir %windir%\System32\Drivers\npf.sys</code>.</li><li>Reinstall Wireshark, installing WinPcap when given the option.</li></ol><p>If there is pcap detritus then something else has installed npf.sys, find out what it is and remove it before installing Wireshark.</p><p>It's also entirely possible that other software, e.g. AV, VPN, Endpoint Protection is causing the issue, do you have anything of that sort installed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53099" class="comments-container"><span id="53106"></span><div id="comment-53106" class="comment"><div id="post-53106-score" class="comment-score"></div><div class="comment-text"><p>What is pcap detritus?</p><p>I have Cisco VPN Client and Dell's Global VPN client installed. I unistalled those, and tried to run wireshark, but nothing changed.</p></div><div id="comment-53106-info" class="comment-info"><span class="comment-age">(01 Jun '16, 06:41)</span> nickBo</div></div><span id="53110"></span><div id="comment-53110" class="comment"><div id="post-53110-score" class="comment-score"></div><div class="comment-text"><p>detritus - left over from installs.</p><p>Did you also go through the other uninstalls and reboot as I suggested?</p></div><div id="comment-53110-info" class="comment-info"><span class="comment-age">(01 Jun '16, 07:08)</span> grahamb ♦</div></div><span id="53201"></span><div id="comment-53201" class="comment"><div id="post-53201-score" class="comment-score"></div><div class="comment-text"><p>Just a rough idea, those multiple desktops introduced in Windows 10. Can you run Wireshark like you did, and then click the desktop selection icon next to the "start" and "search" icons in the taskbar and check whether Windows haven't open the Wireshark window on another desktop?</p></div><div id="comment-53201-info" class="comment-info"><span class="comment-age">(04 Jun '16, 07:55)</span> sindy</div></div></div><div id="comment-tools-53099" class="comment-tools"></div><div class="clear"></div><div id="comment-53099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

