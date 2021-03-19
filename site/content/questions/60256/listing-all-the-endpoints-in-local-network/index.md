+++
type = "question"
title = "Listing all the endpoints in local network"
description = '''I have a Packet Capture file of a network which can connect with the Internet. Now, I want to find the endpoints which communicate in the local network itself. I found that the &quot;Endpoints&quot; features can be used for this purpose but I am having a few doubts.  Do all the computers in the LAN communicat...'''
date = "2017-03-22T06:09:00Z"
lastmod = "2017-03-22T08:14:00Z"
weight = 60256
keywords = [ "endpoints", "statistics" ]
aliases = [ "/questions/60256" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Listing all the endpoints in local network](/questions/60256/listing-all-the-endpoints-in-local-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60256-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Packet Capture file of a network which can connect with the Internet. Now, I want to find the endpoints which communicate in the local network itself. I found that the "Endpoints" features can be used for this purpose but I am having a few doubts.</p><ul><li>Do all the computers in the LAN communicate over "Ethernet" protocol ?</li><li>Do all the endpoints which are listed in the protocols "IPv4", "IPv6", "TCP" and "UDP" are physically outside the LAN ?</li></ul></div><div id="question-tags" class="tags-container tags">endpoints statistics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '17, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/b05827cc3522f2e1742baa234fac2c47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kshitij10496&#39;s gravatar image" /><p>kshitij10496<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kshitij10496 has no accepted answers">0%</span></p></div></div><div id="comments-container-60256" class="comments-container"></div><div id="comment-tools-60256" class="comment-tools"></div><div class="clear"></div><div id="comment-60256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60262"></span>

<div id="answer-container-60262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60262-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Assuming the capture file is made on a host connected to Ethernet this is likely true, although routers in your network may use other network technologies to connect to other parts of the network.</li><li>No, they can be both inside or outside your LAN. <em>IP</em> stands for Internet protocol, or inter-network protocol, so works in and in between networks. The transport protocols TCP and UDP ride on top of the IP protocols, so also in and in between networks.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '17, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60262" class="comments-container"></div><div id="comment-tools-60262" class="comment-tools"></div><div class="clear"></div><div id="comment-60262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

