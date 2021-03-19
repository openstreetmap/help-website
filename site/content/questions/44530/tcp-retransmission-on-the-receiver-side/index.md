+++
type = "question"
title = "TCP Retransmission on the receiver side"
description = '''How does Wireshark knows that a packet on the receiver side is being retransmitted. I mean it makes sense on the sender side: Wireshark sees two identical packets (with the same sequence number) being sent, and so it will mark the second packet as being retransmitted. Note that I am not talking abou...'''
date = "2015-07-27T08:37:00Z"
lastmod = "2015-07-27T10:01:00Z"
weight = 44530
keywords = [ "windows", "tcp", "wireshark" ]
aliases = [ "/questions/44530" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Retransmission on the receiver side](/questions/44530/tcp-retransmission-on-the-receiver-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44530-score" class="post-score" title="current number of votes">0</div><span id="post-44530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark knows that a packet on the receiver side is being retransmitted. I mean it makes sense on the sender side: Wireshark sees two identical packets (with the same sequence number) being sent, and so it will mark the second packet as being retransmitted.</p><p>Note that I am not talking about two identical packets being received and TCP will ignore one of them. What I talking about is when I have only one packet received and Wireshark has marked it as being retransmitted. Is it because for example I receive <strong>packet 1</strong> and then I receive <strong>packet 3</strong>, and then when <strong>packet 2</strong> arrive, Wireshark will assume that <strong>packet 2</strong> is being retransmitted?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/e15d1d4db326472a053064f3e26fc079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_857&#39;s gravatar image" /><p><span>John_857</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_857 has no accepted answers">0%</span></p></div></div><div id="comments-container-44530" class="comments-container"></div><div id="comment-tools-44530" class="comment-tools"></div><div class="clear"></div><div id="comment-44530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44533"></span>

<div id="answer-container-44533" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44533-score" class="post-score" title="current number of votes">0</div><span id="post-44533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John_857 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark makes an educated guess, based on the delta time of the "old" packet arriving relative to the packet loss - if it is following the gap really quick it's marked out of order, otherwise it's called a retransmission.</p><p>A retransmission can never be sent before the receiver has notified the sender about the missing segment(s), so a true retransmission cannot arrive earlier than the round trip time. Exceptions are when the sending stack is going crazy for whatever reason, sending retransmissions way too fast.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '15, 10:03</strong> </span></p></div></div><div id="comments-container-44533" class="comments-container"></div><div id="comment-tools-44533" class="comment-tools"></div><div class="clear"></div><div id="comment-44533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

