+++
type = "question"
title = "How to add packettime in pcap header ?"
description = '''Hi, i am trying to generate pcap files from a collection of packet data. I put the global header and packet data correctly and it appeared correctly in wireshark. But the problem is with the arrival time of the packet, which is not getting as expected; Can someone please describe how to create the f...'''
date = "2014-01-15T22:44:00Z"
lastmod = "2014-01-16T22:52:00Z"
weight = 28948
keywords = [ "header", "pcap" ]
aliases = [ "/questions/28948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add packettime in pcap header ?](/questions/28948/how-to-add-packettime-in-pcap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28948-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i am trying to generate pcap files from a collection of packet data. I put the global header and packet data correctly and it appeared correctly in wireshark. But the problem is with the arrival time of the packet, which is not getting as expected;</p><p>Can someone please describe how to create the first 8 bytes in the pcap header ?</p><p>I give the first 4 byte as seconds from 1970/1/1 till now and next 4 byte as 00 00 00 05.</p></div><div id="question-tags" class="tags-container tags">header pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '14, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/215d9378b10901b1233ef89a5d7cd496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binu%20Babu&#39;s gravatar image" /><p>Binu Babu<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binu Babu has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '14, 00:09</p></div></div><div id="comments-container-28948" class="comments-container"><span id="28977"></span><div id="comment-28977" class="comment"><div id="post-28977-score" class="comment-score"></div><div class="comment-text"><blockquote><p>which is not getting as expected</p></blockquote><p>What are you expecting, and what are you getting?</p></div><div id="comment-28977-info" class="comment-info"><span class="comment-age">(16 Jan '14, 18:22)</span> Guy Harris ♦♦</div></div><span id="28983"></span><div id="comment-28983" class="comment"><div id="post-28983-score" class="comment-score"></div><div class="comment-text"><p>I need to see the arrival time as 2013-01-15 02:00:00.000000000 in pcap file with wireshark. For this i took the seconds since 1970/1/1 till the same datetime as mentioned above and put in the pcap header(as first 4 byte). But its getting as wrong date in wireshark.</p></div><div id="comment-28983-info" class="comment-info"><span class="comment-age">(16 Jan '14, 22:04)</span> Binu Babu</div></div><span id="28984"></span><div id="comment-28984" class="comment"><div id="post-28984-score" class="comment-score"></div><div class="comment-text"><p>What date do you get in Wireshark?</p></div><div id="comment-28984-info" class="comment-info"><span class="comment-age">(16 Jan '14, 22:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-28948" class="comment-tools"></div><div class="clear"></div><div id="comment-28948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28986"></span>

<div id="answer-container-28986" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28986-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is showing in date field as 'Not representable'.</p><p><em>Edit</em>: Hi Guy Harris, I could trace the mistake ,that was in the magic number order. I used it as "D4 C3 B2 A1" and didn't swap the timestamp.Now its working fine by swapping the seconds in the pcap header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/215d9378b10901b1233ef89a5d7cd496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binu%20Babu&#39;s gravatar image" /><p>Binu Babu<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binu Babu has one accepted answer">33%</span></p></div></div><div id="comments-container-28986" class="comments-container"></div><div id="comment-tools-28986" class="comment-tools"></div><div class="clear"></div><div id="comment-28986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

