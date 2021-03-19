+++
type = "question"
title = "Indistinguishable protocol versions"
description = '''How can a dissector deal with different versions of a protocol, when the versions can&#x27;t really be distinguished from the data stream? The version number isn&#x27;t available in the data stream or any associated control stream, and without the version number, it is often not possible to decode the data co...'''
date = "2013-07-14T23:30:00Z"
lastmod = "2013-07-14T23:54:00Z"
weight = 22965
keywords = [ "dissector", "indistinguishable", "versions" ]
aliases = [ "/questions/22965" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Indistinguishable protocol versions](/questions/22965/indistinguishable-protocol-versions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can a dissector deal with different versions of a protocol, when the versions can't really be distinguished from the data stream? The version number isn't available in the data stream or any associated control stream, and without the version number, it is often not possible to decode the data correctly.</p><p>One way is to try to decode a set of possible versions, and to see which ones look reasonable, but this is very circuitous and prone to mistakes. Is there a way for a dissector to ask the user for this information?</p><p>Thanks, Dirk De Schepper</p></div><div id="question-tags" class="tags-container tags">dissector indistinguishable versions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '13, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/d4b633ac6500f32bd32304516ec866d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deschepper&#39;s gravatar image" /><p>deschepper<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deschepper has no accepted answers">0%</span></p></div></div><div id="comments-container-22965" class="comments-container"></div><div id="comment-tools-22965" class="comment-tools"></div><div class="clear"></div><div id="comment-22965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22966"></span>

<div id="answer-container-22966" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22966-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If there is no field in the protocol to indicate the protocol version and dissection for the packet is dependent on the protocol version, then you either need to use heuristics on (part of) the packet to determine the version or (if heuristics have a big chance on failing) use a protocol preference.</p><p>A protocol preference gives the user the possibility to change the behavior of the protocol dissector by setting one or more preferences. Protocol version could be one of those preferences.</p><p>See also: <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.dissector?revision=50557">http://anonsvn.wireshark.org/viewvc/trunk/doc/README.dissector?revision=50557</a> paragraph 2.6</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22966" class="comments-container"><span id="23005"></span><div id="comment-23005" class="comment"><div id="post-23005-score" class="comment-score"></div><div class="comment-text"><p>Then you can't actually have different dissector settings for different communication sessions you're monitoring? I guess it's the fault of the protocol for not providing version information... Thanks for the answer.</p></div><div id="comment-23005-info" class="comment-info"><span class="comment-age">(16 Jul '13, 05:07)</span> deschepper</div></div><span id="23056"></span><div id="comment-23056" class="comment"><div id="post-23056-score" class="comment-score"></div><div class="comment-text"><p>Nope, that is the downside if information in the packets is not enough to determine the protocol version...</p><p>You could use the "Decode As..." functionality to accomplish this if you register both versions of the dissector to the upper layer protocol (which must provide some method of distinguishing each session).</p><p>Could you share a tracefile (on www.cloudshark.org) with both versions of the protocol in it so we can have a look if this is feasible?</p></div><div id="comment-23056-info" class="comment-info"><span class="comment-age">(16 Jul '13, 14:27)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-22966" class="comment-tools"></div><div class="clear"></div><div id="comment-22966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

