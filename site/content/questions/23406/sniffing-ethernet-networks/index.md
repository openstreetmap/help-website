+++
type = "question"
title = "Sniffing Ethernet networks"
description = '''I was wondering is it possible to capture the packets of other computers on a cable network ? if so is it possible to do it by windows or like wifi windows can&#x27;t sniff packets from other computers and doesn&#x27;t support monitor mode ?'''
date = "2013-07-27T12:18:00Z"
lastmod = "2013-07-27T23:50:00Z"
weight = 23406
keywords = [ "ethernet", "sniff", "network" ]
aliases = [ "/questions/23406" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Sniffing Ethernet networks](/questions/23406/sniffing-ethernet-networks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering is it possible to capture the packets of other computers on a cable network ? if so is it possible to do it by windows or like wifi windows can't sniff packets from other computers and doesn't support monitor mode ?</p></div><div id="question-tags" class="tags-container tags">ethernet sniff network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '13, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/1206ef65764ee2e1944067f02209107d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Milad%20Rad&#39;s gravatar image" /><p>Milad Rad<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Milad Rad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '13, 23:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23406" class="comments-container"><span id="23407"></span><div id="comment-23407" class="comment"><div id="post-23407-score" class="comment-score">1</div><div class="comment-text"><p>By "cable network" do you mean "a network that uses a cable rather than a radio", such as an Ethernet network, or do you mean "a network provided by a cable television company", so that you'd be trying to sniff the traffic of other cable modem subscribers?</p></div><div id="comment-23407-info" class="comment-info"><span class="comment-age">(27 Jul '13, 13:19)</span> Guy Harris ♦♦</div></div><span id="23409"></span><div id="comment-23409" class="comment"><div id="post-23409-score" class="comment-score"></div><div class="comment-text"><p>I mean Ethernet like a lan network based on cables in an office</p></div><div id="comment-23409-info" class="comment-info"><span class="comment-age">(27 Jul '13, 22:22)</span> Milad Rad</div></div></div><div id="comment-tools-23406" class="comment-tools"></div><div class="clear"></div><div id="comment-23406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23410"></span>

<div id="answer-container-23410" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23410-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no such thing as "monitor mode" for Ethernet. There is, for Ethernet <em>and</em> Wi-Fi (and other technologies, such as Token Ring and FDDI), "promiscuous mode", which is supported by most Ethernet adapters <em>and</em> is supported by most Ethernet drivers and by most packet capture mechanisms, <em>including</em> WinPcap on Windows.</p><p><em>However</em>, it may not be sufficient to be in promiscuous mode if you're capturing on a switched network. This is discussed in detail on <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">the Ethernet capture page</a> on the Wireshark Wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '13, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23410" class="comments-container"></div><div id="comment-tools-23410" class="comment-tools"></div><div class="clear"></div><div id="comment-23410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

