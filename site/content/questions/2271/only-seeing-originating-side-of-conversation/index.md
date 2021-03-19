+++
type = "question"
title = "Only seeing originating side of conversation"
description = '''I am trying to get a trace from a Cisco 3750 using a port monitor. I am only seeing the originating side of any conversation. It doesn&#x27;t make a difference if the device that is attached to the source switch port is originating the conversation or is the destination. Ex. When I ping this device or pi...'''
date = "2011-02-10T08:45:00Z"
lastmod = "2011-02-14T08:40:00Z"
weight = 2271
keywords = [ "conversation", "only", "originate" ]
aliases = [ "/questions/2271" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Only seeing originating side of conversation](/questions/2271/only-seeing-originating-side-of-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get a trace from a Cisco 3750 using a port monitor. I am only seeing the originating side of any conversation. It doesn't make a difference if the device that is attached to the source switch port is originating the conversation or is the destination. Ex. When I ping this device or ping from this device, I only see the ICMP ECHO request. I never see the reply, even though the devices can PING each other. I have removed and reinstall Wireshark and Winpcap.</p><p>Here is my monitor config from my switch: monitor session 1 source interface Gi2/0/19 monitor session 1 destination interface Gi2/0/24</p></div><div id="question-tags" class="tags-container tags">conversation only originate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/79bf428f46e44022b9c2c0ea1ddadcf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flrdr&#39;s gravatar image" /><p>flrdr<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flrdr has no accepted answers">0%</span></p></div></div><div id="comments-container-2271" class="comments-container"><span id="2273"></span><div id="comment-2273" class="comment"><div id="post-2273-score" class="comment-score"></div><div class="comment-text"><p>My first thought was that the monitor session was setup only mirroring either incoming or outgoing frames, but if you never see the ICMP ECHO reply no matter if the mirrored port is sending or receiving it this can't be the case. Which is kinda strange, I have to admit.</p><p>Does the device at Gi2/0/19 have more than one network card maybe? Maybe an active Wireless card, and you have a asymetric conversation using two interfaces?</p><p>Is the other device in the same subnet, or is there a router involved? If so, what happens if you ping a device in the same subnet?</p></div><div id="comment-2273-info" class="comment-info"><span class="comment-age">(10 Feb '11, 09:49)</span> Jasper ♦♦</div></div><span id="2283"></span><div id="comment-2283" class="comment"><div id="post-2283-score" class="comment-score"></div><div class="comment-text"><p>The device on G2/0/19 only has one NIC. I see the same results pinging within the same subnet. I also tested to other ports with test PCs (1 NIC) with the same results. It appears that the problem is with my laptop or with the Wireshark options. I loaded Wireshark on a new Win7 laptop, and the captures works OK. The real strange thing is - If I use the "bad" laptop to sniff it's own traffic, I can see both sides of the conversation. When I use it to sniff the monitor port, I only see the originator's side. Any ideas on what could be causing this? Any help is greatly appreciated !!</p></div><div id="comment-2283-info" class="comment-info"><span class="comment-age">(11 Feb '11, 09:33)</span> flrdr</div></div></div><div id="comment-tools-2271" class="comment-tools"></div><div class="clear"></div><div id="comment-2271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2323"></span>

<div id="answer-container-2323" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2323-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to determine that a Check Point VPN client (SecureClient) that we run on our laptops was causing the problem. I tried disabling the Check Point services and the security policy, but that didn't help. I had to completely remove the VPN client and wireshark runs just fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/79bf428f46e44022b9c2c0ea1ddadcf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flrdr&#39;s gravatar image" /><p>flrdr<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flrdr has no accepted answers">0%</span></p></div></div><div id="comments-container-2323" class="comments-container"><span id="2331"></span><div id="comment-2331" class="comment"><div id="post-2331-score" class="comment-score"></div><div class="comment-text"><p>Good thing you found what caused the trouble, and probably worth keeping in mind. I myself avoid installing the Cisco VPN client for similar reasons :-)</p></div><div id="comment-2331-info" class="comment-info"><span class="comment-age">(14 Feb '11, 14:07)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2323" class="comment-tools"></div><div class="clear"></div><div id="comment-2323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2284"></span>

<div id="answer-container-2284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2284-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your "bad" laptop has a faulty NIC that doesn't "like" all the frames coming in. The last thing I would check if you have a duplicate MAC address in your network (for example, the "bad" laptop having the same as the device on G2/0/19). Duplicate MAC addresses are very hard to spot unless you're suspecting it, and can lead to network behavior that seems to be random at best.</p><p>Otherwise I think it's either the hardware or the OS being "on the fritz" or both.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '11, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2284" class="comments-container"><span id="2286"></span><div id="comment-2286" class="comment"><div id="post-2286-score" class="comment-score"></div><div class="comment-text"><p>I don't think that it's hardware. The laptop works fine except when using wireshark. Also, it can sniff it's own traffic OK. When it's just listening to a monitored swith port, it's MAC address shouldn't have much to do with it.</p></div><div id="comment-2286-info" class="comment-info"><span class="comment-age">(11 Feb '11, 10:06)</span> flrdr</div></div><span id="2292"></span><div id="comment-2292" class="comment"><div id="post-2292-score" class="comment-score"></div><div class="comment-text"><p>Okay, it was just a thought :-) If the hardware is working fine then it must be a software problem. Next thing I would check if the same hardware booted into a Backtrack or Ubuntu live CD has the same trouble.</p></div><div id="comment-2292-info" class="comment-info"><span class="comment-age">(12 Feb '11, 03:32)</span> Jasper ♦♦</div></div></div><div id="comment-tools-2284" class="comment-tools"></div><div class="clear"></div><div id="comment-2284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

