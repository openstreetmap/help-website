+++
type = "question"
title = "receiving FIN,ACK late"
description = '''We are having a problem with our network traffic where our firewall is dropping a huge number of packets suddenly (our ISP changed network equipment at the same time as us, by an unfortunate coincidence).  We&#x27;re trying to isolate the problem: We did an experiment where we made a request from within ...'''
date = "2014-04-30T10:30:00Z"
lastmod = "2014-04-30T10:54:00Z"
weight = 32316
keywords = [ "ack", "traffic-analysis", "fin", "analysis" ]
aliases = [ "/questions/32316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [receiving FIN,ACK late](/questions/32316/receiving-finack-late)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32316-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having a problem with our network traffic where our firewall is dropping a huge number of packets suddenly (our ISP changed network equipment at the same time as us, by an unfortunate coincidence).</p><p>We're trying to isolate the problem: We did an experiment where we made a request from within the firewall with Wireshark running on one machine, and outside the firewall with Wireshark running and tried to find exactly what packet was being rejected.</p><p>We seem to have reconstructed this chain of events - internal machine initiates communication with server on the Internet. The two servers communicate, conversation complete, everything is allowed via inbound-&gt;outbound firewall policy. After the end of the conversation, the Internet server sends one more packet (a FIN,ACK) and the firewall rejects this as part of the outbound-&gt;inbound firewall policy (since it doesn't recognize the connection any longer as an inbound-&gt;outbound)</p><p>My question is, am I misinterpreting these results? Is it normal for a FIN,ACK to be a response to a RST,ACK? Attached is a packet capture isolated to the specific exchange.</p><p><code> No.     Time        Source                New Column Destination           New Column Protocol Length Info                                                            New Column       1 0.000000    209.251.44.179        25452      74.125.228.74         443        TCP      66     25452 &gt; https [SYN] Seq=0 Win=8192 Len=0 MSS=1380 WS=256 SACK_PERM=1 1       2 0.006201    74.125.228.74         443        209.251.44.179        25452      TCP      66     https &gt; 25452 [SYN, ACK] Seq=0 Ack=1 Win=42900 Len=0 MSS=1430 SACK_PERM=1 WS=64 2       3 0.007895    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [ACK] Seq=1 Ack=1 Win=66048 Len=0                 3       4 0.010897    209.251.44.179        25452      74.125.228.74         443        TLSv1.2  278    Client Hello                                                    4       5 0.016407    74.125.228.74         443        209.251.44.179        25452      TCP      60     https &gt; 25452 [ACK] Seq=1 Ack=225 Win=42880 Len=0               5       6 0.017638    74.125.228.74         443        209.251.44.179        25452      TLSv1.2  1434   Server Hello                                                    6       7 0.017815    74.125.228.74         443        209.251.44.179        25452      TCP      1434   [TCP segment of a reassembled PDU]                              7       8 0.017836    74.125.228.74         443        209.251.44.179        25452      TLSv1.2  872    Certificate                                                     8       9 0.021839    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [ACK] Seq=225 Ack=2761 Win=66048 Len=0            9      10 0.030446    209.251.44.179        25452      74.125.228.74         443        TLSv1.2  316    Client Key Exchange, Change Cipher Spec, Hello Request, Hello Request 10      11 0.038621    74.125.228.74         443        209.251.44.179        25452      TLSv1.2  348    New Session Ticket, Change Cipher Spec, Hello Request, Hello Request 11      12 0.038840    74.125.228.74         443        209.251.44.179        25452      TLSv1.2  111    Application Data                                                12      13 0.038849    74.125.228.74         443        209.251.44.179        25452      TLSv1.2  99     Application Data                                                13      14 0.127251    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [ACK] Seq=487 Ack=3930 Win=65024 Len=0            14      15 0.320594    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [ACK] Seq=487 Ack=3975 Win=65024 Len=0            15      16 7.905897    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [FIN, ACK] Seq=487 Ack=3975 Win=65024 Len=0       16      17 7.905903    209.251.44.179        25452      74.125.228.74         443        TCP      60     25452 &gt; https [RST, ACK] Seq=488 Ack=3975 Win=0 Len=0           17      18 7.910928    74.125.228.74         443        209.251.44.179        25452      TCP      60     https &gt; 25452 [FIN, ACK] Seq=3975 Ack=488 Win=42880 Len=0       18</code></code></p></div><div id="question-tags" class="tags-container tags">ack traffic-analysis fin analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/ed8d06b2959d738b81ff7994c9e86716?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amallah&#39;s gravatar image" /><p>amallah<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amallah has no accepted answers">0%</span></p></div></div><div id="comments-container-32316" class="comments-container"></div><div id="comment-tools-32316" class="comment-tools"></div><div class="clear"></div><div id="comment-32316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32317"></span>

<div id="answer-container-32317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32317-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A reset flag must not be answered, which is a rule in place to prevent two systems telling each other to "shut up" over and over again. So no, it would be illegal to send a FIN as an answer to a reset, but I doubt that is what is happening. I guess the FIN is the answer to the other FIN, and it's just coming in late due to the RTT. You can usually verify this on the side that sends the final FIN - it will most likely not yet have seen the RST when it sent it. It's a little hard to tell without having a real trace and just looking at an ASCII dump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32317" class="comments-container"><span id="32318"></span><div id="comment-32318" class="comment"><div id="post-32318-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. Does this help? <a href="https://webbmason.sharefile.com/d/s9ba2db79c1c499ca">https://webbmason.sharefile.com/d/s9ba2db79c1c499ca</a></p></div><div id="comment-32318-info" class="comment-info"><span class="comment-age">(30 Apr '14, 11:06)</span> amallah</div></div><span id="32320"></span><div id="comment-32320" class="comment"><div id="post-32320-score" class="comment-score"></div><div class="comment-text"><p>The inside_capture.pcapng shows it: the RST in frame 17 is sent 65 microseconds after the FIN is sent in frame 16, which is really really impatient.</p><p>I can only guess that the application closed the TCP socket without waiting for the graceful shutdown being complete (meaning, waiting for a FIN answering the FIN being sent), and so a RST is sent.</p><p>The FIN from the other node arrives shortly after in frame 18 as seen in outside_capture.pcap, probably before the sender knew there was a RST coming in soon after.</p><p>For me the interesting thing is why the IP 192.168.193.215 sends a FIN and then a RST right away - I would investigate this further, but that has to be done on the OS and application side of that station.</p></div><div id="comment-32320-info" class="comment-info"><span class="comment-age">(30 Apr '14, 11:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32317" class="comment-tools"></div><div class="clear"></div><div id="comment-32317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

