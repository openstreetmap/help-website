+++
type = "question"
title = "how to decode 802.11 frames to 802.3 frame"
description = '''Hi, As you may already know, when we capture wireless frames over a WiFi interface, you can choose Monitor mode so all the radio information can be shown. If you don&#x27;t choose Monitor mode, an pseudo Ethernet header will be used so that you can see all the higher level protocols, like tcp, icmp, etc....'''
date = "2017-03-27T02:33:00Z"
lastmod = "2017-03-27T02:33:00Z"
weight = 60338
keywords = [ "802.11" ]
aliases = [ "/questions/60338" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode 802.11 frames to 802.3 frame](/questions/60338/how-to-decode-80211-frames-to-8023-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60338-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>As you may already know, when we capture wireless frames over a WiFi interface, you can choose Monitor mode so all the radio information can be shown. If you don't choose Monitor mode, an pseudo Ethernet header will be used so that you can see all the higher level protocols, like tcp, icmp, etc.</p><p>My question is, how to convert the frames captured under monitor mode to its corresponding 'Ethernet' form?</p></div><div id="question-tags" class="tags-container tags">802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '17, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-60338" class="comments-container"><span id="60344"></span><div id="comment-60344" class="comment"><div id="post-60344-score" class="comment-score"></div><div class="comment-text"><p>You can still see the information from layer 3 and above if the frames are decrypted even with the radiotap (or other) and 802.11 headers present from monitor mode.</p><p>The presence/absence of higher level protocol decoding is not linked to pseudo header vs 802.11 header.</p></div><div id="comment-60344-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:38)</span> Bob Jones</div></div><span id="60436"></span><div id="comment-60436" class="comment"><div id="post-60436-score" class="comment-score"></div><div class="comment-text"><p>but I cannot see any higher level protocol, it was only shown as Data under IEEE 802.11 header. Do I need to decode that manually?</p></div><div id="comment-60436-info" class="comment-info"><span class="comment-age">(29 Mar '17, 20:51)</span> SteveZhou</div></div><span id="60438"></span><div id="comment-60438" class="comment"><div id="post-60438-score" class="comment-score"></div><div class="comment-text"><p>I can only imagine two cases without looking at any tangible evidence, such as an actual trace:</p><p>A. The 802.11 type 'data' frames are encrypted. Are the frames 'protected' - i.e. have the p-bit set in the 802.11 header for these data frames?</p><p>.1.. .... = Protected flag: Data is protected</p><p>B. The Wireshark installation is broken such as decoding no longer works</p><p>For case 1, decrypt first. If this still does not work, try changing the ignore protection bit options under protocols-&gt;IEEE 802.11. For case 2, I have never seen this happen, but try a different machine and/or reinstall.</p><p>I never need to decode manually typical network traffic, i.e. ARP, basic UDP and TCP data flows, etc, that comes from wireless monitor mode.</p></div><div id="comment-60438-info" class="comment-info"><span class="comment-age">(30 Mar '17, 03:35)</span> Bob Jones</div></div></div><div id="comment-tools-60338" class="comment-tools"></div><div class="clear"></div><div id="comment-60338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

