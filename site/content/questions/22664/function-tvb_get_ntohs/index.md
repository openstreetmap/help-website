+++
type = "question"
title = "function tvb_get_ntohs"
description = '''hi everyone,  What is the exact role of function &quot;tvb_get_ntohs&quot; , if we write :  ch1 = tvb_get_ntohs(tvb, 0); ch2 = tvb_get_ntohs(tvb, 2); what does it mean exactly , i know that the tvb is buffer where our data is recorded, but the second element is an offset , What&#x27;s that? and what does it mean t...'''
date = "2013-07-04T10:07:00Z"
lastmod = "2013-07-04T13:41:00Z"
weight = 22664
keywords = [ "tvbget" ]
aliases = [ "/questions/22664" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [function tvb\_get\_ntohs](/questions/22664/function-tvb_get_ntohs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi everyone,</p><p>What is the exact role of function "tvb_get_ntohs" , if we write :</p><p>ch1 = tvb_get_ntohs(tvb, 0); ch2 = tvb_get_ntohs(tvb, 2);</p><p>what does it mean exactly , i know that the tvb is buffer where our data is recorded, but the second element is an offset , What's that? and what does it mean this offset.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">tvbget</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/9fbe9f669a6d14e31178d8193125c39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruz&#39;s gravatar image" /><p>cruz<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruz has no accepted answers">0%</span></p></div></div><div id="comments-container-22664" class="comments-container"></div><div id="comment-tools-22664" class="comment-tools"></div><div class="clear"></div><div id="comment-22664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22671"></span>

<div id="answer-container-22671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22671-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The offset parameter is the offset into the buffer to get the value from, counting from 0.</p><p>In your example, ch1 is set to the 16 bit value at offset 0 in the buffer and ch2 is set to the 16 bit value at offset 2 in the buffer.</p><p>The ntohs part specifies that the data value in the buffer is in network order (big-endian) and it will be converted to the correct order for the host that the software is running on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '13, 13:43</p></div></div><div id="comments-container-22671" class="comments-container"></div><div id="comment-tools-22671" class="comment-tools"></div><div class="clear"></div><div id="comment-22671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

