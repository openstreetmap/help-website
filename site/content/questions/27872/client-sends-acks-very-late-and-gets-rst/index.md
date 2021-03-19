+++
type = "question"
title = "client sends ACKS very late and gets RST"
description = '''This is a dump captured at the client (this is a web traffic generator tool) in a customer test environment. We were told that  the client (.42) is not sending ACKs and this results in the test getting terminated. I am not an expert on networking or trace analysis and am having a tough time figuring...'''
date = "2013-12-06T07:49:00Z"
lastmod = "2013-12-11T11:35:00Z"
weight = 27872
keywords = [ "ack" ]
aliases = [ "/questions/27872" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [client sends ACKS very late and gets RST](/questions/27872/client-sends-acks-very-late-and-gets-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27872-score" class="post-score" title="current number of votes">0</div><span id="post-27872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a dump captured at the client (this is a web traffic generator tool) in a customer test environment. We were told that the client (.42) is not sending ACKs and this results in the test getting terminated. I am not an expert on networking or trace analysis and am having a tough time figuring out if the answer to <em>why</em> the client is not sending an ACK is hidden somewhere in the dump. I also have these basic questions -</p><ol><li>why is the client sending dup ACK for packet 43 - when it has recvd 2 pkts (44,45) following this. Isn't the DUP ACK for an earlier pkt sent when the client misses packets ?</li><li>The server sends this seq no (23985) in 68, but client continues to send the DUP ACK</li><li>Is it possible for the client to send ACKS this late -- eg., 90 is ACK for 56 (RTT - 3.4s), 90 is ACK for 57 (RTT= 11s), 96 has RTT 28s, 108 has RTT of 156s! Doesnt the ACK timer expire in about 500ms ?</li><li>In 115 and 116 (seq 43547), server starts retransmitting right away and sends a RST at 125 - where as in the other cases, the server did nt send an RST though the client send an ACK after &gt; 100 s.</li></ol><p>pcap is at -- <a href="https://drive.google.com/file/d/0B6WbY-hKwR3KSWpQTHF2eVRhQTg/edit?usp=sharing">https://drive.google.com/file/d/0B6WbY-hKwR3KSWpQTHF2eVRhQTg/edit?usp=sharing</a></p><p>PS. I just realized that I cant upload an image - how do I convert the pcap to an image to upload ? --Jai</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/aee31ce6e04b61e9091a980bb1f9f62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jai&#39;s gravatar image" /><p><span>Jai</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '13, 10:32</strong> </span></p></div></div><div id="comments-container-27872" class="comments-container"><span id="27873"></span><div id="comment-27873" class="comment"><div id="post-27873-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>This is a dump</strong> captured at the client</p></blockquote><p>As there is no link to the capture file, please post the file somewhere (google drive, dropbox, cloudshark.org or mega.co.nz) and then add the link to your question.</p></div><div id="comment-27873-info" class="comment-info"><span class="comment-age">(06 Dec '13, 08:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27872" class="comment-tools"></div><div class="clear"></div><div id="comment-27872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27886"></span>

<div id="answer-container-27886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27886-score" class="post-score" title="current number of votes">2</div><span id="post-27886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"why is the client sending dup ACK for packet 43? " Because the client's TCP did <strong><em>NOT</em></strong> see packet #43. The TCP connection is using SACK option and looking at the SACK left and tight edges it is clear that many packets that are seen in your trace never made it to the client's TCP layer. All the black background packets in your trace are not seen by TCP.</p><p>The trace was taken close to (in front of) the client but not in the client itself? If so, it is the 'SuperMic Super Micro Computer, Inc. ' device is dropping packets on its inbound interface. the packets arrive in the same instant, only the first 20 packets made it to TCP, so there might be a queue length of 20 packets...</p><hr /><p><strong>Correction:</strong> Looking further down there are indications that the <a href="http://en.wikipedia.org/wiki/Large_receive_offload">LRO Large Receive Offload</a> is in place. Segments arrive that larger than the negotiated MSS <strong>filter: <code>tcp.len gt 1448</code> :</strong> . So the trace was obviously taken <strong><em>behind</em></strong> the NIC card and the packets are therefore not dropped there. Also the packet rate at the end of the trace is close to zero, certainly not overloading any interfaces there. So there must be something else discarding the packets within the client. The TCP checksumms on inbound packets are correct however.</p><p>My next action would be to check whether Large Receive Offload or Generic Receive Offload are enabled for the interface and turn those off: ethtool -k eth0 will show the current settings. <img src="https://osqa-ask.wireshark.org/upfiles/SACK_in_action.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '13, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Dec '13, 23:01</strong> </span></p></div></div><div id="comments-container-27886" class="comments-container"><span id="27995"></span><div id="comment-27995" class="comment"><div id="post-27995-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for looking at the dump. Yes, you're right that the dump was captured on the client. LRO and GRO were turned on, so we ve tried turning off LRO and GRO as you suggested. It did appear to make a difference in the http errors initially, but when we turned it back on to confirm, we didn't see the errors again either. We're increasing the traffic to see if it reappears. If the pkts are dropped in the client (behind the NIC), how could this have changed ?</p></div><div id="comment-27995-info" class="comment-info"><span class="comment-age">(11 Dec '13, 02:00)</span> <span class="comment-user userinfo">Jai</span></div></div><span id="28017"></span><div id="comment-28017" class="comment"><div id="post-28017-score" class="comment-score"></div><div class="comment-text"><p>I have no idea. I don't know which TCP stack is running there, certainly not one that I would use to stress test a web server though.</p></div><div id="comment-28017-info" class="comment-info"><span class="comment-age">(11 Dec '13, 11:35)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-27886" class="comment-tools"></div><div class="clear"></div><div id="comment-27886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

