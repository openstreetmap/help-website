+++
type = "question"
title = "Promiscuous mode not working?"
description = '''I have WS 2.0.2 running on a laptop capturing packets in promiscuous mode on the wireless interface. I&#x27;m interested in seeing the traffic coming and going from say my mobile phone. It&#x27;s on 192.168.0.41, so in Wireshark I use a capture filter &quot;host 192.168.0.41&quot;, have the wireless interface selected ...'''
date = "2017-05-27T04:52:00Z"
lastmod = "2017-05-27T05:06:00Z"
weight = 61656
keywords = [ "promiscuous" ]
aliases = [ "/questions/61656" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscuous mode not working?](/questions/61656/promiscuous-mode-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61656-score" class="post-score" title="current number of votes">0</div><span id="post-61656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have WS 2.0.2 running on a laptop capturing packets in promiscuous mode on the wireless interface.</p><p>I'm interested in seeing the traffic coming and going from say my mobile phone. It's on 192.168.0.41, so in Wireshark I use a capture filter "host 192.168.0.41", have the wireless interface selected and go ...</p><p>Alas it seems to be capturing almost, but not exactly, no traffic.</p><p>I tried same with a capture filter of "ether host" followed by my phone'</p><p>That is, I can see a variety of broadcasts basically and transmissions that involve the laptop running Wireshark, but nothing that doesn't. I can play around on the phone, web browsing and creating traffic, but the traffic is not seen by the laptop. Yet both laptop and phone are side by side on the same WAP.</p><p>My conclusion is, I'm not in promiscuous mode. Wireshark is not seeing wifi transmissions that are not addressed to the laptop, they are filtered out before Wireshark. The whole point of promiscuous mode, I thought was to enable me to sniff traffic on the airwaves that did not involve my sniffing machine.</p><p>Something I want specifically to diagnose issues with wifi cameras I'm using and other issues from time to time. Is there some setting at the BIOS or OS level needed for wifi packets not addressed to the laptop to be visible and captured?</p><p>I'm running Linux Mint 18.1 on a Dell 5110 laptop for what it's worth. I have WS 2.0.2 running on a laptop capturing packets in promiscuous mode on the wireless interface.</p><p>I'm interested in seeing the traffic coming and going from say my mobile phone. It's on 192.168.0.41, so in Wireshark I use a capture filter "host 192.168.0.41", have the wireless interface selected and go ...</p><p>Alas it seems to be capturing almost, but not exactly, no traffic.</p><p>I tried same with a capture filter of "ether host" followed by my phone'</p><p>That is, I can see a variety of broadcasts basically and transmissions that involve the laptop running Wireshark, but nothing that doesn't. I can play around on the phone, web browsing and creating traffic, but the traffic is not seen by the laptop. Yet both laptop and phone are side by side on the same WAP.</p><p>My conclusion is, I'm not in promiscuous mode. Wireshark is not seeing wifi transmissions that are not addressed to the laptop, they are filtered out before Wireshark. The whole point of promiscuous mode, I thought was to enable me to sniff traffic on the airwaves that did not involve my sniffing machine.</p><p>Something I want specifically to diagnose issues with wifi cameras I'm using and other issues from time to time. Is there some setting at the BIOS or OS level needed for wifi packets not addressed to the laptop to be visible and captured?</p><p>I'm running Linux Mint 18.1 on a Dell 5110 laptop for what it's worth.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '17, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/622f30727ca1ec870212c71931bc23e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bernd-wechner&#39;s gravatar image" /><p><span>bernd-wechner</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bernd-wechner has no accepted answers">0%</span></p></div></div><div id="comments-container-61656" class="comments-container"></div><div id="comment-tools-61656" class="comment-tools"></div><div class="clear"></div><div id="comment-61656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61657"></span>

<div id="answer-container-61657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61657-score" class="post-score" title="current number of votes">0</div><span id="post-61657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Recommended links:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a> <a href="http://www.aircrack-ng.org/">http://www.aircrack-ng.org/</a></p><p>The first one is how to turn your interface into monitor mode so you can (possibly) see all wifi traffic in the RF environment around you. The second contains some tools that might help you put the interface in the correct mode to capture traffic. Just sniffing on a wifi interface that is in managed mode will not do what you want - sniff the traffic from your phone.</p><p>There are a lot more subtleties to wifi packet capture that you will need to get through; these links are a start. As well, filtering wifi traffic has a different set of filters. But first, make sure you get 802.11 traffic then you can worry about capture and display filter syntax.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '17, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-61657" class="comments-container"></div><div id="comment-tools-61657" class="comment-tools"></div><div class="clear"></div><div id="comment-61657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

