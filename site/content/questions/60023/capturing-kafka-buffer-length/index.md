+++
type = "question"
title = "Capturing Kafka buffer length"
description = '''Hi, I wonder what&#x27;s the process of capturing Kafka producer buffer length (whatever is being passed over to socket to the broker as a single chunk).  What I tried is running the following on a machine with Kafka producers: sudo tcpdump -n -s 0 -w kafka.log -i eth0 &#x27;port 9092&#x27;  Then: tshark -V -r kaf...'''
date = "2017-03-13T01:25:00Z"
lastmod = "2017-03-13T09:10:00Z"
weight = 60023
keywords = [ "kafka" ]
aliases = [ "/questions/60023" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Kafka buffer length](/questions/60023/capturing-kafka-buffer-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60023-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wonder what's the process of capturing Kafka producer buffer length (whatever is being passed over to socket to the broker as a single chunk).</p><p>What I tried is running the following on a machine with Kafka producers:</p><pre><code>sudo tcpdump -n -s 0 -w kafka.log -i eth0 &#39;port 9092&#39;</code></pre><p>Then:</p><pre><code>tshark -V -r kafka.log -o &#39;kafka.tcp.port:9092&#39; -d tcp.port==9092,kafka -2 -Tfields -e kafka.bytes_len</code></pre><p>The output looks a bit weird. There are numerous lines with numbers like:</p><pre><code> -1,23,2559,23,2572,23,2351,23,2171,23,4710,23,2335,23,3357,23,2449,23,2454,23,2273,23,2530,23,2417,23,2344,23,2616,23,2499,23,2213,23,2141,23,2575,23,2419,23,2552,23,2532,23,2308,23,2555,23,2247,23,2660,23,3399,23,2451,23,2772,23,2437,23,2631,23,2536,23,2374,23,2397,23,2472,23,2282,23,3334,23,2217,23,2553,23,2301,23,2547,23,2485,23,2654,23283</code></pre><p>Can you confirm whether these number represent real buffer size, or point me to a more correct direction?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">kafka</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/be7a307aae139b8e2b80d91237d20356?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spektom&#39;s gravatar image" /><p>spektom<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spektom has no accepted answers">0%</span></p></div></div><div id="comments-container-60023" class="comments-container"></div><div id="comment-tools-60023" class="comment-tools"></div><div class="clear"></div><div id="comment-60023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60024"></span>

<div id="answer-container-60024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60024-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It would help if you could provide an example pcap file (through cloudshark, dropbox, googledrive or any other filesharing service).</p><p>When looking at the kafka protocol, I suspect there can be multiple values in one kafka PDU and one kafka PDU can span multiple TCP packets. Due to reassembly, Wireshark (and tshark) will gather the whole PDU and then parse it. As there are multiple values in the one PDU, there will also be multiple fields kafka.bytes_len, one for each value.</p><p>What do you mean by "real buffer size"?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-60024" class="comments-container"><span id="60028"></span><div id="comment-60028" class="comment"><div id="post-60028-score" class="comment-score"></div><div class="comment-text"><p>Kafka aggregates data into a buffer (the size is determined by <code>batch.size</code> and <code>linger.ms</code> parameters), then sends it over to a broker. This is what I meant to capture - the buffer size, which is being send to a broker. I've put some sample (1000 packets) here: <a href="https://www.cloudshark.org/captures/e92de4d1daf4">https://www.cloudshark.org/captures/e92de4d1daf4</a></p></div><div id="comment-60028-info" class="comment-info"><span class="comment-age">(13 Mar '17, 05:12)</span> spektom</div></div></div><div id="comment-tools-60024" class="comment-tools"></div><div class="clear"></div><div id="comment-60024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60033"></span>

<div id="answer-container-60033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60033-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The output appears correct:</p><p>If you examine the attached capture with Wireshark, you will note that certain frames contain multiple instances of the field "kafka.bytes_len" with the values as shown in the tshark output (see below).</p><p>I suggest that you look at the wireshark kafka dissection to determine if there exists a field which gives you the information wanted by you ("real buffer size"). (I'm not familiar with the kafka protocol).</p><p>Partial tshark output from your capture file</p><p>Notes: Current version of Wireshark filter name is "kafka.tcp.ports" "-d" option (decode as) is not needed since you are specifying the port in the "-o" option. I added "-e frame number"</p><p>The "kafka.bytes_len" fields are shown only for the frames in which the complete kafka PDU is reassembled. Again, see the Wireshark dissection.</p><pre><code>tshark  -r kafka.log.pcap -o &quot;kafka.tcp.ports:9092&quot;  -2 -Tfields -e frame.number -e kafka.bytes_len
1
2
3
4
5
6
7       -1,23,3937,23,5742,23,4154,23,4320,23,4252,23,4169,23,4962,23,7890,8689
8
9
10      -1,23,6406,2524
11</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '17, 09:17</p></div></div><div id="comments-container-60033" class="comments-container"><span id="60045"></span><div id="comment-60045" class="comment"><div id="post-60045-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I guess the closest I can get is <code>kafka.message_set_size</code></p></div><div id="comment-60045-info" class="comment-info"><span class="comment-age">(13 Mar '17, 22:40)</span> spektom</div></div></div><div id="comment-tools-60033" class="comment-tools"></div><div class="clear"></div><div id="comment-60033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

