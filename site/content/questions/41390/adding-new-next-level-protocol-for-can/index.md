+++
type = "question"
title = "Adding new next level protocol for CAN"
description = '''Hello, I am trying to create a new dissector for CAN. I copied and modified the J1939 dissector. I successfully compiled the new dissector and it is visible as an enabled protocol but it is not visible as a next level protocol under CAN. I see CANopen, DeviceNet and J1939 but not the new dissector. ...'''
date = "2015-04-12T00:06:00Z"
lastmod = "2015-04-12T05:31:00Z"
weight = 41390
keywords = [ "dissector", "can" ]
aliases = [ "/questions/41390" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding new next level protocol for CAN](/questions/41390/adding-new-next-level-protocol-for-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41390-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to create a new dissector for CAN. I copied and modified the J1939 dissector. I successfully compiled the new dissector and it is visible as an enabled protocol but it is not visible as a next level protocol under CAN. I see CANopen, DeviceNet and J1939 but not the new dissector. Where are the next level protocols defined for CAN?</p><p>Thanks Patrick</p></div><div id="question-tags" class="tags-container tags">dissector can</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '15, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/cf47d5a683721d0c4a8d970956ca1e23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmendiuk&#39;s gravatar image" /><p>pmendiuk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmendiuk has no accepted answers">0%</span></p></div></div><div id="comments-container-41390" class="comments-container"></div><div id="comment-tools-41390" class="comment-tools"></div><div class="clear"></div><div id="comment-41390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41392"></span>

<div id="answer-container-41392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41392-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to edit packet-socketcan.c file and add your new protocol at the same places as you can find the J1939 one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '15, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41392" class="comments-container"><span id="41397"></span><div id="comment-41397" class="comment"><div id="post-41397-score" class="comment-score"></div><div class="comment-text"><p>Thanks that was it.</p></div><div id="comment-41397-info" class="comment-info"><span class="comment-age">(12 Apr '15, 08:21)</span> pmendiuk</div></div><span id="41398"></span><div id="comment-41398" class="comment"><div id="post-41398-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41398-info" class="comment-info"><span class="comment-age">(12 Apr '15, 09:24)</span> grahamb ♦</div></div><span id="48095"></span><div id="comment-48095" class="comment"><div id="post-48095-score" class="comment-score"></div><div class="comment-text"><p>Note that CAN subdissector registration has changed, now your subdissector should register with the "can.subdissector" table using <code>dissector_add_for_decode_as</code>.</p><p>Searching the dissectors for "can.subdissector" will show examples.</p></div><div id="comment-48095-info" class="comment-info"><span class="comment-age">(30 Nov '15, 08:14)</span> grahamb ♦</div></div></div><div id="comment-tools-41392" class="comment-tools"></div><div class="clear"></div><div id="comment-41392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

