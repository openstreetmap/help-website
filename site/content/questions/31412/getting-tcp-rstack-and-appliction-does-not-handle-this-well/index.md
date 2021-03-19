+++
type = "question"
title = "Getting TCP RST,ACK and appliction does not handle this well"
description = '''We have a kit we send for demos which is just a Windows 2008R2 server, 2 Windows 7 clients, and 2 Windows 7 embedded devices all with static IP addresses connected to each other via a dumb switch. The 2 embedded devices send data to the server via sockets with not problem. The server also hosts IIS....'''
date = "2014-04-02T10:39:00Z"
lastmod = "2014-04-03T01:30:00Z"
weight = 31412
keywords = [ "rst", "http", "packet", "wireshark" ]
aliases = [ "/questions/31412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting TCP RST,ACK and appliction does not handle this well](/questions/31412/getting-tcp-rstack-and-appliction-does-not-handle-this-well)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31412-score" class="post-score" title="current number of votes">0</div><span id="post-31412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a kit we send for demos which is just a Windows 2008R2 server, 2 Windows 7 clients, and 2 Windows 7 embedded devices all with static IP addresses connected to each other via a dumb switch. The 2 embedded devices send data to the server via sockets with not problem. The server also hosts IIS. I have a .Net application that uses Websync to stream data from the web server to the 2 clients. In this closed network I would see that the stream of data would pause for several seconds every once in a while. Using wireshark I found that at the time of the "pause" the client had sent a TCP [RST, ACK] which made the websync connection wait for its 15 second time out and then everything picked back up again. I have been trying to find an explanation as to why this RST is being sent at all. Sometimes it will go an hour with no reset while other times it will send one once a minute.</p><p>Here is a set of frames where there are 3 successful packets and one that fails with the RST. The interesting thing is that the last POST does not show in the IIS logs.</p><pre><code>5287    12:46:08.970006000  192.168.4.111   192.168.4.112   HTTP    605 POST /webservice/nlogreceiver.svc/binarylogger HTTP/1.1  (application/soap+msbin1)
5288    12:46:08.970397000  192.168.4.112   192.168.4.111   TCP 60  http &gt; 50460 [ACK] Seq=2664 Ack=4432 Win=64000 Len=0
5289    12:46:08.973167000  192.168.4.112   192.168.4.111   HTTP    558 HTTP/1.1 200 OK  (application/soap+msbin1)
5290    12:46:09.169231000  192.168.4.111   192.168.4.112   TCP 54  50460 &gt; http [ACK] Seq=4432 Ack=3168 Win=65536 Len=0
5291    12:46:09.472499000  192.168.4.111   192.168.4.112   TCP 242 [TCP segment of a reassembled PDU]
5292    12:46:09.472631000  192.168.4.111   192.168.4.112   HTTP    300 POST /websync.ashx?token=37043804&amp;src=dn&amp;AspxAutoDetectCookieSupport=1 HTTP/1.1  (application/json)
5293    12:46:09.472949000  192.168.4.112   192.168.4.111   TCP 60  http &gt; 50460 [ACK] Seq=3168 Ack=4866 Win=65536 Len=0
5294    12:46:09.474608000  192.168.4.112   192.168.4.111   HTTP    645 HTTP/1.1 200 OK  (application/json)
5295    12:46:09.475156000  192.168.4.111   192.168.4.112   TCP 66  50462 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
5296    12:46:09.475523000  192.168.4.112   192.168.4.111   TCP 66  http &gt; 50462 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
5297    12:46:09.475607000  192.168.4.111   192.168.4.112   TCP 54  50462 &gt; http [ACK] Seq=1 Ack=1 Win=65536 Len=0
5298    12:46:09.475730000  192.168.4.111   192.168.4.112   HTTP    270 GET /websync.ashx?token=37043804&amp;src=dn&amp;AspxAutoDetectCookieSupport=1 HTTP/1.1 
5299    12:46:09.476687000  192.168.4.112   192.168.4.111   HTTP    262 HTTP/1.1 200 OK  (text/html)
5300    12:46:09.483488000  192.168.4.111   192.168.4.112   TCP 242 [TCP segment of a reassembled PDU]
5301    12:46:09.483586000  192.168.4.111   192.168.4.112   HTTP    949 POST /websync.ashx?token=37043804&amp;src=dn&amp;AspxAutoDetectCookieSupport=1 HTTP/1.1  (application/json)
5302    12:46:09.483800000  192.168.4.112   192.168.4.111   TCP 60  http &gt; 50460 [ACK] Seq=3759 Ack=5949 Win=64512 Len=0
5303    12:46:09.485582000  192.168.4.112   192.168.4.111   HTTP    606 HTTP/1.1 200 OK  (application/json)
5304    12:46:09.685192000  192.168.4.111   192.168.4.112   TCP 54  50462 &gt; http [ACK] Seq=217 Ack=209 Win=65280 Len=0
5305    12:46:09.692156000  192.168.4.111   192.168.4.112   TCP 54  50460 &gt; http [ACK] Seq=5949 Ack=4311 Win=64512 Len=0
5306    12:46:09.757194000  192.168.4.111   192.168.4.112   TCP 54  50462 &gt; http [RST, ACK] Seq=217 Ack=209 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/6bea9ca562ce2c299b509b1c986ebc5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Blackadder&#39;s gravatar image" /><p><span>Blackadder</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Blackadder has no accepted answers">0%</span></p></div></div><div id="comments-container-31412" class="comments-container"><span id="31415"></span><div id="comment-31415" class="comment"><div id="post-31415-score" class="comment-score"></div><div class="comment-text"><p>can you post the capture at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>? Reading ASCII dumps is not going to work well, especially when tracking TCP stuff.</p></div><div id="comment-31415-info" class="comment-info"><span class="comment-age">(02 Apr '14, 11:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="31424"></span><div id="comment-31424" class="comment"><div id="post-31424-score" class="comment-score"></div><div class="comment-text"><p>Ok, I added a new capture here: <a href="https://www.cloudshark.org/captures/f5a062ccfdf6">https://www.cloudshark.org/captures/f5a062ccfdf6</a> It is a filtered capture to only include from either the client or server. Client is 104 and server is 90. There are 2 failures. Timestamp 19:14:11.2085 and 19:15:02:8997 This is when I get the stream failure log so the problem occurs some time before this I guess.</p></div><div id="comment-31424-info" class="comment-info"><span class="comment-age">(02 Apr '14, 12:44)</span> <span class="comment-user userinfo">Blackadder</span></div></div></div><div id="comment-tools-31412" class="comment-tools"></div><div class="clear"></div><div id="comment-31412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31460"></span>

<div id="answer-container-31460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31460-score" class="post-score" title="current number of votes">0</div><span id="post-31460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hint: the timestamps are not helping since they change depending on the time zone settings of the PC Wireshark is running on. It is usually better to specify packet numbers or TCP stream indexes because they're constant within a capture file.</p><p>So far I found a couple of Resets, but none that look problematic from a network point of view. It is quite common these days for IIS and some clients to terminate sessions via reset packet instead of FIN/ACK/FIN/ACK, since it is much faster and frees resources immediately.</p><p>In packets 2011 and 2496, the client finishes the connection with a reset after a GET request, receiving the answer and acknowledging it. This looks just like "okay, got it, thanks, bye!", and no foul play.</p><p>In packet 2641, it is a little different. For some reason the client waits for 110 seconds this time before sending the reset. Once again, no foul play from a packet point of view, but I guess the client may have encountered something that kept it from closing the connection right away. This conversation is not with the .90 though, but with .101. Maybe a wrong server IP, or just something that got into the capture by mistake?</p><p>All other resets are from the server and look pretty normal, too. They look like normal "oh, I guess this connection is not going to be reused again, I waited long enough, so let's close it" packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '14, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31460" class="comments-container"></div><div id="comment-tools-31460" class="comment-tools"></div><div class="clear"></div><div id="comment-31460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

