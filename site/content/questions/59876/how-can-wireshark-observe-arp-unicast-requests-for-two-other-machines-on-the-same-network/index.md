+++
type = "question"
title = "How can Wireshark observe ARP unicast requests for two other machines on the same network?"
description = '''I have three machines that are part of the same network - computer A, which is running Wireshark, computer B, and printer C. I have a packet capture log showing computer B&#x27;s MAC address flooding the network with unicast ARP requests to printer C&#x27;s MAC address, asking about the owner of printer C&#x27;s I...'''
date = "2017-03-06T20:07:00Z"
lastmod = "2017-03-06T21:08:00Z"
weight = 59876
keywords = [ "arp", "unicast" ]
aliases = [ "/questions/59876" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can Wireshark observe ARP unicast requests for two other machines on the same network?](/questions/59876/how-can-wireshark-observe-arp-unicast-requests-for-two-other-machines-on-the-same-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59876-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have three machines that are part of the same network - computer A, which is running Wireshark, computer B, and printer C. I have a packet capture log showing computer B's MAC address flooding the network with unicast ARP requests to printer C's MAC address, asking about the owner of printer C's IP address and asking for a response to computer B's IP address. Printer C is disconnected from the network when this happens. How can Wireshark running on computer A be recording this, given that all of the ARP requests are unicast, not broadcast?</p></div><div id="question-tags" class="tags-container tags">arp unicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '17, 20:07</strong></p><img src="https://secure.gravatar.com/avatar/3cdfc32284611c7fd6c74d494c932586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdm&#39;s gravatar image" /><p>jdm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdm has no accepted answers">0%</span></p></div></div><div id="comments-container-59876" class="comments-container"></div><div id="comment-tools-59876" class="comment-tools"></div><div class="clear"></div><div id="comment-59876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59879"></span>

<div id="answer-container-59879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59879-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ARP request is broadcast, not unicast. This is why it is ARP'ing in the first place...to find the mac address with the destination IP address. Look at the destination mac in the L2 Ethernet header, it will be FF:FF:FF:FF:FF:FF</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '17, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Mar '17, 21:11</p></div></div><div id="comments-container-59879" class="comments-container"></div><div id="comment-tools-59879" class="comment-tools"></div><div class="clear"></div><div id="comment-59879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

