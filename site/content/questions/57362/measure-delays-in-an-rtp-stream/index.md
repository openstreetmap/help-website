+++
type = "question"
title = "Measure delays in an RTP stream"
description = '''My task is to perform an experiment with RTP packets delays measurement (the traffic is simply streaming music from my server to my PC).  I&#x27;ve read a related question (Measure packet delay RTP) and figured out that it&#x27;s not really possible if I capture the traffic only on my PC, because Wireshark ca...'''
date = "2016-11-13T08:02:00Z"
lastmod = "2016-11-13T10:43:00Z"
weight = 57362
keywords = [ "delay", "rtp" ]
aliases = [ "/questions/57362" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Measure delays in an RTP stream](/questions/57362/measure-delays-in-an-rtp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My task is to perform an experiment with RTP packets delays measurement (the traffic is simply streaming music from my server to my PC).</p><p>I've read a related question (<a href="https://ask.wireshark.org/questions/37663/measure-packet-delay-rtp">Measure packet delay RTP</a>) and figured out that it's not really possible if I capture the traffic only on my PC, because Wireshark can't calculate delay in such case. So, obviously, I have to capture traffic also on the server-side. It's OK, I can run tshark there for capturing.</p><p>My question is: what should I do after? How do I merge two captures (local and remote) and how do I pass them to Wireshark to let it calculate delays for me? If I simply merge two pcap's to one file and load it to Wireshark, will it understand that it's the same RTP session captured from two machines and will it be able to calculate packets delays for me?</p></div><div id="question-tags" class="tags-container tags">delay rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/9d8e7bdd418d0b727f76b47e655bc465?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trixter&#39;s gravatar image" /><p>trixter<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trixter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '16, 08:03</p></div></div><div id="comments-container-57362" class="comments-container"></div><div id="comment-tools-57362" class="comment-tools"></div><div class="clear"></div><div id="comment-57362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57364"></span>

<div id="answer-container-57364" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57364-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The simple answer would be "open one of the files, then go to <code>File-&gt;Merge</code>, choose <code>Merge packets chronologically</code>, select the other file and press <code>Open</code>. Then you would just compare the differences of timestamps of pairs of RTP packets bearing the same RTP sequence number.</p><p>However, you need that the real time clock of your server and your PC are well synchronized, as eventual difference of the two machines' real time clock will skew the result. If everything is on a single LAN, the relative significance of the clock difference may be really high.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '16, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '16, 10:21</p></div></div><div id="comments-container-57364" class="comments-container"><span id="57365"></span><div id="comment-57365" class="comment"><div id="post-57365-score" class="comment-score"></div><div class="comment-text"><blockquote><p>"Then you would just compare the differences of timestamps of pairs of RTP packets bearing the same RTP sequence number." Can Wireshark do it automatically or I should write some script to achieve it?</p></blockquote></div><div id="comment-57365-info" class="comment-info"><span class="comment-age">(13 Nov '16, 11:20)</span> trixter</div></div><span id="57380"></span><div id="comment-57380" class="comment"><div id="post-57380-score" class="comment-score"></div><div class="comment-text"><p>There is nothing like that embedded in Wireshark.</p><p>If I were to do that, I'd use the good ol' Excel - I'd export packets with the same ssrc from both captures, not merging them together, into csv files, like this:</p><p><code>tshark -r your\file\name.pcapng -Y "rtp.ssrc == 0xyourssrc" -T fields -e rtp.seq -e frame.time_epoch &gt; your\file\name.csv</code></p><p>I would then import these files to Excel (with space as separator), use the first columns of both (the rtp.seq values) to properly match the pairs of timestamps and notice eventual lost packets, and let Excel calculate the average of differences between the second columns, leaving out lost packets from the calculation.</p></div><div id="comment-57380-info" class="comment-info"><span class="comment-age">(14 Nov '16, 10:20)</span> sindy</div></div></div><div id="comment-tools-57364" class="comment-tools"></div><div class="clear"></div><div id="comment-57364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

