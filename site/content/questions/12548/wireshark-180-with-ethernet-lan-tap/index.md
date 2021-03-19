+++
type = "question"
title = "Wireshark 1.8.0 with ethernet lan tap"
description = '''I am using Wireshark 1.8.0 in ubuntu 12.04, and I made my own passive lan tap from enigma curry website I just checked to make sure the connections are good. all of the connections are intact and not loose. The way my setup is I use ethernet port on my laptop, and I use usb 2.0 ethernet adapter. It ...'''
date = "2012-07-09T23:11:00Z"
lastmod = "2012-07-10T02:19:00Z"
weight = 12548
keywords = [ "passive", "lan", "wireshark", "tap", "ubuntu" ]
aliases = [ "/questions/12548" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.8.0 with ethernet lan tap](/questions/12548/wireshark-180-with-ethernet-lan-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark 1.8.0 in ubuntu 12.04, and I made my own passive lan tap from <a href="http://www.enigmacurry.com/archive/2006/01/1/">enigma curry website</a> I just checked to make sure the connections are good. all of the connections are intact and not loose. The way my setup is I use ethernet port on my laptop, and I use usb 2.0 ethernet adapter. It seem to work on Windows with my lan tap but I am wanting to get it working in ubuntu.</p><p>Any help will be appreciated! :)</p></div><div id="question-tags" class="tags-container tags">passive lan wireshark tap ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/b4a1028edd057cf98a6b33dbee2bc5e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keyboardmonkey&#39;s gravatar image" /><p>keyboardmonkey<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keyboardmonkey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '12, 04:18</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-12548" class="comments-container"></div><div id="comment-tools-12548" class="comment-tools"></div><div class="clear"></div><div id="comment-12548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12550"></span>

<div id="answer-container-12550" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12550-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>Who is enigma and why does he/she love curry? Seriously, please post more information about that "passive lan tap" (link), the way you used it with Windows and what you tried to make it work with Ubuntu.</p></li><li><p>The best way to build your own linux "lan tap" (without soldering) is to configure a bridge, although that's not a passive "tap"! Check these:</p></li></ol><blockquote><p><code>http://www.m0rd0r.eu/?p=395</code><br />
<code>http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge</code><br />
<code>http://tcpreplay.synfin.net/wiki/tcpbridge</code><br />
</p></blockquote><p>If I misunderstood your request, please add more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '12, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '12, 02:33</p></div></div><div id="comments-container-12550" class="comments-container"><span id="12563"></span><div id="comment-12563" class="comment"><div id="post-12563-score" class="comment-score"></div><div class="comment-text"><p>Sorry, The reason why I am using wireshark 1.8 is what I thought to eliminate the need to bridge the two interfaces for packet sniffing.</p></div><div id="comment-12563-info" class="comment-info"><span class="comment-age">(10 Jul '12, 08:44)</span> keyboardmonkey</div></div><span id="12564"></span><div id="comment-12564" class="comment"><div id="post-12564-score" class="comment-score"></div><div class="comment-text"><p>O.K. so how did you do it on Windows?</p><p>BTW: As you are using a "real" Tap, you can just sniff on both network adapters at once. This is possible with Wireshark &gt;= 1.7. Just select multiple interfaces in the dialog "Capture -&gt; Interfaces".</p></div><div id="comment-12564-info" class="comment-info"><span class="comment-age">(10 Jul '12, 08:48)</span> Kurt Knochner ♦</div></div><span id="12571"></span><div id="comment-12571" class="comment"><div id="post-12571-score" class="comment-score"></div><div class="comment-text"><p>It seemed easier to bridge in windows than it is to bridge in ubuntu.</p></div><div id="comment-12571-info" class="comment-info"><span class="comment-age">(10 Jul '12, 12:23)</span> keyboardmonkey</div></div><span id="12588"></span><div id="comment-12588" class="comment"><div id="post-12588-score" class="comment-score"></div><div class="comment-text"><p>I thought you wanted to eliminate the need for a bridge? On Ubuntu, there is no easier way to create a bridge than the ones I posted the links for. Take a look at <strong>tcpbridge</strong>.</p><p>Anyway, with the TAP you built, there is no need to use a bridge, you can just to sniff on both of your adapters in parallel to capture traffic in both directions (given that the TAP works). See my <strong>BTW</strong> in a previous comment.</p></div><div id="comment-12588-info" class="comment-info"><span class="comment-age">(10 Jul '12, 23:52)</span> Kurt Knochner ♦</div></div><span id="12590"></span><div id="comment-12590" class="comment"><div id="post-12590-score" class="comment-score"></div><div class="comment-text"><p>Sorry, that is what I mean I started to use 1.8 on Ubuntu so I can sniff without bridging, I am able to choose Eth0 and Eth1 in wireshark. But, when I start to capture I get nothing I checked inside my lan tap and they all have good connection. I noticed the mac address to my ethernet interfaces won't show up underneath the interface name in wireshark.</p></div><div id="comment-12590-info" class="comment-info"><span class="comment-age">(11 Jul '12, 00:28)</span> keyboardmonkey</div></div><span id="12591"></span><div id="comment-12591" class="comment not_top_scorer"><div id="post-12591-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I checked inside my lan tap and they all have good connection.</p></blockquote><p>did you see traffic with the <strong>same</strong> setup on Windows (same TAP, same computer, same USB network adapter)?</p><blockquote><p>I noticed the mac address to my ethernet interfaces won't show up underneath the interface name in wireshark.</p></blockquote><p>Do you see any traffic if you connect your interfaces to a regular switch and start capturing data? If you can't see any traffic even in this scenario, try to generate some traffic on the sniffer box by pinging other systems on the network. Does that work?</p></div><div id="comment-12591-info" class="comment-info"><span class="comment-age">(11 Jul '12, 00:36)</span> Kurt Knochner ♦</div></div><span id="12643"></span><div id="comment-12643" class="comment not_top_scorer"><div id="post-12643-score" class="comment-score"></div><div class="comment-text"><p>Ok, I just hooked up my laptop straight to my router (eth0 and eth1) and it seems to work, something in my lan tap is not working properly which id what is could be (then again I was hooked up to a router) I will find more up to date lan tap.</p></div><div id="comment-12643-info" class="comment-info"><span class="comment-age">(11 Jul '12, 19:44)</span> keyboardmonkey</div></div><span id="12646"></span><div id="comment-12646" class="comment not_top_scorer"><div id="post-12646-score" class="comment-score"></div><div class="comment-text"><blockquote><p>something in my lan tap is not working properly which id what is could be (then again I was hooked up to a router)</p></blockquote><p>maybe it's better to <a href="http://www.dual-comm.com/products.htm">buy a TAP</a> (or any other vendor) than building one yourself ;-)</p><p>BTW: For simple networks, a <a href="http://www.dual-comm.com/gigabit_port-mirroring-LAN_switch.htm">port mirroring switch</a> is usually sufficient</p></div><div id="comment-12646-info" class="comment-info"><span class="comment-age">(12 Jul '12, 00:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12550" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-12550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

