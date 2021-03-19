+++
type = "question"
title = "How to decode Vivox format RTP to sound?"
description = '''Hi community, I&#x27;m currently playing Overwatch by Blizzard Entertainment. It uses Vivox sound sdk to provide Team Chat function. I captured some 300 seconds of in-game chat stream,and want to decode it. Sadly Wireshark 2.2.5(on Windows 10) can&#x27;t decode this &quot;Vivoxvani&quot;(RTP Payload Type 126 and 127) R...'''
date = "2017-04-01T21:41:00Z"
lastmod = "2017-04-02T03:59:00Z"
weight = 60513
keywords = [ "overwatch", "vivox", "rtp" ]
aliases = [ "/questions/60513" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode Vivox format RTP to sound?](/questions/60513/how-to-decode-vivox-format-rtp-to-sound)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi community, I'm currently playing Overwatch by Blizzard Entertainment. It uses Vivox sound sdk to provide Team Chat function. I captured some 300 seconds of in-game chat stream,and want to decode it. Sadly Wireshark 2.2.5(on Windows 10) can't decode this "Vivoxvani"(RTP Payload Type 126 and 127) RTP stream. Can anyone help me on this issue? Thanks.</p></div><div id="question-tags" class="tags-container tags">overwatch vivox rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '17, 21:41</strong></p><img src="https://secure.gravatar.com/avatar/b8ef241dba23c6b9a9a439341bc091a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breakshadow&#39;s gravatar image" /><p>Breakshadow<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breakshadow has no accepted answers">0%</span></p></div></div><div id="comments-container-60513" class="comments-container"></div><div id="comment-tools-60513" class="comment-tools"></div><div class="clear"></div><div id="comment-60513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60519"></span>

<div id="answer-container-60519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60519-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you'll have to do (without knowing the specifics of this codec) is to save the raw RTP payload and post process that into audio. Wireshark itself have very little codec support, besides straight up PCM A-law/u-law.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60519" class="comments-container"><span id="60541"></span><div id="comment-60541" class="comment"><div id="post-60541-score" class="comment-score"></div><div class="comment-text"><p>Thanks. But it seems that wireshark cannot correctly address the whole RTP stream. It is cut partially,and cannot be save fully as raw. Because Vivox RTP seems strange, the payload type changes from 127 to 126, and to some other numbers. That seems not good.</p></div><div id="comment-60541-info" class="comment-info"><span class="comment-age">(03 Apr '17, 03:38)</span> Breakshadow</div></div></div><div id="comment-tools-60519" class="comment-tools"></div><div class="clear"></div><div id="comment-60519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

