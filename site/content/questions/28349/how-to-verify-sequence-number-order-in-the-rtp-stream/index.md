+++
type = "question"
title = "How to verify sequence number order in the RTP stream"
description = '''I have a file capture of 5000 RTP packets. I need to verify if the packets are recieved in the same sequence as sent. How do i check if there is any out of sequence packet. If i have to check it manually, then i have to look into the sequence number if each packet to find out the out of seq packet. ...'''
date = "2013-12-23T13:09:00Z"
lastmod = "2013-12-27T05:43:00Z"
weight = 28349
keywords = [ "hell", "they" ]
aliases = [ "/questions/28349" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to verify sequence number order in the RTP stream](/questions/28349/how-to-verify-sequence-number-order-in-the-rtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28349-score" class="post-score" title="current number of votes">0</div><span id="post-28349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a file capture of 5000 RTP packets. I need to verify if the packets are recieved in the same sequence as sent. How do i check if there is any out of sequence packet. If i have to check it manually, then i have to look into the sequence number if each packet to find out the out of seq packet.</p><p>Is there any filter of tool which can do this for me.</p><p>Thanks, Naveen</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hell" rel="tag" title="see questions tagged &#39;hell&#39;">hell</span> <span class="post-tag tag-link-they" rel="tag" title="see questions tagged &#39;they&#39;">they</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '13, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/e73c3bcfc47510ff6e48bf34fa444fd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nnandago&#39;s gravatar image" /><p><span>nnandago</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nnandago has no accepted answers">0%</span></p></div></div><div id="comments-container-28349" class="comments-container"></div><div id="comment-tools-28349" class="comment-tools"></div><div class="clear"></div><div id="comment-28349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28373"></span>

<div id="answer-container-28373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28373-score" class="post-score" title="current number of votes">0</div><span id="post-28373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the RTP stream analysis feature of Wireshark and look for packets which are marked not-ok.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-28373" class="comments-container"><span id="28434"></span><div id="comment-28434" class="comment"><div id="post-28434-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. That helped a lot.</p></div><div id="comment-28434-info" class="comment-info"><span class="comment-age">(27 Dec '13, 05:30)</span> <span class="comment-user userinfo">nnandago</span></div></div><span id="28436"></span><div id="comment-28436" class="comment"><div id="post-28436-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-28436-info" class="comment-info"><span class="comment-age">(27 Dec '13, 05:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28373" class="comment-tools"></div><div class="clear"></div><div id="comment-28373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

