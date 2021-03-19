+++
type = "question"
title = "Saved RTP Payload Bigger than expected"
description = '''Hi,  I have an RTP packet capture 273 seconds long. There are 13654 packets in the forward direction and 13646 in the reverse. There are no lost packets and virtually no jitter. The codec is G.729. When I use the &quot;Save payload&quot; feature I get files of 285260 and 272920 bytes respectively for forward ...'''
date = "2012-09-20T07:43:00Z"
lastmod = "2012-09-21T05:00:00Z"
weight = 14397
keywords = [ "g729", "rtp", "payload" ]
aliases = [ "/questions/14397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Saved RTP Payload Bigger than expected](/questions/14397/saved-rtp-payload-bigger-than-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have an RTP packet capture 273 seconds long. There are 13654 packets in the forward direction and 13646 in the reverse. There are no lost packets and virtually no jitter. The codec is G.729. When I use the "Save payload" feature I get files of 285260 and 272920 bytes respectively for forward and reverse. When I then convert these into PCM the audio file in the forward direction is ~15 seconds too long! I would have expected the file sizes to be 20 bytes x the number of RTP packets but it is bigger for the forward. The behavior is the same in Wireshark 1.6.10 and 1.8.2.</p><p>Why is the forward direction file bigger than expected and converted audio too long?</p><p>P.S. Unfortunately I can't figure out what is happening by listening to the audio because it is in Greek.</p><p>Thanks,</p><p>David</p></div><div id="question-tags" class="tags-container tags">g729 rtp payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '12, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/62ce95a565ae6554c7d757dca949ba90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sorkin&#39;s gravatar image" /><p>David Sorkin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sorkin has no accepted answers">0%</span></p></div></div><div id="comments-container-14397" class="comments-container"></div><div id="comment-tools-14397" class="comment-tools"></div><div class="clear"></div><div id="comment-14397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14428"></span>

<div id="answer-container-14428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14428-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you load the two audio files in an audio editor (<a href="http://audacity.sourceforge.net/">Audacity</a> for instance) you can see what it takes to align these streams, even though they are intelligible. Usually one party speaks at a time, so the speech and silence periods should line up somehow. That may show you where the 'extra' data is relative to the audio. 15 seconds sounds like call pickup delay for instance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14428" class="comments-container"></div><div id="comment-tools-14428" class="comment-tools"></div><div class="clear"></div><div id="comment-14428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

