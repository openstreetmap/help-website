+++
type = "question"
title = "what is the meaning of &quot;dropped&quot;count of capture result"
description = '''when i captured some packets, the result shows  &quot;Packets : xxxxx Displayed : xxxxx Marked : 0 Dropped : xxxxx&quot; in the bottom of capture result.(xxxx -&amp;gt; any number) if there is &quot;Dropped&quot; count, for example  &quot;Packets : xxxxx Displayed : xxxxx Marked : 0 Dropped : 10&quot; what does the &quot;10&quot; means? does ...'''
date = "2010-11-18T02:22:00Z"
lastmod = "2010-11-18T02:39:00Z"
weight = 1002
keywords = [ "dropped" ]
aliases = [ "/questions/1002" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what is the meaning of "dropped"count of capture result](/questions/1002/what-is-the-meaning-of-droppedcount-of-capture-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1002-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i captured some packets, the result shows "Packets : xxxxx Displayed : xxxxx Marked : 0 Dropped : xxxxx" in the bottom of capture result.(xxxx -&gt; any number) if there is "Dropped" count, for example "Packets : xxxxx Displayed : xxxxx Marked : 0 Dropped : 10" what does the "10" means? does that mean there are 10 packet the Wireshark didn`t capture? or what does that mean? is it possible there could be uncapturable packet in case the traffic is coming with wire rate?</p></div><div id="question-tags" class="tags-container tags">dropped</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '10, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/23a8654870c975edaf59718ee1344601?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="defpoet4&#39;s gravatar image" /><p>defpoet4<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="defpoet4 has no accepted answers">0%</span></p></div></div><div id="comments-container-1002" class="comments-container"></div><div id="comment-tools-1002" class="comment-tools"></div><div class="clear"></div><div id="comment-1002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1003"></span>

<div id="answer-container-1003" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1003-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, dropped packets count packets which WERE on the wire, but were NOT captured by wireshark. Depending on your capture setup, it can absolutely happen that you have packet drops while capturing. Reasons for drops &gt; 0 are spread widely.</p><p>Two examples:</p><ul><li>Could be your harddrive, if it's too slow to capture to disk at line rate</li><li>Could be the capture setting itself - live scrolling and update list in realtime are a good start to disable when packets are dropped</li></ul><p>Of course lots of other factors are possible, but those are the first two I look at</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '10, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-1003" class="comments-container"></div><div id="comment-tools-1003" class="comment-tools"></div><div class="clear"></div><div id="comment-1003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

