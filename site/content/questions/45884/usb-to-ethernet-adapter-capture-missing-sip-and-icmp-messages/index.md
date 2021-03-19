+++
type = "question"
title = "USB to ethernet adapter - capture missing SIP and ICMP messages"
description = '''I am attempting to monitor sip packets between the sip server/VoIP phone system and a sip to analog gateway. When I connect using a USB to Ethernet adapter I do not see sip or icmp messages. When I use an Ethernet port on the same pc and make no changes to Wireshark except to change the interface I ...'''
date = "2015-09-16T09:26:00Z"
lastmod = "2015-09-20T13:15:00Z"
weight = 45884
keywords = [ "adapter", "sip", "usb" ]
aliases = [ "/questions/45884" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [USB to ethernet adapter - capture missing SIP and ICMP messages](/questions/45884/usb-to-ethernet-adapter-capture-missing-sip-and-icmp-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45884-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to monitor sip packets between the sip server/VoIP phone system and a sip to analog gateway. When I connect using a USB to Ethernet adapter I do not see sip or icmp messages. When I use an Ethernet port on the same pc and make no changes to Wireshark except to change the interface I see sip and icmp messages.<br />
We are about to roll out new pcs and would like to know if Wireshark will work with USB to Ethernet adapters.<br />
</p></div><div id="question-tags" class="tags-container tags">adapter sip usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/58aa0702eccc45144ec197a9d607e82c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cathym&#39;s gravatar image" /><p>cathym<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cathym has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-45884" class="comments-container"><span id="45980"></span><div id="comment-45980" class="comment"><div id="post-45980-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am attempting to monitor sip packets between the sip server/VoIP phone system and a sip to analog gateway.</p></blockquote><p>Are you running Wireshark on the server, the gateway, or a third machine? If you're running Wireshark on the server or gateway, are you communicating with the other machine using the built-in Ethernet port or the USB Ethernet adapter?</p></div><div id="comment-45980-info" class="comment-info"><span class="comment-age">(20 Sep '15, 17:29)</span> Guy Harris ♦♦</div></div><span id="45998"></span><div id="comment-45998" class="comment"><div id="post-45998-score" class="comment-score"></div><div class="comment-text"><p>3rd machine. Using port mirroring, mirroring the sip server to the port the pc is connected to.</p></div><div id="comment-45998-info" class="comment-info"><span class="comment-age">(21 Sep '15, 04:27)</span> cathym</div></div><span id="46022"></span><div id="comment-46022" class="comment"><div id="post-46022-score" class="comment-score"></div><div class="comment-text"><p>And if you plug the mirrored port into the built-in Ethernet port, and capture in promiscuous mode, you see the SIP and ICMP packets, but if you plug it into the USB Ethernet adapter, and capture in promiscuous mode, you don't see those packets?</p></div><div id="comment-46022-info" class="comment-info"><span class="comment-age">(21 Sep '15, 09:18)</span> Guy Harris ♦♦</div></div><span id="46029"></span><div id="comment-46029" class="comment"><div id="post-46029-score" class="comment-score"></div><div class="comment-text"><p>Yes, set to capture to Use promiscuous mode on all interfaces.</p></div><div id="comment-46029-info" class="comment-info"><span class="comment-age">(21 Sep '15, 10:33)</span> cathym</div></div><span id="46031"></span><div id="comment-46031" class="comment"><div id="post-46031-score" class="comment-score"></div><div class="comment-text"><p>What type of adapter is the USB adapter? Check with the vendor of the adapter whether it supports promiscuous mode. It might not - it might just silently ignore requests to put it into promiscuous mode, in which case it wouldn't see any unicast traffic between the two hosts.</p></div><div id="comment-46031-info" class="comment-info"><span class="comment-age">(21 Sep '15, 11:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-45884" class="comment-tools"></div><div class="clear"></div><div id="comment-45884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45977"></span>

<div id="answer-container-45977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45977-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>would like to know if Wireshark will work with USB to Ethernet adapters.</p></blockquote><p>In general: yes. In detail: it depends ;-))</p><p>Please read my answer to a similar question, to figure out if the proposed solution might help you:</p><blockquote><p><a href="https://ask.wireshark.org/questions/12192/usb-to-ethernet-adapter-doesnt-show-under-interfaces">https://ask.wireshark.org/questions/12192/usb-to-ethernet-adapter-doesnt-show-under-interfaces</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '15, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45977" class="comments-container"><span id="46027"></span><div id="comment-46027" class="comment"><div id="post-46027-score" class="comment-score"></div><div class="comment-text"><p>@cathym: Do you see the USB adapter if you run the following command?</p><blockquote><p>dumpcap -D -M</p></blockquote><p>If <strong>NO</strong>: It's the problem I've mentioned above<br />
If <strong>YES</strong>: It's a different problem and more investigation is needed</p></div><div id="comment-46027-info" class="comment-info"><span class="comment-age">(21 Sep '15, 10:01)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-45977" class="comment-tools"></div><div class="clear"></div><div id="comment-45977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

