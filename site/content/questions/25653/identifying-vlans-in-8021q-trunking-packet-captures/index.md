+++
type = "question"
title = "Identifying VLANs in 802.1Q Trunking packet captures"
description = '''I have a client with servers connecting to my Cisco Nexus switches on trunked interfaces. The switch ports are configured with a native VLAN, being the server&#x27;s primary VLAN for PXE boot, and a second VLAN for VM clients. The client would like to be able to identify the VLANs allowed on the trunk fr...'''
date = "2013-10-04T11:19:00Z"
lastmod = "2013-10-05T00:42:00Z"
weight = 25653
keywords = [ "802.1q" ]
aliases = [ "/questions/25653" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying VLANs in 802.1Q Trunking packet captures](/questions/25653/identifying-vlans-in-8021q-trunking-packet-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25653-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client with servers connecting to my Cisco Nexus switches on trunked interfaces. The switch ports are configured with a native VLAN, being the server's primary VLAN for PXE boot, and a second VLAN for VM clients. The client would like to be able to identify the VLANs allowed on the trunk from the server-end, so he can verify the configuration when troubleshooting PXE boot or VM connectivity issues.<br />
</p><p>Is there a protocol that is transmitted, or can be transmitted, in broadcast that should allow a packet capture to reveal all VLANs permitted on a trunk? I know we can learn the native VLAN, but I'm looking for a way for the server to "hear" the whole VLAN range.</p><p>everyone's help is greatly appreciated.</p><p>Dan</p></div><div id="question-tags" class="tags-container tags">802.1q</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/614d9bc2124ffee177bd70cc3e168e5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan%20Walker&#39;s gravatar image" /><p>Dan Walker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan Walker has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-25653" class="comments-container"></div><div id="comment-tools-25653" class="comment-tools"></div><div class="clear"></div><div id="comment-25653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="25657"></span>

<div id="answer-container-25657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25657-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>VLANs can be (are probably the majority of the time) configured statically. So in the case you just will see packets like ARPs being sent with the different VLAN tags. Protocols that advertise VLAN configuration include Cisco's proprietary VTP and the open standard GVRP. But these would need to be turned on at your switch. I'm not sure whether they advertise unless they know (maybe through STP) that the other side is a switch.</p><p>Not really a Wireshark oriented question (though obviously WS will help you see what is going on), but I hope this is useful.</p><p>Of course the real solution to your problem is to use some "operational orchestration" in your environment that configures your virtualisation platform AND your network at the same time ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-25657" class="comments-container"></div><div id="comment-tools-25657" class="comment-tools"></div><div class="clear"></div><div id="comment-25657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25661"></span>

<div id="answer-container-25661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25661-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Nexus should support VTP, which could allow you to advertise vlan info on trunk links (only), as untagged multicast frames with the same destination MAC as CDP (0100:0ccc:cccc). To clarify the other answer, the control is on whether a trunk has been formed and what VTP mode the switch is in, and is not dependent on STP to detect a switch on the other side.</p><p>However, configuring VTP does more than just give the server this info. That protocol is the spawn of the devil IMO, and even Cisco design curriculum suggests against its use in general. You should be hard-coding your vlan information on your trunk links, and you should know/document what those vlan numbers are.</p><p>For an initial integration effort, I hear you (misconfigured vlan numbers between end systems can be a pain). One way to check though with Wireshark is have the client and server send each traffic type to each other with Wireshark running between them, so you can easily see who is tagging what.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '13, 20:32</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '13, 20:35</p></div></div><div id="comments-container-25661" class="comments-container"></div><div id="comment-tools-25661" class="comment-tools"></div><div class="clear"></div><div id="comment-25661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25666"></span>

<div id="answer-container-25666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25666-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the servers themselves are connected on a vlan tagged interface you can create a vlan tagged port on the vSwitch inside the server and create a VM on it to capture the (arp) traffic. It will show the vlan tags (assuming the NIC in the VM is configured correctly to not strip the vlan tag, see <a href="http://wiki.wireshark.org/CaptureSetup/VLAN).">http://wiki.wireshark.org/CaptureSetup/VLAN).</a></p><p>The client can then configure the appropriate vlan portgroups on the vSwitch and attach the VMs to them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '13, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25666" class="comments-container"></div><div id="comment-tools-25666" class="comment-tools"></div><div class="clear"></div><div id="comment-25666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

