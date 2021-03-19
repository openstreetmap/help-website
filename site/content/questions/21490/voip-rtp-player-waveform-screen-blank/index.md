+++
type = "question"
title = "VoIP RTP player waveform screen blank"
description = '''Occasionally when I want to play back/analyze voip rtp traffic, I end up with no waveforms. I have this happen on Windows, Linux, and OS X platforms. Screenshot available at http://www.apple2pl.us/screenshot.png Is there something that I&#x27;m not doing that I should be? '''
date = "2013-05-27T05:16:00Z"
lastmod = "2013-05-27T23:22:00Z"
weight = 21490
keywords = [ "player", "waveform", "rtp", "voip", "blank" ]
aliases = [ "/questions/21490" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP RTP player waveform screen blank](/questions/21490/voip-rtp-player-waveform-screen-blank)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21490-score" class="post-score" title="current number of votes">0</div><span id="post-21490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Occasionally when I want to play back/analyze voip rtp traffic, I end up with no waveforms. I have this happen on Windows, Linux, and OS X platforms.</p><p>Screenshot available at <a href="http://www.apple2pl.us/screenshot.png">http://www.apple2pl.us/screenshot.png</a></p><p>Is there something that I'm not doing that I should be?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-player" rel="tag" title="see questions tagged &#39;player&#39;">player</span> <span class="post-tag tag-link-waveform" rel="tag" title="see questions tagged &#39;waveform&#39;">waveform</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-blank" rel="tag" title="see questions tagged &#39;blank&#39;">blank</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '13, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/8f766cc8f3564b65c5705cf3a402ce9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cracklincrotch&#39;s gravatar image" /><p><span>cracklincrotch</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cracklincrotch has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '13, 05:17</strong> </span></p></div></div><div id="comments-container-21490" class="comments-container"></div><div id="comment-tools-21490" class="comment-tools"></div><div class="clear"></div><div id="comment-21490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21500"></span>

<div id="answer-container-21500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21500-score" class="post-score" title="current number of votes">0</div><span id="post-21500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know, wireshark RTP stream decoding is limited to G.711 (A-law or u-law). Are you sure the captures with a 'blank screen' are encoded with G.711?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '13, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21500" class="comments-container"><span id="21501"></span><div id="comment-21501" class="comment"><div id="post-21501-score" class="comment-score"></div><div class="comment-text"><p>All RTP packets are G.711 u-law. Hitting the player button plays the audio fine. Just no waveforms, marked wrong timestamps, dropped packets, etc.</p><p>I should add, this is not the first time I've had this issue. There is no pattern to it. But I've seen this happen from time to time since 2011.</p></div><div id="comment-21501-info" class="comment-info"><span class="comment-age">(27 May '13, 14:23)</span> <span class="comment-user userinfo">cracklincrotch</span></div></div><span id="21504"></span><div id="comment-21504" class="comment"><div id="post-21504-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have this happen on Windows, Linux, and OS X platforms.<br />
I've seen this happen from time to time since 2011.</p></blockquote><p>sounds like a yet undiscovered (and hard to detect) bug.</p></div><div id="comment-21504-info" class="comment-info"><span class="comment-age">(27 May '13, 23:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21500" class="comment-tools"></div><div class="clear"></div><div id="comment-21500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

