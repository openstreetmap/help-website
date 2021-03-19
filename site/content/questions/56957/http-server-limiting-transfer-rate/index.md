+++
type = "question"
title = "HTTP server limiting transfer rate."
description = '''This capture was taken at the server. It is transferring a ~12MB file using HTTP. The RTT is 220ms I concluded from the capture that the server transmitting the file, is holding up the transfer by only transmitting in 9000 Byte chunks, then waiting for an ACK. The max bytes in flight is 18,000 Bytes...'''
date = "2016-11-03T14:56:00Z"
lastmod = "2016-11-04T13:54:00Z"
weight = 56957
keywords = [ "capture", "transfer.rate" ]
aliases = [ "/questions/56957" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [HTTP server limiting transfer rate.](/questions/56957/http-server-limiting-transfer-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56957-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This capture was taken at the server. It is transferring a ~12MB file using HTTP. The RTT is 220ms</p><p>I concluded from the capture that the server transmitting the file, is holding up the transfer by only transmitting in 9000 Byte chunks, then waiting for an ACK. The max bytes in flight is 18,000 Bytes, even though the client is advertising an RWIN of 65535.</p><p>Does anyone have any other thoughts on this analysis?</p><p>Here's a link to an anonymized version of the capture: <a href="https://www.cloudshark.org/captures/94b162026653">https://www.cloudshark.org/captures/94b162026653</a></p></div><div id="question-tags" class="tags-container tags">capture transfer.rate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '16, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/ff0a86a720311c5bec05905c6752c144?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crrimson&#39;s gravatar image" /><p>crrimson<br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crrimson has no accepted answers">0%</span></p></div></div><div id="comments-container-56957" class="comments-container"><span id="56962"></span><div id="comment-56962" class="comment"><div id="post-56962-score" class="comment-score">1</div><div class="comment-text"><p>About what webserver we are talking? Maybe this helps you a little bit. As I have seen some time gaps at cloudshark. But don´t have anymore time to analyze deeper at the moment. <a href="http://packetbomb.com/solving-tomcat-throughput-issues-on-windows/">http://packetbomb.com/solving-tomcat-throughput-issues-on-windows/</a></p></div><div id="comment-56962-info" class="comment-info"><span class="comment-age">(03 Nov '16, 23:31)</span> Christian_R</div></div><span id="56997"></span><div id="comment-56997" class="comment"><div id="post-56997-score" class="comment-score"></div><div class="comment-text"><p>This happens to be a Tomcat server haha. I love packetbomb, somewhat surprised I didn't find this link before! Thanks.</p><p>I also want to note that on a test server I was able to modify the socketBuffer variable in Tomcat config and noticed some performance differences... I'll watch that video, and reply back.</p></div><div id="comment-56997-info" class="comment-info"><span class="comment-age">(04 Nov '16, 13:35)</span> crrimson</div></div></div><div id="comment-tools-56957" class="comment-tools"></div><div class="clear"></div><div id="comment-56957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56999"></span>

<div id="answer-container-56999" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56999-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok. If we are talking about Tomcat, then this page can help you, too. <a href="http://javaagile.blogspot.de/search?q=tomcat">http://javaagile.blogspot.de/search?q=tomcat</a></p><p>I think you should try tune the TX-Buffers. Because when the server has send a segment with the PUSH Bit = 1 he waits for the ACK (a pause of about 200ms). More I can´t see, because the packets are truncated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '16, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '16, 14:13</p></div></div><div id="comments-container-56999" class="comments-container"><span id="57000"></span><div id="comment-57000" class="comment"><div id="post-57000-score" class="comment-score"></div><div class="comment-text"><p>My initial conclusion was that it was this value: socketBuffer. Still waiting on the server team to change &amp; re-test further.</p><p>Described here: <a href="https://tomcat.apache.org/tomcat-6.0-doc/config/http.html">https://tomcat.apache.org/tomcat-6.0-doc/config/http.html</a> "The size (in bytes) of the buffer to be provided for socket output buffering. -1 can be specified to disable the use of a buffer. By default, a buffers of 9000 bytes will be used."</p><p>I watched the video on Packetbomb, and it seems very similar, but we aren't even sending 64K before PSH, we are sending 9K..</p></div><div id="comment-57000-info" class="comment-info"><span class="comment-age">(04 Nov '16, 14:30)</span> crrimson</div></div><span id="57010"></span><div id="comment-57010" class="comment"><div id="post-57010-score" class="comment-score"></div><div class="comment-text"><p>Yes, that seems to be the limiting value.</p></div><div id="comment-57010-info" class="comment-info"><span class="comment-age">(05 Nov '16, 01:15)</span> Christian_R</div></div></div><div id="comment-tools-56999" class="comment-tools"></div><div class="clear"></div><div id="comment-56999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

