+++
type = "question"
title = "Difference between Wireshark and Packet Tracer?"
description = '''Hello all, I was wondering what are the main differences between Packet tracer ICMP packet capture and the Wireshark packet capture? Thank you in advance!'''
date = "2014-10-13T05:18:00Z"
lastmod = "2014-10-15T18:32:00Z"
weight = 37009
keywords = [ "between", "difference", "tracer", "packet", "wireshark" ]
aliases = [ "/questions/37009" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between Wireshark and Packet Tracer?](/questions/37009/difference-between-wireshark-and-packet-tracer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I was wondering what are the main differences between Packet tracer ICMP packet capture and the Wireshark packet capture?</p><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags">between difference tracer packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '14, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/3b04af832dc157423271b132cfe94c05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="verchiels&#39;s gravatar image" /><p>verchiels<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="verchiels has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Oct '14, 17:32</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37009" class="comments-container"></div><div id="comment-tools-37009" class="comment-tools"></div><div class="clear"></div><div id="comment-37009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37019"></span>

<div id="answer-container-37019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37019-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet Tracer doesn't capture packets, it's a virtualized tool created by Cisco to practice routing and switching. Mainly Cisco NetAcad students use it. It's comparable to GNS3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '14, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></div></div><div id="comments-container-37019" class="comments-container"></div><div id="comment-tools-37019" class="comment-tools"></div><div class="clear"></div><div id="comment-37019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37089"></span>

<div id="answer-container-37089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37089-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet Tracer's traffic simulation tools are similar to Wireshark in the sense that you can click on a PDU (in this case, an envelope) and look at the bytes in the message as well as the decoded meaning of the message at the different layers of the stack, but that's really as far as the similarities go.</p><p>Packet Tracer is not only not a real network, but it's not a virtualized network either, at least not in the same sense as something like GNS3 (which can run real Cisco IOS and create real packets, even those leaving a physical network card). Packet Tracer is limited to its own sandbox and exists solely for training purposes, whereas Wireshark has a greater scope. Wireshark can look at "real" packets from actual networks, both from a network card directly or saved/distributed in a standardized packet capture file format. In short, Wireshark's scope extends to the real world, and the real network administration workforce, whereas Packet Tracer is a classroom training tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '14, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-37089" class="comments-container"></div><div id="comment-tools-37089" class="comment-tools"></div><div class="clear"></div><div id="comment-37089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

