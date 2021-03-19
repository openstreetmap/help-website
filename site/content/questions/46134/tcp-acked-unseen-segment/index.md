+++
type = "question"
title = "TCP ACked Unseen Segment"
description = '''Hi all, I am getting the TCP ACKed Unseen segment. Could anyone explain the stats of these packets. Why is it like this? 760 10:11:22.438873 10.2.248.47 10.110.64.48 TCP 58 [TCP ACKed unseen segment] 42161→3200 [RST, ACK] Seq=322 Ack=2420 Win=0 Len=0 761 10:11:22.438878 10.110.64.48 10.2.248.47 TCP ...'''
date = "2015-09-24T23:38:00Z"
lastmod = "2015-09-25T02:16:00Z"
weight = 46134
keywords = [ "ack", "unseen_segment", "rst+ack" ]
aliases = [ "/questions/46134" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACked Unseen Segment](/questions/46134/tcp-acked-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46134-score" class="post-score" title="current number of votes">0</div><span id="post-46134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am getting the TCP ACKed Unseen segment. Could anyone explain the stats of these packets. Why is it like this? <code>760 10:11:22.438873 10.2.248.47 10.110.64.48    TCP 58  [TCP ACKed unseen segment] 42161→3200 [RST, ACK] Seq=322 Ack=2420 Win=0 Len=0 761 10:11:22.438878 10.110.64.48    10.2.248.47 TCP 58  [TCP ACKed unseen segment] 3200→42161 [RST, ACK] Seq=2420 Ack=322 Win=0 Len=0</code></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-unseen_segment" rel="tag" title="see questions tagged &#39;unseen_segment&#39;">unseen_segment</span> <span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/d55e8327c384401466a4991eb8e826d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rcrkollam&#39;s gravatar image" /><p><span>rcrkollam</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rcrkollam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '15, 02:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46134" class="comments-container"></div><div id="comment-tools-46134" class="comment-tools"></div><div class="clear"></div><div id="comment-46134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46141"></span>

<div id="answer-container-46141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46141-score" class="post-score" title="current number of votes">0</div><span id="post-46141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"TCP ACKed unseen segment" means that this packet acknowledges data that wasn't captured. It was transferred okay, and the receiver acknowledges it, but Wireshark can't find the packet in the capture. This usually happens when the capture device wasn't fast enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-46141" class="comments-container"></div><div id="comment-tools-46141" class="comment-tools"></div><div class="clear"></div><div id="comment-46141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

