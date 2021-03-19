+++
type = "question"
title = "Realtec PCIe GBE Family Controller dropping wired connection"
description = '''On my recently built Windows 7 PC ASUS F2 A85-M Pro motherboard the Realtek PCIe GBE Family Controller keeps dropping a wired connection. Driver version 7.61.612.2012. Has anyone experienced this or know if there is something in the advanced settings that could be miss configured? I do not normally ...'''
date = "2013-08-28T09:25:00Z"
lastmod = "2013-08-28T11:04:00Z"
weight = 24144
keywords = [ "pcie", "controller", "realtek", "family", "gbe" ]
aliases = [ "/questions/24144" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Realtec PCIe GBE Family Controller dropping wired connection](/questions/24144/realtec-pcie-gbe-family-controller-dropping-wired-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24144-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my recently built Windows 7 PC ASUS F2 A85-M Pro motherboard the Realtek PCIe GBE Family Controller keeps dropping a wired connection. Driver version 7.61.612.2012. Has anyone experienced this or know if there is something in the advanced settings that could be miss configured? I do not normally ever power it down but when the connection is lost it requires a restart to reconnect.</p></div><div id="question-tags" class="tags-container tags">pcie controller realtek family gbe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '13, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/86dee9df11ae23ec5478a06da4aa3c58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaryCN&#39;s gravatar image" /><p>GaryCN<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaryCN has no accepted answers">0%</span></p></div></div><div id="comments-container-24144" class="comments-container"><span id="24158"></span><div id="comment-24158" class="comment"><div id="post-24158-score" class="comment-score"></div><div class="comment-text"><p>"Dropping a connection" as in "losing carrier", or as in "has carrier but never receives any packets" or "has carrier but nobody sees its transmitted packets"? (Ethernet is a connectionless medium, so there isn't much else that would be considered a "connection".)</p></div><div id="comment-24158-info" class="comment-info"><span class="comment-age">(28 Aug '13, 23:55)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24144" class="comment-tools"></div><div class="clear"></div><div id="comment-24144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24150"></span>

<div id="answer-container-24150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24150-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This Q&amp;A site is about Wireshark and network analysis with Wireshark.</p><p>Your problem sounds like a hardware problem. I think you will get better answers (or answers at all) in a Asus or Realtek forum.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24150" class="comments-container"><span id="24156"></span><div id="comment-24156" class="comment"><div id="post-24156-score" class="comment-score"></div><div class="comment-text"><p>I had considered that and may just add a PCI Express Ethernet Network Adapter.</p></div><div id="comment-24156-info" class="comment-info"><span class="comment-age">(28 Aug '13, 20:22)</span> GaryCN</div></div><span id="24160"></span><div id="comment-24160" class="comment"><div id="post-24160-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I had considered that and may just add a PCI Express Ethernet Network Adapter.</p></blockquote><p>That would be one option.</p><blockquote><p>I do not normally ever power it down but when the connection is lost it <strong>requires a restart to reconnect</strong>.</p></blockquote><p>What do you mean by that? By *<em>reconnect</em> do you mean a link to the network (link LED) or an IP address (via DHCP)?</p></div><div id="comment-24160-info" class="comment-info"><span class="comment-age">(29 Aug '13, 04:00)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24150" class="comment-tools"></div><div class="clear"></div><div id="comment-24150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

