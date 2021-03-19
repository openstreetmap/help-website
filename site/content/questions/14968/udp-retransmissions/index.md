+++
type = "question"
title = "UDP Retransmissions"
description = '''Is there a mechanism or script that derives the MAC layer (not TCP) retransmission statistics for a UDP connection using Block Acks? I assume that such a script would analyze repeating 802.11 sequence numbers and possibly Block Ack bitmaps.'''
date = "2012-10-12T12:05:00Z"
lastmod = "2012-10-18T12:43:00Z"
weight = 14968
keywords = [ "ack", "retransmission", "block" ]
aliases = [ "/questions/14968" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP Retransmissions](/questions/14968/udp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14968-score" class="post-score" title="current number of votes">0</div><span id="post-14968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a mechanism or script that derives the MAC layer (not TCP) retransmission statistics for a UDP connection using Block Acks? I assume that such a script would analyze repeating 802.11 sequence numbers and possibly Block Ack bitmaps.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '12, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/55fa12360adc0075a07b4312027d6fc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ReidW&#39;s gravatar image" /><p><span>ReidW</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ReidW has no accepted answers">0%</span></p></div></div><div id="comments-container-14968" class="comments-container"></div><div id="comment-tools-14968" class="comment-tools"></div><div class="clear"></div><div id="comment-14968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14979"></span>

<div id="answer-container-14979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14979-score" class="post-score" title="current number of votes">0</div><span id="post-14979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no bulit-in (in the protocol) ethernet and/or UDP retransmission mechanism. So, the short answer: No there is no mechanism or script to derive that information.</p><p>What is the reason for your question? Do you see packet loss?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '12, 01:58</strong> </span></p></div></div><div id="comments-container-14979" class="comments-container"><span id="15019"></span><div id="comment-15019" class="comment"><div id="post-15019-score" class="comment-score"></div><div class="comment-text"><p>I see retransmissions using a AirPcap. Are you saying that the Block Ack bitmask is only used by higher layers and is not related to any low level retransmission mechanism?</p></div><div id="comment-15019-info" class="comment-info"><span class="comment-age">(15 Oct '12, 09:42)</span> <span class="comment-user userinfo">ReidW</span></div></div><span id="15022"></span><div id="comment-15022" class="comment"><div id="post-15022-score" class="comment-score"></div><div class="comment-text"><p>Ah, you are talking about Wifi networks (I missed the <strong>802.11</strong> in your question).</p><p>Looking a second time at your question, I'm not sure if there is a way to derive retransmission statistics from the Block-Acks.</p><p>However, I will have a more detailed look at the problem. Can you post a sample capture somewhere?</p></div><div id="comment-15022-info" class="comment-info"><span class="comment-age">(15 Oct '12, 12:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15023"></span><div id="comment-15023" class="comment"><div id="post-15023-score" class="comment-score"></div><div class="comment-text"><p>Maybe from repeated sequence numbers? <a href="https://www.filesanywhere.com/fs/v.aspx?v=8a716b865b5e6db2a0a9">https://www.filesanywhere.com/fs/v.aspx?v=8a716b865b5e6db2a0a9</a></p></div><div id="comment-15023-info" class="comment-info"><span class="comment-age">(15 Oct '12, 17:59)</span> <span class="comment-user userinfo">ReidW</span></div></div><span id="15090"></span><div id="comment-15090" class="comment"><div id="post-15090-score" class="comment-score"></div><div class="comment-text"><p>I know that Riverbed Cascade Pilot and AirMagnet both report retrans stats - they must be counting repeated sequence numbers. Is there a way to script this for a Wireshark trace?</p></div><div id="comment-15090-info" class="comment-info"><span class="comment-age">(18 Oct '12, 12:43)</span> <span class="comment-user userinfo">ReidW</span></div></div></div><div id="comment-tools-14979" class="comment-tools"></div><div class="clear"></div><div id="comment-14979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

