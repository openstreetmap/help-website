+++
type = "question"
title = "log question, openvpn related"
description = '''Hello, I&#x27;m using wireshark to verify my openvpn connexion is truly encrypted, I&#x27;ve found a guide around the web : http://www.online-tech-tips.com/computer-tips/check-vpn-connection-actually-encrypted/ Problem, I tried the test and ended with similar logs with &amp;amp; without vpn : http://i.imgur.com/t...'''
date = "2016-05-13T22:24:00Z"
lastmod = "2016-05-14T02:06:00Z"
weight = 52557
keywords = [ "openvpn" ]
aliases = [ "/questions/52557" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [log question, openvpn related](/questions/52557/log-question-openvpn-related)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using wireshark to verify my openvpn connexion is truly encrypted, I've found a guide around the web : <a href="http://www.online-tech-tips.com/computer-tips/check-vpn-connection-actually-encrypted/">http://www.online-tech-tips.com/computer-tips/check-vpn-connection-actually-encrypted/</a></p><p>Problem, I tried the test and ended with similar logs with &amp; without vpn : <a href="http://i.imgur.com/tBHRlcM.png">http://i.imgur.com/tBHRlcM.png</a></p><p>In the capture, the packets titled 'standard query' or 'standard query response' are readable with or without vpn connection enabled. Could a wireshark developer tell me if that's normal or if I should be worried?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">openvpn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/1ad0a44c5f297309fc70b4bffa88c081?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asiagoro&#39;s gravatar image" /><p>asiagoro<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asiagoro has no accepted answers">0%</span></p></div></div><div id="comments-container-52557" class="comments-container"></div><div id="comment-tools-52557" class="comment-tools"></div><div class="clear"></div><div id="comment-52557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52559"></span>

<div id="answer-container-52559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52559-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'll dare to answer although I am not a Wireshark developer, as I don't think it needs a Wireshark developer to answer.</p><p>In both packets you've shown, the source IP address and the destination IP address are almost identical, which almost sure means that they are in the same subnet (can't be 100% sure as you have posted just screenshots and not a complete capture file).</p><p>Simplifying a lot, what the VPN software normally does is that it creates a virtual interface in your PC and replaces the default route for all the PC's IP traffic by its own one pointing to that interface, using the original default route's target as a route to the remote VPN server. This means that packets towards any IP address, except the VPN server's own one, go to the virtual interface, which encrypts and encapsulates them and sends them to the VPN server's address using the physical interface.</p><p>However, there is one more exception, and that is LAN traffic (i. e. traffic between devices sharing the same IP subnet). Packets towards equipment on the same LAN do not need any routing information and are sent directly to it rather than to a gateway element (router).</p><p>So the following are my assumptions about your home network:</p><ul><li><p>you use a home router which has an IP address 192.168.1.1 and assigns client PCs their IP addresses using DHCP protocol</p></li><li><p>it also acts as a DNS proxy, which means that it tells the client PCs to use it as DNS server.</p></li></ul><p>So your other traffic to the internet is likely encrypted, but your DNS queries are effectively not, because you send them to your home router which is not a member of the VPN and whenever it cannot respond your query from a previously cached answer, it sends that query "in its own name" (which is its IP address looking towards the internet, so enough to identify you) to the DNS server whose address it has got from your ISP.</p><p>To avoid this, you have to configure your PC to use a DNS in the internet directly, instead of sending the queries to the home router. The VPN provider's or your ISP's web pages may suggest you one. Or you may open the admin interface of your home router and find it there as the ISP has configured it there statically before shipping it or using DHCP every time it comes up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '16, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 May '16, 02:10</p></div></div><div id="comments-container-52559" class="comments-container"></div><div id="comment-tools-52559" class="comment-tools"></div><div class="clear"></div><div id="comment-52559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

