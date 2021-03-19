+++
type = "question"
title = "Sierra Wireless 308 HSPA adapter is not detected in interfaces or via windump on a Win7 notebook"
description = '''Hello, I&#x27;m running wireshark as admin on a win7 laptop and using a Sierra Wireless 308 HSPA adapter that I want to capture on. The wireshark &quot;interfaces&quot; dlg won&#x27;t show this interface. I am using v1.4.3 of wireshark and v4.1.2. When I run windump as admin, it does not show the Sierra Wireless 308 ad...'''
date = "2011-01-24T09:40:00Z"
lastmod = "2011-10-10T19:04:00Z"
weight = 1907
keywords = [ "interfaces" ]
aliases = [ "/questions/1907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sierra Wireless 308 HSPA adapter is not detected in interfaces or via windump on a Win7 notebook](/questions/1907/sierra-wireless-308-hspa-adapter-is-not-detected-in-interfaces-or-via-windump-on-a-win7-notebook)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm running wireshark as admin on a win7 laptop and using a Sierra Wireless 308 HSPA adapter that I want to capture on. The wireshark "interfaces" dlg won't show this interface. I am using v1.4.3 of wireshark and v4.1.2. When I run windump as admin, it does not show the Sierra Wireless 308 adapter either. Any idea what might help?</p></div><div id="question-tags" class="tags-container tags">interfaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '11, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/01522eefdc38c568a342256c33485e8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidfi&#39;s gravatar image" /><p>davidfi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidfi has no accepted answers">0%</span></p></div></div><div id="comments-container-1907" class="comments-container"><span id="6838"></span><div id="comment-6838" class="comment"><div id="post-6838-score" class="comment-score"></div><div class="comment-text"><p>Very interesting. I joined this community because I don't see the USB308 when using Wireshark 1.6.2. I have tried WinXP and Win7 Enterprise 64 bit. When I use a computer with WinXP and Wireshark 1.4.3, I can see the interface just fine.</p><p>I'm using the Generic Watcher from Sierra R 11.3.1104.1 Build 3004</p><p>Did you ever get resolution on your USB308 issue with Wireshark 1.4.3?</p></div><div id="comment-6838-info" class="comment-info"><span class="comment-age">(10 Oct '11, 15:47)</span> mwwagner</div></div><span id="6839"></span><div id="comment-6839" class="comment"><div id="post-6839-score" class="comment-score"></div><div class="comment-text"><p>Note that different versions of Wireshark on Windows might come with different versions of WinPcap; differences of that sort between versions of Wireshark are, if the two versions of Wireshark come with different versions of WinPcap, almost certainly differences between versions of WinPcap.</p></div><div id="comment-6839-info" class="comment-info"><span class="comment-age">(10 Oct '11, 18:48)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1907" class="comment-tools"></div><div class="clear"></div><div id="comment-1907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6840"></span>

<div id="answer-container-6840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6840-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If WinDump doesn't see the interface, the problem isn't with Wireshark, it's with WinPcap.</p><p>Mobile phone Internet connections almost always, if not always, use PPP as the protocol. <a href="http://www.winpcap.org/misc/faq.htm#Q-5">The WinPcap FAQ entry on PPP connections</a> says</p><blockquote><p>Q-5: <em>Can I use WinPcap on a PPP connection?</em></p><p>A: <strong>Windows NT4.</strong> It's <strong><em>not</em></strong> possible to capture on PPP/VPN connections on this operating system.</p><p><strong>Windows 2000/XP (x86)/2003 (x86).</strong> these systems have limitations in the NDIS binding process that prevent a protocol driver from working properly on WAN adapters. WinPcap 3.1 and newer offer limited support for capturing on dial-up adapters using a wrapper over the Microsoft NetMon driver.</p><p>NOTES:</p><ul><li>it is possible to capture control packets (LCP and NCP) using the "Generic Dialup" or "Generic NdisWan" adapter (which is always listed even if no dialup connections are available). Control frames are captured as Ethernet encapsulated PPP frames.</li><li>the PPP protocol is translated by the OS into a fake Ethernet. You'll see Ethernet frames and not PPP frames.</li><li>transmission is not supported.</li><li>filtering and statistics gathering is done at user level.</li></ul><p><strong>Windows XP (x64)/2003 (x64).</strong> It's <strong><em>not</em></strong> possible to capture on PPP/VPN connections on these operating systems.</p><p><strong>Windows Vista and more recent.</strong> It's <strong><em>not</em></strong> possible to capture on PPP/VPN connections on these operating systems.</p></blockquote><p>Windows 7 is more recent than Windows Vista, so there's no support for capturing on mobile phone adapters (or dial-up connections, or VPNs, or...) on Windows 7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Oct '11, 19:06</p></div></div><div id="comments-container-6840" class="comments-container"></div><div id="comment-tools-6840" class="comment-tools"></div><div class="clear"></div><div id="comment-6840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

