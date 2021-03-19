+++
type = "question"
title = "Low throughput when retrieving data from remote server"
description = ''' Dear all, I need help in deciphering the packet capture from one of our customer&#x27;s local server(10.135.146.30). The issue is it is getting low throughput to retrieve data from remote server. From what I see, remote end is sending 2 packets,a full sized and a small packet with PUSH bit set. Also, I ...'''
date = "2014-08-28T10:40:00Z"
lastmod = "2014-08-28T15:08:00Z"
weight = 35845
keywords = [ "throughput" ]
aliases = [ "/questions/35845" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Low throughput when retrieving data from remote server](/questions/35845/low-throughput-when-retrieving-data-from-remote-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35845-score" class="post-score" title="current number of votes">0</div><span id="post-35845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture-Wireshark.png" alt="alt text" /></p><p>Dear all,</p><p>I need help in deciphering the packet capture from one of our customer's local server(10.135.146.30). The issue is it is getting low throughput to retrieve data from remote server. From what I see, remote end is sending 2 packets,a full sized and a small packet with PUSH bit set. Also, I noticed that the server is send 2 ACK packets, one ACK only and one with ACK+PUSH. Base on the capture:</p><ol><li>Once remote end sends packet with PSH set, it will wait for "instruction" from local server.</li><li>Between Last ACK from local server, delay is 300ms.</li><li>Local server is not piggybacking ACK. Sends separate packet for data, may indicate no delayed ACK enabled.</li></ol><p>Is my observation correct?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '14, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/9ed29d5e40ef2d0d4ef9deed4d374831?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sam_01&#39;s gravatar image" /><p><span>sam_01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sam_01 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '14, 10:43</strong> </span></p></div></div><div id="comments-container-35845" class="comments-container"></div><div id="comment-tools-35845" class="comment-tools"></div><div class="clear"></div><div id="comment-35845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35852"></span>

<div id="answer-container-35852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35852-score" class="post-score" title="current number of votes">0</div><span id="post-35852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think on this occasion you can largely ignore the TCP ACKs etc. You have a client process that sends a 16 byte Request APDU to a service ( on TCP port 4100). After about 300 ms you see the Response APDU split across two packets. If this trace was was captured adjacent to the service then the Service Time is 300 ms. If it was captured adjacent to the client you'll need to know the network Round Trip Time (RTT) to determine if it's a Service Time issue.</p><p>You could get a better insight using TRANSUM ( <a href="http://www.tribelabzero.com/resources">http://www.tribelabzero.com/resources</a> ). If you don't fancy that you may still want to read the RTE Model section of the TRANSUM manual.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '14, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35852" class="comments-container"></div><div id="comment-tools-35852" class="comment-tools"></div><div class="clear"></div><div id="comment-35852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

