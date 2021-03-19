+++
type = "question"
title = "Out of Order Packet.  ACK before SYN,ACK"
description = '''I have a packet capture, and we&#x27;re trying to debug a problem with our application just terminating a session. While looking for our problem, we&#x27;ve noticed that the packet capture is out of order. Link to Capture Capture was taken via Cisco span-port, with a single network card. What we&#x27;re seeing is ...'''
date = "2014-09-12T09:11:00Z"
lastmod = "2014-09-12T10:38:00Z"
weight = 36272
keywords = [ "out-of-order" ]
aliases = [ "/questions/36272" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Out of Order Packet. ACK before SYN,ACK](/questions/36272/out-of-order-packet-ack-before-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36272-score" class="post-score" title="current number of votes">0</div><span id="post-36272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a packet capture, and we're trying to debug a problem with our application just terminating a session. While looking for our problem, we've noticed that the packet capture is out of order.</p><p><a href="https://drive.google.com/file/d/0B2XDbKlbTzlqVFFFOV9BeHkzYmM/edit?usp=sharing">Link to Capture</a></p><p>Capture was taken via Cisco span-port, with a single network card.</p><p>What we're seeing is the packets are out of order. Not via timestamps, or packet number, but just the packet conversation (SYN -&gt;, ACK -&gt;, &lt;- SYN ACK)</p><p>Specific example is at 15:58:00.62606500, frame #68417, time 880.210825000. (This is also an instance of when our App just terminated)</p><p>I've used tracewrangler to try and correct the out of order packets. It reported timestamps out of order, so I let it fix them. This had no affect, since it only goes by the absolute time, and the absolute time appears correct in the conversation.</p><p>I also used it to anonymize the packets.</p><p>Thoughts on this? NIC card driver on the Capture PC?</p><p>Mike</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '14, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/d87d2173daa97e7292d8c556d8fafb8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mpking&#39;s gravatar image" /><p><span>Mpking</span><br />
<span class="score" title="8 reputation points">8</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mpking has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '14, 09:22</strong> </span></p></div></div><div id="comments-container-36272" class="comments-container"></div><div id="comment-tools-36272" class="comment-tools"></div><div class="clear"></div><div id="comment-36272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36274"></span>

<div id="answer-container-36274" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36274-score" class="post-score" title="current number of votes">0</div><span id="post-36274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mpking has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would suspect the SPAN port to be the origin of the out-of-order problem, because I have never seen a single NIC being responsible for swapping incoming frame order like that. SPAN ports are not really reliable when it comes to packet order and packet timing, and there are also cases where the SPAN session even had an impact on the "real" communication by delaying it slightly.</p><p>Anyway. Let's assume the order was SYN -&gt; SYN/ACK -&gt; ACK -&gt; RST. Basically the server accepts the TCP connection and tears it down right away. I have seen that kind of thing happen when a server application gets notified by the TCP stack that there is a new connection (right after the three way handshake is complete), and the application decides it doesn't like the client for whatever reason (too many connections, client IP blacklisted, etc.). When it shuts down the TCP socket the stack sends a RST to the client.</p><p>So you might want to check if the application has any kind of mechanism to reject specific clients.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '14, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36274" class="comments-container"><span id="36275"></span><div id="comment-36275" class="comment"><div id="post-36275-score" class="comment-score"></div><div class="comment-text"><p>I'm ok assuming the order is correct, and we've diagnosed what the issue was with the application.</p><p>We just have never seen the out of order get mangled like that, and were curious how it came about.</p></div><div id="comment-36275-info" class="comment-info"><span class="comment-age">(12 Sep '14, 09:38)</span> <span class="comment-user userinfo">Mpking</span></div></div><span id="36276"></span><div id="comment-36276" class="comment"><div id="post-36276-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Mind if I ask what the issue was? :-)</p></div><div id="comment-36276-info" class="comment-info"><span class="comment-age">(12 Sep '14, 09:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36277"></span><div id="comment-36277" class="comment"><div id="post-36277-score" class="comment-score"></div><div class="comment-text"><p>Not really sure myself. We develop the client application, another company develops the server, and they've been dropping the connection. They just say it's our fault. :-)</p></div><div id="comment-36277-info" class="comment-info"><span class="comment-age">(12 Sep '14, 10:22)</span> <span class="comment-user userinfo">Mpking</span></div></div><span id="36278"></span><div id="comment-36278" class="comment"><div id="post-36278-score" class="comment-score"></div><div class="comment-text"><p>lol... yeah, right :)</p></div><div id="comment-36278-info" class="comment-info"><span class="comment-age">(12 Sep '14, 10:38)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36274" class="comment-tools"></div><div class="clear"></div><div id="comment-36274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

