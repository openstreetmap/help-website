+++
type = "question"
title = "Diameter message priority indicators?"
description = '''Hello, I read somewhere that a Diameter Signalling Controller or a Diameter Routing Agent can be configured to prioritize VoLTE related signaling, over all the various Diameter interfaces. When serving this function, operators can provide a higher quality VoLTE service over other services, particula...'''
date = "2014-11-26T15:42:00Z"
lastmod = "2014-11-26T22:37:00Z"
weight = 38189
keywords = [ "priority", "diameter", "message", "volte" ]
aliases = [ "/questions/38189" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter message priority indicators?](/questions/38189/diameter-message-priority-indicators)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I read somewhere that a Diameter Signalling Controller or a Diameter Routing Agent can be configured to prioritize VoLTE related signaling, over all the various Diameter interfaces. When serving this function, operators can provide a higher quality VoLTE service over other services, particularly when other services load the network.</p><p>Is there a way to detect such priority indicators from Wireshark traces?</p><p>Which field should I be looking at and any recommended display filters I could use to see if my Operator has activated such a functionality?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">priority diameter message volte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/c8d00a5dcc1060c9f64abd93d2fd81e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fnm500&#39;s gravatar image" /><p>fnm500<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fnm500 has no accepted answers">0%</span></p></div></div><div id="comments-container-38189" class="comments-container"></div><div id="comment-tools-38189" class="comment-tools"></div><div class="clear"></div><div id="comment-38189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38197"></span>

<div id="answer-container-38197" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38197-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general no, unless part of that prioritization is to mark IP header QoS (in the ToS/DSCP field).</p><p>Typically if an agent supports prioritization it will apply that priority locally on messages it receives, rather than mark priority for packets on the wire. Signalling load issues are going to present themselves in TPS bottlenecks long before bandwidth or network congestion becomes a factor.</p><p>In concept messages could be prioritized based on any criteria visible to the agent but some would be command code (type of message) the Application ID (in VoLTE context, the type of interface roughly) and the type of message of that code (eg:prioritize updates of existing sessions over initial messages for a new session). Locally-processed Diameter messages like watchdogs should also (in my opinion) be prioritized.</p><p>One other comment - depending on the topology you can (and in my opinion, should) isolate your diameter signalling types rather than looking at application prioritization in a common aggregation agent. Keeping VoLTE-related signalling in its own Diameter realm with its own agents is a good way to limit what other Diameter applications can do to your voice service on this front, and there's no technical requirement to have something like credit control in a common realm with EPC/IMS Diameter applications.</p><p>I'm also curious about the recent amount of VoLTE questions on some of these boards - were you by chance at the North America LTE convention last week?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '14, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '14, 22:54</p></div></div><div id="comments-container-38197" class="comments-container"><span id="38258"></span><div id="comment-38258" class="comment"><div id="post-38258-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Quadratic! Really appreciate your detailed reply and recommendations.</p><p>I agree with your thinking. There should be a separate realm for VoLTE related signalling.</p><p>I think the increase in VoLTE questions might have something to do with Verizon and others recently launching their VoLTE service and network engineers trying to understand if everything is working OK.</p><p>Thanks for the tip, I will look at some of the other questions people have been asking. Any particularly good threads you have come across? I wasn't at the LTE convention last week..</p><p>Thanks again.</p></div><div id="comment-38258-info" class="comment-info"><span class="comment-age">(01 Dec '14, 07:10)</span> fnm500</div></div><span id="38262"></span><div id="comment-38262" class="comment"><div id="post-38262-score" class="comment-score"></div><div class="comment-text"><p>Oh, aside from just Verizon I would say that 2015 is going to be the year of commercial VoLTE deployments. I just asked about the convention because I thought it was odd I saw similar questions within such a short time period right afterwards.</p><p>At this point, I don't think there have been enough large-scale Diameter signaling deployments in a VoLTE context to have a really solid view of what will become best-practices for it, though my main concern standards-wise right now is that HSS frontends will become bottlenecks once those Sh interfaces start moving at full steam combined with added roaming-related mobility exchanges in EPS. Similar to the move toward SIP, with Sh we're trading efficient ASN.1 encoding for flat XML files while taking a database frontend with traditionally light S6a load and exploding it. This is a concern to me for us all.</p><p>Having said that, I'm grateful that this technology shift is moving us closer than ever to the IT industry, and toward converged networking in telecom. Telecom vendors moving away from proprietary hardware and embracing not only virtualization/x86 but cloud and even SDN is a huge step forward in my view, as it is really starting to feel like mobile is catching up. I came originally from the IP world, where many of the things that mobile looks at as a bright but distant future in these areas are already a reality, so from my view we're coming back home. :)</p></div><div id="comment-38262-info" class="comment-info"><span class="comment-age">(01 Dec '14, 15:47)</span> Quadratic</div></div></div><div id="comment-tools-38197" class="comment-tools"></div><div class="clear"></div><div id="comment-38197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

