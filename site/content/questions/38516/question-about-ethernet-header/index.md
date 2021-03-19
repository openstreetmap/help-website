+++
type = "question"
title = "question about ethernet header"
description = '''I was trying to make some small frame size packets (64b) and pass them through a switch to see how they react  I was able to do something like that using python and scapy so thats good but i just wanted to confirm that the frame length showing up in the packet see attached image is actually the ethe...'''
date = "2014-12-10T13:33:00Z"
lastmod = "2014-12-10T18:15:00Z"
weight = 38516
keywords = [ "python", "scapy", "framelength", "wireshark" ]
aliases = [ "/questions/38516" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [question about ethernet header](/questions/38516/question-about-ethernet-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38516-score" class="post-score" title="current number of votes">0</div><span id="post-38516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to make some small frame size packets (64b) and pass them through a switch to see how they react I was able to do something like that using python and scapy so thats good but i just wanted to confirm that the frame length showing up in the packet see attached image is actually the ethernet frame size it looks like it is.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ws.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-scapy" rel="tag" title="see questions tagged &#39;scapy&#39;">scapy</span> <span class="post-tag tag-link-framelength" rel="tag" title="see questions tagged &#39;framelength&#39;">framelength</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '14, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/dc616063228a211102c1dc44a1765294?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robm&#39;s gravatar image" /><p><span>robm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robm has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38516" class="comments-container"></div><div id="comment-tools-38516" class="comment-tools"></div><div class="clear"></div><div id="comment-38516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38518"></span>

<div id="answer-container-38518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38518-score" class="post-score" title="current number of votes">2</div><span id="post-38518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On an Ethernet network, the minimum frame size is 64 bytes, including the 14-byte header and the 4-byte CRC at the end of the packet.</p><p>Thus, the minimum size of the Ethernet <em>payload</em> is 46 bytes; 14+46+4 = 64.</p><p>If a program wants to transmit, on an Ethernet, a packet with fewer than 46 bytes of payload - for example, an TCP segment, transmitted over IPv4, with only an ACK, so there's no TCP payload, and with no TCP or IP options, so that the payload would be 20 bytes of IPv4 header and 20 bytes of TCP header, for a total of 40 bytes - padding would have to be added to the end of the payload, to make the frame a total of 64 bytes. For the ACK-only segment, it would have 14 bytes of Ethernet header, 20 bytes of IP header, 20 bytes of TCP header, 6 bytes of padding, and 4 bytes of CRC.</p><p>So if a packet is captured <em>from an actual Ethernet network</em>, it should have always be at least 60 bytes if the CRC is discarded by the adapter before handing the packet to the host, or by the networking stack before handing it to the capture application (so that it's not part of the captured packet; that's usually the case) and at least 64 bytes if the CRC is not discarded.</p><p><em>However</em>, if the packet is being transmitted by the host running the capture program, it will <strong><em>NOT</em></strong> be captured from an Ethernet network; Ethernet adapters do not receive the packets that they transmit. Instead, the OS kernel mechanisms that are used to do the capture will take a copy of the packet <em>before</em> it's handed to the adapter and hand that copy to the capture mechanism. The padding is almost always, if not always, added by the network adapter, not by the OS networking stack, so the packet that gets handed to the capture mechanism will <em>not</em> include the padding (or the CRC, for that matter, as that's also added by the network adapter).</p><p>Frame 2 in your capture is a TCP segment transmitted over IPv4. If it had only one byte of TCP data and no IP or TCP options, and it was being sent by the machine that was actually capturing the traffic, then it would show up in the capture as being a 55-byte packet, the 64-byte minimum size nonwithstanding.</p><p>ARP packets also typically have less than 46 bytes of ARP message - if frames 1 and 3 have 28-byte ARP messages, and were sent by the machine that was actually capturing the traffic, then they would show up in the capture as being 42-byte packets, the 64-bit minimum size again nonwithstanding.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '14, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38518" class="comments-container"></div><div id="comment-tools-38518" class="comment-tools"></div><div class="clear"></div><div id="comment-38518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

