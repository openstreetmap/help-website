+++
type = "question"
title = "Laptop sending many ARP requests"
description = '''Did a capture today which showed my laptop sending ARP after ARP requests to unknown IP addresses.  Example:  182 38.717398 HonHaiPr_7c:4c:f9 Broadcast ARP 42 Who has 192.168.1.135? Tell 192.168.1.130 24 10.035381 HonHaiPr_7c:4c:f9 Broadcast ARP 42 Who has 192.168.1.1? Tell 192.168.1.130 28 16.79452...'''
date = "2017-06-21T16:15:00Z"
lastmod = "2017-06-22T09:08:00Z"
weight = 62221
keywords = [ "arp", "honhaipr" ]
aliases = [ "/questions/62221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Laptop sending many ARP requests](/questions/62221/laptop-sending-many-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Did a capture today which showed my laptop sending ARP after ARP requests to unknown IP addresses.</p><p>Example:</p><p><code> 182 38.717398   HonHaiPr_7c:4c:f9   Broadcast   ARP 42  Who has 192.168.1.135? Tell 192.168.1.130 24  10.035381   HonHaiPr_7c:4c:f9   Broadcast   ARP 42  Who has 192.168.1.1? Tell 192.168.1.130 28  16.794527   HonHaiPr_7c:4c:f9   Broadcast   ARP 42  Who has 192.168.1.108? Tell 192.168.1.130</code></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ARP_requests.png" alt="alt text" /></p><hr /><p>Looking for assistance on how to determine what service or program might be causing this?</p></div><div id="question-tags" class="tags-container tags">arp honhaipr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '17, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/07e5490d4c55e279612f353587bc1595?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geo3d&#39;s gravatar image" /><p>geo3d<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geo3d has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '17, 06:59</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-62221" class="comments-container"></div><div id="comment-tools-62221" class="comment-tools"></div><div class="clear"></div><div id="comment-62221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62229"></span>

<div id="answer-container-62229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62229-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>At first look what IP address does your laptop have. I see unicast packet no.134 sourced from IP 192.168.1.142. Probably this is your address. Whereas ARP requests contain "Tell 192.168.1.130", it means they're sourced from 192.168.1.130. So it can be someone's else laptop sending these ARPs and you see them just because they are broadcasts.</p><p>As for ARPs themselves, this looks like ARP scan. It can be some monitoring software doing discovery. But at first - be sure what PC is the source of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '17, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '17, 02:14</p></div></div><div id="comments-container-62229" class="comments-container"><span id="62232"></span><div id="comment-62232" class="comment"><div id="post-62232-score" class="comment-score"></div><div class="comment-text"><p>PVlad, thanks and yes the ARP requests are coming from my wife's laptop (sorry I wasn't more clear on that). She's been having some bandwidth issues lately so I first changed wifi channels to something with much less traffic then next day did a scan for further troubleshooting. That's when I noticed the numerous ARP scans. Did a lookup on the web and noticed someone else came across same exact issue but no resolution was provided. I'm trying to pinpoint the source program that is sending the ARP requests.</p></div><div id="comment-62232-info" class="comment-info"><span class="comment-age">(22 Jun '17, 04:36)</span> geo3d</div></div></div><div id="comment-tools-62229" class="comment-tools"></div><div class="clear"></div><div id="comment-62229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62239"></span>

<div id="answer-container-62239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62239-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Look for malware.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '17, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/1e2248ffe211b38de2fb9be2943c4308?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Velas&#39;s gravatar image" /><p>Velas<br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Velas has no accepted answers">0%</span></p></div></div><div id="comments-container-62239" class="comments-container"></div><div id="comment-tools-62239" class="comment-tools"></div><div class="clear"></div><div id="comment-62239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

