+++
type = "question"
title = "Schedule a capture"
description = '''Is it possible to set a time for a capture to start and then use the &quot;Stop capture automatically&quot; feature? '''
date = "2015-05-13T07:12:00Z"
lastmod = "2015-05-13T07:29:00Z"
weight = 42361
keywords = [ "scheduled", "captures" ]
aliases = [ "/questions/42361" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Schedule a capture](/questions/42361/schedule-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42361-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to set a time for a capture to start and then use the "Stop capture automatically" feature?</p></div><div id="question-tags" class="tags-container tags">scheduled captures</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/617349a0c8535a550e4ad8fe1c34682f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PWR%20MAD&#39;s gravatar image" /><p>PWR MAD<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PWR MAD has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '15, 07:18</p></div></div><div id="comments-container-42361" class="comments-container"></div><div id="comment-tools-42361" class="comment-tools"></div><div class="clear"></div><div id="comment-42361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42364"></span>

<div id="answer-container-42364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42364-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, not within the GUI version of Wireshark. But you can use <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> and the scheduler of your OS (windows scheduler, Unix cron, etc.) to start the capturing process. To stop the capturing process you can use the scheduler to kill the dumpcap process, or the built-in functionality of dumpcap to stop the capture process after some time.</p><blockquote><p><a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">https://www.wireshark.org/docs/man-pages/dumpcap.html</a></p></blockquote><p>See option <strong>-a duration:</strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42364" class="comments-container"><span id="42365"></span><div id="comment-42365" class="comment"><div id="post-42365-score" class="comment-score"></div><div class="comment-text"><p>Excellent, thank you.</p></div><div id="comment-42365-info" class="comment-info"><span class="comment-age">(13 May '15, 07:30)</span> PWR MAD</div></div><span id="42366"></span><div id="comment-42366" class="comment"><div id="post-42366-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment, as that's how this Q&amp;A site works. Please see the FAQ.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-42366-info" class="comment-info"><span class="comment-age">(13 May '15, 07:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42364" class="comment-tools"></div><div class="clear"></div><div id="comment-42364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

