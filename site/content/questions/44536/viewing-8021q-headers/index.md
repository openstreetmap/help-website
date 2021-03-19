+++
type = "question"
title = "Viewing 802.1Q headers"
description = '''I&#x27;m running Linux Mint Qiana and have two options for ethernet interfaces:  Broadcom NetLink BCM57780 3Com 3c905B 100BaseTX  It doesn&#x27;t appear that the 802.1Q header is visible in the received frames, even for TCP packets for a video stream (at least for the default setup of wireshark that I&#x27;m using...'''
date = "2015-07-27T10:31:00Z"
lastmod = "2015-07-27T10:41:00Z"
weight = 44536
keywords = [ "priority", "802.1q" ]
aliases = [ "/questions/44536" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Viewing 802.1Q headers](/questions/44536/viewing-8021q-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44536-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Linux Mint Qiana and have two options for ethernet interfaces:</p><ul><li>Broadcom NetLink BCM57780</li><li>3Com 3c905B 100BaseTX</li></ul><p>It doesn't appear that the 802.1Q header is visible in the received frames, even for TCP packets for a video stream (at least for the default setup of wireshark that I'm using). I imagine that this either because the frames aren't being sent with a specific 802.1Q inserted or because this portion of the header is stripped before being sent to the final desitnation (or simply because my network card is performing that functionality).</p><p>There must be some way to create a setup in which the 802.1Q header can be viewed though, as the 802.11e[1] priority differentiation depends on the value of the priority code point of the header. I need to be able to act on this priority for testing purposes, so does anyone have any ideas how I might make such a setup?</p></div><div id="question-tags" class="tags-container tags">priority 802.1q</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/2ed42d2e823882a20a098da5e0dc25b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cancub&#39;s gravatar image" /><p>cancub<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cancub has no accepted answers">0%</span></p></div></div><div id="comments-container-44536" class="comments-container"></div><div id="comment-tools-44536" class="comment-tools"></div><div class="clear"></div><div id="comment-44536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44537"></span>

<div id="answer-container-44537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44537-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>VLAN tags are removed by the switch before delivering to the end device. To view VLAN tags, you will need to be able to view frames as they traverse the switch. Please the below wiki page:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>NOTES:</p><ol><li>Some Ethernet adapters require special configurations in order to capture VLAN tags.</li><li>If you are using port mirroring on a switch (SPAN), some switches require special configurations to copy VLAN information.</li></ol><p>If you try one of the configurations in the wiki and still have issues, I would recommend opening a new question with more specific information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44537" class="comments-container"><span id="44538"></span><div id="comment-44538" class="comment"><div id="post-44538-score" class="comment-score"></div><div class="comment-text"><p>Assuming this is always the case, how do 802.11 access points determine which traffic class an incoming packet belongs to?</p></div><div id="comment-44538-info" class="comment-info"><span class="comment-age">(27 Jul '15, 10:46)</span> cancub</div></div><span id="44539"></span><div id="comment-44539" class="comment"><div id="post-44539-score" class="comment-score"></div><div class="comment-text"><p>That is a switch configuration. And of course, different switches have different configurations. But the idea is to create the VLANs in the switch. Then on the port connected to the AP, you must configure the VLANs that will be used by the access point. On the access point, the VLANs must also be configured and usually assigned to separate networks.</p><p>It is important to note the VLANs must be created throughout your entire switch networks. So if you have inter-connecting switches, you will need to configure VLAN trunks to ensure the VLANs travel across the network.</p><p>It is important to note that the AP's are layer 2 devices and will remove the VLAN tags before sending the data to the end client (i.e., wireless client). So if you are looking for VLAN tags, you need to perform the capture at the wired Ethernet interface from the switch (i.e., the interface between the AP and the wired switch).</p></div><div id="comment-44539-info" class="comment-info"><span class="comment-age">(27 Jul '15, 11:25)</span> Amato_C</div></div><span id="44541"></span><div id="comment-44541" class="comment"><div id="post-44541-score" class="comment-score"></div><div class="comment-text"><p>Ah, I think I understand now. Thank you very much for your detailed response. So there's no way to configure switches to forward frames without removing VLAN tags?</p></div><div id="comment-44541-info" class="comment-info"><span class="comment-age">(27 Jul '15, 12:34)</span> cancub</div></div><span id="44542"></span><div id="comment-44542" class="comment"><div id="post-44542-score" class="comment-score"></div><div class="comment-text"><p>Depends what port you are talking about.</p><ol><li><p>Port(s) used to connect switches = these are VLAN trunks and the switch will not remove the VLAN tags.</p></li><li><p>Port going to an access point = VLAN tags will not be removed. This assumes the AP is configured with VLANs</p></li><li><p>Port connecting to an end client = switch will automatically remove the VLAN tag</p></li></ol><p>So assuming you have a VLAN trunk, you could perform a wired capture and see the VLAN tags. Or if you AP allows, you could perform a capture on the wired interface and see the VLAN tags.</p><p>But if your intention is to capture VLAN tags going to an end client (i.e., switch port connects directly to a PC host), then the answer is no.</p></div><div id="comment-44542-info" class="comment-info"><span class="comment-age">(27 Jul '15, 12:42)</span> Amato_C</div></div></div><div id="comment-tools-44537" class="comment-tools"></div><div class="clear"></div><div id="comment-44537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

