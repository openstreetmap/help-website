+++
type = "question"
title = "TCP Re-transmit Troubleshooting - Help Required"
description = '''I am new to TCP troubleshooting, Let me know if below mentioned analysis make sense. In frame 12100 the client tries to send a frame with sequence number 6154844. That sequence number was previously sent by the client in frame 12084. We can see that this as an out-of-order frame, is it possible that...'''
date = "2017-01-27T15:16:00Z"
lastmod = "2017-01-28T11:58:00Z"
weight = 59113
keywords = [ "tcp", "tcp-retransmit" ]
aliases = [ "/questions/59113" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Re-transmit Troubleshooting - Help Required](/questions/59113/tcp-re-transmit-troubleshooting-help-required)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to TCP troubleshooting, Let me know if below mentioned analysis make sense.</p><p>In frame 12100 the client tries to send a frame with sequence number 6154844. That sequence number was previously sent by the client in frame 12084. We can see that this as an out-of-order frame, <strong>is it possible that the clientdid not receive Server's ACK of that sequence number, and the client is retransmitting the frame?</strong></p><p>the TCP window size appears to be small for this session, so each packet sent by the client looks like it gets acknowledged before the client sends the next packet. This makes the retransmit scenario seem unlikely.</p><p>Once the client resends sequence number 6154844, it keeps resending it. Server doesn't acknowledge it because it already has. The client retry count apparently gets exhausted and it attempts to restart the session in frame 12106.</p><p>Server ignores the attempt to start a new session, as it already had a session with that IP address and port number. <strong>Refer image in link</strong> <a href="http://imgur.com/a/ebMSJ"><strong></strong></a><strong><a href="http://imgur.com/a/ebMSJ">http://imgur.com/a/ebMSJ</a></strong></p></div><div id="question-tags" class="tags-container tags">tcp tcp-retransmit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '17, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/46e8a8ff9fe331eccf773ca55ef81e29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arunkumarkak&#39;s gravatar image" /><p>arunkumarkak<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arunkumarkak has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '17, 15:19</p></div></div><div id="comments-container-59113" class="comments-container"><span id="59121"></span><div id="comment-59121" class="comment"><div id="post-59121-score" class="comment-score"></div><div class="comment-text"><p>It would be great if could share us the trace. As we are missing a lot of infos in screenshot. <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-59121-info" class="comment-info"><span class="comment-age">(28 Jan '17, 14:22)</span> Christian_R</div></div></div><div id="comment-tools-59113" class="comment-tools"></div><div class="clear"></div><div id="comment-59113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59114"></span>

<div id="answer-container-59114" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59114-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you are correct. The behaviour is explained by the client not receiving the ACKs. Can you capture at the client?</p><p>I also notice that window size is small. Is the SYN - SYN/ACK in the trace file? Wireshark needs to see the handshake to get the window scaling factors and I suspect it doesn't have them. The evidence for this is that there are several packets from client to service of 1448 bytes even though the window size is showing as 1345.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '17, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-59114" class="comments-container"></div><div id="comment-tools-59114" class="comment-tools"></div><div class="clear"></div><div id="comment-59114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59118"></span>

<div id="answer-container-59118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I wonder what was the environment you've captured in? Look at those timings! We're on receiving side. After receiving first data packet we ACK'ed it immediately, BUT got the next data packet after 9 (!) seconds.If client had not received our ACK, where is regular retransmissions which must be happening after maximum of 0.5 seconds? And this pattern is happening again and again throughout all the trace (screenshot).</p><p>The first retransmission came to us after 28 seconds.</p><p>TCP timestamps is of a GREAT help here. We observe the same Tsecr value of 992435503 in all data packets. This is a sign of all data packets being sent in response to only one our ACK. At the same time Tsval in data packets differs not much, that can be a sign of data packets being sent very closely one to another. It seems that packet train going from the client (10.9.129.22) is hanging somewhere on the highly congested and deeply buffered link. So congested and buffered, that we're receiving one packet every 'some' seconds. But all this packet train was emitted in very short period of time.</p><p>Much later retransmission finally came to us (probably it was emitted after 0.2 seconds from original packet, but got to our side after 28 seconds).</p><p>Here we have another dramatically change - all 3 retransmissions and some other packets from frame no.12094 came in time span less than millisecond. Maybe, congestion at this time was less than before.</p><p>Unfortunately, we can't see full timestamp values - your screenshot is being cut from the right.</p><p>Some other observations:</p><ul><li><p>I think window size is not a problem here, because window scaling is probably in use.</p></li><li><p>You've said that 'The client retry count apparently gets exhausted and it attempts to restart the session in frame 12106.' but I do not see frame 12106. Could you please show it?</p></li><li><p>You've said that 'Server ignores the attempt to start a new session, as it already had a session with that IP address and port number. '</p></li></ul><p>It's hihgly unlikely for client to start another TCP session with the same source port in such short period of time (unless it is hardcoded somehow). But again, we can't see that on the screenshot.</p><p>Thanks for interesting sample!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '17, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '17, 12:17</p></div></div><div id="comments-container-59118" class="comments-container"><span id="59128"></span><div id="comment-59128" class="comment"><div id="post-59128-score" class="comment-score"></div><div class="comment-text"><p>THANKS GUYS. let me upload captured file.</p></div><div id="comment-59128-info" class="comment-info"><span class="comment-age">(28 Jan '17, 21:56)</span> arunkumarkak</div></div></div><div id="comment-tools-59118" class="comment-tools"></div><div class="clear"></div><div id="comment-59118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

