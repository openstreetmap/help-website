+++
type = "question"
title = "No UDP packet with wrong checksum"
description = '''On my Ubuntu 12.04, when I sent TCP packets, wireshark will show all the TCP checksums are wrong, this is understandable because of checksum offloading by the NIC (Intel WiFi NIC). However, when it sent thousands of UDP packets, I don&#x27;t see even one UDP packets with wrong checksum in Wireshark. What...'''
date = "2015-10-28T12:24:00Z"
lastmod = "2015-10-28T12:54:00Z"
weight = 47031
keywords = [ "wireshark" ]
aliases = [ "/questions/47031" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [No UDP packet with wrong checksum](/questions/47031/no-udp-packet-with-wrong-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my Ubuntu 12.04, when I sent TCP packets, wireshark will show all the TCP checksums are wrong, this is understandable because of checksum offloading by the NIC (Intel WiFi NIC). However, when it sent thousands of UDP packets, I don't see even one UDP packets with wrong checksum in Wireshark.</p><p>What could be going on here? I need some packets with wrong UDP checksum to test my application.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-47031" class="comments-container"></div><div id="comment-tools-47031" class="comment-tools"></div><div class="clear"></div><div id="comment-47031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47032"></span>

<div id="answer-container-47032" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47032-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe checksum offloading is not on for UDP. Check your network adapter properties. Checksum offloading can be enabled and disabled separately for IP, TCP, and UDP.</p><p>Or download and install <a href="http://www.colasoft.com/packet_builder/">Colasoft Packet Builder</a>. This is a free tool that will let you craft packets. It can automatically re-calculate the checksum when you change the packets so that the checksum is always correct, but this feature can be turned off.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-47032" class="comments-container"><span id="47033"></span><div id="comment-47033" class="comment"><div id="post-47033-score" class="comment-score"></div><div class="comment-text"><p>Thanks @jim-aragon.In the output for "ethtool -k", the setting for tcp and udp are same. Thanks for the link to Colasoft Packet Builder, I was able to use a binary editor to change the content of udp packet to make the checksum wrong (on purpose).</p></div><div id="comment-47033-info" class="comment-info"><span class="comment-age">(28 Oct '15, 13:03)</span> pktUser1001</div></div></div><div id="comment-tools-47032" class="comment-tools"></div><div class="clear"></div><div id="comment-47032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

