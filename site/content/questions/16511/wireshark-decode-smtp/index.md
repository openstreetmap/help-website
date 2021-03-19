+++
type = "question"
title = "Wireshark decode SMTP"
description = '''I&#x27;m analyzing a SMTP transfer and not sure what Wireshark is reporting in the Info section of &quot;D: DATA fragment, xx bytes&quot;. Has anyone seen this before?'''
date = "2012-12-03T13:01:00Z"
lastmod = "2012-12-03T13:21:00Z"
weight = 16511
keywords = [ "smtp" ]
aliases = [ "/questions/16511" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark decode SMTP](/questions/16511/wireshark-decode-smtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16511-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm analyzing a SMTP transfer and not sure what Wireshark is reporting in the Info section of "D: DATA fragment, xx bytes". Has anyone seen this before?</p></div><div id="question-tags" class="tags-container tags">smtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p>ws2006<br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-16511" class="comments-container"></div><div id="comment-tools-16511" class="comment-tools"></div><div class="clear"></div><div id="comment-16511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16512"></span>

<div id="answer-container-16512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16512-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The content of an email (headers + body) is sent after the SMTP DATA command. If that content is larger than one TCP segment, Wireshark will show every packet that belongs to the DATA "command" as "C: DATA fragment" in the Info column. So, those packets are basically the content of the email.</p><p>You can see the whole SMTP communication.</p><ul><li>select any packet of the SMTP connection</li><li>right click the packet</li><li>select "Follow TCP Stream"</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '12, 13:27</p></div></div><div id="comments-container-16512" class="comments-container"><span id="16541"></span><div id="comment-16541" class="comment"><div id="post-16541-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. It's the DATA Fragment in the info that i was concerned with.</p></div><div id="comment-16541-info" class="comment-info"><span class="comment-age">(04 Dec '12, 06:51)</span> ws2006</div></div><span id="16545"></span><div id="comment-16545" class="comment"><div id="post-16545-score" class="comment-score"></div><div class="comment-text"><p>It's just an info, that Wireshark detected one part (one fragment) of the mail message.</p><p>what concerns do you have?</p></div><div id="comment-16545-info" class="comment-info"><span class="comment-age">(04 Dec '12, 08:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16512" class="comment-tools"></div><div class="clear"></div><div id="comment-16512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

