+++
type = "question"
title = "TCP DUP and resetting phone"
description = '''We have a couple of mitel phones connected to a brocade switch stack having issues. The phones are resetting and dropping randomly. When I do a wireshark sniff on the traffic between the PBX and phones I see lots of TCP DUP ACK messages, which seems to be corresponding to phone outages. Anyone have ...'''
date = "2014-09-26T16:09:00Z"
lastmod = "2014-09-27T09:13:00Z"
weight = 36646
keywords = [ "dup-ack", "tcp" ]
aliases = [ "/questions/36646" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP DUP and resetting phone](/questions/36646/tcp-dup-and-resetting-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36646-score" class="post-score" title="current number of votes">0</div><span id="post-36646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a couple of mitel phones connected to a brocade switch stack having issues. The phones are resetting and dropping randomly. When I do a wireshark sniff on the traffic between the PBX and phones I see lots of TCP DUP ACK messages, which seems to be corresponding to phone outages.</p><p>Anyone have ideas what could be causing it?</p><p>Capture here: <a href="https://www.cloudshark.org/captures/5ea68460fb66">https://www.cloudshark.org/captures/5ea68460fb66</a></p><p>I stripped it down to just the traffic between one set and the PBX. Multiple random phones seem to be affected. The phone and PBX or connected to the same L2 switch.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '14, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/237bbaee214e48f85f1e822669a71477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="webman&#39;s gravatar image" /><p><span>webman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="webman has no accepted answers">0%</span></p></div></div><div id="comments-container-36646" class="comments-container"></div><div id="comment-tools-36646" class="comment-tools"></div><div class="clear"></div><div id="comment-36646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36647"></span>

<div id="answer-container-36647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36647-score" class="post-score" title="current number of votes">1</div><span id="post-36647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How was this capture taken? I guess via SPAN port? Did the phones reset during the time of capture? I'm asking because there is no TCP session reset in the trace.</p><p>If you filter for "tcp.stream==1" you'll see that there is a pattern of of duplicate ACKs with suspicious delta timings of almost 10 seconds for every second ACK. Maybe this is some weird way of the devices doing a session keep alive.</p><p>The other stream ("tcp.stream==0) has some curious retransmissions, starting in frame 126. Curious, because they start coming in 48 seconds (!!!) after the original packet (which does not get acknowledged for some reason), which is a retransmission time out I have never seen before.</p><p>From what I see the TCP stacks of the devices do strange things - if the captures where created on a SPAN port my next move would be to capture the PBX with a real full duplex TAP, because when things are weird you need to make sure it's not the SPAN session that is responsible for some of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36647" class="comments-container"><span id="36648"></span><div id="comment-36648" class="comment"><div id="post-36648-score" class="comment-score"></div><div class="comment-text"><p>It was done with a span port. Will try a tap and see if the results change. Thanks</p></div><div id="comment-36648-info" class="comment-info"><span class="comment-age">(26 Sep '14, 18:23)</span> <span class="comment-user userinfo">webman</span></div></div></div><div id="comment-tools-36647" class="comment-tools"></div><div class="clear"></div><div id="comment-36647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36650"></span>

<div id="answer-container-36650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36650-score" class="post-score" title="current number of votes">0</div><span id="post-36650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry Jasper, but I don't see the 48 seconds retransmission timer and I don't agree with the TCP stream 1 is an idle connection with the PBX sending zero length keepalives so all those duplicate acks are a false alert and can be ignored. The phone is acking with tcp.ack 2 but PBX keeps on sending empty packets with tcp.seq 1<br />
- Nothing weird here, TCP keepalive without a garbage byte) - List item</p><p>The problem starts in packet 125 with the phone sending 176 bytes which doesn't get through so slow retransmission kicks in with increasing rxmit intervals (0.239 - 0.719 - 1.679 - 3.593)<br />
Packet 130 is the ACK of the retransmitted packet, so the PBX has finally received the 176 bytes.<br />
The sequence number in packet 130 however indicates that the PBX in the meantime also sent 176 bytes which did not arrive at the phone. The missing 176 with seq 2641 finally arrive after another 1.089 seconds and the phone acks the data. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_254.png" alt="alt text" /></p><p>So this is an indication that we had a connectivity issue in both directions between 16:03:38.188 and 16:03:41.782 UTC. While this is not nice on a local LAN it is certainly not a reason to 'reset or drop' the phone.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '14, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-36650" class="comments-container"><span id="36651"></span><div id="comment-36651" class="comment"><div id="post-36651-score" class="comment-score"></div><div class="comment-text"><p>If its a connectivity issue in both directions and its on the same switch, then that would have to be a overloaded port on either the PBX or phone, or a problem with the L2 switch. Correct?</p></div><div id="comment-36651-info" class="comment-info"><span class="comment-age">(27 Sep '14, 06:53)</span> <span class="comment-user userinfo">webman</span></div></div><span id="36654"></span><div id="comment-36654" class="comment"><div id="post-36654-score" class="comment-score"></div><div class="comment-text"><p>Right <span>@mrEEde</span>, I overlooked that packet 112 has an empty TCP payload, I just looked at the sequence number - it was probably just too late in the night for me :-)</p></div><div id="comment-36654-info" class="comment-info"><span class="comment-age">(27 Sep '14, 09:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36650" class="comment-tools"></div><div class="clear"></div><div id="comment-36650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

