+++
type = "question"
title = "discrepancy between async and sync in wireshark"
description = '''Hi Team, Do we can decide that a transaction is using async / sync by wireshark ? which the button / tools in wireshark we can see sync / async ? Thanks Wilis'''
date = "2013-07-15T19:17:00Z"
lastmod = "2013-07-16T02:31:00Z"
weight = 22985
keywords = [ "and", "async", "sync", "discrepancy", "between" ]
aliases = [ "/questions/22985" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [discrepancy between async and sync in wireshark](/questions/22985/discrepancy-between-async-and-sync-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22985-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team,</p><p>Do we can decide that a transaction is using async / sync by wireshark ? which the button / tools in wireshark we can see sync / async ?</p><p>Thanks Wilis</p></div><div id="question-tags" class="tags-container tags">and async sync discrepancy between</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 19:17</strong></p><img src="https://secure.gravatar.com/avatar/e753e69aad69de483a84efb1e6b9a4ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wilis&#39;s gravatar image" /><p>Wilis<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wilis has no accepted answers">0%</span></p></div></div><div id="comments-container-22985" class="comments-container"><span id="22986"></span><div id="comment-22986" class="comment"><div id="post-22986-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "synchronous" and "asynchronous" here?</p></div><div id="comment-22986-info" class="comment-info"><span class="comment-age">(15 Jul '13, 20:24)</span> Guy Harris ♦♦</div></div><span id="22987"></span><div id="comment-22987" class="comment"><div id="post-22987-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris,</p><p>Sync is the second transaction will be sent once the first transaction finished. Async is will be sent transaction regardless the first transaction finished.</p><p>Thanks Wilis</p></div><div id="comment-22987-info" class="comment-info"><span class="comment-age">(15 Jul '13, 20:33)</span> Wilis</div></div></div><div id="comment-tools-22985" class="comment-tools"></div><div class="clear"></div><div id="comment-22985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22989"></span>

<div id="answer-container-22989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22989-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so if there is only <em>ONE</em> client thread involved with a client &lt;-&gt; server endpoint pair (i.e., on any given client machine, you don't have multiple client processes or threads sending transactions to a given server between the same endpoints), then you can <em>manually</em> determine whether the client thread is running synchronously or asynchronously by looking at the traces; there are no built-in tools in Wireshark where you can just "push a button" and get the answer. You might be able to write, for example, a Lua script for your particular protocol that could do that; figuring out how to do that is up to you.</p><p>If there's more than one client thread using the endpoint pair, each <em>thread</em> might be acting synchronously, but the client as a whole might act asynchronously, with thread 1 sending a transaction and thread 2 sending another transaction before the reply from transaction 1 is sent back. Unless there's some way to identify which <em>thread</em> sent or received a particular packet, you can't distinguish between threads acting asynchronously and multiple synchronous threads just by looking at a network trace.</p><p>If Wireshark is not running on the client machine, then, unless the protocol has some field in it that lets you identify which thread sent a request or to which thread a reply is being sent, there's no way to determine which thread sent or received a particular packet.</p><p>Even if it <em>is</em> running on the client machine, Wireshark doesn't currently provide a way to associate packets with processes (other than the very limited mechanism supported by OS X Mountain Lion's tcpdump, but not supported by Wireshark, which only associates process names with some outgoing packets by attaching pcap-ng comments to them), and, even if it did, that wouldn't let you identify particular threads within a process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 21:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22989" class="comments-container"></div><div id="comment-tools-22989" class="comment-tools"></div><div class="clear"></div><div id="comment-22989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22993"></span>

<div id="answer-container-22993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22993-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume this question is a follow-up to your other question: <a href="http://ask.wireshark.org/questions/22843/discrepancy-between-psh-and-without-psh">http://ask.wireshark.org/questions/22843/discrepancy-between-psh-and-without-psh</a></p><p>You already asked for a way to detect sync/async requests in Wireshark.</p><blockquote><p>Cite: So we need to increase the performance of our customers/ client servers. Can we know whether the client is using synchronous method or asynchronous method by wireshark ?</p></blockquote><p>As your communication is HTTP the requests can be asynchronous or synchronous <strong>only within the logic of your software</strong>, as there is no such concept in the HTTP protocol.</p><p>The communication of your client uses one TCP connection to send several HTTP/1.1 GET requests (at least according the the information you provided <a href="http://ask.wireshark.org/questions/22843/discrepancy-between-psh-and-without-psh">in your other question</a>).</p><p>As per definition of HTTP the client must wait for the answer before it is allowed to send another request (unless you use <a href="https://en.wikipedia.org/wiki/HTTP_pipelining">HTTP/1.1 pipelining</a>).</p><p>The structure of your communication could be called <strong>serial/sequential</strong> (request, response, request, response, etc.). If you want to speed up the communication you need some form of <strong>parallel</strong> communication, meaning the client must open several parallel TCP connections and send different requests through these TCP connections. If the <strong>order of the client requests is not important</strong>, you don't have to <strong>synchronize</strong> these requests within the application and <strong>then</strong> we are talking about something that could by called <strong>asynchronous</strong> communication within your application.</p><p>Maybe parallel communication will solve the problem you faced in <a href="http://ask.wireshark.org/questions/22843/discrepancy-between-psh-and-without-psh">the other question</a>. However, please see also my analysis in that question for the (real) cause of the performance problems. I think it would be easier to analyze the problem of delayed response within the server, instead of re-writing the client to use parallel communication.</p><blockquote><p>Do we can decide that a transaction is using async / sync by wireshark ? which the button / tools in wireshark we can see sync / async ?</p></blockquote><p><strong>UPDATE</strong></p><p>As @Guy Harris already said: There is no one-click solution in Wireshark to detect 'asynchronous' (I'd say parallel) communication in your scenario. However, you can figure out pretty easily if a client opens several parallel connections to a server by running the following command on the capture file.</p><blockquote><p><code>tshark -nr input.pcap -R "http.request and ip.addr eq x.x.x.x and ip.addr eq y.y.y.y" -T fields -e tcp.stream</code><br />
</p></blockquote><p>Please replace:</p><ul><li>x.x.x.x with the client IP address</li><li>y.y.y.y with the server IP address</li></ul><p>Then look at the tcp.stream numbers (output of tshark). Is there only one number, do the numbers increase constantly or are the numbers intermixed?</p><ul><li>only one number: the client opened only one connection to the server</li><li>numbers increase: the client opened one connection after the other (serial/sequential communication)</li><li>intermixed numbers: the client opened several connections to the server in parallel</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '13, 05:38</p></div></div><div id="comments-container-22993" class="comments-container"><span id="23060"></span><div id="comment-23060" class="comment"><div id="post-23060-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your explanation, we will try your suggestion later. In the other hand, here are the results of snoop from client A and client B :</p><p>Client A :</p><pre><code>No.,&quot;Time&quot;,&quot;Source&quot;,&quot;Destination&quot;,&quot;Protocol&quot;,&quot;Length&quot;,&quot;Info&quot;
1,&quot;0.000000&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;66&quot;,&quot;64484 &gt; http [SYN] Seq=0 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1&quot;
2,&quot;0.000957&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;66&quot;,&quot;http &gt; 64484 [SYN, ACK] Seq=0 Ack=1 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1&quot;
3,&quot;0.001024&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [ACK] Seq=1 Ack=1 Win=49640 Len=0&quot;
4,&quot;0.001492&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;HTTP&quot;,&quot;407&quot;,&quot;GET /notification?ST.MSISDN=6285350245505&amp;ST.IMSI=510105052245505&amp;ST.IMEI=35325904007861&amp;ST.MSCID=12080012042618010686&amp;ST.VENDOR=Samsung&amp;ST.MODEL=I5500 HTTP/1.1 &quot;
5,&quot;0.002502&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64484 [ACK] Seq=1 Ack=354 Win=49640 Len=0&quot;
6,&quot;0.002641&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;408&quot;,&quot;[TCP segment of a reassembled PDU]&quot;
7,&quot;0.002684&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [ACK] Seq=354 Ack=355 Win=49640 Len=0&quot;
8,&quot;0.002878&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [FIN, ACK] Seq=354 Ack=355 Win=49640 Len=0&quot;
9,&quot;0.003148&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;HTTP&quot;,&quot;408&quot;,&quot;GET /notification/?ST.MSISDN=6285350245505&amp;ST.IMSI=510105052245505&amp;ST.IMEI=35325904007861&amp;ST.MSCID=12080012042618010686&amp;ST.VENDOR=Samsung&amp;ST.MODEL=I5500 HTTP/1.1 &quot;
10,&quot;0.003653&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;HTTP&quot;,&quot;238&quot;,&quot;HTTP/1.1 301 Moved Permanently  (text/html)&quot;
11,&quot;0.003692&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [RST] Seq=355 Win=49640 Len=0&quot;
12,&quot;0.003715&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64484 [ACK] Seq=539 Ack=355 Win=49640 Len=0&quot;
13,&quot;0.003764&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64484 [FIN, ACK] Seq=539 Ack=355 Win=49640 Len=0&quot;
14,&quot;0.003777&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [RST] Seq=355 Win=0 Len=0&quot;
15,&quot;0.003826&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64484 &gt; http [RST] Seq=355 Win=0 Len=0&quot;
16,&quot;0.004355&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;HTTP&quot;,&quot;267&quot;,&quot;HTTP/1.1 200 OK &quot;
17,&quot;0.007685&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;66&quot;,&quot;64485 &gt; http [SYN] Seq=0 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1&quot;
18,&quot;0.008641&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;66&quot;,&quot;http &gt; 64485 [SYN, ACK] Seq=0 Ack=1 Win=49640 Len=0 MSS=1460 WS=1 SACK_PERM=1&quot;
19,&quot;0.008700&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64485 &gt; http [ACK] Seq=1 Ack=1 Win=49640 Len=0&quot;
20,&quot;0.009090&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;HTTP&quot;,&quot;403&quot;,&quot;GET /notification?ST.MSISDN=6281382305449&amp;ST.IMSI=510108233303691&amp;ST.IMEI=35464205721261&amp;ST.MSCID=12080012042618010743&amp;ST.VENDOR=Nokia&amp;ST.MODEL=100 HTTP/1.1 &quot;
21,&quot;0.009993&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64485 [ACK] Seq=1 Ack=350 Win=49640 Len=0&quot;
22,&quot;0.010160&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;404&quot;,&quot;[TCP segment of a reassembled PDU]&quot;
23,&quot;0.010201&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64485 &gt; http [ACK] Seq=350 Ack=351 Win=49640 Len=0&quot;
24,&quot;0.010381&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64485 &gt; http [FIN, ACK] Seq=350 Ack=351 Win=49640 Len=0&quot;
25,&quot;0.010624&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;HTTP&quot;,&quot;404&quot;,&quot;GET /notification/?ST.MSISDN=6281382305449&amp;ST.IMSI=510108233303691&amp;ST.IMEI=35464205721261&amp;ST.MSCID=12080012042618010743&amp;ST.VENDOR=Nokia&amp;ST.MODEL=100 HTTP/1.1 &quot;
26,&quot;0.011176&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;HTTP&quot;,&quot;238&quot;,&quot;HTTP/1.1 301 Moved Permanently  (text/html)&quot;
27,&quot;0.011217&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64485 &gt; http [RST] Seq=351 Win=49640 Len=0&quot;
28,&quot;0.011231&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64485 [ACK] Seq=535 Ack=351 Win=49640 Len=0&quot;
29,&quot;0.011271&quot;,&quot;10.251.151.32&quot;,&quot;10.2.230.48&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;64485 &gt; http [RST] Seq=351 Win=0 Len=0&quot;
30,&quot;0.011288&quot;,&quot;10.2.230.48&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;http &gt; 64485 [FIN, ACK] Seq=535 Ack=351 Win=49640 Len=0&quot;</code></pre><p>CLIENT B :</p><pre><code>No.,&quot;Time&quot;,&quot;Source&quot;,&quot;Destination&quot;,&quot;Protocol&quot;,&quot;Length&quot;,&quot;Info&quot;
1,&quot;0.000000&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;389&quot;,&quot;46923 &gt; irdmi [PSH, ACK] Seq=1 Ack=1 Win=49640 Len=335&quot;
2,&quot;0.001783&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46923 [ACK] Seq=1 Ack=336 Win=33 Len=0&quot;
3,&quot;0.011218&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46913 [PSH, ACK] Seq=1 Ack=1 Win=33 Len=76&quot;
4,&quot;0.012526&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;396&quot;,&quot;46913 &gt; irdmi [PSH, ACK] Seq=1 Ack=77 Win=49640 Len=342&quot;
5,&quot;0.014387&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46913 [ACK] Seq=77 Ack=343 Win=33 Len=0&quot;
6,&quot;0.185122&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46912 [PSH, ACK] Seq=1 Ack=1 Win=65 Len=76&quot;
7,&quot;0.186193&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;399&quot;,&quot;46912 &gt; irdmi [PSH, ACK] Seq=1 Ack=77 Win=49640 Len=345&quot;
8,&quot;0.187918&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46912 [ACK] Seq=77 Ack=346 Win=65 Len=0&quot;
9,&quot;0.239474&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46913 [PSH, ACK] Seq=77 Ack=343 Win=33 Len=76&quot;
10,&quot;0.240768&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;398&quot;,&quot;46913 &gt; irdmi [PSH, ACK] Seq=343 Ack=153 Win=49640 Len=344&quot;
11,&quot;0.242604&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46913 [ACK] Seq=153 Ack=687 Win=33 Len=0&quot;
12,&quot;0.259261&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46923 [PSH, ACK] Seq=1 Ack=336 Win=33 Len=76&quot;
13,&quot;0.260272&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;398&quot;,&quot;46923 &gt; irdmi [PSH, ACK] Seq=336 Ack=77 Win=49640 Len=344&quot;
14,&quot;0.262112&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46923 [ACK] Seq=77 Ack=680 Win=33 Len=0&quot;
15,&quot;0.409021&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46912 [PSH, ACK] Seq=77 Ack=346 Win=65 Len=76&quot;
16,&quot;0.410261&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;398&quot;,&quot;46912 &gt; irdmi [PSH, ACK] Seq=346 Ack=153 Win=49640 Len=344&quot;
17,&quot;0.411954&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46912 [ACK] Seq=153 Ack=690 Win=65 Len=0&quot;
18,&quot;0.471328&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46913 [PSH, ACK] Seq=153 Ack=687 Win=33 Len=76&quot;
19,&quot;0.472568&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;402&quot;,&quot;46913 &gt; irdmi [PSH, ACK] Seq=687 Ack=229 Win=49640 Len=348&quot;
20,&quot;0.474414&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46913 [ACK] Seq=229 Ack=1035 Win=33 Len=0&quot;
21,&quot;0.617176&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46912 [PSH, ACK] Seq=153 Ack=690 Win=65 Len=76&quot;
22,&quot;0.618329&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;407&quot;,&quot;46912 &gt; irdmi [PSH, ACK] Seq=690 Ack=229 Win=49640 Len=353&quot;
23,&quot;0.620088&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46912 [ACK] Seq=229 Ack=1043 Win=65 Len=0&quot;
24,&quot;0.631317&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46913 [PSH, ACK] Seq=229 Ack=1035 Win=33 Len=76&quot;
25,&quot;0.739216&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;130&quot;,&quot;irdmi &gt; 46923 [PSH, ACK] Seq=77 Ack=680 Win=33 Len=76&quot;
26,&quot;0.740527&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;399&quot;,&quot;46923 &gt; irdmi [PSH, ACK] Seq=680 Ack=153 Win=49640 Len=345&quot;
27,&quot;0.742451&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46923 [ACK] Seq=153 Ack=1025 Win=33 Len=0&quot;
28,&quot;0.744909&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;46913 &gt; irdmi [ACK] Seq=1035 Ack=305 Win=49640 Len=0&quot;
29,&quot;0.817865&quot;,&quot;10.251.151.32&quot;,&quot;10.251.228.15&quot;,&quot;TCP&quot;,&quot;398&quot;,&quot;46913 &gt; irdmi [PSH, ACK] Seq=1035 Ack=305 Win=49640 Len=344&quot;
30,&quot;0.819795&quot;,&quot;10.251.228.15&quot;,&quot;10.251.151.32&quot;,&quot;TCP&quot;,&quot;60&quot;,&quot;irdmi &gt; 46913 [ACK] Seq=305 Ack=1379 Win=33 Len=0&quot;</code></pre><p>As i know that client A is using Async, and client B is using Sync. Client A using Async because i see that the structure of transaction is not irregullar. Client B using Sync becuse i see that the structure of transaction is regullar.</p><p>Correct me if i am wrong.</p><p>Thanks Wilis</p></div><div id="comment-23060-info" class="comment-info"><span class="comment-age">(16 Jul '13, 20:08)</span> Wilis</div></div><span id="23061"></span><div id="comment-23061" class="comment"><div id="post-23061-score" class="comment-score"></div><div class="comment-text"><blockquote><p>As i know that client A is using Async, and client B is using Sync. Client A using Async because i see that the structure of transaction is not irregullar. Client B using Sync becuse i see that the structure of transaction is regullar.</p></blockquote><p>I explained the difference between sync/async and serial/sequential/parallel above.</p><p>The communication of <strong>both</strong> A and B is using several TCP connections. However, Client A opens one connection after the other (serial/sequential), while Client B uses several connections in <strong>parallel</strong>.</p><p>The output of the tshark command (see my answer) would be:</p><p>Client A:</p><blockquote><p>64484<br />
64485</p></blockquote><p>Client B:</p><blockquote><p>46923<br />
46913<br />
46912<br />
46913<br />
46923<br />
etc.<br />
</p></blockquote><p>So, to me it looks like Client B uses <strong>parallel</strong> communication, while Client A uses <strong>serial/sequential</strong> communication.</p><p>If you still like the terms sync/async, I would say, that the application on Client B <strong>seems to be working in async mode</strong>, as several requests are being sent, before the answer for other requests has arrived. Client A <strong>seems to be working in sync mode</strong>, as it sends a request, waits for an answer, sends a request, waits for an answer, etc.</p></div><div id="comment-23061-info" class="comment-info"><span class="comment-age">(16 Jul '13, 23:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22993" class="comment-tools"></div><div class="clear"></div><div id="comment-22993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

