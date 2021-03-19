+++
type = "question"
title = "Unknown RST,ACK packet causing hung connections on the client side"
description = '''We are having random connection crashes on one of the http clients (X.X.X.X) connecting to an app server (Y.Y.Y.Y). There are 2 ASA firewalls in between performing NAT. Data flow is normal for a while but suddenly it stops. Packet capture shows that from client&#x27;s perspective the connection was never...'''
date = "2013-05-13T21:07:00Z"
lastmod = "2013-05-13T22:49:00Z"
weight = 21121
keywords = [ "rst", "asa" ]
aliases = [ "/questions/21121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown RST,ACK packet causing hung connections on the client side](/questions/21121/unknown-rstack-packet-causing-hung-connections-on-the-client-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having random connection crashes on one of the http clients (X.X.X.X) connecting to an app server (Y.Y.Y.Y). There are 2 ASA firewalls in between performing NAT. Data flow is normal for a while but suddenly it stops. Packet capture shows that from client's perspective the connection was never terminated. Here is what I found so far:</p><ol><li><p>Server side capture shows that it sent a FIN,ACK packet and received a RST,ACK packet from the client. Such termination was not observed on client side.</p></li><li><p>The normal terminations in the previous successful connections were all graceful, with 4-way handshake.</p></li><li><p>Even the source IP and sequence numbers on the RST packet matches existing connections there are enough indicators showing it didn't originate from the client side:</p><ul><li><p>The TTL value is 255 whereas those coming from clients should have 125 (see packets 1 - 24)</p></li><li><p>The window size matches exactly that of the one<br />
advertized by server (65323), whereas in previous packets window size varies between 1460 and 65535.</p></li></ul><p><code>Server side capture: ip.src     tcp.flags       ip.ttl  tcp.window_size x.x.x.x    0x0002          125     65535 y.y.y.y    0x0012          128     16384 x.x.x.x    0x0010          125     1460 x.x.x.x    0x0018          125     65535 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0010          128     65323 x.x.x.x    0x0010          125     65535 y.y.y.y    0x0018          128     65323 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0010          128     65323 x.x.x.x    0x0010          125     65535 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0018          128     65323 x.x.x.x    0x0010          125     65535 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0010          128     65323 x.x.x.x    0x0010          125     65535 y.y.y.y    0x0010          128     65323 y.y.y.y    0x0018          128     65323 x.x.x.x    0x0010          125     64155 x.x.x.x    0x0010          125     65535 x.x.x.x    0x0010          125     65535 y.y.y.y    0x0011          128     65323 x.x.x.x    0x0014          255     65323</code></p></li></ol><p>Has anyone experienced this kind of mysterious RST's earlier? Is it possible that the firewall would send a RST in response to FIN, at the same time not forward it to the other host? Why is it not triggered for all connections except for few connections (a couple of hours after the app is restarted)</p></div><div id="question-tags" class="tags-container tags">rst asa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '13, 21:07</strong></p><img src="https://secure.gravatar.com/avatar/e14ca2c421c54ea693198e806821f50d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xkgt&#39;s gravatar image" /><p>xkgt<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xkgt has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-21121" class="comments-container"></div><div id="comment-tools-21121" class="comment-tools"></div><div class="clear"></div><div id="comment-21121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21123"></span>

<div id="answer-container-21123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21123-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds to me like a timeout on the session on the ASA firewall. As the ASA keeps state of each session, it also needs to manage these state records in order to not fill up the tables. This is why every firewall will have a timeout associated with each session. When a session is idle for too long, it will be removed from the session table. The timeout can be configured (either globally or port specific).</p><p>What is the time difference between the last packet of the client and the FIN packet of the server?</p><p>You can either solve this by increasing the timeout on the firewall or you can use TCP KeepAlives on the client and server to make the session on the firewall not go idle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '13, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21123" class="comments-container"><span id="21125"></span><div id="comment-21125" class="comment"><div id="post-21125-score" class="comment-score"></div><div class="comment-text"><p>That was my first suspect too, but the whole stream lasts just a couple of seconds. There is 1 second gap between the last bunch of ACK's received by the server before it decides to close the connection by sending out FIN,ACK.</p><p>Also, isn't the ASA expected to gracefully close the connection by sending out RST to both sides. It beats me why I didn't get it in client side.</p><p>And this RST doesn't happen for every connection. There were 2605 new connections made in 10 minute window, 5211 FINS (note 1 missing FIN back from client) and only 1 RST. The client side capture doesn't show RST at all.</p><p>Say the firewall does send out this RST in both directions, what happens if this packet fails to reach the client?</p><p>--edit-- Merged two comments to one</p></div><div id="comment-21125-info" class="comment-info"><span class="comment-age">(14 May '13, 01:08)</span> xkgt</div></div><span id="21127"></span><div id="comment-21127" class="comment"><div id="post-21127-score" class="comment-score"></div><div class="comment-text"><p>OK, if it is not the timeout, there must be something else "special" about this session. That would require further analysis of the whole tracefile. Are you able to share the file on www.cloudshark.org or does it contain sensitive data?</p><p>What does the firewall log say? Can you raise the logging level? Are you running the latest firmware?</p><p>When a session has timed out on the ASA and it receives a packet that matches a flushed session. It is not capable to send the client a RST as it does not know who the client is (that information was kept in the session table entry that has been flushed).</p></div><div id="comment-21127-info" class="comment-info"><span class="comment-age">(14 May '13, 01:32)</span> SYN-bit ♦♦</div></div><span id="21128"></span><div id="comment-21128" class="comment"><div id="post-21128-score" class="comment-score"></div><div class="comment-text"><p>I knew I would have to dive in to the firewall logs. I was just post-poning the inevitable looking for other answers. The firewall is maintained by a 3rd party and it doesn't even have logging configured. Need to persuade them turn on logging and setup a log server. I will post back here, if there are any findings.</p></div><div id="comment-21128-info" class="comment-info"><span class="comment-age">(14 May '13, 01:49)</span> xkgt</div></div><span id="21129"></span><div id="comment-21129" class="comment"><div id="post-21129-score" class="comment-score"></div><div class="comment-text"><p>Well, the traces should be able to tell you more as well. Can you scrub the ip addresses and payload (if necessary) and share (either public or privately, see my profile for address)?</p></div><div id="comment-21129-info" class="comment-info"><span class="comment-age">(14 May '13, 02:10)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-21123" class="comment-tools"></div><div class="clear"></div><div id="comment-21123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

