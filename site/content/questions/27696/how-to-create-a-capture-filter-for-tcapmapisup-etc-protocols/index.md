+++
type = "question"
title = "how to create a capture filter for TCAP/MAP/ISUP e.t.c protocols"
description = '''Hello everyone ! Tell me, can I create сapture-filter according to any protocol required me? Signal exchange large, want to reduce the load and file size.  Or other suitable - record only those frames in which an occurrence of TCAP ?'''
date = "2013-12-03T04:08:00Z"
lastmod = "2013-12-03T05:56:00Z"
weight = 27696
keywords = [ "capture-filter" ]
aliases = [ "/questions/27696" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to create a capture filter for TCAP/MAP/ISUP e.t.c protocols](/questions/27696/how-to-create-a-capture-filter-for-tcapmapisup-etc-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone ! Tell me, can I create сapture-filter according to any protocol required me? Signal exchange large, want to reduce the load and file size. Or other suitable - record only those frames in which an occurrence of TCAP ?</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/0f2d15c8c5fb64794cf0125c807d1399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Larush&#39;s gravatar image" /><p>Larush<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Larush has no accepted answers">0%</span></p></div></div><div id="comments-container-27696" class="comments-container"></div><div id="comment-tools-27696" class="comment-tools"></div><div class="clear"></div><div id="comment-27696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27707"></span>

<div id="answer-container-27707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27707-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters (BPF code) are limited to what they can do as they have to be very fast and loop free as they are executed for every packet recived/sent basicaly they look at a fixed offset into a packet and in higer level protocols the information you are looking for will be at diferent offset in different messages. (ref <a href="http://www.cs.ucr.edu/~marios/ethereal-tcpdump.pdf">http://www.cs.ucr.edu/~marios/ethereal-tcpdump.pdf</a> ).</p><p>But you can use IP address and port to limit capture size. If you are using switch mirroring looking over the mirror setup might help too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 07:00</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27707" class="comments-container"><span id="27743"></span><div id="comment-27743" class="comment"><div id="post-27743-score" class="comment-score"></div><div class="comment-text"><p>I work a signalman, I need to analyze the signal exchange between the signal modules, IP address filtering will not reduce the flow of messages. I will study the document.</p></div><div id="comment-27743-info" class="comment-info"><span class="comment-age">(03 Dec '13, 21:13)</span> Larush</div></div></div><div id="comment-tools-27707" class="comment-tools"></div><div class="clear"></div><div id="comment-27707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

