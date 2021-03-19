+++
type = "question"
title = "How to Filter by Multiple IP addresses and Generate Throughput Data Over Time"
description = '''Hello, My objective is to generate a script that can output network throughput over time by network stream &quot;Sender IP to Receiver IP&quot;. Currently I can do that for a single sender and a single receiver using the script below. However, I have one more additional use case where I have 5 senders and one...'''
date = "2015-08-12T12:35:00Z"
lastmod = "2015-08-15T03:11:00Z"
weight = 45016
keywords = [ "tshark" ]
aliases = [ "/questions/45016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Filter by Multiple IP addresses and Generate Throughput Data Over Time](/questions/45016/how-to-filter-by-multiple-ip-addresses-and-generate-throughput-data-over-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My objective is to generate a script that can output network throughput over time by network stream "Sender IP to Receiver IP". Currently I can do that for a single sender and a single receiver using the script below. However, I have one more additional use case where I have 5 senders and one receiver and my current script will not work for that. My question is using multiple sender IP's and a single receiver IP is there an easy way to generate throughput data overtime for each stream?</p><p>tshark -r $file -T fields -e frame.time -e frame.len -2 -R "udp"|\ sed -e 's/..<em>\t/\t/' |\ awk -F"\t" '$1==last {sum += $2; next} {printf("%s# %8d bytes/s# %6.2f Mbit/s#\n",last,sum,sum</em>8/1024/1024);last=$1;sum=$2}'</p><p>output : Jul 27, 2015 12:07:42 579387 bytes/s ( 4.42 Mbit/s)</p><p>Jul 27, 2015 12:07:43 597240 bytes/s ( 4.56 Mbit/s)</p><p>Jul 27, 2015 12:07:44 596070 bytes/s ( 4.55 Mbit/s)</p><p>Jul 27, 2015 12:07:45 595728 bytes/s ( 4.55 Mbit/s)</p><p>...</p><p>....</p><p>Thanks,</p><p>Joe</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/17c3f2c7628cf18f00d2d2136dbc3560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danjoemart&#39;s gravatar image" /><p>danjoemart<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danjoemart has no accepted answers">0%</span></p></div></div><div id="comments-container-45016" class="comments-container"></div><div id="comment-tools-45016" class="comment-tools"></div><div class="clear"></div><div id="comment-45016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45136"></span>

<div id="answer-container-45136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45136-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are many ways to do that.</p><p><strong>Option #1:</strong> Use the tshark stats</p><blockquote><p>tshark -nr http.pcap -q -R "udp and host x.x.x.x and host y.y.y.y" -z io,stat,1</p></blockquote><p>Output:</p><pre><code>=============================
| IO Statistics             |
|                           |
| Duration: 2.611393 secs   |
| Interval: 1 secs          |
|                           |
| Col 1: Frames and bytes   |
|---------------------------|
|          |1               |
| Interval | Frames | Bytes |
|---------------------------|
|  0 &lt;&gt; 1  |      2 |  5324 |
|  1 &lt;&gt; 2  |     12 |  6740 |
|  2 &lt;&gt; Dur|      4 |  2212 |
=============================</code></pre><p>Then parse the output with a script to extract the column with the bytes (per second).</p><p>A more complex example, with filters for different sessions.</p><blockquote><p>tshark -nr http.pcap -q -z io,stat,1,"ip.src eq 192.168.90.55 and ip.dst eq 216.34.181.134" ,"ip.addr eq 216.34.181.134"</p></blockquote><pre><code>===============================================================
| IO Statistics                                               |
|                                                             |
| Duration: 2.611393 secs                                     |
| Interval: 1 secs                                            |
|                                                             |
| Col 1: ip.src eq 192.168.90.55 and ip.dst eq 216.34.181.134 |
|     2: ip.addr eq 216.34.181.134                            |
|-------------------------------------------------------------|
|          |1               |2               |                |
| Interval | Frames | Bytes | Frames | Bytes |                |
|--------------------------------------------|                |
|  0 &lt;&gt; 1  |      0 |     0 |      0 |     0 |                |
|  1 &lt;&gt; 2  |      6 |  3516 |      6 |  3516 |                |
|  2 &lt;&gt; Dur|      0 |     0 |      0 |     0 |                |
===============================================================</code></pre><p><strong>Option #2</strong>: use tshark in a more generic way</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -E separator=;</p></blockquote><p>then use a more complex script to extract whatever you need. You can also combine the whole thing with a display filter.</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e frame.time -e frame.len -e ip.src -e ip.dst -E separator=; -Y "ip.src eq x.x.x.x and ip.dst eq z.z.z.z"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '15, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45136" class="comments-container"></div><div id="comment-tools-45136" class="comment-tools"></div><div class="clear"></div><div id="comment-45136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

