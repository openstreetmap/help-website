+++
type = "question"
title = "Would an old mini-hub work as a TAP?"
description = '''Happy to join the frenzy. I&#x27;ve got 7 switches on my one-segment LAN here, and I&#x27;d like to capture some trace files at the gateway. I don&#x27;t have a TAP, and was wondering if an old-school hub might work, as hubs don&#x27;t forward at the MAC level. It&#x27;s a 4-port mini-hub, and I was going to plug my laptop ...'''
date = "2014-02-26T08:29:00Z"
lastmod = "2014-02-26T15:50:00Z"
weight = 30208
keywords = [ "hub" ]
aliases = [ "/questions/30208" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Would an old mini-hub work as a TAP?](/questions/30208/would-an-old-mini-hub-work-as-a-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30208-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Happy to join the frenzy. I've got 7 switches on my one-segment LAN here, and I'd like to capture some trace files at the gateway. I don't have a TAP, and was wondering if an old-school hub might work, as hubs don't forward at the MAC level. It's a 4-port mini-hub, and I was going to plug my laptop and my daisy-chained switches into it with Wireshark running on my laptop. Yay or nay? Thanks.</p></div><div id="question-tags" class="tags-container tags">hub</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '14, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/fb088ac2aead612a2d6a82572cf8be51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shartnado&#39;s gravatar image" /><p>Shartnado<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shartnado has no accepted answers">0%</span></p></div></div><div id="comments-container-30208" class="comments-container"></div><div id="comment-tools-30208" class="comment-tools"></div><div class="clear"></div><div id="comment-30208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30219"></span>

<div id="answer-container-30219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30219-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming your "hub" is an old-fashioned ethernet repeater, then yes. We use netgear hubs all the time for that at my work. (Netgear doesn't make them anymore - but you can find them on Ebay)</p><p>The term "hub" stopped being synonymous with repeaters a long time ago though. For example a bunch of companies made ethernet "hubs" with one or two fast-ethernet ports, and to accomplish that you have to bridge (ie, switch) between those two domains; but some of them at least repeated within the domain, so that all ethernet 10mbps (10Base-T) ports were repeater ports, while it bridged to/from the 100mbps fast ethernet (100Base-TX) port.</p><p>But it's not hard to find out - just insert the hub in-between two of your switches, connect your PC running wireshark to the hub, send some packets across the two switches (like ICMP ping), and see if wireshark sees the packets (other than the ARP packets, which it will see regardless since they're broadcast).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '14, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30219" class="comments-container"></div><div id="comment-tools-30219" class="comment-tools"></div><div class="clear"></div><div id="comment-30219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

