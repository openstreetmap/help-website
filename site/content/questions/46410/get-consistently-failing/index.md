+++
type = "question"
title = "Get consistently failing"
description = '''When ran a wireshark because even though we can browse to anything on the internet from our server we are receiving; Error Message: 31: GetURL failure HTTP Error 18: An unknown error occurred while transferring data from the server: transfer closed with 4927 bytes remaining to read   We see our GETs...'''
date = "2015-10-07T12:02:00Z"
lastmod = "2015-10-07T12:45:00Z"
weight = 46410
keywords = [ "get" ]
aliases = [ "/questions/46410" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get consistently failing](/questions/46410/get-consistently-failing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46410-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When ran a wireshark because even though we can browse to anything on the internet from our server we are receiving;</p><pre><code>Error Message: 31: GetURL failure HTTP Error 18: An unknown error occurred while transferring data from the server: transfer closed with 4927 bytes remaining to read</code></pre><hr /><p>We see our GETs in the wireshark and are seeing that some look good but also we see periodically lines like the below, and are trying to figure out what issue is and why it's failing. Please help;</p><pre><code>3072  14.125484000  174.36.239.140  10.211.34.16  TCP 1429  [TCP Retransmission] 80?49173 [ACK] Seq=67626 Ack=177 Win=15680 Len=1375[Reassembly error, protocol TCP: New fragment overlaps old data (retransmission?)]
19761 34.145928000  174.36.239.140  10.211.34.16  HTTP  1897  [TCP Out-Of-Order] HTTP/1.1 200 OK  (text/plain)</code></pre><hr /><pre><code>19738 34.079971000  10.211.34.16  174.36.239.140  TCP 66  49237?80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
19743 34.100824000  174.36.239.140  10.211.34.16  TCP 66  80?49237 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1380 SACK_PERM=1 WS=64
19744 34.100852000  10.211.34.16  174.36.239.140  TCP 54  49237?80 [ACK] Seq=1 Ack=1 Win=66048 Len=0
19745 34.100956000  10.211.34.16  174.36.239.140  HTTP  473 GET /cgi-bin/bfgather/windowspatchesspanish?Time=1444229715 HTTP/1.1 
19746 34.121681000  174.36.239.140  10.211.34.16  TCP 60  80?49237 [ACK] Seq=1 Ack=420 Win=15680 Len=0
19747 34.124910000  174.36.239.140  10.211.34.16  TCP 1434  [TCP segment of a reassembled PDU]
19748 34.124980000  174.36.239.140  10.211.34.16  TCP 58  [TCP segment of a reassembled PDU]
19749 34.124987000  174.36.239.140  10.211.34.16  TCP 4190  [TCP segment of a reassembled PDU]
19750 34.124990000  174.36.239.140  10.211.34.16  TCP 58  [TCP segment of a reassembled PDU]
19751 34.124992000  174.36.239.140  10.211.34.16  TCP 2810  [TCP segment of a reassembled PDU]
19752 34.125019000  10.211.34.16  174.36.239.140  TCP 54  49237?80 [ACK] Seq=420 Ack=8281 Win=66048 Len=0
19753 34.125070000  174.36.239.140  10.211.34.16  TCP 58  [TCP segment of a reassembled PDU]
19754 34.125073000  174.36.239.140  10.211.34.16  TCP 2810  [TCP segment of a reassembled PDU]
19755 34.125076000  174.36.239.140  10.211.34.16  TCP 58  [TCP segment of a reassembled PDU]
19756 34.125079000  174.36.239.140  10.211.34.16  TCP 2810  [TCP segment of a reassembled PDU]
19757 34.125096000  10.211.34.16  174.36.239.140  TCP 54  49237?80 [ACK] Seq=420 Ack=13801 Win=66048 Len=0
19760 34.145925000  174.36.239.140  10.211.34.16  TCP 58  [TCP segment of a reassembled PDU]
19762 34.145983000  10.211.34.16  174.36.239.140  TCP 66  49237?80 [ACK] Seq=420 Ack=13806 Win=66048 Len=0 SLE=13805 SRE=13806
19763 34.146092000  10.211.34.16  174.36.239.140  TCP 54  49237?80 [FIN, ACK] Seq=420 Ack=13806 Win=66048 Len=0
19766 34.166846000  174.36.239.140  10.211.34.16  TCP 60  80?49237 [ACK] Seq=15649 Ack=421 Win=15680 Len=0
19783 34.369580000  174.36.239.140  10.211.34.16  TCP 1429  [TCP Retransmission] 80?49237 [ACK] Seq=13806 Ack=421 Win=15680 Len=1375[Reassembly error, protocol TCP: New fragment overlaps old data (retransmission?)]</code></pre></div><div id="question-tags" class="tags-container tags">get</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '15, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/30763ddf6646f359f358805a36415701?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WidgetWolf&#39;s gravatar image" /><p>WidgetWolf<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WidgetWolf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '15, 08:20</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46410" class="comments-container"></div><div id="comment-tools-46410" class="comment-tools"></div><div class="clear"></div><div id="comment-46410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46411"></span>

<div id="answer-container-46411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46411-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without a trace it is hard to say. But an answer for the "Reassembly error, protocol TCP: New fragment overlaps old data (re transmission?)" can be found here:<br />
<a href="https://ask.wireshark.org/questions/46011/reassembly-error-protocol-tcp-new-fragment-overlaps-old-data-re-transmission#46227">https://ask.wireshark.org/questions/46011/reassembly-error-protocol-tcp-new-fragment-overlaps-old-data-re-transmission#46227</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '15, 06:52</p></div></div><div id="comments-container-46411" class="comments-container"><span id="46420"></span><div id="comment-46420" class="comment"><div id="post-46420-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response but this link does not work.</p></div><div id="comment-46420-info" class="comment-info"><span class="comment-age">(08 Oct '15, 06:45)</span> WidgetWolf</div></div><span id="46421"></span><div id="comment-46421" class="comment"><div id="post-46421-score" class="comment-score"></div><div class="comment-text"><p>Please try the edited link</p></div><div id="comment-46421-info" class="comment-info"><span class="comment-age">(08 Oct '15, 06:53)</span> Christian_R</div></div></div><div id="comment-tools-46411" class="comment-tools"></div><div class="clear"></div><div id="comment-46411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

