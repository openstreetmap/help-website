+++
type = "question"
title = "Not honoring own MSS?"
description = '''During the initial TCP handshake, the server specifies a MSS of 1460, and the client specifies a MSS of 1200. However, the server sends segments with lengths of 32786, 15444, 13068, 5940 and 2376. Is this normal? Why the server would behave this way?'''
date = "2011-07-06T14:15:00Z"
lastmod = "2011-07-07T07:34:00Z"
weight = 4932
keywords = [ "handshake", "mss", "tcp" ]
aliases = [ "/questions/4932" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Not honoring own MSS?](/questions/4932/not-honoring-own-mss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4932-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During the initial TCP handshake, the server specifies a MSS of 1460, and the client specifies a MSS of 1200. However, the server sends segments with lengths of 32786, 15444, 13068, 5940 and 2376.</p><p>Is this normal? Why the server would behave this way?</p></div><div id="question-tags" class="tags-container tags">handshake mss tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '11, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/a30f6e3f86c45e342ffe5e002b77c0cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamesm113&#39;s gravatar image" /><p>jamesm113<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamesm113 has no accepted answers">0%</span></p></div></div><div id="comments-container-4932" class="comments-container"></div><div id="comment-tools-4932" class="comment-tools"></div><div class="clear"></div><div id="comment-4932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4935"></span>

<div id="answer-container-4935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4935-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is the program that's capturing the traffic (Wireshark, TShark, tcpdump, dumpcap, etc.) running on the client, the server, or some other machine passively sniffing the traffic between them?</p><p>If this is on the server, you might be seeing <a href="http://en.wikipedia.org/wiki/Large_segment_offload">large segment offload</a>. If it's on the client, you might be seeing <a href="http://en.wikipedia.org/wiki/Large_receive_offload">large receive offload</a>. I.e., if you're capturing on the client or the server, you might not be seeing the actual traffic on the wire, you might be seeing what the host's TCP implementation is sending to the network adapter or receiving from the network adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4935" class="comments-container"></div><div id="comment-tools-4935" class="comment-tools"></div><div class="clear"></div><div id="comment-4935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4940"></span>

<div id="answer-container-4940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4940-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We have seen similar behavior if the traffic passes a misbehaving active device. Likely candidates are:</p><ul><li>A firewall that is not correctly processing TCP options</li><li>An ACE module with misconfigured TCP normalization</li></ul><p>In some cases we see very strange behavior caused by the wrong MSS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-4940" class="comments-container"><span id="4941"></span><div id="comment-4941" class="comment"><div id="post-4941-score" class="comment-score"></div><div class="comment-text"><p>just traced a server hidden behind an old Cisco 10mbit router today... the server advertises a MSS of 536, and then, after a few packets, I see 1024 byte segments comming thru... the router is concatenating the server's payloads, creating larger segments than advertised.</p></div><div id="comment-4941-info" class="comment-info"><span class="comment-age">(07 Jul '11, 09:03)</span> Jasper ♦♦</div></div><span id="4993"></span><div id="comment-4993" class="comment"><div id="post-4993-score" class="comment-score"></div><div class="comment-text"><p>This was a recent hot topic for me. I've learned that a system does NOT have to adhere to it's own advertised MSS...it seems that it should, but it doesn't. SystemA adverts an MSS of 1400, SystemB adverts an MSS of 1200; SystemA won't send SystemB a segment larger than 1200, but SystemA may very well send SystemB a segment that's 1400Bytes. We all assume that with an MSS based on MTU the system is, itself, limited to it's advert'd MSS - but the MSS can be artificially lowered.</p></div><div id="comment-4993-info" class="comment-info"><span class="comment-age">(12 Jul '11, 06:32)</span> GeonJay</div></div></div><div id="comment-tools-4940" class="comment-tools"></div><div class="clear"></div><div id="comment-4940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

