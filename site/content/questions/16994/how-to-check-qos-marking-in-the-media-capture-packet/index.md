+++
type = "question"
title = "how to check QOS marking in the media capture packet"
description = '''Hi, I am trying to find what QOS marking endpoint is sending and receiving on the media captured packets, Kindly advise what field in the SIP SDP I can a look to find QOS marking? Thanks, ZB'''
date = "2012-12-17T12:37:00Z"
lastmod = "2012-12-17T14:10:00Z"
weight = 16994
keywords = [ "rtp" ]
aliases = [ "/questions/16994" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to check QOS marking in the media capture packet](/questions/16994/how-to-check-qos-marking-in-the-media-capture-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16994-score" class="post-score" title="current number of votes">0</div><span id="post-16994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to find what QOS marking endpoint is sending and receiving on the media captured packets, Kindly advise what field in the SIP SDP I can a look to find QOS marking?</p><p>Thanks,</p><p>ZB</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/8d94dfd6c366366fc379cff0f53a6c51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zubik2&#39;s gravatar image" /><p><span>zubik2</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zubik2 has one accepted answer">100%</span></p></div></div><div id="comments-container-16994" class="comments-container"></div><div id="comment-tools-16994" class="comment-tools"></div><div class="clear"></div><div id="comment-16994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16995"></span>

<div id="answer-container-16995" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16995-score" class="post-score" title="current number of votes">0</div><span id="post-16995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Never mind, I figured it out. DSCP value is under IPv4 header Differentiated Services Field.</p><p>Regards,</p><p>ZB</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/8d94dfd6c366366fc379cff0f53a6c51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zubik2&#39;s gravatar image" /><p><span>zubik2</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zubik2 has one accepted answer">100%</span></p></div></div><div id="comments-container-16995" class="comments-container"></div><div id="comment-tools-16995" class="comment-tools"></div><div class="clear"></div><div id="comment-16995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

