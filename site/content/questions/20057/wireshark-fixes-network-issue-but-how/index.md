+++
type = "question"
title = "Wireshark &#x27;fixes&#x27; network issue - but how?"
description = '''Hi All. Here&#x27;s the situation. My company has two sites. The two sites are connected via a sonicwall VPN. We have a licence server that provides software licences via UDP port 5093 at one of the sites. Clients local to that site can pull licences without a problem. Clients at the remote site cannot. ...'''
date = "2013-04-03T07:57:00Z"
lastmod = "2013-04-03T08:45:00Z"
weight = 20057
keywords = [ "udp", "vpn", "licence", "server" ]
aliases = [ "/questions/20057" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 'fixes' network issue - but how?](/questions/20057/wireshark-fixes-network-issue-but-how)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All.</p><p>Here's the situation. My company has two sites. The two sites are connected via a sonicwall VPN. We have a licence server that provides software licences via UDP port 5093 at one of the sites. Clients local to that site can pull licences without a problem. Clients at the remote site cannot.</p><p>If i start wireshark on a remote client and perform a packet capture of all traffic on UDP 5093. that client 'magically' works and pulls a licence off of the licenece server.</p><p>I'm trying to understand why that might be to help me troubleshoot the issue. Can anyone help?</p><p>Many thanks, Matt.</p></div><div id="question-tags" class="tags-container tags">udp vpn licence server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/e5c37808c97d8cd5533c8d6c2f9fffb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mac_xpert&#39;s gravatar image" /><p>mac_xpert<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mac_xpert has no accepted answers">0%</span></p></div></div><div id="comments-container-20057" class="comments-container"></div><div id="comment-tools-20057" class="comment-tools"></div><div class="clear"></div><div id="comment-20057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20058"></span>

<div id="answer-container-20058" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20058-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark by default enables promiscuous mode on the network adapter on which it captures. This means the NIC will now forward all packets to the IP stack instead of just the unicasts for its own mac-address and the broadcasts (and subscribed multicasts).</p><p>You can check whether that's indeed the reason for the license to work by capturing again, but this time without enabling promiscuous mode (in the capture options). If the licensing now fails again, it was indeed the promiscuous mode that made it work magically...</p><p>The next thing to do is find out why the returning packets from the license server are not being forwarded by your NIC. What is the destination mac-address in those packets? Is it a multicast address to which the NIC is not registered? Is it a wrong unicast mac-address?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20058" class="comments-container"><span id="20060"></span><div id="comment-20060" class="comment"><div id="post-20060-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I'll test your suggestion. I have found a fix for the problem, but i'm not sure what the root of the issue is yet. If i set the MTU on the local network adapter on the client PC down to 1370 then the licencing works perfectly, wheras at the standard 1500 setting it gave us problems.</p></div><div id="comment-20060-info" class="comment-info"><span class="comment-age">(03 Apr '13, 09:09)</span> mac_xpert</div></div><span id="20063"></span><div id="comment-20063" class="comment"><div id="post-20063-score" class="comment-score"></div><div class="comment-text"><p>In that case, have a look at fragmentation at the IP layer. VPN's encapsulate packets and can therefore create packets which are too big for the network. IP will then fragment them if the DF bit is not set or will send an "ICMP fragmentation needed, but DF bit set" back to the sender when the DF is set.</p><p>You can set up your VPN devices to alter the MSS value in the TCP SYN packets to make sure all (TCP) packets are small enough to not need fragmentation. However, this will not solve things for UDP. What protocol does the licensing application use?</p></div><div id="comment-20063-info" class="comment-info"><span class="comment-age">(03 Apr '13, 10:00)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-20058" class="comment-tools"></div><div class="clear"></div><div id="comment-20058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

