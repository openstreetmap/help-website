+++
type = "question"
title = "Show the ARP data and the DHCP data and show which data is from the client and which from the server?"
description = '''I did a capture and am asked to show the ARP data and he DHCP data and then show which one is from the client and which one is from the server. How do I do this?'''
date = "2014-11-09T08:21:00Z"
lastmod = "2014-11-09T14:45:00Z"
weight = 37712
keywords = [ "arp", "dhcp", "server", "data", "wireshark" ]
aliases = [ "/questions/37712" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show the ARP data and the DHCP data and show which data is from the client and which from the server?](/questions/37712/show-the-arp-data-and-the-dhcp-data-and-show-which-data-is-from-the-client-and-which-from-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37712-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did a capture and am asked to show the ARP data and he DHCP data and then show which one is from the client and which one is from the server.</p><p>How do I do this?</p></div><div id="question-tags" class="tags-container tags">arp dhcp server data wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/14dfc6b2197d20040b7e35229fb5dc16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MacTavish_10&#39;s gravatar image" /><p>MacTavish_10<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MacTavish_10 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '14, 08:22</p></div></div><div id="comments-container-37712" class="comments-container"></div><div id="comment-tools-37712" class="comment-tools"></div><div class="clear"></div><div id="comment-37712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37716"></span>

<div id="answer-container-37716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37716-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should familiarize yourself with how ARP and DHCP works. In both cases the client is the one asking for something: ARP usually asks for a MAC address for a known IP address, while DHCP asks for an IP address to be assigned to an interface.</p><p>So if you see an ARP packet with "Who has... Tell..." it's the client. If you see a DHCP "Discover" it's the client, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '14, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37716" class="comments-container"></div><div id="comment-tools-37716" class="comment-tools"></div><div class="clear"></div><div id="comment-37716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

