+++
type = "question"
title = "No USB interfaces after Wireshark update"
description = '''I ran Wireshark this morning and was notified that there was a new version available. I accepted the update option and during the install was informed that I had the latest version of Winpcap but the installed version of USBPcap was outdated. The option to install USBPcap 1.2.0.1 was not enabled. So...'''
date = "2017-07-21T08:20:00Z"
lastmod = "2017-07-21T11:04:00Z"
weight = 62981
keywords = [ "usbpcap" ]
aliases = [ "/questions/62981" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No USB interfaces after Wireshark update](/questions/62981/no-usb-interfaces-after-wireshark-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62981-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran Wireshark this morning and was notified that there was a new version available. I accepted the update option and during the install was informed that I had the latest version of Winpcap but the installed version of USBPcap was outdated. The option to install USBPcap 1.2.0.1 was not enabled. So I quit the Wireshark install and then updated USBPcap. After a reboot I installed the latest Wireshark but no USB interfaces are shown. I tried re-installing WINPcap and then re-installing Wireshark. The Wireshark install showed the correct versions of WINPcap and USBPcap but I still have no USB interfaces available in Wireshark. I'm running Win10 Pro 64. Any suggestions?</p></div><div id="question-tags" class="tags-container tags">usbpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '17, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/1751f3b4ff94facb331c3e9b47a1c37d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gomtuu&#39;s gravatar image" /><p>gomtuu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gomtuu has no accepted answers">0%</span></p></div></div><div id="comments-container-62981" class="comments-container"><span id="62983"></span><div id="comment-62983" class="comment"><div id="post-62983-score" class="comment-score">1</div><div class="comment-text"><p>Try uninstalling everything, Wireshark, WinPCap and USBPcap, then reboot. Next install Wireshark allowing the installer to install WinPcap and USBPcap.</p></div><div id="comment-62983-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:36)</span> grahamb ♦</div></div><span id="62985"></span><div id="comment-62985" class="comment"><div id="post-62985-score" class="comment-score"></div><div class="comment-text"><p>The point is that the USBPcap installer has to be run after WIreshark has been installed so that it could place the USBPcapCMD.exe to the proper directory in the Wireshark directory tree, but for some reason it cannot run if you do not manually uninstall the previous version beforehand.</p><p>What you can do if you don't want to uninstall nad reinstall everything is to manually copy USBPcapCMD.exe from C:\Program Files\USBPcap to C:\Program Files\Wireshark\Extcap.</p></div><div id="comment-62985-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:49)</span> sindy</div></div></div><div id="comment-tools-62981" class="comment-tools"></div><div class="clear"></div><div id="comment-62981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62988"></span>

<div id="answer-container-62988" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62988-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, uninstalling everything, rebooting and then allowing the Wireshark install to install everything seems to have worked. Previously when uninstalling Wireshark the C:\Program Files\Wireshark\Extcap directory could not be emptied and thus could not be removed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/1751f3b4ff94facb331c3e9b47a1c37d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gomtuu&#39;s gravatar image" /><p>gomtuu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gomtuu has no accepted answers">0%</span></p></div></div><div id="comments-container-62988" class="comments-container"></div><div id="comment-tools-62988" class="comment-tools"></div><div class="clear"></div><div id="comment-62988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

