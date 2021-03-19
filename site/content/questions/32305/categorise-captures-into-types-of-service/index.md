+++
type = "question"
title = "Categorise captures into types of service"
description = '''Hi, I need to categorise the captured packets into types of services such as Skype, web browsing, e-mail etc. for analysis purposes to find out the trends in network usage at the office. I&#x27;m hoping to be able to generate presentable graphs. Could someone please help me? Thank you very much in advanc...'''
date = "2014-04-29T19:23:00Z"
lastmod = "2014-04-30T00:20:00Z"
weight = 32305
keywords = [ "tos", "statistics", "categorise", "graphs" ]
aliases = [ "/questions/32305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Categorise captures into types of service](/questions/32305/categorise-captures-into-types-of-service)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need to categorise the captured packets into types of services such as Skype, web browsing, e-mail etc. for analysis purposes to find out the trends in network usage at the office. I'm hoping to be able to generate presentable graphs.</p><p>Could someone please help me?</p><p>Thank you very much in advance!</p></div><div id="question-tags" class="tags-container tags">tos statistics categorise graphs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '14, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/8384c92a53af3ff561d86a2014b4278f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amelctr&#39;s gravatar image" /><p>amelctr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amelctr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Apr '14, 19:28</p></div></div><div id="comments-container-32305" class="comments-container"></div><div id="comment-tools-32305" class="comment-tools"></div><div class="clear"></div><div id="comment-32305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32307"></span>

<div id="answer-container-32307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32307-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Presentable graphs" is not really what Wireshark produces, except for the I/O graph (especially in the new QT version), but that one does not work for protocol distribution. There is a protocol distribution statistics, but it's just a tree structure.</p><p>Maybe you should look into something that uses NetFlow to do this, I guess you're finding more useful results in your case. The other alternative might be Cascade Pilot or some of the other commercial analyzers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32307" class="comments-container"></div><div id="comment-tools-32307" class="comment-tools"></div><div class="clear"></div><div id="comment-32307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

