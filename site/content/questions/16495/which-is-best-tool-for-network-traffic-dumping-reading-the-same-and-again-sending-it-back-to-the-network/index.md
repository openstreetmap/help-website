+++
type = "question"
title = "Which is best tool for network traffic dumping, reading the same and again sending it back to the network"
description = '''Hiii, I had an application (basically a server) that has to accept large amount of data filled in different2 structures from multiple clients for UDP packets.I want to dump this data in such a format that is easy to read back from that file and again send it back to the server, ( I MAY SAY A RECORD ...'''
date = "2012-12-03T01:56:00Z"
lastmod = "2012-12-03T03:03:00Z"
weight = 16495
keywords = [ "udp", "packet-capture", "traffic", "network", "dump" ]
aliases = [ "/questions/16495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Which is best tool for network traffic dumping, reading the same and again sending it back to the network](/questions/16495/which-is-best-tool-for-network-traffic-dumping-reading-the-same-and-again-sending-it-back-to-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hiii,</p><p>I had an application (basically a server) that has to accept large amount of data filled in different2 structures from multiple clients for UDP packets.<strong>I want to dump this data in such a format that is easy to read back from that file and again send it back to the server, ( I MAY SAY A RECORD AND REPLAY TYPE MODULE).</strong></p><p>Which tool is suitable for do the same and also that run in the backgound along in the application</p><p>thanks in advance, monz</p></div><div id="question-tags" class="tags-container tags">udp packet-capture traffic network dump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/86a2938611b19f95680b86803b74e494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monz&#39;s gravatar image" /><p>monz<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '12, 08:29</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16495" class="comments-container"></div><div id="comment-tools-16495" class="comment-tools"></div><div class="clear"></div><div id="comment-16495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16498"></span>

<div id="answer-container-16498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16498-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can capture the traffic with tcpdump, dumpcap or tshark/wireshark (which in fact also use dumpcap). As a replay tool you could use bittwist, tcpreplay, or maybe ostinato, see <a href="http://code.google.com/p/ostinato/">http://code.google.com/p/ostinato/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16498" class="comments-container"><span id="16520"></span><div id="comment-16520" class="comment"><div id="post-16520-score" class="comment-score"></div><div class="comment-text"><p>thanx for your reply......:-)</p></div><div id="comment-16520-info" class="comment-info"><span class="comment-age">(03 Dec '12, 20:23)</span> monz</div></div></div><div id="comment-tools-16498" class="comment-tools"></div><div class="clear"></div><div id="comment-16498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

