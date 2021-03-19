+++
type = "question"
title = "How to capture IP addresses between two local PC and Switch"
description = '''I have a windows 7 laptop connected to a dell 2848 switch. I need to know the IP address of the dell switch. I have the MAC address. Is there a process for capturing the IP information between the two devices. I&#x27;m connected via Ethernet cable to a port on the switch.'''
date = "2015-08-05T13:06:00Z"
lastmod = "2015-08-05T14:22:00Z"
weight = 44885
keywords = [ "ipaddress" ]
aliases = [ "/questions/44885" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture IP addresses between two local PC and Switch](/questions/44885/how-to-capture-ip-addresses-between-two-local-pc-and-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44885-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a windows 7 laptop connected to a dell 2848 switch. I need to know the IP address of the dell switch. I have the MAC address. Is there a process for capturing the IP information between the two devices. I'm connected via Ethernet cable to a port on the switch.</p></div><div id="question-tags" class="tags-container tags">ipaddress</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/e30c258725bd9ce2474c8c5bdfafa296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bdlif&#39;s gravatar image" /><p>bdlif<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bdlif has no accepted answers">0%</span></p></div></div><div id="comments-container-44885" class="comments-container"></div><div id="comment-tools-44885" class="comment-tools"></div><div class="clear"></div><div id="comment-44885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44890"></span>

<div id="answer-container-44890" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44890-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Devices connected to a switch generally communicate with each other; that is, they communicate <em>through</em> the switch, but they don't communicate <em>with</em> the switch, therefore, the switch's IP address won't normally show up in a Wireshark trace. To find the switch's IP address, you need to force it to transmit a packet. I suggest using something like the SoftPerfect Network Scanner (NetScan, available as a free download <a href="https://www.softperfect.com/products/networkscanner/">here</a>) to scan your entire network, which will make the switch respond to the scan. You won't need Wireshark. You'll be able to see the switch's response right in NetScan. You'll also see the MAC address of each device that responds. Since you already know the switch's MAC address, it should be easy for you to pick out the switch from all the devices that respond.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-44890" class="comments-container"></div><div id="comment-tools-44890" class="comment-tools"></div><div class="clear"></div><div id="comment-44890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

