+++
type = "question"
title = "Laptop detects packages sent to wifi radio"
description = '''I detect a lot of packages on &#x27;wlan0&#x27; on my laptop. They all look like this: [...] Source Destination Protocol Length Info [...] Avm_XX:XX:XX Frontier_XX:XX:XX Ethernet 1530 Ethernet Unknown: Invalid length/type: 0x05ec (1516)  The source address belongs to the router, the destination address belong...'''
date = "2016-03-14T16:36:00Z"
lastmod = "2016-03-15T07:33:00Z"
weight = 50907
keywords = [ "unknown", "radio" ]
aliases = [ "/questions/50907" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Laptop detects packages sent to wifi radio](/questions/50907/laptop-detects-packages-sent-to-wifi-radio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50907-score" class="post-score" title="current number of votes">0</div><span id="post-50907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I detect a lot of packages on 'wlan0' on my laptop. They all look like this:</p><pre><code>[...] Source        Destination        Protocol  Length Info
[...] Avm_XX:XX:XX  Frontier_XX:XX:XX  Ethernet  1530   Ethernet Unknown: Invalid length/type: 0x05ec (1516)</code></pre><p>The source address belongs to the router, the destination address belongs to a wifi radio which is connected to the wlan. I guess there is nothing wrong with these packages, since the radio is playing a web radio station. But why do I detect them on the wlan0 device of my laptop? I have no intention in any communication between my laptop and the wifi radio.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-radio" rel="tag" title="see questions tagged &#39;radio&#39;">radio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '16, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/4dbc3c5aa5c6b58b0413d22f1fc13610?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="le0m&#39;s gravatar image" /><p><span>le0m</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="le0m has no accepted answers">0%</span></p></div></div><div id="comments-container-50907" class="comments-container"><span id="50908"></span><div id="comment-50908" class="comment"><div id="post-50908-score" class="comment-score"></div><div class="comment-text"><p>Is your laptop connected to the same WiFi network as the WiFi radio (i.e., the device playing a web radio station over the WiFi network)?</p><p>If yes, then the wlan0 device is configured in promiscuous mode and is capturing all the traffic that is on the same WiFi network.</p><p>Also, what operating system or you using?</p></div><div id="comment-50908-info" class="comment-info"><span class="comment-age">(14 Mar '16, 19:39)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="50914"></span><div id="comment-50914" class="comment"><div id="post-50914-score" class="comment-score"></div><div class="comment-text"><p>Yes, both are in the same wifi. I'm using Linux Mint 17.3.</p></div><div id="comment-50914-info" class="comment-info"><span class="comment-age">(15 Mar '16, 02:57)</span> <span class="comment-user userinfo">le0m</span></div></div></div><div id="comment-tools-50907" class="comment-tools"></div><div class="clear"></div><div id="comment-50907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50919"></span>

<div id="answer-container-50919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50919-score" class="post-score" title="current number of votes">1</div><span id="post-50919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are capturing the WiFi traffic in promiscuous mode. The WiFi interface will only capture packets of the currently joined 802.11 network (with a specific SSID and channel).</p><p>For a more detailed explanation, refer to the Wireshark wiki on capturing WiFi:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Promiscuous_mode">https://wiki.wireshark.org/CaptureSetup/WLAN#Promiscuous_mode</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-50919" class="comments-container"></div><div id="comment-tools-50919" class="comment-tools"></div><div class="clear"></div><div id="comment-50919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50928"></span>

<div id="answer-container-50928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50928-score" class="post-score" title="current number of votes">1</div><span id="post-50928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Promiscuous mode behaviour on wireless interfaces largely depends on the hardware and drivers. So let's start from the start and see how the radio frame passes through the layers of processing.</p><ul><li><p>the router always sends the wireless frames towards the WiFi radio so they always reach your laptop's wlan0 receiver input.</p></li><li><p>if the wlan0 hardware is tuned to the same radio channel, it cannot avoid "hearing" those frames.</p></li><li><p>unless it is also joined to the same AP like your WiFi radio receiver, it will drop them due to the difference in ESSID, and <em>promiscuous</em> mode can do nothing about it. (If you would eventually <strong>want</strong> to capture frames with other ESSID, the wlan0 would have to be in <em>monitoring</em> mode instead)</p></li><li><p>only if the frame passes the ESSID check, the "normal" or "promisucous" mode becomes important.</p></li><li><p>if promiscuous mode is active <em>and really works</em> on that wireless hardware &amp; driver (which is not always true), it would let all received frames which have passed the ESSID check to get further, even though their destination MAC address is neither wlan0's own one nor a multicast one nor a broadcast one.</p></li></ul><p>So in another words: it is unlikely that the wlan0 is in promiscuous mode when you do not capture. Try to capture with promiscuous mode off and see whether the packets are still there or not. How to capture without promiscuous mode depends on what software you use (GUI Wireshark or any of the three: dumpcap, tshark, or tcpdump). In GUI Wireshark 2.0.x, you have to untick the "promiscuous mode on all interfaces" checkbox <em>and</em> set promiscuous mode on wlan0 to <code>disabled</code>; for the command-line tools, <code>-P</code> is the parameter <strong>disabling</strong> the promiscuous mode for an individual interface (so you would use <code>-i wlan0 -P</code> in this exact order).</p><p>So the summary is that your laptop's hardware always receives the frames if you use the same wireless channel like the WiFi radio receiver. The difference is how far they get in the hardware and network stack. If you only see them in a capture taken in promiscuous mode, the only thing you could do to save your laptop from receiving them would be to use a different radio channel for the WiFi network for the laptop and the WiFi network for the radio receiver. But without promiscuous mode, they do not bother the network stack and waste the CPU and memory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50928" class="comments-container"></div><div id="comment-tools-50928" class="comment-tools"></div><div class="clear"></div><div id="comment-50928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

