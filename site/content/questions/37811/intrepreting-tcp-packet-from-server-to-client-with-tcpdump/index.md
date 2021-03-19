+++
type = "question"
title = "Intrepreting TCP packet from server to client with TCPDUMP"
description = '''I am trying to understand the flow of TCP dump data from my server to client. On viewing packets i notices a strange single byte packet which i am not able to interpret its occurrence reason(wthr KEEP ALIVE or zero window probe or regular data packet). UnIdentified Packet: 13:19:10.247447 IP (tos 0x...'''
date = "2014-11-13T02:37:00Z"
lastmod = "2014-11-14T23:08:00Z"
weight = 37811
keywords = [ "tcpdump", "tcp" ]
aliases = [ "/questions/37811" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Intrepreting TCP packet from server to client with TCPDUMP](/questions/37811/intrepreting-tcp-packet-from-server-to-client-with-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37811-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to understand the flow of TCP dump data from my server to client. On viewing packets i notices a strange single byte packet which i am not able to interpret its occurrence reason(wthr KEEP ALIVE or zero window probe or regular data packet).</p><p><strong>UnIdentified Packet:</strong></p><pre><code>13:19:10.247447 IP (tos 0x0, ttl 59, id 50276, offset 0, flags [DF], proto TCP (6), length 53)
172.250.10.10.13824 &gt; 172.11.105.5.49524: Flags [P.], cksum 0x6c72 (correct), seq 1456962400:1456962401, ack 3097881588, win 17680, options [nop,nop,TS val 634650466 ecr 44786420], length 1
0x0000:  4500 0035 c464 4000 3b06 af49 acfa 0a0a  [email protected];..I....
0x0010:  ac0b 6905 3600 c174 56d7 7b60 b8a5 ebf4  ..i.6..tV.{`....
0x0020:  8018 4510 6c72 0000 0101 080a 25d3 ff62  ..E.lr......%..b
0x0030:  02ab 62f4 00</code></pre><p><a href="http://pastebin.com/hmDGLXx4">http://pastebin.com/hmDGLXx4</a></p><p>Also, we noticed below performances from our application. Still trying to find the root cause from the same:</p><pre><code>1. Suddenly @ 20:58 , we noticed TCP stopped giving ACK to PUSH message that it received from server.
2. Between 20.58 to 21:15 , from our client application we tried sending data to server, Where send was successful and for those sever request .Application ended up in receiving timeout message.
(**No traces of DATA send found TCPDUMP**)
3. After 20 minutes, socket received ** err:110** in client socket. So, Client application tried to establish new connection with server.Which failed always
4. After performing system reboot we were able to connect with server.
5. when viewing the TCp packets we noticed **seq 1457045850:145704585** multple sequence number cases.What are all the possible reasons that it would occur</code></pre><p><strong>TCP PACKET SAMPLE WITH MULTIPLE SEQ NUMBER:</strong></p><pre><code>20:58:29.02455364, id 11796), length 64     172.11.105.5.49524 &gt; 172.250.10.10.13824: Flags [.], cksum 0x602c (correct), seq 3097912308, ack 1457045851, win 2003, options [nop,nop,TS val 73309529 ecr 646047661,nop,nop,sack 1 {1457045850:1457045851}], length 0
    0x0000:  4500 0040 049b 4000 4006 6a08 ac0b 6905  [email protected]@[email protected]
    0x0010:  acfa 0a0a c174 3600 b8a6 63f4 56d8 c15b  .....t6...c.V..[
    0x0020:  b010 07d3 602c 0000 0101 080a 045e 9d59  ....`,.......^.Y
    0x0030:  2681 e7ad 0101 050a 56d8 c15a 56d8 c15b  &amp;.......V..ZV..[
20:58:35.72482059, id 518286), length 53        172.250.10.10.13824 &gt; 172.11.105.5.49524: Flags [P.], cksum 0x0221 (correct), seq 1457045850:1457045851, ack 3097912308, win 17680, options [nop,nop,TS val 646048331 ecr 73277952], length 1
    0x0000:  4500 0035 ca74 4000 3b06 a939 acfa 0a0a  [email protected];..9....
    0x0010:  ac0b 6905 3600 c174 56d8 c15a b8a6 63f4  ..i.6..tV..Z..c.
    0x0020:  8018 4510 0221 0000 0101 080a 2681 ea4b  ..E..!......&amp;..K
    0x0030:  045e 2200 00                             .^&quot;..
20:58:49.11454159, id 518296), length 53        172.250.10.10.13824 &gt; 172.11.105.5.49524: Flags [P.], cksum 0xfce5 (correct), seq 1457045850:1457045851, ack 3097912308, win 17680, options [nop,nop,TS val 646049670 ecr 73277952], length 1
    0x0000:  4500 0035 ca75 4000 3b06 a938 acfa 0a0a  [email protected];..8....
    0x0010:  ac0b 6905 3600 c174 56d8 c15a b8a6 63f4  ..i.6..tV..Z..c.
    0x0020:  8018 4510 fce5 0000 0101 080a 2681 ef86  ..E.........&amp;...
    0x0030:  045e 2200 00                             .^&quot;..
20:59:15.87796659, id 518306), length 53        172.250.10.10.13824 &gt; 172.11.105.5.49524: Flags [P.], cksum 0xf271 (correct), seq 1457045850:1457045851, ack 3097912308, win 17680, options [nop,nop,TS val 646052346 ecr 73277952], length 1
    0x0000:  4500 0035 ca76 4000 3b06 a937 acfa 0a0a  [email protected];..7....
    0x0010:  ac0b 6905 3600 c174 56d8 c15a b8a6 63f4  ..i.6..tV..Z..c.
    0x0020:  8018 4510 f271 0000 0101 080a 2681 f9fa  ..E..q......&amp;...
    0x0030:  045e 2200 00</code></pre><p>Confused Need some pointer in further understanding.</p></div><div id="question-tags" class="tags-container tags">tcpdump tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/6ad04bff031b8e9268cd4e2e2930d182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ragav&#39;s gravatar image" /><p>Ragav<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ragav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '14, 02:39</p></div></div><div id="comments-container-37811" class="comments-container"><span id="37813"></span><div id="comment-37813" class="comment"><div id="post-37813-score" class="comment-score"></div><div class="comment-text"><p>Can you post the actual capture file at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and give us the link? Reading ASCII dumps is no fun, especially when tracking TCP behavior.</p></div><div id="comment-37813-info" class="comment-info"><span class="comment-age">(13 Nov '14, 02:46)</span> Jasper ♦♦</div></div><span id="37816"></span><div id="comment-37816" class="comment"><div id="post-37816-score" class="comment-score"></div><div class="comment-text"><p>@jaspper : The dump i have here is ascii only.i dont have pcap format i got and i have just now registered myself in cloudshark yet to rx login infos..</p></div><div id="comment-37816-info" class="comment-info"><span class="comment-age">(13 Nov '14, 03:38)</span> Ragav</div></div></div><div id="comment-tools-37811" class="comment-tools"></div><div class="clear"></div><div id="comment-37811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37879"></span>

<div id="answer-container-37879" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37879-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you are receiving are keepalive probes with one octet of garbage. Your server acks only the first one with a sack option. The subsequent keepalives seem to be ignored by your server.</p><p>There has been some discussion about RFC1122 in this forum on the topic:<br />
<a href="https://ask.wireshark.org/questions/11863/why-do-tcp-clients-send-packets-with-no-data">https://ask.wireshark.org/questions/11863/why-do-tcp-clients-send-packets-with-no-data</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-37879" class="comments-container"><span id="37888"></span><div id="comment-37888" class="comment"><div id="post-37888-score" class="comment-score"></div><div class="comment-text"><p>@mrEEde ::suddenly we noticed server has ignored responding to the probes.On what scenarios generally these happen.</p></div><div id="comment-37888-info" class="comment-info"><span class="comment-age">(16 Nov '14, 21:16)</span> Ragav</div></div></div><div id="comment-tools-37879" class="comment-tools"></div><div class="clear"></div><div id="comment-37879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

