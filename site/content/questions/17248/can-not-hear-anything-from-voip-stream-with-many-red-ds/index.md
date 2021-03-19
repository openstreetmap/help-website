+++
type = "question"
title = "Can not hear anything from VoIP stream with many red Ds"
description = '''I did a VoIP filter with G.729 codec. However, after I decoded the stream and played them, I could not hear anything. There were many Ds (Drop by Jitter Buffer) in these stream, which you can see in the image. Does many red Ds make the voice quality lower? Can I do furthermore on these data? Any hel...'''
date = "2012-12-26T18:51:00Z"
lastmod = "2012-12-27T01:01:00Z"
weight = 17248
keywords = [ "sound", "decode", "voip", "no" ]
aliases = [ "/questions/17248" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can not hear anything from VoIP stream with many red Ds](/questions/17248/can-not-hear-anything-from-voip-stream-with-many-red-ds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17248-score" class="post-score" title="current number of votes">0</div><span id="post-17248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did a VoIP filter with G.729 codec. However, after I decoded the stream and played them, I could not hear anything. There were many Ds (Drop by Jitter Buffer) in these stream, which you can see in the image. Does many red Ds make the voice quality lower? Can I do furthermore on these data?<img src="https://osqa-ask.wireshark.org/upfiles/ws.png" alt="alt text" /></p><p>Any help is highly appreciate. Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sound" rel="tag" title="see questions tagged &#39;sound&#39;">sound</span> <span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '12, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/6201b3aba14257d205e6ef1f9d6b013a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lamont%20Hoang&#39;s gravatar image" /><p><span>Lamont Hoang</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lamont Hoang has no accepted answers">0%</span></p></img></div></div><div id="comments-container-17248" class="comments-container"></div><div id="comment-tools-17248" class="comment-tools"></div><div class="clear"></div><div id="comment-17248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17254"></span>

<div id="answer-container-17254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17254-score" class="post-score" title="current number of votes">0</div><span id="post-17254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark RTP stream decode is limited to G.711 (A-law or u-law) only. That means that additional features, like silence suppression and other codecs, aren't supported out-of-the-box. I don't have an G.729 stream at hand to check, but you might want to try ticking the box "Use RTP timestamp" to see what that brings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17254" class="comments-container"></div><div id="comment-tools-17254" class="comment-tools"></div><div class="clear"></div><div id="comment-17254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

