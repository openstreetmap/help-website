+++
type = "question"
title = "Filter to remove display of rdp packets"
description = '''What is the proper filter to use that will prevent the display of rdp, tcp source and destination 3389, packets?'''
date = "2013-07-10T08:56:00Z"
lastmod = "2013-07-10T09:06:00Z"
weight = 22814
keywords = [ "filter", "rdp", "remove", "display" ]
aliases = [ "/questions/22814" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter to remove display of rdp packets](/questions/22814/filter-to-remove-display-of-rdp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22814-score" class="post-score" title="current number of votes">0</div><span id="post-22814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the proper filter to use that will prevent the display of rdp, tcp source and destination 3389, packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/10156942c28427cce55d40c3ca649e67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnspin&#39;s gravatar image" /><p><span>johnspin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnspin has no accepted answers">0%</span></p></div></div><div id="comments-container-22814" class="comments-container"></div><div id="comment-tools-22814" class="comment-tools"></div><div class="clear"></div><div id="comment-22814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22815"></span>

<div id="answer-container-22815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22815-score" class="post-score" title="current number of votes">1</div><span id="post-22815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>try "not tcp.port==3389"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22815" class="comments-container"><span id="22816"></span><div id="comment-22816" class="comment"><div id="post-22816-score" class="comment-score"></div><div class="comment-text"><p>!tcp.port==3389 worked. Thanks.</p></div><div id="comment-22816-info" class="comment-info"><span class="comment-age">(10 Jul '13, 09:06)</span> <span class="comment-user userinfo">johnspin</span></div></div></div><div id="comment-tools-22815" class="comment-tools"></div><div class="clear"></div><div id="comment-22815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

