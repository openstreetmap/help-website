+++
type = "question"
title = "RTP packet  loss"
description = '''Hi, I have a Wireshark RTP trace, taken between 2 telecomm nodes A and B. Currently I am observing packet loss on A( as per statistics in A node) upon taking the interface traces,I could see Wrong sequence number on each of the streams between B to A(where B is source and A is Destination). So my qu...'''
date = "2013-01-27T02:46:00Z"
lastmod = "2013-01-27T04:27:00Z"
weight = 17977
keywords = [ "rtp" ]
aliases = [ "/questions/17977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RTP packet loss](/questions/17977/rtp-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17977-score" class="post-score" title="current number of votes">0</div><span id="post-17977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a Wireshark RTP trace, taken between 2 telecomm nodes A and B. Currently I am observing packet loss on A( as per statistics in A node) upon taking the interface traces,I could see Wrong sequence number on each of the streams between B to A(where B is source and A is Destination).</p><p>So my queries are</p><p>1.) Packet loss is considered by wrong sequence number on each stream individually or Please confirm the allocation of sequence number for multi stream bidirectional communication. 2.) Although i am not having any RTP packet lost registered at B, but from the traces I could see the wrong sequence(using RTP stream analysis) number on the streams from A to B. Any probable reason why this behavior ? 3.) If a have a router between my nodes A and B, then can router detects RTP packet lost ? If yes then how?</p><p>Thanks in Advance.</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '13, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/354a7648a9223ba8d8f2d047d8cdc52d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varsha%20Mishra&#39;s gravatar image" /><p><span>Varsha Mishra</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varsha Mishra has no accepted answers">0%</span></p></div></div><div id="comments-container-17977" class="comments-container"></div><div id="comment-tools-17977" class="comment-tools"></div><div class="clear"></div><div id="comment-17977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17980"></span>

<div id="answer-container-17980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17980-score" class="post-score" title="current number of votes">0</div><span id="post-17980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If there's codecs being used other that PCMA or PCMU, or additional features like VAD/CN, RTP events etc. then you can expect these warnings to be triggered. Than it's up to you to decide if this is really a problem according to the applicable profile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '13, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17980" class="comments-container"><span id="17982"></span><div id="comment-17982" class="comment"><div id="post-17982-score" class="comment-score"></div><div class="comment-text"><p>Hi I think Wiresharks lost packet count gets thrown off by "out-of-sequence" packets duplicted packets and the like.</p></div><div id="comment-17982-info" class="comment-info"><span class="comment-age">(27 Jan '13, 04:27)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-17980" class="comment-tools"></div><div class="clear"></div><div id="comment-17980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

