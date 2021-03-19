+++
type = "question"
title = "WinPcap/NPF not in the Device Manager"
description = '''Hello When installing Wireshark in a Windows XP Virtual Macine, I saw that WinPcap was installed, yet it is not showing up in the Device Manager. From the Device Manager you can select View-&amp;gt;Show hidden devices, then open Non-Plug and Play Drivers and right click on NetGroup Packet Filter Driver....'''
date = "2012-01-08T17:17:00Z"
lastmod = "2012-01-09T12:23:00Z"
weight = 8281
keywords = [ "winpcap" ]
aliases = [ "/questions/8281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WinPcap/NPF not in the Device Manager](/questions/8281/winpcapnpf-not-in-the-device-manager)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8281-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello When installing Wireshark in a Windows XP Virtual Macine, I saw that WinPcap was installed, yet it is not showing up in the Device Manager.</p><p>From the Device Manager you can select View-&gt;Show hidden devices, then open Non-Plug and Play Drivers and right click on NetGroup Packet Filter Driver. In the driver properties you can set the startup type as well as start and stop the driver manually.</p><p>In Windows XP I could only find the "Computer Management (local)/Device Manager" and the NetGroup does not show up, and neither the NPF.</p><p>Question; Does WinPcap/NPF work with a Virtual OS? The NPF driver does show up in the Registry; <code>HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NPF\Start</code> from 0x3 (<code>SERVICE_DEMAND_START</code>) to 0x2 (<code>SERVICE_AUTO_START</code>) or 0x1 (<code>SERVICE_SYSTEM_START</code>).</p></div><div id="question-tags" class="tags-container tags">winpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '12, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/6c566db4ab452f1914ca1a13e35151ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="will&#39;s gravatar image" /><p>will<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="will has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '12, 11:44</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8281" class="comments-container"></div><div id="comment-tools-8281" class="comment-tools"></div><div class="clear"></div><div id="comment-8281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8286"></span>

<div id="answer-container-8286" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8286-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what type of virtual machine you have, but I run Windows XP on a virtual machine under VMware Fusion on Mac OS X. It has Wireshark and WinPcap installed, and if I open "Properties" for "My Computer", select the "Hardware" tab, open "Device Manager" with the button, select View -&gt; Show hidden devices, open up Non-Plug and Play Drivers, and control-click (this is a MacBook Pro, that's the only "right click" I can do :-)) on NetGroup Packet Filter Driver and select Properties from the menu, I get a "NetGroup Packet Filter Driver Properties" window.</p><p>And, yes, I can capture traffic with Wireshark on that virtual machine.</p><p>What happens if you do the same?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '12, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8286" class="comments-container"><span id="8287"></span><div id="comment-8287" class="comment"><div id="post-8287-score" class="comment-score"></div><div class="comment-text"><p>Guy, I have Windows XP Mode – Virtual Machine Shell Information (.vmcx)and was able to find NDF in the Program Files. I have been trying to capture data, and I have the interface correct, but it does not capture any.</p></div><div id="comment-8287-info" class="comment-info"><span class="comment-age">(09 Jan '12, 12:35)</span> will</div></div><span id="8288"></span><div id="comment-8288" class="comment"><div id="post-8288-score" class="comment-score"></div><div class="comment-text"><p>I should add that it is a company PC and I have requested from IT if I could get VMWare Fusion. If there are $$$ involved they will probably say no.</p></div><div id="comment-8288-info" class="comment-info"><span class="comment-age">(09 Jan '12, 13:57)</span> will</div></div><span id="8289"></span><div id="comment-8289" class="comment"><div id="post-8289-score" class="comment-score"></div><div class="comment-text"><p>If your company PC is running Windows or Linux one would <em>hope</em> they'd say no! VMware Fusion is the Mac client version. For Windows or Linux, the client would be VMware Workstation; I suspect from the ".vmcx" that you have <em>some</em> VMware software for the virtual machine.</p><p>As for capturing the traffic, try <a href="http://www.microsoft.com/download/en/details.aspx?id=4865">downloading Microsoft Network Monitor</a> and seeing whether it can capture traffic.</p></div><div id="comment-8289-info" class="comment-info"><span class="comment-age">(09 Jan '12, 14:14)</span> Guy Harris ♦♦</div></div><span id="8297"></span><div id="comment-8297" class="comment"><div id="post-8297-score" class="comment-score"></div><div class="comment-text"><p>Wirehark runs and captures successfully for me using a vanilla XP Mode virtual machine. Have you modified the network settings of the VM in anyway (from the VM Settings, not within the VM)?</p><p>.vmcx is the extension for the XP Mode VM settings file. This is Microsoft's VM technology in Windows 7, not VMWare.</p></div><div id="comment-8297-info" class="comment-info"><span class="comment-age">(10 Jan '12, 03:20)</span> grahamb ♦</div></div></div><div id="comment-tools-8286" class="comment-tools"></div><div class="clear"></div><div id="comment-8286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

