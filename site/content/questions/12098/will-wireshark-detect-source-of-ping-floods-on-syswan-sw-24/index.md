+++
type = "question"
title = "Will wireshark detect source of ping floods on Syswan SW-24?"
description = '''howdee all... first time on. below is one of hundreds emails i&#x27;ve been getting over the last two weeks from my SW-24. the floods last 10-20 minutes, then seem to stop for a while...some days there are multiple floods, others only one. They occur at random times. ...DL&#x27;d WS, BUT...not sure how to set...'''
date = "2012-06-20T22:00:00Z"
lastmod = "2012-06-20T22:52:00Z"
weight = 12098
keywords = [ "sw24", "syswan", "sw-24", "ping-flood" ]
aliases = [ "/questions/12098" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Will wireshark detect source of ping floods on Syswan SW-24?](/questions/12098/will-wireshark-detect-source-of-ping-floods-on-syswan-sw-24)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12098-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>howdee all... first time on. below is one of hundreds emails i've been getting over the last two weeks from my SW-24. the floods last 10-20 minutes, then seem to stop for a while...some days there are multiple floods, others only one. They occur at random times.</p><p>...DL'd WS, BUT...not sure how to set up filters for the SW-24.<br />
</p><p>one of hundreds email to me WAN1 MAC Address: 00-1C-74-00-B0-8C, IP: 24.100.82.111 WAN2 MAC Address: 00-1C-74-00-B0-8D, IP: 192.168.254.1 System Uptime: 16d 12h 41m 41s Firmware Version: Ver 1.0 Rel 04 Build Date: Jun 18 2010 CPU utilization: 5 % Heap Usage: 42 % Queue Usage: 1 %</p><p>Causes: Device Ping Flood! More than 120 pings per minute to SW00B08C(IP=24.100.82.111).</p><p>the 00-1C-74-00-B0-8C, IP: 24.100.82.111, is my Time-Warner cable modem</p><p>is it possible to use WS to detect the source of the ping-floods thru the SW-24?</p><p>Thanks in advance for speedy advice,</p><p>Chas</p></div><div id="question-tags" class="tags-container tags">sw24 syswan sw-24 ping-flood</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '12, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/275db9476859128b22d2e34cee927533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hesynergy&#39;s gravatar image" /><p>hesynergy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hesynergy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12098" class="comments-container"></div><div id="comment-tools-12098" class="comment-tools"></div><div class="clear"></div><div id="comment-12098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12099"></span>

<div id="answer-container-12099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12099-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like your cable modem detects some pings on 24.100.82.111. Those pings come either from the external side or from your LAN.</p><p>If the pings come from the external side (ISP Network), there is no easy way to work with wireshark, as you cannot sniff on the TV cable without further hardware, except your cable modem provides such a functionality. Please check the manual.</p><p>If the pings come from the internal side (rather unlikely), you can sniff the traffic on the LAN, by looking at this link: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>If you manage to sniff traffic, you can use this display filter to show only icmp packets.</p><blockquote><p><code>icmp</code></p></blockquote><p>Sort the list of entries in the packet list by source ip, and you will see who sends most of the icmp packets (possibly pings).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '12, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12099" class="comments-container"><span id="12104"></span><div id="comment-12104" class="comment"><div id="post-12104-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt!</p><p>I am wondering if eliminating the SW-24, for diag. Purposes might simplify things.... Or is this strictly a wan problem....gonna 1. Filter icmp packets, then; 2. disconnect my DSL TO ISOLATE. 3. Disconnect my HP network printer</p><p>Sound reasonable?</p><p>Chas ...</p></div><div id="comment-12104-info" class="comment-info"><span class="comment-age">(21 Jun '12, 07:30)</span> hesynergy</div></div><span id="12105"></span><div id="comment-12105" class="comment"><div id="post-12105-score" class="comment-score"></div><div class="comment-text"><p>well, I don't believe it's an internal device that generates those pings (would be kind of useless), but you never know!</p><p>If you can't sniff on the LAN side, it's of course an option to eliminate the possible sources of the problem and see if the situation changes.</p></div><div id="comment-12105-info" class="comment-info"><span class="comment-age">(21 Jun '12, 07:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12099" class="comment-tools"></div><div class="clear"></div><div id="comment-12099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

