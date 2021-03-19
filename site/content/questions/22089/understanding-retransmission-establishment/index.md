+++
type = "question"
title = "understanding retransmission establishment"
description = '''Hi all, I was reviewing the following 3 way handshake and wanted to understand what is destination host saying regarding type of retransmission. From the traces it looks like the source host is telling to use SACK while there is no answer to that from the destination. 05:29:51.675626 IP 24.6.173.220...'''
date = "2013-06-15T11:21:00Z"
lastmod = "2013-06-15T16:27:00Z"
weight = 22089
keywords = [ "retransmission", "sack" ]
aliases = [ "/questions/22089" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [understanding retransmission establishment](/questions/22089/understanding-retransmission-establishment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22089-score" class="post-score" title="current number of votes">0</div><span id="post-22089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I was reviewing the following 3 way handshake and wanted to understand what is destination host saying regarding type of retransmission. From the traces it looks like the source host is telling to use SACK while there is no answer to that from the destination.</p><pre><code>05:29:51.675626 IP 24.6.173.220.26385 &gt; 198.66.239.146.80: Flags [S], seq 3242633023, win 8192, options [mss 1460,nop,wscale 2,nop,nop,sackOK], length 0
05:29:51.696997 IP 198.66.239.146.80 &gt; 24.6.173.220.26385: Flags [S.], seq 77540153, ack 3242633024, win 57344, options [mss 1460,nop,wscale 0], length 0
05:29:51.697185 IP 24.6.173.220.26385 &gt; 198.66.239.146.80: Flags [.], ack 1, win 16425, length 0</code></pre><p>Can you please explain how this works?</p><p>Thanks in advance, Edmond.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '13, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-22089" class="comments-container"></div><div id="comment-tools-22089" class="comment-tools"></div><div class="clear"></div><div id="comment-22089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22091"></span>

<div id="answer-container-22091" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22091-score" class="post-score" title="current number of votes">1</div><span id="post-22091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Edmond has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The client announces that it knows how SACK works, while the server doesn't announce it. That means that neither client nor server can use SACK since it only works if both parties do know how. It is not "no answer" from the destination, it's just an answer that tells the client that the server doesn't use SACK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '13, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22091" class="comments-container"><span id="22096"></span><div id="comment-22096" class="comment"><div id="post-22096-score" class="comment-score"></div><div class="comment-text"><p>So the type of ACK that the server will respond is that it supports the ACK type of the client or it doesn't, right?</p></div><div id="comment-22096-info" class="comment-info"><span class="comment-age">(15 Jun '13, 15:01)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="22098"></span><div id="comment-22098" class="comment"><div id="post-22098-score" class="comment-score">1</div><div class="comment-text"><p><a href="http://tools.ietf.org/html/rfc2018">RFC 2018</a> describes the way SACK works. There aren't "I support these types of ACK" announcements; there are just "I support SACK, so you can use it" options. So the server will either respond with "SACK permitted" or nothing.</p><p>At least as I read RFC 2018, in the connection you show, the server could send SACKs to the client if it wished to do so, as the client says "SACK permitted", but the client must not send SACKs to the server, as the server did not say "SACK permitted".</p></div><div id="comment-22098-info" class="comment-info"><span class="comment-age">(15 Jun '13, 16:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22091" class="comment-tools"></div><div class="clear"></div><div id="comment-22091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

