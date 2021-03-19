+++
type = "question"
title = "Should an arp ever be for a IP on another network"
description = '''From what I understand if things are configured correctly I shouldn&#x27;t see an ARP to a Target IP on a different subnet. Since it should know the MAC address it should use is the default GW. Something may be misconfigured, but I&#x27;m not seeing it yet. I&#x27;ll attach the network trace. But my question is wh...'''
date = "2015-07-31T14:23:00Z"
lastmod = "2015-07-31T16:44:00Z"
weight = 44709
keywords = [ "arp", "subnet" ]
aliases = [ "/questions/44709" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Should an arp ever be for a IP on another network](/questions/44709/should-an-arp-ever-be-for-a-ip-on-another-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From what I understand if things are configured correctly I shouldn't see an ARP to a Target IP on a different subnet.</p><p>Since it should know the MAC address it should use is the default GW.</p><p>Something may be misconfigured, but I'm not seeing it yet.</p><p>I'll attach the network trace.</p><p>But my question is whether I should be seeing an ARP for an IP on another subnet?</p></div><div id="question-tags" class="tags-container tags">arp subnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '15, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-44709" class="comments-container"><span id="44710"></span><div id="comment-44710" class="comment"><div id="post-44710-score" class="comment-score"></div><div class="comment-text"><p>I uploaded trace.</p><p>See frame 27.</p><p><a href="https://www.cloudshark.org/captures/d8c1f95f6e29">https://www.cloudshark.org/captures/d8c1f95f6e29</a></p></div><div id="comment-44710-info" class="comment-info"><span class="comment-age">(31 Jul '15, 14:30)</span> gipper</div></div></div><div id="comment-tools-44709" class="comment-tools"></div><div class="clear"></div><div id="comment-44709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44714"></span>

<div id="answer-container-44714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44714-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The most probably reason for such behaviour is a misconfigured Subnetmask at the sender. In this case: 52.97.224.112.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '15, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-44714" class="comments-container"><span id="44725"></span><div id="comment-44725" class="comment"><div id="post-44725-score" class="comment-score"></div><div class="comment-text"><p>agree, subnet mask is wrong on the node sending the ARP. It thinks it can reach the destination directly without the default gateway. Easily fixed by correcting the subnet mask setting of that node.</p></div><div id="comment-44725-info" class="comment-info"><span class="comment-age">(01 Aug '15, 10:05)</span> Jasper ♦♦</div></div></div><div id="comment-tools-44714" class="comment-tools"></div><div class="clear"></div><div id="comment-44714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

