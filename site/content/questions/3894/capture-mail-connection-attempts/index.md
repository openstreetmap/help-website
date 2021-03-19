+++
type = "question"
title = "Capture mail connection attempts"
description = '''I manage a site that will not receive mail from 2 seperate domains (that I know of). I need to find out why mail is not being delivered from these domains. The senders do receive an NDR stating that the message was rejected by my clients server as &quot;the message is too old&quot;. They have a simple setup -...'''
date = "2011-05-03T03:18:00Z"
lastmod = "2011-05-03T05:36:00Z"
weight = 3894
keywords = [ "e-mail" ]
aliases = [ "/questions/3894" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture mail connection attempts](/questions/3894/capture-mail-connection-attempts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I manage a site that will not receive mail from 2 seperate domains (that I know of). I need to find out why mail is not being delivered from these domains. The senders do receive an NDR stating that the message was rejected by my clients server as "the message is too old". They have a simple setup - an SBS 2003 server &amp; a Billion router on the same subnet. I will ask the sender to send my client an e-mail &amp; cc me in, that way I will know when it was delivered. As a newbie to Wireshark I need to know how to filter the large amounts of data to find the delivery attempt. What will I be looking for, as I will not know the sender's IP address, only a domain name. Please assist.</p></div><div id="question-tags" class="tags-container tags">e-mail</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/4cc5743cbb994e88eb0718fb7cba9c4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAZ%20IT&#39;s gravatar image" /><p>JAZ IT<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAZ IT has no accepted answers">0%</span></p></div></div><div id="comments-container-3894" class="comments-container"></div><div id="comment-tools-3894" class="comment-tools"></div><div class="clear"></div><div id="comment-3894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3896"></span>

<div id="answer-container-3896" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3896-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I worked it out by setting up an SMTP filter. Unfortunately that shows that the mail was delivered successfully - but it isn't. That;s for another forum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '11, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/4cc5743cbb994e88eb0718fb7cba9c4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAZ%20IT&#39;s gravatar image" /><p>JAZ IT<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAZ IT has no accepted answers">0%</span></p></div></div><div id="comments-container-3896" class="comments-container"></div><div id="comment-tools-3896" class="comment-tools"></div><div class="clear"></div><div id="comment-3896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3897"></span>

<div id="answer-container-3897" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3897-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I worked it out by setting up an SMTP filter. Unfortunately that shows that the mail was delivered successfully - but it isn't. That;s for another forum.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '11, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/4cc5743cbb994e88eb0718fb7cba9c4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAZ%20IT&#39;s gravatar image" /><p>JAZ IT<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAZ IT has no accepted answers">0%</span></p></div></div><div id="comments-container-3897" class="comments-container"></div><div id="comment-tools-3897" class="comment-tools"></div><div class="clear"></div><div id="comment-3897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

