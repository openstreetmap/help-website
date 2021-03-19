+++
type = "question"
title = "Smooth in IO Graphs"
description = '''Hi everyone! I want to export a graphic with the number of packets/second of my capture. The problem is that I have a lot of packets at second 13, and any packet at second 14, for example. So, I would like to apply the smooth option of IO Graphs in Y axis, but I don&#x27;t understand the different betwee...'''
date = "2015-06-27T09:15:00Z"
lastmod = "2015-06-27T11:24:00Z"
weight = 43601
keywords = [ "iographs", "smooth" ]
aliases = [ "/questions/43601" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Smooth in IO Graphs](/questions/43601/smooth-in-io-graphs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone!</p><p>I want to export a graphic with the number of packets/second of my capture. The problem is that I have a lot of packets at second 13, and any packet at second 14, for example. So, I would like to apply the smooth option of IO Graphs in Y axis, but I don't understand the different between M.avg 4 , M.avg 8 , M.avg 16 , M.avg 32 , M.avg 64...</p><p>Can someone explain to me the difference between the smooth?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">iographs smooth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '15, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/ecf95f2aa8bc45e6f9a37260bfe0e2a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ralvarep&#39;s gravatar image" /><p>ralvarep<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ralvarep has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 15:47</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-43601" class="comments-container"></div><div id="comment-tools-43601" class="comment-tools"></div><div class="clear"></div><div id="comment-43601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43603"></span>

<div id="answer-container-43603" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43603-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Smooth means that it will not graph the value per tick but will accumulate 4,8,16,32 ... ticks and built an average over those and graph this average (of 4,16,32 etc). Regards Matthias<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-43603" class="comments-container"><span id="43604"></span><div id="comment-43604" class="comment"><div id="post-43604-score" class="comment-score"></div><div class="comment-text"><p>Thanks mrEEde!</p></div><div id="comment-43604-info" class="comment-info"><span class="comment-age">(27 Jun '15, 12:42)</span> ralvarep</div></div></div><div id="comment-tools-43603" class="comment-tools"></div><div class="clear"></div><div id="comment-43603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

