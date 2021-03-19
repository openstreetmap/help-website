+++
type = "question"
title = "Why chunked HTTP response is not decoded?"
description = '''I have captured opening of news web site main page with wireshark 2.0.1. pcap file download link GET request is parsed by wireshark but response is not. Wireshark shows the following output:  8 [TCP segment of a reassembled PDU]&quot; ... (many such lines) ...  28 [TCP Previous segment not captured] ... ...'''
date = "2016-01-12T07:48:00Z"
lastmod = "2016-01-13T04:34:00Z"
weight = 49128
keywords = [ "reassembly", "chunk", "chunked", "http", "data-chunk" ]
aliases = [ "/questions/49128" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why chunked HTTP response is not decoded?](/questions/49128/why-chunked-http-response-is-not-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49128-score" class="post-score" title="current number of votes">0</div><span id="post-49128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured opening of news web site main page with wireshark 2.0.1.</p><p><a href="http://vrepin.org/studies/Wireshark/test.pcap">pcap file download link</a></p><p>GET request is parsed by wireshark but response is not.</p><p>Wireshark shows the following output:</p><hr /><pre><code>8 [TCP segment of a reassembled PDU]&quot; ... (many such lines)
... 
28 [TCP Previous segment not captured] ...
29 [TCP ACKed unseen segment] ...</code></pre><hr /><p>Then "TCP segment of reassembled PDU" appears again and again (same pattern as above).</p><p>If I select "Follow TCP stream" wireshark decodes the conversation. E.g.:</p><hr /><pre><code>GET / HTTP/1.1
User-Agent: Wget/1.13.4 (linux-gnu)
Accept: */*
Host: newsru.com
Connection: Keep-Alive

HTTP/1.1 200 OK
Server: nginx
Date: Sun, 10 Jan 2016 07:22:44 GMT
Content-Type: text/html; charset=windows-1251
Transfer-Encoding: chunked
Connection: keep-alive
Keep-Alive: timeout=25
Expires: Sun, 10 Jan 2016 07:23:14 GMT
Cache-Control: max-age=30
Serv: ng5</code></pre><p>...</p><hr /><p>(Entire conversation is 163K)</p><p>I am under impression that the problem is in "Transfer-Encoding: chunked" ( no length is given, <a href="http://en.wikipedia.org/wiki/Chunked_transfer_encoding">chunks</a> are used)</p><p>Is it a bug in Wireshark or have I missed some settings to dissect chunked HTML? I've expected to see the settings which controls max length of the HTML payload being dissected but do not see any.</p><p>"Resemble chunked transfer-coded bodies" is set.</p><p>Thanks beforehand!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-chunk" rel="tag" title="see questions tagged &#39;chunk&#39;">chunk</span> <span class="post-tag tag-link-chunked" rel="tag" title="see questions tagged &#39;chunked&#39;">chunked</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-data-chunk" rel="tag" title="see questions tagged &#39;data-chunk&#39;">data-chunk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/b509691f5c44d60a88a7e52336b6d686?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vitaly%20R&#39;s gravatar image" /><p><span>Vitaly R</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vitaly R has no accepted answers">0%</span></p></div></div><div id="comments-container-49128" class="comments-container"></div><div id="comment-tools-49128" class="comment-tools"></div><div class="clear"></div><div id="comment-49128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49129"></span>

<div id="answer-container-49129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49129-score" class="post-score" title="current number of votes">2</div><span id="post-49129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Possibly because your capture is missing some frames from the server?</p><p>For example. see frames 27-29. Frame 27 sends data setting the expected tcp sequence no. to 20380, but frame 28 sends data with a sequence number 26172. There's 5792 bytes missing, likely to be 2 tcp segments given that some of the segments are transporting 2896 bytes of tcp data. Frame 29 shows the client acking sequence no. 29068, that is all data including frame 28, so the client has seen the data, but you didn't capture it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49129" class="comments-container"><span id="49135"></span><div id="comment-49135" class="comment"><div id="post-49135-score" class="comment-score"></div><div class="comment-text"><p>This looks strange. I have just repeated the experiment.</p><p>Now I've made measurements from different machine (and different country). And got similar results: <a href="http://vrepin.org/studies/Wireshark/tst1.pcap">see pcap file</a></p><p>The commands I have used to capture it:</p><pre><code>tshark -i eth0 -w tst1.pcap host newsru.com
wget http://www.newsru.com</code></pre><p>How can it be that the client have seen the data but wireshark has not?</p><p>I have also made a comparison of the index.html file I've got and the response which is shown in the "Follow TCP stream" window. I do see that size of the conversation captured by wireshark is bigger that what wget saved. And meld does not show missed parts.</p></div><div id="comment-49135-info" class="comment-info"><span class="comment-age">(12 Jan '16, 10:33)</span> <span class="comment-user userinfo">Vitaly R</span></div></div><span id="49138"></span><div id="comment-49138" class="comment"><div id="post-49138-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>How can it be that the client have seen the data but wireshark has not?</p></blockquote><p>The server response is (probably) not standard compliant. If you replace <strong>fc4</strong> with CRLFs, Wireshark is able to parse the response.</p><pre><code>Serv: ng5

fc4</code></pre><p>Regards<br />
Kurt</p></div><div id="comment-49138-info" class="comment-info"><span class="comment-age">(12 Jan '16, 10:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="49139"></span><div id="comment-49139" class="comment"><div id="post-49139-score" class="comment-score">1</div><div class="comment-text"><p>The second capture still seems to be missing packets, see frame 92 where it has a tcp sequence number of 56936, but the expected value was 55528. Another 1408 bytes of payload missing.</p><p>The client then acks subsequent frames, extending its window size to accommodate the new data until frame 113 where the client can no longer increase its window size.</p><p>Then in frame 200 the server sends the missing segment.</p><p>However things go wrong again in frame 230, the missing segment is sent in frame 272, and the server now resends a lot of the date it transmitted between 230 and 272. In frame 307 the client finally acks the highest sequence number seen and closes the connection.</p><p>See it seems that all the data is there, but due to the dropped and retransmitted frames Wireshark's tcp and\or http dechunking reassembly has got a bit confused.</p></div><div id="comment-49139-info" class="comment-info"><span class="comment-age">(12 Jan '16, 11:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49143"></span><div id="comment-49143" class="comment"><div id="post-49143-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>:<br />
<code>Possibly because your capture is missing some frames from the server?</code><br />
The capture summary shows the follwing stats:</p><pre><code>Interfaces
Interface:              br0
Dropped packets:        33 (3e+01 %)
Capture filter:         port 80
Link type:              Ethernet
Packet size limit:      262144 bytes</code></pre><p><strong>My side question is:</strong> What does this dropped packets statistic mean?<br />
Does it mean the amount of packets dropped only for the capture (So that we are just not able to see them but there have been reached the system),<br />
or mean the number of dropped packets at this interface (so the system hasn´t seen this packets, too)?</p></div><div id="comment-49143-info" class="comment-info"><span class="comment-age">(12 Jan '16, 12:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="49152"></span><div id="comment-49152" class="comment"><div id="post-49152-score" class="comment-score">1</div><div class="comment-text"><p>Seems that I found the answer to my side question: <a href="https://ask.wireshark.org/questions/2095/what-does-packets-dropped-really-mean">https://ask.wireshark.org/questions/2095/what-does-packets-dropped-really-mean</a></p><p>So if understand it right, this could be the explanation for the missing frames in the tracefile.</p></div><div id="comment-49152-info" class="comment-info"><span class="comment-age">(12 Jan '16, 15:11)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="49163"></span><div id="comment-49163" class="comment not_top_scorer"><div id="post-49163-score" class="comment-score"></div><div class="comment-text"><p>Yep. It looks like the root of the problem is in dissectors/packet-tcp.c:</p><p><strong>desegment_tcp</strong> function:</p><pre><code>msp = (struct tcp_multisegment_pdu*)wmem_tree_lookup32_le(tcpd-&gt;fwd-&gt;multisegment_pdus, seq-1);

...

if (msp &amp;&amp; msp-&gt;seq &lt;= seq &amp;&amp; msp-&gt;nxtpdu &gt; seq) {
/* Continue to defragment the packet */
...
} else {
  /* This segment was not found in our table, so it doesn&#39;t
  * contain a continuation of a higher-level PDU.
  * Call the normal subdissector.
 */
}</code></pre><p>When one of the packets is not coming in a proper time, wireshark finds msp structure but it fails the test msp-&gt;nxtpdu &gt; seq. As a result, new dissection starts for the newly arrived packet and hence the whole logic breaks. The missed packet comes later but it is too late to process it.</p><p>Failed part:</p><pre><code>desegment_tcp: 3, msp = 0x7f7701617ea0
desegment_tcp: msp-&gt;seq: 1, seq: 56936, msp-&gt;nxtpdu: 55529</code></pre></div><div id="comment-49163-info" class="comment-info"><span class="comment-age">(13 Jan '16, 04:34)</span> <span class="comment-user userinfo">Vitaly R</span></div></div></div><div id="comment-tools-49129" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-49129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

