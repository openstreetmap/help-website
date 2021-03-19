+++
type = "question"
title = "TCP Window"
description = '''Hi, Wanted to understand the Behaviour of TCP reception when The Window Size is Increased. Should The Speed at which the Packets are Transmitted by the Server increase??? Assuming that there is processing the Packets very fast. '''
date = "2014-02-03T01:05:00Z"
lastmod = "2014-02-03T03:50:00Z"
weight = 29387
keywords = [ "tcppackets" ]
aliases = [ "/questions/29387" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window](/questions/29387/tcp-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29387-score" class="post-score" title="current number of votes">0</div><span id="post-29387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Wanted to understand the Behaviour of TCP reception when The Window Size is Increased. Should The Speed at which the Packets are Transmitted by the Server increase??? Assuming that there is processing the Packets very fast.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '14, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/15fde9059967ec3ea4f509717682ffc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amin%20Khan&#39;s gravatar image" /><p><span>Amin Khan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amin Khan has no accepted answers">0%</span></p></div></div><div id="comments-container-29387" class="comments-container"></div><div id="comment-tools-29387" class="comment-tools"></div><div class="clear"></div><div id="comment-29387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29393"></span>

<div id="answer-container-29393" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29393-score" class="post-score" title="current number of votes">1</div><span id="post-29393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The speed can do three things when the window size is increased: it can go up, it can stay the same, and it can go down. It all depends on the latency and bandwidth of the links between client and server. The more bandwidth and the higher the latency, the higher the window size needs to be.</p><p>Performance goes up when the line has a high latency and a lot of bandwidth and the window increases. If the line has different speeds (lets say 1GBit and 10Mbit) in different segments the device that has to break down the fast speed to the slow speed can be slammed shut with packets if the window size increases, which leads to packet drop and thus to a slower speed than before.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '14, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29393" class="comments-container"></div><div id="comment-tools-29393" class="comment-tools"></div><div class="clear"></div><div id="comment-29393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

