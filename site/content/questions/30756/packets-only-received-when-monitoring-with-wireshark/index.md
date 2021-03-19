+++
type = "question"
title = "Packets only received when monitoring with wireshark"
description = '''Hi,  I am sending ARP packets from a DSP evaluation board to software on my laptop, when I have wireshark monitoring traffic the pc software connects to my board and starts its process of sending data out. when I don&#x27;t have wireshark running it fails to connect, monitoring with Microsoft network mon...'''
date = "2014-03-13T03:26:00Z"
lastmod = "2014-03-13T09:33:00Z"
weight = 30756
keywords = [ "arp", "microsoft", "wireshark" ]
aliases = [ "/questions/30756" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Packets only received when monitoring with wireshark](/questions/30756/packets-only-received-when-monitoring-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30756-score" class="post-score" title="current number of votes">0</div><span id="post-30756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am sending ARP packets from a DSP evaluation board to software on my laptop, when I have wireshark monitoring traffic the pc software connects to my board and starts its process of sending data out. when I don't have wireshark running it fails to connect, monitoring with Microsoft network monitor instead shows that the arp request from my dsp software isn't being received, if I run both microsoft network monitor and wireshark, I can see on both packages that the ARP packets and subsequent SYN SYN-ACK ACK packets get through.</p><p>I'm hoping this is something wireshark is doing for me when it is running which I should be doing myself, does anyone have any idea what could be happening? i'm stumped at the moment and am running out of things to try.</p><p>Regards, Graham</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-microsoft" rel="tag" title="see questions tagged &#39;microsoft&#39;">microsoft</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/546507f995c7d3de255e59d1cc6d2d76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sly_Raccoon&#39;s gravatar image" /><p><span>Sly_Raccoon</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sly_Raccoon has no accepted answers">0%</span></p></div></div><div id="comments-container-30756" class="comments-container"></div><div id="comment-tools-30756" class="comment-tools"></div><div class="clear"></div><div id="comment-30756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30757"></span>

<div id="answer-container-30757" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30757-score" class="post-score" title="current number of votes">2</div><span id="post-30757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sly_Raccoon has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Possibly Wireshark is set to enable promiscuous mode which then allows the packet to be processed? I think this question has come up previously here, may be <a href="http://ask.wireshark.org/questions/6711/udp-multicast-windows-7-firewall-labview">here</a>.</p><p>An ARP request is sent to the subnet broadcast address, as by it's nature it can't be directed (the reply is), so maybe your laptop isn't recognising the ARP broadcast for some reason, maybe malformed by your DSP software.</p><p>Can you post a sample capture of the traffic somewhere (<a href="http://cloudshark.org">cloudshark</a>, etc.) and post the link back here?</p><p><strong>Edit:</strong></p><p>As discussed below, the DSP is sending Ethernet frames that are 18 bytes shorter than the minimum, so the laptop NIC is dropping them when not in promiscuous mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '14, 09:10</strong> </span></p></div></div><div id="comments-container-30757" class="comments-container"><span id="30758"></span><div id="comment-30758" class="comment"><div id="post-30758-score" class="comment-score"></div><div class="comment-text"><p>Cheers, I have disabled promiscuous mode on wireshark and it doesn't see the ARP request so that looks like the reason why it worked.</p><p>the capture details of the request I am sending are shown below, I am very new to the whole TCP/IP thing but I can't see anyting wrong with it when comparing to other ARP requests.</p><pre><code>No. Time Source Destination Protocol Length Info
1 0.000000000 c6:6a:03:ee:08:02 Broadcast ARP 42 Who has 10.
0.0.3? Tell 10.0.0.2
Frame 1: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface 0
Interface id: 0
Encapsulation type: Ethernet (1)
Arrival Time: Mar 13, 2014 11:15:49.933948000 GMT Standard Time
[Time shift for this packet: 0.000000000 seconds]
Epoch Time: 1394709349.933948000 seconds
[Time delta from previous captured frame: 0.000000000 seconds]
[Time delta from previous displayed frame: 0.000000000 seconds]
[Time since reference or first frame: 0.000000000 seconds]
Frame Number: 1
Frame Length: 42 bytes (336 bits)
Capture Length: 42 bytes (336 bits)
[Frame is marked: False]
[Frame is ignored: False]
[Protocols in frame: eth:arp]
[Coloring Rule Name: ARP]
[Coloring Rule String: arp]
Ethernet II, Src: c6:6a:03:ee:08:02 (c6:6a:03:ee:08:02), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
Destination: Broadcast (ff:ff:ff:ff:ff:ff)
Address: Broadcast (ff:ff:ff:ff:ff:ff)
.... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the
factory default)
.... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast)
Source: c6:6a:03:ee:08:02 (c6:6a:03:ee:08:02)
Address: c6:6a:03:ee:08:02 (c6:6a:03:ee:08:02)
.... ..1. .... .... .... .... = LG bit: Locally administered address (this is NOT the
factory default)
.... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Type: ARP (0x0806)
Address Resolution Protocol (request)
Hardware type: Ethernet (1)
Protocol type: IP (0x0800)
Hardware size: 6
Protocol size: 4
Opcode: request (1)
Sender MAC address: c6:6a:03:ee:08:02 (c6:6a:03:ee:08:02)
Sender IP address: 10.0.0.2 (10.0.0.2)
Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
Target IP address: 10.0.0.3 (10.0.0.3)</code></pre></div><div id="comment-30758-info" class="comment-info"><span class="comment-age">(13 Mar '14, 04:36)</span> <span class="comment-user userinfo">Sly_Raccoon</span></div></div><span id="30768"></span><div id="comment-30768" class="comment"><div id="post-30768-score" class="comment-score"></div><div class="comment-text"><p>I have set up two .net applications to talk to each other over ethernet, using the same two IP addresses as above and that works, the only difference I could see was the .net applications sent out an extra 18 bytes of 00 value after the data I was sending out. I added this to my DSP software and it works.... nowhere have I seen any reference to what these extra bytes would mean and I havent seen them on any other ARP request packets so i'm still as confused as ever.</p></div><div id="comment-30768-info" class="comment-info"><span class="comment-age">(13 Mar '14, 08:18)</span> <span class="comment-user userinfo">Sly_Raccoon</span></div></div><span id="30769"></span><div id="comment-30769" class="comment"><div id="post-30769-score" class="comment-score">1</div><div class="comment-text"><p><a href="http://wiki.wireshark.org/Ethernet#Allowed_Packet_Lengths">Minimum Ethernet frame length</a>. It's 64 bytes, and your DSP wasn't doing that.</p><p>In your sample the frame length was 42 bytes, which (usually in Wireshark) doesn't include the FCS, so your frame was 18 bytes short. When not in promiscuous mode your laptop dropped the "too-short" frame, but accepted it when promiscuous mode was on.</p><p>Adding the padding brought the frame up to the minimum length.</p></div><div id="comment-30769-info" class="comment-info"><span class="comment-age">(13 Mar '14, 09:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30770"></span><div id="comment-30770" class="comment"><div id="post-30770-score" class="comment-score"></div><div class="comment-text"><p>Aha, no I have written a lot of the software running on the DSP so as I wasn't aware of this minimum length, it wasn't included. the PC i'm connecting to sends out ARP requests which are the same I have above, without the padding bytes so I copied that.</p><p>Cheers grahamb, you've been a great help.</p></div><div id="comment-30770-info" class="comment-info"><span class="comment-age">(13 Mar '14, 09:25)</span> <span class="comment-user userinfo">Sly_Raccoon</span></div></div><span id="30771"></span><div id="comment-30771" class="comment"><div id="post-30771-score" class="comment-score"></div><div class="comment-text"><p><span>@Sly_Raccoon</span></p><p>Doing it the hard way by writing your own stack :-)</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-30771-info" class="comment-info"><span class="comment-age">(13 Mar '14, 09:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-30757" class="comment-tools"></div><div class="clear"></div><div id="comment-30757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30766"></span>

<div id="answer-container-30766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30766-score" class="post-score" title="current number of votes">0</div><span id="post-30766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Graham, your DSP device probably does not have the same subnet address as your computer. In order for Wireshark to see an ARP broadcast without having promiscuous mode turned on, the subnet addresses have to match.</p><p>The subnet address is the part of the address that is left after being masked by the subnet mask. For example if your computer address is 192.168.1.100, and your mask is 255.255.255.0, the subnet address is 192.168.1.0/32. If your DSM device were broadcasting to the 10.0.0.0/8 subnet, Wireshark (or any other capture software for that matter) would not be able to see it, because the NIC itself would filter it out rather than pass it up the stack. Promiscuous mode just removes that filter, so you see everything that reaches the NIC.</p><p>Gil</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/b831a43db812aa83ec03216feb92f233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gil%20Yoder&#39;s gravatar image" /><p><span>Gil Yoder</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gil Yoder has no accepted answers">0%</span></p></div></div><div id="comments-container-30766" class="comments-container"><span id="30767"></span><div id="comment-30767" class="comment"><div id="post-30767-score" class="comment-score"></div><div class="comment-text"><p>Why would IP subnets matter for the ARP request which is an Ethernet (MAC) address broadcast?</p></div><div id="comment-30767-info" class="comment-info"><span class="comment-age">(13 Mar '14, 07:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-30766" class="comment-tools"></div><div class="clear"></div><div id="comment-30766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

