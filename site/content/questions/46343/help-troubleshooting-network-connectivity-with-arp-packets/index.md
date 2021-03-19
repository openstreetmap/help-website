+++
type = "question"
title = "Help troubleshooting network connectivity with ARP packets"
description = '''Hello, I&#x27;ve recently started renting an office and have not been able to successfully connect to the Internet with the network config details that have been shared with me by the internet host here. I put in the static IP and gateway and associated details in my TCP/IPv4 properties and when I connec...'''
date = "2015-10-02T08:49:00Z"
lastmod = "2015-10-07T10:05:00Z"
weight = 46343
keywords = [ "arp", "connectivity", "troubleshooting" ]
aliases = [ "/questions/46343" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help troubleshooting network connectivity with ARP packets](/questions/46343/help-troubleshooting-network-connectivity-with-arp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46343-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I've recently started renting an office and have not been able to successfully connect to the Internet with the network config details that have been shared with me by the internet host here. I put in the static IP and gateway and associated details in my TCP/IPv4 properties and when I connect Windows shows it sending and receiving packets, but never reaches the Internet.</p><p>I installed WireShark this morning and did some quick reading about how to use it and what I'm seeing is that my computer is broadcasting an ARP message asking for the MAC address of the gateway, after a little delay the gateway responds with its MAC address, and then my computer either ignores it, or tries to ping it unsuccessfully. And so it just keep repeating this process over and over again, along with numerous SSDP, DNS, and LLMNR packets interspersed throughout. I checked the ARP table on my computer and it was showing a physical address of 00-00-00-00-00-00 for the gateway, so I manually added the gateway's MAC address with the link disconnected, and then when I reconnected it erased the correct MAC address and put the 00-00-00-00-00-00 one back in.</p><p>I'm new to this type of troubleshooting so I'm hoping someone can help me figure out what's going on here!</p><p>Edit: a few more details - the internet here is fiber based and is fed from a single ethernet cable running from the fiber box to a EZXS88W switch. There are 5 static IPs "available", with at least 2 of those 5 known to be in use already. The switch has a wired router connected to it, and the wired router is using the 1st of the 5 static IPs. My end goal is to get a VOIP adapter connected. I originally was connecting to the router with the first static IP, and my computer would connect fine to it, but the VOIP adapater (and second router that I tried) failed to get a connection, trying both dynamic and static IPs to the router. The office owner then gave me the outside connection details (static IP, gateway, subnet mask) and so now I'm connecting directly into the EZXS88W switch. I don't think the problem is with my laptop though because when I connect the VOIP adapter or second router directly to the switch with the static ip assigned, they don't get access to the internet either.</p></div><div id="question-tags" class="tags-container tags">arp connectivity troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '15, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/80e1cc52121876e133b1d2f06beb611a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jessman1128&#39;s gravatar image" /><p>jessman1128<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jessman1128 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '15, 09:22</p></div></div><div id="comments-container-46343" class="comments-container"><span id="46356"></span><div id="comment-46356" class="comment"><div id="post-46356-score" class="comment-score">1</div><div class="comment-text"><p>This is a (Windows) network trouble shooting question. Go talk to the other tenants using this uplink on how they set it up.</p></div><div id="comment-46356-info" class="comment-info"><span class="comment-age">(04 Oct '15, 23:19)</span> Jaap ♦</div></div></div><div id="comment-tools-46343" class="comment-tools"></div><div class="clear"></div><div id="comment-46343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46404"></span>

<div id="answer-container-46404" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46404-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I eventually figured out that my issues were with a faulty network cable. Once I replaced the cable the problems disappeared.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/80e1cc52121876e133b1d2f06beb611a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jessman1128&#39;s gravatar image" /><p>jessman1128<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jessman1128 has one accepted answer">100%</span></p></div></div><div id="comments-container-46404" class="comments-container"></div><div id="comment-tools-46404" class="comment-tools"></div><div class="clear"></div><div id="comment-46404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

