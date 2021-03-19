+++
type = "question"
title = "Promiscuous mode?"
description = '''If I am looking to capture traffic that is flowing in and out of my node, do I take wireshark off of promiscuous mode?'''
date = "2014-07-24T07:11:00Z"
lastmod = "2014-07-24T07:18:00Z"
weight = 34877
keywords = [ "promiscuous" ]
aliases = [ "/questions/34877" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscuous mode?](/questions/34877/promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34877-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I am looking to capture traffic that is flowing in and out of my node, do I take wireshark off of promiscuous mode?</p></div><div id="question-tags" class="tags-container tags">promiscuous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '14, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/8b005b5f2108e2852f31acc75685c36c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwilliams1987&#39;s gravatar image" /><p>jwilliams1987<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwilliams1987 has no accepted answers">0%</span></p></div></div><div id="comments-container-34877" class="comments-container"></div><div id="comment-tools-34877" class="comment-tools"></div><div class="clear"></div><div id="comment-34877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34878"></span>

<div id="answer-container-34878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34878-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could do that to limit what you capture, but in most cases it is not necessary. The results are pretty much the same if you're aiming at only capturing traffic of your own node, and not capturing at a TAP or SPAN port (which would give you much more data than just that of your node)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34878" class="comments-container"><span id="34879"></span><div id="comment-34879" class="comment"><div id="post-34879-score" class="comment-score"></div><div class="comment-text"><p>I am looking to see if some freeware ,that is only supposed to put on the screen your system info, might open a backdoor or send info to a remote node elsewhere. So I am really only interested in traffic in and out of my node.</p></div><div id="comment-34879-info" class="comment-info"><span class="comment-age">(24 Jul '14, 07:23)</span> jwilliams1987</div></div><span id="34880"></span><div id="comment-34880" class="comment"><div id="post-34880-score" class="comment-score"></div><div class="comment-text"><p>Go ahead and capture with promiscuous mode on or off. You can filter on your node IP afterwards to see what it did.</p></div><div id="comment-34880-info" class="comment-info"><span class="comment-age">(24 Jul '14, 07:25)</span> Jasper ♦♦</div></div><span id="34882"></span><div id="comment-34882" class="comment"><div id="post-34882-score" class="comment-score"></div><div class="comment-text"><p>True. Thank you.</p></div><div id="comment-34882-info" class="comment-info"><span class="comment-age">(24 Jul '14, 07:28)</span> jwilliams1987</div></div></div><div id="comment-tools-34878" class="comment-tools"></div><div class="clear"></div><div id="comment-34878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

