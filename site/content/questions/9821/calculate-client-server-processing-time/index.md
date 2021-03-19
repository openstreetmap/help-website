+++
type = "question"
title = "Calculate Client / server processing time"
description = '''Hi Everybody, i use Wireshark since some years to help me to troubleshoot performance issue. As Wireshark can see the between packets, it should provide the total time spend (by processing). I never find in Wireshark where i can have this kind of information. I can&#x27;t imagine Wireshark doesn&#x27;t provid...'''
date = "2012-03-28T08:13:00Z"
lastmod = "2012-03-29T00:24:00Z"
weight = 9821
keywords = [ "calculate", "time" ]
aliases = [ "/questions/9821" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate Client / server processing time](/questions/9821/calculate-client-server-processing-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everybody,</p><p>i use Wireshark since some years to help me to troubleshoot performance issue.</p><p>As Wireshark can see the between packets, it should provide the total time spend (by processing). I never find in Wireshark where i can have this kind of information.</p><p>I can't imagine Wireshark doesn't provide this information.</p><p>Could you help me?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">calculate time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '12, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/25fcd4b6692b20e9189d8f0b52f1663d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="any-one&#39;s gravatar image" /><p>any-one<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="any-one has no accepted answers">0%</span></p></div></div><div id="comments-container-9821" class="comments-container"></div><div id="comment-tools-9821" class="comment-tools"></div><div class="clear"></div><div id="comment-9821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9822"></span>

<div id="answer-container-9822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9822-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is for analyzing network communications, not server performance. Yes, Wireshark sees the time between packets, but Wireshark doesn't know how much of that time was because the server was processing a request, and how much was because it simply didn't have anything to send. Note also that some of the time between packets will be network latency; how much depends partly on where you are doing your capturing.</p><p>However, if you know enough about the communication, you may be able to get an idea of the processing time involved in a particular transaction.</p><p>See <a href="http://sharkfest.wireshark.org/sharkfest.08/T2-4_Chappell_Trace-File-Analysis_Latency.pdf">this link</a> for a Sharkfest presentation in which Laura Chappell shows how to determine the various types of latency involved in a web server communication. Page 9 shows how to determine how much time the server spent processing a GET request before returning data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9822" class="comments-container"><span id="9828"></span><div id="comment-9828" class="comment"><div id="post-9828-score" class="comment-score"></div><div class="comment-text"><p>Hi Jim</p><p>thanks for your reply. I agree, it depends of where the capture is doing. Of course, it's possible to see server processing time only if the capture is done on the server.</p><p>Capturing at both end (in client and in server) during a communication, it should be interresting to calculate easily processing time at each end and so determine easily if the performance issue is caused on the server, on the client or in the network (latency, too many round-trip..).</p><p>Best regards</p></div><div id="comment-9828-info" class="comment-info"><span class="comment-age">(28 Mar '12, 14:17)</span> any-one</div></div></div><div id="comment-tools-9822" class="comment-tools"></div><div class="clear"></div><div id="comment-9822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9831"></span>

<div id="answer-container-9831" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9831-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I,</p><p>i think i find a solution. In wireshark i can display a new column with Dealta-time (which is the time between last packet).</p><p>From a capture done on the server - i filter only packet sent by server - i export to CSV file - I open this CSV in Excel an calculate easily the sum of the column "Delta Time".</p><p>If i'm not wrong, this represent the total processing time of the server.</p><p>Best regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/25fcd4b6692b20e9189d8f0b52f1663d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="any-one&#39;s gravatar image" /><p>any-one<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="any-one has no accepted answers">0%</span></p></div></div><div id="comments-container-9831" class="comments-container"></div><div id="comment-tools-9831" class="comment-tools"></div><div class="clear"></div><div id="comment-9831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

