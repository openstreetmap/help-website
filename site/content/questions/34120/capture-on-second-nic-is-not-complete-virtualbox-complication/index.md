+++
type = "question"
title = "Capture on Second NIC is not complete - VirtualBOX Complication"
description = '''Hello MY Setup: WinXP-SP3 NIC #1: 3COM Etherlink XL 10/100 (ethernet) Bindings: Client for MS Networks; File &amp;amp; Print for MS Net; QOS; AEGIS; MS TCP/IP NIC #2: SiS 190 100/10 (ethernet) Bindings: VirtualBox Bridged Network Driver Only I use this machine as a VirtualBox Host using NIC #1 as networ...'''
date = "2014-06-24T07:09:00Z"
lastmod = "2014-06-24T07:42:00Z"
weight = 34120
keywords = [ "capture", "virtualbox" ]
aliases = [ "/questions/34120" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture on Second NIC is not complete - VirtualBOX Complication](/questions/34120/capture-on-second-nic-is-not-complete-virtualbox-complication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34120-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p><strong>MY Setup</strong>:</p><p><em>WinXP-SP3</em></p><p><strong>NIC #1</strong>: 3COM Etherlink XL 10/100 (ethernet)</p><p><strong>Bindings</strong>: Client for MS Networks; File &amp; Print for MS Net; QOS; AEGIS; MS TCP/IP</p><p><strong>NIC #2</strong>: SiS 190 100/10 (ethernet)</p><p><strong>Bindings</strong>: VirtualBox Bridged Network Driver <strong>Only</strong></p><p>I use this machine as a VirtualBox Host using NIC #1 as network connection</p><p>The VBOX Clients use the NIC #2 as their network connection</p><p>I then run Wireshark on my HOST and start a capture on NIC #2 - I then start a VBox (Windows) Client</p><p>The VBox Client has NIC #2 (Above) as ethernet and has the normal windows binding for MS networking &amp; File sharing etc</p><p>In the capture running on the HOST the traffic which is captured is not complete. The <em>only packets captured are</em> broadcast packets: ARP, NetBIOS</p><p>Any packet which is not a broadcast is not captured and not seen.</p><p><em>Now that I have written this all out logically, I believe I partially understand what is happening.</em></p><p>When a packet arrives at the VBOX Client which is addressed to that client the VBOX bridge adapter pushes the packet to the appropriate machine IP stack which means it is not seen by the VBOX Host machine.</p><p>When a packet arrives at the VBOX Client which is a broadcast address the VBOX bridge adapter (presumably) allows the packet to be seen by other processes which may be listening on the VBOX Host, such as a second VBOX Client participating in the same broadcast space.</p><p>This is (presumably) when the VBOX Host sees the packet and it is captured by WINPCap on the VBOX Host.</p><p>Side note: Running Wireshark on the VBOX Client virtual machine works normally and all packets are seen.</p><p>Is it possible to have WINPCap "<em>sit lower down, be closer to the wire</em>" than any other process ? Namely, <em>before</em> the VBOX bridge driver - No doubt .. it is not.</p><p>One last question that you may be able to answer but this is more my ignorance of how Wireshark is written - My understanding (which is clearly wrong) was that a "sniffer" listened to the physical wire OSI-Layer 1 and as such was first to see everything .. ?</p><p>Thanks for taking the time to read this - please file it appropriately and make any edits/tags you feel are necessary.</p></div><div id="question-tags" class="tags-container tags">capture virtualbox</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '14, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/1c954b3b6f77ecde52a6fc12c5e6d77e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unstruct&#39;s gravatar image" /><p>unstruct<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unstruct has no accepted answers">0%</span></p></div></div><div id="comments-container-34120" class="comments-container"></div><div id="comment-tools-34120" class="comment-tools"></div><div class="clear"></div><div id="comment-34120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34124"></span>

<div id="answer-container-34124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34124-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This isn't a Wireshark question. The application used by Wireshark to capture on Windows is <a href="https://www.winpcap.org/">WinPCap</a>, you might get help for the issue over there.</p><p>Having said that, it may well be down to the fact that WinPCap is an NDIS 5 driver, and only NDIS 6 allows positioning anywhere in the stack. Unfortunately rewriting WinPCap to be an NDIS 6 driver is a significant undertaking.</p><p>Wireshark depends on other applications (WinPCap or libpcap) to actually sniff the traffic using the host OS facilities, and does not itself have access to the any part of the network stack.</p><p>Your issue may also be caused by VPN and AV software that installs filter drivers in the stack and prevents WinPCap from seeing the traffic, do you have any such software installed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34124" class="comments-container"><span id="34125"></span><div id="comment-34125" class="comment"><div id="post-34125-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I removed my AV &amp; Firewall (No VPN running) so I am sure that is not the issue - It is simply due to the VirtualBox Bridge driver ... As you say "This isn't a wireshark question" .. but I am happy to work with what I have now I understand the problem better.</p></div><div id="comment-34125-info" class="comment-info"><span class="comment-age">(24 Jun '14, 07:51)</span> unstruct</div></div></div><div id="comment-tools-34124" class="comment-tools"></div><div class="clear"></div><div id="comment-34124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

