+++
type = "question"
title = "UDP Flooding"
description = '''Hi, Just want to ask it is normal UDP traffic like this?  my network became very slow after this happen in my network, the strange is why so many traffic with IP 172.16.5.1 but using many different MAC ADDRESS? since I&#x27;m new with Wireshark i dunno it is serious problem or not but my network getting ...'''
date = "2010-10-23T08:46:00Z"
lastmod = "2010-10-27T07:50:00Z"
weight = 601
keywords = [ "flood", "udp" ]
aliases = [ "/questions/601" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [UDP Flooding](/questions/601/udp-flooding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Just want to ask it is normal UDP traffic like this?</p><p><img src="http://img716.imageshack.us/i/vlan203guest22102010.jpg" alt="http://img716.imageshack.us/i/vlan203guest22102010.jpg" /></p><p>my network became very slow after this happen in my network, the strange is why so many traffic with IP 172.16.5.1 but using many different MAC ADDRESS?</p><p>since I'm new with Wireshark i dunno it is serious problem or not but my network getting very slow.</p><p>if broadcast address is 255.255.255.255 would it be broadcast in network 172.16.5.0 or it can be broadcast in all different network in one vlan? my network in 172.16.2.0 its very slow, it is possible because of this?</p></div><div id="question-tags" class="tags-container tags">flood udp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '10, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/63c4223f82f7377db9df96035b1bb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoplasma&#39;s gravatar image" /><p>neoplasma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoplasma has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '10, 12:16</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-601" class="comments-container"></div><div id="comment-tools-601" class="comment-tools"></div><div class="clear"></div><div id="comment-601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

7 Answers:

</div>

</div>

<span id="606"></span>

<div id="answer-container-606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-606-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First in answer to your broadcast question: broadcast traffic should be isolated to a single vlan (also called a broadcast domain). You can see exceptions to this rule with vlan bleed -- where two access ports with different vlan tags are connected back-to-back -- but this is changing the physical architecture and not the behavior of broadcast traffic.</p><p>As to your UDP traffic question, this is no normal behavior. I would investigate the 172.16.5.1 device and see what service or application is listening on the 7102 port. Perhaps you have a misconfiguration in the app that has a destination of the broadcast address?</p><p>You mention that the mac address is changing but it is impossible to see this in your example image -- is there any pattern to it?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '10, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/1d8eda08758411bec29092a0b8220126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" /><p>Peter<br />
<span class="score" title="65 reputation points">65</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span></p></div></div><div id="comments-container-606" class="comments-container"></div><div id="comment-tools-606" class="comment-tools"></div><div class="clear"></div><div id="comment-606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="608"></span>

<div id="answer-container-608" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-608-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>so if i have single vlan with 2 network (172.16.2.0, 172.16.5.0) the broadcast trafic 255.255.255.255 will be afect on both network right?</p><p>172.16.5.1 is a door lock system server wich is connect to room hotel, device at room hotel using serial to IP converter to connect with their server (172.16.5.1) by default the device in room doesn't have ethernet port so we use serial to IP converter to conect with server.</p><p>in my images above all the source IP is came from 172.16.5.1, but if i look detail on source MAC Address its came from all ip converter from room hotel. so all device in room hotel using ip address 172.16.5.1 and broadcast on 255.255.255.255</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '10, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/63c4223f82f7377db9df96035b1bb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoplasma&#39;s gravatar image" /><p>neoplasma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoplasma has no accepted answers">0%</span></p></div></div><div id="comments-container-608" class="comments-container"><span id="609"></span><div id="comment-609" class="comment"><div id="post-609-score" class="comment-score"></div><div class="comment-text"><p>Yes, the broadcast traffic from both 172.16.2.0 &amp; 172.16.5.0 will be visible to both if you are using secondary IP address on the same vlan.</p><p>How are the serail-to-IP converters configured? Do they get IP addresses from a DHCP server? I'm not sure I'm following your last paragraph -- could you re-state what is going on with the converters?</p></div><div id="comment-609-info" class="comment-info"><span class="comment-age">(24 Oct '10, 08:32)</span> Peter</div></div></div><div id="comment-tools-608" class="comment-tools"></div><div class="clear"></div><div id="comment-608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="610"></span>

<div id="answer-container-610" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-610-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Yes, the broadcast traffic from both 172.16.2.0 &amp; 172.16.5.0 will be visible to both if you are using secondary IP address on the same vlan.</p></blockquote><p>ok then i asumme that udp broadcast from 172.16.5.1 is the main cause my network in 172.16.2 getting very slow, at least now im confident since vendor from door lock system doubt my analys lol</p><blockquote><p>How are the serail-to-IP converters configured? Do they get IP addresses from a DHCP server? I'm not sure I'm following your last paragraph -- could you re-state what is going on with the converters?</p></blockquote><p>i duno much bout the converter since they are manage by other vendor but im sure the converter using static IP address, i'll ask them tomorow how its works, btw in my last paragraph i mean that many converter in room hotel use the same ip address (172.16.5.1) as capture in wireshark, for example frame number one came from source ip address 172.16.5.1 with mac address 00:11:22:4d:09:3b and frame number two came from source ip address 172.16.5.1 with mac address 00:11:22:4d:09:5b and so on, i think its realy weird, ok thanks peter, i'll update tomorow, sory for my terible english:)<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '10, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/63c4223f82f7377db9df96035b1bb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoplasma&#39;s gravatar image" /><p>neoplasma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoplasma has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-610" class="comments-container"></div><div id="comment-tools-610" class="comment-tools"></div><div class="clear"></div><div id="comment-610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="669"></span>

<div id="answer-container-669" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-669-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi peter i already solve the problem with shutdown all converter in villa:)</p><p>but my question is why this problem only hapen if user on villa connect to the internet through wifi? i already try with other access point and the result is the same, is user conected their laptop using cable direct in to the switch there is no problem with connection eventhough all converter is on</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/63c4223f82f7377db9df96035b1bb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoplasma&#39;s gravatar image" /><p>neoplasma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoplasma has no accepted answers">0%</span></p></div></div><div id="comments-container-669" class="comments-container"></div><div id="comment-tools-669" class="comment-tools"></div><div class="clear"></div><div id="comment-669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="671"></span>

