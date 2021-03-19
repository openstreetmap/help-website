+++
type = "question"
title = "Traffic aggregation"
description = '''Hello Forum Does Wireshark support to aggregate traffic (Tx and Rx) received from a fullduplex Tap (if the monitoring host (with Wireshark) does feature a dual-interface capture card? Thank you! Joseph'''
date = "2016-09-13T09:48:00Z"
lastmod = "2016-09-13T12:06:00Z"
weight = 55527
keywords = [ "rx479", "traffic", "aggregation", "tx" ]
aliases = [ "/questions/55527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic aggregation](/questions/55527/traffic-aggregation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Forum</p><p>Does Wireshark support to aggregate traffic (Tx and Rx) received from a fullduplex Tap (if the monitoring host (with Wireshark) does feature a dual-interface capture card?</p><p>Thank you!</p><p>Joseph</p></div><div id="question-tags" class="tags-container tags">rx479 traffic aggregation tx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p>joseph123<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-55527" class="comments-container"></div><div id="comment-tools-55527" class="comment-tools"></div><div class="clear"></div><div id="comment-55527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55530"></span>

<div id="answer-container-55530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55530-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, as in Wireshark is capable of capturing from multiple network interfaces at a time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55530" class="comments-container"><span id="55533"></span><div id="comment-55533" class="comment"><div id="post-55533-score" class="comment-score"></div><div class="comment-text"><p>It may be worth mentioning that you may have to reorder frames by timestamp if they get recorded out-of-order. This is what reordercap is for, as a command line utility coming with the Wireshark installer.</p></div><div id="comment-55533-info" class="comment-info"><span class="comment-age">(13 Sep '16, 13:34)</span> Jasper ♦♦</div></div><span id="55615"></span><div id="comment-55615" class="comment"><div id="post-55615-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the feedback! I have to admit that I did not yet bought this dual interface capture board. So i was not able to test it myself.</p><p>1. You mentioned an aggregation software reordercap. Does that mean the 2 interfaces of that dual interface capture board do appear as a single capture interface in Wireshark?</p><p>2. In addition you mentioned timestamping. Would you therefore recommend to buy a dual interface capture bord with timestamping feature?</p><p>Thank you!</p><p>Joe</p></div><div id="comment-55615-info" class="comment-info"><span class="comment-age">(17 Sep '16, 05:26)</span> joseph123</div></div><span id="55617"></span><div id="comment-55617" class="comment"><div id="post-55617-score" class="comment-score"></div><div class="comment-text"><ol><li><p>if a capture board is so advanced that it merges the data from the two interfaces itself (and thus probably uses advanced features of pcapng capture format to be able to indicate the direction in which a given frame has been captured), you're unlikely to need reordercap to fiddle with timestamps as such a card is likely to treat them right. But you can e.g. capture at two interfaces on your laptop simultaneously and use one of them per direction, and if one of them is the on-board Ethernet and the other one is an Ethernet over USB adaptor, you may need to compensate the difference in packet travel time from the wire to the kernel. That's where reordercap becomes handy. In this case, you'll have two interfaces, one for A-&gt;B direction at the source cable and another one for the B-&gt;A one.</p></li><li><p>whether or not you need a timestamping board depends on the timing precision you need, so on the actual task. They are expensive so compare your real needs to your real budget.</p></li></ol></div><div id="comment-55617-info" class="comment-info"><span class="comment-age">(17 Sep '16, 06:24)</span> sindy</div></div><span id="55620"></span><div id="comment-55620" class="comment"><div id="post-55620-score" class="comment-score"></div><div class="comment-text"><ol><li><p>Reordercap is not related to your capture interfaces, it's a capture file processor. It is specifically designed to sort the records in a capture file by time stamp, so that eg. merged or multiple interface captures appear in incremental(1) time order. This may occur when the time stamping of the records takes place at multiple locations (eg. interfaces).</p></li><li><p>Even though hardware time stamping is more accurate, it's a cost/benefit question. Is the expense of hardware capture and time stamping justified by the need for it. That is something you have to determine.</p></li></ol><p>Note 1: Even though the records are sorted by timestamp, it still depends on the synchronicity of the time stamp functions wether the packets arrived at the capture interfaces in that temporal order. Unless there's hardware synchronised time stamping, this may not be the case.</p></div><div id="comment-55620-info" class="comment-info"><span class="comment-age">(17 Sep '16, 07:43)</span> Jaap ♦</div></div></div><div id="comment-tools-55530" class="comment-tools"></div><div class="clear"></div><div id="comment-55530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

