+++
type = "question"
title = "MAC address question"
description = '''hi guys, I&#x27;m looking at a UDP conversation and i do not understand the following. The conversation is between IP 128.x.x.x and 166.x.x.x. In the first packet I see the src ip 128.x.x.x and the src mac (let&#x27;s say Vmware_00-_00_00) dst ip = 166.x.x.x dst mac (IETF-VRRP-VRID_01). no when I look on the ...'''
date = "2015-09-25T02:28:00Z"
lastmod = "2015-09-25T04:37:00Z"
weight = 46143
keywords = [ "mac-address" ]
aliases = [ "/questions/46143" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [MAC address question](/questions/46143/mac-address-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>I'm looking at a UDP conversation and i do not understand the following. The conversation is between IP 128.x.x.x and 166.x.x.x. In the first packet I see the src ip 128.x.x.x and the src mac (let's say Vmware_00-_00_00) dst ip = 166.x.x.x dst mac (IETF-VRRP-VRID_01). no when I look on the packet sent from 166.x.x.x to 128.x.x.x the source MAC is different than IETF-VRRP-VRID_01 but the destination MAC address is the same used as the source in the first packet.</p><p>can someone please help me with this ?</p><p>thank you and best regards</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '15, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '15, 14:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46143" class="comments-container"><span id="46154"></span><div id="comment-46154" class="comment"><div id="post-46154-score" class="comment-score"></div><div class="comment-text"><p>That was my assumption as well. BUT what I don't understand, is why in the packet sent back (2nd packet) the dst mac is set to the MAC address of the 128.x.x.x host. I mean if both are behind a router shouldn't the dst mac address in the second packet by the MAC of the router ?</p></div><div id="comment-46154-info" class="comment-info"><span class="comment-age">(25 Sep '15, 04:21)</span> adasko</div></div></div><div id="comment-tools-46143" class="comment-tools"></div><div class="clear"></div><div id="comment-46143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46155"></span>

<div id="answer-container-46155" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46155-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The unexpected mac could be the physical address of the router.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '15, 04:39</p></div></div><div id="comments-container-46155" class="comments-container"><span id="46156"></span><div id="comment-46156" class="comment"><div id="post-46156-score" class="comment-score"></div><div class="comment-text"><p>So when I start the conversation from A - B and I receive the response from B - A the MAC destination address in the packet from B - A is the MAC address of the source (A) device so this cannot be the physical address of the router. <img src="https://osqa-ask.wireshark.org/upfiles/1_LmkbSRf.JPG" alt="alt text" /></p><p>second packet <img src="https://osqa-ask.wireshark.org/upfiles/2.JPG" alt="alt text" /></p><p>you see now what i mean? So the src mac from first frame = dst mac in the second frame , but if there is a router in between, the dst mac in the 2nd packet should be set the routers interface</p></div><div id="comment-46156-info" class="comment-info"><span class="comment-age">(25 Sep '15, 04:54)</span> adasko</div></div><span id="46159"></span><div id="comment-46159" class="comment"><div id="post-46159-score" class="comment-score">1</div><div class="comment-text"><p>So, from my point of view it looks like expected. So the question may be, where has been the capture Point.</p></div><div id="comment-46159-info" class="comment-info"><span class="comment-age">(25 Sep '15, 05:22)</span> Christian_R</div></div><span id="46160"></span><div id="comment-46160" class="comment not_top_scorer"><div id="post-46160-score" class="comment-score"></div><div class="comment-text"><p>But if there is a router between (both look to me, to be not on same sub network). So how can the second packet have the dst mac set to the mac of host A if it's not in hosts B network ?</p></div><div id="comment-46160-info" class="comment-info"><span class="comment-age">(25 Sep '15, 05:28)</span> adasko</div></div><span id="46166"></span><div id="comment-46166" class="comment"><div id="post-46166-score" class="comment-score">1</div><div class="comment-text"><p>Because you are tracing in the subnet of the VMware host.</p></div><div id="comment-46166-info" class="comment-info"><span class="comment-age">(25 Sep '15, 06:42)</span> Christian_R</div></div><span id="46168"></span><div id="comment-46168" class="comment"><div id="post-46168-score" class="comment-score">1</div><div class="comment-text"><p>It starts with a packet MAC(A) to MAC(V), where MAC(V) is actually a virtual router address. It does get forwarded to the server by one of the actual routers in your net.</p><p>When the response packet comes back from the server this packet then gets forwarded via a router i your net and this router uses it's own MAC(R), not the virtual router MAC(V), as source MAC.</p></div><div id="comment-46168-info" class="comment-info"><span class="comment-age">(25 Sep '15, 07:01)</span> Jaap ♦</div></div><span id="46170"></span><div id="comment-46170" class="comment not_top_scorer"><div id="post-46170-score" class="comment-score"></div><div class="comment-text"><p>Jaap, i think i know what i was doing wrong. I took the capture at Server A that is initiating the conversation. When looking at the second packet in the conversation I was (for any reasons) looking and the frames from perspective of the Server B, but as I'm capturing on device A I will see the frame addressing from router to Server A. Am I now correct ?</p></div><div id="comment-46170-info" class="comment-info"><span class="comment-age">(25 Sep '15, 07:28)</span> adasko</div></div><span id="46171"></span><div id="comment-46171" class="comment"><div id="post-46171-score" class="comment-score">1</div><div class="comment-text"><p>Yes now you are correct. That is what I have meant with the point of capturing.</p></div><div id="comment-46171-info" class="comment-info"><span class="comment-age">(25 Sep '15, 07:31)</span> Christian_R</div></div></div><div id="comment-tools-46155" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-46155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46150"></span>

<div id="answer-container-46150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46150-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the MAC address you listed it seems that you're talking to a server via a router using <a href="https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol">Virtual Router Redundancy Protocol</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></img></div></div><div id="comments-container-46150" class="comments-container"></div><div id="comment-tools-46150" class="comment-tools"></div><div class="clear"></div><div id="comment-46150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

