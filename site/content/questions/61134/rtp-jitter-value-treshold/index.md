+++
type = "question"
title = "rtp jitter value treshold"
description = '''Hello  In the RTP streams obtain with tshark (see bellow). What s the treshold for relating problems in the call flow ? Max Delta(ms) treshold Max Jitter(ms) treshold Mean Jitter(ms)treshold &amp;gt;&amp;gt;&amp;gt; involved Problems? thanks a lot'''
date = "2017-05-01T02:37:00Z"
lastmod = "2017-05-01T02:57:00Z"
weight = 61134
keywords = [ "rtp", "stream" ]
aliases = [ "/questions/61134" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rtp jitter value treshold](/questions/61134/rtp-jitter-value-treshold)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello In the RTP streams obtain with tshark (see bellow). What s the treshold for relating problems in the call flow ? Max Delta(ms) treshold Max Jitter(ms) treshold Mean Jitter(ms)treshold &gt;&gt;&gt; involved Problems? thanks a lot</p></div><div id="question-tags" class="tags-container tags">rtp stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '17, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/6081bb9dd57c0a4176c8cbc20208f55d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hamsi&#39;s gravatar image" /><p>hamsi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hamsi has no accepted answers">0%</span></p></div></div><div id="comments-container-61134" class="comments-container"></div><div id="comment-tools-61134" class="comment-tools"></div><div class="clear"></div><div id="comment-61134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61135"></span>

<div id="answer-container-61135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61135-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Timing / jitter statistics don't attribute to the Problem indicator, since the relevance of these values are very target implementation specific, hence cannot be determined by Wireshark. What does contribute to the Problem indicator is wrong timestamps and wrong sequence numbers. These can be determined from the RTP packet sequence itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '17, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61135" class="comments-container"></div><div id="comment-tools-61135" class="comment-tools"></div><div class="clear"></div><div id="comment-61135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

