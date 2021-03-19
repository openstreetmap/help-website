+++
type = "question"
title = "ssdp issue?"
description = '''Inside Linux VM I&#x27;ve started tcpdump to capture on it&#x27;s NIC and I&#x27;ve opened the trace file in Wireshark. What i don&#x27;t understand why do I see packets originating from a different IP source address that is assigned on the VM&#x27;s NIC (even the Layer 2 address is not matching). These are SSDP packets btw...'''
date = "2016-08-23T02:30:00Z"
lastmod = "2016-08-23T02:30:00Z"
weight = 55064
keywords = [ "ssdp" ]
aliases = [ "/questions/55064" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ssdp issue?](/questions/55064/ssdp-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55064-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Inside Linux VM I've started tcpdump to capture on it's NIC and I've opened the trace file in Wireshark. What i don't understand why do I see packets originating from a different IP source address that is assigned on the VM's NIC (even the Layer 2 address is not matching). These are SSDP packets btw.</p><p>Any ideas?<br />
</p></div><div id="question-tags" class="tags-container tags">ssdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '16, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-55064" class="comments-container"><span id="55067"></span><div id="comment-55067" class="comment"><div id="post-55067-score" class="comment-score"></div><div class="comment-text"><p>Why are you surprised by receiving packets on your VM's network interface? Are you saying this NIC is not connected?</p></div><div id="comment-55067-info" class="comment-info"><span class="comment-age">(23 Aug '16, 04:45)</span> Jaap ♦</div></div><span id="55068"></span><div id="comment-55068" class="comment"><div id="post-55068-score" class="comment-score"></div><div class="comment-text"><p>When running netstat -g ( I use this to see all sockets which are bound to a multicast address) I can see only the following IPv6/IPv4 Group Membership :</p><p>224.0.0.1 - The All Hosts multicast group addresses all hosts on the same network segment.</p><p>So why I can SSDP packet targeted to multicast address 239.255.255.250 ?</p></div><div id="comment-55068-info" class="comment-info"><span class="comment-age">(23 Aug '16, 05:07)</span> adasko</div></div><span id="55069"></span><div id="comment-55069" class="comment"><div id="post-55069-score" class="comment-score">1</div><div class="comment-text"><p>The fact that you are receiving multicast traffic at your network interface is not that unusual. The actual joined MC group (All Hosts) is what's being accepted by the network stack, but lower down more traffic may come in. This has to do with the way multicast addresses are mapped onto MAC addresses, and how the (HW/emulated)NIC can filter those.</p></div><div id="comment-55069-info" class="comment-info"><span class="comment-age">(23 Aug '16, 05:36)</span> Jaap ♦</div></div><span id="55071"></span><div id="comment-55071" class="comment"><div id="post-55071-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure i understood you correctly, but do you mean that we should be able to see ALL multicast traffic even if promiscuous mode is not enabled ? Please correct me if I misunderstood you.</p></div><div id="comment-55071-info" class="comment-info"><span class="comment-age">(23 Aug '16, 06:19)</span> adasko</div></div><span id="55075"></span><div id="comment-55075" class="comment"><div id="post-55075-score" class="comment-score">1</div><div class="comment-text"><p>That's correct. Broadcast and often also multicast traffic is received even if promiscuous mode is off because the <strong>hardware</strong> MAC address filter on the network card always lets frames with broadcast or multicast destination MAC through. "Promiscuous mode on" actually means "switch off the destination MAC address filter", but the filter only acts on unicast MAC addresses.</p><p>What @Jaap was saying is that if your machine has not subscribed to some multicast group, frames with that group's MAC address as destination are ignored by the IP stack in the kernel even though the MAC filter on the network card lets them in.</p><p>This may vary, however, depending on the driver and hardware capabilities of the card, some cards may save the kernel from extra load by using more complex filters which can let through only multicast frames with a particular group's destination MAC address. In your case of a <strong>virtual</strong> NIC, it doesn't make a difference whether the multicast frames are filtered at one place or the other if it is always the CPU which provides that functionality.</p></div><div id="comment-55075-info" class="comment-info"><span class="comment-age">(23 Aug '16, 07:09)</span> sindy</div></div></div><div id="comment-tools-55064" class="comment-tools"></div><div class="clear"></div><div id="comment-55064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

