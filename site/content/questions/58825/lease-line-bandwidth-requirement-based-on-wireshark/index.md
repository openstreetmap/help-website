+++
type = "question"
title = "lease line bandwidth requirement based on wireshark"
description = '''Hi , Based on wireshark summary , can i know what is the suitable bandwidth for my lease line connection.. 512kbps is enough ? How to calculated ? Thanks '''
date = "2017-01-16T22:56:00Z"
lastmod = "2017-01-17T02:41:00Z"
weight = 58825
keywords = [ "bandwidth" ]
aliases = [ "/questions/58825" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lease line bandwidth requirement based on wireshark](/questions/58825/lease-line-bandwidth-requirement-based-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>Based on wireshark summary , can i know what is the suitable bandwidth for my lease line connection.. 512kbps is enough ? How to calculated ? Thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/packets.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '17, 22:56</strong></p><img src="https://secure.gravatar.com/avatar/b8cbaa9ee7d5bf40e4c8f703e3197880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suarez123&#39;s gravatar image" /><p>suarez123<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suarez123 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58825" class="comments-container"></div><div id="comment-tools-58825" class="comment-tools"></div><div class="clear"></div><div id="comment-58825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58831"></span>

<div id="answer-container-58831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58831-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to your screenshot you have an average bit rate of 103kbps, so 512 would be enough.</p><p>But that is only valid if you can be sure that</p><ol><li>you captured the traffic long enough to have all up and down peaks covered (e.g. if you capture in the night when nobody is using the lines the values aren't that relevant)</li><li>Averages tend to hide peaks, so it would be better to look at the I/O graph in the statistics menu to check what the peaks are, and base your requirements on those instead of averages.</li></ol><p><img src="http://2.bp.blogspot.com/-IVBBb8B2UuU/UKuqRQ9jJTI/AAAAAAAAADw/bYL4tb4bvoE/s400/averages.png" alt="Averages" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '17, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-58831" class="comments-container"><span id="58861"></span><div id="comment-58861" class="comment"><div id="post-58861-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper :)</p></div><div id="comment-58861-info" class="comment-info"><span class="comment-age">(17 Jan '17, 17:54)</span> suarez123</div></div></div><div id="comment-tools-58831" class="comment-tools"></div><div class="clear"></div><div id="comment-58831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

