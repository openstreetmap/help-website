+++
type = "question"
title = "ARP Question"
description = '''I am a novice wireshark user. I noticed yesterday while trying to solve an unrelated problem that ARP requests appeared to be a majority of the traffic on our network. After letting wireshark run for a while, it was nearly 60%. As I looked closer, it appears that our router is sending ARP packets to...'''
date = "2011-03-02T12:01:00Z"
lastmod = "2013-01-31T18:46:00Z"
weight = 2639
keywords = [ "arp" ]
aliases = [ "/questions/2639" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [ARP Question](/questions/2639/arp-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2639-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a novice wireshark user. I noticed yesterday while trying to solve an unrelated problem that ARP requests appeared to be a majority of the traffic on our network. After letting wireshark run for a while, it was nearly 60%. As I looked closer, it appears that our router is sending ARP packets to IP addresses that don't even exist on our network at least every second. One specific IP address that is not in use on our network (could have been at one time with DHCP an all), totaled up almost 5000 ARP requests in about an hour. Is this normal ARP behavior?</p></div><div id="question-tags" class="tags-container tags">arp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '11, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/757455416602e4b173fd03853d256f82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InTheCloud&#39;s gravatar image" /><p>InTheCloud<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InTheCloud has no accepted answers">0%</span></p></div></div><div id="comments-container-2639" class="comments-container"></div><div id="comment-tools-2639" class="comment-tools"></div><div class="clear"></div><div id="comment-2639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2642"></span>

<div id="answer-container-2642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2642-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is normal to see a pretty high ARP request count if you just capture traffic passively without the use of a SPAN/Mirror Port or any other capture method, because you'll mostly see broadcast traffic (which includes ARP messages).</p><p>The one thing worth investigating might be the fact that there are ARP requests for non-existent IP addresses in your network (even though this is pretty common in most networks; you already mentioned DHCP being a reason for it). Maybe someone is running a network scan, or there is a misconfiguration somewhere pointing to that IP address. ARP requests are used to find MAC (hardware) addresses to be able to send IP packets to the correct network card of the receiving node. If you see ARP requests for an IP that should not exists you might want to find out why and who triggers the ARP. This can be a time consuming process because you need to find the origin of the IP packet that resulted in the ARP request. Routers often ARP for IPs without being the sender of the IP packet that triggered the ARP request, so you need to find out what station does.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '11, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Mar '11, 14:43</p></div></div><div id="comments-container-2642" class="comments-container"></div><div id="comment-tools-2642" class="comment-tools"></div><div class="clear"></div><div id="comment-2642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18207"></span>

<div id="answer-container-18207" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18207-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had this same issue at my home network. I checked out the router and noticed noticed in the DHCP client list there was a device listed with that IP, but that device was turned off and had been for some time. After some further investigation I noticed that the DHCP lease time was set to "forever", causing this device to remain in the client list, therefore the router continued to send ARP requests to a non existent PC. I changed the lease time to two weeks then refreshed the client list, the device was no longer listed. Ran another packet capture and the ARP requests no longer appeared.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 18:46</strong></p><img src="https://secure.gravatar.com/avatar/9854773d977a02fbc4214e4849b1d8d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kidicarus81&#39;s gravatar image" /><p>kidicarus81<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kidicarus81 has no accepted answers">0%</span></p></div></div><div id="comments-container-18207" class="comments-container"></div><div id="comment-tools-18207" class="comment-tools"></div><div class="clear"></div><div id="comment-18207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2652"></span>

<div id="answer-container-2652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2652-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As was previously stated, you do see a lot of arps. One reason is that you may not be seeing all of the traffic on your network, but you are seeing all of the arps. If that truly becomes an issue, there are some ways to mitigate them. One way is to break the network into smaller broadcast domains. Another would be to use private vlans to limit connectivity between workstations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '11, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2652" class="comments-container"></div><div id="comment-tools-2652" class="comment-tools"></div><div class="clear"></div><div id="comment-2652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

