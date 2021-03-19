+++
type = "question"
title = "Does Wireshark check the RTP payload type when extracting audio"
description = '''I have a stream of RTP packets some of which have payload type = 0 (G711) and some have payload type = 101 (DTMF). I have an application where both in-band and out-of-band DTMF digits are transmitted. When I use Wireshark to capture the RTP stream and extract the payload to a .au file, the audio sou...'''
date = "2011-04-18T10:35:00Z"
lastmod = "2012-06-29T10:31:00Z"
weight = 3578
keywords = [ "pops", "audio", "distortion", "rtp", "clicks" ]
aliases = [ "/questions/3578" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark check the RTP payload type when extracting audio](/questions/3578/does-wireshark-check-the-rtp-payload-type-when-extracting-audio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3578-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a stream of RTP packets some of which have payload type = 0 (G711) and some have payload type = 101 (DTMF). I have an application where both in-band and out-of-band DTMF digits are transmitted. When I use Wireshark to capture the RTP stream and extract the payload to a .au file, the audio sounds bad. From a plot I can see that the audio in the .au file contains spikes which causes the pops and clicks in the audio.</p><p>My guess is that Wireshark does not distinguish between payload types in an RTP stream. It just sees the RTP packets as one payload stream (when in fact there are two: payload type 101 and 0). So wireshark mistakenly extracts the payload of each RTP packet and decodes the RTP payload stream as if it was one audio signal.</p><p>Can somebody confirm this?</p></div><div id="question-tags" class="tags-container tags">pops audio distortion rtp clicks</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/f1c30d56f9fdd06191fd241fa534d5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john38274&#39;s gravatar image" /><p>john38274<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john38274 has no accepted answers">0%</span></p></div></div><div id="comments-container-3578" class="comments-container"></div><div id="comment-tools-3578" class="comment-tools"></div><div class="clear"></div><div id="comment-3578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3586"></span>

<div id="answer-container-3586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3586-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is equipped to handle G.711 A-law and u-law encoded RTP streams. Other streams, or multiplexed streams like RFC 2833, cannot be properly handled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3586" class="comments-container"><span id="12329"></span><div id="comment-12329" class="comment"><div id="post-12329-score" class="comment-score"></div><div class="comment-text"><p>it shows payload type dynamic 96 for my case. But the system ensures that packet should be type G.711 a -law. Wireshark can't play RTP for my case. Anything need to be modified for my case?</p></div><div id="comment-12329-info" class="comment-info"><span class="comment-age">(29 Jun '12, 09:28)</span> Mamun</div></div></div><div id="comment-tools-3586" class="comment-tools"></div><div class="clear"></div><div id="comment-3586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12331"></span>

<div id="answer-container-12331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could try to filter out payload type 101 and try again. Also make sure that you do not have duplicate RTP packets. If the case you can try edicap -d</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '12, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/cdbb36db3a1bc78b87865c0e5c0e2e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grinob&#39;s gravatar image" /><p>grinob<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grinob has no accepted answers">0%</span></p></div></div><div id="comments-container-12331" class="comments-container"></div><div id="comment-tools-12331" class="comment-tools"></div><div class="clear"></div><div id="comment-12331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

