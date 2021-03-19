+++
type = "question"
title = "How do we differentiate simple g711a codec or  codec with silence suppressor in wireshark?"
description = '''How do we differentiate simple g711a codec or codec with silence suppressor in wireshark?'''
date = "2013-03-11T23:57:00Z"
lastmod = "2013-03-12T03:40:00Z"
weight = 19372
keywords = [ "codec" ]
aliases = [ "/questions/19372" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do we differentiate simple g711a codec or codec with silence suppressor in wireshark?](/questions/19372/how-do-we-differentiate-simple-g711a-codec-or-codec-with-silence-suppressor-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do we differentiate simple g711a codec or codec with silence suppressor in wireshark?</p></div><div id="question-tags" class="tags-container tags">codec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '13, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/e12d9d0c390836527ae1e83372d959a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="archu&#39;s gravatar image" /><p>archu<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="archu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '13, 01:29</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-19372" class="comments-container"></div><div id="comment-tools-19372" class="comment-tools"></div><div class="clear"></div><div id="comment-19372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19382"></span>

<div id="answer-container-19382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19382-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll see jumps in the RTP time stamps, while the sequence numbers are monotone incrementing. Or you'll see payload type changes to 13 and back. PT 13 is reserved for comfort noise payload. Or you may pick it up from the SDP signalling.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19382" class="comments-container"></div><div id="comment-tools-19382" class="comment-tools"></div><div class="clear"></div><div id="comment-19382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

