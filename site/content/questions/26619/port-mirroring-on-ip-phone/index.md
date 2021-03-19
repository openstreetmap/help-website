+++
type = "question"
title = "Port Mirroring on IP Phone"
description = '''I have IP Phone set of Huawei made. One of the Ethernet port is connected to Modem for connectivity with service provider. It has another LAN port with label PC. If I want to capture the packets of SIP between my IP Phone and Modem can I mirror the Ethernet Port to PC port and capture the SIP Packet...'''
date = "2013-11-01T07:39:00Z"
lastmod = "2013-11-03T03:18:00Z"
weight = 26619
keywords = [ "port", "mirroring" ]
aliases = [ "/questions/26619" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Port Mirroring on IP Phone](/questions/26619/port-mirroring-on-ip-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26619-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have IP Phone set of Huawei made. One of the Ethernet port is connected to Modem for connectivity with service provider. It has another LAN port with label PC. If I want to capture the packets of SIP between my IP Phone and Modem can I mirror the Ethernet Port to PC port and capture the SIP Packets. My IP Phone is not able to register on network and I have to analyse its call setup trace. If anyone can help me how to mirror the physical ports of IP Phone, his / her help will be much appreciated.</p><p>Best Regards, Haider</p></div><div id="question-tags" class="tags-container tags">port mirroring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '13, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/cacf30f4734768167dcaf2bccd08bed8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haider&#39;s gravatar image" /><p>Haider<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haider has no accepted answers">0%</span></p></div></div><div id="comments-container-26619" class="comments-container"></div><div id="comment-tools-26619" class="comment-tools"></div><div class="clear"></div><div id="comment-26619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26633"></span>

<div id="answer-container-26633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26633-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to check the Huawei manual to see whether it is capable of doing a port mirror of the "Ethernet port" to the "PC port". I expect that this is not possible.</p><p>Other possibilities to capture data of the "Ethernet port" of your IP phone are:</p><ul><li>Capture on a span (mirror) port on the switch to which it connects.</li><li>Use a HUB between the IP phone and the switch to duplicate it's traffic</li><li>Use a TAB between the IP phone and the switch to duplicate it's traffic</li><li>Use an extra (small) switch with port mirroring capabilities to mirror the traffic. But be careful that you match the vlan configuration of the port so that you are not blocking some vlans that are needed by the IP phone.</li></ul><p>See also: <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-26633" class="comments-container"></div><div id="comment-tools-26633" class="comment-tools"></div><div class="clear"></div><div id="comment-26633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

