+++
type = "question"
title = "How to re-analyze tcp packets to http after &quot;Out-Of-Order&quot;"
description = '''I use tshark (default options) and get the situation 1329 81.102581 192.168.100.2 → 104.20.6.117 HTTP 589 POST /api/v1/service/get/json HTTP/1.1  1330 81.107743 104.20.6.117 → 192.168.100.2 TCP 54 80→49439 [ACK] Seq=48519 Ack=7574 Win=47104 Len=0 1331 81.174389 104.20.6.117 → 192.168.100.2 TCP 1514 ...'''
date = "2016-11-11T04:42:00Z"
lastmod = "2017-01-10T06:03:00Z"
weight = 57314
keywords = [ "lost_segment", "tshark", "reordering" ]
aliases = [ "/questions/57314" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to re-analyze tcp packets to http after "Out-Of-Order"](/questions/57314/how-to-re-analyze-tcp-packets-to-http-after-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use tshark (default options) and get the situation</p><pre><code>1329  81.102581 192.168.100.2 → 104.20.6.117 HTTP 589 POST /api/v1/service/get/json HTTP/1.1 
1330  81.107743 104.20.6.117 → 192.168.100.2 TCP 54 80→49439 [ACK] Seq=48519 Ack=7574 Win=47104 Len=0
1331  81.174389 104.20.6.117 → 192.168.100.2 TCP 1514 [TCP segment of a reassembled PDU]
1332  81.174400 104.20.6.117 → 192.168.100.2 HTTP 1029 [TCP Previous segment not captured] Continuation
1333  81.174420 104.20.6.117 → 192.168.100.2 TCP 1514 [TCP Out-Of-Order] 80→49439 [ACK] Seq=49979 Ack=7574 Win=47104 Len=1460
1334  81.174423 104.20.6.117 → 192.168.100.2 HTTP 531 Continuation
1335  81.174439 104.20.6.117 → 192.168.100.2 HTTP 59 Continuation</code></pre><p>Can I get a reparsed HTTP request after missing packages? I can see reordered if click "Follow TCP stream" if use wireshark.</p></div><div id="question-tags" class="tags-container tags">lost_segment tshark reordering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '16, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/74124ae01d73f536a320e2947118fdaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexey&#39;s gravatar image" /><p>alexey<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jan '17, 06:37</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57314" class="comments-container"></div><div id="comment-tools-57314" class="comment-tools"></div><div class="clear"></div><div id="comment-57314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58639"></span>

<div id="answer-container-58639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, once TCP's reassembly is messed up (by a missing packet) there's no way for it to recover (for that PDU--it will recover once it can find the start of the next PDU).</p><p>(Follow TCP stream fakes it out by telling the consumer--generally a human!--that there are missing bytes. Wireshark's dissectors--e.g., in this case, the HTTP dissector--would not be able to handle that well.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '17, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58639" class="comments-container"></div><div id="comment-tools-58639" class="comment-tools"></div><div class="clear"></div><div id="comment-58639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