<div id="answer-container-671" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-671-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wifi has less bandwidth available then hard-wire (11Mb or 54Mb generally for <a href="http://en.wikipedia.org/wiki/IEEE_802.11">802.11a/b/g</a>). Also wireless operates differently including: operating at half-duplex, not full and uses a <a href="http://en.wikipedia.org/wiki/CSMA/CA">CSMA/CA</a> method of controlling access to network resources while wired Ethernet uses <a href="http://en.wikipedia.org/wiki/CSMA/CD">CSMA/CD</a>.<br />
</p><p>This difference may seem small at first, but can have dramatic affects on performance particularly in situations with large amounts of broadcast traffic. Wireless is easy to setup (poorly), but requires a lot of planning and design to do correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/1d8eda08758411bec29092a0b8220126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" /><p>Peter<br />
<span class="score" title="65 reputation points">65</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-671" class="comments-container"></div><div id="comment-tools-671" class="comment-tools"></div><div class="clear"></div><div id="comment-671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="674"></span>

<div id="answer-container-674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I notice that UDP port 7102 is used by some online games (Dungeon Fighter Online from Neople) - are you playing those?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-674" class="comments-container"></div><div id="comment-tools-674" class="comment-tools"></div><div class="clear"></div><div id="comment-674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="705"></span>

<div id="answer-container-705" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>thanks peter for your great explaination, i know that my wifi bandwidth is smaller than wire, i just think that its not significant but now i know it can be dramatic effect:)</p><p>@wesmorgan no dude, udp port 7102 is used by aplication in my local network.</p><p>ok thanks guys for your help, case closed:)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/63c4223f82f7377db9df96035b1bb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neoplasma&#39;s gravatar image" /><p>neoplasma<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neoplasma has no accepted answers">0%</span></p></div></div><div id="comments-container-705" class="comments-container"></div><div id="comment-tools-705" class="comment-tools"></div><div class="clear"></div><div id="comment-705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

