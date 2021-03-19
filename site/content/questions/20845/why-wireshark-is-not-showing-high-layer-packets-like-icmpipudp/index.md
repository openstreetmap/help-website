+++
type = "question"
title = "Why Wireshark is not showing high layer packets like ICMP/IP/UDP?"
description = '''I am using Wireshark for 802.11g sniffing. The AP is not using any encryption. I can see the beacons, the probe requests and even ARP communications from one station. But no ICMP/IP/UDP/TCP layer data packets are shown. Actually, if I filter out the beacon signal of my AP, I can see no packets at al...'''
date = "2013-04-29T12:38:00Z"
lastmod = "2013-04-29T12:38:00Z"
weight = 20845
keywords = [ "wireless", "802.11", "wireshark" ]
aliases = [ "/questions/20845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Wireshark is not showing high layer packets like ICMP/IP/UDP?](/questions/20845/why-wireshark-is-not-showing-high-layer-packets-like-icmpipudp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark for 802.11g sniffing. <strong>The AP is not using any encryption</strong>. I can see the beacons, the probe requests and even ARP communications from one station. But no ICMP/IP/UDP/TCP layer data packets are shown. Actually, if I filter out the beacon signal of my AP, I can see no packets at all, even I know clearly that same station is doing Ping right now using wireless interface. Can anybody know what went wrong?</p><p>My Wireshark version is 1.8.2. I am using a Ubuntu 12.10 and a USB wireless adaptor Belkin F5D7050. I have put the wlan interface to monitor mode with <code>airmon-ng start wlan1</code></p></div><div id="question-tags" class="tags-container tags">wireless 802.11 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '13, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/c060cad5a76755e0dc02115cad2906a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gph&#39;s gravatar image" /><p>gph<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gph has no accepted answers">0%</span></p></div></div><div id="comments-container-20845" class="comments-container"><span id="20846"></span><div id="comment-20846" class="comment"><div id="post-20846-score" class="comment-score"></div><div class="comment-text"><p>Does it work with tcpdump? (I suspect it won't, as the relevant code path is shared by tcpdump and dumpcap, the latter being the program Wireshark runs to capture traffic.)</p><p>What driver is being used with that adapter, and is there some indication of what particular model of the adapter it is?</p></div><div id="comment-20846-info" class="comment-info"><span class="comment-age">(29 Apr '13, 17:44)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-20845" class="comment-tools"></div><div class="clear"></div><div id="comment-20845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

