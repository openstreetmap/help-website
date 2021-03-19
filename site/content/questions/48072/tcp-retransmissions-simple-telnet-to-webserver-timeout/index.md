+++
type = "question"
title = "TCP Retransmissions - Simple Telnet to Webserver - Timeout"
description = '''Hi everyone I just ran into an issues in my network, where I wanted to connect from a machine in subnet &quot;C&quot; to a machien in subnet &quot;A&quot; on port 80. On the way, the packet passes two firewalls, which are configured to pass the traffic, I see the traffic in the logs as &quot;passed&quot;. As I still can&#x27;t get a ...'''
date = "2015-11-30T02:51:00Z"
lastmod = "2015-11-30T06:11:00Z"
weight = 48072
keywords = [ "tcp", "tcp-retransmit" ]
aliases = [ "/questions/48072" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Retransmissions - Simple Telnet to Webserver - Timeout](/questions/48072/tcp-retransmissions-simple-telnet-to-webserver-timeout)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone</p><p>I just ran into an issues in my network, where I wanted to connect from a machine in subnet "C" to a machien in subnet "A" on port 80. On the way, the packet passes two firewalls, which are configured to pass the traffic, I see the traffic in the logs as "passed".</p><p>As I still can't get a connection, I ran tcpdump on the client and the server like "tcpdump -s 65535 port 80".</p><p>I uploaded the files to:<br />
<a href="https://noskin.ch/tcp_client.pcap">Client PCAP</a><br />
<a href="https://noskin.ch/tcp_srv.pcap">Server PCAP</a><br />
</p><p>Something seems to be pretty wrong, but I can't deduce much from that pcap...</p></div><div id="question-tags" class="tags-container tags">tcp tcp-retransmit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/001a62488d7db5d6571ad5771ae03d52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="esc4rg0t&#39;s gravatar image" /><p>esc4rg0t<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="esc4rg0t has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Nov '15, 06:03</p></div></div><div id="comments-container-48072" class="comments-container"><span id="48076"></span><div id="comment-48076" class="comment"><div id="post-48076-score" class="comment-score"></div><div class="comment-text"><p>Server link is corrupted</p></div><div id="comment-48076-info" class="comment-info"><span class="comment-age">(30 Nov '15, 04:29)</span> Christian_R</div></div><span id="48077"></span><div id="comment-48077" class="comment"><div id="post-48077-score" class="comment-score"></div><div class="comment-text"><p>What led you to that conclusion? :-)</p></div><div id="comment-48077-info" class="comment-info"><span class="comment-age">(30 Nov '15, 05:36)</span> esc4rg0t</div></div><span id="48078"></span><div id="comment-48078" class="comment"><div id="post-48078-score" class="comment-score"></div><div class="comment-text"><p>The posted Link to the "server pcap" file does not work.</p></div><div id="comment-48078-info" class="comment-info"><span class="comment-age">(30 Nov '15, 06:00)</span> Christian_R</div></div><span id="48080"></span><div id="comment-48080" class="comment"><div id="post-48080-score" class="comment-score"></div><div class="comment-text"><p>fixed, my bad...</p></div><div id="comment-48080-info" class="comment-info"><span class="comment-age">(30 Nov '15, 06:03)</span> esc4rg0t</div></div></div><div id="comment-tools-48072" class="comment-tools"></div><div class="clear"></div><div id="comment-48072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48081"></span>

<div id="answer-container-48081" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48081-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The server ignores the incoming requests. As you haven't stated whether the problem only exists for that one client or for more clients, the possibilities are:</p><ul><li><p>the web daemon is down</p></li><li><p>some firewall is running directly on the server which does not allow requests from that client in</p></li><li><p>if the server has more network cards, there may be a routing issue so it may be sending responses to the client's requests through another card than the one on which you capture, and they may not reach the client because some of the firewalls en route cannot match them with the requests.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></p></div></div><div id="comments-container-48081" class="comments-container"><span id="48084"></span><div id="comment-48084" class="comment"><div id="post-48084-score" class="comment-score"></div><div class="comment-text"><p>Well, you're right, it was indeed a routing issue because one of the machines is multi-homed. I overlooked that an entry was missing...:-/</p></div><div id="comment-48084-info" class="comment-info"><span class="comment-age">(30 Nov '15, 06:20)</span> esc4rg0t</div></div><span id="48088"></span><div id="comment-48088" class="comment"><div id="post-48088-score" class="comment-score"></div><div class="comment-text"><p>@esc4rg0t</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-48088-info" class="comment-info"><span class="comment-age">(30 Nov '15, 07:05)</span> grahamb ♦</div></div></div><div id="comment-tools-48081" class="comment-tools"></div><div class="clear"></div><div id="comment-48081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

