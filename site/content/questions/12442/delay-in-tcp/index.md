+++
type = "question"
title = "delay in TCP"
description = '''Hi!! I am new to wireshark and I am trying to plot and measure the delay of an end to end tcp packet, that is, I would like to find out how long it takes a tcp packet transmitted from a node to be received from the another node. Thanks!!!'''
date = "2012-07-04T08:37:00Z"
lastmod = "2012-07-04T10:31:00Z"
weight = 12442
keywords = [ "rocio" ]
aliases = [ "/questions/12442" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [delay in TCP](/questions/12442/delay-in-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12442-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!!</p><p>I am new to wireshark and I am trying to plot and measure the delay of an end to end tcp packet, that is, I would like to find out how long it takes a tcp packet transmitted from a node to be received from the another node.</p><p>Thanks!!!</p></div><div id="question-tags" class="tags-container tags">rocio</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '12, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/8d28a5820c4e6d8f2e49289dcd08d719?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rocio&#39;s gravatar image" /><p>Rocio<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rocio has no accepted answers">0%</span></p></div></div><div id="comments-container-12442" class="comments-container"></div><div id="comment-tools-12442" class="comment-tools"></div><div class="clear"></div><div id="comment-12442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12444"></span>

<div id="answer-container-12444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12444-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you captured only on one side (client, server or somewhere between), you can't really measure that time exactly, however you can estimate it by looking at the SYN,SYN-ACK,ACK sequence (look at the time difference of these three packets) and the mean RTT of other SEQ/ACK 'sequences'.</p><p>If you want to get a general overview of all packets in a TCP connection (not just a certain packet), you can draw a TCP Stream Graph</p><blockquote><p><code>Statistics -&gt; TCP Stream Graph -&gt; Round Trip Time Graph</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '12, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '12, 10:34</p></div></div><div id="comments-container-12444" class="comments-container"><span id="12447"></span><div id="comment-12447" class="comment"><div id="post-12447-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Kurt!!! :D</p></div><div id="comment-12447-info" class="comment-info"><span class="comment-age">(04 Jul '12, 13:09)</span> Rocio</div></div></div><div id="comment-tools-12444" class="comment-tools"></div><div class="clear"></div><div id="comment-12444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

