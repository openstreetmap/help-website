+++
type = "question"
title = "TCP ack message query in diameter communication"
description = '''Hi Experts, I need understanding on fundamentals. Whenever sender sends diameter message to receiver over TCP protocol - receiver will send tcp ack message. However, I want to understand if it is diameter application which responds back with ack or it is OS (RHEL) TCP/IP stack which sends this ack m...'''
date = "2017-03-17T08:40:00Z"
lastmod = "2017-03-18T05:56:00Z"
weight = 60155
keywords = [ "ack", "diameter", "tcp" ]
aliases = [ "/questions/60155" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TCP ack message query in diameter communication](/questions/60155/tcp-ack-message-query-in-diameter-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60155-score" class="post-score" title="current number of votes">0</div><span id="post-60155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I need understanding on fundamentals. Whenever sender sends diameter message to receiver over TCP protocol - receiver will send tcp ack message.</p><p>However, I want to understand if it is diameter application which responds back with ack or it is OS (RHEL) TCP/IP stack which sends this ack message ?</p><p>If OS - what is application's role in "TCP ACK" message ?</p><p>Thanks in advance !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '17, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-60155" class="comments-container"></div><div id="comment-tools-60155" class="comment-tools"></div><div class="clear"></div><div id="comment-60155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60157"></span>

<div id="answer-container-60157" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60157-score" class="post-score" title="current number of votes">2</div><span id="post-60157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vijay Gharge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The application has no role in the TCP ACK message. TCP Acknowledgements are sent by the TCP stack, which is part of the kernel.</p><p>The TCP ACK packet tells the sender that the data packet was received. The kernel pulls the data segment out of the packet and puts it in the receive buffer, and the application can then read the data from the buffer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '17, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-60157" class="comments-container"><span id="60159"></span><div id="comment-60159" class="comment"><div id="post-60159-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for answer. Though Jasper's response was little ahead of you, your response helped in understanding this case in detail. Hence accepting your comments as answer. <span>@Jasper</span>: Thanks to you too !</p></div><div id="comment-60159-info" class="comment-info"><span class="comment-age">(18 Mar '17, 00:39)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="60164"></span><div id="comment-60164" class="comment"><div id="post-60164-score" class="comment-score"></div><div class="comment-text"><p>That's fine, no worries - it's not about who's the fastest, but which one helped the most. Jim's is better, simple as that ;-)</p></div><div id="comment-60164-info" class="comment-info"><span class="comment-age">(18 Mar '17, 05:56)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-60157" class="comment-tools"></div><div class="clear"></div><div id="comment-60157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60156"></span>

<div id="answer-container-60156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60156-score" class="post-score" title="current number of votes">1</div><span id="post-60156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean a TCP ACK packet (with zero TCP payload bytes), it is a packet coming from the OS stack, acknowledging incoming data. The application has nothing to do with it, it's all stack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '17, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60156" class="comments-container"></div><div id="comment-tools-60156" class="comment-tools"></div><div class="clear"></div><div id="comment-60156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

