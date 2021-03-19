+++
type = "question"
title = "infiniband packet decode"
description = '''where do I find the sources for the infiniband packet decode ?'''
date = "2012-09-13T06:35:00Z"
lastmod = "2012-09-13T06:52:00Z"
weight = 14233
keywords = [ "infiniband" ]
aliases = [ "/questions/14233" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [infiniband packet decode](/questions/14233/infiniband-packet-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14233-score" class="post-score" title="current number of votes">0</div><span id="post-14233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>where do I find the sources for the infiniband packet decode ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-infiniband" rel="tag" title="see questions tagged &#39;infiniband&#39;">infiniband</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '12, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/2459b16afa99f54cce8bbd18d756808a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hal&#39;s gravatar image" /><p><span>Hal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hal has no accepted answers">0%</span></p></div></div><div id="comments-container-14233" class="comments-container"><span id="14236"></span><div id="comment-14236" class="comment"><div id="post-14236-score" class="comment-score"></div><div class="comment-text"><p>Got it. Thanks.</p></div><div id="comment-14236-info" class="comment-info"><span class="comment-age">(13 Sep '12, 06:52)</span> <span class="comment-user userinfo">Hal</span></div></div></div><div id="comment-tools-14233" class="comment-tools"></div><div class="clear"></div><div id="comment-14233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14234"></span>

<div id="answer-container-14234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14234-score" class="post-score" title="current number of votes">0</div><span id="post-14234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the source tree:</p><blockquote><p><code>epan\dissectors\packet-infiniband.c</code><br />
<code>epan\dissectors\packet-infiniband_sdp.c</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Sep '12, 06:43</strong> </span></p></div></div><div id="comments-container-14234" class="comments-container"></div><div id="comment-tools-14234" class="comment-tools"></div><div class="clear"></div><div id="comment-14234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14235"></span>

<div id="answer-container-14235" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14235-score" class="post-score" title="current number of votes">0</div><span id="post-14235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>epan\dissectors&gt;ls packet-inf* packet-infiniband.c<br />
packet-infiniband.h packet-infiniband_sdp.c</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></br></p></div></div><div id="comments-container-14235" class="comments-container"></div><div id="comment-tools-14235" class="comment-tools"></div><div class="clear"></div><div id="comment-14235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

