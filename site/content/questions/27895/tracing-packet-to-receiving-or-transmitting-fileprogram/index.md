+++
type = "question"
title = "Tracing packet to receiving or transmitting file/program"
description = '''Is it possible to trace a packet to the source of its destination within the host machine? AKA Packet 7642 OUTBOUND from HOST(wow.exe) to IP-ADDRESS.  Packet 7643 INBOUND from IP-ADDRESS to HOST(Chrome.exe)'''
date = "2013-12-07T10:24:00Z"
lastmod = "2013-12-07T18:11:00Z"
weight = 27895
keywords = [ "receive", "tracing", "identify", "source", "programs" ]
aliases = [ "/questions/27895" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tracing packet to receiving or transmitting file/program](/questions/27895/tracing-packet-to-receiving-or-transmitting-fileprogram)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27895-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to trace a packet to the source of its destination within the host machine?</p><p>AKA Packet 7642 OUTBOUND from HOST(wow.exe) to IP-ADDRESS. Packet 7643 INBOUND from IP-ADDRESS to HOST(Chrome.exe)</p></div><div id="question-tags" class="tags-container tags">receive tracing identify source programs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '13, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/22c0ce7dfcca02abe029772610d051a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JourneyJay&#39;s gravatar image" /><p>JourneyJay<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JourneyJay has no accepted answers">0%</span></p></div></div><div id="comments-container-27895" class="comments-container"></div><div id="comment-tools-27895" class="comment-tools"></div><div class="clear"></div><div id="comment-27895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27904"></span>

<div id="answer-container-27904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27904-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure I understand the question. Applications don't communicate to each other within the host via IP packets in this way unless you're talking about virtual machines within the host.</p><p>For mapping the application to packets that are leaving the host, the IP and port number (the socket) would be a good indicator. Some applications give themselves away a bit too, such as the "user agent" value in HTTP packets that indicate the browser in use. This isn't foolproof though, and the packet itself certainly wouldn't be enough to derive the executable file on the source computer that ultimately had the packet sent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '13, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-27904" class="comments-container"><span id="27908"></span><div id="comment-27908" class="comment"><div id="post-27908-score" class="comment-score"></div><div class="comment-text"><p>If the PC is capable of directing the packets to an application, then it must also be possible to figure out which application is send/receiving the information. You did not answer my question.</p><p>HOST = "Your IP"</p></div><div id="comment-27908-info" class="comment-info"><span class="comment-age">(07 Dec '13, 23:18)</span> JourneyJay</div></div><span id="27914"></span><div id="comment-27914" class="comment"><div id="post-27914-score" class="comment-score"></div><div class="comment-text"><p>Wireshark can't (currently) do that, but Message Analyzer (formerly Network monitor) from Microsoft can.</p></div><div id="comment-27914-info" class="comment-info"><span class="comment-age">(08 Dec '13, 05:03)</span> grahamb ♦</div></div><span id="27918"></span><div id="comment-27918" class="comment"><div id="post-27918-score" class="comment-score"></div><div class="comment-text"><p>JourneyJay, the host recognizes the IP packet as belonging to a given TCP or a UDP port that an application is listening on. The host knows its own state information for what applications have what sessions running on what ports, and so when it gets an IP packet for destination port 80 (for example), and if it's a web server, it would pass that to the web server application that is "listening" on that port.</p><p>In order to look at a packet on its own and definitively say what program is using it on the host, you need to have the awareness of that computer's operating system, not just the packet.</p><p>In that example, is the computer running Apache or Microsoft IIS? Both would normally expect to see new TCP sessions built on port 80 for client HTTP requests, and Wireshark can surmise that port 80 should call the HTTP dissector, but with that IP packet there is no way to drill down into the operating system of the receiver of the packet to say what application is listening on that port.</p></div><div id="comment-27918-info" class="comment-info"><span class="comment-age">(08 Dec '13, 09:16)</span> Quadratic</div></div></div><div id="comment-tools-27904" class="comment-tools"></div><div class="clear"></div><div id="comment-27904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

