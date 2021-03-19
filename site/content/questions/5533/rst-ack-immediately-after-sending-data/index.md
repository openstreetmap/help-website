+++
type = "question"
title = "[RST, ACK] immediately after sending data?"
description = '''Hi, I&#x27;m trying to figure out a problem where I&#x27;m getting multiple socket exceptions on client machines on the network. Clients always connect to the server, send some data and the server always sends some data back to every client. I&#x27;ve run a prolonged capture and I&#x27;m seeing that when the problem oc...'''
date = "2011-08-05T10:44:00Z"
lastmod = "2011-08-07T07:10:00Z"
weight = 5533
keywords = [ "rst", "ack", "after", "data", "sent" ]
aliases = [ "/questions/5533" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\[RST, ACK\] immediately after sending data?](/questions/5533/rst-ack-immediately-after-sending-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5533-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to figure out a problem where I'm getting multiple socket exceptions on client machines on the network. Clients always connect to the server, send some data and the server always sends some data back to every client. I've run a prolonged capture and I'm seeing that when the problem occurs, the server seems to be sending the data back to the client, but almost immediately after that the server sends an RST+ACK packet, as shown below:</p><pre><code>No.     Time        Source                Destination           Protocol Length Info
  57081 0.000000    10.41.0.9             10.41.1.100           TCP      62     [TCP Port numbers reused] 1224 &gt; 1234 [SYN] Seq=0 Win=32768 Len=0 MSS=1460 SACK_PERM=1
  57082 0.000039    10.41.1.100           10.41.0.9             TCP      62     1234 &gt; 1224 [SYN, ACK] Seq=0 Ack=1 Win=16384 Len=0 MSS=1460 SACK_PERM=1
  57083 0.003693    10.41.0.9             10.41.1.100           TCP      60     1224 &gt; 1234 [ACK] Seq=1 Ack=1 Win=33580 Len=0
  57084 0.031041    10.41.0.9             10.41.1.100           TCP      135    1224 &gt; 1234 [PSH, ACK] Seq=1 Ack=1 Win=33580 Len=81
  57087 0.113171    10.41.1.100           10.41.0.9             TCP      54     1234 &gt; 1224 [ACK] Seq=1 Ack=82 Win=65454 Len=0
  57088 0.069353    10.41.1.100           10.41.0.9             TCP      74     1234 &gt; 1224 [PSH, ACK] Seq=1 Ack=82 Win=65454 Len=20
  57095 0.104433    10.41.1.100           10.41.0.9             TCP      54     1234 &gt; 1224 [RST, ACK] Seq=21 Ack=82 Win=0 Len=0</code></pre><p>A more detailed log is available under http://winger.pl/userfiles/err.txt .</p><p>Does anyone have any suggestions of to what might be causing the [RST, ACK] packets to be sent? The clients seem to be getting the RST/ACK (causing them to throw a socket exception) but I'm not sure they are getting the data. There are no firewalls or routers between the host and the client, any kind of firewall/AV software has been disabled on the system running the host application. Also, the same host application is being used on numerous other locations and I havent' seen this problem anywhere else.</p><p>Kind Regards, Winger</p></div><div id="question-tags" class="tags-container tags">rst ack after data sent</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '11, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/6b3aa429f972408b08f0e886fe6d1329?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Winger&#39;s gravatar image" /><p>Winger<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Winger has no accepted answers">0%</span></p></div></div><div id="comments-container-5533" class="comments-container"></div><div id="comment-tools-5533" class="comment-tools"></div><div class="clear"></div><div id="comment-5533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5556"></span>

<div id="answer-container-5556" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5556-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP RST packets should not be seen normally, one exception is when a Microsoft client closes an SSL session, then you might see "normal" TCP RST packets.</p><p>The fact that your first show frame (#57081) has "[TCP Port numbers reused]" in the info column means that Wireshark has seen another TCP session with the same IP-addresses and port numbers before. I think you need to focus on that. Filter on the port numbers and check how long these two (different) TCP sessions were apart, and then check whether the TIME_WAIT timer on 10.41.1.100 might be longer than that.</p><p>If so, you need to look into the amount of sessions that you need to process and tune the port range that can be used and the TCP timers accordingly (or even start using multiple IP addresses for making these connections).</p><p>It's also a good idea to compare all bad sessions with the good sessions. What do they have in common?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '11, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5556" class="comments-container"><span id="5575"></span><div id="comment-5575" class="comment"><div id="post-5575-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tips - they were helpful (especially the first sentence, as after some googling around I got a feeling that RST is pretty standard). I was able to figure out that the host app does not handle closing of the connections properly (they were closed by the clients but they lingered on from the server's perspective) - every single connection ended with RST, once this was fixed the issue has disappeared.</p></div><div id="comment-5575-info" class="comment-info"><span class="comment-age">(08 Aug '11, 09:44)</span> Winger</div></div><span id="5577"></span><div id="comment-5577" class="comment"><div id="post-5577-score" class="comment-score"></div><div class="comment-text"><p>Glad to hear you were able to solve your issue!</p></div><div id="comment-5577-info" class="comment-info"><span class="comment-age">(08 Aug '11, 10:09)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5556" class="comment-tools"></div><div class="clear"></div><div id="comment-5556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5540"></span>

<div id="answer-container-5540" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5540-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is not uncommon for servers to terminate TCP connections by sending a RST, simply because it is faster than FIN/ACK/FIN/ACK, and there is no TIME_WAIT status afterwards. So far I interpret your trace like this:</p><ul><li>Packets 57081-57083: Three Way Handshake</li><li>Packet 57084: Client requests something from the server and uses PSH to tell it to go ahead and process</li><li>Packet 57087: the server acknowledges the request, without replying with any content (len=0, so no payload in that packet)</li><li>Packet 57088: the server sends the payload, which took 0.069 seconds to generate (determinted by the delta from the acknowledge in 57087)</li><li>Packet 57095: the server closes the connection with a RST packet. Maybe because it knows that its work is done, or maybe because there was no further client request within a certain amount of time.</li></ul><p>So, keep in mind that a reset (RST) packet unfortunately doesn't mean anything went wrong. It could be a "normal" connection termination. This kind of termination is often used by Microsoft products like Internet Explorer, Outlook, Exchange Server etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5540" class="comments-container"><span id="5542"></span><div id="comment-5542" class="comment"><div id="post-5542-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks for the answer. I suppose I should have added that the server application never terminates the connection in that setup - it's always the client doing this after it receives and procesess the data; therefore, in the above example, I would have received FIN/ACK from the client (after packet 57088) and this would be followed by ACK and RST/ACK sent back to the client. The code of the server application simply doesn't perform the closing of the connection. Hence, I'm puzzled why this is occuring and I'm trying to understand the reasons behind it.</p><p>The problem only occurs for approx. 5% of all the transactions taking place.</p><p>Kind Regards, Winger</p></div><div id="comment-5542-info" class="comment-info"><span class="comment-age">(06 Aug '11, 03:31)</span> Winger</div></div><span id="5555"></span><div id="comment-5555" class="comment"><div id="post-5555-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ)</p></div><div id="comment-5555-info" class="comment-info"><span class="comment-age">(07 Aug '11, 06:58)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5540" class="comment-tools"></div><div class="clear"></div><div id="comment-5540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

