+++
type = "question"
title = "SMB communication on tcp port 445 causes huge traffic in network"
description = '''Hello All, I am faced with a strange situation.  All of the lan interfaces in a vlan are receiving too much traffic for two hours every morning.  I captured the traffic and the traffic is tcp traffic between two servers on port 445. The traffic I am talking about is not netbios traffic but it is sti...'''
date = "2015-12-10T05:39:00Z"
lastmod = "2015-12-10T11:49:00Z"
weight = 48418
keywords = [ "flood", "smb" ]
aliases = [ "/questions/48418" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB communication on tcp port 445 causes huge traffic in network](/questions/48418/smb-communication-on-tcp-port-445-causes-huge-traffic-in-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48418-score" class="post-score" title="current number of votes">0</div><span id="post-48418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am faced with a strange situation. All of the lan interfaces in a vlan are receiving too much traffic for two hours every morning. I captured the traffic and the traffic is tcp traffic between two servers on port 445. The traffic I am talking about is not netbios traffic but it is still getting received on all of the interfaces in the vlan on which those two servers reside. I have traced to the source of the traffic and it seems that it is Microsoft SCCM server. I have attached the screenshots of the packet capture and the statistics of that packet capture. Also I am capturing traffic in promiscuous mode but other traffic (traffic other than 445) between those two servers is not seen on every other host in that Vlan. Can somebody please help me…</p><p>Please refer the packet capture details : <a href="http://s30.photobucket.com/user/sushk21/media/Capture_445.png.html"><img src="http://i30.photobucket.com/albums/c331/sushk21/Capture_445.png" alt=" photo Capture_445.png" /></a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flood" rel="tag" title="see questions tagged &#39;flood&#39;">flood</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '15, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/2ec2c457690230aceaadee320100e8bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shivaavaya&#39;s gravatar image" /><p><span>shivaavaya</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shivaavaya has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 05:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-48418" class="comments-container"></div><div id="comment-tools-48418" class="comment-tools"></div><div class="clear"></div><div id="comment-48418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48429"></span>

<div id="answer-container-48429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48429-score" class="post-score" title="current number of votes">0</div><span id="post-48429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After some out-of-band communication with the author of the question, the answer is that the flooding of non-participants of the tcp session in question is caused by use of Mircosoft's Network Load Balancing mechanism in the LAN.</p><p>The packets which flood the non-participants look as follows:</p><pre><code>Ethernet II, Src: d8:8d:37:14:59:a8, Dst: 02:bf:0a:0e:23:f7
Destination: 02:bf:0a:0e:23:f7
    Address: 02:bf:0a:0e:23:f7
    .... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the factory default)
    .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Source: d8:8d:37:14:59:a8
    Address: d8:8d:37:14:59:a8
    .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Type: IPv4 (0x0800)
Internet Protocol Version 4, Src: 10.14.35.232, Dst: 10.14.35.224</code></pre><p>(IP and MAC addresses manually anonymized)</p><p>The destination MAC address is not a multicast one, but it is a "locally administered" one. The <code>02 bf</code> indicates that the MAC is created by MS NLB, the remaining four bytes represent an IPv4 address.</p><p>The overall functionality is such that there is a group of NICs which the administrator wants to participate in handling requests sent to a common IP address depending on their actual load, so they need to make the network deliver each request to all of them. Which one will actually serve a given request is their internal decision.</p><p>To achieve that goal, the group responds to arp requests to the group IP address with the <code>02:bf:ip:ad:re:ss</code> MAC address, but each NIC sends outgoing IP packets with its real MAC address as source. As a consequence, the switches in the network never see the <code>02:bf:ip:ad:re:ss</code> as source MAC, so they cannot associate it to any port, and thus any packet with this address as destination MAC is sent to all ports of the switch (leaving VLANs and the ingress port aside for simplicity). This behaviour is essential to make the whole idea work, and the collateral damage is that everything else connected to that LAN is flooded with copies of all packets sent towards the group IP.</p><p>Microsoft seems to support use of multicast MAC address, instead of a unicast one, for the group IP. On more advanced switches, use of multicast MAC address allows to choose which ports should forward such traffic on egress and which not, but not every switch can do that and some of those which can have to spend extra CPU power on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '15, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 13:10</strong> </span></p></div></div><div id="comments-container-48429" class="comments-container"></div><div id="comment-tools-48429" class="comment-tools"></div><div class="clear"></div><div id="comment-48429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

