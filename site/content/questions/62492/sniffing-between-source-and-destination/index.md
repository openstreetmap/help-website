+++
type = "question"
title = "Sniffing between source and destination"
description = '''I need help on listening to the packets sent from one source to a destination which are basically a router and a WAN device. I don&#x27;t have access to the settings of either devices, the only point I can interfere is the ethernet cable the two devices are connected with. I am using a computer with two ...'''
date = "2017-07-04T06:51:00Z"
lastmod = "2017-07-04T07:16:00Z"
weight = 62492
keywords = [ "sniffing" ]
aliases = [ "/questions/62492" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing between source and destination](/questions/62492/sniffing-between-source-and-destination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62492-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need help on listening to the packets sent from one source to a destination which are basically a router and a WAN device. I don't have access to the settings of either devices, the only point I can interfere is the ethernet cable the two devices are connected with. I am using a computer with two ethernet interfaces and Wireshark as a sniffer but my problem is I want the devices recognize each other and continue their usual traffic as I am not there and also I need a copy of the whole packet network both source and destination to my computer. I tried bridging the connections in Windows but no results.</p><p>Thanks for further help</p></div><div id="question-tags" class="tags-container tags">sniffing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '17, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/b79e1c8c4ba569e09b49aa3ceedbc0df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kemaluysal&#39;s gravatar image" /><p>kemaluysal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kemaluysal has no accepted answers">0%</span></p></div></div><div id="comments-container-62492" class="comments-container"></div><div id="comment-tools-62492" class="comment-tools"></div><div class="clear"></div><div id="comment-62492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62493"></span>

<div id="answer-container-62493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62493-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think this page contains comprehensive information about capture setup:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>As for me using switch with SPAN port would be easier than making quiet transparent bridge on Windows PC. Maybe I'm wrong here. Please be more specific about "I tried bridging the connections in Windows but no results"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '17, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '17, 07:26</p></div></div><div id="comments-container-62493" class="comments-container"><span id="62497"></span><div id="comment-62497" class="comment"><div id="post-62497-score" class="comment-score"></div><div class="comment-text"><p>Establishing a bridge between two Ethernet ports on Windows worked well for me (even at W10) with WinPcap but not with NPcap as the two hook into the network stack at different points.</p><p>Budgetary (about 40$) solutions for traffic mirroring are Mikrotik RB260GS and NetGear GS105E<strong>v2</strong>.</p></div><div id="comment-62497-info" class="comment-info"><span class="comment-age">(04 Jul '17, 08:33)</span> sindy</div></div><span id="62503"></span><div id="comment-62503" class="comment"><div id="post-62503-score" class="comment-score"></div><div class="comment-text"><p>Or booting Linux (from a liveCD even) and setup a bridge that way. tcpdump, dumpcap or Wireshark for capture and you're golden. As you can see, there are many options.</p></div><div id="comment-62503-info" class="comment-info"><span class="comment-age">(04 Jul '17, 10:47)</span> Jaap ♦</div></div></div><div id="comment-tools-62493" class="comment-tools"></div><div class="clear"></div><div id="comment-62493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

