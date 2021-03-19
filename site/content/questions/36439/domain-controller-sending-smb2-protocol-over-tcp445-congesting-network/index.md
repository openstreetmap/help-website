+++
type = "question"
title = "Domain controller sending SMB2 protocol over TCP445 congesting network"
description = '''We have a Windows 2008R2 domain controller sending excess traffic to another win2008R2 domain controller and has been persistent for 2 weeks. Wireshark captured SMB2 protocol over TCP445 to the other DC. But we are unable to identify what is replicating, or file transferring. Appreciate anyone who c...'''
date = "2014-09-19T03:13:00Z"
lastmod = "2014-09-19T14:38:00Z"
weight = 36439
keywords = [ "smb2" ]
aliases = [ "/questions/36439" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Domain controller sending SMB2 protocol over TCP445 congesting network](/questions/36439/domain-controller-sending-smb2-protocol-over-tcp445-congesting-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36439-score" class="post-score" title="current number of votes">0</div><span id="post-36439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a Windows 2008R2 domain controller sending excess traffic to another win2008R2 domain controller and has been persistent for 2 weeks. Wireshark captured SMB2 protocol over TCP445 to the other DC. But we are unable to identify what is replicating, or file transferring. Appreciate anyone who can dissect the information below.</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
      5 0.002933000    10.101.23.250         172.16.10.3           SMB2     4418   Read Response

Frame 5: 4418 bytes on wire (35344 bits), 4418 bytes captured (35344 bits) on interface 0
Ethernet II, Src: 00:1a:64:25:9b:9e (00:1a:64:25:9b:9e), Dst: b8:af:67:ee:51:45 (b8:af:67:ee:51:45)
Internet Protocol Version 4, Src: 10.101.23.250 (10.101.23.250), Dst: 172.16.10.3 (172.16.10.3)
Transmission Control Protocol, Src Port: 445 (445), Dst Port: 65495 (65495), Seq: 4397, Ack: 118, Len: 4364
NetBIOS Session Service
SMB2 (Server Message Block Protocol version 2)

No.     Time           Source                Destination           Protocol Length Info
      6 0.003496000    10.101.23.250         172.16.10.2           DCERPC   4450   Response: call_id: 4825142, Fragment: 1st, Ctx: 0

Frame 6: 4450 bytes on wire (35600 bits), 4450 bytes captured (35600 bits) on interface 0
Ethernet II, Src: 00:1a:64:25:9b:9e (00:1a:64:25:9b:9e), Dst: b8:af:67:ee:51:45 (b8:af:67:ee:51:45)
Internet Protocol Version 4, Src: 10.101.23.250 (10.101.23.250), Dst: 172.16.10.2 (172.16.10.2)
Transmission Control Protocol, Src Port: 445 (445), Dst Port: 63940 (63940), Seq: 1, Ack: 1, Len: 4396
NetBIOS Session Service
SMB2 (Server Message Block Protocol version 2)
Distributed Computing Environment / Remote Procedure Call (DCE/RPC) Response, Fragment: 1st, FragLen: 4280, Call: 4825142, Ctx: 0

No.     Time           Source                Destination           Protocol Length Info
      7 0.005050000    172.16.10.3           10.101.23.250         TCP      60     65495→445 [ACK] Seq=118 Ack=7317 Win=256 Len=0

Frame 7: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: 6c:41:6a:13:1d:b1 (6c:41:6a:13:1d:b1), Dst: 00:1a:64:25:9b:9e (00:1a:64:25:9b:9e)
Internet Protocol Version 4, Src: 172.16.10.3 (172.16.10.3), Dst: 10.101.23.250 (10.101.23.250)
Transmission Control Protocol, Src Port: 65495 (65495), Dst Port: 445 (445), Seq: 118, Ack: 7317, Len: 0

No.     Time           Source                Destination           Protocol Length Info
      8 0.005789000    172.16.10.3           10.101.23.250         SMB2     171    Read Request Len:4280 Off:0

Frame 8: 171 bytes on wire (1368 bits), 171 bytes captured (1368 bits) on interface 0
Ethernet II, Src: 6c:41:6a:13:1d:b1 (6c:41:6a:13:1d:b1), Dst: 00:1a:64:25:9b:9e (00:1a:64:25:9b:9e)
Internet Protocol Version 4, Src: 172.16.10.3 (172.16.10.3), Dst: 10.101.23.250 (10.101.23.250)
Transmission Control Protocol, Src Port: 65495 (65495), Dst Port: 445 (445), Seq: 118, Ack: 8761, Len: 117
NetBIOS Session Service
SMB2 (Server Message Block Protocol version 2)

No.     Time           Source                Destination           Protocol Length Info
      9 0.005790000    172.16.10.2           10.101.23.250         TCP      60     63940→445 [ACK] Seq=1 Ack=2921 Win=353 Len=0

Frame 9: 60 bytes on wire (480 bits), 60 bytes captured (480 bits) on interface 0
Ethernet II, Src: 6c:41:6a:13:1d:b1 (6c:41:6a:13:1d:b1), Dst: 00:1a:64:25:9b:9e (00:1a:64:25:9b:9e)
Internet Protocol Version 4, Src: 172.16.10.2 (172.16.10.2), Dst: 10.101.23.250 (10.101.23.250)
Transmission Control Protocol, Src Port: 63940 (63940), Dst Port: 445 (445), Seq: 1, Ack: 2921, Len: 0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/ee61e4a0c650c5f2729414bc72226213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sykhoo&#39;s gravatar image" /><p><span>sykhoo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sykhoo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '14, 04:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36439" class="comments-container"></div><div id="comment-tools-36439" class="comment-tools"></div><div class="clear"></div><div id="comment-36439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36473"></span>

<div id="answer-container-36473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36473-score" class="post-score" title="current number of votes">0</div><span id="post-36473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you are seeing is DCE-RPC encapsulated in SMB2. You will see a Write Request and Response for every DCE-RPC call, and a Read Request and Response for every DCE-RPC Response. Very messy.</p><p>This is a bit of a long procedure, but this is how you can get more information.</p><p>You need to see the connections start, and so you will have to shut down one server during a maintenance window and restart it. It's important that you capture with Wireshark (or dumpcap) when the servers make the TCP connections.</p><p>Stop the trace and identify the first stream that has the continuous traffic. Filter to select just that stream.</p><p>Filter further by adding the expression dcerpc.pkt_type == 11 to show all DCE-RPC BIND Requests. Within the decode of the BIND Request you will see Context Items (Ctx Item). Within each of these you will see the UUID of the program interface that the BIND sender is trying to connect to. Wireshark decodes most UUIDs. If it doesn't, search for the UUID with Google.</p><p>Repeat the above for any other long running streams.</p><p>Reasearch what those program interfaces are used for.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-36473" class="comments-container"></div><div id="comment-tools-36473" class="comment-tools"></div><div class="clear"></div><div id="comment-36473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

