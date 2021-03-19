+++
type = "question"
title = "TCP and FIN packet"
description = '''Given that the ISN of a packet of a TCP flow is 4290000000 and the sequence number of the FIN packet is 100000, how do i find the size of the total file?'''
date = "2015-04-21T19:30:00Z"
lastmod = "2015-04-22T02:07:00Z"
weight = 41653
keywords = [ "number", "fin", "packet", "tcp", "sequence" ]
aliases = [ "/questions/41653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP and FIN packet](/questions/41653/tcp-and-fin-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41653-score" class="post-score" title="current number of votes">0</div><span id="post-41653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given that the ISN of a packet of a TCP flow is 4290000000 and the sequence number of the FIN packet is 100000, how do i find the size of the total file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 19:30</strong></p><img src="https://secure.gravatar.com/avatar/89dceb4d4bdc43e79f4cb408247d4c56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alicia%20Soh&#39;s gravatar image" /><p><span>Alicia Soh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alicia Soh has no accepted answers">0%</span></p></div></div><div id="comments-container-41653" class="comments-container"></div><div id="comment-tools-41653" class="comment-tools"></div><div class="clear"></div><div id="comment-41653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41664"></span>

<div id="answer-container-41664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41664-score" class="post-score" title="current number of votes">1</div><span id="post-41664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't, at least not reliably, because the sequence number is "only" 32 bits and you can't say for sure how often it wrapped during the file transfer. Also, there may be multiple files transferred in one TCP session, which again denies deduction of the file sizes.</p><p>It's usually better to use the high level protocol fields carrying the file size to determine it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41664" class="comments-container"></div><div id="comment-tools-41664" class="comment-tools"></div><div class="clear"></div><div id="comment-41664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

