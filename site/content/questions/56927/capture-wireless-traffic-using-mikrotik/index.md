+++
type = "question"
title = "Capture wireless traffic using mikrotik"
description = '''Hi  so my laptop has a crap card with no monitoring mode but i have some very nifty mikrotiks  is there anyway i can use the wirless on those in monitoring mode and the capture through the Ethernet interface i think it should work if i try and create a SPAN port on them and then use wireless sniffer...'''
date = "2016-11-02T07:45:00Z"
lastmod = "2016-11-02T08:48:00Z"
weight = 56927
keywords = [ "wireless", "sniffing", "mikrotik" ]
aliases = [ "/questions/56927" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture wireless traffic using mikrotik](/questions/56927/capture-wireless-traffic-using-mikrotik)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56927-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>so my laptop has a crap card with no monitoring mode but i have some very nifty mikrotiks is there anyway i can use the wirless on those in monitoring mode and the capture through the Ethernet interface</p><p>i think it should work if i try and create a SPAN port on them and then use wireless sniffer on the wireless cards and plug into the SPAN (ether side) and see all the traffic at least that is my theory will this work?</p><p>if there is another way please let me know</p></div><div id="question-tags" class="tags-container tags">wireless sniffing mikrotik</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '16, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/98ae0bbe126e829e5ab083d3d40bd1c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reynhard%20Wouda&#39;s gravatar image" /><p>Reynhard Wouda<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reynhard Wouda has no accepted answers">0%</span></p></div></div><div id="comments-container-56927" class="comments-container"></div><div id="comment-tools-56927" class="comment-tools"></div><div class="clear"></div><div id="comment-56927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56928"></span>

<div id="answer-container-56928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56928-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Mikrotik has its own flavour of remote capturing, which consists in prefixing each captured frame with a TZSP header and encapsulation of the result into a UDP packet. So unlike with port mirroring at L2, you can route the encapsulated captured frames over L3 network. Details are <a href="http://wiki.mikrotik.com/wiki/Ethereal/Wireshark">here</a>, you can do the same using Webfig, yet I don't have access to any Mikrotik right now to give you a screenshot.</p><p>If you take the advantage of routing the captured packets, think of not routing them via the interface on which you capture, and think of the bandwidth along the path between the Mikrotik and the machine where you run Wireshark - it's UDP so a dropped packet is lost forever.</p><p>In general, captured wireless frames cannot be monitored on Ethernet port without modification because the frame header is different and because some important bits of information (RSSI, channel...) are not part of the frame. That's why radiotap, TZSP and other encapsulation headers are used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '16, 01:22</p></div></div><div id="comments-container-56928" class="comments-container"></div><div id="comment-tools-56928" class="comment-tools"></div><div class="clear"></div><div id="comment-56928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

