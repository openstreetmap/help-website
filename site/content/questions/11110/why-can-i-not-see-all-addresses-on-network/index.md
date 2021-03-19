+++
type = "question"
title = "Why can I not see all addresses on network?"
description = '''Hi, I need some help. I have installed Wireshark on a PC that is connected to a switch, this inturn is connected to a Motorola CMM and then to multiple Motorola Canopy backhauls which then feed to CMM and then onto the AP/SM. all these are on 10.x.x.x I can see some of the 10.x.x.x IP addresses, I c...'''
date = "2012-05-17T11:17:00Z"
lastmod = "2012-05-17T15:03:00Z"
weight = 11110
keywords = [ "ip" ]
aliases = [ "/questions/11110" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can I not see all addresses on network?](/questions/11110/why-can-i-not-see-all-addresses-on-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11110-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need some help. I have installed Wireshark on a PC that is connected to a switch, this inturn is connected to a Motorola CMM and then to multiple Motorola Canopy backhauls which then feed to CMM and then onto the AP/SM. all these are on 10.x.x.x</p><p>I can see some of the 10.x.x.x IP addresses, I can also see some of the customers IP addresses (i.e. 75.x.x.x, 206.x.x.x) but these are random IP addresses across the network. I have been told that this may be because of the switch or CMM, is there a solution for this? Is there a way to force an IP address into the filter so I can check just 1 IP address?</p><p>With the results I get I just want to see what websites are being viewed - just to monitor how many are logging onto netflix for example!</p><p>Thanks</p><p>Steve</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/11776f84d6e8d1f0bd2c24fd9c1bf602?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevewarden0&#39;s gravatar image" /><p>stevewarden0<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevewarden0 has no accepted answers">0%</span></p></div></div><div id="comments-container-11110" class="comments-container"></div><div id="comment-tools-11110" class="comment-tools"></div><div class="clear"></div><div id="comment-11110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11119"></span>

<div id="answer-container-11119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11119-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>I have installed Wireshark on a PC that is connected to a switch</code><br />
</p></blockquote><p>Based on the information you provided, I assume your PC is connected to a simple access port on the switch. In that case, you will only see your own traffic and broadcast traffic within Wireshark. Maybe that's the traffic you are capturing (10.x.x.x local broadcasts, 75.x.x.x, 206.x.x.x broadcasts from systems behind the CMM).</p><p>If you want to capture the whole traffic, you need to configure port mirroring on your switch or use a TAP or any other method described here: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><blockquote><p><code>just to monitor how many are logging onto netflix for example!</code></p></blockquote><p>In that case you need to mirror/monitor the port where your WAN (Internet) router is connected to your switch (see wiki above and your switch manual). Use the following capture filter to capture DNS requests and HTTP(s) requests:</p><blockquote><p><code>port 53 or port 80 or port 443</code></p></blockquote><p>After you have captured enough data, you can look for netflix requests with this display filters:</p><blockquote><p><code>dns.qry.name contains netflix or http.host contains netflix</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 15:12</p></div></div><div id="comments-container-11119" class="comments-container"></div><div id="comment-tools-11119" class="comment-tools"></div><div class="clear"></div><div id="comment-11119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

