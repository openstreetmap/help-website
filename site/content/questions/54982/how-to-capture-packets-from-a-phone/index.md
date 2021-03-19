+++
type = "question"
title = "how to capture packets from a phone"
description = '''I was having problems capturing wireless packets which run through my phone on my laptop. Am I supposed to use USBcap to capture the packets which run through my phone on my laptop? or can I do it wirelessly if they are both on the same wifi network? Thanks'''
date = "2016-08-19T08:38:00Z"
lastmod = "2016-08-20T11:01:00Z"
weight = 54982
keywords = [ "usbcap", "device", "usb", "wireshark" ]
aliases = [ "/questions/54982" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture packets from a phone](/questions/54982/how-to-capture-packets-from-a-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54982-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was having problems capturing wireless packets which run through my phone on my laptop. Am I supposed to use USBcap to capture the packets which run through my phone on my laptop? or can I do it wirelessly if they are both on the same wifi network? Thanks</p></div><div id="question-tags" class="tags-container tags">usbcap device usb wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/ae9e2c546c843144c149a9c215c9b236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoMa&#39;s gravatar image" /><p>RoMa<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoMa has no accepted answers">0%</span></p></div></div><div id="comments-container-54982" class="comments-container"><span id="54986"></span><div id="comment-54986" class="comment"><div id="post-54986-score" class="comment-score"></div><div class="comment-text"><p>If this isnt even possible please let me know because im new to wireshark so I dont really know its true potential</p></div><div id="comment-54986-info" class="comment-info"><span class="comment-age">(19 Aug '16, 08:59)</span> RoMa</div></div></div><div id="comment-tools-54982" class="comment-tools"></div><div class="clear"></div><div id="comment-54982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54998"></span>

<div id="answer-container-54998" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54998-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way would be to capture the traffic at the Ethernet side of your AP. To do this you will need a TAP, mirroring switch, or L1 hub.</p><p>If your AP is equipped, you may be able to capture pcap on the AP itself and download to your PC through the administrator console of your AP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '16, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-54998" class="comments-container"></div><div id="comment-tools-54998" class="comment-tools"></div><div class="clear"></div><div id="comment-54998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55002"></span>

<div id="answer-container-55002" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55002-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use of USBPcap doesn't make much sense here. If you only want to capture the traffic of your laptop which is connected to the internet via WiFi tethering on a mobile phone, it is enough to capture in promiscuous mode on the WiFi interface of your laptop. But capturing on the phone itself would need another capturing application, there is currently no Wireshark for Android phones nor for iPhone.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '16, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55002" class="comments-container"></div><div id="comment-tools-55002" class="comment-tools"></div><div class="clear"></div><div id="comment-55002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

