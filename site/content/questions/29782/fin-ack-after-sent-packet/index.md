+++
type = "question"
title = "FIN ACK after sent packet"
description = '''I&#x27;m implementing the ssh ftp protocol to connect to an sftp server on port 22 and I keep getting a FIN ACK from the server after I send either a ssh binary packet SSH_KEX_MSG_DH_GEX_REQUEST or an SSH_MSG_KEXINIT, which seems to close the connection. I want to keep the connection open so that I can e...'''
date = "2014-02-12T08:47:00Z"
lastmod = "2014-02-12T09:33:00Z"
weight = 29782
keywords = [ "sshftp" ]
aliases = [ "/questions/29782" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FIN ACK after sent packet](/questions/29782/fin-ack-after-sent-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29782-score" class="post-score" title="current number of votes">0</div><span id="post-29782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm implementing the ssh ftp protocol to connect to an sftp server on port 22 and I keep getting a FIN ACK from the server after I send either a ssh binary packet SSH_KEX_MSG_DH_GEX_REQUEST or an SSH_MSG_KEXINIT, which seems to close the connection. I want to keep the connection open so that I can establish the server authentication. What could be causing this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sshftp" rel="tag" title="see questions tagged &#39;sshftp&#39;">sshftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '14, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/7522ea64bae74f233d3945bf28488794?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikepol&#39;s gravatar image" /><p><span>mikepol</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikepol has no accepted answers">0%</span></p></div></div><div id="comments-container-29782" class="comments-container"></div><div id="comment-tools-29782" class="comment-tools"></div><div class="clear"></div><div id="comment-29782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29783"></span>

<div id="answer-container-29783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29783-score" class="post-score" title="current number of votes">2</div><span id="post-29783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What could be causing this?</p></blockquote><p>a bug in your ssh protocol implementation, which causes the server to close the session. You should enable debugging in the SSH server and check if/what it is reporting.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29783" class="comments-container"><span id="29784"></span><div id="comment-29784" class="comment"><div id="post-29784-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I'll give that a shot.</p></div><div id="comment-29784-info" class="comment-info"><span class="comment-age">(12 Feb '14, 09:27)</span> <span class="comment-user userinfo">mikepol</span></div></div><span id="29785"></span><div id="comment-29785" class="comment"><div id="post-29785-score" class="comment-score"></div><div class="comment-text"><p>O.K.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-29785-info" class="comment-info"><span class="comment-age">(12 Feb '14, 09:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29783" class="comment-tools"></div><div class="clear"></div><div id="comment-29783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

