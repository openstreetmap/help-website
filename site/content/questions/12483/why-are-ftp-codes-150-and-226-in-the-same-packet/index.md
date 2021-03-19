+++
type = "question"
title = "Why are FTP codes 150 and 226 in the same packet?"
description = '''In Wireshark traces, I can find a packet which has both 150 and 226 FTP codes. The server is programmed to handle 150 and 226 codes in different packets: the former followed by latter. If both codes are found in a single packet, the server gets confused and skips the data transfer.  The packet flow ...'''
date = "2012-07-06T05:03:00Z"
lastmod = "2012-07-09T03:16:00Z"
weight = 12483
keywords = [ "ftp" ]
aliases = [ "/questions/12483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why are FTP codes 150 and 226 in the same packet?](/questions/12483/why-are-ftp-codes-150-and-226-in-the-same-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12483-score" class="post-score" title="current number of votes">0</div><span id="post-12483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark traces, I can find a packet which has both 150 and 226 FTP codes. The server is programmed to handle 150 and 226 codes in different packets: the former followed by latter. If both codes are found in a single packet, the server gets confused and skips the data transfer.</p><p>The packet flow is:</p><ol><li>Request: RETR</li><li>[TCP Retransmission] Request: RETR</li><li>[TCP previous segment lost]</li><li>[TCP Retransmission] Response: 150 ..... 226</li></ol><p>Is this expected behavior? If yes, under what scenario?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '12, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/ab531870998566c9b891f91ebc57714d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishal&#39;s gravatar image" /><p><span>vishal</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '12, 22:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12483" class="comments-container"></div><div id="comment-tools-12483" class="comment-tools"></div><div class="clear"></div><div id="comment-12483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12485"></span>

<div id="answer-container-12485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12485-score" class="post-score" title="current number of votes">1</div><span id="post-12485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Per RFC 959, "File Transfer Protocol (FTP)", 150 means "File status okay; about to open data connection" and 226 means "Closing data connection." There should be a data transfer in between these two commands, so it would certainly be unusual to have both commands in the same packet. Still, there is nothing in the RFC that forbids it, so I suppose both commands could appear in the same packet if the file being transferred is extremely small or the server for some reason decides to immediately close the data connection. The RFC does require each reply code to be on a separate line.</p><p>You say the server gets confused and skips the data transfer if both codes are found in a single packet. The server doesn't get confused by these codes; the server is the one sending these codes. The server is not skipping the data transfer because there's both a 150 and a 226 code in the same packet. Rather, there are both a 150 and a 226 code in the same packet because the server has skipped the data transfer.</p><p>Sounds like your server is misbehaving. The presence of both codes in the same packet is not the cause of the problem, it's a symptom of the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '12, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12485" class="comments-container"><span id="12521"></span><div id="comment-12521" class="comment"><div id="post-12521-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim.</p><p>Unfortunately I am new to using FTP at the command level, so I am having trouble understanding everything. So I would spell out all the details for you, as I believe that ways you will be able to help better:</p><p>an RETR command is being issued to retrieve data:</p><p>::::normal case as from Wireshark traces I have:::::</p><h1 id="client-server-request-retr-file-name">client-&gt;server Request: RETR &lt;file name=""&gt;</h1><h1 id="request-command-retr">Request Command: RETR</h1><h1 id="request-arg-file-name">Request Arg: &lt;"file name"&gt;</h1><p>.</p><h1 id="server-client-response-150-file-status-okay-about-to-open-data-connection-rn">server-&gt;client Response: 150 File status Okay; about to open data connection \r\n</h1><p>Response Code: File status Okay; about to open data connection(150) Repsonse Arg: File status Okay; about to open data connection .</p><h1 id="client-server-xxxxx-ftp-ack-seq..-ack..-win..-len..">client-&gt;server xxxxx &gt; ftp [ACK] Seq=.. Ack=.. Win=.. Len=..</h1><p>.</p><h1 id="server-client-response-226-closing-data-connection.-rn">server-&gt;client Response: 226 Closing data connection. \r\n</h1><p>Response Code: Closing data connection(226) Response Arg: Closing data connection . xxxxx is some random 5-digit number</p><p>:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</p><p>. .</p><p>::::::faulty scenario or precisely "unexpected" scenario:::::::::</p><h1 id="client-server-request-retr-file-name-1">client-&gt;server Request: RETR &lt;"file name"&gt;</h1><p>Request Command: RETR</p><p>Request Arg: &lt;"file name"&gt; .</p><h1 id="client-server-tcp-retransmission-request-retr-file-name">client-&gt;server [TCP Retransmission] Request: RETR &lt;"file name"&gt;</h1><p>Request Command: RETR</p><p>Request Arg: &lt;"file name"&gt; .</p><h1 id="server-client-tcp-previous-segment-lost-ftp-xxxxx-ack-seq..-ack..-win..-len..">server-&gt;client [TCP Previous Segment lost] ftp&gt; xxxxx [ACK] Seq=.. Ack=.. Win=.. Len=..</h1><p>.</p><h1 id="server-client-tcp-retransmission-response-150-opening-binary-mode-data-for-file-name-r-n">server-&gt;client [TCP Retransmission] Response: 150 Opening Binary mode data for &lt;"file name"&gt; \r \n</h1><p>Response Code: File status Okay; about to open data connection(150)</p><p>Response Arg: Opening BINARY Mode data connection for &lt;"file name"&gt;</p><p>226 Transfer Complete. \r\n .</p><h1 id="client-server-xxxxx---ftp-ack-seq..-ack..-win..-len..">client-&gt;server xxxxx -&gt; ftp [ACK] Seq=.. Ack=.. Win=.. Len=..</h1><p>::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::</p><p>Can you spot the the reason as to what is going on here in these two scenarios?</p><p>Thanks a million in adavnce.</p><p>Best Regards Vishal.</p></div><div id="comment-12521-info" class="comment-info"><span class="comment-age">(09 Jul '12, 02:14)</span> <span class="comment-user userinfo">vishal</span></div></div><span id="12523"></span><div id="comment-12523" class="comment"><div id="post-12523-score" class="comment-score"></div><div class="comment-text"><p>It would be far easier, if you upload a sample capture file. You can upload it to <a href="http://cloudshark.org">cloudshark.org</a>.</p><p>HINT: As you cannot delete an anonymously uploaded file on <a href="http://cloudshark.org">cloudshark.org</a>, you better don't post any private data. Post just those packets in a capture file, that are required to analyze the problem.</p></div><div id="comment-12523-info" class="comment-info"><span class="comment-age">(09 Jul '12, 03:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12485" class="comment-tools"></div><div class="clear"></div><div id="comment-12485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

