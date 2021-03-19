+++
type = "question"
title = "wlan monitoring a ping: inside the network only 2 packets, outside 4"
description = '''I have the following network setup: PC1 monitor node (not connected to the ssid) PC3 access point  PC5 client1 PC6 client2  I monitor the traffic on PC1 using Wireshark and PC3 using tcpdump. When I ping from PC6 to PC5, I can see 4 packets on PC1: 2 Echo requests which travel from PC6 to AP and the...'''
date = "2013-07-11T04:42:00Z"
lastmod = "2013-07-11T04:54:00Z"
weight = 22846
keywords = [ "wlan" ]
aliases = [ "/questions/22846" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wlan monitoring a ping: inside the network only 2 packets, outside 4](/questions/22846/wlan-monitoring-a-ping-inside-the-network-only-2-packets-outside-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22846-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following network setup:</p><pre><code>PC1           monitor node (not connected to the ssid)
PC3           access point 
PC5           client1
PC6           client2</code></pre><p>I monitor the traffic on PC1 using Wireshark and PC3 using tcpdump.</p><p>When I ping from PC6 to PC5, I can see 4 packets on PC1: 2 Echo requests which travel from PC6 to AP and then to PC5 (mac addresses are adapted on the way) and 2 Echo replies which go the same wa y back.</p><p>However, when I am monitoring the traffic inside the network on PC3, I can only see two packets: 1 Echo request from PC6 to PC5 and one reply back. So, the MAC address changes seem to be hidden inside the network.</p><p>Why are there only 2 packets when monitoring inside the network and 4 when looking at it from an outside monitor?</p></div><div id="question-tags" class="tags-container tags">wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '13, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/9054680f27ded19c27fbee5dd8266ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Parsifal&#39;s gravatar image" /><p>Parsifal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Parsifal has no accepted answers">0%</span></p></div></div><div id="comments-container-22846" class="comments-container"></div><div id="comment-tools-22846" class="comment-tools"></div><div class="clear"></div><div id="comment-22846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22850"></span>

<div id="answer-container-22850" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22850-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, when I am monitoring the traffic inside the network on PC3</p></blockquote><p>If this is your AP, what OS is this and how did you setup the Soft-AP?</p><p>How did you capture the traffic?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22850" class="comments-container"><span id="22863"></span><div id="comment-22863" class="comment"><div id="post-22863-score" class="comment-score"></div><div class="comment-text"><p>We use grml as OS, a Debian derivative. The Soft-AP is setup using hostapd, without encryption. We captured the traffic on PC1 using monitor mode and Wireshark, on PC3 using tcpdump. Thanks!</p></div><div id="comment-22863-info" class="comment-info"><span class="comment-age">(11 Jul '13, 06:15)</span> Parsifal</div></div><span id="22865"></span><div id="comment-22865" class="comment"><div id="post-22865-score" class="comment-score"></div><div class="comment-text"><p>can you please post the whole tcpdump command you were using on PC3?</p></div><div id="comment-22865-info" class="comment-info"><span class="comment-age">(11 Jul '13, 06:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22850" class="comment-tools"></div><div class="clear"></div><div id="comment-22850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

