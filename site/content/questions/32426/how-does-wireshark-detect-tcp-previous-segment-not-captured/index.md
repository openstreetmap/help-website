+++
type = "question"
title = "How does wireshark detect &quot;TCP previous segment not captured&quot;?"
description = '''Hi, I am testing network problem. I see lots of messages &quot;TCP previous segment not captured&quot; in wireshark. It seems payload size is changed (more in detail, reduced). In this case, how does wireshark detect &quot;TCP previous segment not captured&quot; ? Maybe I guess that wireshark uses sequence number and s...'''
date = "2014-05-02T08:30:00Z"
lastmod = "2014-05-02T08:44:00Z"
weight = 32426
keywords = [ "danny" ]
aliases = [ "/questions/32426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark detect "TCP previous segment not captured"?](/questions/32426/how-does-wireshark-detect-tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32426-score" class="post-score" title="current number of votes">0</div><span id="post-32426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am testing network problem. I see lots of messages "TCP previous segment not captured" in wireshark. It seems payload size is changed (more in detail, reduced).</p><p>In this case, how does wireshark detect "TCP previous segment not captured" ? Maybe I guess that wireshark uses sequence number and some other header information. Thanks for the help in advance.</p><p>Danny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-danny" rel="tag" title="see questions tagged &#39;danny&#39;">danny</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/2fb776a40e87ce7dd18d14266f8ade4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danny&#39;s gravatar image" /><p><span>danny</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danny has no accepted answers">0%</span></p></div></div><div id="comments-container-32426" class="comments-container"></div><div id="comment-tools-32426" class="comment-tools"></div><div class="clear"></div><div id="comment-32426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32428"></span>

<div id="answer-container-32428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32428-score" class="post-score" title="current number of votes">1</div><span id="post-32428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP expert module of Wireshark tracks sequence numbers for each TCP connection and detects gaps, meaning that there are TCP segments missing or out-of-order. "TCP previous segment not captured" means that a gap was detected, either because the packet was lost on the way from sender to receiver, or that the capture device recording the packets wasn't fast enough to deal with the incoming flood of packets.</p><p>Check if you see "TCP ACKed unseen segment" messages as well - if you do, you're most likely having capture performance problems and need to get a better (=faster) capture device when recording packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32428" class="comments-container"></div><div id="comment-tools-32428" class="comment-tools"></div><div class="clear"></div><div id="comment-32428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

