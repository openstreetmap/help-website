+++
type = "question"
title = "Wireshark fails to start on Windows 10"
description = '''Wire shark is not opening only in Windows 10.. Is there any way to do that?'''
date = "2015-12-02T01:51:00Z"
lastmod = "2016-11-07T03:00:00Z"
weight = 48178
keywords = [ "win10", "wireshark" ]
aliases = [ "/questions/48178" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fails to start on Windows 10](/questions/48178/wireshark-fails-to-start-on-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48178-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wire shark is not opening only in Windows 10.. Is there any way to do that?</p></div><div id="question-tags" class="tags-container tags">win10 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/8e85b21abd46fd6062b9b0de7f3138f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abdul%20Jaleel&#39;s gravatar image" /><p>Abdul Jaleel<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abdul Jaleel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 02 Dec '15, 02:16</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48178" class="comments-container"><span id="48179"></span><div id="comment-48179" class="comment"><div id="post-48179-score" class="comment-score"></div><div class="comment-text"><p>Can you be a bit more descriptive of your issue?</p><p>What version of Wireshark did you install, and how are you trying to start it?</p></div><div id="comment-48179-info" class="comment-info"><span class="comment-age">(02 Dec '15, 02:17)</span> grahamb ♦</div></div><span id="50634"></span><div id="comment-50634" class="comment"><div id="post-50634-score" class="comment-score">1</div><div class="comment-text"><p>Experiencing a similar issue. From a clean boot, no other apps started other than a few in the tray, I click on the desktop shortcut (have also tried the legacy option as well). In the new UI it starts up, and the loading progress bar stops at ‘Loading module preferences’. The status bar reads ‘Please wait while Wireshark is initializing …’ If I click into the window at this point it goes grey and (Not Responding) appears in the title bar. I have to then kill the application.</p><p>I am running Windows 10 Pro x64, Version 1511, OS Build 10586.104, 16GB RAM, Intel Core i7-4980HQ CPU @ 2.80GHz. 1TB SSD HD with approx. 40% spare space.</p><p>Also worth stating that it also hangs on Mac OSX 10.11 wherever I change the IP lookup preferences.</p></div><div id="comment-50634-info" class="comment-info"><span class="comment-age">(01 Mar '16, 12:35)</span> NRGfxIT</div></div><span id="50635"></span><div id="comment-50635" class="comment"><div id="post-50635-score" class="comment-score"></div><div class="comment-text"><p>Should also have said the version of Wireshark I am running is whatever you have on the website as of the 29th February 2016. As I cannot get it to start I cannot validate its version from any interface.</p></div><div id="comment-50635-info" class="comment-info"><span class="comment-age">(01 Mar '16, 12:38)</span> NRGfxIT</div></div><span id="50636"></span><div id="comment-50636" class="comment"><div id="post-50636-score" class="comment-score"></div><div class="comment-text"><p>For now reverting back to Kali Linux where things seem to be a little more stable ;-)</p></div><div id="comment-50636-info" class="comment-info"><span class="comment-age">(01 Mar '16, 12:40)</span> NRGfxIT</div></div><span id="50638"></span><div id="comment-50638" class="comment"><div id="post-50638-score" class="comment-score">1</div><div class="comment-text"><p>I can confirm that I am running Wireshark v2.0.2.</p><p>Attempts to uninstall is hampered by the 'Wireshark Dump' processes (x2) that cannot be killed from the task manager with an 'Access is denied' error even when running as Admin. These are I believe artefacts from the x2 attempts to load the program and crashing out of it. A re-boot flushes them and I can then uninstall Wireshark.</p><p>Tested also Win32 version 2.0.2 and it hangs in the same way as the x64. Attempts to uninstall requires a re-boot due to the stuck process as with x64.</p><p>Tried the latest build of Wireshark v2.1.0-2200-g9063aca (x64) same hanging issue, and also locked process when attempting to uninstall.</p></div><div id="comment-50638-info" class="comment-info"><span class="comment-age">(01 Mar '16, 13:44)</span> NRGfxIT</div></div></div><div id="comment-tools-48178" class="comment-tools"></div><div class="clear"></div><div id="comment-48178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="50654"></span>

<div id="answer-container-50654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50654-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The dumpcap process is the user mode application that is started by Wireshark (or tshark) to discover and capture from the network interfaces on your machine, usually via the WinPcap driver.</p><p>Unfortunately for you (@NRGfxIT), and a very small number of other folks, there appears to be some issue in your environment that causes the call into WinPcap to hang, which then blocks the dumpcap process. I suspect something in the network stack on your machine, possible VPN or Endpoint protection software causes this. Unfortunately debugging this remotely is near impossible.</p><p>You may want to try replacing WinPcap with the likely replacement for it, <a href="https://github.com/nmap/npcap/releases">npcap</a> as npcap has moved to a more modern driver mechanism within Windows, so may not suffer the issue you have.</p><p>To install npcap, uninstall WinPcap, reboot, and then install npcap in WinPcap compatibility mode. You can then install Wireshark again, which should behappy to use the newly installed version of npcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50654" class="comments-container"><span id="51835"></span><div id="comment-51835" class="comment"><div id="post-51835-score" class="comment-score"></div><div class="comment-text"><p>I'm having the same problem now after upgrading wireshark to the latest version yesterday. It was working before that, and as part of the upgrade process I didn't upgrade WinPCAP (already had the latest version). I think there's something else going on here.</p></div><div id="comment-51835-info" class="comment-info"><span class="comment-age">(21 Apr '16, 04:11)</span> robert_</div></div><span id="51837"></span><div id="comment-51837" class="comment"><div id="post-51837-score" class="comment-score"></div><div class="comment-text"><p>Can you ensure no dumpcap processes are running, terminate then if there are, and then let us know what happens when running <code>path\to\dumpcap.exe -D</code> from a command prompt?</p></div><div id="comment-51837-info" class="comment-info"><span class="comment-age">(21 Apr '16, 05:16)</span> grahamb ♦</div></div><span id="51861"></span><div id="comment-51861" class="comment"><div id="post-51861-score" class="comment-score"></div><div class="comment-text"><p>One day later (with no intervention other than a reboot) and it's working again. Glad I didn't go through the rigmarole of installing ncap :-) By the way, output of dumpcap was <code>1. \Device\NPF_{4799958E-76F0-491A-9229-12E9ABCD8B4F} (Ethernet)</code></p></div><div id="comment-51861-info" class="comment-info"><span class="comment-age">(22 Apr '16, 00:58)</span> robert_</div></div></div><div id="comment-tools-50654" class="comment-tools"></div><div class="clear"></div><div id="comment-50654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51855"></span>

<div id="answer-container-51855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51855-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try Npcap (replacement of WinPcap), the latest version is 0.06 R19:</p><p><a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '16, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-51855" class="comments-container"></div><div id="comment-tools-51855" class="comment-tools"></div><div class="clear"></div><div id="comment-51855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56960"></span>

<div id="answer-container-56960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was having similar problems with 64 bit version 2.20 on Windows 10. Launched the app and got a greyed out screen saying - ‘Please wait while Wireshark is initializing …’</p><p>Tried to upgrade to 2.21 and that didn't make any difference (had to reboot before I could upgrade).<br />
</p><p>Then I remembered that I had added USBPcap on a recent update so I uninstalled Wireshark 2.21, WINPcap, USBPcap, then resinstalled Wireshark 2.21 with WINPcap and now it is working.... Hope this might be helpful...<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '16, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/de3b93697b0e6f29303f008bb3ca24a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PBSki&#39;s gravatar image" /><p>PBSki<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PBSki has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-56960" class="comments-container"></div><div id="comment-tools-56960" class="comment-tools"></div><div class="clear"></div><div id="comment-56960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57045"></span>

<div id="answer-container-57045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Same error. Run as administrator. Windows 10 Pro 1607(OS Build 14393.351)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WIRESHARK.png" alt="alt text" /></p><p>Subj work like a charm after killing Wireshark.exe in Process Explorer and restart.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WIRESHARK2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/7ac258f38485f8302ac1e887fe5595c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smarty&#39;s gravatar image" /><p>smarty<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smarty has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '16, 03:12</p></div></div><div id="comments-container-57045" class="comments-container"><span id="57046"></span><div id="comment-57046" class="comment"><div id="post-57046-score" class="comment-score"></div><div class="comment-text"><p>Please don't run Wireshark as Administrator, it's not necessary and exposes your system to much more risk from malicious traffic.</p><p>See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Privileges</a> for more details.</p></div><div id="comment-57046-info" class="comment-info"><span class="comment-age">(07 Nov '16, 03:17)</span> grahamb ♦</div></div><span id="57047"></span><div id="comment-57047" class="comment"><div id="post-57047-score" class="comment-score">1</div><div class="comment-text"><p>@smarty, the symptoms you describe indicate that you suffer from <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12845">bug12845</a>.</p><p>The issue and workaround have been discussed <a href="https://ask.wireshark.org/questions/55394/wireshark-220-freezes-during-first-start-after-each-reboot">here</a>.</p></div><div id="comment-57047-info" class="comment-info"><span class="comment-age">(07 Nov '16, 03:46)</span> sindy</div></div><span id="57049"></span><div id="comment-57049" class="comment"><div id="post-57049-score" class="comment-score"></div><div class="comment-text"><p>Thx, @sindy.</p></div><div id="comment-57049-info" class="comment-info"><span class="comment-age">(07 Nov '16, 05:13)</span> smarty</div></div></div><div id="comment-tools-57045" class="comment-tools"></div><div class="clear"></div><div id="comment-57045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

