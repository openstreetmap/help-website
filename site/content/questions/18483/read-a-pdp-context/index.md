+++
type = "question"
title = "read a pdp context"
description = '''Hello, I have a question regarding a wireshark trace&#x27;s. I want to see the PDP CONTEXT in the trace but i don&#x27;t know how to do ? below how i make my test : The mobile is under FEMTOCELL coverage(the wireshark is configured with this femto. The Femt is an amplifier home network). i launch the trace i ...'''
date = "2013-02-11T01:43:00Z"
lastmod = "2013-02-12T04:34:00Z"
weight = 18483
keywords = [ "context", "pdp" ]
aliases = [ "/questions/18483" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [read a pdp context](/questions/18483/read-a-pdp-context)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a question regarding a wireshark trace's. I want to see the PDP CONTEXT in the trace but i don't know how to do ? below how i make my test :</p><p>The mobile is under FEMTOCELL coverage(the wireshark is configured with this femto. The Femt is an amplifier home network).</p><p>i launch the trace i activate the data on the mobile i launch a navigation</p><p>I want to see the PDP CONTEXT information. I don't know if i must have a plugin to try this or not ? (version 1.6.12)</p></div><div id="question-tags" class="tags-container tags">context pdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/ceecb02abd441108e8dec0b389d94c40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prima%20Test&#39;s gravatar image" /><p>Prima Test<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prima Test has no accepted answers">0%</span></p></div></div><div id="comments-container-18483" class="comments-container"><span id="18511"></span><div id="comment-18511" class="comment"><div id="post-18511-score" class="comment-score"></div><div class="comment-text"><p>It's not clear what you are trying to do. Do you have a femto cell connected via your home netork and you have mirroring set up in your home network to sniff trafik between this femto cell and the GSM/UMTS core network or a lab setup to do the same? What traffic can you see with Wireshark? Chances are that the traffic femtocell -&gt; network is encrypted.</p></div><div id="comment-18511-info" class="comment-info"><span class="comment-age">(11 Feb '13, 13:16)</span> Anders ♦</div></div><span id="18528"></span><div id="comment-18528" class="comment"><div id="post-18528-score" class="comment-score"></div><div class="comment-text"><p>yes it's exactly that i have a femto cell connected via my home network. And i want to see the communication between the mobile when i lauch a wap navigation and the network. My mobile is configured to dual stack (iPv4/iPv6) but for SFR in France only the ipv4 is supported. So i want see the PDP Context via wireshark to see that the network "says" correctly to the mobile that only ipv4 is supported. it's more clear or not ? but you're right, maybe with the femtocell the network is encrypted.</p></div><div id="comment-18528-info" class="comment-info"><span class="comment-age">(12 Feb '13, 00:35)</span> Prima Test</div></div></div><div id="comment-tools-18483" class="comment-tools"></div><div class="clear"></div><div id="comment-18483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18543"></span>

<div id="answer-container-18543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>(the wireshark is configured with this femto.</p></blockquote><p>What does that mean excatly?</p><p>Usually a Femtocell is a blackbox that has access to the 3G Network over the air <strong>and</strong> acccess to the Provider network via an IP network (your home internet access). Without special hardware, you cannot capture the 3G traffic (and it won't help you, as 3G traffic is encrypted). To be able to capture the IP traffic (from the Femtocell to the Provider network), you need a plain <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a> (TAP, Switch with Mirror Port, etc.).</p><p><strong>HOWEVER</strong> The traffic from the Femtocell to the Provider is (usually) <strong>encrypted</strong>, so all you will see is encrypted data in Wireshark. As you don't know how they encrypt the data and you don't have access to the crypto keys, you won't be able to decrypt that traffic. It's not a limitation of Wireshark, it's just 'security by design' (hopefully).</p><p>If your Femtocell works differently, there may be ways to get hold of the data, but chances are rather bad ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '13, 05:19</p></div></div><div id="comments-container-18543" class="comments-container"></div><div id="comment-tools-18543" class="comment-tools"></div><div class="clear"></div><div id="comment-18543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

