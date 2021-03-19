+++
type = "question"
title = "lot of Syn Syn-ACKs"
description = ''''''
date = "2014-10-21T10:22:00Z"
lastmod = "2014-10-21T12:55:00Z"
weight = 37246
keywords = [ "syn-ack" ]
aliases = [ "/questions/37246" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lot of Syn Syn-ACKs](/questions/37246/lot-of-syn-syn-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37246-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_vCQNyqf.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">syn-ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/4316c1946f08f682c8b02ca026a5a95e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rikki&#39;s gravatar image" /><p>Rikki<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rikki has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37246" class="comments-container"><span id="37247"></span><div id="comment-37247" class="comment"><div id="post-37247-score" class="comment-score"></div><div class="comment-text"><p>i see lot of syn syn-acks when user tries to open a small report (500kb) via SAP. Not sure what this means but the speed that user gets is very very slow</p></div><div id="comment-37247-info" class="comment-info"><span class="comment-age">(21 Oct '14, 10:24)</span> Rikki</div></div></div><div id="comment-tools-37246" class="comment-tools"></div><div class="clear"></div><div id="comment-37246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37253"></span>

<div id="answer-container-37253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37253-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A screenshot is not really telling the whole story. It looks like the client is opening a lot of connections to a lot of different server ports. I can't tell from the screenshot what they are all used for, but I guess the application is coded to pull a lot of details in separate connections.</p><p>Maybe my blog post about a similiar setup (using just one connection, but not in a really efficient way either) can shed some light on why the report is slow:</p><p><a href="http://blog.packet-foo.com/2014/09/how-millisecond-delays-may-kill-database-performance/">http://blog.packet-foo.com/2014/09/how-millisecond-delays-may-kill-database-performance/</a></p><p>My guess is that a lot of small details are pulled one ofter the other, using multiple TCP connections. If so, the only way to improve the situation is to fix the way the report is generated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37253" class="comments-container"></div><div id="comment-tools-37253" class="comment-tools"></div><div class="clear"></div><div id="comment-37253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

