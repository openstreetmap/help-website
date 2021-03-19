+++
type = "question"
title = "Optimal way to capture 802.11 traffic"
description = '''Hi, I have a small WLAN and I am interested in capturing and storing all wireless traffic for later statistical analysis. The analysis will be conducted on 802.11 layer 2 level. It is important to capture ALL wireless traffic going to and from the AP (control and management frames too).  Googling an...'''
date = "2013-01-06T22:42:00Z"
lastmod = "2013-01-07T15:09:00Z"
weight = 17483
keywords = [ "monitoring", "promiscuous", "packet-capture", "802.11", "capture" ]
aliases = [ "/questions/17483" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Optimal way to capture 802.11 traffic](/questions/17483/optimal-way-to-capture-80211-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17483-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a small WLAN and I am interested in capturing and storing all wireless traffic for later statistical analysis. The analysis will be conducted on 802.11 layer 2 level. It is important to capture ALL wireless traffic going to and from the AP (control and management frames too).</p><p>Googling and looking at previous questions here I have concluded that one way to go is having a dedicated machine with a wireless card in promiscuous mode somewhere near the AP acting as a monitor node. Having a LAN with 10 wireless clients all doing network intensive operations such as skype, gaming, video streaming makes me doubt on how reliable the results of this approach will be (that's only a speculation) i.e. there will be many lost packets or the monitor node will not be able to save all the traffic etc.<br />
</p><p>Are there any alternatives perhaps more reliable?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">monitoring promiscuous packet-capture 802.11 capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '13, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/4ad359972c0b3475c35dd93f1f8ff259?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BadAcidTrip&#39;s gravatar image" /><p>BadAcidTrip<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BadAcidTrip has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17483" class="comments-container"><span id="17512"></span><div id="comment-17512" class="comment"><div id="post-17512-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Are there any alternatives perhaps more reliable?</p></blockquote><p>for doing what? Capturing the whole wlan/wifi traffic, without missing packets?</p><p>Hm... what is your problem? Maybe there is another way to approach that problem.</p></div><div id="comment-17512-info" class="comment-info"><span class="comment-age">(07 Jan '13, 10:38)</span> Kurt Knochner ♦</div></div><span id="17534"></span><div id="comment-17534" class="comment"><div id="post-17534-score" class="comment-score"></div><div class="comment-text"><p>Well, ideally I would like to store what the AP "reads and writes" which is all the wifi frames the AP receives and sends. I was hoping that special APs exist for maybe forwarding all their traffic to a port or something like special "managed switches"... you get the idea...</p><p>I noticed that what the monitor node sniffs is a superset of what the AP sees (because of the traffic of other AP's in different channels etc.).</p><p>So my fear is that in a very populated neighborhood the traffic will be so much that nothing will be able keep up with so many disk writes (maybe wireshark will crash first).</p></div><div id="comment-17534-info" class="comment-info"><span class="comment-age">(07 Jan '13, 14:10)</span> BadAcidTrip</div></div></div><div id="comment-tools-17483" class="comment-tools"></div><div class="clear"></div><div id="comment-17483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17539"></span>

<div id="answer-container-17539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17539-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I was hoping that special APs exist for maybe forwarding all their traffic to a port or something like special "managed switches"... you get the idea...</p></blockquote><p>well, commercial solutions do provide that functionality, but mostly in a setup with a WLAN controller.</p><p>If you don't care about the AP, you could use <a href="https://openwrt.org/">OpenWrt</a> or <a href="http://dd-wrt.com/site/index">DD-WRT</a> with one of the cheap WLAN Routers/APs (Netgear, etc.). With *WRT you can ssh to the router/ap and capture traffic on the internal wlan interface.</p><blockquote><p>So my fear is that in a very populated neighborhood the traffic will be so much that nothing will be able keep up with so many disk writes (maybe wireshark will crash first).</p></blockquote><p>yes, that may happen, as the air is a shared medium for all APs, frequencies, channels, etc. So, there is no real <strong>reliable</strong> method of capturing traffic in a wlan environment. Placing the capturing machine at x,y,z in space may work well. Placing it at <strong>x + 3 inch,y,z</strong> may not work at all, due to some interference.</p><p>The best you can do:</p><ul><li>disable all sources of radiation other APs, microwave, radio, tv, special lamps, etc.) near the AP you are monitoring (and the capturing machine).</li><li>place the capturing machine near the AP</li><li>configure the AP to use a static channel, otherwise you will miss packets, if the AP decides to change the channel (your capturing NIC will not!)</li><li>writing the whole traffic to disk should be no problem with current disk technology, if you take into account the max. throughput of a wlan network.</li></ul><p>But again: what is your problem? Why do you want to reliably capture everything? Do you think there is packet loss in your wlan network?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jan '13, 15:11</p></div></div><div id="comments-container-17539" class="comments-container"></div><div id="comment-tools-17539" class="comment-tools"></div><div class="clear"></div><div id="comment-17539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

