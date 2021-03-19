+++
type = "question"
title = "count total traffic between 2 servers by port"
description = '''Hi, can Wireshark count total traffic between 2 servers by port over a timeframe? I need to figure out how much traffic goes between two servers on certain ports as I&#x27;m considering moving one to the cloud and need to estimate data transfer costs. Thanks!'''
date = "2011-01-15T13:43:00Z"
lastmod = "2011-01-15T14:38:00Z"
weight = 1762
keywords = [ "count", "traffic" ]
aliases = [ "/questions/1762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [count total traffic between 2 servers by port](/questions/1762/count-total-traffic-between-2-servers-by-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1762-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, can Wireshark count total traffic between 2 servers by port over a timeframe?</p><p>I need to figure out how much traffic goes between two servers on certain ports as I'm considering moving one to the cloud and need to estimate data transfer costs.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">count traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '11, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/b60f657b5f94547c002a13abc650c841?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanhartd&#39;s gravatar image" /><p>hanhartd<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanhartd has no accepted answers">0%</span></p></div></div><div id="comments-container-1762" class="comments-container"></div><div id="comment-tools-1762" class="comment-tools"></div><div class="clear"></div><div id="comment-1762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1763"></span>

<div id="answer-container-1763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1763-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know exactly what you are looking for, but it seems that you could list the two servers in the disply filter like "ip.addr==&lt;srva&gt; &amp;&amp; ip.addr==&lt;srvb&gt;". Then go into Statistics &gt; Conversations and limit to display filter. Then look at the tcp and udp tabs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '11, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1763" class="comments-container"></div><div id="comment-tools-1763" class="comment-tools"></div><div class="clear"></div><div id="comment-1763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

