+++
type = "question"
title = "TCP SYN Flood interpretation"
description = '''I am trying to interpret a packet capture. I am thinking it is a SYN flood to the same ip address. It looks like it cannot do the 3 way TCP handshake. How do you interpret it? I am not sure how to upload the capture file.  42 1.280976 172.17.4.95 172.17.4.95 TCP 58 37176 → 111 [SYN] Seq=0 Win=1024 L...'''
date = "2016-07-14T08:29:00Z"
lastmod = "2016-07-19T13:15:00Z"
weight = 54065
keywords = [ "syn-flood", "tcp" ]
aliases = [ "/questions/54065" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP SYN Flood interpretation](/questions/54065/tcp-syn-flood-interpretation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to interpret a packet capture. I am thinking it is a SYN flood to the same ip address. It looks like it cannot do the 3 way TCP handshake. How do you interpret it? I am not sure how to upload the capture file.<br />
</p><pre><code>42  1.280976    172.17.4.95 172.17.4.95 TCP 58  37176 → 111 [SYN] Seq=0 Win=1024 Len=0 MSS=1460
43  1.281072    172.17.4.95 172.17.4.95 TCP 58  111 → 37176 [SYN, ACK] Seq=0 Ack=1 Win=32792 Len=0 MSS=16396
44  1.281086    172.17.4.95 172.17.4.95 TCP 54  37176 → 111 [RST] Seq=1 Win=0 Len=0
45  1.281184    172.17.4.95 172.17.4.95 TCP 58  37176 → 135 [SYN] Seq=0 Win=1024 Len=0 MSS=1460
46  1.281190    172.17.4.95 172.17.4.95 TCP 54  135 → 37176 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">syn-flood tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '16, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/8708ece227a348574aabea520e36396c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dblackwell&#39;s gravatar image" /><p>dblackwell<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dblackwell has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '16, 08:32</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54065" class="comments-container"><span id="54066"></span><div id="comment-54066" class="comment"><div id="post-54066-score" class="comment-score"></div><div class="comment-text"><p>You can share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc. and then edit the question with a link to the capture file.</p></div><div id="comment-54066-info" class="comment-info"><span class="comment-age">(14 Jul '16, 08:33)</span> grahamb ♦</div></div></div><div id="comment-tools-54065" class="comment-tools"></div><div class="clear"></div><div id="comment-54065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54171"></span>

<div id="answer-container-54171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54171-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hard to say without more knowledge about your architecture and more of the PCAP to look at....same IPs for client/server is definitely misleading.</p><p>A SYN flood typically appears as many IPs (DDOS) sending a SYN to the server or one IP using it's range of port numbers (0 to 65535) to send SYNs to the server. Since 172.17.4.95:37176 sent the SYN and then responded to the SYN,ACK with a RST, that would not be the behavior expected of an attacker SYN flooding a server. The attacker would want to initiate a bunch of half-open connections, not RST them and allow the resources to be reallocated.</p><p>Also, see <a href="https://ask.wireshark.org/answer_link/3290/">https://ask.wireshark.org/answer_link/3290/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-54171" class="comments-container"><span id="54172"></span><div id="comment-54172" class="comment"><div id="post-54172-score" class="comment-score"></div><div class="comment-text"><p>I was waiting for the capture file, but agreed.</p><p>From the limited trace availability I'd guess this is a port scan (e.g., from nmap) not a SYN flood.</p></div><div id="comment-54172-info" class="comment-info"><span class="comment-age">(19 Jul '16, 13:39)</span> JeffMorriss ♦</div></div><span id="54173"></span><div id="comment-54173" class="comment"><div id="post-54173-score" class="comment-score"></div><div class="comment-text"><p>I'm missing one point in this explanation - if it was a port scan, the scanner should be interested in the answers, so it probably wouldn't use the target address as forged source one?</p><p>So either the port scanner is really a remotely controlled malware running on the same machine, but then it would be quite stupid to reveal itself by scanning the ports on the same machine where it is running, or the packets actually come from outside and use the address of the destination as source, but in such case their sender cannot ever get the responses.</p><p>So I'd be interested in the source mac address of the SYN packets.</p></div><div id="comment-54173-info" class="comment-info"><span class="comment-age">(19 Jul '16, 13:58)</span> sindy</div></div><span id="54231"></span><div id="comment-54231" class="comment"><div id="post-54231-score" class="comment-score"></div><div class="comment-text"><p>Oh, my thought was it was just an intentional port scan being run on the local machine. But I guess it's true that the RST in frame 44 could just as well be because the SYN,ACK in frame 43 was unexpected (out of the blue). Too bad I don't think TCP tells you why the RST was sent; in SCTP the ABORTs tell you when they're because an OOTB packet was received.</p></div><div id="comment-54231-info" class="comment-info"><span class="comment-age">(21 Jul '16, 19:03)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-54171" class="comment-tools"></div><div class="clear"></div><div id="comment-54171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

