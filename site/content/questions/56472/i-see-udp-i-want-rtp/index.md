+++
type = "question"
title = "i see udp i want rtp"
description = '''how to convert the udp to rtp this is a webrtc capture'''
date = "2016-10-17T09:42:00Z"
lastmod = "2016-10-18T03:09:00Z"
weight = 56472
keywords = [ "to", "utp", "decode_rtp", "webrtc" ]
aliases = [ "/questions/56472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [i see udp i want rtp](/questions/56472/i-see-udp-i-want-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56472-score" class="post-score" title="current number of votes">0</div><span id="post-56472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to convert the udp to rtp this is a webrtc capture</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-utp" rel="tag" title="see questions tagged &#39;utp&#39;">utp</span> <span class="post-tag tag-link-decode_rtp" rel="tag" title="see questions tagged &#39;decode_rtp&#39;">decode_rtp</span> <span class="post-tag tag-link-webrtc" rel="tag" title="see questions tagged &#39;webrtc&#39;">webrtc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/d0b948d936fe46343beb03aeba77b29a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="interfaith&#39;s gravatar image" /><p><span>interfaith</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="interfaith has no accepted answers">0%</span></p></div></div><div id="comments-container-56472" class="comments-container"><span id="56483"></span><div id="comment-56483" class="comment"><div id="post-56483-score" class="comment-score"></div><div class="comment-text"><p>which version of wireshark are you using?</p></div><div id="comment-56483-info" class="comment-info"><span class="comment-age">(17 Oct '16, 23:23)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="56484"></span><div id="comment-56484" class="comment"><div id="post-56484-score" class="comment-score"></div><div class="comment-text"><p>WebRTC typically uses SRTP AFAIK, so even if you enable RTP you will not be able to use the telephony analysis tools since the payload is encrypted. SRTP is on my wishlist/todo list for some time now.</p></div><div id="comment-56484-info" class="comment-info"><span class="comment-age">(18 Oct '16, 00:54)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="56492"></span><div id="comment-56492" class="comment"><div id="post-56492-score" class="comment-score"></div><div class="comment-text"><p><span>@Lekensteyn</span>, I'm hereby voting +1000 for SRTP decryption in general.</p><p>But use of telephony analysis tools should be possible except payload playback and export as audio. On the other hand, WebRTC typically uses compressing codecs so even after decryption, the payload playback and export as audio still won't work until someone implements the decompression part of the codec. So export of raw (decrypted) payload followed by decompression using an external tool would be necessary to hear the audio.</p></div><div id="comment-56492-info" class="comment-info"><span class="comment-age">(18 Oct '16, 03:09)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56472" class="comment-tools"></div><div class="clear"></div><div id="comment-56472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56478"></span>

<div id="answer-container-56478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56478-score" class="post-score" title="current number of votes">0</div><span id="post-56478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to menu Analyze, select Enabled Protocols. Search for RTP. Tick 'rtp_udp'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56478" class="comments-container"></div><div id="comment-tools-56478" class="comment-tools"></div><div class="clear"></div><div id="comment-56478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

