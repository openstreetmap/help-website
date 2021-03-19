+++
type = "question"
title = "Server sending RST for a new request when old request was failed"
description = '''After the handshaking process is successfully completed,client sent request and server sends response,this request-reponse business worked seamleesly for one hour  After a hour client sent a request ,server sent the response,but client did not acknowledge for all tcp segments sent by the server due ...'''
date = "2015-12-03T06:22:00Z"
lastmod = "2015-12-03T07:35:00Z"
weight = 48229
keywords = [ "rst+ack", "tcp", "wireshark" ]
aliases = [ "/questions/48229" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server sending RST for a new request when old request was failed](/questions/48229/server-sending-rst-for-a-new-request-when-old-request-was-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48229-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After the handshaking process is successfully completed,client sent request and server sends response,this request-reponse business worked seamleesly for one hour After a hour client sent a request ,server sent the response,but client did not acknowledge for all tcp segments sent by the server due to network issues at client. So server does retransmission for 20 seconds finally it sends [RST/ACK] client after sometimes when network comes back initiates a new request again successfully,server send RST immediately with previous failed request (sequence,acknowedgement) pair.</p><p>I have attached pcap from the when the server sends the response,client acknowledges for few packets and fails to acknowledge for few ,</p><p>What I could not understand is why server sends RST when a new request is made succesfully</p><p><a href="https://www.cloudshark.org/captures/e572ecd7641d">Cloud Shark link</a></p></div><div id="question-tags" class="tags-container tags">rst+ack tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '15, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/7870416ebebf4e1563026b784e3e29aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saimadan&#39;s gravatar image" /><p>saimadan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saimadan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '15, 07:54</p></div></div><div id="comments-container-48229" class="comments-container"><span id="48230"></span><div id="comment-48230" class="comment"><div id="post-48230-score" class="comment-score"></div><div class="comment-text"><p>You forgot to add a question. What you've posted is a statement. And you forgot to post a capture (anonymized using TraceWrangler so that tcp payload and real IP addresses would not be leaked if you consider it necessary) somewhere and provide a link to it. Analysis by text log, especially when you've allowed tshark to replace TCP information by payload information where the latter is available, is close to impossible.</p></div><div id="comment-48230-info" class="comment-info"><span class="comment-age">(03 Dec '15, 06:35)</span> sindy</div></div><span id="48234"></span><div id="comment-48234" class="comment"><div id="post-48234-score" class="comment-score"></div><div class="comment-text"><p>I have attached pcap file,i have just started using wireshark a week back,so i didn't know we can anonymize the actual details</p></div><div id="comment-48234-info" class="comment-info"><span class="comment-age">(03 Dec '15, 07:56)</span> saimadan</div></div></div><div id="comment-tools-48229" class="comment-tools"></div><div class="clear"></div><div id="comment-48229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48233"></span>

<div id="answer-container-48233" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48233-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a perfect network exchange to me. What ever happens seems to be happening at the application level, and is reflected in the packet exchanges you've seen. Make sure that the client and server applications can get synchronized after network issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '15, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-48233" class="comments-container"><span id="48235"></span><div id="comment-48235" class="comment"><div id="post-48235-score" class="comment-score"></div><div class="comment-text"><p>can you please help me understand this behaviour,why server sends a RST when a client is able to make a successful request(i'm novice in networking ,i have just started using wireshark)</p></div><div id="comment-48235-info" class="comment-info"><span class="comment-age">(03 Dec '15, 07:58)</span> saimadan</div></div><span id="48238"></span><div id="comment-48238" class="comment"><div id="post-48238-score" class="comment-score">1</div><div class="comment-text"><p>I am not sure I can see that</p><blockquote><p>a client is able to make a successful request</p></blockquote><p>Because in your capture, the (probably) server rejects, by sending an RST, a mid-session packet, not a new request to establish a TCP session.</p><p>I guess that what confuses you is that you can see "Seq=1" in the packet you think is a new session-establishment request. The background is such that the tcp sequence numbers actually do not start from 1: they start from a random number, and only the difference between the values used in each direction is important for the protocol. For convenience of reading, Wireshark by default shows these differences (called "relative sequence numbers") instead of the real (absolute) values. And if it does not know the absolute sequence number of the initial packet of a direction of a session because that packet is missing in the capture, it uses as "relative 1" the absolute Seq value of the first packet of a direction of a session which is available in the capture.</p><p>In our case, the Seq number does not change (no payload bytes have been transmitted) between the very first packet in the capture and the packet (frame) No. 31 which you confused to be a new session establishment request.</p><p>So as Jaap wrote, the exchange is perfect - in the sense that the server knows that some packets have been irrecoverably lost, so it sends a RST to any attempt of the client to <strong>continue using</strong> that session, which is the correct behaviour. For the tcp client, reception of a packet with RST flag set is an indication that something went wrong, and it informs its client application about that. The client application then has to take appropriate measures based on that information. How exactly a given application deals with information about failure of a connection is beyond scope of network protocol analysis.</p><p>An attempt of the client to establish a new tcp session would look the following in Wireshark: the initial packet would show SYN in the packet list pane, and the Syn bit in TCP flags in packet dissection pane would be 1. The presence of Syn=1 in the packet indicates to the recipient of that packet (the server) that this packet is an opening one for a new session, and also to Wireshark that it should take the sequence number of that packet as relative 1 for the new tcp session even if another tcp session was previously using the same pair of sockets (IP address:port).</p></div><div id="comment-48238-info" class="comment-info"><span class="comment-age">(03 Dec '15, 09:37)</span> sindy</div></div></div><div id="comment-tools-48233" class="comment-tools"></div><div class="clear"></div><div id="comment-48233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

