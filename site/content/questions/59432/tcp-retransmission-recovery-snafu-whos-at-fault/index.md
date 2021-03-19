+++
type = "question"
title = "TCP Retransmission Recovery SNAFU: Who&#x27;s at Fault?"
description = '''Greetings sniffer warriors, I have a strange TCP retransmission recovery error on an HTTPs exchange and I don&#x27;t know who the culprit is, the client or the server. All goes well (handshake, crypto, some data), then the client sends a TCP Zero Window with an ACK of a PARTIAL sequence. For example simp...'''
date = "2017-02-15T06:07:00Z"
lastmod = "2017-02-15T11:54:00Z"
weight = 59432
keywords = [ "ack", "sack", "retransmission", "tcp" ]
aliases = [ "/questions/59432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission Recovery SNAFU: Who's at Fault?](/questions/59432/tcp-retransmission-recovery-snafu-whos-at-fault)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59432-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings sniffer warriors,</p><p>I have a strange TCP retransmission recovery error on an HTTPs exchange and I don't know who the culprit is, the client or the server.</p><p>All goes well (handshake, crypto, some data), then the client sends a TCP Zero Window with an ACK of a PARTIAL sequence. For example simply to illustrate, server sending:</p><p>[1-100 ] Seq 100</p><p>[101-200] Seq 200</p><p>[201-300] Seq 300</p><p>[301-400] Seq 400</p><p>At some point after this, the client sends: TCP Zero Window, ACK 263 (right smack somewhere in the middle of packet Seq 300)</p><p>It does that a few times, then sends a window size update, followed with a regular "ACK 263". The server doesn't seem to know how to send this "mid packet" 263 segment, so it restarts by sending segment 300. The client sends what is interpreted by Wireshark as Dup Acks, still for 263 and the server keeps sending packet Seq 300. After all the previous in-flights die, the trace shows that back and forth behavior packet by packet. Ack 263 -&gt;, &lt;- Seq 300. Eventually a RST kills all this off.</p><p>One wrinkle: SACK_PERM is not enabled. This is not something I control so I'm concentrating on explaining the behavior we see.</p><p>Question: Who's at fault?<br />
</p><p>TCP Zero Window and Update is a normal process, but is it normal / ok for the client to request that the server resume at a point that is not at the boundary of a previously sent packet?</p><p>If yes, is it the server's fault for not providing a retransmission starting at the requested sequence position rather than on a previous packet border?</p><p>Would Selective ACK help in this recovery process?<br />
</p><p>Thank you :)</p></div><div id="question-tags" class="tags-container tags">ack sack retransmission tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/372da64c0dc5a0d8c5e4d79d0b7c46c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Delstar&#39;s gravatar image" /><p>Delstar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Delstar has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-59432" class="comments-container"></div><div id="comment-tools-59432" class="comment-tools"></div><div class="clear"></div><div id="comment-59432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59441"></span>

<div id="answer-container-59441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59441-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Delstar</p><p>and welcome to ask.wireshark.org. I agree with you, that the zero window and window update is the root cause. The server should either send the last frame (with Seq 200) or restart with Seq 263.</p><p>Selective acknowledgements would allow the receiver to signal just the missing bytes.</p><p>Is it possible, that you have a device between sender and receiver, that modifies the TCP stream? The device might be transparent. Potential culprits are bandwidth management systems, WAN optimizers or misbehaving firewalls.</p><p>By the way, is either the sender or the receiver a virtual system?</p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59441" class="comments-container"></div><div id="comment-tools-59441" class="comment-tools"></div><div class="clear"></div><div id="comment-59441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

