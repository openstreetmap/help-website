+++
type = "question"
title = "Bandwidth occupation between two devices"
description = '''Dear Guys, I think wht I&#x27;m gonna ask is very simple for you, but it&#x27;s driving me crazy. We are talking about videodoorphones, I need to prove that the bandwidth occupied between two devices is higher than declared.  They work great in the same LAN, but it&#x27;s not possible to make them work through a V...'''
date = "2016-04-27T06:31:00Z"
lastmod = "2016-04-27T06:52:00Z"
weight = 52014
keywords = [ "traffic", "bandwidth", "size", "data", "occupation" ]
aliases = [ "/questions/52014" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bandwidth occupation between two devices](/questions/52014/bandwidth-occupation-between-two-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52014-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Guys, I think wht I'm gonna ask is very simple for you, but it's driving me crazy. We are talking about videodoorphones, I need to prove that the bandwidth occupied between two devices is higher than declared. They work great in the same LAN, but it's not possible to make them work through a VPN. SO, I need to measure how much data are exchanged when I make a call. Very easy: two IPs in the same LAN: 192.168.20.149 and 192.168.20.150. How wide has to be the bandwidth to make the system work prpoperly? Is it possible to see this infos in real time, while I try to make a call? Thx for your help, and forgive my bad english :)</p></div><div id="question-tags" class="tags-container tags">traffic bandwidth size data occupation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '16, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/6f3c73982add2ae23549afa472c83462?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meglioabbe&#39;s gravatar image" /><p>meglioabbe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meglioabbe has no accepted answers">0%</span></p></div></div><div id="comments-container-52014" class="comments-container"></div><div id="comment-tools-52014" class="comment-tools"></div><div class="clear"></div><div id="comment-52014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52015"></span>

<div id="answer-container-52015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52015-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use Wireshark to capture the communication between the two devices (see <a href="https://wiki.wireshark.org/CaptureSetup">this link</a> for possible capturing setups) and then use tools from the <code>Statistics</code> menu to find the bandwidth.</p><p>However, the routers along the path and VPN boxes at its ends may perform worse than you expect. When talking about packet transports, the raw bandwidth (bits per second) is one thing, but packets per second is another - routers with lower power may have problems with a lot of small packets while they can handle the same amount of data transferred as less but longer packets without trouble). And if the encryption at the VPN boxes is not implemented in hardware, the throughput may be much less than raw speed of the interfaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52015" class="comments-container"><span id="52017"></span><div id="comment-52017" class="comment"><div id="post-52017-score" class="comment-score"></div><div class="comment-text"><p>Dear Sindy, thanks for your prompt answer. Can you suggest the setup to me? Which fitlers to use? I need to monitr the LAN traffic betweem the addresses 192.168.20.150 and 149, my PC is .41. If this is helful, the devices and my PC are connected to the same switch Thank you</p></div><div id="comment-52017-info" class="comment-info"><span class="comment-age">(27 Apr '16, 08:19)</span> meglioabbe</div></div><span id="52020"></span><div id="comment-52020" class="comment"><div id="post-52020-score" class="comment-score"></div><div class="comment-text"><p>That's why I've pointed you to the wiki page. The point is that capturing on a plain (i.e. not "managed") switch is close to impossible, unless you use very specific techniques to drive it mad so that it would start acting as a hub.</p><p>You need to either capture (= run Wireshark or tcpdump) on one of the devices in question, which I assume isn't possible for you, or you need some intermediate device through which the traffic between the two boxes would pass (like e.g. the PC on which you capture if it has two network cards), or you need a switch which can mirror traffic passing through one port to another one, or a hub (an almost extinct species these days).</p><p>So capture filters are the last thing to think about I'd say.</p><p>I'll be on the road for next four hours, so you have plenty of time for reading the Wiki. Feel free to come back if something isn't clear there.</p></div><div id="comment-52020-info" class="comment-info"><span class="comment-age">(27 Apr '16, 08:56)</span> sindy</div></div></div><div id="comment-tools-52015" class="comment-tools"></div><div class="clear"></div><div id="comment-52015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

