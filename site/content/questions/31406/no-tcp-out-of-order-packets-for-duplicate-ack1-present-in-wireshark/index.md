+++
type = "question"
title = "No TCP out-of-order packets for Duplicate ACK#1 present in wireshark"
description = '''Hello All, We are observing multiple TCP Duplicate ACK’s coming from the receiver and after going through the TCP RFC’s and I found the following reasons why our product is replying with multiple TCP DupACK&#x27;s. a. [RFC 2001 – Section 3] under Fast Retransmit, TCP may generate an immediate acknowledgm...'''
date = "2014-04-02T09:56:00Z"
lastmod = "2015-09-11T06:11:00Z"
weight = 31406
keywords = [ "dup-ack", "tcp" ]
aliases = [ "/questions/31406" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No TCP out-of-order packets for Duplicate ACK\#1 present in wireshark](/questions/31406/no-tcp-out-of-order-packets-for-duplicate-ack1-present-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All, We are observing multiple TCP Duplicate ACK’s coming from the receiver and after going through the TCP RFC’s and I found the following reasons why our product is replying with multiple TCP DupACK's.</p><p>a. [RFC 2001 – Section 3] under Fast Retransmit, TCP may generate an immediate acknowledgment (a duplicate ACK) when an out-of-order segment is received (Section 4.2.2.21 of [1], with a note that one reason for doing so was for the experimental fast-retransmit algorithm). This duplicate ACK should not be delayed. The purpose of this duplicate ACK is to let the other end know that a segment was received out of order, and to tell it what sequence number is expected.</p><p>b. [RFC 2001 – Section 3] Since TCP does not know whether a duplicate ACK is caused by a lost segment or just a reordering of segments, it waits for a small number of duplicate ACKs to be received. It is assumed that if there is just a reordering of the segments, there will be only one or two duplicate ACKs before the reordered segment is processed, which will then generate a new ACK. If three or more duplicate ACKs are received in a row, it is a strong indication that a segment has been lost. TCP then performs a retransmission of what appears to be the missing segment, without waiting for a retransmission timer to expire.</p><p>So, the receiver is behaving normally as per TCP standards, and is only sending duplicate ACK#1 which is the indication that an out-of-order TCP packet might have been received, but if I am checking the "Expert Info" of Wireshark then there is no indication of out-of-order pkt.</p><p>Can anyone help here what might be the other possible reason for the receiver to send duplicate ACK's??</p><p>Regards Amitav Nayak</p></div><div id="question-tags" class="tags-container tags">dup-ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/2cb0c7c53746c79a98efde786ac1a4d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amitav&#39;s gravatar image" /><p>Amitav<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amitav has no accepted answers">0%</span></p></div></div><div id="comments-container-31406" class="comments-container"><span id="31409"></span><div id="comment-31409" class="comment"><div id="post-31409-score" class="comment-score"></div><div class="comment-text"><p>I have added the snapshot of my wireshark trace for a better understanding.. In the pic you can see that we have 73 Duplicate ACK coming from receiver whereas there is no indication of an occurrance of an out-of-order packet.</p></div><div id="comment-31409-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:59)</span> Amitav</div></div><span id="31410"></span><div id="comment-31410" class="comment"><div id="post-31410-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Duplicate_ACK_1.png" alt="alt text" /></p></div><div id="comment-31410-info" class="comment-info"><span class="comment-age">(02 Apr '14, 10:03)</span> Amitav</div></div><span id="31529"></span><div id="comment-31529" class="comment"><div id="post-31529-score" class="comment-score"></div><div class="comment-text"><p>If you want to find out the reason you will need to take packet captures from both sides simultaneously. Maybe some device in between is misbehaving.</p></div><div id="comment-31529-info" class="comment-info"><span class="comment-age">(04 Apr '14, 11:47)</span> Roland</div></div></div><div id="comment-tools-31406" class="comment-tools"></div><div class="clear"></div><div id="comment-31406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45785"></span>

<div id="answer-container-45785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Duplicated ACKs may also be caused by very high path latency, brief connection outage or actual packet loss.</p><p>You can check for out of order packets with the filter "tcp.analysis.out_of_order" and check for retransmissions with this filter: tcp.analysis.retransmission || tcp.analysis.fast_retransmission</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '15, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/e4d7bea187b1535763804dd04006e4f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BrunoF&#39;s gravatar image" /><p>BrunoF<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BrunoF has no accepted answers">0%</span></p></img></div></div><div id="comments-container-45785" class="comments-container"></div><div id="comment-tools-45785" class="comment-tools"></div><div class="clear"></div><div id="comment-45785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

