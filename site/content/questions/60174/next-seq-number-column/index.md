+++
type = "question"
title = "Next Seq Number Column"
description = '''I would like to add the Next Sequence Number to my columns. I don&#x27;t see it in my packet details, so I can&#x27;t right-click it, and add it to my columns. How can I do this?'''
date = "2017-03-19T08:47:00Z"
lastmod = "2017-03-19T08:50:00Z"
weight = 60174
keywords = [ "column", "numbers", "sequence" ]
aliases = [ "/questions/60174" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Next Seq Number Column](/questions/60174/next-seq-number-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to add the Next Sequence Number to my columns. I don't see it in my packet details, so I can't right-click it, and add it to my columns. How can I do this?</p></div><div id="question-tags" class="tags-container tags">column numbers sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '17, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/3962b2c1048cf6eda0cdbe8ad3434562?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="droidus&#39;s gravatar image" /><p>droidus<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="droidus has no accepted answers">0%</span></p></div></div><div id="comments-container-60174" class="comments-container"></div><div id="comment-tools-60174" class="comment-tools"></div><div class="clear"></div><div id="comment-60174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60175"></span>

<div id="answer-container-60175" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60175-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Find a TCP packet that doesn't have a zero length payload, e.g. by filtering for "tcp.len &gt; 0" - in one of those packets, you'll see the "next sequence number" field in the TCP header and you can right-click it to add it as a column.</p><p>Or add a custom column manually, and set the "fields" value to "tcp.nxtseq"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '17, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60175" class="comments-container"></div><div id="comment-tools-60175" class="comment-tools"></div><div class="clear"></div><div id="comment-60175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

