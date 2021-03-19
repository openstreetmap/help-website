+++
type = "question"
title = "set marker bit in RTP"
description = '''hi, i have a pcap containing RTP packets. in each packets of this pcap, marker bit is set and sequence number increments for each packet. is it rigth that marker bit is set in each packet?'''
date = "2017-07-13T06:34:00Z"
lastmod = "2017-07-13T07:15:00Z"
weight = 62744
keywords = [ "marker", "rtp" ]
aliases = [ "/questions/62744" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [set marker bit in RTP](/questions/62744/set-marker-bit-in-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62744-score" class="post-score" title="current number of votes">0</div><span id="post-62744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i have a pcap containing RTP packets. in each packets of this pcap, marker bit is set and sequence number increments for each packet. is it rigth that marker bit is set in each packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p><span>ghader</span><br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '17, 06:36</strong> </span></p></div></div><div id="comments-container-62744" class="comments-container"></div><div id="comment-tools-62744" class="comment-tools"></div><div class="clear"></div><div id="comment-62744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62745"></span>

<div id="answer-container-62745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62745-score" class="post-score" title="current number of votes">1</div><span id="post-62745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The marker bit is subject to much discussion. The relevance of the marker bit is defined by the so-called RTP profile used. That profile is the set of rules which apply to that RTP stream. It defines for instance the codec used to encode the audio and/or video. It defines how events in the media stream are signalled in the packets, etc.</p><p>A common use of the marker bit is for synchronisation. eg. when the profile allows for silence suppression (that is: no packets are transmitted when there's silence) it is helpful for the decoder to know when speech resumes. This is flagged by the marker bit. You might ask 'but when there's silence no packets are transmitted, so why do you need the marker bit?' That is because intermediate RTP packets are used to update the background noise level.</p><p>Another example of the use of the marker bit is to signal the start of a new video frame in a sequence of RTP packets carrying video data. This is then according to a video RTP profile.</p><p>So depending on the profile used, this may or may not be as specified. On the other hand, many applications don't depend heavily on the marker bit. <a href="http://www.cs.columbia.edu/~hgs/rtp/faq.html">It varies</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '17, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62745" class="comments-container"></div><div id="comment-tools-62745" class="comment-tools"></div><div class="clear"></div><div id="comment-62745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

