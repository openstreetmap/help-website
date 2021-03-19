+++
type = "question"
title = "TCP Dup Ack.  TCP Retransmission"
description = '''Clients on the network are complaining that a lot of the time, when they try to open a web page, their browser times out. Usually, if they hit refresh, the page will load. I&#x27;ve performed speed tests, ping tests, and DNS tests. They all come back good. I downloaded wireshark and ran a trace while try...'''
date = "2015-06-11T14:12:00Z"
lastmod = "2015-06-12T01:30:00Z"
weight = 43087
keywords = [ "tcp_retransmission", "tcp_dup_ack" ]
aliases = [ "/questions/43087" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Dup Ack. TCP Retransmission](/questions/43087/tcp-dup-ack-tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43087-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Clients on the network are complaining that a lot of the time, when they try to open a web page, their browser times out. Usually, if they hit refresh, the page will load. I've performed speed tests, ping tests, and DNS tests. They all come back good. I downloaded wireshark and ran a trace while trying access the Internet. I get a lot of TCP Dup ACK and TCP Retransmissions. The trace file can be found at <a href="http://pcc-tech.com/wireshark/file3.pcapng">http://pcc-tech.com/wireshark/file3.pcapng</a><br />
</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags">tcp_retransmission tcp_dup_ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '15, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/ba12280701e502c2d4190ebd3aada6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Sanders&#39;s gravatar image" /><p>Tim Sanders<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Sanders has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '15, 14:13</p></div></div><div id="comments-container-43087" class="comments-container"></div><div id="comment-tools-43087" class="comment-tools"></div><div class="clear"></div><div id="comment-43087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43089"></span>

<div id="answer-container-43089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43089-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace shows a lot of SYN retransmissions that would show up as a connection timeout in the browser.<br />
In the example below the SYN packets to 162.159.242.165 (ask.wireshark.org) don't get a reply whereas the subsequent SYN packets to 162.159.241.165 go through immediately.<br />
22 seconds later also the SYN packets to 162.159.242.165 get through immediately. Assuming that both servers were available at the time, I suspect it is the router 192.168.0.254 that blocks the new connections intentionally . <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-243.png" alt="alt text" /><br />
</p><hr /><p>The duplicate acknowlegdements are due to out_of_order arrival or packet loss</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '15, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jun '15, 01:48</p></div></div><div id="comments-container-43089" class="comments-container"><span id="43093"></span><div id="comment-43093" class="comment"><div id="post-43093-score" class="comment-score"></div><div class="comment-text"><p>I've tried two different routers. Although I haven't run a trace using the second router, the users get the same symptoms.</p></div><div id="comment-43093-info" class="comment-info"><span class="comment-age">(12 Jun '15, 04:07)</span> Tim Sanders</div></div><span id="43094"></span><div id="comment-43094" class="comment"><div id="post-43094-score" class="comment-score"></div><div class="comment-text"><p>Then you should be talking to your OfficeScan administrators and have them check the logs. If that doesn't show anything suspicious you will need to start tracing in the router to see if the SYN requests made it into the WAN.</p></div><div id="comment-43094-info" class="comment-info"><span class="comment-age">(12 Jun '15, 05:39)</span> mrEEde</div></div></div><div id="comment-tools-43089" class="comment-tools"></div><div class="clear"></div><div id="comment-43089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

