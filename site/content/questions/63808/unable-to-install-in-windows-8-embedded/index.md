+++
type = "question"
title = "Unable to install in Windows 8 Embedded"
description = '''I am unable to install Wireshark-win64-2.4.1.exe in our machine with Windows 8 embedded standard. We need to analyze USB traffic on one of our USB ports.  As I try to install it with WinPcap and USBPcap, it installs fine. But when we open the Wireshark, it says &quot;Initializing extcap..&quot; for a long tim...'''
date = "2017-10-11T08:06:00Z"
lastmod = "2017-10-11T09:59:00Z"
weight = 63808
keywords = [ "embedded", "windows8", "install" ]
aliases = [ "/questions/63808" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to install in Windows 8 Embedded](/questions/63808/unable-to-install-in-windows-8-embedded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63808-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to install Wireshark-win64-2.4.1.exe in our machine with Windows 8 embedded standard. We need to analyze USB traffic on one of our USB ports. As I try to install it with WinPcap and USBPcap, it installs fine. But when we open the Wireshark, it says "Initializing extcap.." for a long time and after that it goes to "not responding" and we have to terminate it with task manager.</p><p>We are running with USBPcap and WinPCap start with program start up. Also, when we reopen the wireshark again, it says can't open the program. Tried reinstalling a lot of times, but didn't work.</p><p>Any help is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">embedded windows8 install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '17, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/680eda71b2bfea24fc09f6608e86f25c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saisudheer8&#39;s gravatar image" /><p>saisudheer8<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saisudheer8 has no accepted answers">0%</span></p></div></div><div id="comments-container-63808" class="comments-container"><span id="63810"></span><div id="comment-63810" class="comment"><div id="post-63810-score" class="comment-score"></div><div class="comment-text"><p>I know you want to capture on USB, but can you try uninstalling USBPcap and then starting Wireshark? My suspicion is that the USBPcap driver is hanging Wireshark when it attempts to enumerate all the interfaces.</p><p>As an aside I'm not aware of anyone using Wireshark on the Embedded versions of Windows, you might be on the bleeding edge there.</p></div><div id="comment-63810-info" class="comment-info"><span class="comment-age">(11 Oct '17, 09:22)</span> grahamb ♦</div></div><span id="63812"></span><div id="comment-63812" class="comment"><div id="post-63812-score" class="comment-score"></div><div class="comment-text"><p>I have tried installing it without USBPcap. I get the following error: Wireshark.exe - System error The program can't start because api-ms-win-crt-locale-l1-1-0.dll is missing from your computer. Try reinstalling the program to fix this problem.</p></div><div id="comment-63812-info" class="comment-info"><span class="comment-age">(11 Oct '17, 09:43)</span> saisudheer8</div></div><span id="63820"></span><div id="comment-63820" class="comment"><div id="post-63820-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a>, I'm afraid the issue might be the 32-bit installer of 2.4.1. Yesterday I was installing it remotely on a Win7 32-bit notebook and got the same error for repeated uninstall-and-reinstall attempts, but as I could resolve the real issue there without Wireshark, I did not dig further into this .dll trouble. But to make it even more interesting, also tshark and dumpcap were complaining about absence of that .dll. The 2.4.1 on my main notebook (Win10 64 bit) runs fine. Also, the missing .dll issue should not be related to USBPcap, as I didn't install USBPcap there during any of the attempts.</p><p><a href="https://ask.wireshark.org/users/43550/saisudheer8"></a><a href="https://ask.wireshark.org/users/43550/saisudheer8">@saisudheer8</a>, what <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> suggests you is to invoke USBPcapCmd.exe alone directly from the command line rather than invoke it from Wireshark. USBPcapCmd.exe might not need that missing library, so you could be able to capture the USB traffic you are interested in into a .pcap file written directly by USBPcapCmd.exe, and then copy that .pcap file somewhere where Wireshark runs normally (64-bit Windows, linux, Mac OS) and analyse it there. To run USBPcapCmd.exe, WinPcap need not be installed. As for the "initializing extcap" forever, there used to be an issue with large lists of USB (and Bluetooth) devices related to extcap which is Wireshark's (well, dumpcap's) interface to USBPcap, and I'm not sure whether it has already been resolved.</p></div><div id="comment-63820-info" class="comment-info"><span class="comment-age">(11 Oct '17, 12:34)</span> sindy</div></div><span id="63823"></span><div id="comment-63823" class="comment"><div id="post-63823-score" class="comment-score"></div><div class="comment-text"><p>So the symptoms have changed from hanging to reporting a missing DLL. I don't have any Win 7 32 bit (or any Win 32 bit for that matter) systems handy to test. I'll have to fire up a VM for that.</p></div><div id="comment-63823-info" class="comment-info"><span class="comment-age">(11 Oct '17, 13:51)</span> grahamb ♦</div></div><span id="63832"></span><div id="comment-63832" class="comment"><div id="post-63832-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want to capture only one USB Port but I get the traffic from all other ports which confuses my project. Any solution for this?</p></blockquote><p>Please file the sentence above as a separate Question as it is only loosely related to your original one. This is a Q&amp;A site, not a discussion forum.</p><p>I could convert your previous comment to a new question myself but doing so would move your confirmation away from here.</p></div><div id="comment-63832-info" class="comment-info"><span class="comment-age">(11 Oct '17, 22:41)</span> sindy</div></div><span id="63838"></span><div id="comment-63838" class="comment not_top_scorer"><div id="post-63838-score" class="comment-score"></div><div class="comment-text"><p>Done. Thanks</p></div><div id="comment-63838-info" class="comment-info"><span class="comment-age">(12 Oct '17, 03:15)</span> saisudheer8</div></div></div><div id="comment-tools-63808" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-63808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63813"></span>

<div id="answer-container-63813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63813-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That would seem to be an issue with running on Windows 8 Embedded then.</p><p>Can you install USBPCap and use USBPcapCmd.exe to capture, then copy the capture file to a regular Windows system?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '17, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63813" class="comments-container"><span id="63814"></span><div id="comment-63814" class="comment"><div id="post-63814-score" class="comment-score"></div><div class="comment-text"><p>You mean install USBPCap while installing Wireshark right? How important it WinPCap?</p></div><div id="comment-63814-info" class="comment-info"><span class="comment-age">(11 Oct '17, 10:01)</span> saisudheer8</div></div><span id="63822"></span><div id="comment-63822" class="comment"><div id="post-63822-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> <a href="https://ask.wireshark.org/users/19586/sindy">@sindy</a> Thanks for the comments. Let me try this and update you with the results. Appreciate your help.</p></div><div id="comment-63822-info" class="comment-info"><span class="comment-age">(11 Oct '17, 13:29)</span> saisudheer8</div></div><span id="63824"></span><div id="comment-63824" class="comment"><div id="post-63824-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> <a href="https://ask.wireshark.org/users/19586/sindy">@sindy</a> This works! I was able to capture USB traffic through USBPcapCmd.exe. However, I want to capture only one Port but I get the traffic from all other ports which confuses my project. Any solution for this?</p></div><div id="comment-63824-info" class="comment-info"><span class="comment-age">(11 Oct '17, 14:37)</span> saisudheer8</div></div></div><div id="comment-tools-63813" class="comment-tools"></div><div class="clear"></div><div id="comment-63813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

