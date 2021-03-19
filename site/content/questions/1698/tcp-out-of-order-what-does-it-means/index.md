+++
type = "question"
title = "&quot;TCP out of order &quot; what does it means ?!!!"
description = '''I have packet with protocol HTTP and named as &quot;TCP [Out-Of-Order] HTTP/1.1 200 OK (text/html)&quot; please explain what does it means ?'''
date = "2011-01-10T23:54:00Z"
lastmod = "2011-01-11T05:45:00Z"
weight = 1698
keywords = [ "of", "order", "tcp", "out" ]
aliases = [ "/questions/1698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["TCP out of order " what does it means ?!!!](/questions/1698/tcp-out-of-order-what-does-it-means)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1698-score" class="post-score" title="current number of votes">0</div><span id="post-1698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have packet with protocol HTTP and named as "TCP [Out-Of-Order] HTTP/1.1 200 OK (text/html)"</p><p>please explain what does it means ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-of" rel="tag" title="see questions tagged &#39;of&#39;">of</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '11, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/516fcdaa4577fef84a8c3f6e4d239db4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALMahbob&#39;s gravatar image" /><p><span>ALMahbob</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALMahbob has no accepted answers">0%</span></p></div></div><div id="comments-container-1698" class="comments-container"></div><div id="comment-tools-1698" class="comment-tools"></div><div class="clear"></div><div id="comment-1698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1699"></span>

<div id="answer-container-1699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1699-score" class="post-score" title="current number of votes">2</div><span id="post-1699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It simply means that particular frame was received in a different order from which it was sent (after a later packet in the sequence). It is not generally a problem. It probably indicates there are multiple paths between source and destination - and one travels a through a longer path. It means TCP has slightly more work to reassemble segments in the correct order.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '11, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1699" class="comments-container"><span id="1701"></span><div id="comment-1701" class="comment"><div id="post-1701-score" class="comment-score"></div><div class="comment-text"><p>Thank you a lot ,,,</p></div><div id="comment-1701-info" class="comment-info"><span class="comment-age">(11 Jan '11, 05:45)</span> <span class="comment-user userinfo">ALMahbob</span></div></div></div><div id="comment-tools-1699" class="comment-tools"></div><div class="clear"></div><div id="comment-1699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

