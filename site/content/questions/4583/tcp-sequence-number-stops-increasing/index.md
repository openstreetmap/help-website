+++
type = "question"
title = "tcp sequence number stops increasing"
description = '''Hi, I&#x27;m trying to understand why a TCP conversation between client and server ends with the client sending a FIN after many packets have been exchanged back and forth. The only thing I can see that might be an issue is that after a while, the sequence number from the server stops increasing even tho...'''
date = "2011-06-15T18:21:00Z"
lastmod = "2011-06-15T22:55:00Z"
weight = 4583
keywords = [ "tcp" ]
aliases = [ "/questions/4583" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp sequence number stops increasing](/questions/4583/tcp-sequence-number-stops-increasing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4583-score" class="post-score" title="current number of votes">0</div><span id="post-4583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to understand why a TCP conversation between client and server ends with the client sending a FIN after many packets have been exchanged back and forth. The only thing I can see that might be an issue is that after a while, the sequence number from the server stops increasing even though the client's packets are not empty.</p><p>Does this mean the server has not received these packets or has lost its place in the connection, or how do I interpret this result?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '11, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p><span>eelarry</span><br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div></div><div id="comments-container-4583" class="comments-container"></div><div id="comment-tools-4583" class="comment-tools"></div><div class="clear"></div><div id="comment-4583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4584"></span>

<div id="answer-container-4584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4584-score" class="post-score" title="current number of votes">0</div><span id="post-4584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be looking at the Acknowledgment Numbers coming back from the server. These indicate what the server receives. Non increment of the Sequence Numbers of the server packets seem to indicate that it has nothing to send or the receiver window is closed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '11, 22:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4584" class="comments-container"></div><div id="comment-tools-4584" class="comment-tools"></div><div class="clear"></div><div id="comment-4584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

