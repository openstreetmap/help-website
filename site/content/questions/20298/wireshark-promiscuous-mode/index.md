+++
type = "question"
title = "wireshark promiscuous mode"
description = '''I am still seeing packets when i set this capture filter !ether host ab:cd:ef:gh:ij:kl (packets not destined to my mac) and promiscuous mode disabled on the interface. The protocols captured were IGMPV2 and SSDP. Would like to know the reason.Thanks'''
date = "2013-04-10T20:28:00Z"
lastmod = "2013-04-10T21:29:00Z"
weight = 20298
keywords = [ "promiscuous-mode" ]
aliases = [ "/questions/20298" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark promiscuous mode](/questions/20298/wireshark-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20298-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am still seeing packets when i set this capture filter</p><p>!ether host ab:cd:ef:gh:ij:kl (packets not destined to my mac) and promiscuous mode disabled on the interface.</p><p>The protocols captured were IGMPV2 and SSDP. Would like to know the reason.Thanks</p></div><div id="question-tags" class="tags-container tags">promiscuous-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '13, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-20298" class="comments-container"></div><div id="comment-tools-20298" class="comment-tools"></div><div class="clear"></div><div id="comment-20298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20299"></span>

<div id="answer-container-20299" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20299-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are seeing this traffic because it's multicast traffic. IP multicast traffic has its own destination MAC addresses, generally beginning with 01:00:5E, and they different from your NIC's MAC address. However, your NIC listens to the multicast MAC addresses, at least for any multicast group that the computer has joined.</p><p>When your NIC is not in promiscuous mode, it listens to:</p><ul><li>It's own MAC address</li><li>The ethernet broadcast address (ff:ff:ff:ff:ff:ff)</li><li>Multicast MAC addresses</li></ul><p>Your capture is only filtering out the first one of these.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-20299" class="comments-container"><span id="20301"></span><div id="comment-20301" class="comment"><div id="post-20301-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim.If possible can you list out the packet types when the nic is in promiscuous mode.</p></div><div id="comment-20301-info" class="comment-info"><span class="comment-age">(10 Apr '13, 21:41)</span> krishnayeddula</div></div><span id="20339"></span><div id="comment-20339" class="comment"><div id="post-20339-score" class="comment-score"></div><div class="comment-text"><p>When a NIC is in promiscuous mode, it passes all traffic that it sees up to the OS.</p></div><div id="comment-20339-info" class="comment-info"><span class="comment-age">(11 Apr '13, 08:36)</span> Jim Aragon</div></div><span id="20361"></span><div id="comment-20361" class="comment"><div id="post-20361-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When a NIC is in promiscuous mode, it passes all traffic that it sees up to the OS.</p></blockquote><p>...regardless of the destination MAC address. It won't, obviously, pass up traffic it <em>doesn't</em> see, so, for example, it's not, by default, as useful as you'd like on a <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">switched network</a>.</p></div><div id="comment-20361-info" class="comment-info"><span class="comment-age">(11 Apr '13, 18:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-20299" class="comment-tools"></div><div class="clear"></div><div id="comment-20299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

