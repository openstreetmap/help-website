+++
type = "question"
title = "H.323 RTP Stream showing as Gige Vision Protocol"
description = '''On the latest version 2.0.4 my RTP packets are being classified as Gige Vision during a h323 call. In an older version, 1.8x, they show properly as RTP. Is there a way to fix this behavior?'''
date = "2016-06-15T13:07:00Z"
lastmod = "2016-06-15T13:43:00Z"
weight = 53474
keywords = [ "voip" ]
aliases = [ "/questions/53474" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [H.323 RTP Stream showing as Gige Vision Protocol](/questions/53474/h323-rtp-stream-showing-as-gige-vision-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53474-score" class="post-score" title="current number of votes">0</div><span id="post-53474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On the latest version 2.0.4 my RTP packets are being classified as Gige Vision during a h323 call. In an older version, 1.8x, they show properly as RTP. Is there a way to fix this behavior?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '16, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/132238de2ed390fbc7fc67f100881af3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ols&#39;s gravatar image" /><p><span>Ols</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ols has no accepted answers">0%</span></p></div></div><div id="comments-container-53474" class="comments-container"></div><div id="comment-tools-53474" class="comment-tools"></div><div class="clear"></div><div id="comment-53474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53475"></span>

<div id="answer-container-53475" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53475-score" class="post-score" title="current number of votes">0</div><span id="post-53475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ols has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can turn off the gvcp dissecyor or do <span>@decode</span> <span class="__cf_email__" data-cfemail="d7b6a497">[email protected]</span> and select RTP. That dissector register for port 3956 so I assume your RTP packets are on that port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-53475" class="comments-container"><span id="53476"></span><div id="comment-53476" class="comment"><div id="post-53476-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-53476-info" class="comment-info"><span class="comment-age">(15 Jun '16, 13:43)</span> <span class="comment-user userinfo">Ols</span></div></div></div><div id="comment-tools-53475" class="comment-tools"></div><div class="clear"></div><div id="comment-53475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

