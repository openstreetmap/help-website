+++
type = "question"
title = "tcp port 135"
description = '''hi guys, if i want to connect from client to an application server on TCP port 135 (and the port is open on the server) but let&#x27;s say there is a security device along the way from client to server that will block TCP port 135 it will not allow to establish the connection, right ?  Thank you for clea...'''
date = "2015-12-11T02:00:00Z"
lastmod = "2015-12-11T05:55:00Z"
weight = 48441
keywords = [ "block", "tcp" ]
aliases = [ "/questions/48441" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tcp port 135](/questions/48441/tcp-port-135)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48441-score" class="post-score" title="current number of votes">0</div><span id="post-48441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>if i want to connect from client to an application server on TCP port 135 (and the port is open on the server) but let's say there is a security device along the way from client to server that will block TCP port 135 it will not allow to establish the connection, right ?</p><p>Thank you for clearing my doubts !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-48441" class="comments-container"></div><div id="comment-tools-48441" class="comment-tools"></div><div class="clear"></div><div id="comment-48441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48442"></span>

<div id="answer-container-48442" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48442-score" class="post-score" title="current number of votes">1</div><span id="post-48442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adasko has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. That's what ACLs (Access Control Lists) and Firewalls do. Depending on the blocking mechanism you will either see a "blocked" result or a "rejected" result. The difference is that for "block" you'll not see any kind of answer to your connection attempt, while "reject" will tell you that you're not allowed to access that port. Firewalls usually "block" to avoid being detected/tested - your connection simply fails but you cannot easily tell who blocked the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48442" class="comments-container"><span id="48443"></span><div id="comment-48443" class="comment"><div id="post-48443-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper for your clear answer ! out of curiosity, is it common to block TCP port 135 ?</p><p>thank you</p></div><div id="comment-48443-info" class="comment-info"><span class="comment-age">(11 Dec '15, 03:06)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="48446"></span><div id="comment-48446" class="comment"><div id="post-48446-score" class="comment-score">1</div><div class="comment-text"><p>On perimeter firewalls (meaning: the ones at the edge to the internet): yes, absolutely. Internal firewalls may or may not do this, depending on the network segmentation and security requirements.</p></div><div id="comment-48446-info" class="comment-info"><span class="comment-age">(11 Dec '15, 05:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-48442" class="comment-tools"></div><div class="clear"></div><div id="comment-48442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

