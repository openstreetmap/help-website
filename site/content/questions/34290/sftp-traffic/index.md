+++
type = "question"
title = "SFTP traffic"
description = '''I want to monitor just for SFTP traffic. How do I do that? I&#x27;m sure there is a way to filter for just that. I&#x27;ve never used this product before.'''
date = "2014-06-30T08:09:00Z"
lastmod = "2014-06-30T08:19:00Z"
weight = 34290
keywords = [ "sftp" ]
aliases = [ "/questions/34290" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SFTP traffic](/questions/34290/sftp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34290-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to monitor just for SFTP traffic. How do I do that? I'm sure there is a way to filter for just that. I've never used this product before.</p></div><div id="question-tags" class="tags-container tags">sftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '14, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/bf4d6ca9561f52b3973737d924b7a370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kody6107&#39;s gravatar image" /><p>kody6107<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kody6107 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:08</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34290" class="comments-container"></div><div id="comment-tools-34290" class="comment-tools"></div><div class="clear"></div><div id="comment-34290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34291"></span>

<div id="answer-container-34291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34291-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>SFTP is a file transfer protocol over SSH, at least that's my definition of it, so you would need to use a display filter for the SSH port: "tcp.port==22". Or, if you only want to capture SSH, use a capture filter: "tcp port 22". Keep in mind that SSH is encrypted, so the packets you can capture that way are of limited use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '14, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34291" class="comments-container"><span id="34292"></span><div id="comment-34292" class="comment"><div id="post-34292-score" class="comment-score"></div><div class="comment-text"><p>thank you... changing the capture to port 22 did the trick</p></div><div id="comment-34292-info" class="comment-info"><span class="comment-age">(30 Jun '14, 08:54)</span> kody6107</div></div><span id="34293"></span><div id="comment-34293" class="comment"><div id="post-34293-score" class="comment-score"></div><div class="comment-text"><p>@kody6107</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-34293-info" class="comment-info"><span class="comment-age">(30 Jun '14, 08:57)</span> grahamb ♦</div></div></div><div id="comment-tools-34291" class="comment-tools"></div><div class="clear"></div><div id="comment-34291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

