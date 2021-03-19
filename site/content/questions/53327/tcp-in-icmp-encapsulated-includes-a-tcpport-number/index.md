+++
type = "question"
title = "TCP in ICMP encapsulated includes a tcp.port number"
description = '''Hi, i was filtering my log file when i suddenly saw a packet with tcp.ports. BUT it was an ICMP packet. After more investigation, i saw, that it is an icmp redirect encapsulating an ipv4 tcp packet. Wireshark however parses this encapsulated port and tells me, that this packet uses this port. Why is...'''
date = "2016-06-08T23:15:00Z"
lastmod = "2016-06-09T01:06:00Z"
weight = 53327
keywords = [ "icmp", "tcp.port", "tshark" ]
aliases = [ "/questions/53327" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP in ICMP encapsulated includes a tcp.port number](/questions/53327/tcp-in-icmp-encapsulated-includes-a-tcpport-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53327-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i was filtering my log file when i suddenly saw a packet with tcp.ports. BUT it was an ICMP packet. After more investigation, i saw, that it is an icmp redirect encapsulating an ipv4 tcp packet. Wireshark however parses this encapsulated port and tells me, that this packet uses this port. Why is it like this? How can i filter them to not tell me that this icmp request is using that port? Currently i use -e tcp.srcport @ TShark. This leads to a packet with a tcp port but NO stream number. :(</p><p>Greetings</p></div><div id="question-tags" class="tags-container tags">icmp tcp.port tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '16, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/5923ac68c0bcdb604bc92b88d69b5dfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="login47&#39;s gravatar image" /><p>login47<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="login47 has no accepted answers">0%</span></p></div></div><div id="comments-container-53327" class="comments-container"><span id="53328"></span><div id="comment-53328" class="comment"><div id="post-53328-score" class="comment-score"></div><div class="comment-text"><p>btw, this page tells me everytime that the captcha was invalid. however, it worked.</p></div><div id="comment-53328-info" class="comment-info"><span class="comment-age">(08 Jun '16, 23:16)</span> login47</div></div></div><div id="comment-tools-53327" class="comment-tools"></div><div class="clear"></div><div id="comment-53327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53329"></span>

<div id="answer-container-53329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53329-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Protocols can be stacked, hence it's impossible to tell which level to include or exclude for a filter (although this is being thought about, it becomes very complex quickly).</p><p>Prefix your (capture/display) filter 'not icmp and tcp...' to get rid of the ICMP packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '16, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53329" class="comments-container"><span id="53334"></span><div id="comment-53334" class="comment"><div id="post-53334-score" class="comment-score"></div><div class="comment-text"><p>thanks for the answer, but I want all information in one big csv. Thats why I want all packets to be in there, and for each packet the tcp port. But having ICMP request with a tcp.port is not really good :/ however, i was able to filter that with tcp.len for example. Thanks for the answer though!</p></div><div id="comment-53334-info" class="comment-info"><span class="comment-age">(09 Jun '16, 06:33)</span> login47</div></div></div><div id="comment-tools-53329" class="comment-tools"></div><div class="clear"></div><div id="comment-53329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

