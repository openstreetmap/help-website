+++
type = "question"
title = "How to sniff UDP packets from tablet to wi-fi LED controller"
description = '''Hello, I have a wi-fi LED bulb controller that receives UDP packets from my tablet via wi-fi and then translates into RF signals. I want to sniff the UDP packets sent from tablet to the controller via wi-fi (sniffing from the computer in the same network) I am totally new to wireshark and somehow ca...'''
date = "2013-07-10T05:49:00Z"
lastmod = "2013-07-10T07:11:00Z"
weight = 22798
keywords = [ "udp", "packets", "wireshark" ]
aliases = [ "/questions/22798" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to sniff UDP packets from tablet to wi-fi LED controller](/questions/22798/how-to-sniff-udp-packets-from-tablet-to-wi-fi-led-controller)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22798-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a wi-fi LED bulb controller that receives UDP packets from my tablet via wi-fi and then translates into RF signals.</p><p>I want to sniff the UDP packets sent from tablet to the controller via wi-fi (sniffing from the computer in the same network)</p><p>I am totally new to wireshark and somehow cannot get the settings right..</p><p>So for example tablet IP 192.168.0.102 is sending packets to controlelr IP 192.168.0.88 and I am sniffing from my computer (192.168.0.100).</p><p>When I select wi-fi as protocol, no extra settings, run the capture and try to do some traffic to the controller from tablet, I can see no packets with source 192.168.0.102</p><p>Any help would be appreciated</p><p>Best</p></div><div id="question-tags" class="tags-container tags">udp packets wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/3fc6ebc3586d79e3576eeef71978ba10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chichi&#39;s gravatar image" /><p>chichi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chichi has no accepted answers">0%</span></p></div></div><div id="comments-container-22798" class="comments-container"></div><div id="comment-tools-22798" class="comment-tools"></div><div class="clear"></div><div id="comment-22798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22809"></span>

<div id="answer-container-22809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22809-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture Wifi traffic you need either a Linux system or a special hardware adapter on Windows systems (<a href="http://www.riverbed.com/products-solutions/products/performance-management/wireshark-enhancement-products/Wireless-Traffic-Packet-Capture.html">AirPcap adapter</a>).</p><p>See the Wiki for a description how to capture Wifi traffic on Linux:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '13, 07:12</p></div></div><div id="comments-container-22809" class="comments-container"><span id="22822"></span><div id="comment-22822" class="comment"><div id="post-22822-score" class="comment-score"></div><div class="comment-text"><p>Hi, any possibility to do it on a mac? Thanks!</p></div><div id="comment-22822-info" class="comment-info"><span class="comment-age">(10 Jul '13, 09:54)</span> chichi</div></div><span id="22825"></span><div id="comment-22825" class="comment"><div id="post-22825-score" class="comment-score"></div><div class="comment-text"><p>It's described in the link I posted.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X">http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X</a></p></blockquote></div><div id="comment-22825-info" class="comment-info"><span class="comment-age">(10 Jul '13, 12:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22809" class="comment-tools"></div><div class="clear"></div><div id="comment-22809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

