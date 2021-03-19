+++
type = "question"
title = "Identification of rogue IPv6 DNS server"
description = '''On our network, client workstations utilize DHCP for obtaining DNS server settings. I need to figure out why a certain IPv6 host is being added into the list of DNS servers. In other words, I need a way to capture IPV6 based DHCP traffic. Any assistance is greatly appreciated. Thanks xxx '''
date = "2016-01-26T19:54:00Z"
lastmod = "2016-01-27T03:14:00Z"
weight = 49526
keywords = [ "dhcp", "rogue", "ipv6" ]
aliases = [ "/questions/49526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Identification of rogue IPv6 DNS server](/questions/49526/identification-of-rogue-ipv6-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49526-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On our network, client workstations utilize DHCP for obtaining DNS server settings. I need to figure out why a certain IPv6 host is being added into the list of DNS servers. In other words, I need a way to capture IPV6 based DHCP traffic. Any assistance is greatly appreciated.</p><p>Thanks xxx<br />
</p></div><div id="question-tags" class="tags-container tags">dhcp rogue ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '16, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/98b27879fad9befa91f89ea28b6c453c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micahblair&#39;s gravatar image" /><p>micahblair<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micahblair has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '16, 03:11</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49526" class="comments-container"></div><div id="comment-tools-49526" class="comment-tools"></div><div class="clear"></div><div id="comment-49526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49535"></span>

<div id="answer-container-49535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49535-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure I get right what means "IPv6 host is being added into the list of DNS servers". But if it simply means that for a single DHCP discovery you get several DHCP offers, I would assume you need to work around the fact that the dynamically configured host interface only sends DHCP discovery for a certain period of time after L1 comes up, and that you cannot capture on an interface which is not up at L1. Here a hub or a switch with monitoring capability would help - you would connect the cable from one of your dynamically configured hosts to the uplink port of the switch or hub, connect a capturing machine to the monitoring port (if it is a switch with monitoring capability) or to any port if it is a hub and start capturing in promiscuous mode, and as the last step, connect the dynamically configured host to the access port of the hub/switch. This way, the capturing interface would already be up and running while the dynamically configured host would be negotiating at L1 and sending the DHCP discover.</p><p>The next step would be to apply <em>display</em> filter <code>dhcpv6</code> to see only the interesting packets, and look at the contents as well as the source MAC and IP addresses of all the DHCP offers which would come in response to the DHCP discover.</p><p>Now you can find two possibilities:</p><ul><li><p>there is actually a rogue <em>DHCP</em> server in the network, which answers faster than the legal one and augments the list of DNS servers with its "favourite" one - in such case, see the "last step" below.</p></li><li><p>it is your standard DHCP server which provides that rogue DNS server, so you'd have to check its configuration.</p></li></ul><p>The last step would be to use this address information to identify the "illegal" dhcp server. If you are lucky, your manageable switches will show you at which port of which switch this MAC address lives, so you can track it from switch to switch until you get to the one to which it is connected. If you are less lucky, the machine sends also other traffic, so capturing close to your gateway towards internet and analysing the traffic may give you a hint which one it is. The last "passive" resort is the inventory list with MAC addresses.</p><p>If no passive method helps, the next one is to ban that IP from access to internet/company server, the affected user will call IT helpdesk in no time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '16, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '16, 05:05</p></div></div><div id="comments-container-49535" class="comments-container"></div><div id="comment-tools-49535" class="comment-tools"></div><div class="clear"></div><div id="comment-49535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

