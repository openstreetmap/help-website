+++
type = "question"
title = "Excessive duplicate acknowledgements - what does it mean?"
description = '''I have a situation where when I transfer the same file bewteen two offices it takes three times longer in one direction when compared to the other direction. So in the slow direction Office A to Office B in my traces I can see an excessive number of duplicate acknowlegements occuring at different ti...'''
date = "2013-11-04T00:39:00Z"
lastmod = "2013-11-07T04:35:00Z"
weight = 26651
keywords = [ "duplicate", "excessive", "acknowledgments" ]
aliases = [ "/questions/26651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Excessive duplicate acknowledgements - what does it mean?](/questions/26651/excessive-duplicate-acknowledgements-what-does-it-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26651-score" class="post-score" title="current number of votes">0</div><span id="post-26651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a situation where when I transfer the same file bewteen two offices it takes three times longer in one direction when compared to the other direction. So in the slow direction Office A to Office B in my traces I can see an excessive number of duplicate acknowlegements occuring at different times of the tarnsfer. I'm guessing this is causing my transfers to run slower in that direction. If anything I was expecting to see re-try requests (i.e. the packets not making it to Office B) as I have an interface in the path where I see output discards which may be due to NetApp microburts so I'm perplexed as to why I'm seeing so may duplicate acknowledgments coming back. The packet has obvously made it to the destingation so why so many acknowledgements. When I say excessive I typically see 200 duplicates acknowledging the same packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-excessive" rel="tag" title="see questions tagged &#39;excessive&#39;">excessive</span> <span class="post-tag tag-link-acknowledgments" rel="tag" title="see questions tagged &#39;acknowledgments&#39;">acknowledgments</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '13, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/2aa41a5c6d6479a0b61ebe88bd9a60fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MPN&#39;s gravatar image" /><p><span>MPN</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MPN has no accepted answers">0%</span></p></div></div><div id="comments-container-26651" class="comments-container"></div><div id="comment-tools-26651" class="comment-tools"></div><div class="clear"></div><div id="comment-26651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26662"></span>

<div id="answer-container-26662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26662-score" class="post-score" title="current number of votes">0</div><span id="post-26662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what does it mean?</p></blockquote><p>hard to tell without a capture file. There are a lot of possible reasons.</p><p>Based on your description (difference between the direction of data transfer), it could be some kind of QoS solution that tries to hold back the ACKs, to enforce a slowdown of the transfer in one direction.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '13, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26662" class="comments-container"><span id="26709"></span><div id="comment-26709" class="comment"><div id="post-26709-score" class="comment-score"></div><div class="comment-text"><p>ok will take a look through the path.</p><p>Thanks Mark</p></div><div id="comment-26709-info" class="comment-info"><span class="comment-age">(07 Nov '13, 04:00)</span> <span class="comment-user userinfo">MPN</span></div></div><span id="26710"></span><div id="comment-26710" class="comment"><div id="post-26710-score" class="comment-score"></div><div class="comment-text"><p>what kind of connection do you have between the offices? MPLS, Ethernet, etc.?</p></div><div id="comment-26710-info" class="comment-info"><span class="comment-age">(07 Nov '13, 04:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26662" class="comment-tools"></div><div class="clear"></div><div id="comment-26662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

