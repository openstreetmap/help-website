+++
type = "question"
title = "Wireshark can&#x27;t capture multicast packet in promiscuous mode without IGMP join"
description = '''I write a program to send multicast packets to 225.0.0.37 continuously on a Linux box, then I use wireshark in promiscuous mode on my Mac to see if it can see the packets, but no good. Both of them are connected to the same wifi. I know I should send IGMP join message first if I want to receive the ...'''
date = "2017-03-07T21:49:00Z"
lastmod = "2017-03-08T02:58:00Z"
weight = 59905
keywords = [ "igmp", "promiscuous", "wifi", "multicast" ]
aliases = [ "/questions/59905" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark can't capture multicast packet in promiscuous mode without IGMP join](/questions/59905/wireshark-cant-capture-multicast-packet-in-promiscuous-mode-without-igmp-join)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I write a program to send multicast packets to 225.0.0.37 continuously on a Linux box, then I use wireshark in promiscuous mode on my Mac to see if it can see the packets, but no good. Both of them are connected to the same wifi. I know I should send IGMP join message first if I want to receive the multicast message in general(I did receive if I send IGMP join), but if I am in promiscuous mode, I should see the packets anyway. Is my understanding wrong?</p></div><div id="question-tags" class="tags-container tags">igmp promiscuous wifi multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/75de90cd2dddc1467b3f3db8d49dfb30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfly&#39;s gravatar image" /><p>jfly<br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfly has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '17, 22:45</p></div></div><div id="comments-container-59905" class="comments-container"></div><div id="comment-tools-59905" class="comment-tools"></div><div class="clear"></div><div id="comment-59905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59912"></span>

<div id="answer-container-59912" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59912-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The IGMP report or join is used to indicate to the infrastructure your intent to consume the multicast group. This way, the infrastructure knows to forward the group to your physical interface.</p><p>Promiscuous mode allows the network interface on your system to pass up all frames and not provide any type of filter. However, if the infrastructure is not sending them to the interface, promisc mode will not help - they are not there to be passed up.<br />
</p><p>So you really need both: the infrastructure has to send you the frames, and then they need to be sent up the stack for handling in the packet capture tool.</p><p>Now WiFi adds an entirely different level of complexity. Multicast is handled in very different ways by different WiFi systems. For instance: some do a multicast_to_unicast conversion, sometimes; some don't send out multicast at all and they just drop it; some send any multicast received from wireless right back on the wireless side but are selective about wired side; some manage their own IGMP snooping states and only transmit multicast if a host asked for it, and this can be either as true multicast or unicast. If encryption is used, multicast or unicast is important because the encryption keys from WPA2 would be different in the two cases.</p><p>On top of this, all multicast sent from a host to the network over WiFi are actually unicast at layer 2 (802.11) destined for the access point so you will only see this traffic if you are in monitor+promisc mode on a wifi capture system.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-59912" class="comments-container"></div><div id="comment-tools-59912" class="comment-tools"></div><div class="clear"></div><div id="comment-59912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

