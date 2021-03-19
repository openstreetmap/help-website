+++
type = "question"
title = "How to recognize a flow in wireshark?"
description = '''Hey guys, I am very new in wireshark... I want to know how can I recognize different flows in pcap files? I think that packets with the same source and destination address and the same protocol are one flow. Is that right? Thanks,'''
date = "2014-12-20T08:05:00Z"
lastmod = "2014-12-20T10:16:00Z"
weight = 38642
keywords = [ "flow", "wireshark" ]
aliases = [ "/questions/38642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to recognize a flow in wireshark?](/questions/38642/how-to-recognize-a-flow-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I am very new in wireshark... I want to know how can I recognize different flows in pcap files? I think that packets with the same source and destination address and the same protocol are one flow. Is that right?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">flow wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '14, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/092c4be3e389b7abf01fedcf335e90b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alixx&#39;s gravatar image" /><p>alixx<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alixx has no accepted answers">0%</span></p></div></div><div id="comments-container-38642" class="comments-container"></div><div id="comment-tools-38642" class="comment-tools"></div><div class="clear"></div><div id="comment-38642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38644"></span>

<div id="answer-container-38644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38644-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually, flows are recognized by the so-called 5-tupel: two sockets (which is a combination of an IP address and a port) talking to each other, and the layer 4 protocol in use.</p><p>E.g.: 192.168.0.1:1025 talking to 10.0.0.1:80 via TCP is such a 5-tupel, and would be considered a "flow" in most cases (unless someone has a different idea of what "flow" means). I would prefer "connection" instead, which is clearer.</p><p>You can identify those connections in the statistics -&gt; conversations statistics window when selecting the TCP or UDP tab.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '14, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38644" class="comments-container"><span id="38649"></span><div id="comment-38649" class="comment"><div id="post-38649-score" class="comment-score"></div><div class="comment-text"><blockquote><p>unless someone has a different idea of what "flow" means</p></blockquote><p>Are "flows" unidirectional (so that a TCP connection has <em>two</em> TCP flows) or bidirectional (so that a TCP connection and a TCP flow are the same thing)?</p><blockquote><p>I would prefer "connection" instead, which is clearer.</p></blockquote><p>Although, for UDP, there aren't connections at the transport layer, and a conversation at the protocol layer above UDP might involve more than two transport-layer endpoints (e.g., with TFTP, where the first request is from UDP port XXX to UDP port 69, the reply is from UDP port YYY to UDP port XXX, and all subsequent traffic is between UDP ports XXX and YYY).</p><p>Wireshark really needs a generalized notion of conversations, so that, for example, TFTP packets over IPv4 over Ethernet would belong to a link-layer conversation between its two MAC addresses (one or both of which might be routers rather than end nodes), an IPv4 conversation between its IPv4 addresses, a UDP conversation between its two UDP ports, and a TFTP conversation between the client and server.</p><p>Something in the UI showing conversations could also show flows, in the unidirectional sense.</p><p>But I digress. :-)</p></div><div id="comment-38649-info" class="comment-info"><span class="comment-age">(20 Dec '14, 15:44)</span> Guy Harris ♦♦</div></div><span id="38654"></span><div id="comment-38654" class="comment"><div id="post-38654-score" class="comment-score"></div><div class="comment-text"><p>It's all in the definitions I guess ;-)</p></div><div id="comment-38654-info" class="comment-info"><span class="comment-age">(22 Dec '14, 05:24)</span> Jasper ♦♦</div></div><span id="38655"></span><div id="comment-38655" class="comment"><div id="post-38655-score" class="comment-score"></div><div class="comment-text"><p>If your definition of "flow" matches Jasper's description (and mine does), Wireshark automatically labels flows which you can then use in a display filter. Expand the TCP/UDP header, and look for [Stream Index: #]. So for example if the TCP packet you have selected is labeled [Stream Index: 4], you can then use "tcp.stream == 4" in your display filter. This is a /very/ handy shortcut to something like "ip.addr X.X.X.X and ip.addr Y.Y.Y.Y and tcp.port eq AAAA and tcp.port eq BBBB". In fact it is so handy, that I add the stream number as a custom column in my default wireshark view.</p></div><div id="comment-38655-info" class="comment-info"><span class="comment-age">(22 Dec '14, 05:32)</span> smp</div></div></div><div id="comment-tools-38644" class="comment-tools"></div><div class="clear"></div><div id="comment-38644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

