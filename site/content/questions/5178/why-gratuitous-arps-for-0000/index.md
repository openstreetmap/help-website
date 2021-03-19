+++
type = "question"
title = "Why gratuitous ARPs for 0.0.0.0?"
description = '''In a trace file I captured today, I noticed four packets that Wireshark identified as “Gratuitous ARP for 0.0.0.0 (request).” I know that an ARP probe should come from 0.0.0.0, but these four packets were both FROM and TO 0.0.0.0. They are not RARPs or inverse ARPs. eth.type is ARP (0x0806), not RAR...'''
date = "2011-07-22T21:16:00Z"
lastmod = "2011-07-24T09:14:00Z"
weight = 5178
keywords = [ "arp", "gratuitous" ]
aliases = [ "/questions/5178" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why gratuitous ARPs for 0.0.0.0?](/questions/5178/why-gratuitous-arps-for-0000)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a trace file I captured today, I noticed four packets that Wireshark identified as “Gratuitous ARP for 0.0.0.0 (request).” I know that an ARP probe should come from 0.0.0.0, but these four packets were both FROM and TO 0.0.0.0.</p><p>They are not RARPs or inverse ARPs. eth.type is ARP (0x0806), not RARP (0x8035). arp.opcode is 1 (request), not 3 (reverse request) or 8 (inverse request).</p><p>In the ARP portion of the packet, the Sender MAC Address is 00:00:85:9c:21:ca, which is the same as the Ethernet source address. The 00:00:85 OUI identifies this as a Canon NIC. It's probably a small all-in-one printer/scanner/copier/fax. The Sender IP Address and Target IP Address are both 0.0.0.0. The Target MAC Address is 00:00:00:00:00:00.</p><p>With a Target IP address of 0.0.0.0, it's not doing address conflict detection, and it's not looking up the MAC address associated with an IP address. What is the purpose of these packets?</p></div><div id="question-tags" class="tags-container tags">arp gratuitous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '11, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '11, 21:20</p></div></div><div id="comments-container-5178" class="comments-container"></div><div id="comment-tools-5178" class="comment-tools"></div><div class="clear"></div><div id="comment-5178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5193"></span>

<div id="answer-container-5193" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5193-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've seen this happen when an embedded platform starts up, the network software stack starts and attaches to the Ethernet interface. Since it's not configured with an IP address yet (DHCP pending) the attachment takes place with the Null IP address. This results in the mentioned ARP.</p><p>After the DHCP client does its thing, a new ARP is seen, with the correct IP address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '11, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5193" class="comments-container"></div><div id="comment-tools-5193" class="comment-tools"></div><div class="clear"></div><div id="comment-5193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5181"></span>

<div id="answer-container-5181" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5181-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First thing that comes to mind is that these arp packets might be used to advertise ones presence on the network to some managing software. Maybe a Canon Camera that want to be found by the camera software? Or like you said, a printer that wants to be found automagically by the driver?</p><p>Please note that this is just a hunch, not from real life experience! :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '11, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5181" class="comments-container"></div><div id="comment-tools-5181" class="comment-tools"></div><div class="clear"></div><div id="comment-5181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

