+++
type = "question"
title = "URGENT: Units of rtp.timestamp and frame.time_relative"
description = '''I am using the fields rtp.timestamp and frame.time_relative for calcualtion of jitter. What are the units of these fields? milliseconds? '''
date = "2010-11-29T20:38:00Z"
lastmod = "2010-11-30T01:12:00Z"
weight = 1170
keywords = [ "rtp", "calculate", "time" ]
aliases = [ "/questions/1170" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [URGENT: Units of rtp.timestamp and frame.time\_relative](/questions/1170/urgent-units-of-rtptimestamp-and-frametime_relative)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1170-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the fields rtp.timestamp and frame.time_relative for calcualtion of jitter. What are the units of these fields? milliseconds?</p></div><div id="question-tags" class="tags-container tags">rtp calculate time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '10, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/da051abac41879aed4060d544d37fd6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skypemesm&#39;s gravatar image" /><p>skypemesm<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skypemesm has no accepted answers">0%</span></p></div></div><div id="comments-container-1170" class="comments-container"></div><div id="comment-tools-1170" class="comment-tools"></div><div class="clear"></div><div id="comment-1170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1174"></span>

<div id="answer-container-1174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1174-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>frame.time_relative is in units of seconds; it has a fractional part, so it can have a higher resolution than one second.</p><p>As for RTP, to quote <a href="http://www.ietf.org/rfc/rfc3550.txt">RFC 3550</a>, the specification for RTP, "The timestamp reflects the sampling instant of the first octet in the RTP data packet. The sampling instant MUST be derived from a clock that increments monotonically and linearly in time to allow synchronization and jitter calculations (see Section 6.4.1). The resolution of the clock MUST be sufficient for the desired synchronization accuracy and for measuring packet arrival jitter (one tick per video frame is typically not sufficient). The clock frequency is dependent on the format of data carried as payload and is specified statically in the profile or payload format specification that defines the format, or MAY be specified dynamically for payload formats defined through non-RTP means.", so the units of the rtp.timestamp field depends on the type of payload - and might not be the same for all payloads of a given type and not be determinable just by looking at the RTP traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '10, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Nov '10, 01:13</p></div></div><div id="comments-container-1174" class="comments-container"><span id="1199"></span><div id="comment-1199" class="comment"><div id="post-1199-score" class="comment-score"></div><div class="comment-text"><p>An example: Media Attribute (a): rtpmap:0 PCMU/8000 The sampling frequency is 8000 Hz, so a time-tick is 1/8000 s.</p></div><div id="comment-1199-info" class="comment-info"><span class="comment-age">(01 Dec '10, 23:30)</span> Anders ♦</div></div></div><div id="comment-tools-1174" class="comment-tools"></div><div class="clear"></div><div id="comment-1174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

