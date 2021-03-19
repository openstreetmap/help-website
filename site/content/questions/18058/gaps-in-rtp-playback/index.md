+++
type = "question"
title = "Gaps in RTP Playback"
description = '''I&#x27;ve come across a number of VoIP calls that when decoded in wireshark show an odd time distortion between the two audio legs. For instance leg A -&amp;gt; B shows audio beginning at 2 seconds and continues until 32 seconds. Leg A &amp;lt;- B shows a small amount of audio up until 2 second, then a yellow ba...'''
date = "2013-01-29T15:52:00Z"
lastmod = "2013-02-01T00:58:00Z"
weight = 18058
keywords = [ "playback", "audio", "rtp", "gap" ]
aliases = [ "/questions/18058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Gaps in RTP Playback](/questions/18058/gaps-in-rtp-playback)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18058-score" class="post-score" title="current number of votes">0</div><span id="post-18058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've come across a number of VoIP calls that when decoded in wireshark show an odd time distortion between the two audio legs.</p><p>For instance leg A -&gt; B shows audio beginning at 2 seconds and continues until 32 seconds. Leg A &lt;- B shows a small amount of audio up until 2 second, then a yellow bar in the playback window, then no activity until say 35 seconds, another yellow bar, and then audio until 65 seconds.</p><p>I see this fairly commonly, but it's perplexing, and for calls where the legs are this far off I'll usually export as RAW and then import into something like audacity and they play perfectly synced.</p><p>Is there a reason this happens or anything I can do within wireshark to correct it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-playback" rel="tag" title="see questions tagged &#39;playback&#39;">playback</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-gap" rel="tag" title="see questions tagged &#39;gap&#39;">gap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/72c7afb4a99d2bc517281a272cd6ba72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mulloy&#39;s gravatar image" /><p><span>Mulloy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mulloy has no accepted answers">0%</span></p></div></div><div id="comments-container-18058" class="comments-container"></div><div id="comment-tools-18058" class="comment-tools"></div><div class="clear"></div><div id="comment-18058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18221"></span>

<div id="answer-container-18221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18221-score" class="post-score" title="current number of votes">0</div><span id="post-18221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without having looked at the capture I would guess the RTP timestamps make an (illegal) jump. You ignore that part when you export raw audio and play that. Would you have an RTP player, you would see an event raised in the jitter buffer, as the playout engine has to skip through time. But that's what your VoIP equipment has to do to handle such non-compliant RTP streams.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18221" class="comments-container"></div><div id="comment-tools-18221" class="comment-tools"></div><div class="clear"></div><div id="comment-18221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

