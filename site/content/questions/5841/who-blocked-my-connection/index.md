+++
type = "question"
title = "who blocked my connection???"
description = '''when i try to connect via VNC i see the next log, can you help me i need to find who is been blocked my connection No. Time Source Destination Protocol Info  51 477.905684 10.206.96.8 10.206.80.103 TCP xmapi &amp;gt; esmmanager [SYN] Seq=0 Win=16384 Len=0 MSS=1024 WS=0 TSV=4798594 TSER=0 Frame 51: 74 by...'''
date = "2011-08-24T07:45:00Z"
lastmod = "2011-08-24T08:02:00Z"
weight = 5841
keywords = [ "rst" ]
aliases = [ "/questions/5841" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [who blocked my connection???](/questions/5841/who-blocked-my-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5841-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i try to connect via VNC i see the next log, can you help me i need to find who is been blocked my connection</p><p>No. Time Source Destination Protocol Info 51 477.905684 10.206.96.8 10.206.80.103 TCP xmapi &gt; esmmanager [SYN] Seq=0 Win=16384 Len=0 MSS=1024 WS=0 TSV=4798594 TSER=0</p><p>Frame 51: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) Ethernet II, Src: 63:30:00:00:00:00 (63:30:00:00:00:00), Dst: 6f:31:65:74:68:31 (6f:31:65:74:68:31) Internet Protocol, Src: 10.206.96.8 (10.206.96.8), Dst: 10.206.80.103 (10.206.80.103) Version: 4 Header length: 20 bytes Differentiated Services Field: 0x10 (DSCP 0x04: Unknown DSCP; ECN: 0x00) Total Length: 60 Identification: 0x4abd (19133) Flags: 0x00 Fragment offset: 0 Time to live: 64 Protocol: TCP (6) Header checksum: 0x0028 [incorrect, should be 0x69e4] Source: 10.206.96.8 (10.206.96.8) Destination: 10.206.80.103 (10.206.80.103) Transmission Control Protocol, Src Port: xmapi (1933), Dst Port: esmmanager (5600), Seq: 0, Len: 0</p><p>No. Time Source Destination Protocol Info 52 477.905983 10.206.96.8 10.206.80.103 TCP xmapi &gt; esmmanager [SYN] Seq=0 Win=16384 Len=0 MSS=1024 WS=0 TSV=4798594 TSER=0</p><p>Frame 52: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) Ethernet II, Src: 63:30:00:00:00:00 (63:30:00:00:00:00), Dst: 4f:63:65:74:68:31 (4f:63:65:74:68:31) Internet Protocol, Src: 10.206.96.8 (10.206.96.8), Dst: 10.206.80.103 (10.206.80.103) Version: 4 Header length: 20 bytes Differentiated Services Field: 0x10 (DSCP 0x04: Unknown DSCP; ECN: 0x00) Total Length: 60 Identification: 0x4abd (19133) Flags: 0x00 Fragment offset: 0 Time to live: 64 Protocol: TCP (6) Header checksum: 0x0028 [incorrect, should be 0x69e4] Source: 10.206.96.8 (10.206.96.8) Destination: 10.206.80.103 (10.206.80.103) Transmission Control Protocol, Src Port: xmapi (1933), Dst Port: esmmanager (5600), Seq: 0, Len: 0</p><p>No. Time Source Destination Protocol Info 53 477.950840 10.206.80.103 10.206.96.8 TCP esmmanager &gt; xmapi [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</p><p>Frame 53: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) Ethernet II, Src: 63:30:00:00:00:00 (63:30:00:00:00:00), Dst: 69:32:65:74:68:31 (69:32:65:74:68:31) Internet Protocol, Src: 10.206.80.103 (10.206.80.103), Dst: 10.206.96.8 (10.206.96.8) Version: 4 Header length: 20 bytes Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00) Total Length: 40 Identification: 0x8e1a (36378) Flags: 0x00 Fragment offset: 0 Time to live: 125 Protocol: TCP (6) Header checksum: 0xe9aa [correct] Source: 10.206.80.103 (10.206.80.103) Destination: 10.206.96.8 (10.206.96.8) Transmission Control Protocol, Src Port: esmmanager (5600), Dst Port: xmapi (1933), Seq: 1, Ack: 1, Len: 0</p><p>No. Time Source Destination Protocol Info 54 477.950885 10.206.80.103 10.206.96.8 TCP esmmanager &gt; xmapi [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</p><p>Frame 54: 54 bytes on wire (432 bits), 54 bytes captured (432 bits) Ethernet II, Src: 63:30:00:00:00:00 (63:30:00:00:00:00), Dst: 49:63:65:74:68:31 (49:63:65:74:68:31) Internet Protocol, Src: 10.206.80.103 (10.206.80.103), Dst: 10.206.96.8 (10.206.96.8) Version: 4 Header length: 20 bytes Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00) Total Length: 40 Identification: 0x8e1a (36378) Flags: 0x00 Fragment offset: 0 Time to live: 125 Protocol: TCP (6) Header checksum: 0xe9aa [correct] Source: 10.206.80.103 (10.206.80.103) Destination: 10.206.96.8 (10.206.96.8) Transmission Control Protocol, Src Port: esmmanager (5600), Dst Port: xmapi (1933), Seq: 1, Ack: 1, Len: 0</p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '11, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/188575f0aa0ccc42abda8e5b518560fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ds_ds&#39;s gravatar image" /><p>ds_ds<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ds_ds has no accepted answers">0%</span></p></div></div><div id="comments-container-5841" class="comments-container"></div><div id="comment-tools-5841" class="comment-tools"></div><div class="clear"></div><div id="comment-5841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5843"></span>

<div id="answer-container-5843" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5843-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the system you want to VNC to does not have the VNC port open or maybe it has some host based firewall rules that are blocking your connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5843" class="comments-container"><span id="5958"></span><div id="comment-5958" class="comment"><div id="post-5958-score" class="comment-score"></div><div class="comment-text"><p>hi Synbit</p><p>the server have a vnc open if i make a test from net lan the connection is OK, i have the problem when my connection go across the firewell.</p><p>i review the firewall rules and i dont see a problem, i i make a tcpdump in firewall i see all connection accept.</p><p>do you have any idea??</p></div><div id="comment-5958-info" class="comment-info"><span class="comment-age">(30 Aug '11, 08:24)</span> ds_ds</div></div><span id="5960"></span><div id="comment-5960" class="comment"><div id="post-5960-score" class="comment-score"></div><div class="comment-text"><p>Did you also check the host based firewall rules on the server (iptables or similar)?</p></div><div id="comment-5960-info" class="comment-info"><span class="comment-age">(30 Aug '11, 08:45)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5843" class="comment-tools"></div><div class="clear"></div><div id="comment-5843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

