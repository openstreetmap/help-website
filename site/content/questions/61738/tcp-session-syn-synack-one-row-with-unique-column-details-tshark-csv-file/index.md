+++
type = "question"
title = "TCP Session Syn &amp; Syn/Ack One row with unique column details Tshark csv file"
description = '''Trying to use Tshark to create a csv file containing:  prefer live capture filtering on &quot;tcp[tcpflags] &amp;amp; (tcp-syn)&quot; working or reading from a pcap using display filtering if required from the result of the above capture filter This is the output I am desiring in one row with data from the two sy...'''
date = "2017-06-01T17:44:00Z"
lastmod = "2017-06-02T01:46:00Z"
weight = 61738
keywords = [ "statistics", "custom", "endpoint", "tshark", "tshark_2pass" ]
aliases = [ "/questions/61738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Session Syn & Syn/Ack One row with unique column details Tshark csv file](/questions/61738/tcp-session-syn-synack-one-row-with-unique-column-details-tshark-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to use Tshark to create a csv file containing:</p><p>prefer live capture filtering on "tcp[tcpflags] &amp; (tcp-syn)" working or reading from a pcap using display filtering if required from the result of the above capture filter</p><p>This is the output I am desiring in one row with data from the two syn-syn/ack packets from each session. ip.src, ip.id (from src), ip.dst, ip.id (from dst), tcp.srcport, tcp.dstport, all on one row.</p><p>I know this requires data from the stream as it is contained in two packets. I don't want to capture the ack, only syn-syn/ack to reduce packets needed to see the session setup with syn's only.</p><p>I can get the values for individual packets, but not the bidirectional session on one row.</p><p>I need to do this repeatedly, so trying to get this built to optimize repeated captures/ reports.</p><p>Imagine it requires 2 pass if can be done in live capture?</p><p>Failing not being able to do this at capture, I can read the resultant syn-syn/ack capture file after capture to build the single row with the ip.id's and other details in both directions for each session.</p><p>I am also looking to build another report that is similar to endpoint statistics adding some unique fields into the report to shorten the list of all sessions to one row per peer ip's.</p><p>appreciate ideas!</p><p>Thanks,</p><p>Bill</p></div><div id="question-tags" class="tags-container tags">statistics custom endpoint tshark tshark_2pass</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '17, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/0a57afcbb8cd956e0f42b1bd1a2c3783?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetman007&#39;s gravatar image" /><p>packetman007<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetman007 has no accepted answers">0%</span></p></div></div><div id="comments-container-61738" class="comments-container"></div><div id="comment-tools-61738" class="comment-tools"></div><div class="clear"></div><div id="comment-61738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61743"></span>

<div id="answer-container-61743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think this can be done via tshark, because it always prints fields (using -Tfields -e...) per packet. So you'll always end up with two rows that way, not just one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '17, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61743" class="comments-container"><span id="61751"></span><div id="comment-61751" class="comment"><div id="post-61751-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I was thinking similarly, but thought there might be some 2 pass process using tcp stream or other session endpoint statistic variables that might make it possible. Appreciate your help. Bill</p></div><div id="comment-61751-info" class="comment-info"><span class="comment-age">(02 Jun '17, 08:09)</span> packetman007</div></div></div><div id="comment-tools-61743" class="comment-tools"></div><div class="clear"></div><div id="comment-61743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

