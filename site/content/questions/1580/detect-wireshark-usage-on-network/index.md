+++
type = "question"
title = "Detect wireshark usage on network"
description = '''How can I know if somebody is using wireshark to analyze traffic on the network?'''
date = "2011-01-01T17:18:00Z"
lastmod = "2013-10-28T06:00:00Z"
weight = 1580
keywords = [ "analyze", "wireshark" ]
aliases = [ "/questions/1580" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Detect wireshark usage on network](/questions/1580/detect-wireshark-usage-on-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1580-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I know if somebody is using wireshark to analyze traffic on the network?</p></div><div id="question-tags" class="tags-container tags">analyze wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '11, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/da051abac41879aed4060d544d37fd6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skypemesm&#39;s gravatar image" /><p>skypemesm<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skypemesm has no accepted answers">0%</span></p></div></div><div id="comments-container-1580" class="comments-container"></div><div id="comment-tools-1580" class="comment-tools"></div><div class="clear"></div><div id="comment-1580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1583"></span>

<div id="answer-container-1583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1583-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>While packet sniffing is generally quite passive, in that you are meant to be listening to just copies of packets there are techniques. As Hansang said one way is to detect how the network responds to certain ARP packets. Machine in promiscous mode (which Wireshark will normally have turned on, respond slightly different to non-promiscuous boxes. Another thing is to look for the name resolution queries that a Wireshark client might be using. If Wireshark has NR turned on, it will try and do a reverse lookup on IP addresses it sees. So if you inject a packet into the network with an IP address that other boxes are unlikely to be using, you might see Wireshark trying to do this reverse lookup.</p><p>In either case this isn't proof of wireshark use, and can probably be countered by appropriate configuration by the wireshark user.</p><p>To be honest if you want to try and manage the impact of packet sniffing on your network you are best off a) having a clear policy for your staff or those authorised to use network - and enforce it as a people management problem and b) lock down your network with appropriate configuration and have appropriate authentication/authorisation/auditing for system administration of your network.</p><p>In my opinion, if you are concerned about Wireshark use on you network, then you probably need to look at the broader issues of appropriate network security policy (such as encryption, network access control, separation of duties, and so on).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1583" class="comments-container"></div><div id="comment-tools-1583" class="comment-tools"></div><div class="clear"></div><div id="comment-1583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1581"></span>

<div id="answer-container-1581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1581-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In a modern network using switches, they wouldn't be able to do much w/o resorting to arp poisoning or flooding. But other than tat, I'm not sure how you could tell.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-1581" class="comments-container"></div><div id="comment-tools-1581" class="comment-tools"></div><div class="clear"></div><div id="comment-1581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26461"></span>

<div id="answer-container-26461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26461-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All of the above is correct. However, if you have reason to suspect a specific user, there is a way to detect for certain that their network card is in promiscuous mode.</p><p>This needs to be done on the local network segment...</p><p>Assume the suspected computer has a MAC of AA:AA:AA:AA:AA:AA - use Hping3 to craft a ping (ICMP type 8) to the correct IP address, but a destination MAC address of ZZ:ZZ:ZZ:ZZ:ZZ:ZZ. If the NIC is is normal operation, it will ignore the packet and you will get no response. If the NIC is in promiscuous mode, it will process the packet and pass it to the TCP/IP stacks. You will get a response.</p><p>Works in my testing anyway...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p>kpalmgren<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span></p></div></div><div id="comments-container-26461" class="comments-container"></div><div id="comment-tools-26461" class="comment-tools"></div><div class="clear"></div><div id="comment-26461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

