+++
type = "question"
title = "how to calculate ACK"
description = '''Given the 3 frames how is the acknowledgment receipt of 2700 calculated? Transmission Control Protocol, Src Port: http (80), Dst Port: 52545 (52545), Seq: 1, Ack: 973, Len: 1460 Transmission Control Protocol, Src Port: http (80), Dst Port: 52545 (52545), Seq: 1461, Ack: 973, Len: 1239 Transmission C...'''
date = "2012-03-14T07:42:00Z"
lastmod = "2012-03-14T07:48:00Z"
weight = 9537
keywords = [ "ack", "calculation" ]
aliases = [ "/questions/9537" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to calculate ACK](/questions/9537/how-to-calculate-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9537-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given the 3 frames how is the acknowledgment receipt of 2700 calculated?</p><p>Transmission Control Protocol, Src Port: http (80), Dst Port: 52545 (52545), Seq: 1, Ack: 973, Len: 1460</p><p>Transmission Control Protocol, Src Port: http (80), Dst Port: 52545 (52545), Seq: 1461, Ack: 973, Len: 1239</p><p>Transmission Control Protocol, Src Port: 52545 (52545 ), Dst Port: http(80), Seq: 973, Ack: 2700, Len: 0</p></div><div id="question-tags" class="tags-container tags">ack calculation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '12, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/7827a84cc5b49c2271709298dbca678e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dingdong123&#39;s gravatar image" /><p>dingdong123<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dingdong123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '12, 07:43</p></div></div><div id="comments-container-9537" class="comments-container"></div><div id="comment-tools-9537" class="comment-tools"></div><div class="clear"></div><div id="comment-9537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9538"></span>

<div id="answer-container-9538" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9538-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simple: Sequence No from the second packet plus its length: 1461 + 1239 = 2700.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '12, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9538" class="comments-container"><span id="9539"></span><div id="comment-9539" class="comment"><div id="post-9539-score" class="comment-score"></div><div class="comment-text"><p>thanks. Also what is the explanation for the 3rd frames length being 0?</p></div><div id="comment-9539-info" class="comment-info"><span class="comment-age">(14 Mar '12, 07:49)</span> dingdong123</div></div><span id="9540"></span><div id="comment-9540" class="comment"><div id="post-9540-score" class="comment-score"></div><div class="comment-text"><p>Also simple: its only purpose is to acknowledge the first two frames, but the node has no own content to transmit. In that case the TCP payload length is zero - a quite common thing to observe.</p></div><div id="comment-9540-info" class="comment-info"><span class="comment-age">(14 Mar '12, 08:16)</span> Jasper ♦♦</div></div></div><div id="comment-tools-9538" class="comment-tools"></div><div class="clear"></div><div id="comment-9538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

