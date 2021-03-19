+++
type = "question"
title = "how to read for example the following frame.time_delta between 2 packets"
description = '''176 Jul 25, 2016 01:10:16.993463000 CEST 0.000424000 23.6.1.111 23.4.1.10 177 Jul 25, 2016 01:10:16.994604000 CEST 0.001141000 23.4.1.10 23.6.1.111  tshark -r r.pcap -T fields -E header=y -e frame.number -e frame.time -e frame.time_delta -e ip.src -e ip.dst | awk &#x27;{print $7}&#x27; &amp;gt; RRT  e=0 while rea...'''
date = "2016-07-24T19:06:00Z"
lastmod = "2016-07-26T04:06:00Z"
weight = 54278
keywords = [ "miliseconds" ]
aliases = [ "/questions/54278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to read for example the following frame.time\_delta between 2 packets](/questions/54278/how-to-read-for-example-the-following-frametime_delta-between-2-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>176 Jul 25, 2016 01:10:16.993463000 CEST    0.000424000 23.6.1.111  23.4.1.10
177 Jul 25, 2016 01:10:16.994604000 CEST    0.001141000 23.4.1.10   23.6.1.111

tshark -r r.pcap -T fields -E header=y -e frame.number -e frame.time -e frame.time_delta -e ip.src -e ip.dst | awk &#39;{print $7}&#39; &gt; RRT

e=0
while read p; do let e=$e+$p; done &lt; RRT
echo $e
0.16371100000000005</code></pre><p>$e here means 164 ms??</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">miliseconds</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '16, 19:06</strong></p><img src="https://secure.gravatar.com/avatar/5002cb544de33c526f994599d3ae391f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppcap&#39;s gravatar image" /><p>ppcap<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppcap has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '16, 04:06</p></div></div><div id="comments-container-54278" class="comments-container"></div><div id="comment-tools-54278" class="comment-tools"></div><div class="clear"></div><div id="comment-54278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54332"></span>

<div id="answer-container-54332" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54332-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>0.001141000 0.001 == 1 ms 0.0001 == 100 micro 0.000141000 === 141 microsec 0.000000100 === 100 nanosec 0.000000001 === 1 nanosec</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/5002cb544de33c526f994599d3ae391f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppcap&#39;s gravatar image" /><p>ppcap<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppcap has one accepted answer">50%</span></p></div></div><div id="comments-container-54332" class="comments-container"></div><div id="comment-tools-54332" class="comment-tools"></div><div class="clear"></div><div id="comment-54332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

