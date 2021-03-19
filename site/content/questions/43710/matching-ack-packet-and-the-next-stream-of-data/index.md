+++
type = "question"
title = "matching ack packet and the next stream of data"
description = '''I am tracing wireshark and matching tcp packets in order to calculate the delays occuring, i can match a data packet and it&#x27;s acknowlegment, but my problem is, when i have an ack packet with window size two for example, i receive this ack at the sender side and comes right after it 2 data packets se...'''
date = "2015-06-30T02:14:00Z"
lastmod = "2015-06-30T07:08:00Z"
weight = 43710
keywords = [ "ack", "tcp-cwnd", "tcp", "wireshark" ]
aliases = [ "/questions/43710" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [matching ack packet and the next stream of data](/questions/43710/matching-ack-packet-and-the-next-stream-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43710-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am tracing wireshark and matching tcp packets in order to calculate the delays occuring, i can match a data packet and it's acknowlegment, but my problem is, when i have an ack packet with window size two for example, i receive this ack at the sender side and comes right after it 2 data packets sent from the sender side, but this ack and it's stream of data at the RECIEVER side are my problem, i have this ack packet as source and i receive the stream of two packets sometime in the future and they might overlap with other packets ..how do i match this ack and 1 and this ack and 2 at the receiver ??</p><p>sender receiver</p><pre><code>ack windowSize=2</code></pre><p>&lt;------------------------</p><pre><code>1</code></pre><p>------------------------&gt;</p><pre><code>2</code></pre><p>------------------------&gt;</p><pre><code>next ack</code></pre><p>&lt;-----------------------</p></div><div id="question-tags" class="tags-container tags">ack tcp-cwnd tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-43710" class="comments-container"></div><div id="comment-tools-43710" class="comment-tools"></div><div class="clear"></div><div id="comment-43710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43732"></span>

<div id="answer-container-43732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43732-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hm, I'm confused about what you are asking here<br />
The headline goes : matching ack packet and the next stream of data<br />
So one could guess that you want to see the next incoming data for the same tcp session after an ACK was sent.</p><p>Your 'picture' suggests that the ACKs would be flowing controlled by the window_size - which it is not!</p><pre><code>sender                       receiver
    &lt;------------------------ (0) ack windowSize=2 &quot;This ack&quot;
(1) ------------------------&gt;
(2) ------------------------&gt;
     &lt;----------------------- (3) &quot;next ack&quot;</code></pre><p>"how do i match this ack and 1 and this ack and 2 at the receiver ??"<br />
"this ack (0) and (1) " is easy as the tcp.ack number at the receiver is the next expected tcp.seq number from the sender (1).<br />
"this ack (0) ... and (2) " is not so trivial as (2)'s sequence number is dependent of the tcp.len of (1): tcp.seq plus tcp.len - wireshark does the math for you in field tcp.nxtseq<br />
I don't know how you can predict this information by looking at segment (0). My suggestion is to add following fields to the column list<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-1.png" alt="alt text" /></p><p>Than you can see in the packet list which segments are 'ack-ed' - even the frame number</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-dumpwithheaders.pcapng.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-43732" class="comments-container"><span id="43773"></span><div id="comment-43773" class="comment"><div id="post-43773-score" class="comment-score"></div><div class="comment-text"><p>you do get my question but i do not understand this "your 'picture' suggests that the ACKs would be flowing controlled by the window_size - which it is not! " do u mean that after a stream of packets i get one ACK only for that stream 'collective ack' and thus the number of acks is not equal to the window size ?</p></div><div id="comment-43773-info" class="comment-info"><span class="comment-age">(01 Jul '15, 03:00)</span> yas1234</div></div><span id="43780"></span><div id="comment-43780" class="comment"><div id="post-43780-score" class="comment-score"></div><div class="comment-text"><p>Typically a receiver acknowledges 'every other segment', that is<br />
for every 2 received segment you see 1 outgoing ACK acknowledging both segments.</p><p>If there is only one segment left to be sent (= the receiver will only see a single segment coming in) you will/should see a 'delayed' ACK aknowledging the only left segment. Window_size is used for TCP Flow Control and is a different topic...</p></div><div id="comment-43780-info" class="comment-info"><span class="comment-age">(01 Jul '15, 05:39)</span> mrEEde</div></div></div><div id="comment-tools-43732" class="comment-tools"></div><div class="clear"></div><div id="comment-43732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

