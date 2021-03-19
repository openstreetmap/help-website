+++
type = "question"
title = "MTU size and Path MTU Discovery"
description = '''I am a bit confused by the MTU limit on different devices. My understanding the default for Ethernet II frames is a max MTU size of 1500. So in other words, MTU is based on the size of the entire frame! Math is not my strong point! So I understand a default frame size of 1500 would mean I could send...'''
date = "2012-04-06T08:17:00Z"
lastmod = "2012-04-06T10:03:00Z"
weight = 9982
keywords = [ "frames", "ethernet", "packets", "mtu" ]
aliases = [ "/questions/9982" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MTU size and Path MTU Discovery](/questions/9982/mtu-size-and-path-mtu-discovery)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9982-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a bit confused by the MTU limit on different devices. My understanding the default for Ethernet II frames is a max MTU size of 1500. So in other words, MTU is based on the size of the entire frame! Math is not my strong point! So I understand a default frame size of 1500 would mean I could send a 1458 payload size using Path MTU Discovery method(8 bytes for ICMP header + 20 IP Header + 14 for Ethernet II = total frame size 1500. I wasn't able to test this portion. My tests found I could not send a payload size equal to or greater than 1473 to a Cisco router. In this case 1473+42=1515. I also noticed if I only add the ICMP header and the IP header (leaving off the Ethernet II part) I come up with 1501. So is the Cisco routers MTU limit 1500 or 1514?</p><p>I also noticed on my Windows 7 system the default MTU is set to 1300. In doing a test ping from my Windows 7 system I noticed I can only send a payload of 1272, 1273 fails. In this case the 1300 limit is reached by adding the 8 bytes for ICMP header and 20 for IP header.</p><p>Perhaps my confusion is in the way Wireshark displays the packet details because I am looking at the Frame section and the total bytes on the wire. So is the 14 for Ethernet II taken into account when checking against the MTU size limit on a device?</p></div><div id="question-tags" class="tags-container tags">frames ethernet packets mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '12, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/39cd80ed85e55962a47b03253968662c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networkguy09&#39;s gravatar image" /><p>networkguy09<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networkguy09 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '12, 08:18</p></div></div><div id="comments-container-9982" class="comments-container"></div><div id="comment-tools-9982" class="comment-tools"></div><div class="clear"></div><div id="comment-9982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9992"></span>

<div id="answer-container-9992" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Maximum Transmission Unit for a physical layer of a network isn't the largest size of packet that can be sent out on that physical layer, it's the largest size of <em>payload</em> that can be sent; i.e., it's <em>not</em> based on the size of the entire frame. The largest Ethernet packet that can be transmitted on a standard Ethernet is 1518 bytes - 14 bytes of Ethernet header, 1500 bytes of payload, and 4 bytes of CRC.</p><p>So the MTU <em>is</em> 1500, but that doesn't count the Ethernet header (or the CRC).</p><p>This means that the largest IPv4 packet you can transmit has a payload of 1480 bytes, not 1458 bytes - 14 bytes of Ethernet header, 20 bytes of IPv4 header (with no options), 1480 bytes of IPv4 payload, and 4 bytes of CRC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9992" class="comments-container"><span id="9994"></span><div id="comment-9994" class="comment"><div id="post-9994-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation. I drew it out and it makes more sense now looking at it.</p></div><div id="comment-9994-info" class="comment-info"><span class="comment-age">(06 Apr '12, 11:30)</span> networkguy09</div></div><span id="9995"></span><div id="comment-9995" class="comment"><div id="post-9995-score" class="comment-score"></div><div class="comment-text"><p>I drew something basically like this.</p><p>[Ethernet II Header 14 bytes] [DATA] [CRC 4 bytes] (this data section is where the MTU is defined)</p><p>Now inside the above data section....</p><p>[IPv4 Header 20 bytes] [DATA]</p><p>Now inside the above data section....</p><p>[ICMP Header 8 bytes] [DATA]</p><p>Now inside the above data section....</p><p>What's left you can use here, in the case of 1500 MTU limit 1472 can go inside this data field.</p><p>Earlier on my original post I was confused about what section is the payload in this instance, because they are all considered payloads.</p></div><div id="comment-9995-info" class="comment-info"><span class="comment-age">(06 Apr '12, 11:30)</span> networkguy09</div></div></div><div id="comment-tools-9992" class="comment-tools"></div><div class="clear"></div><div id="comment-9992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

