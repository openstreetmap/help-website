+++
type = "question"
title = "Over 1,000 duplicate ACKs without TCP retransmission"
description = '''I&#x27;m capturing packets using tshark at the server side (simple client-server setup with a number of routers in-between - the server is behind a NAT gateway). The client is connected to a private LTE network, so the air interface could cause some packet loss, which was expected.  During the capture, I...'''
date = "2016-09-22T02:02:00Z"
lastmod = "2016-09-22T04:58:00Z"
weight = 55743
keywords = [ "dup-ack", "tshark", "tcp" ]
aliases = [ "/questions/55743" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Over 1,000 duplicate ACKs without TCP retransmission](/questions/55743/over-1000-duplicate-acks-without-tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55743-score" class="post-score" title="current number of votes">0</div><span id="post-55743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing packets using tshark at the server side (simple client-server setup with a number of routers in-between - the server is behind a NAT gateway). The client is connected to a private LTE network, so the air interface could cause some packet loss, which was expected.</p><p>During the capture, I've seem quite a few times where the client (10.5.21.32) sends over 1,000 duplicate ACK to the server. I've attached some of the typical entries below.</p><p>The format is:</p><p>Packet ID / timestamp / Source IP / Source Port / Dest IP / Dest Port / Length / Info</p><p><strong>First, some entries with out-of-order packet arrivals (I think this is normal).</strong></p><pre><code>27011 1474467575.009112204   10.5.21.32 43880 10.5.3.229   8080 78 TCP 43880 → 8080 [ACK] Seq=2920 **Ack=82981452**
27012 1474467575.009180913   10.5.3.229 8080 10.5.21.32   43880 10202 TCP [TCP segment of a reassembled PDU]
27013 1474467575.009265903   10.5.3.229 8080 10.5.21.32   43880 5858 TCP [TCP segment of a reassembled PDU]
27018 1474467575.014182750   10.5.21.32 43880 10.5.3.229   8080 94 TCP [TCP Dup ACK 27011#1] 43880 → 8080 [ACK] Seq=2920 **Ack=82981452**
27019 1474467575.014185135   10.5.3.229 8080 10.5.21.32   43880 1514 TCP [TCP Out-Of-Order] [TCP segment of a reassembled PDU]</code></pre><p><strong>Next, some entries with retransmissions (normal too).</strong></p><pre><code>27122 1474467575.024498471   10.5.21.32 43880 10.5.3.229   8080 94 TCP [TCP Dup ACK 27011#61] 43880 → 8080 [ACK] Seq=2920 **Ack=82981452**
27123 1474467575.024500370   10.5.3.229 8080 10.5.21.32   43880 1514 TCP [TCP Retransmission] 8080 → 43880 [ACK] Seq=83052404 Ack=2920</code></pre><p><strong>Now is the questionable part: tshark keeps capturing duplicate ACKs with the same Seq and Ack numbers, even when there're no retransmissions or out-of-order packets.</strong></p><pre><code>27474 1474467575.045264093   10.5.21.32 43880 10.5.3.229   8080 94 TCP [TCP Dup ACK 27011#246] 43880 → 8080 [ACK] Seq=2920 **Ack=82981452**
27475 1474467575.045266169   10.5.3.229 8080 10.5.21.32   43880 4410 TCP [TCP segment of a reassembled PDU]</code></pre><p>etc. etc.</p><p>until</p><pre><code>28708 1474467575.145437844   10.5.21.32 43880 10.5.3.229   8080 94 TCP [TCP Dup ACK 27011#889] 43880 → 8080 [ACK] Seq=2920 **Ack=82981452**</code></pre><p>which is the last dup ack in this case (889 in total). This happened a couple more times.</p><p>Note that all these dup acks were sent within a period of ~130ms. The RTT between client and server is ~20ms.</p><p>I've analyzed the entire trace (lasted ~7 min), and below are the statistics:</p><pre><code>Out of order: 2655 packets, 4019670 bytes  
Retransmission: 3683 packets, 5542322 bytes  
Duplicate ACK: 42078  
Total packets: 844503</code></pre><p>Any advice on why there are so many more duplicate ACKs than the retransmission events?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/5b505a91634dbad2eb6c081340c7197f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chang&#39;s gravatar image" /><p><span>Chang</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Sep '16, 02:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55743" class="comments-container"></div><div id="comment-tools-55743" class="comment-tools"></div><div class="clear"></div><div id="comment-55743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55746"></span>

<div id="answer-container-55746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55746-score" class="post-score" title="current number of votes">1</div><span id="post-55746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Chang has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is usually caused by buffer bloat: <a href="https://en.wikipedia.org/wiki/Bufferbloat">https://en.wikipedia.org/wiki/Bufferbloat</a></p><p>I also talked about this kind of thing in my Sharkfest 2015 talk available here, starting at 25:00:</p><p><a href="https://www.youtube.com/watch?v=L5cbn2iF91s#t=25m00s">https://www.youtube.com/watch?v=L5cbn2iF91s#t=25m00s</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '16, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55746" class="comments-container"><span id="55748"></span><div id="comment-55748" class="comment"><div id="post-55748-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jasper, this answers my question.</p></div><div id="comment-55748-info" class="comment-info"><span class="comment-age">(22 Sep '16, 04:58)</span> <span class="comment-user userinfo">Chang</span></div></div></div><div id="comment-tools-55746" class="comment-tools"></div><div class="clear"></div><div id="comment-55746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

