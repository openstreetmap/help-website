+++
type = "question"
title = "Why don&#x27;t we get UDP header when we capture IGMP queries and responses ?"
description = '''Hello everybody, We all know that multicast is based on UDP. IGMP works on multicast. Having said that, we don&#x27;t get UDP header when we capture IGMP queries or responses. Just wanted to know what am I missing in my understanding ? Thanks'''
date = "2017-05-16T11:52:00Z"
lastmod = "2017-05-16T21:46:00Z"
weight = 61442
keywords = [ "udp", "multicast" ]
aliases = [ "/questions/61442" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why don't we get UDP header when we capture IGMP queries and responses ?](/questions/61442/why-dont-we-get-udp-header-when-we-capture-igmp-queries-and-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61442-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody,</p><p>We all know that multicast is based on UDP. IGMP works on multicast.</p><p>Having said that, we don't get UDP header when we capture IGMP queries or responses.</p><p>Just wanted to know what am I missing in my understanding ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">udp multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '17, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/7c96ca6bc6350c661e78a1754b57b28c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Inquisitive&#39;s gravatar image" /><p>Inquisitive<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Inquisitive has no accepted answers">0%</span></p></div></div><div id="comments-container-61442" class="comments-container"></div><div id="comment-tools-61442" class="comment-tools"></div><div class="clear"></div><div id="comment-61442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61445"></span>

<div id="answer-container-61445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61445-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>"We all know that multicast is based on UDP". I'm sorry, but that assumption is wrong. You're confusing IP multicast with the most common transport protocol on top of it (UDP). The UDP protocol (IP protocol #17) is not the only protocol riding on top of IP. IGMP is its own protocol (IP protocol #2) on top of IP. Have a look <a href="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">here at IANA</a> for all assigned IP protocol numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61445" class="comments-container"><span id="61448"></span><div id="comment-61448" class="comment"><div id="post-61448-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. That helps. Now, I understand the difference between IP Multicast and UDP based Multicast.</p><ul><li>IGMP represents multicast traffic but these packets may either get transported within UDP packets or without them.</li><li>UDP can carry multicast traffic but multicast traffic doesn't necessarily need to be transported via UDP only.</li><li>IGMP and IP work in layer 3 , so none of them encapsulates the packets of the other.</li><li>When Multicast (not IP Multicast as on Internet )is implemented via UDP, we get UDP header.</li><li>When IP Multicast ( on Internet ) is used, we do not get UDP header as IP Multicast</li></ul><p>Just wanted to check if I am correct in my understanding.</p></div><div id="comment-61448-info" class="comment-info"><span class="comment-age">(16 May '17, 17:12)</span> Inquisitive</div></div><span id="61452"></span><div id="comment-61452" class="comment"><div id="post-61452-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-61452-info" class="comment-info"><span class="comment-age">(16 May '17, 23:38)</span> Jaap ♦</div></div><span id="61453"></span><div id="comment-61453" class="comment"><div id="post-61453-score" class="comment-score">1</div><div class="comment-text"><ul><li>IGMP <em>manages</em> group membership amongst IP peers. It uses IP protocol #2 to be carried on top of IP between them. <strong>This has nothing to do with UDP</strong></li><li>UDP carries <em>datagrams</em> between IP peers. That may either be Unicast, Multicast or even Broadcast transport. It is the IP layer (and datalink layer below that) that makes the Unicast/Multicast distinction. Other protocols can sit on top of IP, so these too can be Unicast or Multicast to their destination(s).</li><li>IGMP is a control protocol running alongside and makes use of IP as network protocol.</li><li>If we transport datagrams using UDP we get a UDP header, independent of whether the IP layer provides a Unicast or Multicast service.</li></ul></div><div id="comment-61453-info" class="comment-info"><span class="comment-age">(16 May '17, 23:49)</span> Jaap ♦</div></div></div><div id="comment-tools-61445" class="comment-tools"></div><div class="clear"></div><div id="comment-61445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61450"></span>

<div id="answer-container-61450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61450-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Multicast is a way to deliver traffic only to particular group of hosts.</li><li>Multicast traffic is destined to IPv4 or IPv6 multicast addresses (224.0.0.0/4; FF00::/8) on L3 and is destined to MAC adresses 01:00:5E:xx:xx:xx or 33-33-xx-xx-xx-xx on L2.</li><li>Many protocols use multicast type of delivery (OSPF, EIGRP, mDNS and others). Some of them use UDP (mDNS), some of them do not (OSPF).</li><li>IGMP is used to control multicast groups in one brodcast domain; it's built on top of IP with no use of UDP. IGMP represents multicast control, it doesn't intended to carry streams. IGMP is built on top of IP so actually it's encapsulated within IP.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div></div><div id="comments-container-61450" class="comments-container"></div><div id="comment-tools-61450" class="comment-tools"></div><div class="clear"></div><div id="comment-61450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

