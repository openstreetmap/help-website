+++
type = "question"
title = "How to filter out TCP ACKs?"
description = '''Hi, How is it possible that I filter out (remove) the packets that are only TCP ACKs in a capture? I want to use it in tshark.'''
date = "2015-06-02T04:10:00Z"
lastmod = "2015-06-02T04:21:00Z"
weight = 42826
keywords = [ "filter", "capture-filter", "packet-capture", "tcp", "tshark" ]
aliases = [ "/questions/42826" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter out TCP ACKs?](/questions/42826/how-to-filter-out-tcp-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42826-score" class="post-score" title="current number of votes">0</div><span id="post-42826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>How is it possible that I filter out (remove) the packets that are only TCP ACKs in a capture? I want to use it in tshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '15, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/153acafac1c1aa00460b1cfa5632d4ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aby_mcs&#39;s gravatar image" /><p><span>aby_mcs</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aby_mcs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '15, 04:10</strong> </span></p></div></div><div id="comments-container-42826" class="comments-container"></div><div id="comment-tools-42826" class="comment-tools"></div><div class="clear"></div><div id="comment-42826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42827"></span>

<div id="answer-container-42827" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42827-score" class="post-score" title="current number of votes">3</div><span id="post-42827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aby_mcs has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. The filter is "tcp.flags.ack==0". But that will leave you with anything that isn't TCP plus a couple of SYN packets (if at all). Because even data packets will have the ACK flag set.</p><p>If you want to remove all packets that contain no data and just acknowledge data coming from the other side, use "tcp and not tcp.len==0", to filter away everything that isn't TCP or has no TCP payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '15, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42827" class="comments-container"></div><div id="comment-tools-42827" class="comment-tools"></div><div class="clear"></div><div id="comment-42827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

