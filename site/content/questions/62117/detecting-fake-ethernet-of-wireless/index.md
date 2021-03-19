+++
type = "question"
title = "Detecting fake ethernet of wireless"
description = '''According to the wireshark wiki capturing on WLAN&#x27;s may capture only user data packets with &quot;fake&quot; Ethernet headers. In this case, you won&#x27;t see any 802.11 management or control packets at all, and the 802.11 packet headers are &quot;translated&quot; by the network driver to &quot;fake&quot; Ethernet packet headers. Ca...'''
date = "2017-06-19T01:52:00Z"
lastmod = "2017-06-20T16:56:00Z"
weight = 62117
keywords = [ "ethernet", "802.11" ]
aliases = [ "/questions/62117" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Detecting fake ethernet of wireless](/questions/62117/detecting-fake-ethernet-of-wireless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62117-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to the <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">wireshark wiki</a></p><p><code>capturing on WLAN's may capture only user data packets with "fake" Ethernet headers. In this case, you won't see any 802.11 management or control packets at all, and the 802.11 packet headers are "translated" by the network driver to "fake" Ethernet packet headers.</code></p><p>Can one detect that a packet has an 802.11 history? That is, that it was captured as 802.11 and then modified to contain a fake Ethernet instead? Or is the fake Ethernet is indistinguishable from a regular one?</p></div><div id="question-tags" class="tags-container tags">ethernet 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/e6497f67a248956d28c81a2f3c263de5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Kroizman&#39;s gravatar image" /><p>Guy Kroizman<br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Kroizman has no accepted answers">0%</span></p></div></div><div id="comments-container-62117" class="comments-container"></div><div id="comment-tools-62117" class="comment-tools"></div><div class="clear"></div><div id="comment-62117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62191"></span>

<div id="answer-container-62191" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62191-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I agree with <a href="https://ask.wireshark.org/users/19586/sindy"></a><a href="https://ask.wireshark.org/users/19586/sindy">@sindy</a></a> that it is really not possible to positively identify these cases where we have 802.11--&gt;EthII/802.3 conversion, but I wanted to share some things things that I have picked up over the years that may 'suggest' a wireless adapter collection. These are not deterministic - only some things I have found that tend to be different between wired and wireless world:</p><ol><li><p>Wireless typically has much more packet loss, so when looking at TCP flows, I typically see very little packet loss on wired side, but the same network I might see 10x (or more!) the amount of TCP retransmission or UDP loss. Packet loss happens for other reasons, but I have a feel for the level on my networks that I run, so I can guess based on the amount of loss. If your evaluation is unknown, this may not be the most useful technique.</p></li><li><p>Delay on my wireless networks can be noticeable when comparing wireless to wired networks. If you have a baseline of what to expect on wired, you may detect a difference as the wireless could be a lot higher - in the 100s of ms or more (I have seen many seconds on poorly designed/busy wireless networks). This is most noticeable with powersave wireless clients that may sleep for one or more DTIM periods. Do some analysis with ping responses or something to see if you can detect differences. Smokeping is a nice tool for this comparison. The variance in response time is always higher for me as well when comparing wireless to wired response time delays - the distributions are very different.</p></li><li><p>On Linux and MAC OS, I see the 4-way EAPOL keying process in the 'faked' capture (I should check to see if the data is decrypted...). For whatever reason, when capturing on the interface and not in monitor mode, these are passed up. I suspect the 802.1X process is done in user space so they have to be passed up (e.g. wpa_supplicant with Linux). Only helps if you see them in the trace, and I have never seen this with Windows, or if your WiFi network is unencrypted.</p></li><li><p>capinfos tool with pcapng seems to give interface name in the output. If you know the interface name you would be able to tell. Otherwise, if you don't know, and you see 'wlan0' maybe you can guess what that you are in this situation. On my MAC, it says 'en0'. I have a MacBook Air, so en0 is wifi. I think if you have a MacBook Pro, the wired interface is en0 and wifi is en1 (I don't have a pro, but feel free to donate one and I will let you know for sure!) so that isn't a huge help unless you know the system that took the capture. But on Windows and Linux it can often be a little more descriptive.</p></li></ol><p>My view is that if I see enough of these traits, I can guess how the capture was taken. Unfortunately I live in a world where deterministic answers are not always available and yet we have to solve the problem anyway. I am forced to guess sometimes to move forward in many situations, so techniques that allow us to reduce risk while still guessing are quite useful in the real word.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '17, 16:56</p></div></div><div id="comments-container-62191" class="comments-container"><span id="62193"></span><div id="comment-62193" class="comment"><div id="post-62193-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have a MacBook Air, so en0 is wifi. I think if you have a MacBook Pro, the wired interface is en0 and wifi is en1</p></blockquote><p>If you have a MacBook Pro <em>with a built-in Ethernet</em>, that's the case. MacBook Pros haven't come with a built-in Ethernet for many years, however; mine doesn't have one, and the Wi-Fi is en0.</p></div><div id="comment-62193-info" class="comment-info"><span class="comment-age">(20 Jun '17, 18:43)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62191" class="comment-tools"></div><div class="clear"></div><div id="comment-62191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62138"></span>

<div id="answer-container-62138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62138-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Mostly the second. The fake ethernet headers are there to completely replace the 802.11 headers, so you can only use the MAC address (which is inherited from the 802.11 header to the Ethernet one) to identify the interface of the device which has sent the packet. If it is an address of a WLAN interface, the packet came directly through WLAN; if it is an address of a wired interface, it hasn't. But if you e.g. have a wired bridge between two WLANs, you have to look at the position of that device too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jun '17, 13:32</p></div></div><div id="comments-container-62138" class="comments-container"></div><div id="comment-tools-62138" class="comment-tools"></div><div class="clear"></div><div id="comment-62138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

