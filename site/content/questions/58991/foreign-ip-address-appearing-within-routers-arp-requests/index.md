+++
type = "question"
title = "Foreign IP address appearing within router&#x27;s ARP requests"
description = '''Hi there, I am quite new to programs like Wireshark for sniffing web traffic. However as of recent I have had strange disruptions to my wifi network and I am concerned as I live in a unit where the router is shared amongst 4 other people. As such I did some basic traffic monitoring to learn about th...'''
date = "2017-01-23T18:26:00Z"
lastmod = "2017-01-23T18:53:00Z"
weight = 58991
keywords = [ "arp", "arpspoofing", "security", "null", "beginner" ]
aliases = [ "/questions/58991" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Foreign IP address appearing within router's ARP requests](/questions/58991/foreign-ip-address-appearing-within-routers-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58991-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am quite new to programs like Wireshark for sniffing web traffic. However as of recent I have had strange disruptions to my wifi network and I am concerned as I live in a unit where the router is shared amongst 4 other people.</p><p>As such I did some basic traffic monitoring to learn about the potential processes and thus stumbled upon this.</p><p>I am just looking at ARP traffic to see if there are any strange nuances and I want to clarify this particularly. I slapped on an ARP filter to find some usual devices sending ARP requests to and from my router. However what scared me is the fact there was an IP based in the US that was being identified by my neighbour's computer.</p><p>The exact Detail:</p><p>"David's Local" ARP Who is 169.254.92.168? Tell 0.0.0.0 My IP does not start with 169 address and furthermore the prior address is linked to a server in Fairfax US, I live in Oceania.</p><p>Why is there a Null destination.</p><p>Furthermore what creeps me out is, all the devices registered on the network are sending ARP information to a fixed address that is not listed on the devices I have currently idetnified belonging to my network. And based on my neighbour's ARP requests, It keeps asking for an ARP request for This particular address, however the destination is a null address 0.0.0.0</p><p>To simplify some of this, there are continual ARP resolution requests to an IP address in my local network that I cannot recognize or identiify, However all ARP requests for this particular IP are directed to a Null address. So basically all requests for ARP are sent to this IP, but an ARP requests for that IP is sent to a null. And to add theres a foreign Ip from another country being requested which is also being told to a null IP.</p><p>Please help</p></div><div id="question-tags" class="tags-container tags">arp arpspoofing security null beginner</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 18:26</strong></p><img src="https://secure.gravatar.com/avatar/443d450ed9fec9e368175a7e97bae345?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nilstor&#39;s gravatar image" /><p>Nilstor<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nilstor has no accepted answers">0%</span></p></div></div><div id="comments-container-58991" class="comments-container"></div><div id="comment-tools-58991" class="comment-tools"></div><div class="clear"></div><div id="comment-58991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58992"></span>

<div id="answer-container-58992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's called Automatic IP Addressing. It's an address range that can be self assigned when there is no response to a DHCP discover. The article below will explain further.</p><p><a href="http://packetlife.net/blog/2008/sep/24/169-254-0-0-addresses-explained/">http://packetlife.net/blog/2008/sep/24/169-254-0-0-addresses-explained/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '17, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jan '17, 18:54</p></div></div><div id="comments-container-58992" class="comments-container"><span id="58997"></span><div id="comment-58997" class="comment"><div id="post-58997-score" class="comment-score"></div><div class="comment-text"><p>Hey Rooster,</p><p>Thanks for the response, so would it be fair to say it just indicates theres a device on the local network that is unable to connect to the DHCP server?</p><p>To add as well, I was wondering about the null addresses. Why is it so that these IPs are sending these requests to 0.0.0.0.</p><p>And sorry to ask further but would you be able to comment about these null addresses for the 2nd IP. To add to what I've found out, my neighbour is the one holding the myseterious IP (contrary to what I thought at first) but the funny thing is, every ARP request directed towards his IP is sent to a null address '0.0.0.0' however all other ARP requests in the network are sent back to their original devices.</p><p>My main underlying concern is the possibility of network interference or unauthorized devices taking advantage of the network or a combination of both. I apologize if my response is too wordy and I appreciate your help.</p></div><div id="comment-58997-info" class="comment-info"><span class="comment-age">(23 Jan '17, 22:28)</span> Nilstor</div></div><span id="59009"></span><div id="comment-59009" class="comment"><div id="post-59009-score" class="comment-score"></div><div class="comment-text"><p>DHCP allows you to 'lease' an IP address. For the duration of the lease you may use it, afterwards you have to release it. Usually you try to renew the lease before it expires, but as in your case this sometimes fails. Once expired all you can do is use 0.0.0.0 as your IP address in ARP. Your MAC address is still valid though, so you still receive ARP replies. In short, nothing to worry about, other that failing DHCP service.</p></div><div id="comment-59009-info" class="comment-info"><span class="comment-age">(24 Jan '17, 05:51)</span> Jaap ♦</div></div><span id="59037"></span><div id="comment-59037" class="comment"><div id="post-59037-score" class="comment-score"></div><div class="comment-text"><p>Yes, it most likely indicates a device failed to lease an address from a DHCP server and self-assigned an address in the AIPAP designated range of addresses.</p><p>As for the ARP requests for "169.254.x.x tell 0.0.0.0", it is most likely the host attempting IP duplication detection to verify the address is wants to use is not already in use within the broadcast domain by another host before it binds its adapter to the address.</p></div><div id="comment-59037-info" class="comment-info"><span class="comment-age">(24 Jan '17, 16:36)</span> Rooster_50</div></div></div><div id="comment-tools-58992" class="comment-tools"></div><div class="clear"></div><div id="comment-58992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

