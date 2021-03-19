+++
type = "question"
title = "Why do TCP ACK packets have length &gt; 0"
description = '''Hello, I can see that some ACK packet without PSH flag sends data as well. I have thought that ACK packet will always have len=0, but I see packets with ACK flag only and len=1380. '''
date = "2015-01-06T08:07:00Z"
lastmod = "2015-01-06T10:58:00Z"
weight = 38904
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/38904" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why do TCP ACK packets have length &gt; 0](/questions/38904/why-do-tcp-ack-packets-have-length-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38904-score" class="post-score" title="current number of votes">0</div><span id="post-38904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I can see that some ACK packet without PSH flag sends data as well. I have thought that ACK packet will always have len=0, but I see packets with ACK flag only and len=1380.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '15, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/ebd0a43a556bbb894cf06fc35c5c6293?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Otas&#39;s gravatar image" /><p><span>Otas</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Otas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>06 Jan '15, 08:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38904" class="comments-container"></div><div id="comment-tools-38904" class="comment-tools"></div><div class="clear"></div><div id="comment-38904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38907"></span>

<div id="answer-container-38907" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38907-score" class="post-score" title="current number of votes">2</div><span id="post-38907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Otas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Its called as piggybacking,Piggybacking is a bi-directional data transmission technique. It makes the most of the sent data frames from receiver to emitter, adding the confirmation that the data frame sent by the sender was received successfully (ACK acknowledge). This practically means, that instead of sending an acknowledgement in an individual frame it is piggy-backed on the data frame</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '15, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-38907" class="comments-container"><span id="38911"></span><div id="comment-38911" class="comment"><div id="post-38911-score" class="comment-score"></div><div class="comment-text"><p>Hello Kishan,</p><p>thank you for lightning response. Fully clarified.</p><p>BR</p><p>Otas</p></div><div id="comment-38911-info" class="comment-info"><span class="comment-age">(06 Jan '15, 10:58)</span> <span class="comment-user userinfo">Otas</span></div></div></div><div id="comment-tools-38907" class="comment-tools"></div><div class="clear"></div><div id="comment-38907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38909"></span>

<div id="answer-container-38909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38909-score" class="post-score" title="current number of votes">1</div><span id="post-38909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After the SYN packet, every single packet will have the ACK bit set, so data packets are also ACK packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '15, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38909" class="comments-container"></div><div id="comment-tools-38909" class="comment-tools"></div><div class="clear"></div><div id="comment-38909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

