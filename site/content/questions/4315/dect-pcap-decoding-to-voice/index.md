+++
type = "question"
title = "DECT pcap decoding to voice"
description = '''Hi guys, any Idea, how to decode DECT captured file into Voice: many Thx.'''
date = "2011-06-01T06:45:00Z"
lastmod = "2011-06-02T12:42:00Z"
weight = 4315
keywords = [ "dect" ]
aliases = [ "/questions/4315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DECT pcap decoding to voice](/questions/4315/dect-pcap-decoding-to-voice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, any Idea, how to decode DECT captured file into Voice:</p><p>many Thx.</p></div><div id="question-tags" class="tags-container tags">dect</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '11, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p>reza666<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span></p></div></div><div id="comments-container-4315" class="comments-container"></div><div id="comment-tools-4315" class="comment-tools"></div><div class="clear"></div><div id="comment-4315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4345"></span>

<div id="answer-container-4345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4345-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That may prove difficult, since the B-field data is encrypted for any decent implementation. If it's not then filter out all B-field data of a connection and put it through a G.726 decoder (assuming Basic Service is basic speech). There's currently no automated way to do this with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4345" class="comments-container"></div><div id="comment-tools-4345" class="comment-tools"></div><div class="clear"></div><div id="comment-4345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

