+++
type = "question"
title = "mac flooding attack, unicast and sniffer"
description = '''hi all, If I&#x27;m not mistaken, in a switched environment a host will see all unicast (directly addressed to it) , broadcast (within same VLAN) and multicast (when belonging to the multicast group) frames. Now let&#x27;s consider that I run a MAC flooding attack on the switch in question. It fills up the wh...'''
date = "2016-01-06T05:00:00Z"
lastmod = "2016-01-06T14:49:00Z"
weight = 48903
keywords = [ "mac", "flooding", "sniffer" ]
aliases = [ "/questions/48903" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mac flooding attack, unicast and sniffer](/questions/48903/mac-flooding-attack-unicast-and-sniffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48903-score" class="post-score" title="current number of votes">0</div><span id="post-48903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>If I'm not mistaken, in a switched environment a host will see all unicast (directly addressed to it) , broadcast (within same VLAN) and multicast (when belonging to the multicast group) frames.</p><p>Now let's consider that I run a MAC flooding attack on the switch in question. It fills up the whole MAC table ( 8.000, 16.000 entries, whatever).Now, Host A wants to connect to B (both on same switch, same VLAN). Host A has in his arp table the MAC address of host B. Host A sends the packet, it arrives on the switch (it will not learn the port Host A is on, because the CAM table is full) but it will not find Host B's MAC address as well (I know, that it can be present, but let's assume that it's not). So because Host A knew the MAC address of Host B I'm more than sure that Host A sends out an unicast frame. So the switch inspects it's CAM table looking for Host B's MAC and "says" i don't know where host B is at, so let me send the frame / packet to all ports. Even though it will send it to all ports it's still a unicast. My question now is (if all the above is correct), when I'm running Wireshark on host C (connected to same switch, same VLAN) will I be able to see the packet ? Or do I have to enable promiscuous mode inside Wireshark ?</p><p>thank you in advance!</p><p>BR</p><p>Adam<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-flooding" rel="tag" title="see questions tagged &#39;flooding&#39;">flooding</span> <span class="post-tag tag-link-sniffer" rel="tag" title="see questions tagged &#39;sniffer&#39;">sniffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '16, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '16, 05:02</strong> </span></p></div></div><div id="comments-container-48903" class="comments-container"></div><div id="comment-tools-48903" class="comment-tools"></div><div class="clear"></div><div id="comment-48903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48906"></span>

<div id="answer-container-48906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48906-score" class="post-score" title="current number of votes">2</div><span id="post-48906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Host C will receive the packet, but because the packet's destination MAC will differ from Host C's one, Host C's NIC will drop the packet before handing it over to software (kernel and, important for you, Wireshark) <em>unless</em> it is switched over to promiscuous mode. One of available ways how to switch a NIC to promiscuous mode is to do so using Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '16, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '16, 05:57</strong> </span></p></div></div><div id="comments-container-48906" class="comments-container"><span id="48923"></span><div id="comment-48923" class="comment"><div id="post-48923-score" class="comment-score"></div><div class="comment-text"><p>What about broadcast ? Say, Host B's MAC is not in Host A's arp table, so it will start with arp request. Will all devices in the same VLAN see it(for example Host C) or will i have to enable promisc mode?</p></div><div id="comment-48923-info" class="comment-info"><span class="comment-age">(06 Jan '16, 12:15)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="48924"></span><div id="comment-48924" class="comment"><div id="post-48924-score" class="comment-score"></div><div class="comment-text"><p>From the point of view of the NIC, a packet with broadcast dst MAC must be handed over to the software, so promiscuous mode is not necessary to let broadcast packets be captured.</p><p>Anticipating your next question, filtering of multicast packets is normally a job of the switch. The client uses IGMP to inform the switch in which multicast streams it is interested, and the switch does not send to it any others, so the NIC does not need to discriminate. On the other hand, not every switch supports IGMP controlled multicast filtering.</p><p>So I'd think that the NIC handles multicast packets the same way like broadcast ones, but I am not 100% sure here.</p></div><div id="comment-48924-info" class="comment-info"><span class="comment-age">(06 Jan '16, 13:13)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48930"></span><div id="comment-48930" class="comment"><div id="post-48930-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So I'd think that the NIC handles multicast packets the same way like &gt; broadcast ones, but I am not 100% sure here.</p></blockquote><p>Actually: NICs do filter IP multicast packets.</p><p>Specifically, when a client joins an IP multicast group, the IP address is mapped to an 'ethernet multicast group address' (I think that's the right terminology) and the NIC is configured to accept packets address to that ethernet address. (The mapping is not 1 to 1: A group if IP multicast addresses is mapped to an ethernet address).</p><p>Therefore, Host C will need to set promiscuous mode to see all the IP multicast packets (assuming that host C has not already joined an IP multicast which maps to the ethernet address for the IP multicast address which is to be monitored).</p><p>A web search finds lots of info:</p><p>E.g.,</p><p><a href="http://www.dqnetworks.ie/toolsinfo.d/multicastaddressing.html">http://www.dqnetworks.ie/toolsinfo.d/multicastaddressing.html</a></p></div><div id="comment-48930-info" class="comment-info"><span class="comment-age">(06 Jan '16, 14:49)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-48906" class="comment-tools"></div><div class="clear"></div><div id="comment-48906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

