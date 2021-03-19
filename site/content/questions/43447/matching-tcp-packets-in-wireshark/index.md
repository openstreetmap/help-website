+++
type = "question"
title = "matching tcp packets in wireshark"
description = '''i am very troubled when tracing my wireshark packets so please help, i&#x27;m filtering TCP packets, assuming im capturing at the Sender side, now sender sends packet to the rcvr who replies with ack packet containing the new window size for example 5, so the sender sends a stream of 5 packets, after tha...'''
date = "2015-06-22T09:43:00Z"
lastmod = "2015-06-22T10:28:00Z"
weight = 43447
keywords = [ "ack", "data", "trace", "tcp", "wireshark" ]
aliases = [ "/questions/43447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [matching tcp packets in wireshark](/questions/43447/matching-tcp-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43447-score" class="post-score" title="current number of votes">0</div><span id="post-43447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am very troubled when tracing my wireshark packets so please help, i'm filtering TCP packets, assuming im capturing at the Sender side, now sender sends packet to the rcvr who replies with ack packet containing the new window size for example 5, so the sender sends a stream of 5 packets, after that he receives from the receiver the ack of the first packet in the stream with new window size..and so on ..now to match each of those data packets and it's acknowledgment, the ack number = the data packet's sequence number + length ..is that correct??? Also im trying to get the delays between all that, my problem is what happens when there's a lost packet in this stream of 5, for ex packet 3 is lost, how does the ACK for Packet 4 LOOK IN THIS CASE ? i mean do i just know there's a lost packet from the sack option OR the sequence number doesn't change until i get the lost packet or the ack number stays unchanged or what ?? sorry but i got troubled because i am looping on all packets and trying to match them and there's something wrong in my logic !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '15, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-43447" class="comments-container"></div><div id="comment-tools-43447" class="comment-tools"></div><div class="clear"></div><div id="comment-43447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43449"></span>

<div id="answer-container-43449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43449-score" class="post-score" title="current number of votes">0</div><span id="post-43449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the ACK number for a packet is the packet's sequence number plus the data length. (Number of TCP data bytes in the packet, not total packet bytes. The Ethernet header and trailer, the IP header, and the TCP header are not included.) If packet 2 is acknowledged and then packet 3 is lost, the ACK for packet 4 will be a Duplicate ACK and it will be the same as the ACK for packet 2. ACKs are cumulative, so the ACK number cannot be incremented until the lost packet is received.</p><p>An ACK of 10,000 means "I've received <strong>everything</strong> through 9,999, and I expect 10,000 next." If SACK is in use, receipt of packet 4 will be shown in the SACK blocks, but the ACK number will not change until the missing packet shows up.</p><p>To follow all this, I recommend adding these fields as columns:</p><ul><li>TCP length (tcp.len)</li><li>Sequence number (tcp.seq)</li><li>Next expected sequence number (tcp.nxtseq)</li><li>Acknowledgment number (tcp.ack)</li></ul><p>Let Wireshark match the data packets to acknowledgment packets for you. Also add:</p><ul><li>Packet number being acknowledged (tcp.analysis.acks_frame)</li></ul><p>Remember that there does not have to be an acknowledgment packet for every single data packet. If Delayed ACK is in use, there could be an ACK for every other data packet, or for every three data packets, or every four data packets, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-43449" class="comments-container"><span id="43452"></span><div id="comment-43452" class="comment"><div id="post-43452-score" class="comment-score"></div><div class="comment-text"><p>okay in the case of lost packet , by duplicate ack u mean they both have same sequence no. or same ack number ?, also if i want to match packet 4 and it's ack which actually doesn't carry the expected ack number bec of duplication , and sack is not in use ...is there anyway to match them ?</p></div><div id="comment-43452-info" class="comment-info"><span class="comment-age">(22 Jun '15, 10:28)</span> <span class="comment-user userinfo">yas1234</span></div></div></div><div id="comment-tools-43449" class="comment-tools"></div><div class="clear"></div><div id="comment-43449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

