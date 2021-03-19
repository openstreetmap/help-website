+++
type = "question"
title = "What is the different between TCP Previous segment not captured and TCP Previous segment lost message?"
description = ''' What is the different between TCP Previous segment not captured and TCP Previous segment lost message? and Is this messages is critical error ?  thanks. '''
date = "2016-05-18T23:09:00Z"
lastmod = "2016-05-23T02:23:00Z"
weight = 52755
keywords = [ "errors" ]
aliases = [ "/questions/52755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the different between TCP Previous segment not captured and TCP Previous segment lost message?](/questions/52755/what-is-the-different-between-tcp-previous-segment-not-captured-and-tcp-previous-segment-lost-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52755-score" class="post-score" title="current number of votes">0</div><span id="post-52755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/TCP_segment_not_captured.png" alt="alt text" /></p><p>What is the different between TCP Previous segment not captured and TCP Previous segment lost message?</p><p>and Is this messages is critical error ?</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/d061a8f87e43eba3709731ee538b010a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DSLab&#39;s gravatar image" /><p><span>DSLab</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DSLab has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52755" class="comments-container"></div><div id="comment-tools-52755" class="comment-tools"></div><div class="clear"></div><div id="comment-52755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52756"></span>

<div id="answer-container-52756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52756-score" class="post-score" title="current number of votes">1</div><span id="post-52756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no difference - it's the same diagnostic message, but the wording was changed to be more exact. When a TCP segment isn't seen in the capture file there are a couple of reasons why:</p><ol><li>it was never on the "wire", because the capture device was placed at a location where the packet did not pass through (e.g. when routing is using different paths for both directions)</li><li>it was lost before it arrived at the capture device (and the destination), which means true packet loss</li><li>the capture device was too slow to record all packets (capture device performance problem)</li></ol><p>The old message "segment lost" suggested only the second reason. The new message simply says "the segment is not in the capture, for whatever reason". So it covers all three reasons instead of just one.</p><p>Regarding "critical error": it depends. When it is not in the capture file because of reason 2, and it happens a lot (costing time), it may get critical. Otherwise it may not, because packet loss simply happens in almost any network - but it doesn't need to be critical if a retransmission is fast enough not to slow things down.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '16, 01:10</strong> </span></p></div></div><div id="comments-container-52756" class="comments-container"><span id="52829"></span><div id="comment-52829" class="comment"><div id="post-52829-score" class="comment-score"></div><div class="comment-text"><p>thanks for your answer!</p></div><div id="comment-52829-info" class="comment-info"><span class="comment-age">(23 May '16, 01:58)</span> <span class="comment-user userinfo">DSLab</span></div></div><span id="52830"></span><div id="comment-52830" class="comment"><div id="post-52830-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-52830-info" class="comment-info"><span class="comment-age">(23 May '16, 02:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-52756" class="comment-tools"></div><div class="clear"></div><div id="comment-52756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

