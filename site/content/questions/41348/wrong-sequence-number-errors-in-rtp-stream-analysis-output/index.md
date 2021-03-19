+++
type = "question"
title = "Wrong sequence number errors in RTP Stream Analysis output"
description = '''I&#x27;m using Version 1.12.4 of Wireshark (Win64) and am attempting to analyse RTP packets that are carrying an MPEG-2 transport stream. What I&#x27;m finding is that any RTP packet that contains a &quot;null&quot; MPEG-2 transport stream packet (PID 0x1ff) is flagged as a NULL packet in the main Wireshark display. Th...'''
date = "2015-04-10T04:22:00Z"
lastmod = "2015-04-10T08:07:00Z"
weight = 41348
keywords = [ "rtp", "analysis", "mpeg2-ts" ]
aliases = [ "/questions/41348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong sequence number errors in RTP Stream Analysis output](/questions/41348/wrong-sequence-number-errors-in-rtp-stream-analysis-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41348-score" class="post-score" title="current number of votes">0</div><span id="post-41348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Version 1.12.4 of Wireshark (Win64) and am attempting to analyse RTP packets that are carrying an MPEG-2 transport stream.</p><p>What I'm finding is that any RTP packet that contains a "null" MPEG-2 transport stream packet (PID 0x1ff) is flagged as a NULL packet in the main Wireshark display.</p><p>The upshot of this appears to be that the RTP stream analyser ignores these NULL RTP packets which inevitably results in a "Wrong sequence number" entry in the analysis output as the packet sequence number is deemed to be non-contiguous.</p><p>This seems wrong to me. Null MPEG-2 transport stream packets are perfectly legal and to be expected in order to hit a particular fixed bit rate. The presence of them in the stream shouldn't result in an error being flagged in the analysis tool.</p><p>Or am I not understanding something correctly and Wireshark really is trying to tell me something useful?</p><p>Thanks in advance for any information offered.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-mpeg2-ts" rel="tag" title="see questions tagged &#39;mpeg2-ts&#39;">mpeg2-ts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/9f09039bdf7955ed043321dfcf281b1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanB&#39;s gravatar image" /><p><span>IanB</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '15, 04:24</strong> </span></p></div></div><div id="comments-container-41348" class="comments-container"></div><div id="comment-tools-41348" class="comment-tools"></div><div class="clear"></div><div id="comment-41348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41351"></span>

<div id="answer-container-41351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41351-score" class="post-score" title="current number of votes">0</div><span id="post-41351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark RTP analysis has no notion of profiles for the various transports. It basically only understands the transport of continues voice (G.711) and a bit of Comfort Noise and DTMF signalling. Since other profiles make use of similar methods they come out fairly well in these analysis, but certain details may cause problems, like you've seen.</p><p>Unfortunately it is a significant job to make a fault tolerant MitM RTP endpoint which can handle all profiles, which is what would have to be done in Wireshark, and so far this has not happened.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '15, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41351" class="comments-container"></div><div id="comment-tools-41351" class="comment-tools"></div><div class="clear"></div><div id="comment-41351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

