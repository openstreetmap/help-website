+++
type = "question"
title = "Monitor mode on LAN?"
description = '''Hi, I want to use wireshark to sniff all the packages that are sent and received in my local network. The machine running wireshark is wired and all the other devices on the network use Wifi. Every article that I read says you need to place your network adapter in monitor mode to capture traffic not...'''
date = "2014-07-09T08:05:00Z"
lastmod = "2014-07-09T08:14:00Z"
weight = 34507
keywords = [ "lan", "monitor-mode" ]
aliases = [ "/questions/34507" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor mode on LAN?](/questions/34507/monitor-mode-on-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to use wireshark to sniff all the packages that are sent and received in my local network. The machine running wireshark is wired and all the other devices on the network use Wifi. Every article that I read says you need to place your network adapter in monitor mode to capture traffic not meant for me, but monitor mode only applies to wireless network adapters. So how does it work when I want to capture wireless traffik to and from the router when I am connected with a cable?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lan monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/221cea8ddbe56b13502ec323aac67b0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajiv&#39;s gravatar image" /><p>Rajiv<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajiv has no accepted answers">0%</span></p></div></div><div id="comments-container-34507" class="comments-container"></div><div id="comment-tools-34507" class="comment-tools"></div><div class="clear"></div><div id="comment-34507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34510"></span>

<div id="answer-container-34510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34510-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does your setup look like this?</p><pre><code>wifi device ---- thin air ----- router ---- thin air ----- wifi device
                                  |
                                  |
                               Ethernet
                                  |
                                  |
                             PC with Wireshark</code></pre><p>If yes, then you <strong>cannot capture</strong> data of the wireless clients, as the packets will never be sent to the ethernet port of your Wireshark PC, unless they are talking to your IP address or if it is broadcast/multicast traffic. The reason is: There is an internal switch in your wireless router that works like a real switch. See the Wiki for an explanation</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>If you need to see wireless traffic, you really need to <strong>capture the wireless traffic</strong>, which is done by enabling monitor mode of the wifi adapter. Please read the Wiki</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>Please be aware, that monitor mode on Windows does not work with Wireshark/WinPcap alone, as you'll need special hardware (AirPcap - search this site for it). Alternatively you can run Linux on your Wireshark PC, where it's usually much easier to enable monitor mode (see the Wiki).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '14, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34510" class="comments-container"><span id="34522"></span><div id="comment-34522" class="comment"><div id="post-34522-score" class="comment-score"></div><div class="comment-text"><p>Or run another sniffer on Windows that supports monitor mode; if you want to read those captures in Wireshark, that might still be possible (Wireshark can read captures from Microsoft Network Monitor, for example).</p></div><div id="comment-34522-info" class="comment-info"><span class="comment-age">(09 Jul '14, 12:31)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34510" class="comment-tools"></div><div class="clear"></div><div id="comment-34510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

