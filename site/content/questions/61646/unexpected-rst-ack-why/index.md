+++
type = "question"
title = "Unexpected RST-ACK Why"
description = '''Using Wireshark I produced the following trace. My question is, how do I determine why the host 10.0.10.110 sends the first RST,ACK in 222? Additionally, why does the server sent three RST,ACK (222, 226, and 228) before it sends a SYN in 229? 220 484.990061 10.0.10.115 10.0.10.110 TCP 263 10001 → 51...'''
date = "2017-05-26T15:23:00Z"
lastmod = "2017-05-27T01:34:00Z"
weight = 61646
keywords = [ "rst", "ack", "windows7" ]
aliases = [ "/questions/61646" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unexpected RST-ACK Why](/questions/61646/unexpected-rst-ack-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61646-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark I produced the following trace.</p><p>My question is, how do I determine why the host 10.0.10.110 sends the first RST,ACK in 222? Additionally, why does the server sent three RST,ACK (222, 226, and 228) before it sends a SYN in 229?</p><pre><code>220 484.990061  10.0.10.115 10.0.10.110 TCP 263 10001 → 51020 [PSH, ACK] Seq=26523 Ack=1 Win=2047 Len=209
221 485.199823  10.0.10.110 10.0.10.115 TCP 54  51020 → 10001 [ACK] Seq=1 Ack=26732 Win=4053 Len=0
222 488.965709  10.0.10.110 10.0.10.115 TCP 54  51020 → 10001 [RST, ACK] Seq=1 Ack=26732 Win=0 Len=0
223 489.765740  Pronet_ec:0e:2b Broadcast   ARP 60  Who has 10.0.10.110? Tell 10.0.10.115
224 489.765773  Dell_80:e0:60   Pronet_ec:0e:2b ARP 42  10.0.10.110 is at b8:ca:3a:80:e0:60
225 489.795624  10.0.10.115 10.0.10.110 TCP 60  10001 → 10001 [SYN] Seq=0 Win=2047 Len=0 MSS=1400
226 489.795667  10.0.10.110 10.0.10.115 TCP 54  10001 → 10001 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
227 490.065686  10.0.10.115 10.0.10.110 TCP 60  [TCP Port numbers reused] 10001 → 10001 [SYN] Seq=0 Win=2047 Len=0 MSS=1400
228 490.065733  10.0.10.110 10.0.10.115 TCP 54  10001 → 10001 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
229 494.704070  10.0.10.110 10.0.10.115 TCP 66  51050 → 10001 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
230 494.704856  10.0.10.115 10.0.10.110 TCP 60  10001 → 51050 [SYN, ACK] Seq=0 Ack=1 Win=2047 Len=0 MSS=1400
231 494.704870  10.0.10.110 10.0.10.115 TCP 54  51050 → 10001 [ACK] Seq=1 Ack=1 Win=64400 Len=0
232 494.992380  10.0.10.115 10.0.10.110 TCP 263 10001 → 51050 [PSH, ACK] Seq=1 Ack=1 Win=2047 Len=209
233 495.195210  10.0.10.110 10.0.10.115 TCP 54  51050 → 10001 [ACK] Seq=1 Ack=210 Win=64191 Len=0</code></pre>Here is what is happening -- the client (10.0.10.115) is pushing data to the server (10.0.10.110). The server acknowledges it, which is the normal communication flow. 220 and 221 show the normal flow. 222 shows that the server sends an RST,ACK. 225 shows the client responding with a SYN. In 226, the server sends another RST,ACK to which the client responds with another SYN (227). The server send another RST,ACK in 228 and the client sends another SYN (229). At that point, the server sends a SYN,ACK in 230, and the client responds with an ACK in 231. 232 and 233 show normal communication flow.</div><div id="question-tags" class="tags-container tags">rst ack windows7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '17, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/71f3901b34be99348e410287db7f7dc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randy_ynchausti&#39;s gravatar image" /><p>randy_ynchausti<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randy_ynchausti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '17, 01:29</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-61646" class="comments-container"></div><div id="comment-tools-61646" class="comment-tools"></div><div class="clear"></div><div id="comment-61646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61652"></span>

<div id="answer-container-61652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61652-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The RST,ACK in 222 is probably a normal session termination thing, which is kind of common now (instead of using FIN-ACK-FIN-ACK, which is slower).</p><p>The other resets are most likely caused by the fact that the client is trying to reuse the same socket pair again - normally, the client should use a different ephemeral port for each connection it starts. If the socket pairs are reused too soon you'll get a reset because the server stack doesn't accept a new connection yet that has the same IP and port pairs until some time has passed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '17, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61652" class="comments-container"></div><div id="comment-tools-61652" class="comment-tools"></div><div class="clear"></div><div id="comment-61652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

