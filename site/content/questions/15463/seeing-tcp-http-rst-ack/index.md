+++
type = "question"
title = "Seeing TCP http [RST, ACK]"
description = '''I am analyzing throughput on a network and am running an HTTP GET file of 400MB from one of our servers. The TCP connection appears to get set up correctly, but part way through, I am seeing a RST,ACK followed by &#x27;Continuation or non-HTTP traffic&#x27; entries. These continuation packets just end after a...'''
date = "2012-11-01T06:27:00Z"
lastmod = "2012-11-01T06:27:00Z"
weight = 15463
keywords = [ "rst", "ack", "rmpp" ]
aliases = [ "/questions/15463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing TCP http \[RST, ACK\]](/questions/15463/seeing-tcp-http-rst-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15463-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing throughput on a network and am running an HTTP GET file of 400MB from one of our servers. The TCP connection appears to get set up correctly, but part way through, I am seeing a RST,ACK followed by 'Continuation or non-HTTP traffic' entries. These continuation packets just end after a bunch of them with no ACKS from the other end and no apparent termination of the TCP connection following the continuation packets. Am I correct in assuming that the TCP connection ends with the RST, ACK? If so, why does the other end keep sending the continuation packets? The client I'm using is the 10.x.x.x address, the server is the 69.x.x.x address. Any help is appreciated. Thanks.</p><pre><code>Number  Time    Source  Destination Protocol    Length  Info
21  37:25.6 10.161.62.101   69.147.163.122  HTTP    225 GET /400MB.zip HTTP/1.0 
22  37:25.7 69.147.163.122  10.161.62.101   TCP 54  http &gt; rmpp [ACK] Seq=1 Ack=172 Win=7168 Len=0
23  37:25.7 69.147.163.122  10.161.62.101   HTTP    1444    HTTP/1.0 200 OK  (application/zip)[Packet size limited during capture]
24  37:25.7 69.147.163.122  10.161.62.101   HTTP    147 Continuation or non-HTTP traffic
25  37:25.7 10.161.62.101   69.147.163.122  TCP 54  rmpp &gt; http [ACK] Seq=172 Ack=1484 Win=128480 Len=0
26  37:25.7 69.147.163.122  10.161.62.101   HTTP    1444    Continuation or non-HTTP traffic[Packet size limited during capture]
:
:
39504   37:50.3 10.161.62.101   69.147.163.122  TCP 54  rmpp &gt; http [RST, ACK] Seq=173 Ack=33001474 Win=0 Len=0
39505   37:50.3 69.147.163.122  10.161.62.101   HTTP    1444    Continuation or non-HTTP traffic[Packet size limited during capture]
39506   37:50.3 69.147.163.122  10.161.62.101   HTTP    1444    Continuation or non-HTTP traffic[Packet size limited during capture]
:
:
39584   37:50.4 69.147.163.122  10.161.62.101   HTTP    1444    Continuation or non-HTTP traffic[Packet size limited during capture]
39585   37:52.3 10.161.62.101   69.147.163.1    ICMP    74  Echo (ping) request  id=0x0300, seq=8192/32, ttl=128</code></pre></div><div id="question-tags" class="tags-container tags">rst ack rmpp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '12, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/672a28884c09910274400dd6d2c8671e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="integratech&#39;s gravatar image" /><p>integratech<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="integratech has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Nov '12, 06:39</p></div></div><div id="comments-container-15463" class="comments-container"><span id="15464"></span><div id="comment-15464" class="comment"><div id="post-15464-score" class="comment-score"></div><div class="comment-text"><p>Guessing from the filename you are probably trying to download a 400 MB file.</p><p>Frame 39504 shows your RESET coming from your client. The ACK-no indicates that approx. 33 MByte were successfully transfered.</p><p>The interesting question is: What happened before the RST?</p><p>Can you publish the packets before 39504, preferably showing SEQ- and ACK-numbers?</p></div><div id="comment-15464-info" class="comment-info"><span class="comment-age">(01 Nov '12, 06:41)</span> packethunter</div></div><span id="15470"></span><div id="comment-15470" class="comment"><div id="post-15470-score" class="comment-score"></div><div class="comment-text"><p>packethunter...I can't paste here and have it format correctly. Anyway, at a point around lines 20000 I see a slew of about 150 DUP ACKs, some TCP Window Update packets, and a TCP Fast Retransmission. Then the sequence of download begins again with packets sent and an ACK. Then out of the blue the RST happens, and then there are just Continuation packets for a while, then they just stop.</p></div><div id="comment-15470-info" class="comment-info"><span class="comment-age">(01 Nov '12, 07:52)</span> integratech</div></div><span id="15472"></span><div id="comment-15472" class="comment"><div id="post-15472-score" class="comment-score"></div><div class="comment-text"><p>How about putting the trace up at <a href="http://www.cloudshark.org">www.cloudshark.org</a>? Please only do that if it does not contain sensitive data, because anyone can look at it.</p></div><div id="comment-15472-info" class="comment-info"><span class="comment-age">(01 Nov '12, 08:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-15463" class="comment-tools"></div><div class="clear"></div><div id="comment-15463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

