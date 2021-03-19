+++
type = "question"
title = "Wireshark filters"
description = '''Hi,I have one socket chat program and I want capture their traffic, I want write a filter that can capture based on special text ,for example if they said &quot;hi&quot; ,wireshark capture it . please help me to write this filtering .'''
date = "2016-03-26T04:01:00Z"
lastmod = "2016-03-26T09:16:00Z"
weight = 51216
keywords = [ "filter", "text" ]
aliases = [ "/questions/51216" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark filters](/questions/51216/wireshark-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51216-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,I have one socket chat program and I want capture their traffic, I want write a filter that can capture based on special text ,for example if they said "hi" ,wireshark capture it . please help me to write this filtering .</p></div><div id="question-tags" class="tags-container tags">filter text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '16, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/ae7852f0d8deb0a2f32c0385c4204509?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eli&#39;s gravatar image" /><p>Eli<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eli has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 15:44</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-51216" class="comments-container"></div><div id="comment-tools-51216" class="comment-tools"></div><div class="clear"></div><div id="comment-51216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51217"></span>

<div id="answer-container-51217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51217-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the unlikely case of your chat traffic being un-encrypted the filter would be</p><pre><code>frame contains &quot;hi&quot; or frame contains &quot;Hi&quot;</code></pre><p>but I have doubts that his is the case. If it is TLS encrypted you cannot see the plain text data and therefore cannot filter on the content of the encrypted packets.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '16, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-51217" class="comments-container"></div><div id="comment-tools-51217" class="comment-tools"></div><div class="clear"></div><div id="comment-51217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

