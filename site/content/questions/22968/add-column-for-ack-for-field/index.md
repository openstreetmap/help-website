+++
type = "question"
title = "Add column for &quot;ACK For&quot; field"
description = '''Can anyone help me guide how can we add coloumn ACK for , where it will say that current packet is acknowledged for Packt no XYZ. Thank for help.'''
date = "2013-07-15T02:32:00Z"
lastmod = "2013-07-15T02:51:00Z"
weight = 22968
keywords = [ "columns" ]
aliases = [ "/questions/22968" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add column for "ACK For" field](/questions/22968/add-column-for-ack-for-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22968-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone help me guide how can we add coloumn ACK for , where it will say that current packet is acknowledged for Packt no XYZ.</p><p>Thank for help.</p></div><div id="question-tags" class="tags-container tags">columns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/6615a61d69b703d89076bb0f18342bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m_1607&#39;s gravatar image" /><p>m_1607<br />
<span class="score" title="35 reputation points">35</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m_1607 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '13, 02:36</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22968" class="comments-container"></div><div id="comment-tools-22968" class="comment-tools"></div><div class="clear"></div><div id="comment-22968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22970"></span>

<div id="answer-container-22970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22970-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand your question correctly, you want a column that shows the content of the field "tcp.analysis.acks_frame"?</p><p>You can do this by manually adding a custom column in the column preferences. Or you can select an ACK packet and expand the trees in the packet detail pane. Then rightclick on the line "This is an ACK to the segment in frame: xxx" and choose "Apply as Column". Then rightclick on the header of the new column and choose "Edit column Details" to change the column title to "ACK".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22970" class="comments-container"></div><div id="comment-tools-22970" class="comment-tools"></div><div class="clear"></div><div id="comment-22970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22969"></span>

<div id="answer-container-22969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22969-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Due to TCP being able to acknowledge multiple successfully recieved segments within a single ACK, there is no such information quickly accessible. The ACK number tells you the next expected sequence number so what you are looking for is a way to differentiate the current ACK number from the previously recieved ACK number and then looking up incoming segments' sequence numbers to see how many and which have matched in between.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22969" class="comments-container"></div><div id="comment-tools-22969" class="comment-tools"></div><div class="clear"></div><div id="comment-22969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

