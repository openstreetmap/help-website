+++
type = "question"
title = "Multiple MAC Addresses - Port Security - DCHP"
description = '''I have a situation and will give as much data as I can to paint this picture. First this only happens to machines that are newly connected to the network. Second I have noticed there are some devices on the network that are static assigned, but are within the DHCP Pool with no reservations. Third we...'''
date = "2011-09-10T18:20:00Z"
lastmod = "2011-09-11T08:50:00Z"
weight = 6260
keywords = [ "static", "mac", "multiple", "dhcp" ]
aliases = [ "/questions/6260" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple MAC Addresses - Port Security - DCHP](/questions/6260/multiple-mac-addresses-port-security-dchp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6260-score" class="post-score" title="current number of votes">0</div><span id="post-6260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a situation and will give as much data as I can to paint this picture. First this only happens to machines that are newly connected to the network. Second I have noticed there are some devices on the network that are static assigned, but are within the DHCP Pool with no reservations. Third we are running port-security with the shutdown feature on this Cisco Switch.</p><p>Device starts and does the DHCP discover. DHCP gives the IP of one of the static devices. PC accepts and then I see a DHCP decline. Then another address is given by DHCP, another static, PC accepts and then I see the DHCP decline. Then finally DHCP gives a not used address and the PC accepts and all is well. The strange thing is that all three MAC addresses are now seen on the port in Port-Security.</p><p>How can this be? We have even seen more addresses on a port and the port gets shutdown.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '11, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/9ce461c5106930f053a102a629e6f67a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomTinsley&#39;s gravatar image" /><p><span>TomTinsley</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomTinsley has no accepted answers">0%</span></p></div></div><div id="comments-container-6260" class="comments-container"></div><div id="comment-tools-6260" class="comment-tools"></div><div class="clear"></div><div id="comment-6260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6264"></span>

<div id="answer-container-6264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6264-score" class="post-score" title="current number of votes">3</div><span id="post-6264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first thing to do is to fix the network misconfiguration. Each device that is assigned a static IP address within the DHCP scope with no DHCP reservation should either be reassigned a static address outside the DHCP scope, or a reservation should be created.</p><p>Most DHCP servers have a mechanism to check if an address is in use. Windows Server calls it "DHCP conflict detection." If you enable this, the DHCP server will ping the address before offering it to a client. If the DHCP server gets a response to the ping, it will not offer the address. It will select another address and repeat the confict detection process. Note that Microsoft considers it a best practice to use client-side conflict detection rather than server conflict detection, but if you are not able to reassign the static IP addresses or create DHCP reservations, this might help.</p><p>Finally, what do you mean "all three MAC addresses are now seen on the port....?" The only MAC addresses that should be seen in Port-Security are the MAC addresses of systems passing ingress traffic. In other words, assuming this is an access port with only one device connected, then the only MAC address you should see in the Port-Security configuration is the MAC address of the directly connected device. The DHCP server has tried to hand out three IP addresses, but this does not involve three MAC addresses. The number of IP addresses that the DHCP server offers to the client should have nothing to do with the number of MAC addresses that appear on the port.</p><p>You said this happens to newly connected devices. Was there another device connected to the same port before the new device, or was the port unused? When you connect a new device to a port, the switch still remembers the MAC address(es) of the previously connected device(s) unless you manually clear the configuration or you have port security aging enabled. Even though you only have one device at a time connected to the port, you can accidentally exceed the number of MAC addresses allowed in the Port-Security configuration over time as devices age and are replaced with newer devices.</p><p>If you are using dynamic secure MAC addresses, the switch will remember the MAC addresses until you clear the configuration, or until the switch is rebooted. If you are using sticky secure MAC addresses, the switch will remember the MAC addresses even if the switch is rebooted. You will have to manually clear the old MAC address(es).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '11, 21:12</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-6264" class="comments-container"><span id="6267"></span><div id="comment-6267" class="comment"><div id="post-6267-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. I have told the DHCP Team to do the static reservation for the device as well.</p><p>The three MAC Addresses... I mean this switchport has no mac addresses on it. The machine is a newley imaged machine. So hooking up to the switchport, no ip is on the host and no MAC is on the switchport.</p><p>I realize the only mac addresses that should be seen on the switchport is the source address entering the switchport. This is why I am confused. Why/How could a MAC for an HP Printer be on tne switchport? I tracked down the mac address and did find it on another switch on the network.</p><p>I will need to look harder at the sniffer trace and the switchport/pc.</p></div><div id="comment-6267-info" class="comment-info"><span class="comment-age">(11 Sep '11, 05:45)</span> <span class="comment-user userinfo">TomTinsley</span></div></div></div><div id="comment-tools-6264" class="comment-tools"></div><div class="clear"></div><div id="comment-6264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6271"></span>

<div id="answer-container-6271" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6271-score" class="post-score" title="current number of votes">1</div><span id="post-6271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Windows 7 uses a random MAC address for the LLTD service (Link Layer Topology Discovery, used for SOHO networks to check if the PC is connected to a switch or hub).</p><p>Unless the service is disabled the random MAC address is generated and used when the users clicks "See full map" in the network sharing center.</p><p>This still does not explain the use of the HP printers MAC address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '11, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-6271" class="comments-container"></div><div id="comment-tools-6271" class="comment-tools"></div><div class="clear"></div><div id="comment-6271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

