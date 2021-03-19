+++
type = "question"
title = "Capture 5GHz WiFi traffic for a 40MHz width channel."
description = '''Hello, Am trying to capture Wireless traffic in 5Ghz band in 40Mhz mode (HT40). I am using &quot;802.11a/b/g/n 3x3 Wireless LAN PCIe Mini Card&quot; for the capture and the operating system is Ubuntu 12.04. Following are the steps am following:  sudo iwconfig wlan2 mode monitor (To get into the monitor mode.)...'''
date = "2016-07-15T03:52:00Z"
lastmod = "2016-07-15T12:44:00Z"
weight = 54074
keywords = [ "sniffing", "capture", "miracast", "rtp", "monitor" ]
aliases = [ "/questions/54074" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture 5GHz WiFi traffic for a 40MHz width channel.](/questions/54074/capture-5ghz-wifi-traffic-for-a-40mhz-width-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54074-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Am trying to capture Wireless traffic in 5Ghz band in 40Mhz mode (HT40). I am using "802.11a/b/g/n 3x3 Wireless LAN PCIe Mini Card" for the capture and the operating system is Ubuntu 12.04.</p><p>Following are the steps am following:</p><ol><li>sudo iwconfig wlan2 mode monitor (To get into the monitor mode.)</li><li>sudo iw dev wlan2 set channel 40 (Setting the channel to 5200)</li><li>Running wireshark (2.0.3) on wlan2 to capture the traffic</li></ol><p>Issue I am facing.</p><p>An not able to capture the both primary and secondary channels here. First of all I have to run below command to start capturing the actual data.</p><p>iw dev wlan2 set channel 40 ht40+</p><p>but we are not able to capture the primary channel data here.</p><p>Question:</p><p>what is the right procedure to capture in 40MHz mode. How can we capture both primary and secondary data simultaneously.</p></div><div id="question-tags" class="tags-container tags">sniffing capture miracast rtp monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '16, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/6535f6fd84581179d7326b312736832c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shivamudugal&#39;s gravatar image" /><p>shivamudugal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shivamudugal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '16, 16:34</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-54074" class="comments-container"></div><div id="comment-tools-54074" class="comment-tools"></div><div class="clear"></div><div id="comment-54074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54078"></span>

<div id="answer-container-54078" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54078-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you ever tried the follwing command?</p><p><code>iw dev wlan2 set channel 40 ht40-</code></code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-54078" class="comments-container"><span id="54121"></span><div id="comment-54121" class="comment"><div id="post-54121-score" class="comment-score"></div><div class="comment-text"><p>As I have understood the HT40 mode means that 40Mhz width channel and its achieved by bundling adjacent 20MHz width channels. One of the 20Mhz is referred as the primary/main channel and the other is referred as the auxiliary/secondary. Each carrying specific data (may be primary is carrying the management frames and other data) and the secondary carrying the actual data.</p><p>Now my requirement is to capture both primary and secondary in a single capture. How to achieve this. As I have seen in "iw" tool, we can set one of ht40 or ht40+/ht40-. How to capture both (ht40 and ht40+) or (ht40 and ht40-). Considering ht40 is the primary and ht40+/- is the secondary.</p><p>Please correct my if an wrong in my understanding.</p></div><div id="comment-54121-info" class="comment-info"><span class="comment-age">(17 Jul '16, 22:29)</span> shivamudugal</div></div><span id="54122"></span><div id="comment-54122" class="comment"><div id="post-54122-score" class="comment-score"></div><div class="comment-text"><p>Did you try one of the techniques described in the answers? I think your understanding is correct, and the symbol for +/- on HT40 indicates where the secondary channel lies. A beacon frame will tell you as well: in the HT Information IE, there will be a field that will indicate where the secondary channel lies (above or below), in which case use the appropriate iw command with HT40+ or HT40-. This should give both channels.</p><p>Note that just because a wireless device supports 40MHz, it may not support monitor mode with 40MHz. Play around with it: maybe something like this - as we know 20MHz likely works (no trace provided to review, but assume you have one that is from both monitor/promiscuous mode):</p><ol><li>Find your beacons</li><li>Find the HT information IE and it will tell you whether the adjacent channel is high or low. The beacon will also tell you if it supports 40MHz bandwidth, LDPC, SGI, etc. All of this could be important if your capture device is to pick up these frames.</li><li>Config your capture device with the appropriate iw command</li><li>Validate that you are seeing traffic you expect, like QoS Data, etc, from the client. The radiotap header will tell you if it is 40MHz or 20MHz bandwidth.</li></ol><p>If it doesn't work, keep trying: change iw commands, move channels, get a different capture device, etc.</p></div><div id="comment-54122-info" class="comment-info"><span class="comment-age">(17 Jul '16, 22:54)</span> Bob Jones</div></div><span id="54123"></span><div id="comment-54123" class="comment"><div id="post-54123-score" class="comment-score"></div><div class="comment-text"><p>In addition to the comment made by @Bob Jones My understanding is the following by assuming that channel 40 is your primary: A 40 MHz channel can be achieved by the following channel bindings:</p><p><code> Channel 40 + Channel 44 = HT40+</code></p><p><code></code></p><p><code>Channel 40 + Channel 36 = HT40- </code></p><p>That is, my understanding, in easy words said what Ht40+ and HT40- do.</p></div><div id="comment-54123-info" class="comment-info"><span class="comment-age">(17 Jul '16, 23:42)</span> Christian_R</div></div><span id="54125"></span><div id="comment-54125" class="comment"><div id="post-54125-score" class="comment-score"></div><div class="comment-text"><p>@Bob Jones @Christian_R</p><p>Thanks for the information. I will do some tryouts with "iw" options...</p><p>Is there a way to find out if my capture device supports monitor mode with 40MHz. As i have said in my first post, am using qualcomm's "802.11a/b/g/n 3x3 Wireless LAN PCIe Mini Card". This one support 40Mhz channel width and also can capture either primary (ht40) or secondary (ht40+/-) at a time. But not together.</p></div><div id="comment-54125-info" class="comment-info"><span class="comment-age">(18 Jul '16, 03:03)</span> shivamudugal</div></div><span id="54150"></span><div id="comment-54150" class="comment"><div id="post-54150-score" class="comment-score"></div><div class="comment-text"><p>Am able to capture either of primary or secondary channels at a time a given time. But my requirement is to capture both of them in a single capture.</p><p>QoS data will be on secondary channel and management frames will be on the primary channel. Some times QoS data will also creep into primary channel. So I want to capture both primary and secondary channel in a single capture.</p><p>But till now by using "iw" options am able to capture only primary or secondary.</p></div><div id="comment-54150-info" class="comment-info"><span class="comment-age">(18 Jul '16, 22:57)</span> shivamudugal</div></div><span id="54151"></span><div id="comment-54151" class="comment not_top_scorer"><div id="post-54151-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a capture with a beacon inside?</p></div><div id="comment-54151-info" class="comment-info"><span class="comment-age">(18 Jul '16, 23:29)</span> Christian_R</div></div></div><div id="comment-tools-54078" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-54078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54082"></span>

<div id="answer-container-54082" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54082-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Only a slight modification to @Christian_R's comment, which is on point - from</p><p><a href="https://en.wikipedia.org/wiki/List_of_WLAN_channels">https://en.wikipedia.org/wiki/List_of_WLAN_channels</a></p><p>Channel 40 in UNII-1 band is 20MHz. I would try to move to channel 36 and use your HT+ command. It may seem equivalent to a channel 40 HT40- (i.e. channel 36 HT40+) but it may not be, depending on some specific conditions set in the driver. It may not solve your problem, just something to try.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-54082" class="comments-container"></div><div id="comment-tools-54082" class="comment-tools"></div><div class="clear"></div><div id="comment-54082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

