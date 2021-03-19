+++
type = "question"
title = "audio synchronization"
description = '''I am trying to reconstruct two rtp streams (audio). I was using rtp timestamp as a clock rate to reconstruct and synchronization. But for few instances i see that the rtp timestamp is not linear. So how do i calculate the actual time? Is there any formula for this? thanks rahul'''
date = "2014-02-02T21:16:00Z"
lastmod = "2014-02-07T09:17:00Z"
weight = 29385
keywords = [ "timestamp", "rtp" ]
aliases = [ "/questions/29385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [audio synchronization](/questions/29385/audio-synchronization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29385-score" class="post-score" title="current number of votes">0</div><span id="post-29385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to reconstruct two rtp streams (audio). I was using rtp timestamp as a clock rate to reconstruct and synchronization. But for few instances i see that the rtp timestamp is not linear. So how do i calculate the actual time? Is there any formula for this?</p><p>thanks rahul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '14, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/4e7b8d9cab960a29a748b0e218c6af9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rahulhgowda&#39;s gravatar image" /><p><span>rahulhgowda</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rahulhgowda has no accepted answers">0%</span></p></div></div><div id="comments-container-29385" class="comments-container"><span id="29394"></span><div id="comment-29394" class="comment"><div id="post-29394-score" class="comment-score"></div><div class="comment-text"><p>What does the RTP timestamp do it it's not linear? Does it jump, does it coincide with a codec change?</p></div><div id="comment-29394-info" class="comment-info"><span class="comment-age">(03 Feb '14, 04:31)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="29506"></span><div id="comment-29506" class="comment"><div id="post-29506-score" class="comment-score"></div><div class="comment-text"><p>I am using kapanga soft-phone for capturing RTP and later trying to reconstruct RTP. For synchronization i am filling silence with the difference of two voice packet RTP timestamp. I see that when i mute and return back the rtp timestamp jumps lot. I also noticed that no rtp flow on mute. I was not able to handle silence insertion during this situation.<br />
</p><p>eg: G711ulaw - from wireshark</p><pre><code>0.00 -------first packet
...
78.459090(time) - 1179(seq)---- rtp voice packet timestamp 963360
78.467873(time) - 1180 (seq) --- Comfort Noise   timestamp 963520
78.532292(time) - 1181 (seq) --- Comfort Noise   timestamp 964000
93.541290(time) - 1182(seq)---- rtp voice packet timestamp 1201760</code></pre><p>From the above example i see that frame time for two voice packet gives the difference of(93.541290 - 78.459090 = 15.0822) where as when i do the calculations using rtp timestamp its different, ((1201760 - 963360)/8000 = 29.8). So i if fill silence for 29.8 sec my audio goes out of sync.</p></div><div id="comment-29506-info" class="comment-info"><span class="comment-age">(06 Feb '14, 21:09)</span> <span class="comment-user userinfo">rahulhgowda</span></div></div></div><div id="comment-tools-29385" class="comment-tools"></div><div class="clear"></div><div id="comment-29385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29512"></span>

<div id="answer-container-29512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29512-score" class="post-score" title="current number of votes">0</div><span id="post-29512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So it does jump, and there's a codec change. It's also related to a specific action (mute). These are all possible causes for the sending RTP endpoint to mess up the timestamping, and leave it to the receiver to figure out. Unfortunately there's little you can do other than follow the lead of the packet time stamps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '14, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-29512" class="comments-container"><span id="29540"></span><div id="comment-29540" class="comment"><div id="post-29540-score" class="comment-score"></div><div class="comment-text"><p>thank you for the response. Actually i am trying to be a receiver here and want to reconstruct the audio. Its not exactly a codec change rather a Comfort Noise(CN) packet(Silence packet). Both codec (g711) and CN has same sample rate(8000).</p><p>So you are suggesting to use the packet time stamps.But i have concerns using this as i am using UDP as transport and there are chances of out of order packets and it may not work as desired(just a thought)</p></div><div id="comment-29540-info" class="comment-info"><span class="comment-age">(07 Feb '14, 09:17)</span> <span class="comment-user userinfo">rahulhgowda</span></div></div></div><div id="comment-tools-29512" class="comment-tools"></div><div class="clear"></div><div id="comment-29512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

