+++
type = "question"
title = "ARP request from DHCP server NOT broadcasted (ARP unicast)"
description = '''Hi everyone, I am capturing traces of my home network and I am seeing ARP requests from the router connected to the Internet to my PC every 20-30 seconds. As this router is configured to serve IP addresses (DHCP) I suppose this is normal traffic. What is buffling me is that the router is not broadca...'''
date = "2014-06-04T02:15:00Z"
lastmod = "2014-06-04T20:16:00Z"
weight = 33371
keywords = [ "arp", "non-broadcast" ]
aliases = [ "/questions/33371" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ARP request from DHCP server NOT broadcasted (ARP unicast)](/questions/33371/arp-request-from-dhcp-server-not-broadcasted-arp-unicast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am capturing traces of my home network and I am seeing ARP requests from the router connected to the Internet to my PC every 20-30 seconds. As this router is configured to serve IP addresses (DHCP) I suppose this is normal traffic.</p><p>What is buffling me is that the router is not broadcasting the ARP requests, but sending them to the MAC address of my PC. I have checked the source MAC address and IP address of the ARP request and they are really corresponds to the ones of the router router (does not seem to be any spoofing going on).</p><p>Here an instance of such a request:</p><p>5 143.028579000 00:24:fe:c1:xx:xx 50:46:5d:70:xx:xx ARP 60 Who has 192.168.2.114? Tell 192.168.2.1</p><p>Does anyone have any idea when an ARP request is allowed not to be broadcasted, but sent with a destination address?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">arp non-broadcast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/b4d42d58238c79a15ea2536c78fe4737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mabad&#39;s gravatar image" /><p>mabad<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mabad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '14, 04:18</p></div></div><div id="comments-container-33371" class="comments-container"><span id="33387"></span><div id="comment-33387" class="comment"><div id="post-33387-score" class="comment-score"></div><div class="comment-text"><p>I have also noticed that my PC is also sending ARP requests, but more scarcely, to the DCHP Server (a router) containing the MAC Address of the router within the Ethernet frame, like the requests from the router is doing. The router and the PC send in the ARP request 0:0:0:0:0:0 as the Destination MAC Address (which theoretically they are asking for, but curiously they might seem to know about it as they are sending the frame to the MAC Address of the device in question).</p></div><div id="comment-33387-info" class="comment-info"><span class="comment-age">(04 Jun '14, 08:14)</span> mabad</div></div></div><div id="comment-tools-33371" class="comment-tools"></div><div class="clear"></div><div id="comment-33371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33414"></span>

<div id="answer-container-33414" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33414-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is normal if they're just attempting to refresh their ARP cache. You should still see the "Target MAC" as all zeros but if the MAC was known already it would just be costly network-wise to broadcast for a refresh.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 20:16</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-33414" class="comments-container"><span id="33421"></span><div id="comment-33421" class="comment"><div id="post-33421-score" class="comment-score"></div><div class="comment-text"><p>Thanks. All I had read about ARP is that requests are always broadcasted. Just wanted to confirm that there are exceptions that confirm the rule.</p></div><div id="comment-33421-info" class="comment-info"><span class="comment-age">(05 Jun '14, 01:50)</span> mabad</div></div><span id="33422"></span><div id="comment-33422" class="comment"><div id="post-33422-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-33422-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:02)</span> grahamb ♦</div></div><span id="33435"></span><div id="comment-33435" class="comment"><div id="post-33435-score" class="comment-score"></div><div class="comment-text"><p>I have checked the RFC 1122. The implementation part of the ARP protocol is stated: (2) Unicast Poll -- Actively poll the remote host by periodically sending a point-to-point ARP Request to it, and delete the entry if no ARP Reply is received from N successive polls.</p></div><div id="comment-33435-info" class="comment-info"><span class="comment-age">(05 Jun '14, 04:15)</span> mabad</div></div></div><div id="comment-tools-33414" class="comment-tools"></div><div class="clear"></div><div id="comment-33414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

