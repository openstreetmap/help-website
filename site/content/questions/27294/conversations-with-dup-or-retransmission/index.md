+++
type = "question"
title = "Conversations with DUP or Retransmission"
description = '''I read how to get a count of conversations - my next question is is there a way to count how many different conversations have DUP or TCP Retransmission packets in them?'''
date = "2013-11-22T13:43:00Z"
lastmod = "2013-11-22T14:46:00Z"
weight = 27294
keywords = [ "dup-ack", "conversation", "retransmissions" ]
aliases = [ "/questions/27294" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conversations with DUP or Retransmission](/questions/27294/conversations-with-dup-or-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27294-score" class="post-score" title="current number of votes">0</div><span id="post-27294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I read how to get a count of conversations - my next question is is there a way to count how many different conversations have DUP or TCP Retransmission packets in them?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/76308c22a91c18badcc7a4fae2408c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Platzen&#39;s gravatar image" /><p><span>Platzen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Platzen has no accepted answers">0%</span></p></div></div><div id="comments-container-27294" class="comments-container"></div><div id="comment-tools-27294" class="comment-tools"></div><div class="clear"></div><div id="comment-27294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27295"></span>

<div id="answer-container-27295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27295-score" class="post-score" title="current number of votes">2</div><span id="post-27295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several ways to do that. One fast and simple method is this:</p><ul><li>set a display filter for the conditions you're looking for, e.g. <code>tcp.analysis.retransmission or tcp.analysis.duplicate_ack</code> (add whatever field you need)</li><li>show the conversations: <code>Statistics -&gt; Conversations -&gt; TCP [tab]</code><br />
</li><li>enable the following option: <code>Limit to display filter</code> (at the bottom of the window)</li><li>what you now see are those TCP connections that match the display filter, hence those connections with retransmissions and dup ACK (in this example)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '13, 15:03</strong> </span></p></div></div><div id="comments-container-27295" class="comments-container"></div><div id="comment-tools-27295" class="comment-tools"></div><div class="clear"></div><div id="comment-27295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

