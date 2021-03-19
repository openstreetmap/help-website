+++
type = "question"
title = "TCP DUP causing software to crash?"
description = '''Hello, im currently running into the following problem: http://abload.de/image.php?img=60-er-jahre-russische2yxhd.jpg This shows the communication between a client and server application on Port 17001. The problem is that the Client will timeout / lose the connection to server and has to be restarte...'''
date = "2017-01-19T13:11:00Z"
lastmod = "2017-01-20T02:16:00Z"
weight = 58894
keywords = [ "dup", "ack", "tcp", "rst" ]
aliases = [ "/questions/58894" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP DUP causing software to crash?](/questions/58894/tcp-dup-causing-software-to-crash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, im currently running into the following problem:</p><p><a href="http://abload.de/image.php?img=60-er-jahre-russische2yxhd.jpg">http://abload.de/image.php?img=60-er-jahre-russische2yxhd.jpg</a></p><p>This shows the communication between a client and server application on Port 17001. The problem is that the Client will timeout / lose the connection to server and has to be restarted to be working properly again.</p><p>This communcation is over an IPSEC-VPN.</p><p>I've captured the traffic and i can see that the Client seends a whole lot of TCP DUP ACK followed by RST in answer to Retransmission.</p><p>Could the cause of the aborts lie in the TCP DUP ACKS?</p></div><div id="question-tags" class="tags-container tags">dup ack tcp rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '17, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/8ec55f5a602ba4cd12beee04f6f8140a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doktorake&#39;s gravatar image" /><p>doktorake<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doktorake has no accepted answers">0%</span></p></div></div><div id="comments-container-58894" class="comments-container"><span id="58895"></span><div id="comment-58895" class="comment"><div id="post-58895-score" class="comment-score"></div><div class="comment-text"><p>If possible, please provide a capture file. It's just no fun trying to figure things out from a messy screenshot.</p><p>Check out this blog post: <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-58895-info" class="comment-info"><span class="comment-age">(19 Jan '17, 13:36)</span> Jasper ♦♦</div></div><span id="58898"></span><div id="comment-58898" class="comment"><div id="post-58898-score" class="comment-score"></div><div class="comment-text"><p>Thank for the input. I dont know where i should upload the pcap, so i uploaded it at: <a href="https://ufile.io/5b3ee">https://ufile.io/5b3ee</a></p><p>Hope that is ok.</p></div><div id="comment-58898-info" class="comment-info"><span class="comment-age">(19 Jan '17, 15:42)</span> doktorake</div></div></div><div id="comment-tools-58894" class="comment-tools"></div><div class="clear"></div><div id="comment-58894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58899"></span>

<div id="answer-container-58899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58899-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP DUP ACKs are not the problem, they are just an indicator for packet loss. The interesting thing in this case is that (looking at TCP stream #3, filter on it by using "tcp.stream==3") the connection is torn down before the data transfer is complete.</p><p>There is in fact packet loss which is signaled by the receiver, and when the sender starts resolving it using retransmissions it looks like a normal recovery at first. But then the receiver suddenly sends a FIN in packet 3179 (even though it didn't yet receive all missing packets), which is technically not incorrect as it means "hey, I'm done sending" - but then it also sends a reset in 3181, which means "stop immediately, abort abort abort". Keep in mind that at this point in time, packets are still missing, as can be seen in the SACK option of the FIN packet.</p><p>So it looks to me like the client giving up and aborting the connection here instead of patiently waiting for the missing packets to be retransmitted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '17, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58899" class="comments-container"><span id="58911"></span><div id="comment-58911" class="comment"><div id="post-58911-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the INPUT.</p><p>As the communication goes trough a VPN tunnel with the Server sides being an external DMZ IP and the client IP being internal, could it be possible that the VPN-Tunnel starts to rebuild (cause of expiring SA or smth other) causing a few packets being and the client starting to go via WAN ( as the port is reachable) and then RST the servers answer via the tunnel (once it starts working again).</p><p>But im guessing its just inside the application how it reacts to packetloss....</p></div><div id="comment-58911-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:01)</span> doktorake</div></div><span id="58913"></span><div id="comment-58913" class="comment"><div id="post-58913-score" class="comment-score">1</div><div class="comment-text"><p>It's the clients fault here, because it doesn't show enough patience to receive the remaining retransmissions as far as I can tell. So I doubt its a tunnel problem.</p></div><div id="comment-58913-info" class="comment-info"><span class="comment-age">(20 Jan '17, 07:04)</span> Jasper ♦♦</div></div><span id="58974"></span><div id="comment-58974" class="comment"><div id="post-58974-score" class="comment-score"></div><div class="comment-text"><p>I've could reproduce the error with a different pcap outcome.</p><p><a href="https://ufile.io/c7fe0">https://ufile.io/c7fe0</a></p><p>This time the client answers with RST,ACK. Is this any different now?</p></div><div id="comment-58974-info" class="comment-info"><span class="comment-age">(23 Jan '17, 04:27)</span> doktorake</div></div><span id="58976"></span><div id="comment-58976" class="comment"><div id="post-58976-score" class="comment-score"></div><div class="comment-text"><p>i didnt notice the huge timegap between data and RST.</p><p>As there is a 30minute gap, i suppose its just a timeout on the application side.</p></div><div id="comment-58976-info" class="comment-info"><span class="comment-age">(23 Jan '17, 05:28)</span> doktorake</div></div><span id="58977"></span><div id="comment-58977" class="comment"><div id="post-58977-score" class="comment-score"></div><div class="comment-text"><p>Yes, very likely... RST with an ACK is often a non-critical connection abort. Meaning: it's used instead of FIN/ACK FIN/ACK because its faster and needs less ressources. And with a long timeout like that, the connection is most likely just shut down due to inactivity.</p></div><div id="comment-58977-info" class="comment-info"><span class="comment-age">(23 Jan '17, 05:33)</span> Jasper ♦♦</div></div></div><div id="comment-tools-58899" class="comment-tools"></div><div class="clear"></div><div id="comment-58899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

