+++
type = "question"
title = "Will wireshark analyze the entire network traffic"
description = '''I am using a machine which is connected through LAN. If i will install Wireshark on my machine, will it capture the Network traffic of the entire network connected to the LAN? or it is only specific to the machine where it is installed. Thanks, Smruti'''
date = "2012-09-03T22:28:00Z"
lastmod = "2012-09-04T02:12:00Z"
weight = 14009
keywords = [ "capture" ]
aliases = [ "/questions/14009" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Will wireshark analyze the entire network traffic](/questions/14009/will-wireshark-analyze-the-entire-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a machine which is connected through LAN. If i will install Wireshark on my machine, will it capture the Network traffic of the entire network connected to the LAN? or it is only specific to the machine where it is installed.</p><p>Thanks, Smruti</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '12, 22:28</strong></p><img src="https://secure.gravatar.com/avatar/84931ba9e662f83d38cf9907bc56962b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smruti%20Ranjan%20Roul&#39;s gravatar image" /><p>Smruti Ranja...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smruti Ranjan Roul has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 04:09</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14009" class="comments-container"></div><div id="comment-tools-14009" class="comment-tools"></div><div class="clear"></div><div id="comment-14009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14016"></span>

<div id="answer-container-14016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14016-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might.</p><p>It depends on exactly what your LAN cable connects to on the other end and if your network card (and drivers) can be set into promiscuous mode. If it's a port on a switch then you'll only see your own traffic, and broadcast traffic from the LAN. If it's a hub then you should see all LAN traffic.</p><p>See the <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> page (and the other associated pages) on the wiki for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14016" class="comments-container"></div><div id="comment-tools-14016" class="comment-tools"></div><div class="clear"></div><div id="comment-14016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14018"></span>

<div id="answer-container-14018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14018-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In all likelihood, it will only see traffic your machine is participating in, or which is broadcast to all machines.</p><p>The reason for this is that for years, most LANs have been built based on <a href="http://en.wikipedia.org/wiki/Switched_ethernet">switched Ethernet technology</a>, as opposed to <a href="http://en.wikipedia.org/wiki/Network_hub">hub-based Ethernet</a> or <a href="http://en.wikipedia.org/wiki/Bus_(computing)">bus-based networking</a>. In those older technologies, every machine on the LAN saw all traffic, purely because they were all electrically connected to each other. With switched Ethernet, the switch makes decisions about which packets to send to which ports. This makes the network faster and slightly more secure.</p><p>(Switched Ethernet isn't a very good security measure, because it's easy to defeat with <a href="http://en.wikipedia.org/wiki/Arp_poisoning">ARP poisoning</a>.)</p><p>Now, maybe it is possible you are still on a hub-based Ethernet, or similar. That can only be the case with 100 Mbit/s and slower networks. Part of the <a href="http://en.wikipedia.org/wiki/Gigabit_ethernet">Gigabit Ethernet</a> spec is a requirement for switches. You won't find a GigE hub.</p><p>I should also note that wireless networking effectively behaves like LANs of old: every machine connected to a given Wi-Fi network can see all traffic, purely due to the nature of radio communication.</p><p>If you are on a wired LAN with <a href="http://en.wikipedia.org/wiki/Managed_switch#Typical_switch_management_features">managed</a> switches and you have administrative access to those switches, you will probably find a feature you can enable in them called <a href="http://en.wikipedia.org/wiki/Port_mirroring">port mirroring</a>. That feature exists specifically to restore the older pre-switched LAN behavior: it designates one port as special, directing copies of all traffic to it, even packets not aimed at MAC addresses connected to that port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/8b0e3f6ae64ff27a7a01a0f49f8ee469?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Warren%20Young&#39;s gravatar image" /><p>Warren Young<br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Warren Young has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 02:14</p></div></div><div id="comments-container-14018" class="comments-container"><span id="14020"></span><div id="comment-14020" class="comment"><div id="post-14020-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response. Then i can conclude that the tool will only capture the traffic specific to a single machine where it is installed. And it will also capture the interaction of the machine with other machine over the network though more number of machines are placed in the same LAN.</p><p>Please correct me if i am wrong.</p></div><div id="comment-14020-info" class="comment-info"><span class="comment-age">(04 Sep '12, 02:21)</span> Smruti Ranja...</div></div><span id="14023"></span><div id="comment-14023" class="comment"><div id="post-14023-score" class="comment-score"></div><div class="comment-text"><p>I covered this above. If you have switched Ethernet and they're dumb switches or they're managed by you don't have admin access, and you can't trick other machines into talking through you in <a href="http://en.wikipedia.org/wiki/Man-in-the-middle_attack">MitM</a> fashion with ARP poisoning....then yes. You should read those Wikipedia articles I linked to. It will clear up even more of this.</p></div><div id="comment-14023-info" class="comment-info"><span class="comment-age">(04 Sep '12, 02:26)</span> Warren Young</div></div><span id="14028"></span><div id="comment-14028" class="comment"><div id="post-14028-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info..</p></div><div id="comment-14028-info" class="comment-info"><span class="comment-age">(04 Sep '12, 03:50)</span> Smruti Ranja...</div></div><span id="14048"></span><div id="comment-14048" class="comment"><div id="post-14048-score" class="comment-score"></div><div class="comment-text"><p>yes.. thanks for the valuable time u have spent.</p></div><div id="comment-14048-info" class="comment-info"><span class="comment-age">(04 Sep '12, 19:42)</span> Smruti Ranja...</div></div></div><div id="comment-tools-14018" class="comment-tools"></div><div class="clear"></div><div id="comment-14018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

