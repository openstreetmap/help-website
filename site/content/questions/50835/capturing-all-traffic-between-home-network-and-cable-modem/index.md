+++
type = "question"
title = "Capturing all traffic between home network and cable modem"
description = '''Hello, Is it possible to capture all WAN traffic (between a WiFi router and the cable modem) by inserting an Ethernet Switch and plugging in the router, Cable modem, and a PC running WireShark? If not, any suggestions on how to capture all traffic going to the WAN? Thanks, Dieter K.'''
date = "2016-03-11T14:55:00Z"
lastmod = "2016-03-11T15:32:00Z"
weight = 50835
keywords = [ "cable_modem" ]
aliases = [ "/questions/50835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing all traffic between home network and cable modem](/questions/50835/capturing-all-traffic-between-home-network-and-cable-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50835-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to capture all WAN traffic (between a WiFi router and the cable modem) by inserting an Ethernet Switch and plugging in the router, Cable modem, and a PC running WireShark?</p><p>If not, any suggestions on how to capture all traffic going to the WAN?</p><p>Thanks, Dieter K.</p></div><div id="question-tags" class="tags-container tags">cable_modem</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '16, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/2f15f5151d7dc68979d7758159d41521?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dieter&#39;s gravatar image" /><p>Dieter<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dieter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '16, 15:55</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-50835" class="comments-container"></div><div id="comment-tools-50835" class="comment-tools"></div><div class="clear"></div><div id="comment-50835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50836"></span>

<div id="answer-container-50836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50836-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to capture all WAN traffic (between a WiFi router and the cable modem) by inserting an Ethernet Switch and plugging in the router, Cable modem, and a PC running WireShark?</p></blockquote><p>A <em>switch</em> would only work if it has a mirror port, so that you can see all traffic passing through the switch from that port. A true "dumb" <em>hub</em> (as opposed to a switching hub, which is a switch with the word "hub" in its description) would work. See <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark Wiki's "how to capture on Ethernet" page</a> for details.</p><p>This should be able to capture all traffic going from the machines on your home network to the cable modem or from the cable modem to machines on your hoe network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50836" class="comments-container"></div><div id="comment-tools-50836" class="comment-tools"></div><div class="clear"></div><div id="comment-50836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

