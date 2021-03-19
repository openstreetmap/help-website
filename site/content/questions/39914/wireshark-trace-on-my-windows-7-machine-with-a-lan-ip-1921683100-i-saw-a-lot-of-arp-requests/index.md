+++
type = "question"
title = "Wireshark trace on my Windows 7 machine with a LAN IP 192.168.3.100. I saw a lot of ARP requests"
description = '''I ran a Wireshark trace on my Windows 7 machine with a LAN IP 192.168.3.100. I saw a lot of ARP requests like &#x27;Who has 192.168.1.165? Tell 192.168.3.9&#x27;, etc. with different IPs which are not my machine&#x27;s IP. What is going on? Good/Bad.? Do you propose any changes to my network?'''
date = "2015-02-17T07:57:00Z"
lastmod = "2015-02-18T02:36:00Z"
weight = 39914
keywords = [ "wireshark" ]
aliases = [ "/questions/39914" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark trace on my Windows 7 machine with a LAN IP 192.168.3.100. I saw a lot of ARP requests](/questions/39914/wireshark-trace-on-my-windows-7-machine-with-a-lan-ip-1921683100-i-saw-a-lot-of-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39914-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran a Wireshark trace on my Windows 7 machine with a LAN IP 192.168.3.100. I saw a lot of ARP requests like 'Who has 192.168.1.165? Tell 192.168.3.9', etc. with different IPs which are not my machine's IP. What is going on? Good/Bad.? Do you propose any changes to my network?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '15, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/43854fc2a2a894f0e78664c3a256f295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vinee&#39;s gravatar image" /><p>Vinee<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vinee has no accepted answers">0%</span></p></div></div><div id="comments-container-39914" class="comments-container"></div><div id="comment-tools-39914" class="comment-tools"></div><div class="clear"></div><div id="comment-39914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39923"></span>

<div id="answer-container-39923" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39923-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ARP comes up in many variations, most good, some bad. It's primary use is to find the MAC address of the host handling the IP address. This could be to see where to address the Ethernet frame on the network, or to check if any host is indeed using this IP address. This last one can be used by a DHCP server to check for address collisions, or to check the alive status of a host on the network, to see if an IP address has become available again.</p><p>It may be that a computer (eg. laptop in suspend) wakes up connected to your network and tries to reestablish contact with a host from the previously connected network. If it falls in the same (private) IP network range, it tries to ARP for it's MAC address (which has been forgotten).</p><p>It could be used for a network scan to see which (IP-)hosts are present on the network. This could be used for detection purposes, or a scan by a malicious program. There's no way to tell from the ARP traffic itself.</p><p>All in all a (relative) lot of ARP traffic is somewhat common and by itself nothing to be alarmed about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '15, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39923" class="comments-container"><span id="39926"></span><div id="comment-39926" class="comment"><div id="post-39926-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap for the response</p></div><div id="comment-39926-info" class="comment-info"><span class="comment-age">(18 Feb '15, 03:02)</span> Vinee</div></div></div><div id="comment-tools-39923" class="comment-tools"></div><div class="clear"></div><div id="comment-39923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

