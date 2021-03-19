+++
type = "question"
title = "Promiscuous mode implies Monitor Mode compatibility?"
description = '''I mean, I just want to put my wireless card interface into promiscuous mode to scan my wireless network I&#x27;m connected to. Do I necessarily need a monitor mode wifi card compatible? Should I necessarily set my interface promiscuous flag on before running Wireshark using its promiscuous mode? (Ubuntu ...'''
date = "2014-07-19T11:58:00Z"
lastmod = "2014-07-19T12:49:00Z"
weight = 34774
keywords = [ "promiscuous" ]
aliases = [ "/questions/34774" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscuous mode implies Monitor Mode compatibility?](/questions/34774/promiscuous-mode-implies-monitor-mode-compatibility)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I mean, I just want to put my wireless card interface into promiscuous mode to scan my wireless network I'm connected to. Do I necessarily need a monitor mode wifi card compatible?</p><p>Should I necessarily set my interface promiscuous flag on before running Wireshark using its promiscuous mode? (Ubuntu 12.04LTS)</p><pre><code>sudo ip link set wlan0 promisc on</code></pre><p>I've already tried that without having a monitor compatible card without success. I only recieve broadcast and multicast packets.</p></div><div id="question-tags" class="tags-container tags">promiscuous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '14, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/5f6001f7b74af5228928f35770f0d79e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redraw&#39;s gravatar image" /><p>redraw<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redraw has no accepted answers">0%</span></p></div></div><div id="comments-container-34774" class="comments-container"></div><div id="comment-tools-34774" class="comment-tools"></div><div class="clear"></div><div id="comment-34774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34775"></span>

<div id="answer-container-34775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34775-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Monitor mode is required to capture wireless traffic not destined for the capturing host. See the wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">wlan</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '14, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '14, 12:50</p></div></div><div id="comments-container-34775" class="comments-container"><span id="34776"></span><div id="comment-34776" class="comment"><div id="post-34776-score" class="comment-score"></div><div class="comment-text"><p>It says: "In promiscuous mode the MAC address filter mentioned above is disabled and all packets of the currently joined 802.11 network (with a specific SSID and channel) are captured." That's what I want to do. Capture packets from my joined WLAN network. So, why should I need monitor mode? I only trying to put my interface into promiscuous mode, but I only recieve broadcast and multicast packets.</p></div><div id="comment-34776-info" class="comment-info"><span class="comment-age">(19 Jul '14, 12:58)</span> redraw</div></div><span id="34781"></span><div id="comment-34781" class="comment"><div id="post-34781-score" class="comment-score"></div><div class="comment-text"><p>It also says "Promiscuous mode is, in theory, possible on many 802.11 adapters, but often does not work in practice; if you specify promiscuous mode, the attempt to enable promiscuous mode may fail, the adapter might only capture traffic to and from your machine, or the adapter might not capture any packets."</p></div><div id="comment-34781-info" class="comment-info"><span class="comment-age">(19 Jul '14, 14:43)</span> grahamb ♦</div></div><span id="34783"></span><div id="comment-34783" class="comment"><div id="post-34783-score" class="comment-score"></div><div class="comment-text"><p>Ok. So that's another compatibility list I should see: the promiscuous mode compatible cards maybe? Or it has to be with Wireshark+interface issues?</p></div><div id="comment-34783-info" class="comment-info"><span class="comment-age">(19 Jul '14, 15:40)</span> redraw</div></div><span id="34784"></span><div id="comment-34784" class="comment"><div id="post-34784-score" class="comment-score"></div><div class="comment-text"><p>One last question @grahamb ♦. I could sniff packets using ettercap with ARP poisoning and MITM. So I recieve the packets and foward them to the router. So, why promiscuous mode wouldn't see those packets just listening on the wifi area (without arp spoofing/mitm)?</p></div><div id="comment-34784-info" class="comment-info"><span class="comment-age">(19 Jul '14, 19:40)</span> redraw</div></div><span id="34788"></span><div id="comment-34788" class="comment"><div id="post-34788-score" class="comment-score"></div><div class="comment-text"><p>AFAIK it's down to the NIC drivers and how they filter traffic. There's nothing much that libpcap can do about it.</p></div><div id="comment-34788-info" class="comment-info"><span class="comment-age">(20 Jul '14, 03:42)</span> grahamb ♦</div></div></div><div id="comment-tools-34775" class="comment-tools"></div><div class="clear"></div><div id="comment-34775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

