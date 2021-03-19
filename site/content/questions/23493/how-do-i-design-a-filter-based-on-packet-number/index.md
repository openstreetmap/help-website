+++
type = "question"
title = "How do I design a filter based on packet number"
description = '''I discovered that some TCP sessions do not stop after [FIN ACK]. To calculate the real throughput, I have to exclude the packets being sent after [FIN ACK]. I am trying to design a filter to filter out packets after a certain time (or packet number) and before a certain time (or packet number). What...'''
date = "2013-07-31T22:51:00Z"
lastmod = "2013-08-03T10:27:00Z"
weight = 23493
keywords = [ "filter", "time", "packet-number" ]
aliases = [ "/questions/23493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I design a filter based on packet number](/questions/23493/how-do-i-design-a-filter-based-on-packet-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I discovered that some TCP sessions do not stop after [FIN ACK]. To calculate the real throughput, I have to exclude the packets being sent after [FIN ACK]. I am trying to design a filter to filter out packets after a certain time (or packet number) and before a certain time (or packet number).</p><p>What should be the syntax of the filter?</p></div><div id="question-tags" class="tags-container tags">filter time packet-number</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/5dc1b6a50ce1e6edcbdea02e9fe1d2eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3mgold&#39;s gravatar image" /><p>3mgold<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3mgold has no accepted answers">0%</span></p></div></div><div id="comments-container-23493" class="comments-container"></div><div id="comment-tools-23493" class="comment-tools"></div><div class="clear"></div><div id="comment-23493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23525"></span>

<div id="answer-container-23525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using tshark</p><p>use the below filter</p><p>tshark -r trace.pcap -R "frame.number&gt;500"</p><p>frame.number &gt; 500 will only show you packets after frame number 500 that is first 499 packets will not be shown to you</p><p>else in wireshark you can put the above filter in filter window and apply</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '13, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/3ac62e4a103b118d6c93f65777d77402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAVI_TANDON&#39;s gravatar image" /><p>RAVI_TANDON<br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAVI_TANDON has no accepted answers">0%</span></p></div></div><div id="comments-container-23525" class="comments-container"></div><div id="comment-tools-23525" class="comment-tools"></div><div class="clear"></div><div id="comment-23525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

