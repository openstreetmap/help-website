+++
type = "question"
title = "Wireshark cannot see wireless interface on Ubuntu on virtual machine"
description = '''Hello, I have installed wireshark on ubuntu through VM.I could just simplify everything and install it on my normal OS (windows 10), but I would like it in my open source OS just so I can get more familiar with it.  The whireshark version I am using is: 1.12.1 The problem I have is, when I check the...'''
date = "2016-09-12T18:13:00Z"
lastmod = "2016-09-12T21:24:00Z"
weight = 55503
keywords = [ "ubuntu", "vm", "wireshark" ]
aliases = [ "/questions/55503" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark cannot see wireless interface on Ubuntu on virtual machine](/questions/55503/wireshark-cannot-see-wireless-interface-on-ubuntu-on-virtual-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55503-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have installed wireshark on ubuntu through VM.I could just simplify everything and install it on my normal OS (windows 10), but I would like it in my open source OS just so I can get more familiar with it.</p><p>The whireshark version I am using is: 1.12.1</p><p>The problem I have is, when I check the interfaces, there is nothing in regards to my network. When I type in the command "tshark -D" I get the following:</p><ol><li>eth0</li><li>any</li><li>lo (Loopback)</li><li>bluetooth-monitor</li><li>nflog</li><li>nfqueue</li><li>usbmon1</li></ol><p>None of these are referring to my wireless network. I am currently using my school campus WiFi and it is not showing up. Also, when I check all of these interfaces, there is 0 package flow</p></div><div id="question-tags" class="tags-container tags">ubuntu vm wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '16, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/27e181ea31a62600c2c08d1e5c1c0033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alex067&#39;s gravatar image" /><p>alex067<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alex067 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '16, 22:45</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55503" class="comments-container"></div><div id="comment-tools-55503" class="comment-tools"></div><div class="clear"></div><div id="comment-55503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55506"></span>

<div id="answer-container-55506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have installed wireshark on ubuntu through VM</p></blockquote><p>...</p><blockquote><p>None of these are referring to my wireless network.</p></blockquote><p>Your virtual machine might not have a (virtual) wireless adapter; all the VMs on VMware Fusion on my MacBook Pro have Ethernet interfaces but no Wi-Fi interfaces, even though the MacBook Pro has no Ethernet interface unless I plug in my Thunderbolt Ethernet adapter.</p><p>If you want to capture on your wireless network, you'll have to run Wireshark (or tcpdump or whatever) on the <em>host</em> machine, not a VM guest, unless whatever VM software you're using has the ability to provide a virtual Wi-Fi adapter, or unless you get a USB Wi-Fi adapter, plug it into your machine, and have the OS and VM software attach it to the Ubuntu guest rather than to the host (assuming that there's a driver for it in Ubuntu).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 21:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55506" class="comments-container"><span id="55507"></span><div id="comment-55507" class="comment"><div id="post-55507-score" class="comment-score"></div><div class="comment-text"><p>I see, but how come I can access the internet through my ubuntu? It says it is connected to a wireless network at the top right, which I would assume indicates that I am indeed connected to the internet through the guest machine, as well as the host?</p></div><div id="comment-55507-info" class="comment-info"><span class="comment-age">(12 Sep '16, 22:04)</span> alex067</div></div><span id="55509"></span><div id="comment-55509" class="comment"><div id="post-55509-score" class="comment-score"></div><div class="comment-text"><p>It is because the virtualization software includes an internal switch or router to which the virtual ethernet adapter of each VM is "connected". But this switch handles ethernet frames, not 802.11 ones; only the ethernet "part" of a received 802.11 frame (simplifying a bit) is extracted and sent to the switch, and vice versa, when your VM sends an ethernet frame, it is encapsulated into an 802.11 and sent out. So from the VM, you cannot control (or at least read from) the wireless interface directly.</p></div><div id="comment-55509-info" class="comment-info"><span class="comment-age">(12 Sep '16, 22:18)</span> sindy</div></div></div><div id="comment-tools-55506" class="comment-tools"></div><div class="clear"></div><div id="comment-55506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

