+++
type = "question"
title = "Duplicate Acks on a new circuit"
description = '''We have a new circuit that connects us to a trading providor. Initial http/https connectivity seems fine. When I try to download a 30MB file it is taking over 20 minutes and my capture shows many many TCP DUP ACK packets. How can I pinpoint the cause?'''
date = "2015-01-05T12:35:00Z"
lastmod = "2015-01-05T15:19:00Z"
weight = 38896
keywords = [ "tcpdupacks" ]
aliases = [ "/questions/38896" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Acks on a new circuit](/questions/38896/duplicate-acks-on-a-new-circuit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38896-score" class="post-score" title="current number of votes">0</div><span id="post-38896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a new circuit that connects us to a trading providor. Initial http/https connectivity seems fine. When I try to download a 30MB file it is taking over 20 minutes and my capture shows many many TCP DUP ACK packets. How can I pinpoint the cause?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdupacks" rel="tag" title="see questions tagged &#39;tcpdupacks&#39;">tcpdupacks</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/23fbd754dfc0458ba4a3891166276c68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EDK&#39;s gravatar image" /><p><span>EDK</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EDK has no accepted answers">0%</span></p></div></div><div id="comments-container-38896" class="comments-container"></div><div id="comment-tools-38896" class="comment-tools"></div><div class="clear"></div><div id="comment-38896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38897"></span>

<div id="answer-container-38897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38897-score" class="post-score" title="current number of votes">0</div><span id="post-38897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you see many DUP ACK packets you probably suffer from packet loss. Check if you have messages about lost/not capture segments and retransmissions. Filter for tcp.analysis.flags to see all TCP expert messages.</p><p>If you can, post a sample capture at <a href="http://www.cloudshark.org">Cloudshark</a>, and tell us the link so we can take a look. If you need to sanitize your data first, use <a href="http://www.tracewrangler.com">TraceWrangler</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '15, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38897" class="comments-container"></div><div id="comment-tools-38897" class="comment-tools"></div><div class="clear"></div><div id="comment-38897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

