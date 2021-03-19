+++
type = "question"
title = "dissecting packets using libwireshark in multithreaded environment"
description = '''hello all, I am using libwireshark.so (shared library for wireshark)v1.6.5 for dissecting network packets, now i want to make my application multithreaded.  so, is it possible to use libworeshark in a multithreaded environment, because every time i am executing the multithreaded application for diss...'''
date = "2013-02-28T23:59:00Z"
lastmod = "2013-03-01T02:39:00Z"
weight = 19016
keywords = [ "development", "libwireshark", "dissection", "multithreaded", "c++" ]
aliases = [ "/questions/19016" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [dissecting packets using libwireshark in multithreaded environment](/questions/19016/dissecting-packets-using-libwireshark-in-multithreaded-environment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello all,</p><p>I am using libwireshark.so (shared library for wireshark)v1.6.5 for dissecting network packets, now i want to make my application multithreaded.</p><p>so, is it possible to use libworeshark in a multithreaded environment, because every time i am executing the multithreaded application for dissecting packets, first thread works fine, after then no thread can dissect data.</p></div><div id="question-tags" class="tags-container tags">development libwireshark dissection multithreaded c++</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-19016" class="comments-container"></div><div id="comment-tools-19016" class="comment-tools"></div><div class="clear"></div><div id="comment-19016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19021"></span>

<div id="answer-container-19021" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19021-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Libwireshark is not thread safe, and isn't likely to be made so in the future. You'll just have to call libwireshark from a single process thread.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19021" class="comments-container"></div><div id="comment-tools-19021" class="comment-tools"></div><div class="clear"></div><div id="comment-19021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

