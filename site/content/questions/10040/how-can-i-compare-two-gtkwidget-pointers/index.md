+++
type = "question"
title = "[closed] How can I compare two Gtkwidget pointers?"
description = '''I want to compare values two Gtkwidget pointers for equality..... how can I do this? I am trying to typecast it to int, but it isn&#x27;t working... Gtkwidget *a; Gtkwidget *b;  if((int)a==(int)b) { //do something } '''
date = "2012-04-10T03:03:00Z"
lastmod = "2012-04-10T07:30:00Z"
weight = 10040
keywords = [ "development", "gtk" ]
aliases = [ "/questions/10040" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How can I compare two Gtkwidget pointers?](/questions/10040/how-can-i-compare-two-gtkwidget-pointers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10040-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to compare values two <code>Gtkwidget</code> pointers for equality..... how can I do this?</p><p>I am trying to typecast it to <code>int</code>, but it isn't working...</p><pre><code>Gtkwidget  *a;
Gtkwidget  *b;

if((int)a==(int)b)
{
//do something
}</code></pre></div><div id="question-tags" class="tags-container tags">development gtk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '12, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/0aba772e8e3564a308f2bdb6077efd44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prashanth%20cm&#39;s gravatar image" /><p>prashanth cm<br />
<span class="score" title="-1 reputation points">-1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prashanth cm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 10 Apr '12, 07:30</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-10040" class="comments-container"></div><div id="comment-tools-10040" class="comment-tools"></div><div class="clear"></div><div id="comment-10040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant. Only tangentially related to Wireshark." by multipleinterfaces 10 Apr '12, 07:30

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10044"></span>

<div id="answer-container-10044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10044-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>if(a==b) {}</code> will work just fine. Comparison for strict equality is defined for pointer types.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '12, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-10044" class="comments-container"></div><div id="comment-tools-10044" class="comment-tools"></div><div class="clear"></div><div id="comment-10044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

