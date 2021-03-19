+++
type = "question"
title = "BAD_ADRESSES"
description = '''hi All; we have an issue last 2 days, Machines on networks get Ip adress but could not access to domaine. When checkd the DHCP server, we found out a list of BAD_ADRESS, even if those ip is not assigned. we Checked out the network if for other DHCP servers using wireshark ( Bootp == 2 Filetr), we fo...'''
date = "2013-03-28T02:26:00Z"
lastmod = "2013-03-28T04:49:00Z"
weight = 19895
keywords = [ "arp", "dhcp", "bad_adresses", "dns" ]
aliases = [ "/questions/19895" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [BAD\_ADRESSES](/questions/19895/bad_adresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19895-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi All;</p><p>we have an issue last 2 days, Machines on networks get Ip adress but could not access to domaine. When checkd the DHCP server, we found out a list of BAD_ADRESS, even if those ip is not assigned. we Checked out the network if for other DHCP servers using wireshark ( Bootp == 2 Filetr), we found that all ip offers are from the principal DHCP Server. now we don't really know what is the problem??</p><p>is there any way to analyse the ARP or DNS server using Wireshark?</p><p>Regards;</p></div><div id="question-tags" class="tags-container tags">arp dhcp bad_adresses dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '13, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/7b24340bbeb6eba8ce25f965ece2d515?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mysystem&#39;s gravatar image" /><p>mysystem<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mysystem has no accepted answers">0%</span></p></div></div><div id="comments-container-19895" class="comments-container"></div><div id="comment-tools-19895" class="comment-tools"></div><div class="clear"></div><div id="comment-19895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19897"></span>

<div id="answer-container-19897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19897-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From what I understand ( and I had to Google for it), "BAD_ADDRESS" is what is written in Windows 2008 DHCP Server logs when it goes to allocate an IP address, but finds that a host is already using it (the DHCP server does a ARP or ICMP test) and logs this event. This forum entry gave me the clue <a href="http://community.spiceworks.com/topic/251943-bad_address-in-windows-2008-dhcp-server">http://community.spiceworks.com/topic/251943-bad_address-in-windows-2008-dhcp-server</a></p><p>While you may not find a rogue DHCP server, you should be able to determine who is using that IP address. From any host you can try to ping the conflicting address, and even if you don't get a result, you should get an ARP response. From Windows you can this with "arp -a". Once you have a MAC address then it is up to you work out from your network switch mac-address tables and so forth to track down the port. Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '13, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-19897" class="comments-container"></div><div id="comment-tools-19897" class="comment-tools"></div><div class="clear"></div><div id="comment-19897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

