+++
type = "question"
title = "how do you capture network packets on android similar to ios?"
description = '''With an iPad/iPod/iPhone I know you can get the network packets while using the chargeing cable connected to a mac. Is there a way to do this with and android tablet or phone?'''
date = "2012-12-07T20:10:00Z"
lastmod = "2012-12-08T01:35:00Z"
weight = 16719
keywords = [ "android", "ios", "cable" ]
aliases = [ "/questions/16719" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do you capture network packets on android similar to ios?](/questions/16719/how-do-you-capture-network-packets-on-android-similar-to-ios)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16719-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With an iPad/iPod/iPhone I know you can get the network packets while using the chargeing cable connected to a mac. Is there a way to do this with and android tablet or phone?</p></div><div id="question-tags" class="tags-container tags">android ios cable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 20:10</strong></p><img src="https://secure.gravatar.com/avatar/472d8d467e4034170d17ff88d733c2d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guardian&#39;s gravatar image" /><p>guardian<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guardian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '12, 20:11</p></div></div><div id="comments-container-16719" class="comments-container"></div><div id="comment-tools-16719" class="comment-tools"></div><div class="clear"></div><div id="comment-16719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16722"></span>

<div id="answer-container-16722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16722-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture the traffic <strong>on</strong> the android device (to see 3G traffic), that's only possible if you root the device. Then you can install tcpdump (or other similar software. search google for "android tcpdump").</p><p>If you want to capture the wifi/wlan traffic, you don't need a sniffer on the android device. You can capture the traffic with a system that is able to listen to the wifi/wlan traffic. Please check the WLAN wiki.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/WLAN</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '12, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Dec '12, 01:36</p></div></div><div id="comments-container-16722" class="comments-container"><span id="16725"></span><div id="comment-16725" class="comment"><div id="post-16725-score" class="comment-score"></div><div class="comment-text"><p>I have used tPacketCapture (<a href="https://play.google.com/store/apps/details?id=jp.co.taosoftware.android.packetcapture&amp;hl=en)">https://play.google.com/store/apps/details?id=jp.co.taosoftware.android.packetcapture&amp;hl=en)</a> a little bit. It doesn't need root but does create a vpn service and intercepts frames there.</p></div><div id="comment-16725-info" class="comment-info"><span class="comment-age">(08 Dec '12, 11:47)</span> MartinM</div></div></div><div id="comment-tools-16722" class="comment-tools"></div><div class="clear"></div><div id="comment-16722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

