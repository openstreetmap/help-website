+++
type = "question"
title = "TCP Window Updates"
description = '''Hi, I have a case example of a connection that I thought would be a great way to start learning Wireshark. However I have a number of questions. First of the issue is when trying to download an image from a webserver it takes an extremely long time. This connection is however going through an F5. If...'''
date = "2012-11-19T01:14:00Z"
lastmod = "2012-12-04T01:01:00Z"
weight = 16039
keywords = [ "tcp" ]
aliases = [ "/questions/16039" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window Updates](/questions/16039/tcp-window-updates)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16039-score" class="post-score" title="current number of votes">0</div><span id="post-16039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a case example of a connection that I thought would be a great way to start learning Wireshark. However I have a number of questions.</p><p>First of the issue is when trying to download an image from a webserver it takes an extremely long time. This connection is however going through an F5. If : <em>I download the image directly from the server it is fine.</em> If I download the image via a VIP it takes a long time.</p><p>Now on digging about I found that the issue was because one of the ports was at half duplex. This was changed and everything was fine. But for the sake of learning I thought Id look into why one connection was fine and one was not.</p><p>I have an output of the connection that was failing.</p><pre><code>16:54:21.430108 IP 172.16.1.100.51825 &gt; 8.8.8.8.http: P 1607486190:1607486783(593) ack 220110437 win 257 &lt;--- The HTTP GET. Though this appears in the wrong sequence.
16:54:21.431053 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . ack 593 win 2053
16:54:21.434377 IP 172.16.1.100.51837 &gt; 8.8.8.8.http: S 2012441610:2012441610(0) win 8192 &lt;mss 1260,nop,wscale 8,nop,nop,sackOK&gt;
16:54:21.435982 IP 8.8.8.8.http &gt; 172.16.1.100.51837: S 1139646199:1139646199(0) ack 2012441611 win 5840 &lt;mss 1460,nop,nop,sackOK,nop,wscale 2&gt;
16:54:21.436069 IP 172.16.1.100.51837 &gt; 8.8.8.8.http: . ack 1 win 260 --&gt; Long delay until the next packet (?)
16:54:29.609962 IP 8.8.8.8.http &gt; 172.16.1.100.51825: P 1:359(358) ack 593 win 2053
16:54:29.610271 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 359:1619(1260) ack 593 win 2053
16:54:29.610306 IP 172.16.1.100.51825 &gt; 8.8.8.8.http: . ack 1619 win 260 &lt;-- Is this a Window Update
16:54:29.610339 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 1619:2879(1260) ack 593 win 2053
16:54:29.611179 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 2879:4139(1260) ack 593 win 2053
16:54:29.611200 IP 172.16.1.100.51825 &gt; 8.8.8.8.http: . ack 4139 win 260
16:54:29.611224 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 4139:5399(1260) ack 593 win 2053
16:54:29.611238 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 5399:6659(1260) ack 593 win 2053
16:54:29.611253 IP 172.16.1.100.51825 &gt; 8.8.8.8.http: . ack 6659 win 260
16:54:29.612069 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 6659:7919(1260) ack 593 win 2053
16:54:29.612088 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 7919:9179(1260) ack 593 win 2053
16:54:29.612105 IP 172.16.1.100.51825 &gt; 8.8.8.8.http: . ack 9179 win 260
16:54:29.612130 IP 8.8.8.8.http &gt; 172.16.1.100.51825: . 9179:10439(1260) ack 593 win 2053</code></pre><p>Based on the above I have 3 questions (based on the above) :</p><p>1) What would cause the HTTP get to be shown in the wrong position/sequence (poss corrupt seq number ?)</p><p>2) Though Im seeing a huge difference in time stamps, there appears to be not retransmissions or duplicate ACKs showing any sign of packet loss ?</p><p>3) Finally is this actually a window update. The amount of traffic being sent compared to the window size doesn't seem to correlate ?</p><p>If anyone can shed any light of this it would be greatly appreciated.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p><span>bart80</span><br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '12, 01:15</strong> </span></p></div></div><div id="comments-container-16039" class="comments-container"><span id="16053"></span><div id="comment-16053" class="comment"><div id="post-16053-score" class="comment-score"></div><div class="comment-text"><p>ASCII dumps of traces are pretty hard to read, so if you can, upload the file/excerpt to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the link.</p></div><div id="comment-16053-info" class="comment-info"><span class="comment-age">(19 Nov '12, 08:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="16055"></span><div id="comment-16055" class="comment"><div id="post-16055-score" class="comment-score"></div><div class="comment-text"><p>Yep I appreciate that. The problem I have is that the captures are from a customer so I have to do a find and replace on the IP`s. Which wouldnt be so easy within a capture. Are there no pointers you can provide based on just the above ??</p></div><div id="comment-16055-info" class="comment-info"><span class="comment-age">(19 Nov '12, 08:36)</span> <span class="comment-user userinfo">bart80</span></div></div></div><div id="comment-tools-16039" class="comment-tools"></div><div class="clear"></div><div id="comment-16039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16105"></span>

