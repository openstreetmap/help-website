+++
type = "question"
title = "Why did this connection reset while downloading a file over HTTP?"
description = '''I host a couple of sites dealing with many file uploads/downloads. Every now and then I see failures in my log files, for reasons I only wish I knew. My visitors are mostly anonymous to me, but today I managed to capture one failed download with tcpdump and I&#x27;m asking for help understanding it bette...'''
date = "2014-01-04T18:45:00Z"
lastmod = "2014-01-07T00:02:00Z"
weight = 28580
keywords = [ "rst", "download", "http" ]
aliases = [ "/questions/28580" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why did this connection reset while downloading a file over HTTP?](/questions/28580/why-did-this-connection-reset-while-downloading-a-file-over-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28580-score" class="post-score" title="current number of votes">0</div><span id="post-28580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I host a couple of sites dealing with many file uploads/downloads. Every now and then I see failures in my log files, for reasons I only wish I knew. My visitors are mostly anonymous to me, but today I managed to capture one failed download with tcpdump and I'm asking for help understanding it better.</p><p>The client (67.189.6.55) was a modern version of Firefox, downloads list showed the files as "Failed".</p><p>The capture is available at <a href="http://www.cloudshark.org/captures/238c31c13426">http://www.cloudshark.org/captures/238c31c13426</a></p><p>What conclusions can be drawn from how the attached stream ends?</p><pre><code>No.     Time        Source         Destination   Protocol Length Info
  1 0.000000    67.189.6.55    148.251.25.18 TCP  66     62330 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
  2 0.000062    148.251.25.18  67.189.6.55   TCP  66     http &gt; 62330 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1460 SACK_PERM=1 WS=128
  3 0.234566    67.189.6.55    148.251.25.18 TCP  60     62330 &gt; http [ACK] Seq=1 Ack=1 Win=65700 Len=0
  4 0.251202    67.189.6.55    148.251.25.18 HTTP 612    GET /download?o=abee26401673422e8cc6b066aed9c1ba HTTP/1.1 
  5 0.251266    148.251.25.18  67.189.6.55   TCP  54     http &gt; 62330 [ACK] Seq=1 Ack=559 Win=15744 Len=0
  6 0.302918    148.251.25.18  67.189.6.55   TCP  1514   [TCP segment of a reassembled PDU]
 --8&lt;--
 16 0.499921    67.189.6.55    148.251.25.18 TCP  60     62330 &gt; http [ACK] Seq=559 Ack=11681 Win=64240 Len=0
 17 0.500034    148.251.25.18  67.189.6.55   TCP  1510   [TCP segment of a reassembled PDU]
 --8&lt;--
 24 0.505703    67.189.6.55    148.251.25.18 TCP  60     62330 &gt; http [ACK] Seq=559 Ack=14601 Win=61320 Len=0
 25 0.506461    148.251.25.18  67.189.6.55   TCP  1514   [TCP segment of a reassembled PDU]
 --8&lt;--
 30 0.511704    67.189.6.55    148.251.25.18 TCP  60     [TCP Window Update] 62330 &gt; http [ACK] Seq=559 Ack=14601 Win=65700 Len=0
 31 0.523490    67.189.6.55    148.251.25.18 TCP  60     62330 &gt; http [RST, ACK] Seq=559 Ack=14601 Win=0 Len=0</code></pre><p>In my Tomcat logs this manifests itself as</p><pre><code>Caused by: java.net.SocketException: Connection reset
    at java.net.SocketOutputStream.socketWrite(SocketOutputStream.java:118)
    at java.net.SocketOutputStream.write(SocketOutputStream.java:159)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '14, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/a5d0d78390a8712a0b8b6a8141a0184d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="llehtinen&#39;s gravatar image" /><p><span>llehtinen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="llehtinen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '14, 18:59</strong> </span></p></div></div><div id="comments-container-28580" class="comments-container"></div><div id="comment-tools-28580" class="comment-tools"></div><div class="clear"></div><div id="comment-28580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28596"></span>

<div id="answer-container-28596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28596-score" class="post-score" title="current number of votes">1</div><span id="post-28596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a client problem. For some reason it sends ACK packets only a couple of times, mostly packet 16 for packets up to packet 13, and then it gets strange - because in packet 24 it acknowledges packet 15, and does the same ACK again in packet 30. After that in packet 31 a Reset is sent. Clearly the client seems to be confused :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '14, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28596" class="comments-container"><span id="28609"></span><div id="comment-28609" class="comment"><div id="post-28609-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I noticed #15 with psh bit set, it should mean like "hey, 67. guy, please took off all of those bytes, give me an Ack, and i will give you next chunks of data". But #16 only acks #13 rather than 15, under such condition, is 148. allowed to send additional bytes? Is it a standard behavior? Maybe I mis-undertood the psh bit here.</p><p>Could you help me to understand psh bit more precisely?</p></div><div id="comment-28609-info" class="comment-info"><span class="comment-age">(06 Jan '14, 18:07)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="28610"></span><div id="comment-28610" class="comment"><div id="post-28610-score" class="comment-score"></div><div class="comment-text"><p>I referred to rfc1122 page 83, which states that the discussion in rfc-793 erroneously implies that a received PSH flag must be passed to the app layer. Passing a received PSH flag to the app layer is now OPTIONAL.</p></div><div id="comment-28610-info" class="comment-info"><span class="comment-age">(06 Jan '14, 18:42)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="28611"></span><div id="comment-28611" class="comment"><div id="post-28611-score" class="comment-score">1</div><div class="comment-text"><p>The PSH bit is a notification to process the segment immediately when sending and receiving it, which means that no "waiting for more segments" mechanism is allowed (well, let's say "waiting/buffering SHOULD not happen"). It does not mean that there may not be more data sent afterwards, it only means "process this right away".</p><p>A PSH bit also means that the data should be passed towards the application layer on the receiving side immediately (as you quoted), but it may not mean that the TCP stack has to acknowledge it right away. RFCs are one thing, reality is often something else :-)</p></div><div id="comment-28611-info" class="comment-info"><span class="comment-age">(07 Jan '14, 00:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-28596" class="comment-tools"></div><div class="clear"></div><div id="comment-28596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28581"></span>

<div id="answer-container-28581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28581-score" class="post-score" title="current number of votes">0</div><span id="post-28581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(Not sure if I was correct, just for your reference. Looking forward experts' input later)</p><p>Your web server was doing its job well on file transfer until the client reset the TCP connection. Nothing wrong on tcp side as I can see, it must be a purely application level issue. Live application debugging would be needed to figure out the reason of TCP reset.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '14, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '14, 03:29</strong> </span></p></div></div><div id="comments-container-28581" class="comments-container"><span id="28603"></span><div id="comment-28603" class="comment"><div id="post-28603-score" class="comment-score"></div><div class="comment-text"><p>I have to overturn my previous conclusion. This is definitely a server side problem! Apparently, this client is just one of the example to the issue log found on your server, isn't it? It cannot be every client was having problem.</p><p>I reviewed the trace again and found that #17's tcp length = 1456 which is bigger than the negotiated value 1460 during handshaking. And after that, #24 and #30 only acked #15 as Jasper mentioned. There must be some problem after receiving the weird length packet on the client, and this caused the client send out an reset to end the connection.</p><p>You should take a look at the web server to figure out why it would send out weird length tcp segment. Maybe a NIC card driver issue.</p></div><div id="comment-28603-info" class="comment-info"><span class="comment-age">(06 Jan '14, 08:23)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-28581" class="comment-tools"></div><div class="clear"></div><div id="comment-28581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

