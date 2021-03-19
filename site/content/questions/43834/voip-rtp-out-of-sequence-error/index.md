+++
type = "question"
title = "Voip - RTP out of sequence error"
description = '''How does wireshark determine out of sequence for rtp packets. I have a capture that shows the first 5 packets coming from one voip device as &quot;out of sequence&quot; but the rest are good - it&#x27;s repeating the first 5 packets (i.e. 0, 1, 2, 3, 0, 1 etc). Coming from the other voip device all packets are in ...'''
date = "2015-07-02T18:35:00Z"
lastmod = "2015-07-03T07:35:00Z"
weight = 43834
keywords = [ "rtp", "voip" ]
aliases = [ "/questions/43834" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Voip - RTP out of sequence error](/questions/43834/voip-rtp-out-of-sequence-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43834-score" class="post-score" title="current number of votes">0</div><span id="post-43834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does wireshark determine out of sequence for rtp packets. I have a capture that shows the first 5 packets coming from one voip device as "out of sequence" but the rest are good - it's repeating the first 5 packets (i.e. 0, 1, 2, 3, 0, 1 etc). Coming from the other voip device all packets are in correct sequence. When we look at it through the player, it shows 99.9% of the rtp packets are out of sequence from both devices. It also will not play back. Is this a Wireshark bug? When you listen to the actual audio from the device, it sounds chopy.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '15, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-43834" class="comments-container"></div><div id="comment-tools-43834" class="comment-tools"></div><div class="clear"></div><div id="comment-43834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43852"></span>

<div id="answer-container-43852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43852-score" class="post-score" title="current number of votes">0</div><span id="post-43852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RFC is very clear about how sources must count their packets, unfortunately in real life many implementations screw this up, leaving the endpoints to fend for themselves. Wireshark tries to be as true to the source as possible, in that it should represent what the source sends out, vs. what an advanced, possibly DSP equipped, endpoint can restore from it.</p><p>As for this specific case it looks like the one device is in error, but without looking at the capture file it's hard to tell why this interferes with the other stream. If you can share the capture file this would allow for a more thorough analysis.</p><p>And: what wireshark version are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '15, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43852" class="comments-container"></div><div id="comment-tools-43852" class="comment-tools"></div><div class="clear"></div><div id="comment-43852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

