+++
type = "question"
title = "RS485 to wifi adapter traffic capture"
description = '''I have a RS485 to wifi adapter made by rheem (AKA Econet). It is assigned a WiFi IP of 192.168.1.75 by my ATT router. This device sends and receives data from a internet server (?) The computer running wireshark is connected to a ethernet port on the same router. I entered &quot;host 192.168.1.75&quot; as a f...'''
date = "2016-05-12T18:33:00Z"
lastmod = "2016-05-14T09:35:00Z"
weight = 52486
keywords = [ "capture-filter" ]
aliases = [ "/questions/52486" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RS485 to wifi adapter traffic capture](/questions/52486/rs485-to-wifi-adapter-traffic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52486-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a RS485 to wifi adapter made by rheem (AKA Econet). It is assigned a WiFi IP of 192.168.1.75 by my ATT router. This device sends and receives data from a internet server (?) The computer running wireshark is connected to a ethernet port on the same router. I entered "host 192.168.1.75" as a filter and I see nothing but the occasional who has 192.168.1.75 issued by my router (?). I know the MAC address of this device if that's any help. I not sure what I expect to see but I do not think it send that much data. The baud rate is 38400. I determined by looking at the router NAT table it is sending data to 54.173.66.19 I changed the filter to 54.173.66.19 still nothing unless I open that IP in the computer browser then I see the trafic to the computer IP.</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/f3e9d55c042f8ab3897b5456006a8ea0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HVAC&#39;s gravatar image" /><p>HVAC<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HVAC has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '16, 19:19</p></div></div><div id="comments-container-52486" class="comments-container"></div><div id="comment-tools-52486" class="comment-tools"></div><div class="clear"></div><div id="comment-52486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52490"></span>

<div id="answer-container-52490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52490-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>RS485 adapters are a proprietary interface and thus not supported by PCAP so you cannot specify to capture on that interface.</p><p>The occasional "Who has 192.168.1.75" packet is the one you're capturing from either your local LAN or WiFi adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '16, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p>wbenton<br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-52490" class="comments-container"></div><div id="comment-tools-52490" class="comment-tools"></div><div class="clear"></div><div id="comment-52490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52564"></span>

<div id="answer-container-52564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52564-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is not relevant to your issue that the box uses RS485 on its wired end. Please look around this Q&amp;A site and the Wireshark wiki pages about capture setup <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">on Ethernet</a> and <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">on WLAN</a> to understand what are the constraints of capturing on these network types, what "monitoring mode" of WLAN capturing means and which hardware and operating systems support it, and how to handle decryption of WPA-encrypted wireless traffic.</p><p>Your issue is that you are capturing on wired Ethernet interface bridged (switched) with the WLAN on your AT&amp;T router, so you can only see unicast packets for your PC and multicast/broadcast packets (such as the ARP request "Who has 192.168.1.75? Tell 192.168.1.1" you've seen), but no unicast traffic which your PC doesn't send or is not an intended recipient of.</p><p>If the Wiki pages mentioned above don't show you the way, come back and describe the hardware equipment of your PC (how many wired ethernet interfaces it has, whether it has a WLAN interface, what operating system do you use) to get a more detailed suggestion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '16, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52564" class="comments-container"></div><div id="comment-tools-52564" class="comment-tools"></div><div class="clear"></div><div id="comment-52564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

