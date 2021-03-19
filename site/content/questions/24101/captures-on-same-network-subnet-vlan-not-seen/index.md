+++
type = "question"
title = "Captures on same network subnet (vlan) not seen"
description = '''My network has about 5 network subnets (vlans), all created on the Firewall and trunked on the core switch. Other switches are uplinked to the core switch. A ping from 10.2.100.19 to 10.2.100.16, when filtered on wireshark doesn&#x27;t capture this ICMP, while ping from 10.2.100.19 to 172.16.27.225 (anot...'''
date = "2013-08-27T09:11:00Z"
lastmod = "2013-08-27T09:36:00Z"
weight = 24101
keywords = [ "gbabe" ]
aliases = [ "/questions/24101" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Captures on same network subnet (vlan) not seen](/questions/24101/captures-on-same-network-subnet-vlan-not-seen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24101-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My network has about 5 network subnets (vlans), all created on the Firewall and trunked on the core switch. Other switches are uplinked to the core switch. A ping from 10.2.100.19 to 10.2.100.16, when filtered on wireshark doesn't capture this ICMP, while ping from 10.2.100.19 to 172.16.27.225 (another vlan) appeared on wireshark. This was tested with a couple of ips and it seemed activity between same subnet were not been captured. The SPAN created on the core switch is a vlan source session. Please assist here as it's imperative to capture this traffic. What could be wrong? IS this a known issue? COuld there be packet loss? Assist please.</p></div><div id="question-tags" class="tags-container tags">gbabe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/ffd98f3990fc56b0844a9256326bfbe2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikpo&#39;s gravatar image" /><p>ikpo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikpo has no accepted answers">0%</span></p></div></div><div id="comments-container-24101" class="comments-container"></div><div id="comment-tools-24101" class="comment-tools"></div><div class="clear"></div><div id="comment-24101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24102"></span>

<div id="answer-container-24102" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24102-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>When the traffic is within the same vlan and the systems are connected to the same access switch, the traffic will not pass the core (as it does not need to be routed by the FW and it does not need to be switched between access switches). Therefor, you will not see it in the span session. The span session with source vlan on the core switch will only mirror traffic that enters <strong>the core switch</strong> on that particular vlan, but this traffic never enters the core switch.</p><p>You will need to create a local span session on the access-switch or create a RSPAN session on the access switch and forward the traffic in the capture vlan over the trunk to the switch where your capture device is located.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24102" class="comments-container"><span id="24109"></span><div id="comment-24109" class="comment"><div id="post-24109-score" class="comment-score"></div><div class="comment-text"><p>It's a common misconception that spanning a VLAN will force all packets of that VLAN <strong>anywhere</strong> on the network to come over and exit the one switch through the SPAN port :-)</p></div><div id="comment-24109-info" class="comment-info"><span class="comment-age">(27 Aug '13, 10:34)</span> Jasper ♦♦</div></div></div><div id="comment-tools-24102" class="comment-tools"></div><div class="clear"></div><div id="comment-24102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

