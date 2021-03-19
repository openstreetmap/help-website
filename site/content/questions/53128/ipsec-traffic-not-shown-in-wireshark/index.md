+++
type = "question"
title = "IPSEC traffic not shown in Wireshark"
description = '''Hello, I have configured to mirror traffic from a cisco switch port which is connected to cisco ASA outside interface to monitor IPSEC traffic, but all I can see is an ordinary traffic and no IPSEC Is there any special configuration in Wireshark to enable IPSEC monitoring? Thank you'''
date = "2016-06-02T01:15:00Z"
lastmod = "2016-06-02T02:09:00Z"
weight = 53128
keywords = [ "asa", "cisco", "ipsec" ]
aliases = [ "/questions/53128" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IPSEC traffic not shown in Wireshark](/questions/53128/ipsec-traffic-not-shown-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have configured to mirror traffic from a cisco switch port which is connected to cisco ASA outside interface to monitor IPSEC traffic, but all I can see is an ordinary traffic and no IPSEC</p><p>Is there any special configuration in Wireshark to enable IPSEC monitoring?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">asa cisco ipsec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '16, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/b4b084155ffd1a07f47d5b5943da601f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fgasimzade&#39;s gravatar image" /><p>fgasimzade<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fgasimzade has no accepted answers">0%</span></p></div></div><div id="comments-container-53128" class="comments-container"></div><div id="comment-tools-53128" class="comment-tools"></div><div class="clear"></div><div id="comment-53128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53132"></span>

<div id="answer-container-53132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53132-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several possibilities to consider:</p><ul><li><p>you are monitoring a wrong interface of the ASA</p></li><li><p>the ipsec packets do not make it to the monitoring port due to some issue of the switch monitoring implementation</p></li><li><p>the network card, driver, and the capturing library at the capturing PC do not let the ipsec packets through (I guess you haven't forgotten to capture in promiscuous mode)</p></li><li><p>some (usually security) software at the capturing machine interferes with the capturing process</p></li><li><p>the packets do arrive but Wireshark does not dissect them as ipsec ones, perhaps because they use non-default configuration.</p></li></ul><p>Can you check the transport protocol (Cisco uses unusual things like IPSEC over UDP), the ports, and eventually VLAN used, and check whether any packets between the IP addresses in question (ASA's one and VPN client's one) exist in the capture, and if yes, whether they match the protocol and ports of the IPSEC settings in use?</p><p>Also, VLAN tags are usually stripped by the network card driver on Windows, so if you capture on Windows and look for a particular VLAN, you may never find it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53132" class="comments-container"><span id="53133"></span><div id="comment-53133" class="comment"><div id="post-53133-score" class="comment-score"></div><div class="comment-text"><p>Sorry, it was the promiscuous mode that was not enabled, I thought it is not necessary with port mirroring</p><p>Thank you</p></div><div id="comment-53133-info" class="comment-info"><span class="comment-age">(02 Jun '16, 03:20)</span> fgasimzade</div></div><span id="53134"></span><div id="comment-53134" class="comment"><div id="post-53134-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-53134-info" class="comment-info"><span class="comment-age">(02 Jun '16, 03:34)</span> grahamb ♦</div></div><span id="53135"></span><div id="comment-53135" class="comment"><div id="post-53135-score" class="comment-score"></div><div class="comment-text"><p>It is the other way round:</p><ul><li><p>promiscuous mode is solely a behaviour of the network card which you use to capture. You have to select this mode so that the card would let through to upper protocol stack layers also those incoming unicast frames whose destination MAC address does not match its own one.</p></li><li><p>monitoring on switch is necessary to make the switch copy all frames seen at chosen port(s)/in chosen VLAN(s) to the monitoring port to which a capturing card is connected regardless their destination MAC address. It is necessary as the very purpose of a switch is normally to send to each connected piece of equipment only those frames which are interesting for it.</p></li></ul><p>So if you had a hub, you wouldn't need to set monitoring mode in it, but you still would need promiscuous mode on the capturing card.</p></div><div id="comment-53135-info" class="comment-info"><span class="comment-age">(02 Jun '16, 03:40)</span> sindy</div></div></div><div id="comment-tools-53132" class="comment-tools"></div><div class="clear"></div><div id="comment-53132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53129"></span>

<div id="answer-container-53129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53129-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the IPSEC tunnel is terminated at the ASA outside interface, therefore you are looking at mirrored traffic inside the tunnel. There's nothing Wireshark can do about that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53129" class="comments-container"><span id="53131"></span><div id="comment-53131" class="comment"><div id="post-53131-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is terminated on ASA outside interface, but traffic physically is going through the mirrored switch port and I thought capturing traffic from that switch port will let me see IPSEC traffic. Am I wrong?</p></div><div id="comment-53131-info" class="comment-info"><span class="comment-age">(02 Jun '16, 01:36)</span> fgasimzade</div></div></div><div id="comment-tools-53129" class="comment-tools"></div><div class="clear"></div><div id="comment-53129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

