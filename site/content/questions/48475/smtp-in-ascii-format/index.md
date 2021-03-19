+++
type = "question"
title = "smtp in ascii format"
description = '''Hello all, I am not familiar with wireshark, can any one please tell me how can I capture the SMTP payload in ASCII format, thanks in advance.'''
date = "2015-12-12T09:22:00Z"
lastmod = "2015-12-12T10:18:00Z"
weight = 48475
keywords = [ "smtp", "ascii" ]
aliases = [ "/questions/48475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [smtp in ascii format](/questions/48475/smtp-in-ascii-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I am not familiar with wireshark, can any one please tell me how can I capture the SMTP payload in ASCII format, thanks in advance.</p></div><div id="question-tags" class="tags-container tags">smtp ascii</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/86c7080d8f49db5dc435f8a8c53b7877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nazzoka&#39;s gravatar image" /><p>Nazzoka<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nazzoka has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '15, 10:19</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48475" class="comments-container"></div><div id="comment-tools-48475" class="comment-tools"></div><div class="clear"></div><div id="comment-48475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48476"></span>

<div id="answer-container-48476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48476-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just capture the traffic as normal, then use a display filter of "smtp".</p><p>As long as the SMTP traffic isn't encrypted you can see the payload by right-clicking any packet in the SMTP conversation and then selecting Follow -&gt; TCP Stream.</p><p>The resulting dialog will show the entire conversation which you can copy to the clipboard. The email be in multiple parts so you might have to do a little editing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '15, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '15, 10:20</p></div></div><div id="comments-container-48476" class="comments-container"><span id="48477"></span><div id="comment-48477" class="comment"><div id="post-48477-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot</p></div><div id="comment-48477-info" class="comment-info"><span class="comment-age">(12 Dec '15, 10:27)</span> Nazzoka</div></div></div><div id="comment-tools-48476" class="comment-tools"></div><div class="clear"></div><div id="comment-48476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

