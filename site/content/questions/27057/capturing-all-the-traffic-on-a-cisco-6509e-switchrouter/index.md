+++
type = "question"
title = "Capturing all the traffic on a Cisco 6509E (switch/router)"
description = '''I have a CISCO 6509E switch/router and I would like to capture ALL the traffic that is passing through it. This is a very common switch/router. It is dedicated and acting like a load balancer to three Apache web servers. The traffic is not terribly heavy. I could mirror the three switch ports which ...'''
date = "2013-11-17T10:33:00Z"
lastmod = "2013-11-17T11:07:00Z"
weight = 27057
keywords = [ "traffic", "6509e", "cisco" ]
aliases = [ "/questions/27057" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing all the traffic on a Cisco 6509E (switch/router)](/questions/27057/capturing-all-the-traffic-on-a-cisco-6509e-switchrouter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a CISCO 6509E switch/router and I would like to capture ALL the traffic that is passing through it. This is a very common switch/router. It is dedicated and acting like a load balancer to three Apache web servers. The traffic is not terribly heavy. I could mirror the three switch ports which feed off the 6509E and set up wireshark on each. Are there monitoring ports on the 6509E which would allow me plug in WireShark and see everything? I should probably be asking this question to CISCO. I guess my general question is, is there a way to set up WireShark to capture all of the Unicast, Multicast and Broadcast traffic for all ports on a switch or a router?</p></div><div id="question-tags" class="tags-container tags">traffic 6509e cisco</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/16c80ca493c77f3486cbb7ff38cc5d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoberist&#39;s gravatar image" /><p>Zoberist<br />
<span class="score" title="0 reputation points">0</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoberist has no accepted answers">0%</span></p></div></div><div id="comments-container-27057" class="comments-container"></div><div id="comment-tools-27057" class="comment-tools"></div><div class="clear"></div><div id="comment-27057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27058"></span>

<div id="answer-container-27058" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27058-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, the 6500 series can do mirror/monitor/SPAN ports. If you configure all ports that have devices on them to be mirrored to a single output port and hook up a Wireshark PC to that port you could theoretically capture all the traffic. Theoretically, because the output port has a certain maximum bandwidth (1G or 10G maybe), and if the monitored ports send more than that to the output port it will not forward all of it to the Wireshark PC.</p><p>You should take a look at the "monitor session" command, like on this page:</p><p><a href="http://www.cisco.com/en/US/products/hw/switches/ps708/products_tech_note09186a008015c612.shtml">http://www.cisco.com/en/US/products/hw/switches/ps708/products_tech_note09186a008015c612.shtml</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '13, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27058" class="comments-container"><span id="27062"></span><div id="comment-27062" class="comment"><div id="post-27062-score" class="comment-score"></div><div class="comment-text"><p>Outstanding, thank you very much especially for the URL. I am reading the document now.</p></div><div id="comment-27062-info" class="comment-info"><span class="comment-age">(17 Nov '13, 17:20)</span> Zoberist</div></div><span id="27063"></span><div id="comment-27063" class="comment"><div id="post-27063-score" class="comment-score">1</div><div class="comment-text"><p>Note that the page in question, and other pages discussing mirror/monitor/SPAN/etc. capabilities on various switches, can be found on the per-vendor pages under the <a href="http://wiki.wireshark.org/SwitchReference">SwitchReference page on the Wireshark Wiki</a>.</p></div><div id="comment-27063-info" class="comment-info"><span class="comment-age">(17 Nov '13, 18:21)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27058" class="comment-tools"></div><div class="clear"></div><div id="comment-27058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

