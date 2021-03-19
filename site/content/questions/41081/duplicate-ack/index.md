+++
type = "question"
title = "Duplicate Ack"
description = '''Hi everyone, Plz i want to know something about the Duplicate Ack : when i see in wireshark capture [tcp dup ack 10#1] the &quot;10#1&quot; what does that means? Thank you for your help.'''
date = "2015-04-01T01:22:00Z"
lastmod = "2015-04-01T01:32:00Z"
weight = 41081
keywords = [ "duplicatedack" ]
aliases = [ "/questions/41081" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Duplicate Ack](/questions/41081/duplicate-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41081-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>Plz i want to know something about the Duplicate Ack : when i see in wireshark capture [tcp dup ack 10#1] the "10#1" what does that means?</p><p>Thank you for your help.</p></div><div id="question-tags" class="tags-container tags">duplicatedack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/90875c0c2524531263f27b57e1d27ea3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hub&#39;s gravatar image" /><p>hub<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hub has no accepted answers">0%</span></p></div></div><div id="comments-container-41081" class="comments-container"></div><div id="comment-tools-41081" class="comment-tools"></div><div class="clear"></div><div id="comment-41081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41082"></span>

<div id="answer-container-41082" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41082-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means that a previously acknowledged packet was acknowledged again, which usually indicates out-of-order arrival or packet loss. The number behind the # sign is the counter of how often the same packet was acknowledged. #1 means one duplicate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '15, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41082" class="comments-container"></div><div id="comment-tools-41082" class="comment-tools"></div><div class="clear"></div><div id="comment-41082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

