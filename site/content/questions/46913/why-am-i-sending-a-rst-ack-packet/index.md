+++
type = "question"
title = "Why am I sending a [RST, ACK] packet?"
description = '''So I&#x27;ve been developing client/server software (for an MMORPG). Sometimes, randomly it would seem, users get disconnected from the server for no reason... We finally managed to capture this incident using WireShark... It would seem the client is sending a [RST, ACK] packet to the server. Why could t...'''
date = "2015-10-25T12:37:00Z"
lastmod = "2015-10-26T02:11:00Z"
weight = 46913
keywords = [ "rst", "rst+ack" ]
aliases = [ "/questions/46913" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I sending a \[RST, ACK\] packet?](/questions/46913/why-am-i-sending-a-rst-ack-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46913-score" class="post-score" title="current number of votes">0</div><span id="post-46913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I've been developing client/server software (for an MMORPG).</p><p>Sometimes, randomly it would seem, users get disconnected from the server for no reason...</p><p>We finally managed to capture this incident using WireShark...</p><p>It would seem the client is sending a [RST, ACK] packet to the server.</p><p>Why could this be happening? The dedicated computer hosting the server has a firewall on, but it is set to allow connections from the port that the client connects to... On top of that the clients ARE able to connect, they just disconnect sometimes...</p><p>Here's a picture of the packet in question, <a href="http://puu.sh/kXkEe/3607a35510.jpg">http://puu.sh/kXkEe/3607a35510.jpg</a></p><p>It has the same Ack# as the previous packet, so here's a picture of that one too... <a href="http://puu.sh/kXkMk/e2d7911022.jpg">http://puu.sh/kXkMk/e2d7911022.jpg</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '15, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/824d26857db745e387ff98bb578c5f07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ricky%20Rodrigues&#39;s gravatar image" /><p><span>Ricky Rodrigues</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ricky Rodrigues has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '15, 12:55</strong> </span></p></div></div><div id="comments-container-46913" class="comments-container"><span id="46914"></span><div id="comment-46914" class="comment"><div id="post-46914-score" class="comment-score"></div><div class="comment-text"><p>I think it is the same picture.</p></div><div id="comment-46914-info" class="comment-info"><span class="comment-age">(25 Oct '15, 12:43)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46916"></span><div id="comment-46916" class="comment"><div id="post-46916-score" class="comment-score"></div><div class="comment-text"><p>Sorry here is the other SS... <a href="http://puu.sh/kXkMk/e2d7911022.jpg">http://puu.sh/kXkMk/e2d7911022.jpg</a></p></div><div id="comment-46916-info" class="comment-info"><span class="comment-age">(25 Oct '15, 12:54)</span> <span class="comment-user userinfo">Ricky Rodrigues</span></div></div><span id="46917"></span><div id="comment-46917" class="comment"><div id="post-46917-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace on public accessible place (e.g. cloudshark.com)?</p></div><div id="comment-46917-info" class="comment-info"><span class="comment-age">(25 Oct '15, 15:02)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46913" class="comment-tools"></div><div class="clear"></div><div id="comment-46913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46915"></span>

<div id="answer-container-46915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46915-score" class="post-score" title="current number of votes">0</div><span id="post-46915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not so easy to tell with just this screenshot. But the session looks quite calm until this RST shows up. If I were you I would look deeper at the 192.168.0.2 side, and look what the app log is telling you. Because, in this case it seems to me that the most probably reasons for this RST is an app related problem at the 192.168.0.2 side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '15, 12:54</strong> </span></p></div></div><div id="comments-container-46915" class="comments-container"></div><div id="comment-tools-46915" class="comment-tools"></div><div class="clear"></div><div id="comment-46915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46925"></span>

<div id="answer-container-46925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46925-score" class="post-score" title="current number of votes">0</div><span id="post-46925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am not an expert with wireshark but looking at the pics the client side window value is always low and there are no window updates being pushed through so this could be a good place to look also.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/1d67795c1484b0652b735a3827dcb9b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m0rph&#39;s gravatar image" /><p><span>m0rph</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m0rph has no accepted answers">0%</span></p></div></div><div id="comments-container-46925" class="comments-container"></div><div id="comment-tools-46925" class="comment-tools"></div><div class="clear"></div><div id="comment-46925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

