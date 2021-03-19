+++
type = "question"
title = "How can I replay a tcp packet captured by wireshark?"
description = '''Hello everyone, I captured a tcp traffic using wireshark and saved the traffic in pcap file.  I did two tests: Test 1: #tcprewrite --infile=capturedtraffic.pcap --outfile=temp.pcap --srcipmap=0.0.0.0/0:192.168.1.15 --enet-smac=00:0c:29:de:78:42 #tcpreplay --intf1=eth0 temp.pcap  Test 2: # tcplivepla...'''
date = "2016-01-05T07:42:00Z"
lastmod = "2016-01-05T15:16:00Z"
weight = 48871
keywords = [ "tcpreplay", "linux", "pcap", "kali", "wireshark" ]
aliases = [ "/questions/48871" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I replay a tcp packet captured by wireshark?](/questions/48871/how-can-i-replay-a-tcp-packet-captured-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48871-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I captured a tcp traffic using wireshark and saved the traffic in pcap file. I did two tests:</p><pre><code>Test 1:
#tcprewrite --infile=capturedtraffic.pcap --outfile=temp.pcap --srcipmap=0.0.0.0/0:192.168.1.15 --enet-smac=00:0c:29:de:78:42
#tcpreplay --intf1=eth0 temp.pcap

Test 2:
# tcpliveplay eth0 capturedtraffic.pcap 192.168.1.13 00:24:21:1e:29:b2 random</code></pre><p>For both tests, the TCP replay didn't work. I'm getting RST. I didn't find also a traffic comming to my TCP server application. Do you have any ideas on how to resolve this problems?</p><p>The captured data:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Original_data_qX8zAh0.png" alt="alt text" /></p><p>The test results:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_error_gj3Rq8k.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcpliveplay_output_1idhCrs.png" alt="alt text" /></p><p>Note that I used Kali Linux. Thanks in advance. Jack</p></div><div id="question-tags" class="tags-container tags">tcpreplay linux pcap kali wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '16, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/66121113957280e290083bbf7e3e3954?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jackABA&#39;s gravatar image" /><p>jackABA<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jackABA has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jan '16, 02:13</p></div></div><div id="comments-container-48871" class="comments-container"><span id="48898"></span><div id="comment-48898" class="comment"><div id="post-48898-score" class="comment-score"></div><div class="comment-text"><p>Seems to me this is a tcpreplay issue not Wireshark. You'll probably find more helpful support on the tcpreplay-users mailing list as suggested by the <a href="http://tcpreplay.appneta.com/wiki/support.html">tcpreplay support page</a>.</p></div><div id="comment-48898-info" class="comment-info"><span class="comment-age">(06 Jan '16, 02:50)</span> grahamb ♦</div></div></div><div id="comment-tools-48871" class="comment-tools"></div><div class="clear"></div><div id="comment-48871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48892"></span>

<div id="answer-container-48892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48892-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcpliveplay description says that it modifies the captured data, while sending them, in such a way that as much as possible of the original packets would be preserved but the tcp session would establish properly, i.e. the SEQ and ACK numbers are not replayed from the stored version but modified to match the initial values of the new session.</p><p>So little can be said until you make clear at what phase the server sends the RST. After receiving SYN? After receiving the first "real" packet after the initial handshake (SYN, SYN+ACK, ACK)?</p><p>Both the original capture (which you are attempting to replay) and the capture of the replay attempt would be the best input data for any further analysis.</p><p>If I've understood you right and the machine which is running the tcpliveplay is getting RST whereas the server has not received even the SYN packet, there is a firewall somewhere on the way between the two machines which prevents the SYN packet from being delivered and itself responds to it with RST.</p><p>Or you may have missed this part of the <a href="http://tcpreplay.appneta.com/wiki/tcpliveplay.html">manual</a>:</p><p>Due to the nature of the replay, you must suppress the kernel RST flags because the replay is injecting packets into the replay station’s NIC. Issue the following:</p><pre><code># sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s &lt;your ip&gt; -d &lt;dst ip&gt; --dport &lt;dst port, example 80 or 23 etc.&gt; -j DROP</code></pre><p>Example of suppress command:</p><pre><code># sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s 10.0.2.15 -d 192.168.1.10 --dport 80 -j DROP</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jan '16, 15:20</p></div></div><div id="comments-container-48892" class="comments-container"><span id="48897"></span><div id="comment-48897" class="comment"><div id="post-48897-score" class="comment-score"></div><div class="comment-text"><p>Thanks for quick replay. we have already used the iptables command. but we have the same issue. we are getting RST. I added some screenshots that describe the issue.</p></div><div id="comment-48897-info" class="comment-info"><span class="comment-age">(06 Jan '16, 02:15)</span> jackABA</div></div><span id="48899"></span><div id="comment-48899" class="comment"><div id="post-48899-score" class="comment-score"></div><div class="comment-text"><p>I agree with @grahamb, but add some more remarks... tcpliveplay says, at the page I've linked in my answer, that the capture to be replayed must contain just a single tcp session.</p><p>The Wireshark packet list you've pasted from the original capture shows two distinct sessions (packets 1-7 and 8-last), each from a different port at client side. It is possible that this confuses tcpliveplay already before it reaches the end of the first session while sending.</p><p>So you have to use Wireshark filters and <code>File -&gt; Save As</code> to extract the individual session(s) into individual pcap file(s), and then replay it (them) individually.</p><p>The capture from the replay shows that tcpliveplay has sent the SYN packet, the intended server (or something else) has responded by a SYN,ACK packet, but tcpliveplay has never sent the ACK to that one itself, which made the server make two retransmit attempts for the SYN, ACK, and only after still getting no response, send the RST.</p></div><div id="comment-48899-info" class="comment-info"><span class="comment-age">(06 Jan '16, 03:15)</span> sindy</div></div></div><div id="comment-tools-48892" class="comment-tools"></div><div class="clear"></div><div id="comment-48892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

