+++
type = "question"
title = "TCP retransmission analysis problem with Wireshark"
description = '''I&#x27;m using Wireshark to analyze capture file dumped with tcpdump, but I can&#x27;t understand some results as follows: (1)Fast retransmission. In my opinion, fast retransmission will happen while receiving 3 same duplicate acks, but in reality it happens after dozens of or even more than one hundred acks ...'''
date = "2014-03-11T00:45:00Z"
lastmod = "2014-03-11T20:31:00Z"
weight = 30679
keywords = [ "sack", "retransmission", "tcp", "out-of-order" ]
aliases = [ "/questions/30679" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP retransmission analysis problem with Wireshark](/questions/30679/tcp-retransmission-analysis-problem-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30679-score" class="post-score" title="current number of votes">0</div><span id="post-30679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark to analyze capture file dumped with tcpdump, but I can't understand some results as follows:</p><p>(1)Fast retransmission. In my opinion, fast retransmission will happen while receiving 3 same duplicate acks, but in reality it happens after dozens of or even more than one hundred acks have been received.</p><pre><code>3660 6.364478 TCP 94 [TCP Dup ACK 3380#140] 37595 &gt; http [ACK] Seq=1 Ack=3214429 Len=0
3661 6.365102 HTTP 1494 [TCP Fast Retransmission] http &gt; 37595 Seq=3214429 Ack=1 Len=1428</code></pre><p>(2)Weird retransmission. I've found retransmission happend after being acked. Maybe due to SACK?</p><pre><code>10041 18.681817 TCP 86 [TCP Dup ACK 10015#13] 37595 &gt; http [ACK] Seq=1 Ack=9180613 Len=0(SACK: 9099217-9100645 9182041-9217741)
10042 18.683154 HTTP 1494 [TCP Retransmission] http &gt; 37595 Seq=9127777 Ack=1 Len=1428</code></pre><p>(3)Out of order. This is a <a href="http://ask.wireshark.org/questions/11066/vendor-claims-wireshark-incorrectly-reporting-out-of-order-packets">question that has been asked by Janis Bishop</a>. I can understand that receiver end can receive out of order packet due to multi route path, but why can the sender end send out of order packet?</p><pre><code>10036 18.678996 HTTP    1494 http &gt; 37595 Seq=9216313 Ack=1 Len=1428
10037 18.679020 TCP 78 [TCP Dup ACK 10015#11] 37595 &gt; http [ACK] Seq=1 Ack=9180613 Len=0
10038 18.680609 HTTP    1494 [TCP Out-Of-Order] http &gt; 37595 Seq=9066373 Ack=1 Len=1428
10039 18.680642 TCP 86 [TCP Dup ACK 10015#12] 37595 &gt; http [ACK] Seq=1 Ack=9180613 Len=0
10040 18.681794 HTTP    1494 [TCP Out-Of-Order] http &gt; 37595 Seq=9099217 Ack=1 Len=1428</code></pre><p>I did the capture at the server end(also as the data sender).In my situation, the client end(as data receiver) send request to the server, then the server send data back.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/76caadbe100710088c0a7f7ecc2e9152?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kikita&#39;s gravatar image" /><p><span>kikita</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kikita has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Mar '14, 20:59</strong> </span></p></div></div><div id="comments-container-30679" class="comments-container"></div><div id="comment-tools-30679" class="comment-tools"></div><div class="clear"></div><div id="comment-30679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30682"></span>

<div id="answer-container-30682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30682-score" class="post-score" title="current number of votes">0</div><span id="post-30682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) Usually, the reason why you see is tons of DUP acks before the fast retransmission comes in is that you're close to the destination of the lost packet, which means the distance is very short. Keep in mind that your 3 dup acks need to travel half the RTT to the sender, and then the retransmission needs to come back to you (another half RTT). That way your receiver keeps pumping out dup acks while the fast retransmission process takes one full RTT (plus a bit more) to get processed. And that is in situations where everything else is working fine. If you have bottlenecks in your network you can see tons of dup acks sent out before receiving the retransmission; I just broke a record in a case I analyzed recently where there were more than 1000 duplicate ACKs for one single lost packet...</p><p>2) this can happen to, e.g. if the ack didn't make it to the server, or for any other reason. To diagnose that you'd need a capture taken simultaneously close to the other node.</p><p>3) It does not have to be a multi route path. Depending on prioritization and buffer management in routers and other devices packets sometimes get forwarded earlier than those already waiting in line. Generally speaking, senders do not send out packets out of order, they get mixed up on the way. If you capture at the sender and see out of orders coming out you've got something very unusual, which would require further investigation into the TCP stack...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30682" class="comments-container"><span id="30703"></span><div id="comment-30703" class="comment"><div id="post-30703-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much.</p><p>I did the capture at the server end(also as the data sender).In my situation, the client end(as data receiver) send request to the server, then the server send data back.</p><p>So question 2 is still weird, the capture information reveals that the server has received ack to seq(9180613), which is higher than seq(9127777), but server still send back packet begun with seq(9127777), which is not needed. From the ack(to seq 9180613) packet's detail information in the option segment(SACK: 9099217-9100645 9182041-9217741), does this mean that packet begun with seq(9100646) is still not received indeed?</p><p>Question 3 is indeed unusual, and it has also happened before in the link above.</p></div><div id="comment-30703-info" class="comment-info"><span class="comment-age">(11 Mar '14, 20:31)</span> <span class="comment-user userinfo">kikita</span></div></div></div><div id="comment-tools-30682" class="comment-tools"></div><div class="clear"></div><div id="comment-30682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

