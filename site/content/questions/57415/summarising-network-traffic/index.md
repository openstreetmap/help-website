+++
type = "question"
title = "Summarising network traffic"
description = '''Hi,  I&#x27;m using a Windows 10 laptop with performance monitor and see occasional network spikes. Is there a WireShark filter I can use to see what&#x27;s using the bandwidth? It&#x27;d be ideal to be able to identify that 50% of all packets are related to application X or going to IP 192.168.1.1. Thanks'''
date = "2016-11-16T03:39:00Z"
lastmod = "2016-11-16T03:50:00Z"
weight = 57415
keywords = [ "bandwidth", "utilization", "summary" ]
aliases = [ "/questions/57415" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Summarising network traffic](/questions/57415/summarising-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57415-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using a Windows 10 laptop with performance monitor and see occasional network spikes. Is there a WireShark filter I can use to see what's using the bandwidth? It'd be ideal to be able to identify that 50% of all packets are related to application X or going to IP 192.168.1.1.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">bandwidth utilization summary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '16, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/519cbaefe09a535e3882a857b8f56f23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aetius&#39;s gravatar image" /><p>aetius<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aetius has no accepted answers">0%</span></p></div></div><div id="comments-container-57415" class="comments-container"></div><div id="comment-tools-57415" class="comment-tools"></div><div class="clear"></div><div id="comment-57415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57417"></span>

<div id="answer-container-57417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57417-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried to use <code>Statistics -&gt; Conversations</code> and sort the lines by Packets or Bytes, A-&gt;B or B-&gt;A, by clicking the header of the respective column?</p><p>Wireshark won't tell you which application is responsible for a particular traffic; for that, other tools exist in Windows (I don't remember the name of the one you need in particular, sorry). Indirectly, you can identify applications by the port used at server side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57417" class="comments-container"><span id="57418"></span><div id="comment-57418" class="comment"><div id="post-57418-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'll give that a go</p></div><div id="comment-57418-info" class="comment-info"><span class="comment-age">(16 Nov '16, 04:11)</span> aetius</div></div><span id="57427"></span><div id="comment-57427" class="comment"><div id="post-57427-score" class="comment-score"></div><div class="comment-text"><p>use "netstat -ano" to view all active and listening sockets along with the PID using that socket. Then use "Task Manager" to view the PID and associated application or service.</p></div><div id="comment-57427-info" class="comment-info"><span class="comment-age">(16 Nov '16, 15:46)</span> Rooster_50</div></div></div><div id="comment-tools-57417" class="comment-tools"></div><div class="clear"></div><div id="comment-57417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

