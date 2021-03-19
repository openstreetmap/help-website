+++
type = "question"
title = "How can I capture Bluetooth traffic with Bluetooth format?"
description = '''Currently I can capture the Bluetooth traffic using Wireshark. The way I did is following: Node A creates a PAN and paired with Node B. Then There will be an interface named pan0 in A and B. I choose pan0 as the captured interface in Wireshark, all the udp/tcp traffic can be captured. However, the t...'''
date = "2013-01-15T15:34:00Z"
lastmod = "2014-03-20T10:27:00Z"
weight = 17710
keywords = [ "wireshark", "bluetooth" ]
aliases = [ "/questions/17710" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture Bluetooth traffic with Bluetooth format?](/questions/17710/how-can-i-capture-bluetooth-traffic-with-bluetooth-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently I can capture the Bluetooth traffic using Wireshark. The way I did is following: Node A creates a PAN and paired with Node B. Then There will be an interface named pan0 in A and B. I choose pan0 as the captured interface in Wireshark, all the udp/tcp traffic can be captured.</p><p>However, the traffic is encapsulated in Ethernet format, which losses a lot of information from the Bluetooth mac layer. I am asking Can I capture the bluetooth traffic with bluetooth header format？</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark bluetooth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '13, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/5d4b0e49653f79a63f4024c3f377f6bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geneopenflow&#39;s gravatar image" /><p>geneopenflow<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geneopenflow has no accepted answers">0%</span></p></div></div><div id="comments-container-17710" class="comments-container"></div><div id="comment-tools-17710" class="comment-tools"></div><div class="clear"></div><div id="comment-17710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31001"></span>

<div id="answer-container-31001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31001-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check version of your Wireshark. From version 1.10 all popular Bluetooth protocols/profiles are supported. If you have 1.6 or 1.8 try install newer Wireshark (or build from source). For Ubuntu 12.04+:</p><p>$ sudo add-apt-repository ppa:whoopie79/ppa $ sudo apt-get update $ sudo apt-get install wireshark</p><p>Source: <a href="http://linuxg.net/how-to-install-wireshark-1-10-2-on-ubuntu-13-10-13-04-12-10-12-04-linux-mint-15-14-13-and-elementary-os-0-2-luna/">http://linuxg.net/how-to-install-wireshark-1-10-2-on-ubuntu-13-10-13-04-12-10-12-04-linux-mint-15-14-13-and-elementary-os-0-2-luna/</a></p><p>If you do not see "bluetoothN" interfaces, you also have too old "libpcap"... But you will able to sniffing via "usbmonN" interfaces (if you have "standard" USB Dongle). Probably Ubuntu 14.04 will have enough new libpcap/wireshark to have correct bluetooth support (<a href="https://launchpad.net/ubuntu/trusty/i386/libpcap-dev).">https://launchpad.net/ubuntu/trusty/i386/libpcap-dev).</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/45a69e9e5c0af55bfef57c8c6b637a95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michal%20Labedzki&#39;s gravatar image" /><p>Michal Labedzki<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michal Labedzki has no accepted answers">0%</span></p></div></div><div id="comments-container-31001" class="comments-container"></div><div id="comment-tools-31001" class="comment-tools"></div><div class="clear"></div><div id="comment-31001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20503"></span>

<div id="answer-container-20503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20503-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Whole Blueooth are now supported. There is also special Bluetooth interface named Bluetooth0 (1, 2, etc.) Also you can sniffing Bluetooth by USB (Bluetooth USB dongle).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/45a69e9e5c0af55bfef57c8c6b637a95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michal%20Labedzki&#39;s gravatar image" /><p>Michal Labedzki<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michal Labedzki has no accepted answers">0%</span></p></div></div><div id="comments-container-20503" class="comments-container"><span id="30882"></span><div id="comment-30882" class="comment"><div id="post-30882-score" class="comment-score"></div><div class="comment-text"><p>I am also trying capture bluetooth packets using wireshark , I connected my bluetooth dongle to ubuntu PC and started wireshark but i am not able to see bluetooth interface like bluetooth0 or bluetooth1</p><p>Can you help me out enable bluetooth interface in wireshark??????</p></div><div id="comment-30882-info" class="comment-info"><span class="comment-age">(17 Mar '14, 06:28)</span> sreeram1443</div></div></div><div id="comment-tools-20503" class="comment-tools"></div><div class="clear"></div><div id="comment-20503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

