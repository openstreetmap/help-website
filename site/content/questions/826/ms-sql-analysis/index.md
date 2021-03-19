+++
type = "question"
title = "MS SQL analysis"
description = '''Hello All, I am looking into MS SQL service response time i didn&#x27;t found any info about it is there any analysis for it and some Tshark query would be helpful. Please advice Thanks'''
date = "2010-11-04T22:43:00Z"
lastmod = "2010-11-07T09:21:00Z"
weight = 826
keywords = [ "mssql" ]
aliases = [ "/questions/826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MS SQL analysis](/questions/826/ms-sql-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All, I am looking into MS SQL service response time i didn't found any info about it is there any analysis for it and some Tshark query would be helpful.</p><p>Please advice Thanks</p></div><div id="question-tags" class="tags-container tags">mssql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '10, 22:43</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div></div><div id="comments-container-826" class="comments-container"></div><div id="comment-tools-826" class="comment-tools"></div><div class="clear"></div><div id="comment-826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="848"></span>

<div id="answer-container-848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-848-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(couldn't post this as a comment due to character limitation) Tbaror, it depends on how proficient you are with pkt analysis. But the way I would start is by lookinging for TCP level anomalies. Open the trace in Wireshark and do a 'tcp.analysis.flags' to see what shows up. Things to took for are 1) FAST RETRANSMISSIONS 2) Increment duplicate ACK numbers (Dup Ack #1, Dup Ack #2, Dup Ack #3...etc) 3) Long gaps in between packets. You should add a delta (delta from previous packet) so you can quickly sort on it. Or you can change the default time display if you don't want to add a new column - but I highly recommend it. 4) TCP zero window events</p><p>If every other packet is flagged as "out of sequence, out of order, etc, then your capture was done incorrectly and you need to start over.</p><p>Once you've ruled out any and all tcp level issues (lack of tcp window size, etc.) then you need to look at what query is causing the server to be slow.</p><p>This will show up when you sort by the delta column. Typically, you will see a select/update query followed by a long delay before the server spits out the answer. In this case, it's safe to assume that server processing delay is at fault.</p><p>Other things to look for are records that come back one row at a time. One clue that this is happening is by looking at the end of the response. It will be marked by certain words that delimit the rows, or it may have the PSH bit set.</p><p>Also, the two most common issues I see with DB slowness (not including inefficient queries) are 1) table scan because index is not there or updated and 2) lack of batch size that causes inefficient SELECT queries.</p><p>Depending on your level of expertise, you will know what to do with the above info, or you may need more clarification. Just come back with the parts that don't make sense and I can expand on the topic. Also, if you go back to Wireshark's site, you should see a link for Sharkfest. I did a presentation with slow DB query where the batch size caused quite a bit of pain for the developers. If you can't find it, let me know as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '10, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-848" class="comments-container"></div><div id="comment-tools-848" class="comment-tools"></div><div class="clear"></div><div id="comment-848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

