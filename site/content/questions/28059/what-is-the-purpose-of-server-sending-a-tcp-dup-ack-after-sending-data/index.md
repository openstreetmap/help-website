+++
type = "question"
title = "what is the purpose of server sending a [TCP Dup ACK] after sending data?"
description = '''Did some search but couldn&#x27;t find a good answer about the tcp dup ack. The server sent data on frame 4, immediately after that on frame 5, server sends a [TCP Dup ACK], the difference is between frame 4 and 5 is the seq number, what is the purpose of this ack from server? The detail view of the atta...'''
date = "2013-12-12T10:25:00Z"
lastmod = "2013-12-13T22:27:00Z"
weight = 28059
keywords = [ "dup" ]
aliases = [ "/questions/28059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is the purpose of server sending a \[TCP Dup ACK\] after sending data?](/questions/28059/what-is-the-purpose-of-server-sending-a-tcp-dup-ack-after-sending-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28059-score" class="post-score" title="current number of votes">0</div><span id="post-28059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Did some search but couldn't find a good answer about the tcp dup ack. The server sent data on frame 4, immediately after that on frame 5, server sends a [TCP Dup ACK], the difference is between frame 4 and 5 is the seq number, what is the purpose of this ack from server?</p><p>The detail view of the attachment is from frame4. thanks a lot for any response.<a href="https://osqa-ask.wireshark.org/upfiles/tcpdup.JPG">link text</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup" rel="tag" title="see questions tagged &#39;dup&#39;">dup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/3005d4836284975e36e239ba2b6f8c11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="czhang&#39;s gravatar image" /><p><span>czhang</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="czhang has no accepted answers">0%</span></p></div></div><div id="comments-container-28059" class="comments-container"><span id="28080"></span><div id="comment-28080" class="comment"><div id="post-28080-score" class="comment-score"></div><div class="comment-text"><p>anyone has any idea? appreciate it.</p></div><div id="comment-28080-info" class="comment-info"><span class="comment-age">(13 Dec '13, 08:19)</span> <span class="comment-user userinfo">czhang</span></div></div></div><div id="comment-tools-28059" class="comment-tools"></div><div class="clear"></div><div id="comment-28059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28095"></span>

<div id="answer-container-28095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28095-score" class="post-score" title="current number of votes">0</div><span id="post-28095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, here's my one 'idea'</p><p>The trace was taken after the original packet has been GRE-tunneled, so the sequence of packets is not necessarily what was actually sent by the server.</p><p>If packet #5 was actually sent before #4 and was passed by #4 on its way to the trace capture point you end up seeing what you see - which doesn't make much sense to me either.</p><p>You might want to look at the ip.id in the inner packets to verify the original sequence at the sender - or take a trace directly at the server (outside the GRE tunnel).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 22:27</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28095" class="comments-container"></div><div id="comment-tools-28095" class="comment-tools"></div><div class="clear"></div><div id="comment-28095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