<div id="answer-container-16105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16105-score" class="post-score" title="current number of votes">0</div><span id="post-16105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi bart80,</p><p>First, it looks like you're showing two different conversations:</p><pre><code>172.16.1.100.51825 &gt; 8.8.8.8.http
172.16.1.100.51837 &gt; 8.8.8.8.http</code></pre><p>172.16.1.100 (or a node in the path) seem to be limiting it's TCP MSS to 1260 bytes.</p><pre><code>1) What would cause the HTTP get to be shown in the wrong position/sequence (poss corrupt seq number ?)</code></pre><p>Are you using both relative and absolute sequence numbers?</p><pre><code>&quot;Long delay until the next packet (?)</code></pre><p>Line 5 and 6 are two different conversations, so the 8 second delay is not path delay for instance.</p><pre><code>2) Though Im seeing a huge difference in time stamps, there appears to be not retransmissions or duplicate ACKs showing any sign of packet loss ?</code></pre><p>Doesn't look like it.</p><pre><code>3) Finally is this actually a window update. The amount of traffic being sent compared to the window size doesn&#39;t seem to correlate ?</code></pre><p>Yes the receiver window is oddly small.. Are the window sizes showing as calculated (since you seem to support window scaling)?</p><p>For simpler analysis, open the packet capture in Wireshark, right click on a conversation of interest and select "Follow TCP Stream" or something, save that file, run it through a pcap-anonymizer and upload it to Cloudshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/c23b8846cec43a35da426aa0657605a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="holmahenkel&#39;s gravatar image" /><p><span>holmahenkel</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="holmahenkel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '12, 04:11</strong> </span></p></div></div><div id="comments-container-16105" class="comments-container"><span id="16109"></span><div id="comment-16109" class="comment"><div id="post-16109-score" class="comment-score"></div><div class="comment-text"><p>Thanks, for your updates. I`ll look over these points and try to get a file up to cloud shark. One point I wanted to ask, is that I checked the calculated window size. For the ACK it shows win=260 with 260 also for the calculated side. But for each TCP segment (data) is shows a Window size of 2053. Is the Window showing in the packet for the receive window for the source it is coming from. The reason I ask is that 2 1260 byte (tcp.len) packets are sent from the server even though the window is 2053 ?</p><p>Thanks again...</p></div><div id="comment-16109-info" class="comment-info"><span class="comment-age">(20 Nov '12, 04:47)</span> <span class="comment-user userinfo">bart80</span></div></div><span id="16115"></span><div id="comment-16115" class="comment"><div id="post-16115-score" class="comment-score"></div><div class="comment-text"><p>Ah, yes a window size is advertised in both directions, so if 172.16.1.100 (sender) where to send data to 8.8.8.8 (receiver) it would know that 8.8.8.8's advertised window (rwnd) is 2053 bytes. In your example 8.8.8.8 is sending data to 172.16.1.100, so 8.8.8.8 only worries about 172.16.1.100's advertised window of 260[*] bytes. Hopes this makes sense :-D</p><ul><li><ul><li>Yes, a strange value. I thought 8.8.8.8 should wait for a Window Update.. Sure the packet capture is 100%?</li></ul></li></ul><p><a href="http://tools.ietf.org/html/rfc793#page-4">http://tools.ietf.org/html/rfc793#page-4</a> - "Flow Control" have some more information regarding windows.</p></div><div id="comment-16115-info" class="comment-info"><span class="comment-age">(20 Nov '12, 06:28)</span> <span class="comment-user userinfo">holmahenkel</span></div></div><span id="16523"></span><div id="comment-16523" class="comment"><div id="post-16523-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response but using the following example -- 172.16.1.100.51825 &gt; 8.8.8.8.http: . ack 4139 win 260<br />
-- From my understanding this is 172.16.1.00 telling 8.8.8.8 that the rwin size is 260. So 8.8.8.8 can only send upto 260 bytes of data before waiting for an ACK ?</p></div><div id="comment-16523-info" class="comment-info"><span class="comment-age">(04 Dec '12, 01:01)</span> <span class="comment-user userinfo">bart80</span></div></div></div><div id="comment-tools-16105" class="comment-tools"></div><div class="clear"></div><div id="comment-16105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

