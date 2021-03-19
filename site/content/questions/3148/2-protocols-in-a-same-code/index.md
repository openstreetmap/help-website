+++
type = "question"
title = "2 protocols in a same code?"
description = '''I have a protocol such that there is a x header and y header. How can i have these headers under a single packet-xyz.c file?  It should look something like this .. IP TCP X Y'''
date = "2011-03-27T02:21:00Z"
lastmod = "2011-03-27T14:50:00Z"
weight = 3148
keywords = [ "header", "protocol" ]
aliases = [ "/questions/3148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [2 protocols in a same code?](/questions/3148/2-protocols-in-a-same-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a protocol such that there is a x header and y header. How can i have these headers under a single packet-xyz.c file? It should look something like this .. IP TCP X Y</p></div><div id="question-tags" class="tags-container tags">header protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '11, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p>niks3089<br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-3148" class="comments-container"></div><div id="comment-tools-3148" class="comment-tools"></div><div class="clear"></div><div id="comment-3148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3165"></span>

<div id="answer-container-3165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3165-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Write two separate dissectors, and put the source to both of them in the packet-xyz.c file. Have the dissector for protocol X call the dissector for protocol Y, when appropriate. The only difference between this and having two dissectors in different source files is that you put them both in the same source file. (Using a single dissector for both protocol layers is the wrong way to do it.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3165" class="comments-container"></div><div id="comment-tools-3165" class="comment-tools"></div><div class="clear"></div><div id="comment-3165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

