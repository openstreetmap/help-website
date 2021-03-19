+++
type = "question"
title = "Why I am unable to view phone traffic on my wifi except for multicast packets."
description = '''I am new to wireshare. I set it up yesterday on my mac and enabled promiscuous mode. I connected both my mac and android phone to my home wifi. I am able to see all packets for the mac. However, I am not seeing all packets for my android phone but rather just a few packets, which after research seem...'''
date = "2015-11-27T07:52:00Z"
lastmod = "2015-11-27T08:00:00Z"
weight = 48024
keywords = [ "mobile", "android", "monitor-mode" ]
aliases = [ "/questions/48024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why I am unable to view phone traffic on my wifi except for multicast packets.](/questions/48024/why-i-am-unable-to-view-phone-traffic-on-my-wifi-except-for-multicast-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshare. I set it up yesterday on my mac and enabled promiscuous mode. I connected both my mac and android phone to my home wifi. I am able to see all packets for the mac. However, I am not seeing all packets for my android phone but rather just a few packets, which after research seems to be a multicast packets. See screenshot below:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-11-27_at_12.41.22_AM_zCkcBuN.png" alt="alt text" /></p><p>So where are all the tcp/http connection? I tried to enable monitor mode but got an error that it is not supported by the device and wireshark failed to capture any packets.</p><p>Am I missing something or this is how it is supposed to work?</p></div><div id="question-tags" class="tags-container tags">mobile android monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '15, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/3eea165e5121368690c56a08a226a403?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arsene&#39;s gravatar image" /><p>Arsene<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arsene has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '15, 07:53</p></div></div><div id="comments-container-48024" class="comments-container"></div><div id="comment-tools-48024" class="comment-tools"></div><div class="clear"></div><div id="comment-48024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48025"></span>

<div id="answer-container-48025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48025-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to <a href="https://ask.wireshark.org/questions/47830/dhcp-troubleshooting-missing-offer-and-ack">this question</a> first, and then eventually come back with additional question. Without monitor mode working, you cannot capture traffic in which your capturing machine is not involved.</p><p>If you are able to make your capturing machine a WiFi access point and connect the Android phone to internet through that access point, or if you can run tcpdump on the existing access point, it would be a different situation and you could see the phone's traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '15, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '15, 08:07</p></div></div><div id="comments-container-48025" class="comments-container"></div><div id="comment-tools-48025" class="comment-tools"></div><div class="clear"></div><div id="comment-48025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

