+++
type = "question"
title = "Frame Header 802.3 vs 802.11"
description = '''Where can I see the difference of wired vs wireless in the frame header structure in wireshark? And what describes the physical setup in both 802.3 &amp;amp; 802.11? Thanks!'''
date = "2013-12-13T10:20:00Z"
lastmod = "2013-12-13T11:02:00Z"
weight = 28084
keywords = [ "802.11", "802.3" ]
aliases = [ "/questions/28084" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Frame Header 802.3 vs 802.11](/questions/28084/frame-header-8023-vs-80211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28084-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Where can I see the difference of wired vs wireless in the frame header structure in wireshark? And what describes the physical setup in both 802.3 &amp; 802.11?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">802.11 802.3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '13, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/e031014bcaa7fa7b5559b6f9ade9bc58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John92&#39;s gravatar image" /><p>John92<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John92 has no accepted answers">0%</span></p></div></div><div id="comments-container-28084" class="comments-container"></div><div id="comment-tools-28084" class="comment-tools"></div><div class="clear"></div><div id="comment-28084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28085"></span>

<div id="answer-container-28085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28085-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds suspiciously like a HomeWork assignment. Anyway - wireless frames have an additional radio layer that is followed by the ethernet header that you will see on the wire. To capture this radio layer you need to be able to put your capture card into monitor mode.</p><p>As to the "physical setup" - you might want to read some RFCs, because it is way too much for a Q&amp;A answer (at least one of mine; Kurt is usually writing a lot more text :-)). Google a bit, and you'll see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28085" class="comments-container"><span id="28088"></span><div id="comment-28088" class="comment"><div id="post-28088-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Kurt is usually writing a lot more text :-))</p></blockquote><p>No longer... My yearly coningent of written words is almost depleted, so don't expect any longer texts for the remaining days... ;-)</p></div><div id="comment-28088-info" class="comment-info"><span class="comment-age">(13 Dec '13, 11:37)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28085" class="comment-tools"></div><div class="clear"></div><div id="comment-28085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

