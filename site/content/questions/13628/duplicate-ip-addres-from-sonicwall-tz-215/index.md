+++
type = "question"
title = "Duplicate IP addres from Sonicwall TZ-215"
description = '''I have an Copper pipe which includes 60 usable Public IP Addresses. Maybe 20 of them are actually in use; lets say 10.0.0.2 - 10.0.0.22 ( using local IPs for security ) I am currently getting intermittent connectivity on my network. I assigned my laptop 10.0.0.2 and all other routers are assigned 10...'''
date = "2012-08-14T11:57:00Z"
lastmod = "2012-08-14T16:18:00Z"
weight = 13628
keywords = [ "duplicate", "mac-address" ]
aliases = [ "/questions/13628" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate IP addres from Sonicwall TZ-215](/questions/13628/duplicate-ip-addres-from-sonicwall-tz-215)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13628-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an Copper pipe which includes 60 usable Public IP Addresses.</p><p>Maybe 20 of them are actually in use; lets say 10.0.0.2 - 10.0.0.22 ( using local IPs for security )</p><p>I am currently getting intermittent connectivity on my network.</p><p>I assigned my laptop 10.0.0.2 and all other routers are assigned 10.0.0.x if x &gt; 2 &amp;&amp; x &lt;=22</p><p>I am pinging the HP1810 switch, 10.0.0.3, and one router, 10.0.0.4. I am also pinging the Main Router IP, 10.0.0.1, the WAN serial IP, 192.0.0.1 and DNS, 4.2.2.2</p><p>From External I am pinging 10.0.0.3 and 192.0.0.1</p><p>When the issue occurs, I lose packets on my internal ping ONLY to 10.0.0.1, 192.0.0.1, 4.2.2.2. I do not lose packets on internal pinging to 10.0.0.3, 10.0.0.4, nor do the external pings show dropped packets.</p><p>It appears that something is clogging things up such as a broadcast, loop, or duplicate IP addresses.</p><p>I troubleshooted by running wireshark from my laptop on 10.0.0.2. I then ran an ipscanner to the subnet to get the ARPs back from them.</p><p>When I apply filter : expert.message contains "Duplicate IP address"</p><p>I see a lot of</p><blockquote><p>Duplicate IP address detected for 10.0.0.z (xx:xx:xx:xx:xx:xx) - also in use by yy:yy:yy:yy:yy:yy (frame 149)</p></blockquote><p>Now the MAC address xx:... correlates to a Sonicwall TZ-215 and z has been 10 different IPs and yy:... mac address has been 10 different MACs.</p><p>Is this what is causing my issues? the Sonicwall somehow fixing itself to multiple IP address on the subnet?</p><p>I also received the following:</p><blockquote><p>582 7.423492000 Cisco_ <em>xx:xx:xx Dell</em> _yy:yy:yy ARP 60 Who has 10.0.0.2? Tell 10.0.0.15 (duplicate use of 10.0.0.15 detected!)</p></blockquote><p>and</p><blockquote><p>583 7.423559000 Dell_ <em>yy:yy:yy Cisco</em> _xx:xx:xx ARP 42 10.0.0.2 is at yy:yy:yy:yy:yy:yy (duplicate use of 10.0.0.15 detected!)</p></blockquote><p>Now the Dell with yy:... MAC address is my laptop that sent out the ipscan and the Cisco xx:... is presumably a router with the ip address 10.0.0.15</p><p>What is that about as well?</p><p>Thanks for the help peoples!!</p></div><div id="question-tags" class="tags-container tags">duplicate mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/79af03a314d8a2bca111b2737b33f8ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eherr9633&#39;s gravatar image" /><p>eherr9633<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eherr9633 has no accepted answers">0%</span></p></div></div><div id="comments-container-13628" class="comments-container"></div><div id="comment-tools-13628" class="comment-tools"></div><div class="clear"></div><div id="comment-13628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13639"></span>

<div id="answer-container-13639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this what is causing my issues? the Sonicwall somehow fixing itself to multiple IP address on the subnet?</p></blockquote><p>Sounds like the SonicWall is doing Proxy ARP for parts of the network. This can be caused by</p><ul><li>running the SonicWall in bridged mode</li><li>A "wrong" NAT policy on the SonicWall, which can cause it to perform Proxy ARP for the local network</li><li>a possible configuration error with VPN IP pools. If you chose a part of your LAN network for the VPN pool, the firewall could do ProxyARP for those IP addresses as well. I have seen this with other firewalls, but I can't remember if I have ever seen it with SonicWall!</li><li>a bug in the firmware</li></ul><p>If the SonicWall is not configured for bridging, I suggest to look for any "strange" NAT rules, that don't make any sense in your environment. Think TWICE, then disable them. Then clear the ARP cache on your test system and try again.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13639" class="comments-container"></div><div id="comment-tools-13639" class="comment-tools"></div><div class="clear"></div><div id="comment-13639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

