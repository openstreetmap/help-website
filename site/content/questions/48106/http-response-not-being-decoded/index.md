+++
type = "question"
title = "HTTP response not being decoded"
description = '''So....here&#x27;s a snippet of what I have: tshark -n -r _web-72.52.135.69-Mon-2015-11-30--19-36-02.pcapng  1 0.000000000 10.0.2.35 -&amp;gt; 72.52.135.69 TCP 66 61481â80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1  2 0.068716000 72.52.135.69 -&amp;gt; 10.0.2.35 TCP 66 80â61481 [SYN, ACK] Seq=0 Ack=1 Win=14...'''
date = "2015-11-30T13:19:00Z"
lastmod = "2015-11-30T14:46:00Z"
weight = 48106
keywords = [ "http" ]
aliases = [ "/questions/48106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP response not being decoded](/questions/48106/http-response-not-being-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So....here's a snippet of what I have:</p><pre><code>tshark -n -r _web-72.52.135.69-Mon-2015-11-30--19-36-02.pcapng
  1 0.000000000    10.0.2.35 -&gt; 72.52.135.69 TCP 66 61481â80 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 SACK_PERM=1
  2 0.068716000 72.52.135.69 -&gt; 10.0.2.35    TCP 66 80â61481 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1380 SACK_PERM=1
  3 0.068913000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 61481â80 [ACK] Seq=1 Ack=1 Win=65535 Len=0
  4 0.069064000    10.0.2.35 -&gt; 72.52.135.69 HTTP 606 GET / HTTP/1.1
  5 0.138513000 72.52.135.69 -&gt; 10.0.2.35    TCP 64 80â61481 [ACK] Seq=1 Ack=549 Win=15344 Len=0
  6 2.740825000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
  7 2.740868000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
  8 2.740878000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
  9 2.740893000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 10 2.740899000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 11 2.740903000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 12 2.740946000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 13 2.740950000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 61481â80 [ACK] Seq=549 Ack=2761 Win=63880 Len=0
 14 2.740952000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 61481â80 [ACK] Seq=549 Ack=5521 Win=61120 Len=0
 15 2.741087000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 61481â80 [ACK] Seq=549 Ack=8281 Win=63880 Len=0
 16 2.741091000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 [TCP ACKed unseen segment] 61481â80 [ACK] Seq=549 Ack=11041 Win=61120 Len=0
 17 2.741093000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 [TCP ACKed unseen segment] 61481â80 [ACK] Seq=549 Ack=13801 Win=58360 Len=0
 18 2.742424000    10.0.2.35 -&gt; 72.52.135.69 TCP 64 [TCP ACKed unseen segment] 61481â80 [FIN, ACK] Seq=549 Ack=13801 Win=65535 Len=0
 19 2.809661000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP Previous segment not captured] [TCP segment of a reassembled PDU]
 20 2.809680000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 21 2.809682000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 22 2.809710000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 23 2.809774000 72.52.135.69 -&gt; 10.0.2.35    TCP 1438 [TCP segment of a reassembled PDU]
 24 2.809789000 72.52.135.69 -&gt; 10.0.2.35    TCP 625 [TCP segment of a reassembled PDU]
 25 2.809792000 72.52.135.69 -&gt; 10.0.2.35    TCP 64 80â61481 [FIN, ACK] Seq=21268 Ack=549 Win=15344 Len=0</code></pre><p>tshark (version 1.12.6) doesn't seem to be able to see the HTTP response, which is in packet #6:</p><pre><code>HTTP/1.1 200 OK
Date: Mon, 30 Nov 2015 19:35:21 GMT
Server: Apache/2.4.16 (Unix) OpenSSL/1.0.1e-fips mod_bwlimited/1.4
X-Powered-By: PHP/5.4.45
Set-Cookie: _PHP_SESSION_PHP=351; expires=Mon, 07-Dec-2015 19:35:21 GMT; path=/
Vary: Accept-Encoding,User-Agent
Content-Encoding: gzip
Content-Length: 20911
Connection: close
Content-Type: text/html</code></pre><p>I see the same thing in Wireshark 2.0. Any clue on why this isn't been seen as HTTP? Thank you.</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/feeceb13b3a434a147fa2c173ad18db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngelXX&#39;s gravatar image" /><p>DigiAngelXX<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngelXX has no accepted answers">0%</span></p></div></div><div id="comments-container-48106" class="comments-container"></div><div id="comment-tools-48106" class="comment-tools"></div><div class="clear"></div><div id="comment-48106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48107"></span>

<div id="answer-container-48107" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is because you have enabled TCP reassembly.<br />
In Wireshark you can right click the TCP header in the Detail Pane and then disable TCP reassembly.<br />
<br />
<img src="https://osqa-ask.wireshark.org/upfiles/TCP_Reassembly2.png" alt="alt text" /><br />
<br />
Or you can Go to Edit -&gt; Preference -&gt; Protocol -&gt; TCP and disable the setting there.<br />
<br />
<img src="https://osqa-ask.wireshark.org/upfiles/TCP_Reassembly.png" alt="alt text" /></p><p>For Tshark: The easiest way is to prepare that things in Wireshark and remeber the profile name (right corner). And then start tshark with -C PROFILE_NAME like: <code>tshark -C PROFILE_NAME</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></img></div></div><div id="comments-container-48107" class="comments-container"><span id="48108"></span><div id="comment-48108" class="comment"><div id="post-48108-score" class="comment-score"></div><div class="comment-text"><p>That totally did the trick...thank you very much.</p></div><div id="comment-48108-info" class="comment-info"><span class="comment-age">(30 Nov '15, 14:50)</span> DigiAngelXX</div></div><span id="48110"></span><div id="comment-48110" class="comment"><div id="post-48110-score" class="comment-score"></div><div class="comment-text"><p>Hint:<br />
If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-48110-info" class="comment-info"><span class="comment-age">(30 Nov '15, 15:46)</span> Christian_R</div></div></div><div id="comment-tools-48107" class="comment-tools"></div><div class="clear"></div><div id="comment-48107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

