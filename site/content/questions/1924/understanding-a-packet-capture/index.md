+++
type = "question"
title = "Understanding a Packet Capture"
description = '''I am new to Wireshark and have created a packet capture between two servers, one within the LAN and the other in our DMZ. The program tells me it uses port 8004, which I have opened up on our firewall. From what I see in the catpure, it looks like it&#x27;s using 8004 but routing it to another port? Any ...'''
date = "2011-01-25T07:39:00Z"
lastmod = "2012-10-17T19:03:00Z"
weight = 1924
keywords = [ "capture" ]
aliases = [ "/questions/1924" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding a Packet Capture](/questions/1924/understanding-a-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1924-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark and have created a packet capture between two servers, one within the LAN and the other in our DMZ. The program tells me it uses port 8004, which I have opened up on our firewall. From what I see in the catpure, it looks like it's using 8004 but routing it to another port? Any help reading this would be great ... Here is a portion of my capture.</p><pre><code>192.168.1.23    192.168.3.10    TCP 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=4006900096 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=660724035 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60177 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60177 [RST, ACK] Seq=1 Ack=587607840 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=1954781099 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=939193442 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60178 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60178 [RST, ACK] Seq=1 Ack=1625215588 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP 60179 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60179 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60179 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60179 [RST, ACK] Seq=1 Ack=2224311254 Win=0 Len=0    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60179 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.1.23    192.168.3.10    TCP [TCP Port numbers reused] 60179 &gt; 8004 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=8 SACK_PERM=1    
192.168.3.10    192.168.1.23    TCP 8004 &gt; 60179 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0    
192.168.3.10    192.168.1.23    TCP [TCP ACKed lost segment] 8004 &gt; 60179 [RST, ACK] Seq=1 Ack=45320348 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/5dfec6cdb80dedf2a428145a81bc1808?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HSD&#39;s gravatar image" /><p>HSD<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HSD has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 May '13, 01:33</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-1924" class="comments-container"><span id="7097"></span><div id="comment-7097" class="comment"><div id="post-7097-score" class="comment-score"></div><div class="comment-text"><p>I'm getting the same kind of error except; in my case a port which is closed is quickly (5 seconds later) being reused.<br />
</p><p>Example: TCP-PORT=545454 -&gt; do a TCP session on port=545454 SYN/SYN-ACK/SYN/SYN-ACK/DATA/FIN-ACK/ACK/FIN-ACK/ACK wait 5 seconds -&gt; do a TCP session on port=545454 SYN SEQNUM=0 -&gt; ACK SEQNUM=0 ACKNUM=1507571667</p><p>This causes a RST to be triggered. There seems to be a link as if the second TCP session is being "fudged" with a bad ACKNUM.</p></div><div id="comment-7097-info" class="comment-info"><span class="comment-age">(27 Oct '11, 08:05)</span> grandman</div></div><span id="21124"></span><div id="comment-21124" class="comment"><div id="post-21124-score" class="comment-score"></div><div class="comment-text"><p>You can't reuse a connection tuple (src_ip,src_port, dst_ip, dst_port, protocol) within 5 seconds. The server normally waits for 2xMSL seconds before tearing down a connection. If any new connection request comes on the same tuple, it will send out a RST packet (There are exceptions though, see TIME-WAIT assassination)</p></div><div id="comment-21124-info" class="comment-info"><span class="comment-age">(14 May '13, 00:38)</span> xkgt</div></div></div><div id="comment-tools-1924" class="comment-tools"></div><div class="clear"></div><div id="comment-1924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1926"></span>

<div id="answer-container-1926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1926-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The server is on port 8004. The client also has a port. So if the communication is going from client to server, the first example is:</p><p>60177 &gt; 8004 (TCP Source Port 60177, TCP Destination 8004)</p><p>When the server responds to the clinet</p><p>8004 &gt; 60177 (TCP Source Port 8004, TCP Destination 60177)</p><p>Later on you will see other source/destination combination for subsequent TCP sessions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-1926" class="comments-container"></div><div id="comment-tools-1926" class="comment-tools"></div><div class="clear"></div><div id="comment-1926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1928"></span>

<div id="answer-container-1928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1928-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a typical case of "client wants to talk to a server port that isn't listened on or blocked by a firewall reject rule". Your client repeatedly sends a SYN to port 8004 and gets a RST back, which means that the server or a device in between refused the connection.</p><p>Things to check:</p><ol><li>On the server: is there a program/service running that is offering services on port 8004? You can check using the netstat command on the command line if the port is listened on.</li><li>If there is a service running you might have a problem with a firewall or other ACL device. Check your network path between client and server for such devices and their rule sets.</li></ol><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1928" class="comments-container"></div><div id="comment-tools-1928" class="comment-tools"></div><div class="clear"></div><div id="comment-1928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15068"></span>

<div id="answer-container-15068" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15068-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There seems to be another active TCB with src port 60177 and dst port 8004, so wireshark is pumping message that TCP ports are reused. It is not easy to identify the cause unless you look at the whole packet capture since beginning of time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/e14ca2c421c54ea693198e806821f50d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xkgt&#39;s gravatar image" /><p>xkgt<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xkgt has no accepted answers">0%</span></p></div></div><div id="comments-container-15068" class="comments-container"></div><div id="comment-tools-15068" class="comment-tools"></div><div class="clear"></div><div id="comment-15068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

