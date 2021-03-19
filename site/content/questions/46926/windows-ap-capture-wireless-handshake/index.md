+++
type = "question"
title = "Windows AP - Capture Wireless Handshake"
description = '''Hi guys, I&#x27;m still trying to figure this out and perhaps you can help me out with this one. I tried searching for a couple of days but I gave up now. What I would like to achieve is to grab the Wireless SSID Key that a client tries to connect with to my access point. As I don&#x27;t actually have an AP f...'''
date = "2015-10-26T03:53:00Z"
lastmod = "2015-10-27T10:54:00Z"
weight = 46926
keywords = [ "wireless", "capture", "windows", "passphrase" ]
aliases = [ "/questions/46926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Windows AP - Capture Wireless Handshake](/questions/46926/windows-ap-capture-wireless-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46926-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I'm still trying to figure this out and perhaps you can help me out with this one. I tried searching for a couple of days but I gave up now.</p><p>What I would like to achieve is to grab the Wireless SSID Key that a client tries to connect with to my access point. As I don't actually have an AP for this exercise, I'm using Windows 8.1 to create a hostednetwork:</p><pre><code>netsh wlan set hostednetwork mode=allow ssid=”TestMe” key=”Password.01”</code></pre><p>Then I start it with:</p><pre><code>netsh wlan start hostednetwork</code></pre><p>Now it is available, I can see it from other wireless devices. When I do not select in the NIC option to share the connection with another NIC, Windows will automatically create a new NIC where the traffic is forwarded from/to the wireless network. When I start WireShark and then I try to connect with a wrong (or even with the good one) passphrase, I don't see the actual handshake. I see the DHCP Request from the device nothing earlier?</p><p>Thanks :)</p></div><div id="question-tags" class="tags-container tags">wireless capture windows passphrase</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/a2e4acd8d2d4df1ac9fa6b32c74d86a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simnether&#39;s gravatar image" /><p>simnether<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simnether has no accepted answers">0%</span></p></div></div><div id="comments-container-46926" class="comments-container"></div><div id="comment-tools-46926" class="comment-tools"></div><div class="clear"></div><div id="comment-46926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46995"></span>

<div id="answer-container-46995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a>. I think you will likely need an AirPcap adapter to see the frames you're interested in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-46995" class="comments-container"></div><div id="comment-tools-46995" class="comment-tools"></div><div class="clear"></div><div id="comment-46995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

