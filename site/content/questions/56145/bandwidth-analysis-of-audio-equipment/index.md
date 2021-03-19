+++
type = "question"
title = "bandwidth analysis of audio equipment"
description = '''I&#x27;ve been trying to analyze some equipment in an audio system. I&#x27;ve run wireshark on my mac while connected to a couple of different devices. Our consoles interface allows me to choose which ports are utilized for the traffic. When I start to capture packets from the network while connected to a wir...'''
date = "2016-10-04T13:04:00Z"
lastmod = "2016-10-04T13:04:00Z"
weight = 56145
keywords = [ "bandwidth" ]
aliases = [ "/questions/56145" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [bandwidth analysis of audio equipment](/questions/56145/bandwidth-analysis-of-audio-equipment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56145-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to analyze some equipment in an audio system. I've run wireshark on my mac while connected to a couple of different devices. Our consoles interface allows me to choose which ports are utilized for the traffic. When I start to capture packets from the network while connected to a wireless access point I'm unable to see any traffic between the console and or the ipad. I've tried running in monitor mode and without the monitor mode checked.<br />
</p><p>Should the computer I'm running wireshark on be connected between the access point (that the ipad connects to) and the console or can I simply connect the laptop running wireshark to the wifi network that the ipad is on? Or do I need to do more research about the way wireshark should be setup and run?</p><p>Any help would be greatly appreciated!</p><p>Loren</p></div><div id="question-tags" class="tags-container tags">bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '16, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/2be56f33c88a6b343477d2f047a6d301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lorenjz&#39;s gravatar image" /><p>lorenjz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lorenjz has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-56145" class="comments-container"><span id="56162"></span><div id="comment-56162" class="comment"><div id="post-56162-score" class="comment-score"></div><div class="comment-text"><p>Seems my yesterday's comment got lost in transmission.</p><p>If you have an alternative to capturing in the air, you should always prefer it. Or, from the other perspective, you should only capture in the air if you need to diagnose air interface issues or if you have no other point on the path between the device you are interested in and the rest of the world but the air interface.</p><p>So in your case, I would recommend to capture on the Ethernet interface between the access point to which the ipad is connected over the air and the other devices. If, however, the ipad talks to other devices which are also connected to the same AP over the air, bringing another AP into the setup, connecting it to the other one using wired Ethernet and connecting the ipad to one AP and the other devices to the other AP provides you much less burden to deal with than capturing in the air using monitoring mode.</p><p>If I haven't scared you enough and you decide to use the over-the-air capture anyway, monitoring mode is a must, and on a Mac, monitoring works the best of all platforms. So your issue may be encryption - if you use it, you have to capture the ipad's "login" to the WLAN.</p><p>There is a <a href="https://wiki.wireshark.org/CaptureSetup">wiki page on capturing setup in general</a> which further refers to wired and wireless setups in detail.</p></div><div id="comment-56162-info" class="comment-info"><span class="comment-age">(05 Oct '16, 07:33)</span> sindy</div></div></div><div id="comment-tools-56145" class="comment-tools"></div><div class="clear"></div><div id="comment-56145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

